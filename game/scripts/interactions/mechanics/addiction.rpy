label addiction_event(Girl):
    $ Girl.drain_word("asked_to_meet")

    $ Girl.event_happened[1] += 1

    $ Player.add_word(1, 0, "fix")

    if Player.location != "bg_player":
        if Girl.location == Player.location or Girl in Player.Party:
            "Out of the blue, [Girl.name] says she wants to talk to you in your room and drags you over there."

            $ Player.location = "bg_player"
        else:
            call Girls_arrive(Girl)

            if not _return:
                return

            "[Girl.name] hurriedly says she wants to talk to you in your room and drags you over there."

            call set_the_scene(location = "bg_player")
    else:
        if Girl.location == Player.location or Girl in Player.Party:
            "[Girl.name] turns to you with a bit of a dazed look."
        else:
            call Girls_arrive(Girl)

            if not _return:
                return

            "[Girl.name] turns to you with a bit of a dazed look."

    call clear_the_room(Girl)
    $ shift_focus(Girl)

    if Girl.event_happened[1] == 1:
        if Girl == RogueX:
            $ Girl.change_face("bemused")

            ch_r "Hey there [Girl.player_petname]. You seem to be fitting in well. . ."

            if not Girl.permanent_History["kiss"]:
                ch_r "Look, since the other day when I first. . . touched you, "
            else:
                ch_r "Look, since the other day when I first. . . kissed you, "

            ch_r "I've had this kind of. . . buzz. At first I thought it was just from finally being able to touch someone, "

            $ Girl.eyes = "sexy"

            ch_r "But I think maybe. . . could I touch you again?"
        elif Girl == KittyX:
            $ Girl.change_face("bemused", 2)

            ch_k "Oh. . . hey, [Girl.player_petname]. I've been thinking. . ."

            if not Girl.permanent_History["kiss"]:
                ch_k "Look, since a while back when I first. . . touched you, "
            else:
                ch_k "Look, since a while back when I first. . . kissed you, "

            ch_k "I've kinda been thinking. . . feeling a little odd. . ."

            $ Girl.eyes = "side"

            ch_k "Would you mind if I touched you again real quick?"
        elif Girl == EmmaX:
            $ Girl.change_face("bemused")

            ch_e "Oh, hello [Girl.player_petname]. . ."
            ch_e "You've been doing well in your studies, it seems. . ."
            ch_e "Look, since the other day when we first. . . came into contact. . ."

            $ Girl.change_face("sadside", 1, brows = "angry")

            ch_e "I've been. . . struggling with something."
            ch_e "A feeling. . ."

            $ Girl.eyes = "sexy"

            ch_e "I was thinking perhaps that. . . touching you again might help?"
        elif Girl == LauraX:
            $ Girl.change_face("bemused")

            ch_l "Oh, hey, [Girl.player_petname]."
            ch_l "You think maybe I could touch you again?"

            menu:
                extend ""
                "Ok?":
                    ch_l "Cool."
                "Why?":
                    ch_l "Oh. . . no reason."
                    ch_l "I just sort of feel a little jumpy, and wanted to try something."
        elif Girl == JeanX:
            $ Girl.change_face("confused", 1)

            ch_j "Oh. . ."
            ch_j "Hey there. . . [Girl.player_petname]."

            $ Girl.change_face("confused", 2)

            ch_j "I'm just going to touch you for a second."

            $ Girl.change_face("bemused", 1)

            ch_j "Didn't want to freak you out. . ."

            menu:
                extend ""
                "Ok?":
                    call change_Girl_stat(Girl, "love", 3)
                    call change_Girl_stat(Girl, "love", 3)
                    call change_Girl_stat(Girl, "obedience", 3)
                    call change_Girl_stat(Girl, "inhibition", 3)

                    ch_j "Cool."
                "Why?":
                    $ Girl.change_face("angry", 2)

                    ch_j "None of your business!"

                    $ Girl.change_face("bemused", 1, eyes = "side")

                    ch_j "I was just thinking about the last time we touched and. . ."
                    ch_j "I don't know. Whatever."

                    $ Girl.change_face("bemused", 1)
        elif Girl == StormX:
            $ Girl.change_face("sad")

            ch_s "[Girl.player_petname], I was wondering if you could help me with a problem I've been having. . ."

            $ Girl.change_face("sadside")

            ch_s "For a while now, I've been feeling a bit. . ."
            ch_s "uncomfortable."
            ch_s ". . ."

            $ Girl.change_face("sad")

            ch_s "I've been feeling. . . trapped."
            ch_s "-as if the walls are closing in on me."
            ch_s "I believe this started when you first touched me, and it's been building since."
            ch_s "I wanted to see if. . . additional contact might help."
        elif Girl == JubesX:
            $ Girl.change_face("bemused")

            ch_v "Hey, so. . . [Girl.player_petname]. . ."
            ch_v "It didn't take. . ."

            menu:
                extend ""
                "What didn't?":
                    pass
                "So?":
                    pass
                "Ok.":
                    pass

            ch_v "I was able to go out in the sun earlier, but it wore off."
            ch_v "It started to itch, then to burn. . ."
            ch_v "I guess it's only temporary. . ."
            ch_v ". . ."
            ch_v "Do you think I could. . ."
            ch_v "Bite you some more?"

            menu:
                extend ""
                "That's a little extreme.":
                    ch_v "I guess. . ."
                "I'd rather you didn't.":
                    ch_v "I can understand that. . ."
                "No.":
                    ch_v ". . ."
            ch_v "I guess that is a bit much. . ."
    elif Girl.event_happened[1] == 2:
        jump second_addiction_event
    else:
        jump third_addiction_event

    menu:
        extend ""
        "Another kiss?" if Girl.permanent_History["kiss"]:
            if approval_check(Girl, 660, "LI", Alt = [[RogueX,JeanX], 560]):
                call change_Girl_stat(Girl, "lust", 3)
                call change_Girl_stat(Girl, "love", 6)
                $ Girl.change_face("sexy")

                if Girl == RogueX:
                    ch_r "Yeah, sure, pucker up, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "Um, yeah!"
                elif Girl == EmmaX:
                    ch_e "Took the words out of my mouth, [Girl.player_petname]."
                elif Girl == LauraX:
                    ch_l "Sure, I'm in."
                elif Girl == JeanX:
                    ch_j "Sure, whatever."
                elif Girl == StormX:
                    ch_s "Ah, that could work."
                elif Girl == JubesX:
                    ch_v "Well, that's not usually how \"vampire\" works, but we could give it a shot. . ."
                "She leans in for another kiss."

                call before_action(Girl, "kiss")
            else:
                $ Girl.change_face("sad", 2)

                if Girl == RogueX:
                    ch_r "I don't think so, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "Um, no thanks."
                elif Girl == EmmaX:
                    ch_e "I don't think that would be appropriate right now."
                elif Girl == LauraX:
                    ch_l "Um, no thanks."
                elif Girl == JeanX:
                    ch_j "Not really what I was thinking. . ."
                elif Girl == StormX:
                    ch_s "I would rather not."
                elif Girl == JubesX:
                    ch_v "Nah. . ."

                jump addiction_bad_end
        "How about a kiss?" if not Girl.permanent_History["kiss"]:
            if approval_check(Girl, 660, "LI", Alt = [[RogueX,JeanX], 560]):
                call change_Girl_stat(Girl, "lust", 3)
                call change_Girl_stat(Girl, "love", 6)
                $ Girl.change_face("bemused", 1)

                if Girl == RogueX:
                    ch_r "Yeah, sure, let's do that."
                elif Girl == KittyX:
                    ch_k "What? Oh, um, ok. . ."
                elif Girl == EmmaX:
                    ch_e "Oh, well. . . I suppose we could do that. . ."
                elif Girl == LauraX:
                    ch_l "Oh. . . I guess, sure."
                elif Girl == JeanX:
                    ch_j "Sure, whatever."
                elif Girl == StormX:
                    ch_s "A kiss? I suppose it could work."
                elif Girl == JubesX:
                    ch_v "Well, that's not usually how \"vampire\" works, but we could give it a shot. . ."
                "She leans in for a kiss."

                call before_action(Girl, "kiss")
            else:
                $ Girl.change_face("sad", 2)

                if Girl == RogueX:
                    ch_r "I don't think so, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "Um, no thanks."
                elif Girl == EmmaX:
                    ch_e "I don't think that would be appropriate right now."
                elif Girl == LauraX:
                    ch_l "Um, no thanks."
                elif Girl == JeanX:
                    ch_j "Not what I had in mind, no."
                elif Girl == StormX:
                    ch_s "No. . . I doubt that would work."
                elif Girl == JubesX:
                    ch_v "That's not usually how \"vampire\" works. . ."

                jump addiction_bad_end
        "Sure, if it would make you feel better." if Girl != JubesX:
            if approval_check(Girl, 700, "LI", Alt = [[RogueX], 600]):
                call change_Girl_stat(Girl, "lust", 3)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "love", 3)
                call change_Girl_stat(Girl, "love", 4)
                $ Girl.change_face("sexy")

                if Girl == RogueX:
                    ch_r "I've got an idea for that."
                elif Girl == KittyX:
                    ch_k "Good, because I have an idea. . ."
                elif Girl == EmmaX:
                    ch_e "Well, we may as well enjoy the experience. . ."
                elif Girl == LauraX:
                    ch_r "Cool."
                elif Girl == JeanX:
                    ch_j "How about this. . ."
                elif Girl == StormX:
                    ch_s "Perhaps a kiss then. . ."
                "She leans in for a kiss."

                call before_action(Girl, "kiss")
            else:
                call change_Girl_stat(Girl, "lust", 3)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "love", 3)
                call change_Girl_stat(Girl, "love", 4)
                $ Girl.change_face("smile")

                call girl_touches_you (Girl)
        "What, you just want to touch my face? No thanks." if Girl != JubesX:
            if approval_check(Girl, 500, "L", Alt = [[RogueX,JeanX],400]) or Girl.permanent_History["kiss"]:
                call change_Girl_stat(Girl, "love", -3)
                call change_Girl_stat(Girl, "inhibition", 3)
                $ Girl.brows = "confused"
                $ Girl.eyes = "surprised"
                $ Girl.mouth = "sad"

                if Girl == RogueX:
                    ch_r "Well, how 'bout if I gave you a kiss?"
                elif Girl == KittyX:
                    ch_k "Well. . .I could give you a kiss?"
                elif Girl == EmmaX:
                    ch_e "Would you be interested in. . . a kiss?"
                elif Girl == LauraX:
                    ch_l "Then. . . wanna make out a little?"
                elif Girl == JeanX:
                    ch_j "Hmmm. . ."
                    ch_j "Wanna make out then?"
                elif Girl == StormX:
                    ch_s "What if I gave you a kiss?"

                menu:
                    extend ""
                    "Sure, that'll do.":
                        call change_Girl_stat(Girl, "lust", 3)
                        call change_Girl_stat(Girl, "love", 5)
                        $ Girl.change_face("sexy")
                        "She leans in for a kiss."

                        call before_action(Girl, "kiss")
                    "Only if we can make out a bit." if Girl not in (LauraX,JeanX):
                        call change_Girl_stat(Girl, "love", 3)
                        call change_Girl_stat(Girl, "obedience", 5)
                        $ Girl.change_face("sexy")

                        if Girl == RogueX:
                            ch_r "Fine, we can do that."
                        elif Girl == KittyX:
                            ch_k "Sure, that counds good."
                        elif Girl == EmmaX:
                            ch_e "I don't see why not."
                        elif Girl == StormX:
                            ch_s "Oh. I suppose we could. . ."

                            call before_action(Girl, "kiss")
                    "Not good enough.":
                        call change_Girl_stat(Girl, "love", -5)
                        $ Girl.brows = "angry"

                        $ between_event_count = 3
                        call addiction_ultimatum
            else:
                $ Girl.brows = "angry"

                $ between_event_count = 2
                call addiction_ultimatum
        "You could just touch my face or something." if Girl == JubesX:
            if approval_check(Girl, 700, "LI"):
                call change_Girl_stat(Girl, "lust", 3)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "love", 3)
                call change_Girl_stat(Girl, "love", 4)
                $ Girl.change_face("sexy")

                ch_v "Well, we may as well do more than that. . ."
                "She leans in for a kiss."

                call before_action(Girl, "kiss")
            else:
                call change_Girl_stat(Girl, "lust", 3)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "love", 3)
                call change_Girl_stat(Girl, "love", 4)
                $ Girl.change_face("smile")

                ch_v "Worth a shot. . ."

                call girl_touches_you (Girl)
        "You want to drink my blood? No thanks." if Girl == JubesX:
            if approval_check(Girl, 500, "L") or Girl.permanent_History["kiss"]:
                call change_Girl_stat(Girl, "love", -3)
                call change_Girl_stat(Girl, "inhibition", 3)
                $ Girl.brows = "confused"
                $ Girl.eyes = "surprised"
                $ Girl.mouth = "sad"

                ch_v "What if I gave you a kiss?"

                menu:
                    extend ""
                    "Sure, that'll do.":
                        call change_Girl_stat(Girl, "lust", 3)
                        call change_Girl_stat(Girl, "love", 5)
                        $ Girl.change_face("sexy")

                        "She leans in for a kiss."

                        call before_action(Girl, "kiss")
                    "Only if we can make out a bit.":
                        call change_Girl_stat(Girl, "love", 3)
                        call change_Girl_stat(Girl, "obedience", 5)
                        $ Girl.change_face("sexy")

                        ch_v "I think I could manage. . ."

                        call before_action(Girl, "kiss")
                    "Not good enough.":
                        call change_Girl_stat(Girl, "love", -5)
                        $ Girl.brows = "angry"

                        $ between_event_count = 3

                        call addiction_ultimatum
            else:
                $ Girl.brows = "angry"

                $ between_event_count = 2

                call addiction_ultimatum

    jump addiction_good_end

