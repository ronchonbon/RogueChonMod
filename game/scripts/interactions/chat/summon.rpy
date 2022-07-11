label summon(Girl):
    $ D20 = renpy.random.randint(1, 20)

    if D20 <= 3:
        $ line = "no"
    elif time_index > 2:
        if approval_check(Girl, 700, "L") or approval_check(Girl, 300, "O"):
            if Girl == RogueX:
                Girl.text "ok, it's getting late but I can hang out for a bit"
            elif Girl == KittyX:
                Girl.text "it's getting kinda late, but we can hang out for a bit"
            elif Girl == EmmaX:
                Girl.text "It's getting late, but fine, what did you want?"
            elif Girl == LauraX:
                Girl.text "You're up too? Sure, we can hang."
            elif Girl == JeanX:
                Girl.text "you're up too? yeah, thats fine"
            elif Girl == StormX:
                Girl.text "You are awake? I can join you."
            elif Girl == JubesX:
                Girl.text "ok!"
            elif Girl == MystiqueX:
                Girl.text "It is late, but very well."

            call add_Girls(Girl)
        else:
            if Girl == RogueX:
                Girl.text "it's a bit late, [Girl.player_petname], maybe tomorrow"
            elif Girl == KittyX:
                Girl.text "it's kinda late? maybe tomorrow"
            elif Girl == EmmaX:
                Girl.text "It's late, [Girl.player_petname], tell me tomorrow."
            elif Girl == LauraX:
                Girl.text "Nah."
            elif Girl == JeanX:
                Girl.text "id rather not. . ."
            elif Girl == StormX:
                Girl.text "It is too late, I need to sleep."
            elif Girl == JubesX:
                Girl.text "im kinda busy, [Girl.player_petname]"
            elif Girl == MystiqueX:
                Girl.text "Not now."

        return
    elif not approval_check(Girl, 700, "L") or not approval_check(Girl, 600, "O"):
        if not approval_check(Girl, 300):
            if Girl == RogueX:
                Girl.text "not really interested, [Girl.player_petname]"
            elif Girl == KittyX:
                Girl.text "im kinda busy, [Girl.player_petname]"
            elif Girl == EmmaX:
                Girl.text "I don't really feel up to that, [Girl.player_petname]."
            elif Girl == LauraX:
                Girl.text "I'm busy, [LauraX.player_petname]."
            elif Girl == JeanX:
                Girl.text "im busy, [Girl.player_petname]"
            elif Girl == StormX:
                Girl.text "I am busy, [Girl.player_petname]."
            elif Girl == JubesX:
                Girl.text "im kinda busy, [Girl.player_petname]"
            elif Girl == MystiqueX:
                Girl.text "I have things to do, [Girl.player_petname]."

            return
        elif Girl.location == "bg_classroom" or Girl.teaching:
            if Girl == RogueX:
                Girl.text "im kinda in class right now, [Girl.player_petname], you could join me"
            elif Girl == KittyX:
                Girl.text "im in class right now, [Girl.player_petname], you up for it?"
            elif Girl == EmmaX:
                Girl.text "You can find me in the classroom, [Girl.player_petname]."
            elif Girl == LauraX:
                Girl.text "I'm in class, did you want to come too?"
            elif Girl == JeanX:
                Girl.text "im in class right now"
            elif Girl == StormX:
                Girl.text "You can find me in the classroom."
            elif Girl == JubesX:
                Girl.text "im in class, did you want to come too?"
        elif Girl.location == "bg_dangerroom":
            if Girl == RogueX:
                Girl.text "im training at the moment, [Girl.player_petname], care to join me?"
            elif Girl == KittyX:
                Girl.text "im in the DR, [Girl.player_petname], want in?"
            elif Girl == EmmaX:
                Girl.text "I'm getting some training in, [Girl.player_petname], care to join me?"
            elif Girl == LauraX:
                Girl.text "I'm in the Danger Room, [LauraX.player_petname], want in?"
            elif Girl == JeanX:
                Girl.text "im in the danger room, [Girl.player_petname]"
            elif Girl == StormX:
                Girl.text "I am in the Danger Room, [Girl.player_petname], care to join me?"
            elif Girl == JubesX:
                Girl.text "im in the Danger Room, [Girl.player_petname], want in?"
            elif Girl == MystiqueX:
                Girl.text "Come join me in the Danger Room, [Girl.player_petname]."
        elif Girl.location == "bg_campus":
            if Girl == RogueX:
                Girl.text "im hanging out on campus, [Girl.player_petname], want to hang with me?"
            elif Girl == KittyX:
                Girl.text "im chillin in the quad, [Girl.player_petname], want to come?"
            elif Girl == EmmaX:
                Girl.text "I'm relaxing in the square, if you'd care to join me."
            elif Girl == LauraX:
                Girl.text "I'm napping under a tree here, want to come?"
            elif Girl == JeanX:
                Girl.text "im relaxing in the quad right now"
            elif Girl == StormX:
                Girl.text "I am relaxing in the courtyard, care to join me?"
            elif Girl == JubesX:
                Girl.text "im just enjoying the sun, want to come?"
            elif Girl == MystiqueX:
                Girl.text "I am outside enjoying the weather."
        elif Girl.location == Girl.home:
            if Girl == RogueX:
                Girl.text "im in my room, [Girl.player_petname], want to swing by?"
            elif Girl == KittyX:
                Girl.text "im in my room, [Girl.player_petname], want to hang?"
            elif Girl == EmmaX:
                Girl.text "I'm in my room, [Girl.player_petname]."
            elif Girl == LauraX:
                Girl.text "I'm in my room, [LauraX.player_petname], want to hang?"
            elif Girl == JeanX:
                Girl.text "im in my room, [Girl.player_petname]"
            elif Girl == StormX:
                Girl.text "I am in my room, [Girl.player_petname], care to join me?"
            elif Girl == JubesX:
                Girl.text "im in my room, [Girl.player_petname], did you wanna drop by?"
            elif Girl == MystiqueX:
                Girl.text "I'm in my room, [Girl.player_petname]."
        elif Girl.location == "bg_player":
            if Girl == RogueX:
                Girl.text "I happen to be in your room, [Girl.player_petname], im waiting for you. . ."
            elif Girl == KittyX:
                Girl.text "im in your room, [Girl.player_petname], come home. . ."
            elif Girl == EmmaX:
                Girl.text "I'm waiting in your room, [Girl.player_petname]. . ."
            elif Girl == LauraX:
                Girl.text "I'm in your room, [LauraX.player_petname], why aren't you?"
            elif Girl == JeanX:
                Girl.text "im in your room, [Girl.player_petname], where are you"
            elif Girl == StormX:
                Girl.text "I am in your room, [Girl.player_petname], coming home soon?"
            elif Girl == JubesX:
                Girl.text "im in your room, [Girl.player_petname], are you coming back?"
            elif Girl == MystiqueX:
                Girl.text "I'm waiting in your room, [Girl.player_petname]. . ."
        elif Girl.location == "bg_shower":
            if approval_check(Girl, 1600):
                if Girl == RogueX:
                    Girl.text "im kinda in the shower right now, [Girl.player_petname], care to join me?"
                elif Girl == KittyX:
                    Girl.text "im in the shower, [Girl.player_petname], want to get wet?"
                elif Girl == EmmaX:
                    Girl.text "I'm in the shower right now, [Girl.player_petname], do you need an invitation?"
                elif Girl == LauraX:
                    Girl.text "I'm in the shower right now. Join me?"
                elif Girl == JeanX:
                    Girl.text "im in the shower rn"
                elif Girl == StormX:
                    Girl.text "I am in the shower right now. Care to join me?"
                elif Girl == JubesX:
                    Girl.text "im in the shower atm. join me?"
                elif Girl == MystiqueX:
                    Girl.text "I'm taking a shower now, if you are interested."
            else:
                if Girl == RogueX:
                    Girl.text "im kinda in the shower right now, [Girl.player_petname], maybe we could touch base later"
                elif Girl == KittyX:
                    Girl.text "im in the shower right now, [Girl.player_petname], ttyl"
                elif Girl == EmmaX:
                    Girl.text "I'm in the shower right now, [Girl.player_petname], perhaps I'll see you later."
                elif Girl == LauraX:
                    Girl.text "I'm in the shower right now, [LauraX.player_petname]. We can connect later."
                elif Girl == JeanX:
                    Girl.text "im in the shower, [Girl.player_petname]"
                    Girl.text "dont come knocking"
                elif Girl == StormX:
                    Girl.text "I am in the shower right now, [Girl.player_petname]. We can connect later."
                elif Girl == JubesX:
                    Girl.text "im in the shower right now, [Girl.player_petname]. we can hang later"
                elif Girl == MystiqueX:
                    Girl.text "I'm in the shower, do not bother me."

                return
        elif Girl.location == "hold":
            if Girl == RogueX:
                Girl.text "im not really around right now, see you later?"
            elif Girl == KittyX:
                Girl.text "im kinda off the grid right now. sorry?"
            elif Girl == EmmaX:
                Girl.text "I'm off campus for a bit, I'll be back later."
            elif Girl == LauraX:
                Girl.text "I'm on task right now. Sorry."
            elif Girl == JeanX:
                Girl.text "busy"
            elif Girl == StormX:
                Girl.text "I am occupied right now. I am sorry."
            elif Girl == JubesX:
                Girl.text "im a little busy right now. sorry!"
            elif Girl == MystiqueX:
                Girl.text "I'm not available."

            return
        else:
            if Girl == RogueX:
                Girl.text "why don't you come over here, [Girl.player_petname]?"
            elif Girl == KittyX:
                Girl.text "why don't you come over here, [Girl.player_petname]?"
            elif Girl == EmmaX:
                Girl.text "You could always come over here, [Girl.player_petname]."
            elif Girl == LauraX:
                Girl.text "Why don't you come to me?"
            elif Girl == JeanX:
                Girl.text "come here?"
            elif Girl == StormX:
                Girl.text "Perhaps you could come to me?"
            elif Girl == JubesX:
                Girl.text "Why don't you come to me?"
            elif Girl == MystiqueX:
                Girl.text "You should come to me."

        menu(nvl = True):
            extend ""
            "Sure, I'll be right there.":
                Player.text "Sure, I'll be right there."

                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "inhibition", 1)

                if Girl == RogueX:
                    Girl.text "see you!"
                elif Girl == KittyX:
                    Girl.text "see ya!"
                elif Girl == EmmaX:
                    Girl.text "I'll be waiting."
                elif Girl == LauraX:
                    Girl.text "See you when you get here."
                elif Girl == JeanX:
                    Girl.text "good"
                elif Girl == StormX:
                    Girl.text "I will see you soon then."
                elif Girl == JubesX:
                    Girl.text "cool, see you then"
                elif Girl == MystiqueX:
                    Girl.text "Excellent."

                $ line = "go to"
            "Nah, we can talk later.":
                Player.text "Nah, we can talk later."

                call change_Girl_stat(Girl, "obedience", 1)
                call change_Girl_stat(Girl, "obedience", 2)

                if Girl == RogueX:
                    Girl.text "oh, ok. talk to you later then"
                elif Girl == KittyX:
                    Girl.text "oh, ok. later then"
                elif Girl == EmmaX:
                    Girl.text "Very well."
                elif Girl == LauraX:
                    Girl.text "Ok. Later then."
                elif Girl == JeanX:
                    Girl.text "k"
                elif Girl == StormX:
                    Girl.text "Fine. Later then."
                elif Girl == JubesX:
                    Girl.text "ok. later then"
                elif Girl == MystiqueX:
                    Girl.text "Maybe."
            "Could you please come visit me? I'm lonely.":
                Player.text "Could you please come visit me? I'm lonely."

                if approval_check(Girl, 600, "L") or approval_check(Girl, 1400):
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 1)

                    if Girl == StormX:
                        Girl.text "Well we cannot have that. . ."
                    elif Girl == JubesX:
                        Girl.text "aw, how could I say \"no\"?"

                    $ line = "lonely"
                else:
                    call change_Girl_stat(Girl, "inhibition", 1)

                    if Girl == LauraX:
                        Girl.text "Man, you are such a sap."
                    elif Girl == JeanX:
                        Girl.text "needy much?"

                    $ line = "no"
            "Come on, it'll be fun.":
                Player.text "Come on, it'll be fun."

                if approval_check(Girl, 400, "L") and approval_check(Girl, 800):
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", 1)

                    $ line = "fun"
                else:
                    call change_Girl_stat(Girl, "inhibition", 1)

                    $ line = "no"
            "I said come over here.":
                Player.text "I said come over here."

                if approval_check(Girl, 600, "O"):
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "love", -1)
                    call change_Girl_stat(Girl, "obedience", 1)

                    $ line = "command"
                elif D20 >= 7 and approval_check(Girl, 1400):
                    call change_Girl_stat(Girl, "love", -2)
                    call change_Girl_stat(Girl, "love", -1)
                    call change_Girl_stat(Girl, "obedience", 2)
                    call change_Girl_stat(Girl, "obedience", 1)

                    if Girl == RogueX:
                        Girl.text "I suppose I can, [Girl.player_petname]."
                    elif Girl == KittyX:
                        Girl.text "ok, fine, [Girl.player_petname]"
                    elif Girl == EmmaX:
                        Girl.text "Ok, fine, [Girl.player_petname]."
                    elif Girl == LauraX:
                        Girl.text "Ok, fine."
                    elif Girl == JeanX:
                        Girl.text "fine"
                    elif Girl == StormX:
                        Girl.text "Fine."
                    elif Girl == JubesX:
                        Girl.text "ok fine"
                    elif Girl == MystiqueX:
                        Girl.text "Mmm, ok."

                    $ line = "yes"
                elif approval_check(Girl, 200, "O"):
                    call change_Girl_stat(Girl, "love", -4)
                    call change_Girl_stat(Girl, "love", -2)

                    if Girl == RogueX:
                        Girl.text "I don't know who you think you are, boss'in me around like that."
                    elif Girl == KittyX:
                        Girl.text "you're not my supervisor!"
                    elif Girl == EmmaX:
                        Girl.text "Who do you think is in charge here?!"
                    elif Girl == LauraX:
                        Girl.text "Don't even try it."
                    elif Girl == JeanX:
                        Girl.text "and I said no."
                    elif Girl == StormX:
                        Girl.text "And I refused."
                    elif Girl == JubesX:
                        Girl.text "no way."
                    elif Girl == MystiqueX:
                        Girl.text "How amusing."

                    call change_Girl_stat(Girl, "obedience", -2)
                    call change_Girl_stat(Girl, "inhibition", 2)
                    call change_Girl_stat(Girl, "inhibition", 1)

                    if Girl == RogueX:
                        Girl.text "if you want to see me, you know where to find me."
                    elif Girl == KittyX:
                        Girl.text "you know where to find me."
                    elif Girl == EmmaX:
                        Girl.text "You'd better hope you don't find me here."
                    elif Girl == LauraX:
                        Girl.text "I'm staying put."
                    elif Girl == JeanX:
                        Girl.text "im staying here."
                    elif Girl == StormX:
                        Girl.text "I would rather stay."
                    elif Girl == JubesX:
                        Girl.text "im staying here."
                    elif Girl == MystiqueX:
                        Girl.text "No."
                else:
                    call change_Girl_stat(Girl, "love", 1)
                    call change_Girl_stat(Girl, "obedience", -1)
                    call change_Girl_stat(Girl, "inhibition", 1)
                    call change_Girl_stat(Girl, "inhibition", 1)

                    $ line = "no"
    else:
        if Girl.love > Girl.obedience:
            if Girl == RogueX:
                Girl.text "id love to, [Girl.player_petname]!"
            elif Girl == KittyX:
                Girl.text "sure!"
            elif Girl == EmmaX:
                Girl.text "I'd love to."
            elif Girl == LauraX:
                Girl.text "Sure."
            elif Girl == JeanX:
                Girl.text "ok fine"
            elif Girl == StormX:
                Girl.text "On my way."
            elif Girl == JubesX:
                Girl.text "sure!"
            elif Girl == MystiqueX:
                Girl.text "On my way."
        else:
            if Girl == RogueX:
                Girl.text "ok, I'll be right over, [Girl.player_petname]"
            elif Girl == KittyX:
                Girl.text "ok, be there in a jiff, [Girl.player_petname]"
            elif Girl == EmmaX:
                Girl.text "I'll be right there, [Girl.player_petname]."
            elif Girl == LauraX:
                Girl.text "Ok, I'm in route."
            elif Girl == JeanX:
                Girl.text "ok, if you insist. . ."
            elif Girl == StormX:
                Girl.text "Very well."
            elif Girl == JubesX:
                Girl.text "cool, omw"
            elif Girl == MystiqueX:
                Girl.text "I'll be right there, [Girl.player_petname]."

        $ line = "yes"

    if not line:
        return
    elif line == "go to":
        if Girl.location == "bg_player":
            if Girl == RogueX:
                Girl.text "ill be waiting"
            elif Girl == KittyX:
                Girl.text "ill be here for you"
            elif Girl == EmmaX:
                Girl.text "I'll be waiting for you."
            elif Girl == LauraX:
                Girl.text "I'll be waiting."
            elif Girl == JeanX:
                Girl.text "dont keep me waiting"
            elif Girl == StormX:
                Girl.text "I will be waiting."
            elif Girl == JubesX:
                Girl.text "ill be waiting"
            elif Girl == MystiqueX:
                Girl.text "I'll be expecting you."
        elif Girl.location == Girl.home:
            if Girl == RogueX:
                Girl.text "ill get tidied up"
            elif Girl == KittyX:
                Girl.text "ill clean up a few things"
            elif Girl == EmmaX:
                Girl.text "I'll tidy up a few things."
            elif Girl == LauraX:
                Girl.text "I'll. . . make some space."
            elif Girl == JeanX:
                Girl.text "dont keep me waiting"
            elif Girl == StormX:
                Girl.text "I will see you soon then."
            elif Girl == JubesX:
                Girl.text "ill get ready"
            elif Girl == MystiqueX:
                Girl.text "Don't keep me waiting."
        elif Girl.location == "bg_campus":
            if Girl == RogueX:
                Girl.text "ill keep an eye out for you"
            elif Girl == KittyX:
                Girl.text "ive got a nice spot in the shade"
            elif Girl == EmmaX:
                Girl.text "I've got a nice location picked out."
            elif Girl == LauraX:
                Girl.text "Look for the biggest tree."
            elif Girl == JeanX:
                Girl.text "ok"
            elif Girl == StormX:
                Girl.text "I will keep an eye out for you."
            elif Girl == JubesX:
                Girl.text "im still in the shade a bit"
            elif Girl == MystiqueX:
                Girl.text "Lovely."
        elif Girl.location == "bg_classroom" or Girl.teaching:
            if Girl == RogueX:
                Girl.text "see you!"
            elif Girl == KittyX:
                Girl.text "ill hold a seat for you!"
            elif Girl == EmmaX:
                Girl.text "You don't want to miss too much."
            elif Girl == LauraX:
                Girl.text "K, there's room next to me."
            elif Girl == JeanX:
                Girl.text "ok then"
            elif Girl == StormX:
                Girl.text "I will see you soon then."
            elif Girl == JubesX:
                Girl.text "k, there's room next to me"
        elif Girl.location == "bg_dangerroom":
            if Girl == RogueX:
                Girl.text "ill be warming up!"
            elif Girl == KittyX:
                Girl.text "ill be warming up!"
            elif Girl == EmmaX:
                Girl.text "I'll try to save some for you."
            elif Girl == LauraX:
                Girl.text "I'll try to leave some bots for 'ya."
            elif Girl == JeanX:
                Girl.text "ill try not to finish the exercise myself"
            elif Girl == StormX:
                Girl.text "I will see you soon then."
            elif Girl == JubesX:
                Girl.text "don't be long :)"
            elif Girl == MystiqueX:
                Girl.text "I will be here."
        elif Girl.location == "bg_shower":
            if Girl == RogueX:
                Girl.text "I guess ill be here"
            elif Girl == KittyX:
                Girl.text "I guess ill be lathering up"
            elif Girl == EmmaX:
                Girl.text "Don't keep me waiting. . ."
            elif Girl == LauraX:
                Girl.text "I'll leave you some hot water."
            elif Girl == JeanX:
                Girl.text "ill see you then"
            elif Girl == StormX:
                Girl.text "I will leave you some hot water."
            elif Girl == JubesX:
                Girl.text "ill leave you some hot water ;)"
            elif Girl == MystiqueX:
                Girl.text "Don't keep me waiting."

        call hide_all

        $ Player.traveling = True

        if Girl.location == "bg_player":
            jump player_room
        elif Girl.location == Girl.home:
            $ Girl = Girl

            jump girls_room
        elif Girl.location == "bg_campus":
            jump campus
        elif Girl.location == "bg_classroom":
            jump classroom
        elif Girl.location == "bg_dangerroom":
            jump danger_room
        elif Girl.location == "bg_shower":
            jump shower_room
        elif Girl.location == "bg_pool":
            jump pool
        elif Girl.location == "bg_study":
            jump study
        elif Girl.location == "bg_mall":
            jump mall
    elif line == "no":
        if Girl.location == "bg_classroom" or Girl.teaching:
            if Girl == RogueX:
                Girl.text "I seriously cant, [Girl.player_petname], big test coming up"
            elif Girl == KittyX:
                Girl.text "I really need to study, [Girl.player_petname]"
            elif Girl == EmmaX:
                if Girl.teaching:
                    Girl.text "I can't exactly leave class, [Girl.player_petname]."
                else:
                    Girl.text "I have a lot of paperwork, [Girl.player_petname]."
            elif Girl == LauraX:
                Girl.text "I can't skip this lecture."
            elif Girl == JeanX:
                Girl.text "sorry, [Girl.player_petname], im kinda busy"
            elif Girl == StormX:
                Girl.text "I cannot leave class like this."
            elif Girl == JubesX:
                Girl.text "I cant skip this lecture"
        elif Girl.location == "bg_dangerroom":
            if Girl == RogueX:
                Girl.text "wish I could, [Girl.player_petname], but I need to get some hours in"
            elif Girl == KittyX:
                Girl.text "im just getting a workout in"
            elif Girl == EmmaX:
                Girl.text "I'm just getting warmed up here."
            elif Girl == LauraX:
                Girl.text "I'm just getting warmed up though!"
            elif Girl == JeanX:
                Girl.text "sorry, [Girl.player_petname], im kinda busy"
            elif Girl == StormX:
                Girl.text "I have work to put in here."
            elif Girl == JubesX:
                Girl.text "im just getting into it [Girl.player_petname]"
            elif Girl == MystiqueX:
                Girl.text "I have a schedule, [Girl.player_petname]."
        else:
            if Girl == RogueX:
                Girl.text "sorry, [Girl.player_petname], but im kinda busy right now"
            elif Girl == KittyX:
                Girl.text "sorry, [Girl.player_petname], but im kinda busy"
            elif Girl == EmmaX:
                Girl.text "I have a lot to finish up here."
            elif Girl == LauraX:
                Girl.text "Sorry, [LauraX.player_petname], I'm kinda busy."
            elif Girl == JeanX:
                Girl.text "sorry, [Girl.player_petname], im kinda busy"
            elif Girl == StormX:
                Girl.text "I am sorry, [Girl.player_petname], I am occupied."
            elif Girl == JubesX:
                Girl.text "sorry, [Girl.player_petname], im kinda busy"
            elif Girl == MystiqueX:
                Girl.text "Not now, [Girl.player_petname]"

        return
    elif line == "lonely":
        if Girl == RogueX:
            Girl.text "oh, how could I say no to you, [Girl.player_petname]?"
        elif Girl == KittyX:
            Girl.text "awwww, how sweet!"
        elif Girl == EmmaX:
            Girl.text "Well, we can't have that now."
        elif Girl == LauraX:
            Girl.text "You are such a dork!"
        elif Girl == JeanX:
            Girl.text "oh fine"
        elif Girl == StormX:
            Girl.text "Why must you be so adorable?"
        elif Girl == JubesX:
            Girl.text "aw, well I can help with that!"
        elif Girl == MystiqueX:
            Girl.text "You are strangely endearing."
    elif line == "command":
        if Girl == RogueX:
            Girl.text "if you insist, [Girl.player_petname]"
        elif Girl == KittyX:
            Girl.text "yes [Girl.player_petname]"
        elif Girl == EmmaX:
            Girl.text "If I must. . ."
        elif Girl == LauraX:
            Girl.text "Yes, [LauraX.player_petname]."
        elif Girl == JeanX:
            Girl.text "fine [Girl.player_petname]"
        elif Girl == StormX:
            Girl.text "Yes, [Girl.player_petname]."
        elif Girl == JubesX:
            Girl.text "ok [Girl.player_petname]"
        elif Girl == MystiqueX:
            Girl.text "Yes, [Girl.player_petname]."

    $ Girl.change_Outfit()

    call Girls_arrive(Girl)

    return