label second_addiction_event:
    $ Girl.change_face("manic")

    if Girl == RogueX:
        ch_r "Ok, so remember the other day, when I wanted to touch you, but you refused?"
    elif Girl == KittyX:
        ch_k "Hey, remember when I wanted to touch you, but you were[Girl.like]\"no_way?\""
    elif Girl == EmmaX:
        ch_e "Do you recall a while back, I wanted to touch you, and you refused me?"
    elif Girl == LauraX:
        ch_l "Hey, Remember the other day when you wouldn't let me touch you?"
    elif Girl == JeanX:
        ch_j "Oh, hey. . ."
        ch_j "Do you remember the other day, when I offered to touch you. . ."
        ch_j "And you were extremely ungrateful about it? . ."
    elif Girl == StormX:
        ch_s "Since the other day, I've been thinking about this. . ."
        ch_s "You remember I asked for your assistance. . ."
    elif Girl == JubesX:
        ch_v "Hey, um, remember how I wanted to drink your blood the other day?"

    menu:
        extend ""
        "Yeah. . .":
            pass
        "How could I forget. . ." if Girl == JubesX:
            pass
        "Not really. . .":
            $ Girl.brows = "angry"
            call change_Girl_stat(Girl, "love", -3)
            call change_Girl_stat(Girl, "obedience", 3)

    if Girl == RogueX:
        ch_r "Well I can't take it anymore, I feel this. . . craving to touch you again and it's driving me nuts."
    elif Girl == KittyX:
        ch_k "Well. . . I just toss and turn all night, I'm really uncomfortable."
    elif Girl == EmmaX:
        ch_e "Well it seems to be getting worse."
        ch_e "I just can't seem to keep my mind off of it."
    elif Girl == LauraX:
        ch_l "I'm really uncomfortable. I really think it would help if I could touch you real quick."
    elif Girl == JeanX:
        ch_j "Well. . ."
        ch_j "I've decided. . . "
        ch_j ". . . in my infinite mercy. . ."
        ch_j ". . . to give you another chance. . ."
        ch_j ". . ."
        ch_j "Look, I've just been feeling on edge lately."
    elif Girl == StormX:
        ch_s "I was left. . . unsatisfied."
        ch_s "I was hoping that perhaps you had changed you mind about helping me. . ."
    elif Girl == JubesX:
        ch_v "Well, I haven't been able to get outside since then, and it's really been bumming me out."

    menu:
        extend ""
        "That's terrible. Have you seen a doctor?":
            call change_Girl_stat(Girl, "love", 5)
            call change_Girl_stat(Girl, "obedience", 3)

            if Girl == RogueX:
                ch_r "That's sweet of you, yes. Doc McCoy said that he couldn't determine a cause. . ."
                ch_r "but I think it has something to do with your touch."
            elif Girl == KittyX:
                ch_k "Aw, that's sweet. Doc McCoy said that he couldn't figure out a cause. . ."
                ch_k "I do think touching you is important, somehow."
            elif Girl == EmmaX:
                ch_e "That's sweet of you to ask, yes. Henry was unable to determine a cause for it. . ."
                ch_e "I believe it has something to do with your touch."
            elif Girl == LauraX:
                ch_l "Oh, yeah. McCoy said he couldn't figure it out. . ."
                ch_l "I think it has something to do with your touch."
            elif Girl == JeanX:
                call change_Girl_stat(Girl, "lust", 3)

                ch_j "I went to see Hank about it, but I think he was getting a little too \"into\" the physical. . ."
                ch_j "Anyway, he seemed to think it had something to do with your touch."
            elif Girl == StormX:
                ch_s "It would not help. . ."
                ch_s "I believe I understand these feelings, they are my own fault. . ."
            elif Girl == JubesX:
                pass
        "Serves you right.":
            $ Girl.brows = "angry"
            $ Girl.mouth = "sad"
            call change_Girl_stat(Girl, "love", -7)
            call change_Girl_stat(Girl, "obedience", 5)

            if Girl == RogueX:
                ch_r "Ass!"
            elif Girl == KittyX:
                ch_k "Jerk!"
            elif Girl == EmmaX:
                ch_e "Bore."
            elif Girl == LauraX:
                ch_l "Jackass."
            elif Girl == JeanX:
                $ Girl.eyes = "side"

                ch_j "Yeah, probably, but whatever."

                $ Girl.change_face("sly")
            elif Girl == StormX:
                ch_s "That is uncalled for!"
            elif Girl == JubesX:
                ch_v "Hey! I never asked to be a vampire!"
        "Are you a pirate?" if Girl == RogueX:
            $ Girl.brows = "confused"
            call change_Girl_stat(Girl, "love", 3)
            call change_Girl_stat(Girl, "obedience", 3)

            ch_r "Arrr. Love a guy with a sense of humor."
        "I have that effect on people." if Girl != RogueX:
            $ Girl.brows = "confused"
            call change_Girl_stat(Girl, "love", 3)
            call change_Girl_stat(Girl, "obedience", 3)

            if Girl == KittyX:
                ch_k "Hehe, um, yeah. . ."
            elif Girl == EmmaX:
                ch_e "I suppose I don't want to know how you know that. . ."
            elif Girl == LauraX:
                ch_l "Seriously?"
                ch_l "Have -you- looked into that?"
            elif Girl == JeanX:
                $ Girl.change_face("surprised")
                call change_Girl_stat(Girl, "love", 3)
                call change_Girl_stat(Girl, "obedience", 2)

                ch_j "Really?"

                $ Girl.change_face("angry", eyes = "side")

                ch_j "Well that'd explain it, I guess. . ."

                $ Girl.change_face("sly")
            elif Girl == StormX:
                ch_s "From what I have heard around campus, that may be true. . ."
                ch_s "Nonetheless, you are uniquely suited to helping me."
    $ Girl.change_face("bemused")

    if Girl == RogueX:
        ch_r "I've just been feeling a bit weird since we last touched, shaky, buzzed. I can't concentrate on anything."
        ch_r ". . .Anyway, I've reconsidered your. . . offer. I'm willing to be a bit . . . flexible here."
    elif Girl == KittyX:
        ch_k "Anyway, it's a real hassle. . . I haven't been able to concentrate well. . ."
        ch_k "I'd really appreciate if you could help me out here. . ."
    elif Girl == EmmaX:
        ch_e "Yes, well, I haven't been able to get my work done lately, I feel very foggy."
        ch_e "I would certainly be willing to offer some sort of. . . compensation. . ."
    elif Girl == LauraX:
        ch_l "Yeah, so I've been off my game, missing a lot of easy hits."
        ch_l "Could you throw me a bone here?"
    elif Girl == JeanX:
        $ Girl.change_face("angry", eyes = "side")

        ch_j "Anyway, I don't like this. . ."
        ch_j "I don't like feeling somehow. . ."
        ch_j "-Less- than -perfect.-"

        $ Girl.change_face("normal", brows = "sad")

        ch_j "I mean, you must be used to it, but try to see it from my perspective!"
        ch_j ". . ."
        ch_j "So what do you say?"
    elif Girl == StormX:
        ch_s "I have been having trouble concentrating in class."
        ch_s "I don't believe this can continue. . ."
    elif Girl == JubesX:
        ch_v "Yeah, I checked with both Doctors McCoy -and- Strange, and neither had many options."
        ch_v "They both agreed that it probably had to do with sucking your blood the other night."
        ch_v "But also that it wouldn't be healthy for me to drain you dry like that. . ."

    $ between_event_count = 2

    call addiction_ultimatum
    jump addiction_good_end

label third_addiction_event:
    $ Girl.event_happened[1] += 1
    $ Girl.change_face("manic", 2)

    if Girl == RogueX:
        ch_r "Ok, I've given you plenty of chances here. . . Plenty."
        ch_r "This is driving me crazy, it's like I have a full body itch that I can't scratch."
    elif Girl == KittyX:
        ch_k "Ok[Girl.like]seriously, this is getting nuts."
        ch_k "I have been SUPER patient so far, and enough is enough."
    elif Girl == EmmaX:
        ch_e "You have to understand, [Girl.player_petname], this is incredibly uncomfortable."
        ch_e "I haven't had a full night's sleep in a while now, it's quite unbearable."
    elif Girl == LauraX:
        $ Girl.change_face("angry", eyes = "manic")

        ch_l "Hey, I don't know what the deal is here, but I don't like it."
        ch_l "Cut me some slack here, or I'll cut it myself."
    elif Girl == JeanX:
        $ Girl.change_face("angry", eyes = "manic")

        ch_j "Now look here, fucko!"
        ch_j "I have had just about enough of your \"not doing what Jean says\" nonsense!"
        ch_j "What is it you want from me?!"
    elif Girl == StormX:
        $ Girl.change_face("angry", eyes = "white")

        ch_s "[Player.name]!"
        ch_s "This has gone on long enough!"

        $ Girl.change_face("angry", eyes = "manic")

        ch_s "I am finding this. . . urge within me intollerable, and we simply must resolve it!"
    elif Girl == JubesX:
        ch_v "I, um, I really can't control this thirst anymore. . ."

    menu:
        extend ""
        "And Dr. McCoy hasn't been able to find a cause?":
            call change_Girl_stat(Girl, "love", 5)
            call change_Girl_stat(Girl, "obedience", 3)

            if Girl == RogueX:
                ch_r "Nothing! He's run all sorts of tests, and nothing's come up!"
                ch_r "It has to be you, something about your touch, your mutant power."
            elif Girl == KittyX:
                ch_k "Nothing! Test after test, and nothing so far!"
                ch_k "It has to be you, something about your touch, your mutant power."
            elif Girl == EmmaX:
                ch_e "No! I am at my whit's end with that man, so many pointless tests."
                ch_e "I know it's something about you, about your touch, your mutant power."
            elif Girl == LauraX:
                ch_l "No! I haven't been poked and prodded so much in years, but nothing so far."
                ch_l "I figure it has to be your powers or something."
            elif Girl == JeanX:
                ch_j "I wish!"

                call change_Girl_stat(Girl, "lust", 3)

                ch_j "I've given him all the used panties he could possibly use, but he's been completely useless!"
                ch_j "It -has- to be your powers or something."
            elif Girl == StormX:
                ch_s "As I said, I know the cause, I do not need his advice."
            elif Girl == JubesX:
                ch_v "Like I said, you seem to be the only option!"
        "Well, I did make some tempting offers. . .":
            $ Girl.brows = "angry"
            $ Girl.mouth = "sad"
            call change_Girl_stat(Girl, "love", -7)
            call change_Girl_stat(Girl, "obedience", 5)

            if Girl == RogueX:
                ch_r "Yeah, very tempting."
            elif Girl == KittyX:
                ch_k "Yeah, um. . . sure."
            elif Girl == EmmaX:
                ch_e "I suppose I may have reconsidered. . ."
            elif Girl == LauraX:
                ch_l "Yeah, I mean now they might be. . ."
            elif Girl == JeanX:
                ch_j "Bull Shit. . ."
                ch_j "You just tried to. . . do things. . ."

                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "obedience", 2)

                ch_j "Still, at this point. . ."
            elif Girl == StormX:
                ch_s "Oh, I remember your \"offers.\""
                ch_s ". . ."

                $ Girl.change_face("sadside", 2)

                ch_s "I have given them a great deal of thought. . ."
            elif Girl == JubesX:
                ch_v "Says you!"

    $ Girl.brows = "angry"
    $ Girl.mouth = "sad"
    $ Girl.blushing = "_blush1"

    if Girl == RogueX:
        ch_r "So. . .I need this to end. I need to figure this out. I'll do anything here."
    elif Girl == KittyX:
        ch_k "So[Girl.like]can we do something here or what?"
    elif Girl == EmmaX:
        ch_e "I may be a bit more. . . flexible in my negotiations. . ."
    elif Girl == LauraX:
        ch_l "I'm open to suggestions here."
    elif Girl == JeanX:
        call change_Girl_stat(Girl, "obedience", 3)
        call change_Girl_stat(Girl, "obedience", 2)

        ch_j "I'm just so tired. . ."
    elif Girl == StormX:
        ch_s "What must it take to bring this to an end?"
    elif Girl == JubesX:
        ch_v "I guess. . ."
        ch_v "I guess I need to just. . . swallow. . ."
        ch_v "my pride. . ."

    $ between_event_count = 2

    call addiction_ultimatum
    jump addiction_good_end

label addiction_ultimatum:
    $ Girl.add_word(1, "ultimatum", "ultimatum")

    $ approval_bonus = int(Girl.addiction/2)

    if Girl.addiction >= 80:
        $ between_event_count += 2
    elif Girl.addiction >= 50:
        $ between_event_count += 1

    if Girl == RogueX:
        if Girl.event_happened[1] == 1:
            ch_r "Fine then, what would work for you?"
        else:
            ch_r "What do I need to do for another touch?"
    elif Girl == KittyX:
        if Girl.event_happened[1] == 1:
            ch_k "So[Girl.Like]what do you want?"
        else:
            ch_k "Ok, so what'll it take to get another hit?"
    elif Girl == EmmaX:
        if Girl.event_happened[1] == 1:
            ch_e "Very well, what is it that you want?"
        else:
            ch_e "What would it take then?"
    elif Girl == LauraX:
        ch_l "Ok, fine, what do you want?"
    elif Girl == JeanX:
        if Girl.event_happened[1] == 1:
            ch_j "What is it that you want?"
        else:
            ch_j "What'll it take?"
    elif Girl == StormX:
        ch_s "So, what is it you ask of me?"
    elif Girl == JubesX:
        ch_v "What do you want here?"

    if "locked" not in Player.traits:
        menu:
            "Do you want to lock the door first?"
            "Yes":
                "You go to lock the door."

                if not approval_check(Girl, 1000):
                    $ Girl.change_face("perplexed")
                    call change_Girl_stat(Girl, "obedience", 2)

                    if Girl == RogueX:
                        ch_r "Um, [Girl.player_petname]?"
                    elif Girl == KittyX:
                        ch_k "Creeper much?"
                    elif Girl == EmmaX:
                        ch_e "Why do I feel you might have ulterior motives here. . ."
                    elif Girl == LauraX:
                        ch_l "Well that's a red flag. . ."
                    elif Girl == JeanX:
                        ch_j "Huh."
                    elif Girl == StormX:
                        call change_Girl_stat(Girl, "love", -1)
                        call change_Girl_stat(Girl, "love", -1)

                        ch_s "I don't know that I'm comfortable with this. . ."
                    elif Girl == JubesX:
                        ch_v "Ooooh, kay?"

                $ Player.traits.append("locked")

                call set_Character_taboos
            "No":
                pass
    while between_event_count:
        $ stored_bonus = approval_bonus

        if not approval_check(Girl, 1200, "LO"):
            $ Girl.forced = 1

            $ multi_action = 0

        menu addiction_ultimatum_menu:
            extend ""

            "Nothing, just touch whatever you like.":
                $ Girl.forced = 0

                if Girl.player_petname in ["master", "sir"]:
                    call change_Girl_stat(Girl, "lust", 3)
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "love", 1)
                    $ Girl.change_face("sexy")

                    if Girl == RogueX:
                        ch_r "Thank you, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "Oh, thank you."
                    elif Girl == EmmaX:
                        ch_e "Oh, appreciated."
                    elif Girl == LauraX:
                        ch_l "Thank you, [Girl.player_petname]."
                    elif Girl == JeanX:
                        call change_Girl_stat(Girl, "love", 3)
                        call change_Girl_stat(Girl, "love", 2)

                        ch_j "Good."
                    elif Girl == StormX:
                        ch_s "Well then. . ."
                    elif Girl == JubesX:
                        ch_v "Then I suppose I choose. . ."

                    "She leans in for a kiss."

                    call before_action(Girl, "kiss")
                elif approval_check(Girl, 650, "LI", Alt = [[RogueX], 600]):
                    call change_Girl_stat(Girl, "lust", 3)
                    call change_Girl_stat(Girl, "love", 5)
                    $ Girl.change_face("sexy")

                    if Girl == RogueX:
                        ch_r "I've got an idea for that."
                    elif Girl == KittyX:
                        ch_k "Oh, cool."
                    elif Girl == EmmaX:
                        ch_e "Thank you, [Girl.player_petname]"
                    elif Girl == LauraX:
                        ch_l "Ok, cool."
                    elif Girl == JeanX:
                        call change_Girl_stat(Girl, "love", 3)
                        call change_Girl_stat(Girl, "love", 2)

                        ch_j "Really?"
                        ch_j "Ok."
                    elif Girl == StormX:
                        ch_s "Well then. . ."
                    elif Girl == JubesX:
                        ch_v "Oh! Then how about I just try a simple touch. . ."

                    "She leans in for a kiss."

                    call before_action(Girl, "kiss")
                else:
                    call change_Girl_stat(Girl, "lust", 3)
                    call change_Girl_stat(Girl, "love", 6)
                    $ Girl.change_face("smile")

                    call girl_touches_you (Girl)

                while Girl.addiction > 20 and round > 10:
                    $ Girl.addiction -= 1

                    $ round -= 1
                    if round == 10:
                        Girl.voice "I suppose we don't have time for any more than that."
            "How about a kiss?":
                if Girl.permanent_History["kiss"] or approval_check(Girl, 600, "LI", Alt = [[RogueX,JeanX], 560]) or Girl.player_petname in ("master", "sir"):
                    $ Girl.forced = 0
                    call change_Girl_stat(Girl, "lust", 3)
                    call change_Girl_stat(Girl, "love", 6)
                    $ Girl.change_face("sexy")

                    if Girl == RogueX:
                        ch_r "That all? Yeah, sure, let's do that."
                    elif Girl == KittyX:
                        ch_k "Oh, um, ok, sure."
                    elif Girl == EmmaX:
                        ch_e "I suppose we could. . ."
                    elif Girl == LauraX:
                        ch_l "Yeah, ok."
                    elif Girl == JeanX:
                        ch_j "Ok, cool."
                    elif Girl == StormX:
                        ch_s "A kiss? I suppose it could work."
                    elif Girl == JubesX:
                        ch_v "You've convinced me. . ."

                    "She leans in for a kiss."

                    call before_action(Girl, "kiss")

                    $ Girl.addiction = 20 if Girl.addiction > 20 else Girl.addiction
                    $ Girl.addiction = 5 if Girl == JubesX else Girl.addiction
                else:
                    if Girl == RogueX:
                        ch_r "That's kinda personal."
                    elif Girl == KittyX:
                        ch_k "I don't know. . ."
                    elif Girl == EmmaX:
                        ch_e "I don't think that would be appropriate. . ."
                    elif Girl == LauraX:
                        ch_l "Eh. . . nah."
                    elif Girl == JeanX:
                        ch_j "Um. . .no?"
                    elif Girl == StormX:
                        ch_s "No. . . I doubt that would work."
                    elif Girl == JubesX:
                        ch_v "I don't like you like that. . ."
            "How about you let me touch you instead?":
                if Girl == RogueX:
                    ch_r "That depends, [Girl.player_petname]. Where were you thinking?"
                elif Girl == KittyX:
                    ch_k "I don't know[Girl.like]what were you thinking, [Girl.player_petname]?"
                elif Girl == EmmaX:
                    ch_e "I'm not sure, [Girl.player_petname]. What did you have in mind?"
                elif Girl == LauraX:
                    ch_l "So, what were you thinking here?"
                elif Girl == JeanX:
                    call change_Girl_stat(Girl, "obedience", 3)

                    ch_j "What, like feel me up?"
                elif Girl == StormX:
                    ch_s "Hmmm. . . I dislike the implications here. . ."
                elif Girl == JubesX:
                    ch_v "Oh, I don't know about that. . ."

                menu:
                    extend ""
                    "How about I give you a full contact back massage?":
                        call Massage_Prep (Girl)

                        "[Girl.name] gets back up."

                        if Girl.addiction >= 50:
                            call girl_touches_you (Girl)
                    "How about you let me touch your breasts?":
                        $ stored_bonus = approval_bonus

                        call top_off (Girl, 2)

                        $ approval_bonus = stored_bonus

                        call start_Action(Girl, "fondle_breasts")

                        if "fondle_breasts" in Girl.recent_history:
                            call change_Girl_stat(Girl, "obedience", 10)
                            call change_Girl_stat(Girl, "inhibition", 10)

                            if Girl == RogueX:
                                ch_r "I hope that was enough."
                            elif Girl == KittyX:
                                ch_k "Was that good enough for you?"
                            elif Girl == EmmaX:
                                ch_e "I imagine that was plenty."
                            elif Girl == LauraX:
                                ch_l "That was enough, right?"
                            elif Girl == JeanX:
                                ch_j "So, that work for you?"
                            elif Girl == StormX:
                                ch_s "Surely that was plenty. . ."
                            elif Girl == JubesX:
                                ch_v "So, fair trade?"
                    "How about you just let me touch your thighs?":
                        $ stored_bonus = approval_bonus

                        call Bottoms_Off (Girl, 2)

                        $ approval_bonus = stored_bonus

                        if Girl.legs_covered:
                            if Girl == RogueX:
                                ch_r "Ok, but after we do this, I get a little touch too."
                            elif Girl == KittyX:
                                ch_k "Sure, but after this, I'll still need to touch you."
                            elif Girl == EmmaX:
                                ch_e "Fine, but I will still need some other contact."
                            elif Girl == LauraX:
                                ch_l "Yeah, but, I'll need to touch you after this."
                            elif Girl == JeanX:
                                ch_j "Ok, but, You've gotta let me touch you after. . ."
                            elif Girl == StormX:
                                ch_s "So long as you provide me what I need as well."
                            elif Girl == JubesX:
                                ch_v "Ok, we'll see. . ."

                        call start_Action(Girl, "fondle_thighs")

                        if "fondle_thighs" in Girl.recent_history:
                            call change_Girl_stat(Girl, "obedience", 5)
                            call change_Girl_stat(Girl, "inhibition", 5)

                            if Girl == RogueX:
                                ch_r "I hope that was enough."
                            elif Girl == KittyX:
                                ch_k "Was that good enough for you?"
                            elif Girl == EmmaX:
                                ch_e "I imagine that was plenty."
                            elif Girl == LauraX:
                                ch_l "That was enough, right?"
                            elif Girl == JeanX:
                                ch_j "So, that work for you?"
                            elif Girl == StormX:
                                ch_s "I assume that was plenty?"
                            elif Girl == JubesX:
                                ch_v "So, fair trade?"

                            if Girl.legs_covered:
                                call girl_touches_you (Girl)
                    "How about you let me touch your pussy?":
                        $ stored_bonus = approval_bonus

                        call Bottoms_Off (Girl, 0)

                        $ approval_bonus = stored_bonus

                        call start_Action(Girl, "fondle_pussy")

                        if "fondle_pussy" in Girl.recent_history:
                            call change_Girl_stat(Girl, "obedience", 10)
                            call change_Girl_stat(Girl, "obedience", 5)
                            call change_Girl_stat(Girl, "inhibition", 10)
                            call change_Girl_stat(Girl, "inhibition", 5)

                            if Girl == RogueX:
                                ch_r "I hope that was enough."
                            elif Girl == KittyX:
                                ch_k "Was that good enough for you?"
                            elif Girl == EmmaX:
                                ch_e "I imagine that was plenty."
                            elif Girl == LauraX:
                                ch_l "That was enough, right?"
                            elif Girl == JeanX:
                                ch_j "So, that work for you?"
                            elif Girl == StormX:
                                ch_s "That must have been more than enough."
                            elif Girl == JubesX:
                                ch_v "That was plenty, right?"
                    "Never mind, something else":
                        jump addiction_ultimatum_menu
            "You could touch me.":
                menu:
                    "How about you give me a handjob?":
                        call start_Action(Girl, "handjob")
                    "How about you titfuck me?":
                        call start_Action(Girl, "titjob")
                    "How about you blow me?":
                        call start_Action(Girl, "blowjob")
                    "Never mind, something else":
                        jump addiction_ultimatum_menu

                if "angry" not in Girl.recent_history:
                    if "blowjob" in Girl.recent_history or "handjob" in Girl.recent_history or "titjob" in Girl.recent_history:
                        call change_Girl_stat(Girl, "obedience", 10)
                        call change_Girl_stat(Girl, "obedience", 5)
                        call change_Girl_stat(Girl, "inhibition", 10)
                        call change_Girl_stat(Girl, "inhibition", 5)

                        if Girl == RogueX:
                            ch_r "I hope that was enough."
                        elif Girl == KittyX:
                            ch_k "Was that good enough for you?"
                        elif Girl == EmmaX:
                            ch_e "I imagine that was plenty."
                        elif Girl == LauraX:
                            ch_l "That was enough, right?"
                        elif Girl == JeanX:
                            ch_j "So, that work for you?"
                        elif Girl == StormX:
                            ch_s "I can't imagine you would expect more."
                        elif Girl == JubesX:
                            ch_v "That had to be plenty."
            "How about you strip for me, and then I let you touch me?":
                $ stored_bonus = Girl.check_clothing()

                call Group_Strip(Girl)

                menu:
                    "Ok, that was enough, you can touch me now.":
                        call girl_touches_you (Girl)

                        call change_Girl_stat(Girl, "obedience", 10)
                        call change_Girl_stat(Girl, "inhibition", 10)
                    "That was pretty weak, I'll need a bit more.":
                        $ Girl.change_face("angry")

                        if stored_bonus > Girl.check_clothing() and Girl.check_clothing() < 3:
                            call change_Girl_stat(Girl, "love", -40)
                            call change_Girl_stat(Girl, "inhibition", 5)
                            call change_Girl_stat(Girl, "obedience", 20)

                            if Girl == RogueX:
                                ch_r "You're reneging after I went this far?!"
                            elif Girl == KittyX:
                                ch_k "Hey! I. . . took off some stuff."
                            elif Girl == EmmaX:
                                ch_e "I've made far more off far less. . ."
                            elif Girl == LauraX:
                                ch_l "Hey, you get what you get."
                            elif Girl == JeanX:
                                ch_j "Bull Shit, that was some Grade A flesh."
                            elif Girl == StormX:
                                ch_s "I can't imagine you expected more."
                            elif Girl == JubesX:
                                ch_v "What else did you expect?!"

                            jump addiction_bad_end
                        else:
                            if Girl == RogueX:
                                ch_r "Seriously? What will this take?"
                            elif Girl == KittyX:
                                ch_k "That wasn't enough?!"
                            elif Girl == EmmaX:
                                ch_e "I think that was -more- than sufficient."
                            elif Girl == LauraX:
                                ch_l "Not cool."
                            elif Girl == JeanX:
                                ch_j "Well. . . that's all you get for now!"
                            elif Girl == StormX:
                                ch_s "Well. . . that's unfortunate."
                            elif Girl == JubesX:
                                ch_v "Cheh."
            "I have some ideas. . ." if Girl.event_happened[1] >= 10:
                call enter_main_sex_menu(Girl)
            "Have you considered a . . . chemical solution?" if Girl.event_happened[1] >= 10 and Player.semen and not Girl.had_chat[2]:
                call addiction_serum
            "Would you like some \"serum?\"" if Girl.event_happened[1] >= 10 and Player.semen and Girl.had_chat[2]:
                call addiction_serum
            "Nope, you're on your own." if menu_context != "sunshock":
                if Girl.event_happened[1] >= 10:
                    call addiction_fix_beg
                elif Girl.addiction >= 70:
                    $ Girl.change_face("angry", 2)
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "obedience", 3)

                    if Girl == RogueX:
                        ch_r "I ain't tak'in \"no\" for an answer here, figure it out."
                    elif Girl == KittyX:
                        ch_k "Uhuh, we're figuring this one out."
                    elif Girl == EmmaX:
                        ch_e "I'm afraid that you'll need a better answer than that."
                    elif Girl == LauraX:
                        ch_l "Nooope."
                    elif Girl == JeanX:
                        call change_Girl_stat(Girl, "obedience", 3)

                        ch_j "The last person that told me \"no\" doesn't remember his own grandparents!"
                    elif Girl == StormX:
                        ch_s ". . ."
                        ch_s "Unfortunate."
                    elif Girl == JubesX:
                        ch_v "I definitely -want- to leave you alive here. . ."

                    $ between_event_count = 0
                else:
                    $ Girl.change_face("angry", 2)
                    call change_Girl_stat(Girl, "love", -30)
                    call change_Girl_stat(Girl, "obedience", 5)

                    if Girl == RogueX:
                        ch_r "Well then!"
                    elif Girl == KittyX:
                        ch_k "Jerk!"
                    elif Girl == EmmaX:
                        ch_e "Well then!"
                    elif Girl == LauraX:
                        ch_l "Hmmph!"
                    elif Girl == JeanX:
                        $ JeanX.eyes = "psychic"

                        ch_j "Rah!"

                        $ JeanX.eyes = "normal"
                    elif Girl == StormX:
                        $ StormX.eyes = "white"

                        ch_s ". . ."

                        $ StormX.eyes = "squint"
                    elif Girl == JubesX:
                        ch_v "Sleep-"
                        ch_v "-Tight."

                    "[Girl.name] gives one last look over her shoulder before slamming the door and storming out."

                    call remove_Girl(Girl)

                    jump addiction_bad_end
            "Oh, never mind." if menu_context == "sunshock":
                call change_Girl_stat(JubesX, "love", -2)
                call change_Girl_stat(JubesX, "love", -2)
                call change_Girl_stat(JubesX, "obedience", 1)
                call change_Girl_stat(JubesX, "obedience", 2)
                $ JubesX.change_face("angry", 1)

        if "angry" in Girl.recent_history:
            if Girl.addiction >= 80:
                if Girl == RogueX:
                    ch_r "If I wasn't feeling so buzzed right now. . ."
                elif Girl == KittyX:
                    ch_k "If I could keep my balance well enough to punch you. . ."
                elif Girl == EmmaX:
                    ch_e "If my head wasn't buzzing like a million bees. . ."
                elif Girl == LauraX:
                    ch_l "You're lucky I can barely see straight. . ."
                elif Girl == JeanX:
                    ch_j "I have such a migraine right now. . ."
                elif Girl == StormX:
                    ch_s ". . ."
                elif Girl == JubesX:
                    ch_v "Grrrrr. . ."
            else:
                if Girl == RogueX:
                    ch_r "This is just not worth it. I'm out of here."
                elif Girl == KittyX:
                    ch_k "Nope, this is too much, I'm outtie."
                elif Girl == EmmaX:
                    ch_e "I'm afraid you overplayed your hand here, [Girl.player_petname]."
                elif Girl == LauraX:
                    ch_l "Nah, you pushed it too far there, [Girl.player_petname]."
                elif Girl == JeanX:
                    ch_j "Fuck all of this!"
                    ch_j "All the fucks!"
                elif Girl == StormX:
                    ch_s ". . ."
                elif Girl == JubesX:
                    ch_v "The nerve!"
                jump addiction_bad_end

        if Girl.addiction <= 20:
            return

        $ approval_bonus = stored_bonus

        if not Girl.remaining_Actions:
            if between_event_count:
                if Girl == RogueX:
                    ch_r "[[pant, pant] Get to the point already, [Player.name]. . ."
                    ch_r "[[pant, pant] I can't keep this up all day."
                elif Girl == KittyX:
                    ch_k "[[pant, pant] Wrap it up, [Player.name]. . ."
                    ch_k "[[pant, pant] I'm worn out. . ."
                elif Girl == EmmaX:
                    ch_e "[[pant, pant] Could we wrap this up, [Player.name]. . ."
                    ch_e "[[pant, pant] I really do have plans later."
                elif Girl == LauraX:
                    ch_l "Hey, um, get to the point already, [Player.name]. . ."
                    ch_l "I've got things to do. . ."
                elif Girl == JeanX:
                    ch_j "[[pant, pant] Hey, um, [Player.name]. . ."
                    ch_j "[[pant, pant] I'd like to sort this out soonish. . ."
                elif Girl == StormX:
                    ch_s "[[pant, pant] I am unable to continue this all day. . ."
                elif Girl == JubesX:
                    ch_v "[[pant, pant] I'm a little worn out. . ."

                $ Girl.remaining_Actions = 1
            else:
                if Girl == RogueX:
                    ch_r "[[pant, pant] Ok, that's about all I can manage. . ."
                elif Girl == KittyX:
                    ch_k "[[pant, pant] Whew, enough, enough. . ."
                elif Girl == EmmaX:
                    ch_e "[[pant, pant] I think we'll have to call it a day there. . ."
                elif Girl == LauraX:
                    ch_l "Ok, I've got things to do, so. . ."
                elif Girl == JeanX:
                    ch_j "[[pant, pant] Ok. . . that'll do for now. . ."
                elif Girl == StormX:
                    ch_s "[[pant, pant] I cannot continue. . ."
                elif Girl == JubesX:
                    ch_v "[[pant, pant] I really can't. . ."

                jump addiction_bad_end
        if not between_event_count and approval_check(Girl, 1200, "LO"):
            $ between_event_count += 1

        if between_event_count:
            if Girl == RogueX:
                ch_r "I'll still need a bit more than that. . ."
            elif Girl == KittyX:
                ch_k "I'm still feeling off. . ."
            elif Girl == EmmaX:
                ch_e "That's not quite enough yet. . ."
            elif Girl == LauraX:
                ch_l "I'm still not feeling right. . ."
            elif Girl == JeanX:
                ch_j "That. . . still isn't enough. . ."
            elif Girl == StormX:
                ch_s ". . . that wasn't quite enough. . ."
            elif Girl == JubesX:
                ch_v "That. . . doesn't feel like enough. . ."
        elif Girl.addiction >= 80:
            if between_event_count > 3:
                if Girl == RogueX:
                    ch_r "I'd- I don't want to do that. . ."
                elif Girl == KittyX:
                    ch_k "That's not really something I'd enjoy. . ."
                elif Girl == EmmaX:
                    ch_e "You'd push things that far. . ."
                elif Girl == LauraX:
                    ch_l "Come on, not cool. . ."
                elif Girl == JeanX:
                    ch_j "You are really pushing your luck here. . ."
                elif Girl == StormX:
                    ch_s "Surely we could do something else. . ."
                elif Girl == JubesX:
                    ch_v "Couldn't we do something else? . ."
                    $ approval_bonus -= 3

                $ approval_bonus += 5
            elif between_event_count > 2:
                if Girl == RogueX:
                    ch_r "But. . . I just can't. . ."
                elif Girl == KittyX:
                    ch_k "But. . . come on. . ."
                elif Girl == EmmaX:
                    ch_e "Surely there must be something we can agree to. . ."
                elif Girl == LauraX:
                    ch_l "Seriously,[Girl.player_petname]. . ."
                elif Girl == JeanX:
                    ch_j "But. . ."
                    ch_j "Seriously?!"
                elif Girl == StormX:
                    ch_s "Are you serious?"
                    $ approval_bonus -= 5
                elif Girl == JubesX:
                    ch_v "What else you got?"

                $ approval_bonus += 10
            elif between_event_count > 1:
                if Girl == RogueX:
                    ch_r "PLEASE, I'm begging you here, be reasonable!"
                elif Girl == KittyX:
                    ch_k "Come on! I'm begging you here. . ."
                elif Girl == EmmaX:
                    ch_e "Leave me with a little dignity here. . ."
                elif Girl == LauraX:
                    ch_l "You've got to. . . please?"
                elif Girl == JeanX:
                    ch_j "I. . ."
                    ch_j "You. . ."
                    ch_j ". . ."
                    ch_j "Please. . ."
                elif Girl == StormX:
                    ch_s "Could you be more reasonable?"
                    $ approval_bonus -= 10
                elif Girl == JubesX:
                    ch_v "Give me some options here. . ."

                $ approval_bonus += 20
        else:
            if between_event_count > 2:
                if Girl == RogueX:
                    ch_r "Try something else, I'm not into that."
                elif Girl == KittyX:
                    ch_k "Isn't there anything I can do here?"
                elif Girl == EmmaX:
                    ch_e "You must be joking, we can come to an arrangement."
                elif Girl == LauraX:
                    ch_l "Nah, be serious."
                elif Girl == JeanX:
                    ch_j "Yeah, no way."
                elif Girl == JubesX:
                    ch_v "Definitely not. . ."
            elif between_event_count > 1:
                if Girl == RogueX:
                    ch_r "Come on, isn't there anything I can do here?"
                elif Girl == KittyX:
                    ch_k "Gimme a break here."
                elif Girl == EmmaX:
                    ch_e "There must be something you'd want. . ."
                elif Girl == LauraX:
                    ch_l "Come on, let's do this."
                elif Girl == JeanX:
                    ch_j "Get serious here, [Girl.player_petname]."
                elif Girl == StormX:
                    ch_s ". . . I cannot."
                    $ approval_bonus -= 5
                elif Girl == JubesX:
                    ch_v "I. . . can't. . ."

                $ approval_bonus += 10

        $ between_event_count -= 1 if between_event_count > 0 else 0
        $ round -= 10 if round >= 21 else round - 10

    if Girl.addiction >= 80:
        $ Girl.change_face("angry")

        "[Girl.name] trembles with rage."

        call change_Girl_stat(Girl, "love", -30)
        call change_Girl_stat(Girl, "inhibition", 40)

        if Girl == RogueX:
            ch_r "Well then!"
            ch_r "No way, no how. I'm going to get this taken care of, NOW!"
        elif Girl == KittyX:
            ch_k "Jerk!"
            ch_k "We are settling this now."
        elif Girl == EmmaX:
            ch_e "Well then!"
            ch_e "Sometimes you have to do it yourself. . ."
        elif Girl == LauraX:
            ch_l "Hmmph!"
        elif Girl == JeanX:
            $ JeanX.eyes = "psychic"
            call change_Girl_stat(Girl, "obedience", 10)
            ch_j "Raaaaaaahhhh!"
        elif Girl == StormX:
            $ StormX.eyes = "white"
            ch_s ". . ."
            "You hear thunder outside. . ."
        elif Girl == JubesX:
            ch_v "Oh, suck you!"

            $ Girl.change_face("angry", mouth = "open")

            call punch

            "She opens her jaws and lunges for your throat, but stops herself at the last second."

            $ Girl.change_face("angry", eyes = "side")

            "She shakes it off and approaches more calmly."

            $ Girl.change_face("angry")

            "-barely."

        call girl_touches_you (Girl, 1)

        $ Girl.addiction_rate += 2
        $ Girl.resistance = 1 if Girl.resistance < 1 else Girl.resistance
        $ Girl.event_happened[1] = 10

        jump addiction_bad_end

    $ Girl.change_face("sad")

    if Girl == RogueX:
        ch_r "Sorry [Girl.player_petname], you've run out of chances. I'm out of here."
    elif Girl == KittyX:
        ch_k "Well, I guess I should get going then. . ."
    elif Girl == EmmaX:
        ch_e "Well, I'm afraid we're out of time to mess around, I should be going."
    elif Girl == LauraX:
        ch_l "Ok, fine, I gotta get going anyway. . ."
    elif Girl == JeanX:
        ch_j "Well. . . fine. Whatever. I'm going. . ."
    elif Girl == StormX:
        ch_s ". . . Very well. You've made yourself clear."
    elif Girl == JubesX:
        ch_v "If you're just going to screw around, I'm out of here. . ."

    jump addiction_bad_end