label dismiss(Girl):
    if Girl in Player.Party:
        $ Player.Party.remove(Girl)

    $ leaving = False

    menu:
        "You can leave if you like.":
            if Girl.location == Player.location and not approval_check(Girl, 700, "O"):
                if Girl == RogueX:
                    Girl.voice "Thanks, but I think I'll stick around."
                elif Girl == KittyX:
                    Girl.voice "Well, I think I'll stay."
                elif Girl == EmmaX:
                    Girl.voice "Be that as it may, I'll stick around for a bit."
                elif Girl == LauraX:
                    Girl.voice "Ok. [[she does not seem to be moving. . .]"
                elif Girl == JeanX:
                    Girl.voice "Ok. [[she does not seem to be moving. . .]"
                elif Girl == StormX:
                    Girl.voice "You have been heard. [[she does not seem to be moving. . .]"
                elif Girl == JubesX:
                    Girl.voice "K. . . [[she does not seem to be moving. . .]"
            else:
                if Girl == RogueX:
                    Girl.voice "Sure, ok. See you later."
                elif Girl == KittyX:
                    Girl.voice "Ok, later!"
                elif Girl == EmmaX:
                    Girl.voice "Very well, [Girl.player_petname]"
                elif Girl == LauraX:
                    Girl.voice "Ok."
                elif Girl == JeanX:
                    Girl.voice "Ok."
                elif Girl == StormX:
                    Girl.voice "Ok then."
                elif Girl == JubesX:
                    Girl.voice "K. . ."

                $ leaving = True
        "Could you give me the room please?":
            if Girl.location == Player.location and not approval_check(Girl, 800, "LO"):
                if Girl == RogueX:
                    Girl.voice "I'd rather stick around."
                elif Girl == KittyX:
                    Girl.voice "I've got nowhere better to be."
                elif Girl == EmmaX:
                    Girl.voice "As it happens, I don't have any other plans."
                elif Girl == LauraX:
                    Girl.voice "Nobody's kicking you out [[She doesn't move]."
                elif Girl == JeanX:
                    Girl.voice "What? No."
                elif Girl == StormX:
                    Girl.voice "I'd rather stay."
                elif Girl == JubesX:
                    Girl.voice "Nah, I'm good here."
            elif not approval_check(Girl, 500, "LO"):
                if Girl == RogueX:
                    Girl.voice "I think I should probably stick around."
                elif Girl == KittyX:
                    Girl.voice "Yeah, no."
                elif Girl == EmmaX:
                    Girl.voice "I don't think that I can."
                elif Girl == LauraX:
                    Girl.voice "Nope."
                elif Girl == JeanX:
                    Girl.voice "What? No."
                elif Girl == StormX:
                    Girl.voice "No, thank you."
                elif Girl == JubesX:
                    Girl.voice "Nah, I'm good here."
            else:
                if "dismissed" not in Girl.daily_history:
                    call change_Girl_stat(Girl, "obedience", 5)
                    call change_Girl_stat(Girl, "obedience", 5)

                if Girl == RogueX:
                    Girl.voice "Not a problem, see you later then."
                elif Girl == KittyX:
                    Girl.voice "Sure, ok."
                elif Girl == EmmaX:
                    Girl.voice "Very well. . ."
                elif Girl == LauraX:
                    Girl.voice "Sure, ok."
                elif Girl == JeanX:
                    Girl.voice "Whatever."
                elif Girl == StormX:
                    Girl.voice "Ok then."
                elif Girl == JubesX:
                    Girl.voice "Fine. . ."

                $ leaving = True
        "You can go now.":
            if Girl.location == Player.location and not approval_check(Girl, 500, "O"):
                if Girl == RogueX:
                    Girl.voice "I think I'll stay."
                elif Girl == KittyX:
                    Girl.voice "Um, no."
                elif Girl == EmmaX:
                    Girl.voice "No, I don't believe that I can."
                elif Girl == LauraX:
                    Girl.voice "But I won't."
                elif Girl == JeanX:
                    Girl.voice "Right. [[she's not moving]"
                elif Girl == StormX:
                    Girl.voice "But I would rather stay."
                elif Girl == JubesX:
                    Girl.voice "Yeah, but I'm not."
            elif not approval_check(Girl, 300, "O"):
                $ Girl.change_face("confused")

                if Girl == RogueX:
                    Girl.voice "Well if you want me to go, then maybe I should stick around."
                elif Girl == KittyX:
                    Girl.voice "Not when you've got me curious."
                elif Girl == EmmaX:
                    Girl.voice "Now I am intrigued."
                elif Girl == LauraX:
                    Girl.voice "Why?"
                elif Girl == JeanX:
                    Girl.voice "Uh-huh. [[she's not moving]"
                elif Girl == StormX:
                    Girl.voice "Oh?"
                elif Girl == JubesX:
                    Girl.voice "Why's that?"
            else:
                if Girl == RogueX:
                    Girl.voice "If you wish."
                elif Girl == KittyX:
                    Girl.voice "Um, ok."
                elif Girl == EmmaX:
                    Girl.voice "Very well. . ."
                elif Girl == LauraX:
                    Girl.voice "Ok."
                elif Girl == JeanX:
                    Girl.voice "Whatever."
                elif Girl == StormX:
                    Girl.voice "Ok then."
                elif Girl == JubesX:
                    Girl.voice "Oh, ok. . ."

                $ leaving = True
        "Never mind.":
            return

    if leaving:
        call remove_Girl(Girl)
    elif not leaving:
        menu:
            extend ""
            "I insist, get going.":
                if approval_check(Girl, 1200, "LO") or approval_check(Girl, 500, "O"):
                    if Girl == RogueX:
                        Girl.voice "Ok, if you insist."
                    elif Girl == KittyX:
                        Girl.voice "Um, ok."
                    elif Girl == EmmaX:
                        Girl.voice "Very well. . ."
                    elif Girl == LauraX:
                        Girl.voice "Ok, fine."
                    elif Girl == JeanX:
                        Girl.voice ". . ."
                        Girl.voice "Fine."
                    elif Girl == StormX:
                        Girl.voice ". . . Fine."
                    elif Girl == JubesX:
                        Girl.voice "Ok, fine. . ."

                    $ leaving = True
                elif approval_check(Girl, 1000, "LO") or approval_check(Girl, 300, "O"):
                    $ Girl.change_face("angry")

                    if Girl == RogueX:
                        Girl.voice "Fine, if you're going to be a dick about it."
                    elif Girl == KittyX:
                        Girl.voice "Fine, jerk!"
                    elif Girl == EmmaX:
                        Girl.voice "I'll leave, but do not test me, [Girl.player_petname]"
                    elif Girl == LauraX:
                        Girl.voice "I've got stuff to do anyway."
                    elif Girl == JeanX:
                        Girl.voice ". . ."
                        Girl.voice "Oh, I forgot to mention, I needed to go do. . . something."
                    elif Girl == StormX:
                        Girl.voice "Well, I did have some errands to run."
                    elif Girl == JubesX:
                        Girl.voice "Whatever. . ."

                    $ leaving = True
                else:
                    $ Girl.change_face("angry")

                    if Girl == RogueX:
                        Girl.voice "Like hell I will."
                    elif Girl == KittyX:
                        Girl.voice "Noooope."
                    elif Girl == EmmaX:
                        Girl.voice "Well now I'm definitely not."
                    elif Girl == LauraX:
                        Girl.voice "Not until I see what you have planned here."
                    elif Girl == JeanX:
                        Girl.voice "Well that doesn't sound fun."
                    elif Girl == StormX:
                        Girl.voice "I would definitely prefer to stay now."
                    elif Girl == JubesX:
                        Girl.voice "Well now I'm -definitely- sticking around. . ."
            "Ok, never mind.":
                pass

    if leaving:
        call remove_Girl(Girl)

    return