label addiction_good_end:
    $ Girl.daily_history.append("fixed")
    $ Girl.event_happened[1] = 10
    $ Girl.change_face("surprised")

    if Girl == RogueX:
        ch_r "Wow. I feel a lot better now, a lot more centered. I think I really am addicted to you here."
    elif Girl == KittyX:
        ch_k "Whoa. That felt great. I think maybe a little -too- great. . ."
    elif Girl == EmmaX:
        ch_e "Amazing. That really did shake out the cobwebs. . . I think this may become an issue."
    elif Girl == LauraX:
        ch_l "Huh. That did the trick. Thanks."
    elif Girl == JeanX:
        ch_j "Wow!"

        call change_Girl_stat(Girl, "love", 3)
        call change_Girl_stat(Girl, "obedience", 2)

        ch_j "I think that really worked. . ."
        ch_j "You've got something there, I might be back for more. . ."
    elif Girl == StormX:
        ch_s "Oh. . . thank you."
        ch_s "I feel. . . much better now."
        ch_s "Yes, that will do nicely."
    elif Girl == JubesX:
        ch_v "Huh. . . I do feel better."
        ch_v "Maybe that's all it took!"
        ch_v "Well that's certainly easier than drinking blood. . ."

    if "swallowed" in Girl.recent_history:
        $ Girl.change_face("bemused", 1)

        if Girl == RogueX:
            ch_r "Hmm, there might be something to your. . . fluids too. They felt so warm. . ."
        elif Girl == KittyX:
            $ Girl.blushing = "_blush2"

            ch_k "And you, um. . . tasted really good too. . "
        elif Girl == EmmaX:
            ch_e "I suspect there's something to your. . . fluids as well. . ."
        elif Girl == LauraX:
            ch_l "You tasted pretty good too, real. . . warm? . ."
        elif Girl == JeanX:
            ch_j "And did you know. . ."

            call change_Girl_stat(Girl, "love", 3)
            call change_Girl_stat(Girl, "obedience", 2)

            ch_j "I think your jizz might be magic or something."
        elif Girl == StormX:
            ch_s "I must admit, I did not expect your. . . semen to have such an impact."
        elif Girl == JubesX:
            ch_v "Not that, um. . . that other thing wasn't great too. . ."

    $ Girl.change_face("normal", 0)
    $ Girl.mouth = "sad"

    call sex_over

    if Girl not in Player.Phonebook:
        if Girl == RogueX:
            ch_r "I'm going to need to get in touch, you should probably have my number, here you go."
        elif Girl == KittyX:
            ch_k "You should[Girl.like]call me sometime, here's my number."
        elif Girl == EmmaX:
            ch_e "I'm going to need to get in touch, take down my number. . ."
        elif Girl == LauraX:
            ch_l "I'll probably need to get in touch, here's my number."
        elif Girl == JeanX:
            ch_j "We should probably trade numbers."
            ch_j ". . . just in case."
        elif Girl == StormX:
            ch_s "I suppose I should give you my phone number. . ."
        elif Girl == JubesX:
            ch_v "I guess I should give you my number. . ."

        $ Player.Phonebook.append(Girl)
    if Girl == RogueX:
        ch_r "I may need to do this again sometime. . . I'll see ya later."
    elif Girl == KittyX:
        ch_k "We should. . . um, do this again sometimeokbye."
    elif Girl == EmmaX:
        ch_e "We should. . . hook up some time."
    elif Girl == LauraX:
        ch_l "See ya later, we should hook up."
    elif Girl == JeanX:
        ch_j "We should. . . hang out. . ."
    elif Girl == StormX:
        ch_s "We may have to do this more regularly. . ."
    elif Girl == JubesX:
        ch_v "I might, um. . , need to top off."

    $ Girl.resistance = 1

label addiction_bad_end:
    $ Girl.event_happened[3] = 5
    $ Girl.recent_history.append("addiction")
    $ Girl.daily_history.append("addiction")
    $ Girl.drain_word("ultimatum", 0)

    $ approval_bonus = 0

    $ Girl.forced = 0

    $ multi_action = True

    $ Girl.addiction_rate += 2

    call sex_over
    $ checkout()

    $ Girl.arm_pose = 1

    if Girl not in Player.Party:
        if Player.location == Girl.home:
            "You head back to your room."
        elif Player.location == "bg_player" and Girl.location == Player.location:
            "[Girl.name] heads out."

        call remove_Girl(Girl)

    $ renpy.pop_call()
    $ renpy.pop_call()

    return

label addiction_fix_beg:
    $ Girl.change_face("angry")
    $ Girl.forced = 0

    if "beg" in Girl.recent_history:
        call change_Girl_stat(Girl, "love", -10)

    call change_Girl_stat(Girl, "obedience", 2)
    call change_Girl_stat(Girl, "obedience", 1)

    if Girl.player_petname in ("master", "sir"):
        $ Girl.change_face("sad")

        if Girl.addiction <= 80 or "beg" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "If you insist, [Girl.player_petname]."
            elif Girl == KittyX:
                ch_k "Ok, ok, fine. . . [Girl.player_petname]"
            elif Girl == EmmaX:
                ch_e "I suppose I'll have to make do, [Girl.player_petname]."
            elif Girl == LauraX:
                ch_l "Ok, fine, [Girl.player_petname]."
            elif Girl == JeanX:
                ch_j ". . ."
                ch_j "Fine. . ."
            elif Girl == StormX:
                ch_s "So be it."
            elif Girl == JubesX:
                ch_v "Fine. . ."

            "[Girl.name] shrugs dejectedly, and then leaves the room."

            jump addiction_bad_end
        else:
            $ Girl.eyes = "manic"

            "[Girl.name] shivers slightly."

            if Girl == RogueX:
                ch_r "Please, [Girl.player_petname], please reconsider?"
            elif Girl == KittyX:
                ch_k "Please, [Girl.player_petname], I'm losing it. . ."
            elif Girl == EmmaX:
                ch_e ". . ."
                ch_e "Please, [Girl.player_petname]?"
            elif Girl == LauraX:
                ch_l "Come on, [Girl.player_petname]?"
            elif Girl == JeanX:
                ch_j ". . ."

                call change_Girl_stat(Girl, "obedience", 4)

                ch_j ". . .please?"
            elif Girl == StormX:
                ch_s ". . ."
            elif Girl == JubesX:
                ch_v "Please!"
            $ Girl.recent_history.append("beg")
    elif Girl.addiction <= 85:
        if Girl == RogueX:
            ch_r "Well then!"
        elif Girl == KittyX:
            ch_k "Jerk!"
        elif Girl == EmmaX:
            ch_e "Well then!"
        elif Girl == LauraX:
            ch_l "Hmmph!"
        elif Girl == JeanX:
            $ JeanX.eyes = "psychic"

            ch_j "Fuck all of this!"

            $ JeanX.eyes = "normal"
        elif Girl == StormX:
            ch_s ". . ."
        elif Girl == JubesX:
            ch_v "Asshole!"

        "[Girl.name] trembles with rage and walks out."

        jump addiction_bad_end
    else:
        $ Girl.change_face("angry")

        "[Girl.name] trembles with rage."

        call change_Girl_stat(Girl, "love", -10)
        call change_Girl_stat(Girl, "obedience", -5)

        if Girl == RogueX:
            ch_r "You. . ."
            ch_r "I just can't take \"no\" for an answer here."
        elif Girl == KittyX:
            ch_k "!!!"
            ch_k "I just can't even!"
        elif Girl == EmmaX:
            ch_e ". . ."
            ch_e "Fine."
            ch_e "Sometimes you have to do it yourself. . ."
        elif Girl == LauraX:
            ch_l "Grrrrrrrrrrr. . ."
        elif Girl == JeanX:
            $ JeanX.eyes = "psychic"

            ch_j "Raaaaaaahhhh!"
        elif Girl == StormX:
            ch_s ". . ."
        elif Girl == JubesX:
            ch_v "Oh, suck you!"

            $ Girl.change_face("angry", mouth = "open")

            call punch

            "She opens her jaws and lunges for your throat, but stops herself at the last second."

            $ Girl.change_face("angry", eyes = "side")

            "She shakes it off and approaches more calmly."

            $ Girl.change_face("angry")

            "-barely."

        call girl_touches_you (Girl, 1)

        call change_Girl_stat(Girl, "inhibition", 10)
        call change_Girl_stat(Girl, "inhibition", 5)
        $ Girl.addiction_rate += 2

        if Girl.addiction <= 40:
            jump addiction_fix_end
        else:
            "[Girl.name] trembles with rage and walks out."

            jump addiction_bad_end
    return

label addiction_fix(Girl):
    $ Girl.drain_word("asked_to_meet")
    $ Girl = check_girl(Girl)

    call set_the_scene
    $ shift_focus(Girl)

    $ Girl.location = Player.location
    $ Girl.change_Outfit()

    call Girls_arrive(Girl)

    if not _return:
        return

    call clear_the_room(Girl)

    $ Girl.change_face("manic")

    $ taboo = 0

    $ Girl.taboo = 0

    if Player.location != "bg_player" and Player.location != Girl.home:
        if Girl.location == Player.location or Girl in Player.Party:
            "[Girl.name] says she wants to talk to you in your room and drags you over there."
        else:
            "[Girl.name] shows up, says she wants to talk to you in your room and drags you over there."
    else:
        if Girl.location == Player.location or Girl in Player.Party:
            "[Girl.name] turns to you with a hungry look."
        else:
            "[Girl.name] pops into your room in a bit of a tizzy."
    if Girl.event_happened[1] < 11:
        if Girl == RogueX:
            ch_r "Hey, so we figured out what's causing this buzz."
            ch_r "Since I saw you last, it's been easier to deal with, it builds slower, goes away faster."
            ch_r "I can almost handle it now, but not quite, you know?"
        elif Girl == KittyX:
            ch_k "So I got a handle on what's been happening with me."
            ch_k "With you."
            ch_k "With this buzzing. . ."
            ch_k "I think it's a little easier now? Seems to get better more quickly?"
            ch_k "But I could still use a little personal time. . ."
        elif Girl == EmmaX:
            ch_e "You'll be pleased to know that I think I've sorted out our. . . drama."
            ch_e "This whole \"buzzing\" issue."
            ch_e "I think that it's settled into a dull pang, something manageable."
            ch_e "Not that I want to manage it -all- the time. . ."
        elif Girl == LauraX:
            ch_l "Hey, I think I've got that buzzing sorted out."
            ch_l "I don't think it's as strong, I think I can manage it now."
            ch_l "Still, I like how it feels when it's good. . ."
        elif Girl == JeanX:
            ch_j ". . ."
            ch_j "Hey, [Girl.player_petname]. . ."
            ch_j "Remember how when I touched you, it made me feel better?"
            ch_j "Well. . . I want to feel better. . ."
        elif Girl == StormX:
            ch_s "The other day, I think I figured out what I find so. . . compelling."
            ch_s "I think that my connection to the elements is always there. . ."
            ch_s "I can always feel it."
            ch_s "When we touch, however, I lose that connection."
            ch_s "It hurts."
            ch_s ". . ."
            ch_s "But a part of me likes it. . ."
        elif Girl == JubesX:
            ch_v "It worked!"
            ch_v "I've been able to be out all day!"
            ch_v ". . ."
            ch_v ". . . but. . ."
            ch_v "It wore off again."
            ch_v "It only seems to last a little bit each time. . ."

        menu:
            extend ""
            "And still no alternative but touching me?":
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 1)

                if Girl == RogueX:
                    ch_r "Nothing! McCoy's tried everything he can think of."
                elif Girl == KittyX:
                    ch_k "Nothing!"
                elif Girl == EmmaX:
                    ch_e "Unfortunately not. Hank's tried everything."
                elif Girl == LauraX:
                    ch_l "Doesn't look that way."
                elif Girl == JeanX:
                    ch_j "Yeah, I wish, but no."
                elif Girl == StormX:
                    ch_s "Nothing else really provides that sort of. . . thrill."
                elif Girl == JubesX:
                    ch_v "Nope, nothing else seems to work."
            "Well anything I can do to help. . .":
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 1)

                if Girl == RogueX:
                    ch_r "I appreciate that, [Girl.player_petname]."
                elif Girl == KittyX:
                    ch_k "Aw, thanks, [Girl.player_petname]."
                elif Girl == EmmaX:
                    ch_e "I am quite appreciative of that, [Girl.player_petname]."
                elif Girl == LauraX:
                    ch_l "Yeah, thanks, [Girl.player_petname]."
                elif Girl == JeanX:
                    call change_Girl_stat(Girl, "love", 3)
                    call change_Girl_stat(Girl, "obedience", 3)

                    ch_j "Great, so. . ."
                elif Girl == StormX:
                    ch_s "Well, I don't want to be a burden. . ."
                    ch_s "I'm sure we can make this mutually beneficial. . ."
                elif Girl == JubesX:
                    ch_v "I would totally appreciate that."
            "You could always whore yourself out again.":
                $ Girl.change_face("angry", 2)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "obedience", 1)

                if Girl == RogueX:
                    ch_r "Yeah, I'm aware of my options, thanks for pointing that out."
                elif Girl == KittyX:
                    ch_k "Yeah, thanks for that image."
                elif Girl == EmmaX:
                    ch_e ". . ."
                elif Girl == LauraX:
                    ch_l "Not cool."
                elif Girl == JeanX:
                    $ Girl.change_face("bemused", 1)
                    call change_Girl_stat(Girl, "obedience", 1)

                    ch_j "Yeah, but I'd like to avoid that, you know?"
                elif Girl == StormX:
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 2)

                    ch_s "Never that."

                    $ Girl.addiction_rate -= 2

                    jump addiction_bad_end
                elif Girl == JubesX:
                    ch_v "Or I could just rip your throat out. . ."
                    ch_v "Relax."
    else:
        if Girl.player_petname in ("master", "sir"):
            $ Girl.change_face("bemused")

            if Girl == RogueX:
                ch_r "I need another fix, [Girl.player_petname]. What can I do about it?"
            elif Girl == KittyX:
                ch_k "I could use another fix, [Girl.player_petname]. Could you help me?"
            elif Girl == EmmaX:
                ch_e "I could do with a fix, [Girl.player_petname]. Care to help me out?"
            elif Girl == LauraX:
                ch_l "Gimme another fix, [Girl.player_petname]. . . Please?"
            elif Girl == JeanX:
                ch_j "So could I get another fix, [Girl.player_petname]? . ."
            elif Girl == StormX:
                ch_s "Could you touch me again, [Girl.player_petname]?"
            elif Girl == JubesX:
                ch_v "Could you let me touch you again, [Girl.player_petname]?"
        else:
            if Girl == RogueX:
                ch_r "Hey, I think I need another fix, I'm feeling a bit out of it."
            elif Girl == KittyX:
                ch_k "Hey, um, could I get another fix?"
            elif Girl == EmmaX:
                ch_e "[Girl.player_petname]. . . I could do with another fix. . . if you have the time."
            elif Girl == LauraX:
                ch_l "Hey, could I get another fix?"
            elif Girl == JeanX:
                ch_j "Hook me up?"
            elif Girl == StormX:
                ch_s "Could you touch me again?"
            elif Girl == JubesX:
                ch_v "Could I get another hit?"

    $ Girl.blushing = "_blush1"

    $ between_event_count = 2
    $ approval_bonus = 0

    call addiction_ultimatum
    jump addiction_fix_end