label Girls_arrive(arriving_Girls):
    if arriving_Girls in all_Girls:
        $ arriving_Girls = [arriving_Girls]

    $ arriving_Girls = sort_Girls_by_approval(arriving_Girls)

    call add_Girls(arriving_Girls)

    python:
        for G in all_Girls:
            if G in Nearby:
                G.location = "nearby"

    return

label Girl_leaving(Girl):
    if not approval_check(Girl, 700):
        if Girl.location == "bg_classroom" or Girl.teaching:
            if Girl == RogueX:
                Girl.voice "I'm headed to class right now, [Girl.player_petname]."
            elif Girl == KittyX:
                Girl.voice "I'm[Girl.like]headed to class right now."
            elif Girl == EmmaX:
                if Girl.teaching:
                    Girl.voice "I have a class to teach."
                else:
                    Girl.voice "I have some paperwork to take care of."
            elif Girl == LauraX:
                Girl.voice "I've got class."
            elif Girl == JeanX:
                Girl.voice "I've got class."
            elif Girl == StormX:
                if Girl.teaching:
                    Girl.voice "I've got class to teach."
            elif Girl == JubesX:
                Girl.voice "I've got class."
        elif Girl.location == "bg_dangerroom":
            if Girl == RogueX:
                Girl.voice "I'm hitting the Danger Room, [Girl.player_petname]."
            elif Girl == KittyX:
                Girl.voice "I'm[Girl.like]hitting the Danger Room."
            elif Girl == EmmaX:
                Girl.voice "I have a workout scheduled."
            elif Girl == LauraX:
                Girl.voice "I'm hitting the Danger Room."
            elif Girl == JeanX:
                Girl.voice "I'm getting some exercise."
            elif Girl == StormX:
                Girl.voice "I am heading for the Danger Room."
            elif Girl == JubesX:
                Girl.voice "I'm hitting the Danger Room."
            elif Girl == MystiqueX:
                Girl.voice "I have a workout scheduled."
        elif Girl.location == "bg_campus":
            if Girl == RogueX:
                Girl.voice "I'm going to hang out on campus, [Girl.player_petname]."
            elif Girl == KittyX:
                Girl.voice "I'm[Girl.like]going to hang out on campus."
            elif Girl == EmmaX:
                Girl.voice "I'm going to take in some sun."
            elif Girl == LauraX:
                Girl.voice "I'm taking a nap in the quad."
            elif Girl == JeanX:
                Girl.voice "I'm taking a break in the quad."
            elif Girl == StormX:
                Girl.voice "I am going to relax in the courtyard."
            elif Girl == JubesX:
                Girl.voice "I'm gonna get some sun."
            elif Girl == MystiqueX:
                Girl.voice "I am going to go enjoy the weather."
        elif Girl.location == Girl.home:
            if Girl == RogueX:
                Girl.voice "I'm heading back to my room, [Girl.player_petname]."
            elif Girl == KittyX:
                Girl.voice "I'm[Girl.like]heading back to my room."
            elif Girl == EmmaX:
                Girl.voice "I'm heading back to my room."
            elif Girl == LauraX:
                Girl.voice "I'm headed back to my room."
            elif Girl == JeanX:
                Girl.voice "I'm going back to my room."
            elif Girl == StormX:
                Girl.voice "I am returning to my room."
            elif Girl == JubesX:
                Girl.voice "I'm headed back to my room."
            elif Girl == MystiqueX:
                Girl.voice "I will be in my room."
        elif Girl.location == "bg_player":
            if Girl == RogueX:
                Girl.voice "I'll be heading to your room, [Girl.player_petname]."
            elif Girl == KittyX:
                Girl.voice "I'll[Girl.like]be heading to your room."
            elif Girl == EmmaX:
                Girl.voice "I'll be heading to your room."
            elif Girl == LauraX:
                Girl.voice "I'm gonna hang out in your room for a bit."
            elif Girl == JeanX:
                Girl.voice "I'm hanging out in your room for a bit."
            elif Girl == StormX:
                Girl.voice "I am planning to relax in your room."
            elif Girl == JubesX:
                Girl.voice "I'm gonna go hang in your room."
            elif Girl == MystiqueX:
                Girl.voice "I plan on spending some time in your room."
        elif Girl.location == "bg_pool":
            if Girl == RogueX:
                Girl.voice "I'm headed for the pool."
            elif Girl == KittyX:
                Girl.voice "I'm[Girl.like]hitting up the pool."
            elif Girl == EmmaX:
                Girl.voice "I was heading for a swim."
            elif Girl == LauraX:
                Girl.voice "I was hitting the pool."
            elif Girl == JeanX:
                Girl.voice "I going to hit the pool."
            elif Girl == StormX:
                Girl.voice "I was going to take a swim."
            elif Girl == JubesX:
                Girl.voice "I was hitting the pool."
            elif Girl == MystiqueX:
                Girl.voice "I think I'll take a dip."
        elif Girl.location == "bg_shower":
            if approval_check(Girl, 1400):
                if Girl == RogueX:
                    Girl.voice "I'm hitting the showers, later."
                elif Girl == KittyX:
                    Girl.voice "I'm catching a shower, later!"
                elif Girl == EmmaX:
                    Girl.voice "I'm going to take a quick shower."
                elif Girl == LauraX:
                    Girl.voice "I'm hitting the showers, later."
                elif Girl == JeanX:
                    Girl.voice "I'm hitting the showers."
                elif Girl == StormX:
                    Girl.voice "I am hitting the showers, I will see you later."
                elif Girl == JubesX:
                    Girl.voice "I'm hitting the showers, later."
                elif Girl == MystiqueX:
                    Girl.voice "I'm going to to the showers."
            else:
                if Girl == RogueX:
                    Girl.voice "I'm . . . headed out, see you later."
                elif Girl == KittyX:
                    Girl.voice "I'm outta here, later!"
                elif Girl == EmmaX:
                    Girl.voice "I'll see you later."
                elif Girl == LauraX:
                    Girl.voice "I'm headed out."
                elif Girl == JeanX:
                    Girl.voice "I'm headed out."
                elif Girl == StormX:
                    Girl.voice "I will see you later."
                elif Girl == JubesX:
                    Girl.voice "I'm headed out."
                elif Girl == MystiqueX:
                    Girl.voice "I will see you later."
        else:
            if Girl == RogueX:
                Girl.voice "I'm headed out, see you later."
            elif Girl == KittyX:
                Girl.voice "I'm headed out, see you later."
            elif Girl == EmmaX:
                Girl.voice "I'll see you later."
            elif Girl == LauraX:
                Girl.voice "I'm headed out, later."
            elif Girl == JeanX:
                Girl.voice "I'm headed out."
            elif Girl == StormX:
                Girl.voice "I will see you later."
            elif Girl == JubesX:
                Girl.voice "I'm headed out, later."
            elif Girl == MystiqueX:
                Girl.voice "Goodbye for now."

        call hide_Girl(Girl)

        return

    if Girl.location == "bg_classroom" or Girl.teaching:
        if Girl == RogueX:
            Girl.voice "I'm headed to class right now, [Girl.player_petname], you could join me."
        elif Girl == KittyX:
            Girl.voice "I'm headed to class right now, you could[Girl.like]join me."
        elif Girl == EmmaX:
            if Girl.teaching:
                Girl.voice "I've got a class to teach, but you could probably learn a thing or two from it."
            else:
                Girl.voice "I have some paperwork to take care of, but you could keep me company."
        elif Girl == LauraX:
            Girl.voice "I've got class, want in?"
        elif Girl == JeanX:
            Girl.voice "I've got class."
        elif Girl == StormX:
            Girl.voice "I've got class to teach, are you attending?"
        elif Girl == JubesX:
            Girl.voice "I've got class, you interested?"
    elif Girl.location == "bg_dangerroom":
        if Girl == RogueX:
            Girl.voice "I'm hitting the Danger Room, [Girl.player_petname], care to join me?"
        elif Girl == KittyX:
            Girl.voice "I'm hitting the Danger Room, care to[Girl.like]join me?"
        elif Girl == EmmaX:
            Girl.voice "I have a workout planned, but there's room for one more."
        elif Girl == LauraX:
            Girl.voice "I've got some Danger Room time, want in?"
        elif Girl == JeanX:
            Girl.voice "I've got some Danger Room time scheduled."
        elif Girl == StormX:
            Girl.voice "I am heading for the Danger Room, care to join me?"
        elif Girl == JubesX:
            Girl.voice "I've got some Danger Room time, you interested?"
        elif Girl == MystiqueX:
            Girl.voice "Interested in joining me for a workout?"
    elif Girl.location == "bg_campus":
        if Girl == RogueX:
            Girl.voice "I'm going to hang out on campus, [Girl.player_petname], want to hang with me?"
        elif Girl == KittyX:
            Girl.voice "I'm going to[Girl.like]hang out on campus, want to chill with me?"
        elif Girl == EmmaX:
            Girl.voice "I'm planning to get some sunning in, care to join me?"
        elif Girl == LauraX:
            Girl.voice "I'm taking a nap on the quad, you want in?"
        elif Girl == JeanX:
            Girl.voice "I'm hanging out on the quad."
        elif Girl == StormX:
            Girl.voice "I am going to relax in the courtyard, care to join me?"
        elif Girl == JubesX:
            Girl.voice "I'm gonna get some sun on the quad, you interested?"
        elif Girl == MystiqueX:
            Girl.voice "Would you like to join me on the quad, [Girl.player_petname]?"
    elif Girl.location == Girl.home:
        if Girl == RogueX:
            Girl.voice "I'm heading back to my room, [Girl.player_petname], want to swing by?"
        elif Girl == KittyX:
            Girl.voice "I'm heading back to my room, want to[Girl.like]hang out?"
        elif Girl == EmmaX:
            Girl.voice "I'm heading back to my room, but you can walk me back."
        elif Girl == LauraX:
            Girl.voice "I'm headed back to my room, you want in?"
        elif Girl == JeanX:
            Girl.voice "I'm headed back to my room."
        elif Girl == StormX:
            Girl.voice "I am returning to my room, care to join me?"
        elif Girl == JubesX:
            Girl.voice "I'm headed back to my room, you interested?"
        elif Girl == MystiqueX:
            Girl.voice "I'm going back to my room, but you are welcome."
    elif Girl.location == "bg_player":
        if Girl == RogueX:
            Girl.voice "I'll be heading to your room, [Girl.player_petname]."
        elif Girl == KittyX:
            Girl.voice "I'll[Girl.like]be heading to your room."
        elif Girl == EmmaX:
            Girl.voice "I'm actually heading to your room, [Girl.player_petname]."
        elif Girl == LauraX:
            Girl.voice "I'm going to hang out in your room for a bit, you coming?"
        elif Girl == JeanX:
            Girl.voice "I'm going to hang out in your room for a bit."
        elif Girl == StormX:
            Girl.voice "I am planning to relax in your room, care to join me?"
        elif Girl == JubesX:
            Girl.voice "I'm going to hang out in your room for a bit, you interested?"
        elif Girl == MystiqueX:
            Girl.voice "I will be in your room."
    elif Girl.location == "bg_shower":
        if approval_check(Girl, 1600):
            if Girl == RogueX:
                Girl.voice "I'm hitting the showers, [Girl.player_petname], care to join me?"
            elif Girl == KittyX:
                Girl.voice "I'm[Girl.like]hitting the showers, want to join me?"
            elif Girl == EmmaX:
                Girl.voice "I'm catching a quick shower, care to join me?"
            elif Girl == LauraX:
                Girl.voice "I'm hitting the showers, you could use one too."
            elif Girl == JeanX:
                Girl.voice "I'm hitting the showers."
            elif Girl == StormX:
                Girl.voice "I am hitting the showers, care to join me?"
            elif Girl == JubesX:
                Girl.voice "I'm hitting the showers, you should join me."
            elif Girl == MystiqueX:
                Girl.voice "Come join me in the showers, [Girl.player_petname]."
        else:
            if Girl == RogueX:
                Girl.voice "I'm hitting the showers, [Girl.player_petname], maybe we could touch base later."
            elif Girl == KittyX:
                Girl.voice "I'm hitting the showers, maybe we could[Girl.like]touch base later."
            elif Girl == EmmaX:
                Girl.voice "I'm headed for the showers, make sure to keep your distance."
            elif Girl == LauraX:
                Girl.voice "I'm hitting the showers, see you later."
            elif Girl == JeanX:
                Girl.voice "I'm hitting the showers, maybe hang back for a bit."
            elif Girl == StormX:
                Girl.voice "I will see you later."
            elif Girl == JubesX:
                Girl.voice "I'm hitting the showers, laters."
            elif Girl == MystiqueX:
                Girl.voice "I will see you later."

            return
    elif Girl.location == "bg_pool":
        if Girl == RogueX:
            Girl.voice "I'm headed for the pool. Wanna come?"
        elif Girl == KittyX:
            Girl.voice "I'm[Girl.like]hitting up the pool. You coming?"
        elif Girl == EmmaX:
            Girl.voice "I was heading for a swim. Care to join me?"
        elif Girl == LauraX:
            Girl.voice "I was hitting the pool. Wanna come?"
        elif Girl == JeanX:
            Girl.voice "I was hitting the pool."
        elif Girl == StormX:
            Girl.voice "I was going to take a swim, care to join me?"
        elif Girl == JubesX:
            Girl.voice "I was hitting the pool. Wanna come?"
        elif Girl == MystiqueX:
            Girl.voice "I'm going to take a dip in the pool, if you're interested."
    else:
        if Girl == RogueX:
            Girl.voice "Why don't you come with me, [Girl.player_petname]?"
        elif Girl == KittyX:
            Girl.voice "Wanna[Girl.like]come with me, [Girl.player_petname]?"
        elif Girl == EmmaX:
            Girl.voice "Would you care to come with me?"
        elif Girl == LauraX:
            Girl.voice "Wanna join me?"
        elif Girl == JeanX:
            Girl.voice "Are you coming with?"
        elif Girl == StormX:
            Girl.voice "Care to join me?"
        elif Girl == JubesX:
            Girl.voice "Wanna join me?"
        elif Girl == MystiqueX:
            Girl.voice "You should koin me, [Girl.player_petname]."

    $ D20 = renpy.random.randint(1, 20)

    menu:
        extend ""
        "Sure, I'll catch up.":
            $ line = "go to"
        "Nah, we can talk later.":
            if Girl == RogueX:
                Girl.voice "Oh, ok. Talk to you later then."
            elif Girl == KittyX:
                Girl.voice "Ok, cool. Talk to you later then."
            elif Girl == EmmaX:
                Girl.voice "Very well, I'll talk to you later."
            elif Girl == LauraX:
                Girl.voice "Sure, whatever."
            elif Girl == JeanX:
                Girl.voice "Fine, whatever."
            elif Girl == StormX:
                Girl.voice "Very well."
            elif Girl == JubesX:
                Girl.voice "Sure, whatever."
            elif Girl == MystiqueX:
                Girl.voice "Very well."

            $ line = None
        "Could you please stay with me? I'll get lonely.":
            if approval_check(Girl, 600, "L") or approval_check(Girl, 1400):
                if Girl == StormX:
                    Girl.voice "Well we cannot have that. . ."
                elif Girl == JubesX:
                    Girl.voice "Aw, how could I say \"no\"?"

                $ line = "lonely"
            else:
                if Girl == LauraX:
                    Girl.voice "Man, you are such a sap."
                elif Girl == JeanX:
                    Girl.voice "Needy much?"

                $ line = "no"
        "Come on, it'll be fun.":
            if approval_check(Girl, 400, "L") and approval_check(Girl, 800):
                call change_Girl_stat(Girl, "love", 1)
                call change_Girl_stat(Girl, "obedience", 1)

                $ line = "fun"
            else:
                call change_Girl_stat(Girl, "inhibition", 1)

                $ line = "no"
        "No, stay here.":
            if approval_check(Girl, 600, "O"):
                $ line = "command"
            elif D20 >= 7 and approval_check(Girl, 1400):
                if Girl == RogueX:
                    Girl.voice "I suppose I can, [Girl.player_petname]."
                elif Girl == KittyX:
                    Girl.voice "Uh, sure, I guess."
                elif Girl == EmmaX:
                    Girl.voice "I guess it wasn't that important. . ."
                elif Girl == LauraX:
                    Girl.voice "I guess if you need me here."
                elif Girl == JeanX:
                    Girl.voice ". . . Fine."
                elif Girl == StormX:
                    Girl.voice "Fine."
                elif Girl == JubesX:
                    Girl.voice "I guess I could. . ."
                elif Girl == MystiqueX:
                    Girl.voice "Hmm. . ."

                $ line = "yes"
            elif not approval_check(Girl, 200, "O"):
                if Girl == RogueX:
                    Girl.voice "I don't know who you think you are, boss'in me around like that."
                    Girl.voice "If you want to see me, you know where to find me."
                elif Girl == KittyX:
                    Girl.voice "[Girl.Like]in your dreams, [Girl.player_petname]."
                    Girl.voice "I'm gone."
                elif Girl == EmmaX:
                    Girl.voice "Does that work with your little strumpets?"
                elif Girl == LauraX:
                    Girl.voice "Don't tell me what to do."
                    Girl.voice "I'm out of here."
                elif Girl == JeanX:
                    Girl.voice "Ha!"
                    Girl.voice "You're not the boss of me."
                elif Girl == StormX:
                    Girl.voice "And I refused."
                    Girl.voice "I would rather stay."
                elif Girl == JubesX:
                    Girl.voice "No way."
                elif Girl == MystiqueX:
                    Girl.voice "Very funny."

                $ line = None
            else:
                $ line = "no"

    if not line:
        call hide_Girl(Girl)

        return
    elif line == "no":
        if Girl.location == "bg_classroom" or Girl.teaching:
            if Girl == RogueX:
                Girl.voice "I seriously can't, [Girl.player_petname], big test coming up."
            elif Girl == KittyX:
                Girl.voice "Totally can't, [Girl.player_petname], Gotta study for the test."
            elif Girl == EmmaX:
                if Girl.teaching:
                    Girl.voice "I'm not \"cutting class,\" [Girl.player_petname]."
                else:
                    Girl.voice "I'm afraid not, [Girl.player_petname], I need to get this work done."
            elif Girl == LauraX:
                Girl.voice "I really can't miss this one."
            elif Girl == JeanX:
                Girl.voice "I'd rather not."
            elif Girl == StormX:
                Girl.voice "I cannot skip class like this."
            elif Girl == JubesX:
                Girl.voice "I really can't miss this one."
        elif Girl.location == "bg_dangerroom":
            if Girl == RogueX:
                Girl.voice "Wish I could, [Girl.player_petname], but I need to get some hours in."
            elif Girl == KittyX:
                Girl.voice "Sorry [Girl.player_petname], but I[Girl.like]need the practice?"
            elif Girl == EmmaX:
                Girl.voice "I'm sorry, but how do you think I keep this figure?"
            elif Girl == LauraX:
                Girl.voice "Sorry [LauraX.player_petname], but I'm going a little stir crazy."
            elif Girl == JeanX:
                Girl.voice "I'd rather not."
            elif Girl == StormX:
                Girl.voice "I have work to put in here."
            elif Girl == JubesX:
                Girl.voice "Sorry [Girl.player_petname], I need the exercise."
            elif Girl == MystiqueX:
                Girl.voice "Sorry [Girl.player_petname], you know I like my routine."
        else:
            if Girl == RogueX:
                Girl.voice "I'm sorry, [Girl.player_petname], but I'm kinda busy right now."
            elif Girl == KittyX:
                Girl.voice "I'm[Girl.like]sorry, [Girl.player_petname], I've got things to do."
            elif Girl == EmmaX:
                Girl.voice "I'm sorry, I'm just much too busy at the moment."
            elif Girl == LauraX:
                Girl.voice "Sorry, I have stuff to do."
            elif Girl == JeanX:
                Girl.voice "I'd rather not."
            elif Girl == StormX:
                Girl.voice "I am sorry, [Girl.player_petname], I am occupied."
            elif Girl == JubesX:
                Girl.voice "Sorry, I'm kinda busy."
            elif Girl == MystiqueX:
                Girl.voice "Not now."

        call hide_Girl(Girl)

        return
    elif line == "go to":
        call hide_Girl(Girl)
        $ change_clothes()

        if Girl.location == "bg_player":
            if Girl == RogueX:
                Girl.voice "I'll be waiting."
            elif Girl == KittyX:
                Girl.voice "I'll be waiting."
            elif Girl == EmmaX:
                Girl.voice "I'll be waiting."
            elif Girl == LauraX:
                Girl.voice "Good."
            elif Girl == JeanX:
                Girl.voice "Good."
            elif Girl == StormX:
                Girl.voice "I will be waiting."
            elif Girl == JubesX:
                Girl.voice "Good."
            elif Girl == MystiqueX:
                Girl.voice "Good."
        elif Girl.location == Girl.home:
            if Girl == RogueX:
                Girl.voice "I'll meet you there."
            elif Girl == KittyX:
                Girl.voice "I'll meet you there."
            elif Girl == EmmaX:
                Girl.voice "I'll be waiting."
            elif Girl == LauraX:
                Girl.voice "Ok."
            elif Girl == JeanX:
                Girl.voice "Ok."
            elif Girl == StormX:
                Girl.voice "I will see you soon then."
            elif Girl == JubesX:
                Girl.voice "Ok."
            elif Girl == MystiqueX:
                Girl.voice "Mmm, see you soon."
        elif Girl.location == "bg_campus":
            if Girl == RogueX:
                Girl.voice "Let's head over there."
            elif Girl == KittyX:
                Girl.voice "Let's head over there."
            elif Girl == EmmaX:
                Girl.voice "Ok, let's."
            elif Girl == LauraX:
                Girl.voice "Ok, nice."
            elif Girl == JeanX:
                Girl.voice "Ok."
            elif Girl == StormX:
                Girl.voice "I will keep an eye out for you."
            elif Girl == JubesX:
                Girl.voice "Ok, nice."
            elif Girl == MystiqueX:
                Girl.voice "Lovely."
        elif Girl.location == "bg_classroom" or Girl.teaching:
            if Girl == RogueX:
                Girl.voice "See you then!"
            elif Girl == KittyX:
                Girl.voice "Cool, study buddy!"
            elif Girl == EmmaX:
                if Girl.teaching:
                    Girl.voice "I'll see you there."
                else:
                    Girl.voice "Excellent, that should pass the time."
            elif Girl == LauraX:
                Girl.voice "Ok, get a move on then."
            elif Girl == JeanX:
                Girl.voice "Ok."
            elif Girl == StormX:
                Girl.voice "I will see you soon then."
            elif Girl == JubesX:
                Girl.voice "Ok, get a move on then."
        elif Girl.location == "bg_dangerroom":
            if Girl == RogueX:
                Girl.voice "I'll be warming up!"
            elif Girl == KittyX:
                Girl.voice "I'll be ready and waiting!"
            elif Girl == EmmaX:
                Girl.voice "I'll try to leave some for you."
            elif Girl == LauraX:
                Girl.voice "I'll get warmed up."
            elif Girl == JeanX:
                Girl.voice "I'll get warmed up."
            elif Girl == StormX:
                Girl.voice "I will see you soon then."
            elif Girl == JubesX:
                Girl.voice "I'll get warmed up."
            elif Girl == MystiqueX:
                Girl.voice "Mhm, see you soon."
        elif Girl.location == "bg_shower":
            if Girl == RogueX:
                Girl.voice "I guess I'll see you there."
            elif Girl == KittyX:
                Girl.voice "I guess I'll see you there."
            elif Girl == EmmaX:
                Girl.voice "I'll get started."
            elif Girl == LauraX:
                Girl.voice "Ok, nice."
            elif Girl == JeanX:
                Girl.voice "Ok, nice."
            elif Girl == StormX:
                Girl.voice "I will leave you some hot water."
            elif Girl == JubesX:
                Girl.voice "Ok, nice."
            elif Girl == MystiqueX:
                Girl.voice "You're in for a treat."
        elif Girl.location == "bg_pool":
            if Girl == RogueX:
                Girl.voice "Let's head over there."
            elif Girl == KittyX:
                Girl.voice "Ok, let's go."
            elif Girl == EmmaX:
                Girl.voice "Ok, let's."
            elif Girl == LauraX:
                Girl.voice "Cool."
            elif Girl == JeanX:
                Girl.voice "Cool."
            elif Girl == StormX:
                Girl.voice "Excellent."
            elif Girl == JubesX:
                Girl.voice "Cool."
            elif Girl == MystiqueX:
                Girl.voice "Excellent."

        call hide_all

        $ Player.traveling = False

        if Girl.location == "bg_player":
            jump player_room
        elif Girl.location == Girl.home:
            $ Girl = Girl

            jump girls_room
        elif Girl.location == "bg_campus":
            jump campus
        elif Girl.location == "bg_classroom":
            jump classroom
        elif Girl.location == "bg_dangerroom":
            jump danger_room
        elif Girl.location == "bg_shower":
            jump shower_room
        elif Girl.location == "bg_pool":
            jump pool
        elif Girl.location == "bg_study":
            jump study
        elif Girl.location == "bg_mall":
            jump mall
    elif line == "lonely":
        if Girl == RogueX:
            Girl.voice "Oh, how could I say \"no\" to you, [Girl.player_petname]?"
        elif Girl == KittyX:
            Girl.voice "I guess[Girl.like]I couldn't leave you lonely. . ."
        elif Girl == EmmaX:
            Girl.voice "Well we wouldn't want that. . ."
        elif Girl == LauraX:
            Girl.voice "Well, I guess you should never go alone. . ."
        elif Girl == JeanX:
            Girl.voice "Well, I guess. . ."
        elif Girl == StormX:
            Girl.voice "Why must you be so adorable?"
        elif Girl == JubesX:
            Girl.voice "Aw, well I can help with that!"
        elif Girl == MystiqueX:
            Girl.voice "Why do I like you. . ."
    elif line == "command":
        if Girl == RogueX:
            Girl.voice "Fine, if you insist, [Girl.player_petname]."
        elif Girl == KittyX:
            Girl.voice "Humph, ok."
        elif Girl == EmmaX:
            Girl.voice "If you insist."
        elif Girl == LauraX:
            Girl.voice "Yes [LauraX.player_petname]."
        elif Girl == JeanX:
            Girl.voice "Fine, [Girl.player_petname]. . ."
        elif Girl == StormX:
            Girl.voice "Yes, [Girl.player_petname]."
        elif Girl == JubesX:
            Girl.voice "Ok, [Girl.player_petname]."
        elif Girl == MystiqueX:
            Girl.voice "Mmm, yes, [Girl.player_petname]."

    if Girl == RogueX:
        Girl.voice "I can stay for a bit."
    elif Girl == KittyX:
        Girl.voice "I guess I can stick around."
    elif Girl == EmmaX:
        Girl.voice "I suppose I can stay for a while."
    elif Girl == LauraX:
        Girl.voice "I'll stick around."
    elif Girl == JeanX:
        Girl.voice "I'll stick around."
    elif Girl == StormX:
        Girl.voice "I'll stick around."
    elif Girl == JubesX:
        Girl.voice "I'll stay here."
    elif Girl == MystiqueX:
        Girl.voice "I suppose I can stay."

    $ Girl.location = Player.location

    return