label addiction_fix_end:
    $ Girl.change_face("normal", 0)
    $ Girl.mouth = "sad"

    call show_full_body(Girl)

    if Girl == RogueX:
        if Girl.event_happened[1] < 11:
            if "forced tag" in Girl.recent_history:
                ch_r "I got what I needed. I really wish that I could avoid it, but it looks like I'm stuck with you."
                ch_r "Just. . . in future maybe try to be less of a dick about it?"
            elif not Girl.forced:
                ch_r "Thanks. I really appreciate this. I can't really explain it, but if I don't get. . . "
                ch_r "access every now and then, I just feel awful, crawling out of my skin. Being with you, helps calm me down."

                if approval_check(Girl, 750):
                    ch_r "And, you know, we had a lot of fun in the process."
                else:
                    ch_r "And thanks for, you know, not taking advantage of the situation."
            else:
                ch_r "Well, I hope you got what you wanted out of this. I really wish that I could avoid it, but it looks like I'm stuck with you."
                ch_r "Just. . . in future maybe try to be less of a dick about it?"
        else:
            if "forced tag" in Girl.recent_history:
                ch_r "Well, I got what I needed. I guess I'll see you around."
            elif not Girl.forced:
                ch_r "Hmmmm, that was real nice, [Girl.player_petname]."
                ch_r "I'm looking forward more and more to these . . . \"sessions\" of ours."
            else:
                ch_r "Well, looks like we both got what we wanted. I guess I'll see you around."
    elif Girl == KittyX:
        if Girl.event_happened[1] < 11:
            if "forced tag" in Girl.recent_history:
                ch_k "Ok, that should do it. . ."
                ch_k "Could you maybe not force me into that though?"
            elif not Girl.forced:
                ch_k "Thanks for helping me out. It really feels awful when I let it go too long."

                if approval_check(Girl, 850):
                    ch_k "And we got to have some fun with it too. . ."
                else:
                    ch_k "And thanks for[Girl.like]not taking advantage. . . you know?"
            else:
                ch_k "Well, you seemed to have fun. . ."
                ch_k "Maybe. . . could you be less of a jerk about it. . ."
                ch_k "Please?"
        else:
            if "forced tag" in Girl.recent_history:
                ch_k "Ok, that should do it. . . guess I'll see you around."
            elif not Girl.forced:
                ch_k "Mmmmm, that was greeeeat, [Girl.player_petname]."
                ch_k "I hope to see you again real soon. . ."
            else:
                ch_k "Well, you seemed to have fun. . . I'll see you around."
    elif Girl == EmmaX:
        if Girl.event_happened[1] < 11:
            if "forced tag" in Girl.recent_history:
                ch_e "Well. . . I suppose that will satisfy me."
                ch_e "You could perhaps catch more flies with honey, you know. . ."
            elif not Girl.forced:
                ch_e "I appreciate your. . . assistance."
                ch_e "This really is quite inconvenient, but I suppose it could be worse."

                if approval_check(Girl, 800):
                    ch_e "You really aren't the worst company out there. . ."
                else:
                    ch_e "I appreciate your. . . restraint in handling our situation."
            else:
                ch_e "Well. . . you seem to have gotten the best of this arrangement. . ."
                ch_e "You could perhaps catch more flies with honey, you know. . ."
        else:
            if "forced tag" in Girl.recent_history:
                ch_e "Well. . . I suppose that will satisfy me. . . at least for the time being."
            elif not Girl.forced:
                ch_e "Hmmmm, that was quite pleasant, [Girl.player_petname]."
                ch_e "I suppose I am quite anticipating our next rendezvous."
            else:
                ch_e "Well. . . you seem to have gotten the best of this arrangement. . ."
                ch_e "For now, at least. . ."
    elif Girl == LauraX:
        if Girl.event_happened[1] < 11:
            if "forced tag" in Girl.recent_history:
                ch_l "Ok, that should do it."
                ch_l "Maybe don't be such an asshole though."
            elif not Girl.forced:
                ch_l "Mmmm, that's a weight off. . ."
                ch_l "Thanks for helping to sort me out there, [Girl.player_petname]."

                if approval_check(Girl, 750):
                    ch_l "And hey, not a bad way to spend some time, right?"
                else:
                    ch_l "And thanks for not pushing things, eh?"
            else:
                call change_Girl_stat(Girl, "love", -5)

                ch_l "Ok, I guess you got what you wanted. I seem to be stuck with you here."
                ch_l "Maybe don't be such an asshole though."
        else:
            if "forced tag" in Girl.recent_history:
                ch_l "Ok, that should do it. See you later."
            elif not Girl.forced:
                ch_l "Good times, [Girl.player_petname]."
                ch_l "See ya later."
            else:
                call change_Girl_stat(Girl, "love", -5)

                ch_l "Ok, looks like you got what you wanted. Guess I'll see you around."
    elif Girl == JeanX:
        if Girl.event_happened[1] < 11:
            if "forced tag" in Girl.recent_history:
                ch_j "Ok, that's the stuff. . ."
            elif not Girl.forced:
                call change_Girl_stat(Girl, "love", 3)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "obedience", 2)

                ch_j "Ok, that's the stuff. . ."
                ch_j "Thanks, [Girl.player_petname]."
                if approval_check(Girl, 750):
                    ch_j "And it worked out pretty well for you, right?"
                else:
                    ch_j "and at least you didn't go \"full perv\" on me."
            else:
                call change_Girl_stat(Girl, "love", -5)
                call change_Girl_stat(Girl, "obedience", 2)

                ch_j "Well. . ."
                ch_j "That happened. . ."
                ch_j "I guess it was worth it though. . ."
        else:
            if "forced tag" in Girl.recent_history:
                ch_j "Ok, that should do it. See you later."
            elif not Girl.forced:
                ch_j "Ok, thanks, [Girl.player_petname]."
                ch_j "Later."
            else:
                call change_Girl_stat(Girl, "love", -5)
                call change_Girl_stat(Girl, "obedience", 2)

                ch_j "Ok, I guess that'll be all. . ."
    elif Girl == StormX:
        if Girl.event_happened[1] < 11:
            if "forced tag" in Girl.recent_history:
                call change_Girl_stat(Girl, "love", 5)
                call change_Girl_stat(Girl, "obedience", 5)

                ch_s ". . . I'm sorry."
                ch_s "You left me no option. . ."
            elif not Girl.forced:
                ch_s "Thank you for. . . indulging me."
                ch_s "I find these urges. . . inconvenient. . ."

                if approval_check(Girl, 800):
                    ch_s ". . . but there are far worse I could be stuck with. . ."
                else:
                    ch_s "I do appreciate you limiting your excesses."
            else:
                ch_s "Well. . . I hope you are also satisfied. . ."
                ch_s "We do not need to be so antagonistic. . ."
        else:
            if "forced tag" in Girl.recent_history:
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 1)

                ch_s ". . . I am sorry. . ."
            elif not Girl.forced:
                ch_s ". . . I did enjoy that, [Girl.player_petname]."
                ch_s "I shall see you later. . ."
            else:
                ch_s "Well. . . I hope you are also satisfied. . ."
                ch_s "For now, I am as well. . ."
    elif Girl == JubesX:
        if Girl.event_happened[1] < 11:
            if "forced tag" in Girl.recent_history:
                ch_v "Well. . . I'm sorry it came to that. . ."
                ch_v "I hope we can work together better than this. . ."
            elif not Girl.forced:
                ch_v "Thanks. . . "
                ch_v "You really don't miss the sunlight until it's gone, uh?"

                if approval_check(Girl, 750):
                    ch_v "And that wasn't so bad, right?"
                else:
                    ch_v "And thanks for, you know, not taking advantage of the situation."
            else:
                ch_v "I guess this is the cost of being able to go out in the sunlight again. . ."
                ch_v "Could you please be a little less of a dick about it though?"
        else:
            if "forced tag" in Girl.recent_history:
                ch_v "Don't push me to the \"red line\" again. . ."
            elif not Girl.forced:
                ch_v "Hmmmm, that was nice, [Girl.player_petname]."
                ch_v "I'll see you next time I get a tan. . ."
            else:
                ch_v "Ok, I guess we got what we wanted from this. . ."

    if Girl.event_happened[1] < 11:
        $ Girl.event_happened[1] = 11

    $ Girl.event_happened[1] += 1
    $ Girl.daily_history.append("fixed")

    if "forced tag" not in Girl.recent_history:
        menu:
            extend ""
            "Bye":
                pass
            "See you next time. . .":
                if not Girl.forced and approval_check(Girl, 800):
                    $ Girl.change_face("bemused", 1, eyes = "side")

                    if Girl == RogueX:
                        ch_r "Yeah, later."
                    elif Girl == KittyX:
                        ch_k "Ok, cool."
                    elif Girl == EmmaX:
                        ch_e "Perhaps. . ."
                    elif Girl == LauraX:
                        ch_l "Ok."
                    elif Girl == JeanX:
                        ch_j "Yeah?"
                    elif Girl == StormX:
                        ch_s "Until then."
                    elif Girl == JubesX:
                        ch_v "Yeah, sure."
                else:
                    $ Girl.change_face("angry", 1)
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 2)

                    "She scowls"
            "Did you want to stick around?":
                if not Girl.forced and approval_check(Girl, 800, "LI"):
                    $ Girl.change_face("smile", 1)
                    $ Player.Party.append(Girl)

                    if Girl == RogueX:
                        ch_r "Sure, ok."
                    elif Girl == KittyX:
                        ch_k "Ok, cool."
                    elif Girl == EmmaX:
                        ch_e "I suppose I could find the time. . ."
                    elif Girl == LauraX:
                        ch_l "Ok."
                    elif Girl == JeanX:
                        ch_j "Yeah?"
                    elif Girl == StormX:
                        ch_s "I could. . ."
                    elif Girl == JubesX:
                        ch_v "Sure, I guess."
                else:
                    $ Girl.change_face("angry", 1)
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 1)

                    if Girl == RogueX:
                        ch_r "No thanks."
                    elif Girl == KittyX:
                        ch_k "Um. . . no. . ."
                    elif Girl == EmmaX:
                        ch_e "That is not what this is. . ."
                    elif Girl == LauraX:
                        ch_l "Nope."
                    elif Girl == JeanX:
                        ch_j "No?"
                    elif Girl == StormX:
                        ch_s "You do not understand this situation. . ."
                    elif Girl == JubesX:
                        ch_v "I'm so not in the mood. . ."

    jump addiction_bad_end

label addiction_serum:
    if "no_serum" in Girl.recent_history:
        if Girl == RogueX:
            ch_r "No, we tried that and you blew it."
        elif Girl == KittyX:
            ch_k "Nope, try something else."
        elif Girl == EmmaX:
            ch_e "I'm afraid you had your shot with that one."
        elif Girl == LauraX:
            ch_l "Time for plan B, [Girl.player_petname]."
        elif Girl == JeanX:
            ch_j "You blew that one, [Girl.player_petname]."
        elif Girl == StormX:
            ch_s "No, I do not think so."
        elif Girl == JubesX:
            ch_v "No chance."
        return

    $ stored_actions = Girl.remaining_Actions
    $ Girl.remaining_Actions = 0

    if not Girl.had_chat[2]:
        $ Girl.change_face("confused")

        if Girl == RogueX:
            ch_r "What do you mean by that?"
        elif Girl == KittyX:
            ch_k "Chemical what?"
        elif Girl == EmmaX:
            ch_e "Oh? In what way?"
        elif Girl == LauraX:
            ch_l "Huh?"
        elif Girl == JeanX:
            ch_j "What are you talking about now?"
        elif Girl == StormX:
            ch_s "What do you suggest?"
        elif Girl == JubesX:
            ch_v "Yes, blood."
            ch_v "We tried blood."

            $ Girl.change_face("startled")

            ch_v "Is this blood?!"

        menu:
            extend ""
            "I think I could. . . [[trick her]":
                ch_p "I was just thinking, I've been studying hard in class and could maybe whip up a. . .serum, that would reduce the cravings."

                $ Girl.change_face()

                if Girl == RogueX:
                    ch_r "Hmm. . . well if you think you can figure out something that would stop this, I'm game."
                elif Girl == KittyX:
                    ch_k "Huh, really? Didn't take you for a chemistry whiz, but anything's worth a shot."
                elif Girl == EmmaX:
                    ch_e "Consider me a bit skeptical, given your grades, but I'm open to ideas."
                elif Girl == LauraX:
                    ch_l "Huh. . . Ok, I guess it's worth a shot."
                elif Girl == JeanX:
                    ch_j "What?"
                    ch_j "I mean, I guess we could try it. . ."
                elif Girl == StormX:
                    ch_s "Given your grades, I'm not sure I trust you on this. . ."
                elif Girl == JubesX:
                    ch_v "So -not- blood then. . ."
                    ch_v "Well, I guess anything's worth a shot. . ."
            "My jiz.":
                $ Girl.blushing = "_blush1"

                if Girl == RogueX:
                    if Girl.permanent_History["swallowed"]:
                        $ Girl.change_face("bemused")

                        ch_r "Hmm, well it has seemed to work for me in the past. . ."
                    else:
                        $ Girl.change_face("surprised")

                        ch_r "Your what? . . . You want me to drink your jiz?"
                    if approval_check(Girl, 750) and not Girl.forced:
                        $ Girl.change_face("sexy")

                        ch_r "Well if that's the plan, couldn't I just get some from the source?"
                    else:
                        ch_r "Well, I guess if touching you works, this could work too. . ."
                elif Girl == KittyX:
                    if Girl.permanent_History["swallowed"]:
                        $ Girl.change_face("bemused")

                        ch_k "Well. . . It's not like that doesn't work. . ."
                    else:
                        $ Girl.change_face("surprised", 2)

                        ch_k "Your what? . . . You want me to. . ."
                        ch_k ". . . drink your jiz?"
                    if approval_check(Girl, 850) and not Girl.forced:
                        $ Girl.change_face("sexy")

                        ch_k "I mean, I don't -could- drink it from the bottle. . ."
                    else:
                        ch_k "I guess this might be the simplest way. . ."
                elif Girl == EmmaX:
                    if Girl.permanent_History["swallowed"]:
                        $ Girl.change_face("bemused")

                        ch_e "I suppose it does have some. . . restorative properties. . ."
                    else:
                        $ Girl.change_face("surprised")

                        ch_e "Well. . . I suppose it does make a certain amount of sense. . ."
                    if approval_check(Girl, 950) and not Girl.forced:
                        $ Girl.change_face("sexy")

                        ch_e "I might be convinced to drink it from the source, you know. . ."
                    else:
                        ch_e "I have entertained worse offers. . ."
                elif Girl == LauraX:
                    if Girl.permanent_History["swallowed"]:
                        $ Girl.change_face("bemused")

                        ch_l "Yeah, makes sense. . ."
                    else:
                        $ Girl.change_face("surprised")

                        ch_l "Huh? Huh. . . yeah, makes sense."
                    if approval_check(Girl, 850):
                        $ Girl.change_face("sexy")

                        ch_l "Do you want me to just get down there?"
                    else:
                        ch_l "So, we doing this?"
                elif Girl == JeanX:
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 2)

                    if Girl.permanent_History["swallowed"]:
                        $ Girl.change_face("surprised")

                        ch_j "Oh!"

                        $ Girl.change_face("bemused")

                        ch_j "Yeah, that works. . ."
                    else:
                        $ Girl.change_face("surprised")

                        ch_j "Well, I guess maybe if it comes from you. . ."
                    if approval_check(Girl, 850):
                        $ Girl.change_face("sexy")

                        ch_j "Did you want me to just get it from you, or. . ."
                    else:
                        ch_j "So what kinda deal are we talking here?"
                elif Girl == StormX:
                    if Girl.permanent_History["swallowed"]:
                        $ Girl.change_face("bemused")

                        ch_s "It has worked out in the past. . ."
                    else:
                        $ Girl.change_face("surprised")

                        ch_s "Hmmm. . . with the ways your powers function, that may work. . ."
                    if approval_check(Girl, 950):
                        $ Girl.change_face("sexy")

                        ch_s "I wouldn't mind. . . taking some directly. . ."
                    else:
                        ch_s "I could consider it. . ."
                elif Girl == JubesX:
                    if Girl.permanent_History["swallowed"]:
                        $ Girl.change_face("bemused")

                        ch_v "I guess that works too. . ."
                    else:
                        $ Girl.change_face("surprised")

                        ch_v "Your what? . . . Jiz, uh?"
                    if approval_check(Girl, 750) and not Girl.forced:
                        $ Girl.change_face("sexy")

                        ch_v "I could always just suck you dry myself. . ."
                    else:
                        ch_v "Well, it's kinda -like- blood. . ."

                $ approval_bonus += 20

                $ Girl.had_chat[3] = 1
            "Never mind.":
                $ Girl.remaining_Actions = stored_actions

                return

    elif Girl.had_chat[3]:
        $ Girl.change_face("bemused", 1)

        $ approval_bonus += 20

        if Girl == RogueX:
            ch_r "Hmm, it was good last time. . ."

            if approval_check(Girl, 750) and not Girl.forced:
                $ Girl.change_face("sexy")

                ch_r "I'd really rather get it straight off the tap. . ."
            else:
                $ Girl.change_face("sad")
                $ Girl.brows = "normal"

                ch_r "I guess this is as good a \"treatment\" as any."
        elif Girl == KittyX:
            ch_k "Well, it was tasty. . ."

            if approval_check(Girl, 850) and not Girl.forced:
                $ Girl.change_face("sexy")

                ch_k "I take my milk from the bottle. . ."
            else:
                $ Girl.change_face("sad")
                $ Girl.brows = "normal"

                ch_k "This'll work out, I guess."
        elif Girl == EmmaX:
            ch_e "You do possess a unique bouquet. . ."

            if approval_check(Girl, 950) and not Girl.forced:
                $ Girl.change_face("sexy")

                ch_e "I'd rather take my medicine. . . directly."
            else:
                $ Girl.change_face("sad")
                $ Girl.brows = "normal"

                ch_e "I suppose we can make this work."
        elif Girl == LauraX:
            ch_l "Yeah, I mean it was pretty good. . ."

            if approval_check(Girl, 850) and not Girl.forced:
                $ Girl.change_face("sexy")

                ch_l "I'd really rather get it straight off the tap. . ."
            else:
                $ Girl.change_face("sad")
                $ Girl.brows = "normal"

                ch_l "I guess this works."
        elif Girl == JeanX:
            ch_j "Well, it is tasty. . ."

            if approval_check(Girl, 850) and not Girl.forced:
                $ Girl.change_face("sexy")

                ch_j "I could just suck you off or something. . ."
            else:
                $ Girl.change_face("sad")
                $ Girl.brows = "normal"

                ch_j "I guess I don't mind. . ."
        elif Girl == StormX:
            ch_s "I did enjoy it last time. . ."

            if approval_check(Girl, 950) and not Girl.forced:
                $ Girl.change_face("sexy")

                ch_s "We could be more direct about it. . ."
            else:
                $ Girl.change_face("sad")
                $ Girl.brows = "normal"

                ch_s "I suppose I could work with that."
        elif Girl == JubesX:
            ch_v "I guess one smoothie is as good as another. . ."

            if approval_check(Girl, 750) and not Girl.forced:
                $ Girl.change_face("sexy")

                ch_v "I could always just suck you dry myself. . ."
            else:
                $ Girl.change_face("sad")
                $ Girl.brows = "normal"

                ch_v "Sure, why not."
    elif Girl.had_chat[2]:
        ch_p "I was just thinking, I could whip up more of that serum. . ."

        $ Girl.change_face("bemused")

        if Girl == RogueX:
            ch_r "Well, whatever that stuff is, it worked well enough last time. . ."
        elif Girl == KittyX:
            ch_k "Well, it did seem to do the trick. . ."
        elif Girl == EmmaX:
            ch_e "Yes. . . it certain was. . . interesting. . ."
        elif Girl == LauraX:
            ch_l "Yeah, ok. Kinda tasted like jizz though. . ."
        elif Girl == JeanX:
            ch_j "Right, the \"serum\" -wink-."
        elif Girl == StormX:
            ch_s "Oh, very well. It wasn't that bad. . ."
        elif Girl == JubesX:
            ch_v "Yeah, I'm sure you could. . ."

        $ approval_bonus += 10

    $ Count = 3

    while Count and "has serum" not in Girl.recent_history:
        $ line = 0
        $ Count -= 1

        menu:
            "What do you ask for in exchange?"
            "Give it to her":
                $ Girl.forced = 0
                $ Girl.mouth = "smile"
                call change_Girl_stat(Girl, "love", Alt = [[JeanX], 500,3])

                ch_p "No problem."

                $ Girl.recent_history.append("has serum")
            "Well, a handy might do the trick. . .":
                $ Girl.change_face("sexy")

                if approval_check(Girl, 1100) or (approval_check(Girl, 800) and Girl.had_chat[2]):
                    $ Girl.arm_pose = 2

                    if Girl == RogueX:
                        if Girl.had_chat[3]:
                            ch_r "Heh, I guess I could work the pump for a bit."
                        else:
                            ch_r "I guess if that's what you want. . ."
                    elif Girl == KittyX:
                        if Girl.had_chat[3]:
                            ch_k "Oh, we're going \"manual\" then. . ."
                        else:
                            ch_k "Hmm, yeah, cost of doing business. . ."
                    elif Girl == EmmaX:
                        if Girl.had_chat[3]:
                            ch_e "Well, I suppose if you want something done right. . ."
                        else:
                            ch_e "I suppose one good turn deserves another. . ."
                    elif Girl == LauraX:
                        ch_l "Sure, I could lend you a hand. . ."
                    elif Girl == JeanX:
                        call change_Girl_stat(Girl, "obedience", 2)

                        ch_j "Sure, why not. . ."
                    elif Girl == StormX:
                        ch_s "I suppose that I could. . ."
                    elif Girl == JubesX:
                        ch_v "Sure, that's fine. . ."

                    call start_Action(Girl, "handjob")

                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)
                    $ Girl.recent_history.append("has serum")
                else:
                    $ Girl.brows = "confused"

                    if Girl == RogueX:
                        ch_r "Pssht, you wish."
                    elif Girl == KittyX:
                        ch_k "Heh, as if."
                    elif Girl == EmmaX:
                        ch_e "Oh, I'm sure you'd enjoy that."
                    elif Girl == LauraX:
                        ch_l "Heh, yeah right."
                    elif Girl == JeanX:
                        ch_j "Hmm, not interested."
                    elif Girl == StormX:
                        ch_s "You shall have to handle that part yourself."
                    elif Girl == JubesX:
                        ch_v "Um, I'd rather not. . ."
            "How about a blowjob?":
                $ Girl.change_face("sexy")

                if approval_check(Girl, 1300) or (approval_check(Girl, 800) and Girl.had_chat[3]):
                    if Girl == RogueX:
                        if Girl.had_chat[3]:
                            ch_r "Heh, I guess I could get it straight from the source."
                        else:
                            ch_r "I. . . suppose I could. . ."
                    elif Girl == KittyX:
                        if Girl.had_chat[3]:
                            ch_k "Oh, I guess straight off the tap. . ."
                        else:
                            ch_k "Hmm, yeah, cost of doing business. . ."
                    elif Girl == EmmaX:
                        if Girl.had_chat[3]:
                            ch_e "Doesn't hurt to get it from the source. . ."
                        else:
                            ch_e "I suppose one good turn deserves another. . ."
                    elif Girl == LauraX:
                        ch_l "I could give it a taste. . ."
                    elif Girl == JeanX:
                        call change_Girl_stat(Girl, "obedience", 2)

                        ch_j "Sure, why not. . ."
                    elif Girl == StormX:
                        ch_s "If I must. . ."
                    elif Girl == JubesX:
                        ch_v "I guess that wouldn't suck. . ."

                    call start_Action(Girl, "blowjob")

                    $ Girl.recent_history.append("has serum")
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)
                else:
                    $ Girl.brows = "confused"

                    if Girl == RogueX:
                        ch_r "Pssht, you wish."
                    elif Girl == KittyX:
                        ch_k "Heh, as if."
                    elif Girl == EmmaX:
                        ch_e "Oh, I'm sure you'd enjoy that."
                    elif Girl == LauraX:
                        ch_l "Heh, yeah right."
                    elif Girl == JeanX:
                        call change_Girl_stat(Girl, "obedience", 1)

                        ch_j "Hmm. Not interested."
                    elif Girl == StormX:
                        ch_s "I don't think that I will."
                    elif Girl == JubesX:
                        ch_v "Maybe not. . ."
            "Ask for a favor for it.":
                $ Girl.change_face("sexy")

                if Girl == RogueX:
                    ch_r "Oh? What sort of favor were you expecting, [Girl.player_petname]?"
                elif Girl == KittyX:
                    ch_k "Yeah? What'd you want, [Girl.player_petname]?"
                elif Girl == EmmaX:
                    ch_e "What is it you're expecting of me, [Girl.player_petname]?"
                elif Girl == LauraX:
                    ch_l "Ok, what're you thinking, [Girl.player_petname]?"
                elif Girl == JeanX:
                    ch_j "What kinda favor?"
                elif Girl == StormX:
                    ch_s "In what way?"
                elif Girl == JubesX:
                    ch_v "Hm. Like what?"

                $ Girl.remaining_Actions = 1

                call enter_main_sex_menu(Girl)

                if "angry" not in Girl.recent_history:
                    call change_Girl_stat(Girl, "love", 2)

                    if Girl == RogueX:
                        ch_r "I'm glad we could work something out, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "Ok, what next?"
                    elif Girl == EmmaX:
                        ch_e "I suppose that was fair."
                    elif Girl == LauraX:
                        ch_l "Ok, now with that out of the way. . ."
                    elif Girl == JeanX:
                        call change_Girl_stat(Girl, "obedience", 3)
                        call change_Girl_stat(Girl, "obedience", 2)
                        call change_Girl_stat(Girl, "inhibition", 2)

                        ch_j "Ok, we got that out of the way."
                    elif Girl == StormX:
                        ch_s "Now live up to your bargain."
                    elif Girl == JubesX:
                        ch_v "Ok, now your turn. . ."

                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "obedience", 1)
                    call change_Girl_stat(Girl, "inhibition", 2)
                    $ Girl.recent_history.append("has serum")
                else:
                    if Girl == RogueX:
                        ch_r "Well that ain't gonna fly, [Girl.player_petname]."
                    elif Girl == KittyX:
                        ch_k "As if, [Girl.player_petname]."
                    elif Girl == EmmaX:
                        ch_e "You must be joking, [Girl.player_petname]."
                    elif Girl == LauraX:
                        ch_l "Nope."
                    elif Girl == JeanX:
                        ch_j "Nah, not interested."
                    elif Girl == StormX:
                        ch_s "I do not think so."
                    elif Girl == JubesX:
                        ch_v "No thanks. . ."

                    $ Count = 0
            "I'm charging for a sip, $5.":
                $ line = "Five"
            "I'm afraid I'll have to charge, $10.":
                $ line = "Ten"
            "Never mind.":
                if Girl == RogueX:
                    ch_r "Oh, ok. . ."
                elif Girl == KittyX:
                    ch_k "Um, ok. . ."
                elif Girl == EmmaX:
                    ch_e "Ok. . ."
                elif Girl == LauraX:
                    ch_l "Oh, ok. . ."
                elif Girl == JeanX:
                    ch_j "Oooookay?"
                elif Girl == StormX:
                    ch_s "Very well?"
                elif Girl == JubesX:
                    ch_v "Oookay. . ."

                $ Girl.remaining_Actions = stored_actions

                return

        if line == "Five" or line == "Ten":
            $ Girl.change_face("angry")
            $ Girl.mouth = "surprised"

            if Girl == RogueX:
                if Girl.had_chat[3]:
                    ch_r "[line] bucks, just to drink your cum?"
                elif Girl.had_chat[2]:
                    ch_r "[line] bucks, just for this supposed \"serum\"?"
                else:
                    ch_r "[line] bucks, just for that serum?"
            elif Girl == KittyX:
                if Girl.had_chat[3]:
                    ch_k "[line] bucks for a mouthfull of jiz?"
                elif Girl.had_chat[2]:
                    ch_k "[line] bucks, just for this supposed \"serum\"?"
                else:
                    ch_k "[line] bucks, just for that serum?"
            elif Girl == EmmaX:
                if Girl.had_chat[3]:
                    ch_e "[line] dollars? You're charging for warm semen?"
                elif Girl.had_chat[2]:
                    ch_e "[line] bucks, just for this supposed \"serum\"?"
                else:
                    ch_e "[line] bucks, just for that suspect liquid?"
            elif Girl == LauraX:
                if Girl.had_chat[3]:
                    ch_l "[line] bucks for fresh cum?"
                elif Girl.had_chat[2]:
                    ch_l "[line] bucks, just for some \"serum\"?"
                else:
                    ch_l "[line] bucks, just for that stuff?"
            elif Girl == JeanX:
                ch_j "So lemme get this straight."

                call change_Girl_stat(Girl, "obedience", 1)

                if Girl.had_chat[3]:
                    ch_j "[line] bucks for some jiz?"
                elif Girl.had_chat[2]:
                    ch_j "[line] bucks, just for some shady \"serum\"?"
                else:
                    ch_j "[line] bucks, just for that junk?"
            elif Girl == StormX:
                if Girl.had_chat[3]:
                    ch_s "[line] dollars? You're charging for fresh semen?"
                elif Girl.had_chat[2]:
                    ch_s "[line] dollars, for this supposed \"serum\"?"
                else:
                    ch_s "[line] dollars, for that concoction?"
            elif Girl == JubesX:
                if Girl.had_chat[3]:
                    ch_v "[line] bucks? cash for spunk?"
                elif Girl.had_chat[2]:
                    ch_v "[line] bucks, for this \"serum\"?"
                else:
                    ch_v "[line] bucks, for. . . whatever that is?"

            $ Girl.change_face()
            $ Girl.eyes = "side"
            call change_Girl_stat(Girl, "love", 1)
            call change_Girl_stat(Girl, "love", -4)

            Girl.voice ". . ."

            $ Girl.change_face()
            $ Girl.brows = "sad"

            if line == "Ten":
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "love", -10)

            if Girl.had_chat[2] and line == "Ten" and Girl.addiction >= 75:
                if Girl == RogueX:
                    ch_r "Five was bad enough! Fine, here you go, but not a penny more."
                elif Girl == KittyX:
                    ch_k "Five was bad enough! Ok, whatever, here."
                elif Girl == EmmaX:
                    ch_e "Five wasn't enough for you? Fine."
                elif Girl == LauraX:
                    ch_l "You're busting my balls here. Ok, ten, fine."
                elif Girl == JeanX:
                    call change_Girl_stat(Girl, "obedience", 2)

                    ch_j "Seriously? Ten bucks? . . "
                    ch_j "Whatever, take it."
                elif Girl == StormX:
                    ch_s "Do not continue to take advantage of a good deal."
                elif Girl == JubesX:
                    ch_v "This is getting pricey. . ."

                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "inhibition", 2)

                if not approval_check(Girl, 1200, "LI"):
                    $ Girl.forced = 1

                    $ multi_action = 0

                $ Player.cash += 10
                $ Girl.recent_history.append("has serum")
            elif Girl.had_chat[2] and line == "Five":
                if Girl == RogueX:
                    ch_r "Ok, here you go."
                elif Girl == KittyX:
                    ch_k "Ok, fine."
                elif Girl == EmmaX:
                    ch_e "Oh, very well."
                elif Girl == LauraX:
                    ch_l "I guess, here."
                elif Girl == JeanX:
                    call change_Girl_stat(Girl, "obedience", 2)

                    ch_j "Fine, whatever."
                elif Girl == StormX:
                    ch_s "Oh, very well. . ."
                elif Girl == JubesX:
                    ch_v "Hmm, ok. . ."

                call change_Girl_stat(Girl, "obedience", 4)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 4)

                if not approval_check(Girl, 1200, "LI"):
                    $ Girl.forced = 1

                    $ multi_action = 0

                $ Player.cash += 5
                $ Girl.recent_history.append("has serum")
            else:
                if Girl == RogueX:
                    ch_r "No way, I don't even know if this'll work."
                elif Girl == KittyX:
                    ch_k "No way, this might not even work!"
                elif Girl == EmmaX:
                    ch_e "I'm not paying for something so suspicious."
                elif Girl == LauraX:
                    ch_l "No way."
                elif Girl == JeanX:
                    ch_j "Screw it."
                elif Girl == StormX:
                    ch_s "I will not take that chance."
                elif Girl == JubesX:
                    ch_v "Nah. . ."

        if "swallowed" in Girl.recent_history:
            $ Girl.addiction = 20 if Girl.addiction >= 20 else 0

            if Girl == RogueX:
                if Girl.had_chat[3]:
                    ch_r "Well, I think that hit the spot. . ."

                    $ Girl.remaining_Actions = stored_actions

                    return
                else:
                    ch_r "That was. . . good actually, now what about this serum?"
            elif Girl == KittyX:
                if Girl.had_chat[3]:
                    ch_k "Hmm, delicious. . ."

                    $ Girl.remaining_Actions = stored_actions

                    return
                else:
                    ch_k "That was. . . fine, but what about this serum?"
            elif Girl == EmmaX:
                if Girl.had_chat[3]:
                    ch_e "Quite satisfying. . ."

                    $ Girl.remaining_Actions = stored_actions

                    return
                else:
                    ch_e "Now that we've dealt with the payment, what about this \"serum?\""
            elif Girl == LauraX:
                if Girl.had_chat[3]:
                    ch_l "That was good. . ."

                    $ Girl.remaining_Actions = stored_actions

                    return
                else:
                    ch_l "Ok, so you mentioned a \"serum?\""
            elif Girl == JeanX:
                if Girl.had_chat[3]:
                    ch_j "That was actually real tasty. . ."

                    $ Girl.remaining_Actions = stored_actions

                    return
                else:
                    ch_j "Ok, so about that \"serum?\""
            elif Girl == StormX:
                if Girl.had_chat[3]:
                    ch_s "That should take care of it. . ."

                    $ Girl.remaining_Actions = stored_actions

                    return
                else:
                    ch_s "Ok, now about that \"serum?\""
            elif Girl == JubesX:
                if Girl.had_chat[3]:
                    ch_v "Mmmmm. . ."
                    ch_v "Mmmmm!!"

                    $ Girl.remaining_Actions = stored_actions

                    return
                else:
                    ch_v "Mmmmm. . ."
                    ch_v "Um, I mean, what about this serum?"
        elif "handjob" in Girl.recent_history or "blowjob" in Girl.recent_history:
            if Girl == RogueX:
                ch_r "Ok, I think I worked that one off, now how about that serum?"
            elif Girl == KittyX:
                ch_k "Ok, I think I earned it, now what about this serum?"
            elif Girl == EmmaX:
                ch_e "I think that should be sufficient, what about this \"serum?\""
            elif Girl == LauraX:
                ch_l "That worked out, so you mentioned a \"serum?\""
            elif Girl == JeanX:
                ch_j "Ok, let's have that serum."
            elif Girl == StormX:
                ch_s "Satisfied? Now produce this \"serum.\""
            elif Girl == JubesX:
                ch_v "Well? Cough it up."

        if "has serum" in Girl.recent_history:
            $ Count = 0
        elif Count == 1:
            if Girl == RogueX:
                ch_r "I don't have all day, get serious."
            elif Girl == KittyX:
                ch_k "There's gotta be something else you want?"
            elif Girl == EmmaX:
                ch_e "I need you to make a reasonable offer here. . ."
            elif Girl == LauraX:
                ch_l "Hey, get serious here."
            elif Girl == JeanX:
                ch_j "Come on, what do you want?"
            elif Girl == StormX:
                ch_s "Try to be serious here."
            elif Girl == JubesX:
                ch_v "Not happening. . ."
        elif Count:
            if Girl == RogueX:
                ch_r "Come on, what else do you want here?"
            elif Girl == KittyX:
                ch_k "Come on, anything else?"
            elif Girl == EmmaX:
                ch_e "I'm trying to be flexible here. . ."
            elif Girl == LauraX:
                ch_l "Hey, give me a better idea."
            elif Girl == JeanX:
                ch_j "I've gotta have something of interest. . ."
            elif Girl == StormX:
                ch_s "I expect we can come to an agreement here."
            elif Girl == JubesX:
                ch_v "Gimme something to work with here. . ."

    if "has serum" in Girl.recent_history:
        if not Player.semen:
            ch_p "I'm kind of. . . out of stock at the moment, sorry. . ."

            $ Girl.change_face("angry", 1)
            call change_Girl_stat(Girl, "love", -5)
            call change_Girl_stat(Girl, "obedience", -5)
            call change_Girl_stat(Girl, "obedience", 2)
            call change_Girl_stat(Girl, "inhibition", -2)

            if line == "Ten":
                $ Player.cash -= 10
            elif line == "Five":
                $ Player.cash -= 5

            Girl.voice "Grrr. . ."

            $ line = 0

            $ Girl.remaining_Actions = stored_actions

            return

        "You leave the room for a moment. . ."

        $ Player.semen -= 1

        "You hand her a small bottle filled with \"serum.\""
        "She opens the bottle and gives it a little sniff."

        if Girl.had_chat[3]:
            "She glances hesitantly at you, but gulps it down, and wipes her lips."

            call change_Girl_stat(Girl, "inhibition", 2)
        elif Girl.permanent_History["swallowed"] >= 5 or Girl not in (RogueX, KittyX):
            "She looks a bit confused, but then grins, gulps it down, and wipes her lips."

            call change_Girl_stat(Girl, "inhibition", 1)
            call change_Girl_stat(Girl, "inhibition", 2)

            if Girl == RogueX:
                ch_r "That was your jiz, wasn't it. You could have just told me."
                ch_r "I know how well that stuff works."
            elif Girl == KittyX:
                ch_k "Hey, that was just jiz!"
                ch_k "Well, I guess it works."
            elif Girl == EmmaX:
                ch_e "I should have realized that you weren't some chemical genius."
                ch_e "Using your own juices as a cure-all?"
                ch_e "Still, I suppose this is a convenient alternative."
            elif Girl == LauraX:
                ch_l "Oh. That was jiz."
                ch_l "Makes sense."
            elif Girl == JeanX:
                call change_Girl_stat(Girl, "love", 3)
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 3)

                ch_j "Oh, the \"serum\" is jiz."
                ch_j "I am shocked."
                ch_j "Really."
            elif Girl == StormX:
                ch_s "Well. . . it appears that you are playing a trick."
                ch_s "This is semen, is it not? Yours?"
            elif Girl == JubesX:
                ch_v "Oh, you just bottled your jiz."
                ch_v "That makes sense."

            $ Girl.had_chat[3] = 1
        elif Girl.permanent_History["swallowed"] or Girl not in (RogueX, KittyX):
            $ Girl.change_face("surprised")

            if Girl == RogueX:
                ch_r "Hmmm. . . hey, this is your jiz, isn't it?!"
            elif Girl == KittyX:
                ch_k "Hey, that was just jiz!"
            elif Girl == EmmaX:
                ch_e "I should have realized that you weren't some chemical genius."
                ch_e "Using your own juices as a cure-all?"
            elif Girl == LauraX:
                ch_l "Hey, that was just jiz."
            elif Girl == JeanX:
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 3)
                call change_Girl_stat(Girl, "obedience", 2)
                call change_Girl_stat(Girl, "inhibition", 3)

                ch_j "Did you know that this \"serum\" is just jiz?"
            elif Girl == StormX:
                ch_s "Well. . . it appears that you are playing a trick."
                ch_s "This is semen, is it not? Yours?"
            elif Girl == JubesX:
                ch_v "Oh, you just bottled your jiz."
                ch_v "That makes sense."

            menu:
                extend ""
                "Um, yes?":
                    $ Girl.change_face("confused")
                    $ Girl.mouth = "lipbite"
                "Of course not!":
                    $ Girl.change_face("confused")
                    $ Girl.mouth = "smile"

            "She looks sternly at you, but then gulps it down and wipes her lips."

            if Girl == RogueX:
                ch_r "Ugh, I'm still getting used to the taste of that, you should have just told me."
            elif Girl == KittyX:
                ch_k "Ew, gross. . . you could have just told me."
            elif Girl == EmmaX:
                ch_e "Well, it's not like it's the first time I've taken sperm recreationally."
            elif Girl == LauraX:
                ch_l "Well, I guess it works. . ."
            elif Girl == JeanX:
                call change_Girl_stat(Girl, "love", 2)

                ch_j "Whatever."
            elif Girl == StormX:
                ch_s "I suppose so long as it works. . ."
            elif Girl == JubesX:
                ch_v "Oh, it's fine, tastes great, actually."

            $ Girl.had_chat[3] = 1
        else:
            "She then gulps it down and wipes her lips."
            if Girl == RogueX:
                ch_r "Ugh, that stuff goes down hard. . ."
            elif Girl == KittyX:
                ch_k "Ew, this stuff is thick. . ."
            elif Girl == JeanX:
                ch_j "Whew, that's. . . potent."

        $ Girl.eyes = "closed"
        $ Girl.brows = "sad"
        $ Girl.mouth = "smile"

        "[Girl.name] shudders with ecstasy."

        $ Girl.change_face()

        if Girl.had_chat[3]:
            if Girl == RogueX:
                ch_r "Hmm, even knowing what that stuff is, it does seem to work."
            elif Girl == KittyX:
                ch_k "Still kinda weird, but it works."
            elif Girl == EmmaX:
                ch_e "I'm still stunned at how effective that is."
            elif Girl == LauraX:
                ch_l "Ah, that's better."
            elif Girl == JeanX:
                ch_j "I have to say this, your jizz does hit the spot. . ."
            elif Girl == StormX:
                ch_s "You do have a unique flavor. . ."
            elif Girl == JubesX:
                ch_v "That was great, thanks."

            $ Girl.recent_history.append("swallowed")
            $ Girl.daily_history.append("swallowed")
        else:
            if Girl == RogueX:
                ch_r ". . . that does certainly take the edge off. Thank you."
            elif Girl == KittyX:
                ch_k ". . . but it does do the trick. Thanks."
            elif Girl == JeanX:
                ch_j "Whatever that was, it seems to have worked."

        $ Girl.recent_history.remove("has serum")
        $ Girl.recent_history.append("serum")
        $ Girl.daily_history.append("serum")
        $ Girl.addiction = 20 if Girl.addiction >= 20 else 0
        $ Girl.addiction_rate += 2

        if "addictive" in Player.traits:
            $ Girl.addiction_rate += 2

        $ Girl.had_chat[2] += 1
    else:
        if Girl == RogueX:
            ch_r "Too bad we couldn't come to an arrangement here. . ."
        elif Girl == KittyX:
            ch_k "I wish you'd be more flexible. . ."
        elif Girl == EmmaX:
            ch_e "You drive too hard a bargain. . ."
        elif Girl == LauraX:
            ch_l "Well, I guess that's that. . ."
        elif Girl == JeanX:
            ch_j "You don't know how to negotiate as well as I do."
            ch_j "I'm a stable genius."
        elif Girl == StormX:
            ch_s "We should have been able to negotiate here."
        elif Girl == JubesX:
            ch_v "We need to work something out here, right?"

        $ Girl.recent_history.append("no_serum")

    $ Girl.remaining_Actions = stored_actions

    return
