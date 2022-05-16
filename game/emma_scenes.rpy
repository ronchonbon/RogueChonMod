

label EmmaMeet:
    $ bg_current = "bg_classroom"
    $ EmmaX.OutfitDay = "casual1"
    $ EmmaX.Outfit = "casual1"
    $ EmmaX.change_outfit("casual1")
    call clear_the_room (EmmaX, 0, 1)
    $ EmmaX.location = "bg_emma"
    $ EmmaX.love = 300
    $ EmmaX.obedience = 0
    $ EmmaX.inhibition = 200
    call shift_focus (EmmaX)
    call set_the_scene
    $ EmmaX.sprite_location = stage_right
    call Lastnamer
    $ EmmaX.player_petnames.append(_return)
    $ EmmaX.player_petname = _return

    "You enter the classroom and have a seat."
    "The bell to class rings, but Professor McCoy seems to be late."
    "A strange woman enters the room and heads to the podium with a regal stride."
    $ EmmaX.change_face("normal")
    show Emma_Sprite at sprite_location(EmmaX.sprite_location) with easeinright
    $ EmmaX.location = "bg_classroom"
    $ EmmaX.ArmPose = 1
    ch_u "Hello students. My name is Emma Frost, and I have been invited to conduct this class."
    ch_e "I hope that over my tenure here you will demonstrate talents and hard work worthy of my respect."
    "She scans her eyes over the room, passing over each student."
    $ EmmaX.change_face("surprised")
    pause 1
    $ EmmaX.change_face("sly",Mouth="sad")
    $ EmmaX.change_stat("love", 90, -10)
    $ EmmaX.lust += 5
    "As her eyes pass over you, they briefly widen and then narrow."
    $ EmmaX.change_face("sly")
    ch_e "Very well, let us begin, class."
    $ EmmaX.change_face("normal")
    "The class is pretty basic today, mostly a lecture on her areas of expertise, psychology and literature."
    $ EmmaX.lust += 5
    "She asks a lot of questions of the students, and singles you out more than once. You notice her glancing in your direction as other students answer."
    $ EmmaX.lust += 5
    call Wait
    call clear_the_room (EmmaX, 0, 1)
    $ EmmaX.location = "bg_classroom"
    call set_the_scene
    ch_e "All right students, class dismissed."
    ch_e "[EmmaX.player_petname], could you wait a moment, I have something to discuss with you."
    menu:
        extend ""
        "Yes?":
            $ EmmaX.change_stat("love", 70, 10)
            $ EmmaX.change_face("normal")
        "I've got places to be.":
            $ EmmaX.change_stat("love", 70, -15)
            $ EmmaX.change_stat("obedience", 80, 10)
            $ EmmaX.change_face("angry")
            ch_e "[Player.name], do not take that attitude with me."
            "She places herself in the doorway, preventing you from leaving."
        "For such a sexy teacher? I've got some time.":
            $ EmmaX.change_stat("love", 70, -5)
            $ EmmaX.change_stat("obedience", 80, 5)
            $ EmmaX.change_face("angry",1, Mouth="smirk")
            ch_e "That's rather. . . inappropriate."
            $ EmmaX.change_face("bemused", Mouth="smile")
            $ EmmaX.change_stat("love", 70, 20)
            $ EmmaX.change_stat("lust", 50, 5)
            $ EmmaX.change_stat("inhibition", 25, 15)
            ch_e "But also obvious, so I can't criticize you too harshly."

    ch_e "I've heard about you from Professor Xavier and. . . others."

    if Player.Rep <= 200:
        $ EmmaX.change_stat("obedience", 80, 10)
        $ EmmaX.change_stat("inhibition", 90, 15)
        $ EmmaX.change_stat("lust", 50, 5)
        $ EmmaX.change_face("angry", Brows="confused")
        ch_e "You seem to be a bit of a scoundrel. . ."
    elif Player.Rep < 600:
        $ EmmaX.change_stat("obedience", 80, 5)
        $ EmmaX.change_stat("inhibition", 90, 5)
        $ EmmaX.change_stat("lust", 50, 5)
        $ EmmaX.change_face("sly")
        ch_e "You have quite a reputation around campus. . ."
    else:
        $ EmmaX.change_face("smile")
        ch_e "You have managed a reasonble reputation. . ."

    if TotalSEXP >= 110 or (len(Player.Harem) >= 2 and "Historia" not in Player.Traits):
        $ EmmaX.change_stat("love", 70, 5)
        $ EmmaX.change_stat("obedience", 80, 10)
        $ EmmaX.change_stat("inhibition", 200, 10)
        $ EmmaX.change_stat("lust", 50, 5)
        $ EmmaX.change_face("sly")
        ch_e "and a number of conquests to your name. . ."
    elif TotalSEXP >= 60:
        $ EmmaX.change_stat("love", 70, 5)
        $ EmmaX.change_stat("obedience", 80, 5)
        $ EmmaX.change_stat("inhibition", 200, 5)
        $ EmmaX.change_stat("lust", 50, 2)
        $ EmmaX.change_face("smile")
        ch_e "and are not without some romantic entanglements. . ."
    else:
        $ EmmaX.change_face("smile", Brows="confused")
        ch_e "though I haven't heard of much of a romantic life. . ."

    if Player.Lvl >= 7:
        $ EmmaX.change_stat("love", 70, 5)
        $ EmmaX.change_stat("obedience", 80, 5)
        $ EmmaX.change_face("smile")
        ch_e "but your grades have been excellent."
    elif Player.Lvl >= 3:
        $ EmmaX.change_face("normal", Brows="confused")
        ch_e "but your grades been marginal at best."
    else:
        $ EmmaX.change_stat("love", 70, -5)
        $ EmmaX.change_stat("lust", 10, -5, 1)
        $ EmmaX.change_face("normal", Brows="sad")
        ch_e "but you haven't been living up to your potential in class."

    $ EmmaX.change_face("normal", Eyes="side")
    ch_e "My particular interest in this case, however. . ."
    $ EmmaX.change_face("sly")
    ch_e "is that I cannot get a \"read\" on you."
    $ EmmaX.change_face("sly", Mouth="normal")
    ch_e "My mutant power is telepathy, the same as Professor Xavier's."
    ch_e "I've grown accustomed to knowing what those around me are thinking."
    $ EmmaX.change_face("bemused", Eyes="side")
    ch_e "With you. . . I cannot do that, which presents an interesting. . ."
    $ EmmaX.change_face("sly")
    ch_e "challenge. . ."
    menu:
        extend ""
        "I imagine it would.":
            $ EmmaX.change_stat("love", 70, 5)
            $ EmmaX.change_stat("inhibition", 200, 5)
            $ EmmaX.change_face("normal")
            ch_e "Hmm, yes."
        "Huh.":
            $ EmmaX.change_stat("love", 70, -1)
            $ EmmaX.change_stat("obedience", 80, -1)
            $ EmmaX.change_face("confused", Mouth="normal")
            ch_e ". . . yes."
            $ EmmaX.change_face("normal")
        "So you can't see what I'm picturing right now?":
            $ EmmaX.change_stat("obedience", 80, 5)
            $ EmmaX.change_face("bemused")
            pause 0.5
            $ EmmaX.change_face("bemused", Eyes="down")
            "She glances downward."
            $ EmmaX.change_face("sly")
            $ EmmaX.change_stat("love", 70, 10)
            $ EmmaX.change_stat("inhibition", 200, 10)
            $ EmmaX.change_stat("lust", 50, 15)
            ch_e "I can't read your mind, but I'm not blind, [EmmaX.player_petname]."
    ch_e "In any case, I think we should set aside some time to talk."
    ch_e "I'd like to make you a personal project, so I can see how you tick."
    menu:
        extend ""
        "I'd be ok with that.":
            $ EmmaX.change_stat("love", 70, 5)
            $ EmmaX.change_stat("inhibition", 200, 5)
            $ EmmaX.change_face("smile")
            ch_e "Excellent, I look forward to it."
        "I don't know if you should experiment on your students.":
            $ EmmaX.change_stat("love", 70, -5)
            $ EmmaX.change_face("normal", Mouth="sad")
            ch_e "There's nothing for you to worry about."
            $ EmmaX.change_face("sly")
            ch_e "I'll be. . . gentle."
        "If it means spending more time with you. . .":
            if ApprovalCheck(EmmaX, 295, "L"):
                $ EmmaX.change_stat("inhibition", 200, 5)
                $ EmmaX.change_stat("lust", 50, 5)
                $ EmmaX.change_face("sly")
                ch_e "Oh, I believe we'll be spending a good deal of time together. . ."
            else:
                $ EmmaX.change_face("angry")
                ch_e "Much as it may pain me, it would. . ."
                $ EmmaX.change_face("normal")
        "What do I get out of it?":
            if not ApprovalCheck(EmmaX, 290, "L"):
                $ EmmaX.change_stat("love", 70, -5)
                $ EmmaX.change_stat("obedience", 80, 5)
                $ EmmaX.change_stat("inhibition", 200, 5)
                $ EmmaX.change_face("angry")
                ch_e "You'll stand some chance of passing this class, [EmmaX.player_petname]."
                $ EmmaX.change_face("normal")
            else:
                if EmmaX.obedience > 0:
                    $ EmmaX.change_face("confused", Mouth="smirk")
                    ch_e "What would you {i}like{/i} to \"get out of it?\""
                    menu:
                        extend ""
                        "I guess if it helps your \"research.\" . .":
                            $ EmmaX.change_stat("love", 70, 10)
                            $ EmmaX.change_stat("obedience", 80, -5)
                            $ EmmaX.change_face("smile")
                            ch_e "I'm glad to see that you can be reasonable."
                        "Spending more time with you would be plenty. . .":
                            $ EmmaX.change_stat("love", 70, 5)
                            $ EmmaX.change_stat("obedience", 80, 5)
                            $ EmmaX.change_stat("lust", 20, 5)
                            $ EmmaX.change_face("sly")
                            ch_e "It certainly should be."
                        "A kiss?":
                            $ EmmaX.change_stat("love", 70, -5)
                            $ EmmaX.change_stat("obedience", 80, 10)
                            $ EmmaX.change_face("surprised",1, Mouth="surprised")
                            ch_e "[EmmaX.player_petname], that is incredibly inappropriate!"
                            $ EmmaX.change_face("sadside",0,Brows="angry")
                            ch_e "I would {i}never{/i} consider such a thing with a student."
                            if ApprovalCheck(EmmaX, 220, "I"):
                                $ EmmaX.change_face("sly",1)
                                $ EmmaX.change_stat("love", 70, 5)
                                $ EmmaX.change_stat("obedience", 80, 5)
                                $ EmmaX.change_stat("inhibition", 200, 5)
                                $ EmmaX.change_stat("lust", 50, 5)
                                ch_e ". . .never. . ."
                        "I think you know what I'd want. . .":
                            $ EmmaX.change_stat("obedience", 80, 5)
                            $ EmmaX.change_stat("lust", 50, 5)
                            $ EmmaX.change_face("sly",Brows="angry")
                            ch_e "Yes, I imagine that I do. . ."
                            if ApprovalCheck(EmmaX, 220, "I"):
                                $ EmmaX.change_face("sly",1)
                                $ EmmaX.change_stat("love", 70, 5)
                                $ EmmaX.change_stat("obedience", 80, 5)
                                $ EmmaX.change_stat("inhibition", 200, 10)
                                $ EmmaX.change_stat("lust", 50, 5)
                                ch_e "And we may be able to come to some sort of \"mutually beneficial\" arrangement."
                            else:
                                $ EmmaX.change_face("bemused",0)
                                $ EmmaX.change_stat("love", 70, -5)
                                ch_e "But figuring out whether I'm correct is the entire point here."
                else:
                    $ EmmaX.change_face("normal")
                    ch_e "The satisfaction of helping my. . . studies."
                    if ApprovalCheck(EmmaX, 300, "L"):
                        $ EmmaX.change_face("sly")
                        $ EmmaX.change_stat("obedience", 80, 5)
                        $ EmmaX.change_stat("inhibition", 200, 5)
                        $ EmmaX.change_stat("lust", 50, 5)
                        ch_e "-and maybe if you're good. . ."
                    else:
                        ch_e "-and nothing more."

    $ EmmaX.change_face("normal",0)
    ch_e "That said, class is finished for the day and I have some paperwork to attend to, so I'll see you. . ."
    ch_e ". . . later. . ."
    hide Emma_Sprite with easeoutright
    "She strides out of the room and down the hall."
    $ EmmaX.location = "bg_emma"
    $ EmmaX.history.append("met")
    $ active_Girls.append(EmmaX) if EmmaX not in active_Girls else active_Girls
    $ Round -= 10
    return





label Emma_Teacher_Caught(Girl=0):


    if "noticed " + Girl.Tag in EmmaX.recent_history:
        return
    if ApprovalCheck(EmmaX, 500, "I") and ApprovalCheck(EmmaX, 1500) and EmmaX.GirlLikeCheck(Girl) >= 500:
        "[EmmaX.name] notices the two of you, but just tilts her head in approval and continues on."
        $ EmmaX.GLG(Girl,800,3,1)
        $ Girl.GLG(EmmaX,800,3,1)
        $ EmmaX.recent_history.append("noticed " + Girl.Tag)
        return

    ch_e "[Player.name]? [Girl.name]? Could you stop what you're doing immediately?"
    call checkout (1)

    $ Girl.change_face("bemused", 2, Eyes="side")
    call AllReset (Girl)
    if ApprovalCheck(Girl, 700, "I"):
        $ Girl.change_face("bemused", 1)
        "[Girl.name] shrugs and returns to her seat."
        call Partner_Like (EmmaX, 2, -1, 500, Girl)
    else:
        "[Girl.name] jumps and dashes out of the room."
        call Partner_Like (EmmaX, -2, -3, 500, Girl)
        call Remove_Girl (Girl)

    $ Girl.Rep -= 1
    call Partner_Like (Girl, 3, 2, 800, EmmaX)
    $ EmmaX.GLG(Girl,800,3,1)

    $ Player.Rep -= 1
    ch_e "Thank you."
    ch_e "And [Player.name], see me after class for detention. . ."

    $ renpy.pop_call()
    $ renpy.pop_call()
    $ Player.Traits.append("detention")
    $ Player.daily_history.append("detention")
    jump Class_Room





label Emma_Caught_Classroom:

    call shift_focus (EmmaX)
    "As you walk down the halls, you hear some odd noises coming from the classroom."
    show blackscreen onlayer black
    $ Player.AddWord(1,"interruption")
    $ bg_current = "bg_classroom"
    call clear_the_room (EmmaX, 0, 1)
    $ EmmaX.change_outfit(Changed=1)
    $ EmmaX.location = 0
    call set_the_scene
    $ EmmaX.location = "bg_desk"
    $ Taboo = 0
    $ EmmaX.change_face("sexy")
    $ EmmaX.eyes = "closed"
    $ EmmaX.ArmPose = 1
    $ Count = 0
    hide blackscreen onlayer black
    $ primary_action = "masturbation"
    $ girl_offhand_action = "fondle_pussy"
    $ second_girl_offhand_action = "fondle_breasts"
    $ EmmaX.recent_history.append("classcaught")
    $ EmmaX.daily_history.append("unseen")
    $ EmmaX.recent_history.append("unseen")
    $ Line = 0
    $ EmmaX.DrainWord("no_masturbation")
    $ EmmaX.recent_history.append("masturbation")
    $ EmmaX.daily_history.append("masturbation")
    "You see [EmmaX.name] leaning back against her desk, her hands tracing slow paths across her body."

    if "Historia" in Player.Traits:
        call Emma_M_Interupted
    else:
        call Emma_M_Cycle
    if "angry" in EmmaX.recent_history:
        return


    $ EmmaX.eyes = "sexy"
    $ EmmaX.brows = "confused"
    $ EmmaX.mouth = "normal"
    $ EmmaX.ArmPose = 1
    $ EmmaX.change_outfit()
    $ bg_current = "bg_classroom"
    call Display_Girl (EmmaX)
    if "classcaught" in EmmaX.history:
        ch_e "I notice you make a habit of dropping in."
        $ EmmaX.change_outfit()
    else:

        $ EmmaX.history.append("classcaught")
        if "Historia" not in Player.Traits:
            $ approval_bonus = 25
        ch_e "Well."
        $ EmmaX.change_face("angry", Eyes="side")
        ch_e "It appears that you've caught me in a somewhat. . . compromising position. . ."
        menu:
            extend ""
            "Yup.":
                $ EmmaX.change_face("perplexed", Mouth="normal")
                $ EmmaX.change_stat("love", 70, -1)
                $ EmmaX.change_stat("obedience", 50, -2)
                $ EmmaX.change_stat("lust", 80, -5)
                ch_e "Er, well. . ."
            "Are you supposed to be shlicking it in class?":
                $ EmmaX.change_face("angry", Eyes="side")
                $ EmmaX.change_stat("obedience", 50, 5)
                $ EmmaX.change_stat("inhibition", 70, 5)
                ch_e "Hrm."
                $ EmmaX.change_face("sly", Brows="angry")
                $ EmmaX.change_stat("lust", 80, 3)
                ch_e "I imagine I shouldn't, but you know how it can be,"
                $ EmmaX.brows = "normal"
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "-surrounded by attractive co-eds all day long. . ."
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "yourself included. . ."
            "I think it was pretty hot.":
                $ EmmaX.change_face("sly")
                $ EmmaX.change_stat("love", 70, 5)
                $ EmmaX.change_stat("obedience", 50, 10)
                $ EmmaX.change_stat("inhibition", 70, 10)
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "Hmm, well I suppose I can't blame you for that. . ."
            "What do you mean?":
                $ EmmaX.change_face("angry")
                $ EmmaX.change_stat("love", 70, -10)
                $ EmmaX.change_stat("obedience", 50, -5)
                ch_e "I mean how I was. . ."
                $ EmmaX.change_face("surprised")
                $ EmmaX.change_stat("love", 70, 15)
                $ EmmaX.change_stat("obedience", 50, 15)
                $ EmmaX.change_stat("inhibition", 70, 5)
                ch_e "Oh!"
                $ EmmaX.change_face("perplexed")
                ch_e "Yes, obviously it was nothing, just getting some. . ."
                $ EmmaX.eyes = "side"
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "paperwork done. . ."
                $ EmmaX.change_face("sly")
                $ Line = 1
        ch_e "So how did you want to handle this. . . situation?"
        menu:
            extend ""
            "I think I can forget all about it.":
                $ EmmaX.change_face("smile")
                $ EmmaX.change_stat("love", 80, 10)
                $ EmmaX.change_stat("obedience", 60, 10)
                $ EmmaX.change_stat("inhibition", 70, 15)
                ch_e "Thank you, [EmmaX.player_petname]. I appreciate your discretion."
                $ EmmaX.change_face("sly")
                ch_e "Are you {i}certain{/i} there's nothing I could do to thank you?"
            "What solution did you have in mind?":
                $ EmmaX.change_face("sly")
                $ EmmaX.change_stat("love", 70, 5)
                $ EmmaX.change_stat("obedience", 60, 15)
                $ EmmaX.change_stat("inhibition", 70, 15)
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "Oh, I'm sure I could make it worth your while. . ."
            "What situation?":
                if Line != 1:
                    $ EmmaX.change_face("confused")
                    $ EmmaX.change_stat("love", 70, -10)
                    $ EmmaX.change_stat("obedience", 50, -5)
                    ch_e "I mean how I was. . ."
                    $ EmmaX.change_face("surprised")
                    $ EmmaX.change_stat("love", 70, 15)
                    $ EmmaX.change_stat("obedience", 50, 15)
                    $ EmmaX.change_stat("inhibition", 70, 5)
                    ch_e "Oh!"
                    $ EmmaX.change_face("perplexed")
                    ch_e "Yes, obviously it was nothing, just getting some. . ."
                    $ EmmaX.eyes = "side"
                    $ EmmaX.change_stat("lust", 80, 5)
                    ch_e "paperwork done. . ."
                    $ EmmaX.change_face("sly")
                else:
                    $ EmmaX.change_face("angry")
                    $ EmmaX.change_stat("love", 70, -5)
                    $ EmmaX.change_stat("inhibition", 70, 5)
                    ch_e "I do wonder if you're just being dense. . ."
                    $ EmmaX.change_face("sly")
                    ch_e "Still. . ."
        $ Line = 0
        $ multi_action = 0
        $ approval_bonus = 25
        menu:
            extend ""
            "Could you strip?":
                $ EmmaX.change_stat("love", 70, 5)
                $ EmmaX.change_stat("obedience", 50, 10)
                $ EmmaX.change_stat("inhibition", 70, 15)
                ch_e "So you wanted a better view of the action?"
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "I suppose I could accomodate that. . ."
                ch_e "to a point. . ."
                "Ms Frost walks to the door and locks it behind her."
                $ Taboo = 0
                $ EmmaX.Taboo = 0
                if "Historia" in Player.Traits:
                    return 1
                call Group_Strip (EmmaX)
            "Could you just keep going?":
                $ EmmaX.change_stat("love", 70, 10)
                $ EmmaX.change_stat("obedience", 50, 15)
                $ EmmaX.change_stat("inhibition", 70, 15)
                ch_e "Oh, you wanted to watch some more?"
                ch_e "I can't exactly blame you."
                $ EmmaX.eyes = "down"
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "Were you going to put on a show as well?"
                menu:
                    "Yeah!":
                        $ EmmaX.change_stat("love", 70, 5)
                        $ EmmaX.change_stat("inhibition", 70, 10)
                        $ EmmaX.change_stat("lust", 80, 5)
                        ch_e "Excellent."
                        if "Historia" not in Player.Traits:
                            call Seen_First_Peen (EmmaX)
                        "You begin to stroke your cock."
                        $ offhand_action = "jackin"
                    "No, you go ahead.":
                        $ EmmaX.change_face("sad")
                        $ EmmaX.change_stat("love", 70, -10)
                        $ EmmaX.change_stat("obedience", 50, 5)
                        $ EmmaX.change_stat("inhibition", 70, 5)
                        ch_e "Pity."
                $ EmmaX.change_face("sly")
                "[EmmaX.name] walks to the door and locks it behind her."
                $ Taboo = 0
                $ EmmaX.Taboo = 0
                $ primary_action = "masturbation"
                $ girl_offhand_action = "fondle_breasts"
                "She leans back and runs her fingertips along her breasts."
                if "Historia" in Player.Traits:
                    return 1
                call Emma_M_Cycle
            "Could I feel you up?":
                $ EmmaX.change_stat("love", 70, 5)
                $ EmmaX.change_stat("obedience", 50, 10)
                $ EmmaX.change_stat("inhibition", 70, 10)
                ch_e "Hmm, I could use some help . . .around the office. . . "
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "perhaps you have some suggestions?"
                "[EmmaX.name] walks to the door and locks it behind her."
                $ Taboo = 0
                $ EmmaX.Taboo = 0
                if "Historia" in Player.Traits:
                    return 1
                call Emma_FB_Prep
            "Could you give me a hand? [[point to your cock]":
                $ EmmaX.change_stat("love", 70, -5)
                $ EmmaX.change_stat("obedience", 50, 5)
                $ EmmaX.brows = "surprised"
                ch_e "I appreciate boldness, [EmmaX.player_petname], but be a bit more realistic."
                $ EmmaX.brows = "normal"
                $ EmmaX.change_stat("love", 70, 10)
                $ EmmaX.change_stat("inhibition", 70, 5)
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "Perhaps instead I could just offer a little. . . token of my appreciation."
                "[EmmaX.name] walks to the door and locks it behind her."
                $ Taboo = 0
                $ EmmaX.Taboo = 0
                if "Historia" in Player.Traits:
                    return 1
                call Group_Strip (EmmaX)
            "I should just get going then.":
                $ EmmaX.change_face("surprised")
                $ EmmaX.change_stat("obedience", 50, 5)
                ch_e "Oh."
                $ EmmaX.change_face("confused")
                $ EmmaX.change_stat("love", 70, -5)
                $ EmmaX.change_stat("inhibition", 70, -5)
                ch_e "Well, I suppose. . ."
                $ EmmaX.change_face("perplexed")
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "I'll see you. . . in class then. . ."
        $ EmmaX.change_outfit()
        "Afterwards, [EmmaX.name] collects her things and strides toward the door."
        "She turns back with her hand on the door."
        $ EmmaX.change_face("sly")
        ch_e "Oh, and [EmmaX.player_petname]?"
        ch_e "You can just call me \"Emma.\""
        $ EmmaX.name = "Emma"
        $ EmmaX.names.append("Emma")
        $ EmmaX.location = "bg_emma"
        hide Emma_Sprite with easeoutleft
        $ Round = 20 if Round > 20 else Round
        $ multi_action = 1
    return






label Emma_Detention:

    call shift_focus (EmmaX)
    call clear_the_room (EmmaX, 0, 1)
    if "traveling" in Player.recent_history:
        "You enter the room and see [EmmaX.name] waiting for you at the back of the room."
    else:
        "After class, the students file out, and you wait a few minutes until they're all gone."
        "Once the last student leaves, [EmmaX.name] approaches you."
    show blackscreen onlayer black
    $ bg_current = "bg_classroom"
    $ EmmaX.location = "bg_classroom"
    $ EmmaX.change_outfit()
    call set_the_scene
    $ EmmaX.change_face("sly")
    $ EmmaX.ArmPose = 2
    $ Count = 0
    call clear_the_room (EmmaX, 0, 1)
    hide blackscreen onlayer black
    $ Line = 0
    if "detention" in Player.daily_history:
        ch_e "I'm glad you take your. . . education seriously."
    else:

        $ EmmaX.change_face("surprised")
        ch_e "Oh, [EmmaX.player_petname], you really shouldn't skip your detention like that. . ."
    $ Player.Traits.remove("detention")
    $ EmmaX.recent_history.append("detention")
    $ EmmaX.daily_history.append("detention")
    $ EmmaX.change_face("sly")
    $ EmmaX.change_stat("lust", 80, 3)
    ch_e "You've been such a naughty pupil. . ."
    $ EmmaX.ArmPose = 1
    $ EmmaX.change_face("sadside", Brows="normal")
    $ EmmaX.change_stat("lust", 80, 5)
    ch_e "Chasing after those young girls. . ."
    $ EmmaX.change_face("sly")
    $ EmmaX.change_stat("lust", 80, 3)
    if "detention" in EmmaX.history:
        ch_e "How will we deal with it this time?"
    else:

        ch_e "What am I to do with you. . ."
        $ EmmaX.history.append("detention")

    "[EmmaX.name] walks to the door and locks it behind her."
    $ Taboo = 0
    $ EmmaX.Taboo = 0
    $ Player.Traits.append("locked")
    menu:
        extend ""
        "I guess I should focus on my studies.":
            if ApprovalCheck(EmmaX, 900) and "classcaught" in EmmaX.history:
                $ EmmaX.change_face("perplexed")
                $ EmmaX.change_stat("inhibition", 70, -3)
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "Oh. Really? I was thinking of a more. . . recreational punishment."
                menu:
                    extend ""
                    "Kidding, of course, what should we do? [[sex stuff]":
                        $ EmmaX.change_face("sly")
                        $ EmmaX.change_stat("love", 90, 3)
                        $ EmmaX.change_stat("obedience", 60, 5)
                        $ EmmaX.change_stat("inhibition", 70, 5)
                        ch_e "Why do I put up with you?"
                        call Emma_SexMenu
                    "No, you're right, I take my education too lightly.":
                        $ EmmaX.change_stat("love", 80, 1)
                        $ EmmaX.change_stat("inhibition", 70, -2)
                        $ EmmaX.change_stat("lust", 80, 5)
                        ch_e "Oh. Ok. Um. . ."
                        $ EmmaX.change_face("sad")
                        $ EmmaX.change_stat("obedience", 60, 5)
                        $ EmmaX.change_stat("lust", 80, 5)
                        ch_e "I guess we could go over some of the topics from today's class then. . ."
                        $ EmmaX.change_stat("lust", 80, 5)
                        $ Player.XP += 10
            else:

                $ EmmaX.change_face("sad", Mouth="normal")
                $ EmmaX.change_stat("love", 50, 5)
                $ EmmaX.change_stat("love", 80, 5)
                $ EmmaX.change_stat("obedience", 60, 5)
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "Yes. . . Exactly. . ."
                $ EmmaX.change_stat("inhibition", 50, 5)
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "I guess we could go over some of the topics from today's class then. . ."
                $ EmmaX.change_stat("inhibition", 70, 5)
                $ EmmaX.change_stat("lust", 80, 5)
                $ Player.XP += 10
        "I could think of a few things. . . [[sex stuff]":
            if ApprovalCheck(EmmaX, 900) and "classcaught" in EmmaX.history:
                $ EmmaX.change_face("sly")
                $ EmmaX.change_stat("lust", 80, 5)
                $ EmmaX.change_stat("love", 90, 5)
                $ EmmaX.change_stat("obedience", 60, 5)
                $ EmmaX.change_stat("inhibition", 70, 5)
                ch_e "I just bet you can. . ."
                call Emma_SexMenu
            else:

                $ EmmaX.change_face("sad", Mouth="smirk")
                $ EmmaX.change_stat("love", 80, 5)
                $ EmmaX.change_stat("obedience", 60, 5)
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "I'm sure you could. . . but unfortunately this isn't the time for it."
                $ EmmaX.change_stat("inhibition", 50, 5)
                $ EmmaX.change_stat("inhibition", 70, 5)
                $ EmmaX.change_stat("lust", 80, 5)
                ch_e "We'll just have to settle for going over some of the topics from today's class. . ."
                $ EmmaX.change_stat("inhibition", 50, 5)
                $ EmmaX.change_stat("lust", 80, 5)
                $ Player.XP += 10
    $ Round -= 20 if Round > 20 else 0
    ch_e "Ok, I think that's plenty for now. . ."
    ch_e "You wouldn't want to make this a habit. . ."
    $ approval_bonus = 0
    $ EmmaX.change_outfit()
    $ Player.DrainWord("locked",0,0,1)
    return








label Emma_Key:
    call shift_focus (EmmaX)
    call set_the_scene
    $ EmmaX.change_face("bemused")
    $ EmmaX.ArmPose = 2
    ch_e "You've been coming by fairly often. . ."
    ch_e ". . . you might want a key. . ."
    ch_p "Thanks."
    $ EmmaX.ArmPose = 1
    $ Keys.append(EmmaX)
    $ EmmaX.Event[0] = 1
    return






label Emma_Taboo_Talk:


    if "taboo" in EmmaX.history:
        return

    $ EmmaX.change_face("sly")
    if "taboocheck" not in EmmaX.history:
        ch_e "[EmmaX.player_petname], I know that we've had some. . . fun,"
        $ EmmaX.change_face("sly", Eyes="side")
        ch_e "but that was between us, in private."
        $ EmmaX.change_face("sly")
        ch_e "I can't have our trysts become. . . public knowledge."
        ch_e "I am a teacher here, you understand."
        ch_e "You're a student."
        $ EmmaX.change_face("sadside")
        ch_e "It's complicated."
        ch_e "So I'm afraid that we can only. . ."
        $ EmmaX.change_face("sad")
        ch_e ". . .interact, when we're alone."
        ch_e "Do you understand?"
    else:
        ch_e "I believe I made clear why I couldn't do anything like that in public. . ."

    $ Line = 1
    while Line >= 1:
        menu:
            extend ""
            "Yeah, I suppose.":
                $ EmmaX.change_face("smile")
                if "taboocheck" in EmmaX.history:
                    pass
                elif Line != 4:

                    $ EmmaX.change_stat("love", 60, 10)
                    $ EmmaX.change_stat("love", 70, 10)
                    $ EmmaX.change_stat("love", 90, 10)
                    $ EmmaX.change_stat("obedience", 60, 5)
                    $ EmmaX.change_stat("inhibition", 70, 5)
                else:
                    $ EmmaX.change_stat("love", 60, 10)
                    $ EmmaX.change_stat("love", 90, 10)

                ch_e "Thank you for your discretion."
                $ EmmaX.change_face("sly")
                if ApprovalCheck(EmmaX, 2000) and "taboocheck" in EmmaX.history:
                    ch_e "Although. . . I suppose we could make an exception. . ."
                    $ EmmaX.change_stat("inhibition", 90, 10)
                    $ Line = -1
                else:
                    ch_e "I do hope that we can still find some time to meet up."
                    $ Line = 0

            "I don't care who sees us." if Line != 2 and Line != 4:
                if "taboocheck" in EmmaX.history:
                    ch_e "I'm aware. . ."
                    if ApprovalCheck(EmmaX, 500, "I"):
                        $ EmmaX.change_face("sly")
                        ch_e "Frankly, I don't either."
                        $ EmmaX.change_face("angry", Eyes="side")
                        ch_e "It's not about that though, if we get caught, I get fired."
                        $ EmmaX.change_face("angry")
                        ch_e "If I get fired, then I can't stay here."
                        $ EmmaX.change_face("sly")
                        ch_e "So that really isn't an option."
                    else:
                        $ EmmaX.change_face("confused", 1)
                        ch_e "You might not, but I have a reputation to maintain."
                elif ApprovalCheck(EmmaX, 500, "I"):
                    $ EmmaX.change_stat("lust", 80, 5)
                    $ EmmaX.change_stat("inhibition", 70, 5)
                    $ EmmaX.change_face("sly")
                    ch_e "Frankly, I don't either."
                    $ EmmaX.change_face("angry", Eyes="side")
                    ch_e "It's not about that though, if we get caught, I get fired."
                    $ EmmaX.change_face("angry")
                    $ EmmaX.change_stat("love", 90, 10)
                    $ EmmaX.change_stat("obedience", 60, 10)
                    ch_e "If I get fired, then I can't stay here."
                    $ EmmaX.change_face("sly")
                    ch_e "So that really isn't an option."
                else:
                    $ EmmaX.change_stat("lust", 80, 5)
                    $ EmmaX.change_stat("love", 90, 10)
                    $ EmmaX.change_stat("obedience", 60, 10)
                    $ EmmaX.change_face("confused", 1)
                    ch_e "Well you might not, but I have a reputation to maintain."
                $ EmmaX.change_face("sly")
                ch_e "So can you understand why we must be discrete?"
                $ Line = 4 if Line != 1 else 2

            "Couldn't you just mindwipe anyone who sees?" if Line != 3 and Line != 4:
                if "taboocheck" in EmmaX.history:
                    ch_e "Yes, we've been over why that wouldn't exactly be an option."
                else:
                    if ApprovalCheck(EmmaX, 500, "I"):
                        $ EmmaX.change_face("sly")
                        $ EmmaX.change_stat("lust", 80, 5)
                        $ EmmaX.change_stat("love", 80, 5)
                        $ EmmaX.change_stat("obedience", 60, 5)
                        $ EmmaX.change_stat("inhibition", 70, 5)
                        ch_e "You must have read my mind."
                    elif ApprovalCheck(EmmaX, 800, "LO"):
                        $ EmmaX.change_face("sly",1)
                        $ EmmaX.change_stat("lust", 80, 5)
                        $ EmmaX.change_stat("love", 90, 10)
                        $ EmmaX.change_stat("obedience", 60, 10)
                        $ EmmaX.change_stat("inhibition", 70, 5)
                        ch_e "Oh, you naughty boy."
                    else:
                        $ EmmaX.change_face("surprised",1)
                        $ EmmaX.change_stat("lust", 80, 5)
                        $ EmmaX.change_stat("obedience", 60, 10)
                        $ EmmaX.change_stat("inhibition", 50, 15)
                        $ EmmaX.change_stat("inhibition", 70, 10)
                        ch_e "What? I would never!"
                    $ EmmaX.change_face("angry",Eyes="side")
                    ch_e "Either way though, that's not really an option either."
                ch_e "I can't muck about with the students' minds too much without Charles catching on."
                ch_e "Casually mindwiping students certainly wouldn't pass unnoticed."
                if EmmaX in Rules:

                    ch_p "But Xavier is off the board now. . ."
                    $ EmmaX.change_face("sly")
                    ch_e "I suppose that's true. . ."
                    ch_e "A little helpful editing might not hurt. . ."
                    $ Line = -1
                else:
                    $ EmmaX.change_face("confused",Mouth="normal")
                    ch_e "So are we on the same page here?"
                    $ Line = 4 if Line != 1 else 3

            "I don't care, let's do it." if Line == 4:
                $ Line = 0
                if ApprovalCheck(EmmaX, 2000):
                    $ EmmaX.change_face("surprised", Eyes="side")
                    $ EmmaX.change_stat("lust", 80, 5)
                    $ EmmaX.change_stat("inhibition", 50, 15)
                    $ EmmaX.change_stat("inhibition", 70, 10)
                    ch_e "Oh, I will get in so much trouble for this. . ."
                    $ EmmaX.change_stat("love", 90, 5)
                    $ EmmaX.change_stat("obedience", 60, 15)
                    $ EmmaX.change_face("sly")
                    ch_e "but you're worth it."
                    $ Line = -1
                elif ApprovalCheck(EmmaX, 800, "I"):
                    $ EmmaX.change_face("surprised", Eyes="side")
                    $ EmmaX.change_stat("lust", 80, 5)
                    $ EmmaX.change_stat("obedience", 60, 15)
                    ch_e "Oh, I will get in so much trouble for this. . ."
                    $ EmmaX.change_face("sly")
                    ch_e "but it will be so much fun."
                    $ Line = -1
                elif "taboocheck" in EmmaX.history:
                    $ EmmaX.change_face("angry")
                    $ EmmaX.change_stat("love", 90, -5)
                    $ EmmaX.change_stat("obedience", 60, -5)
                    ch_e "You're going to have to respect my boundaries on this one."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")
                    $ renpy.pop_call()
                else:
                    $ EmmaX.change_face("angry")
                    $ EmmaX.change_stat("love", 90, -5)
                    $ EmmaX.change_stat("obedience", 60, -5)
                    $ EmmaX.change_stat("inhibition", 70, 10)
                    ch_e "Well that's just too bad."
                    ch_e "If you can't respect such a simple limitation, then I believe we're done for now."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")
                    $ renpy.pop_call()


    if "taboocheck" not in EmmaX.history:
        $ EmmaX.history.append("taboocheck")
    if Line == -1:

        $ EmmaX.history.append("taboo")
        $ EmmaX.history.remove("taboocheck")
    $ Line = 0
    return





label Emma_ThreeCheck(Pass=3, Quest=[], Girl=0, BO=[]):

    if EmmaX.SEXP <= 30:
        $ EmmaX.change_face("confused")
        ch_e "[EmmaX.player_petname], I barely put up with you, don't try to bring other girls into this."
        return
    if "three" in EmmaX.history:
        return

    $ Line = 0
    $ BO = all_Girls[:]
    $ BO.remove(EmmaX)
    while BO:
        if "saw with " + BO[0].Tag in EmmaX.Traits:
            $ Line = "I saw you with " + BO[0].Tag
        if BO[0].location == bg_current:
            $ Girl = BO[0]
            $ BO = [1]
        $ BO.remove(BO[0])

    if not Girl or Girl not in all_Girls:
        $ Quest.append(2)
        if Line:
            $ EmmaX.change_face("angry", Eyes = "side")
            if Line:
                ch_e "[Line] earlier. I'm not sure how I feel about that."
            $ Line = 0
            if "sleeptime" in EmmaX.history:

                ch_e "I saw you considering having me sleep over with that. . . girl. . ."
                $ EmmaX.history.remove("sleeptime")

    if "threecheck" not in EmmaX.history:
        $ EmmaX.change_face("bemused", Eyes = "side")
        "[EmmaX.name] moves close to you and whispers. . ."
        if ApprovalCheck(EmmaX, 900, "L"):
            ch_e "[EmmaX.player_petname], I really do. . . care for you. . ."
        elif ApprovalCheck(EmmaX, 800, "L"):
            ch_e "[EmmaX.player_petname], I do think you're. . . interesting. . ."
        elif ApprovalCheck(EmmaX, 500, "O"):
            ch_e "[EmmaX.player_petname], there is something. . . compelling about you. . ."
        elif ApprovalCheck(EmmaX, 500, "I"):
            ch_e "[EmmaX.player_petname], you know that I'm. . . flexible,"
        else:
            ch_e "[EmmaX.player_petname], I don't know what this even is yet, but. . ."
        ch_e "I'm a teacher at this school, and I can't exactly be caught forming some sort of. . ."
        ch_e "harem with the students."
        ch_e "Just you and I would be scandalous, but multiple students?"
        ch_e "That could be a disaster."
    else:
        ch_e "I already explained why I couldn't do this around other girls."
    while Pass > 0:
        menu:
            extend ""
            "Yeah, I suppose.":
                $ EmmaX.change_face("smile")
                if "threecheck" not in EmmaX.history:
                    $ EmmaX.change_stat("love", 60, 10)
                    $ EmmaX.change_stat("love", 90, 10)

                ch_e "Thank you for not insisting."
                $ EmmaX.change_face("sly")
                if Pass == 1 and ApprovalCheck(EmmaX, 2000):
                    ch_e "though I suppose. . . perhaps I could make an exception. . ."
                    $ Pass = 0
                else:
                    ch_e "I do hope that we can still find some. . . personal time?"
                    $ Pass = -1

            "But she's cool with it." if 2 not in Quest:


                $ Quest.append(2)
                if Girl.location == bg_current:
                    $ Pass -= 1
                    if "poly Emma" in Girl.Traits:

                        if Girl == RogueX:
                            ch_r "Yeah, like I said, ready when you are."
                        elif Girl == KittyX:
                            ch_k "Yup, sounds fun."
                        elif Girl == LauraX:
                            ch_l "Yeah, I'm in."
                    else:
                        $ Girl.Traits.append("poly Emma")
                        if ApprovalCheck(Girl, 1500) and Girl.LikeEmma >= 800:
                            if Girl == RogueX:
                                ch_r "I really am."
                            elif Girl == KittyX:
                                ch_k "Yeah, you bet."
                            elif Girl == LauraX:
                                ch_l "Sure."
                        elif ApprovalCheck(Girl, 1500) and Girl.LikeEmma >= 600:
                            if Girl == RogueX:
                                ch_r "Yeah, you'll do."
                            elif Girl == KittyX:
                                ch_k "Yeah, you're ok."
                            elif Girl == LauraX:
                                ch_l "Yeah, it's cool."
                        elif ApprovalCheck(Girl, 2000):
                            if Girl == RogueX:
                                ch_r "You and I get along like cats and bitches. . ."
                                ch_r "but I do want to make him happy."
                            elif Girl == KittyX:
                                ch_k "I don't like you much, but I do want him to be happy."
                            elif Girl == LauraX:
                                ch_l "Ugh, yeah. . ."
                                ch_l "I mean this guy seems to like you."
                        elif ApprovalCheck(Girl, 500) and Girl.LikeEmma >= 800:
                            if Girl == RogueX:
                                ch_r "This guy I could take or leave, but you clean up real nice."
                            elif Girl == KittyX:
                                ch_k "Well, I don't know about this guy, but. . . you're pretty."
                            elif Girl == LauraX:
                                ch_l "Hey, even without [Player.name] here, you're a catch."
                        else:
                            if Girl == RogueX:
                                ch_r "I said no such thing!"
                            elif Girl == KittyX:
                                ch_k "I didn't say anything like that!"
                            elif Girl == LauraX:
                                ch_l "Say what now?"
                            $ Girl.Traits.remove("poly Emma")
                            $ Pass += 1
                if EmmaX.GirlLikeCheck(Girl) >= 700:
                    ch_e "And you're quite fetching yourself dear. . ."
                    $ Pass -= 1 if Pass > 0 else 0
                elif EmmaX.GirlLikeCheck(Girl) >= 500:
                    ch_e "And you're. . . acceptable. . ."
                else:
                    ch_e "And that's just lovely, really. . ."
                    $ Pass += 1
                ch_e "But I'm afraid that any sort of dalliance would be an issue."


            "Xavier doesn't care." if Taboo and EmmaX in Rules and 3 not in Quest:
                $ Quest.append(3)
                ch_e "Well, that may be, but it could still get out."
                $ Pass -= 1

            "Xavier won't find out here." if not Taboo and 3 not in Quest:
                $ Quest.append(3)
                ch_e "Well, that may be, but it could still get out."
                $ Pass -= 1

            "I don't care, let's do this." if Quest:
                if ApprovalCheck(EmmaX, 2000) and Pass <= 2:
                    $ EmmaX.change_face("surprised", Eyes="side")
                    $ EmmaX.change_stat("lust", 80, 5)
                    $ EmmaX.change_stat("inhibition", 50, 15)
                    $ EmmaX.change_stat("inhibition", 70, 10)
                    $ EmmaX.change_stat("love", 90, 5)
                    $ EmmaX.change_stat("obedience", 60, 15)
                    ch_e "Oh, I could get in so much trouble for this. . ."
                    $ EmmaX.change_face("sly")
                    ch_e "but you're worth it."
                    $ Pass = 0
                elif ApprovalCheck(EmmaX, 800, "I") and Pass <= 2:
                    $ EmmaX.change_face("surprised", Eyes="side")
                    $ EmmaX.change_stat("lust", 80, 5)
                    $ EmmaX.change_stat("obedience", 60, 15)
                    ch_e "Oh, I could get in so much trouble for this. . ."
                    $ EmmaX.change_face("sly")
                    ch_e "but it will be so much fun."
                    $ Pass = 0
                elif "threecheck" not in EmmaX.history:
                    $ EmmaX.change_face("angry")
                    $ EmmaX.change_stat("love", 90, -5)
                    $ EmmaX.change_stat("obedience", 60, -5)
                    ch_e "You're going to have to learn to take \"no\" for an answer on this one."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")
                    $ Pass = -1
                else:
                    $ EmmaX.change_face("angry")
                    $ EmmaX.change_stat("love", 90, -5)
                    $ EmmaX.change_stat("obedience", 60, -5)
                    $ EmmaX.change_stat("inhibition", 70, 10)
                    ch_e "Well that's just too bad."
                    ch_e "If you can't respect such a simple limitation, then I believe we're done for now."
                    $ EmmaX.recent_history.append("angry")
                    $ EmmaX.daily_history.append("angry")
                    $ Pass = -1

    if "threecheck" not in EmmaX.history:
        $ EmmaX.history.append("threecheck")
    if Pass == -1:

        $ renpy.pop_call()
    else:

        $ EmmaX.history.append("three")
        $ EmmaX.history.remove("threecheck")
        if Girl in all_Girls:
            if "poly " + Girl.Tag not in EmmaX.Traits:
                $ EmmaX.Traits.append("poly " + Girl.Tag)
            $ EmmaX.recent_history.append("noticed " + Girl.Tag)
            $ Girl.recent_history.append("noticed Emma")
    return






label Emma_BF:
    $ EmmaX.DrainWord("asked meet")
    call shift_focus (EmmaX)
    if EmmaX.location != bg_current:
        $ EmmaX.location = bg_current
        if EmmaX not in Party:
            "[EmmaX.name] approaches you and asks if the two of you can talk."
        else:
            "[EmmaX.name] turns towards you and asks if the two of you can talk."

    call set_the_scene (0)
    call Display_Girl (EmmaX)
    "You can tell she's a bit uncomfortable about whatever she has to say."
    call Taboo_Level
    call clear_the_room (EmmaX)
    $ EmmaX.daily_history.append("relationship")
    $ EmmaX.change_face("bemused", 1)

    ch_e "[EmmaX.player_petname], we've been. . . enjoying ourselves for a while now."
    ch_e ". . ."
    $ EmmaX.eyes = "sexy"
    menu:
        ch_e "You have been enjoying yourself?"
        "Yeah. And it's been amazing.":
            $ EmmaX.change_stat("love", 200, 20)
        "Yeah, I guess":
            $ EmmaX.change_stat("love", 200, 10)
        "Uhm. . .maybe?":
            $ EmmaX.change_stat("love", 200, -10)
            $ EmmaX.change_stat("obedience", 200, 30)
    if EmmaX.SEXP >= 10:
        ch_e "I think we've been engaging in some rather inappropriate behavior. . ."
    if EmmaX.SEXP >= 15:
        ch_e "-for a student and teacher, at least. . ."
    if len(Player.Harem) >= 2:
        ch_e "I understand that this isn't an exclusive deal for you. . ."
    elif Player.Harem:
        ch_e "I understand that you've been dating [Player.Harem[0].name]. . ."

    if not EmmaX.Event[5]:
        ch_e "So, that being the case. . ."
        ch_e "I was wondering if you'd like to make this a bit more official."
        ch_e "If I could perhaps consider you my. . ."
        ch_e "Boyfriend?"
        ch_e "-or something to that effect."
    elif Player.Harem:
        ch_e ". . . but I would still like to also consider you my boyfriend as well."
    else:
        ch_e "I don't know why I put up with you, but I do still want to be your girlfriend."
    $ EmmaX.Event[5] += 1
    menu:
        extend ""
        "Are you kidding? I'd love to!":
            $ EmmaX.change_stat("love", 200, 25)
            "[EmmaX.name] wraps her arms around you and starts kissing you passionately."
            $ EmmaX.change_face("kiss")
            call Emma_Kissing_Launch ("kiss")
            $ EmmaX.action_counter["kiss"] += 1
        "Uhm, okay.":
            $ EmmaX.brows = "confused"
            "[EmmaX.name] seems a little put off by how casually you’re taking all this."
        "I'm with someone else now." if Player.Harem:
            $ EmmaX.change_face("sad",1)
            ch_e "I understand. I thought that perhaps you could go out with me as well?"
            menu:
                extend ""
                "Yes. Absolutely." if "EmmaYes" in Player.Traits:
                    $ EmmaX.change_stat("love", 200, 30)
                    "[EmmaX.name] wraps her arms around you and starts kissing you passionately."
                    $ EmmaX.change_face("kiss")
                    call Emma_Kissing_Launch ("kiss")
                    $ EmmaX.action_counter["kiss"] += 1
                "She wouldn't understand." if len(Player.Harem) == 1:
                    $ Line = "no"
                "They wouldn't be cool with that." if len(Player.Harem) > 1:
                    $ Line = "no"
                "I'm sorry, but. . . no." if EmmaX.Event[5] != 20:
                    $ Line = "no"
                "No way.":
                    jump Emma_BF_Jerk
            if Line == "no":
                $ EmmaX.change_stat("love", 200, -10)
                ch_e "Well. . ."
                ch_e "I suppose I understand."
                $ EmmaX.Event[5] = 20
                call Remove_Girl (EmmaX)
                $ Line = 0
                return
        "Not really.":
            jump Emma_BF_Jerk

    if "Historia" not in Player.Traits:
        $ Player.Harem.append(EmmaX)
        if "EmmaYes" in Player.Traits:
            $ Player.Traits.remove("EmmaYes")
    $ EmmaX.player_petnames.append("boyfriend")
    $ EmmaX.change_face("sexy")
    ch_e "So then. . . how would you like to celebrate?"
    if "Historia" in Player.Traits:
        return 1
    $ approval_bonus = 10
    $ Player.AddWord(1,"interruption")
    call Emma_SexMenu
    $ approval_bonus = 0
    return

label Emma_BF_Jerk:
    $ EmmaX.change_face("angry", 1)
    ch_e "Well! Suit yourself."
    $ EmmaX.change_stat("obedience", 50, 40)
    if EmmaX.Event[5] != 20:
        $ EmmaX.change_stat("obedience", 200, (20* EmmaX.Event[5]))
    if 20 > EmmaX.Event[5] >= 3:
        $ EmmaX.change_face("sad")
        ch_e "You know, I'm tired of caring what you think about the matter."
        ch_e "I'm doing to consider us a couple whether you approve or not."
        ch_e "And with that, adieu."
        if "Historia" in Player.Traits:
            return 1
        $ EmmaX.player_petnames.append("boyfriend")
        $ Achievements.append("I am not your Boyfriend!")
        $ bg_current = "bg_player"
        call Remove_Girl (EmmaX)
        call set_the_scene
        $ renpy.pop_call()
        jump Player_Room
    if EmmaX.Event[5] > 1:
        ch_e "It was such a mistake asking you again. You still need to mature."
    if EmmaX.Event[5] != 20:
        $ EmmaX.change_stat("love", 200, -(50* EmmaX.Event[5]))
    else:
        $ EmmaX.change_stat("love", 200, -50)
    ch_e "Get away from me."
    if "Historia" in Player.Traits:
        return
    $ bg_current = "bg_player"
    call Remove_Girl (EmmaX)
    $ renpy.pop_call()
    jump Player_Room


label Emma_Love(Shipping=[], Shipshape=0, BO=[]):
    $ EmmaX.DrainWord("asked meet")

    $ BO = all_Girls[:]
    $ BO.remove(EmmaX)
    while BO:
        if ApprovalCheck(BO[0], 1200, "LO"):
            $ Shipping.append(BO[0])
        $ BO.remove(BO[0])
    $ Shipshape = len(Shipping)

    if EmmaX.location == bg_current or EmmaX in Party:
        "[EmmaX.name] glances over at you with an apprising look on her face."
    else:
        "[EmmaX.name] turns a corner and notices you."
    if bg_current != "bg_emma" and bg_current != "bg_player":
        "With little word, she takes your hand and pulls you back to her room."
        $ bg_current = "bg_emma"
    $ EmmaX.location = bg_current
    call set_the_scene
    call clear_the_room (EmmaX)
    call Taboo_Level
    $ EmmaX.daily_history.append("relationship")

    $ EmmaX.change_face("sexy",Eyes="side")
    ch_e "As you are aware, this. . . situation has been going for a while now."
    ch_e "It's been very. . . comfortable for me."
    $ EmmaX.change_face("sexy")
    ch_e "I have enjoyed your company. . . is what I'm trying to say."
    menu:
        extend ""
        "It's more than just company, we're together in this.":
            $ EmmaX.change_face("smile",1)
            $ EmmaX.change_stat("love", 200, 10)
            $ EmmaX.change_stat("inhibition", 90, 5)
            ch_e "Yes!"
            ch_e "Yes, we certainly are more than that."
            $ EmmaX.change_face("sly")
            ch_e "You must have read my mind."
        "I've enjoyed it a lot too.":
            $ EmmaX.change_face("sly")
            $ EmmaX.change_stat("love", 200, 5)
            $ EmmaX.change_stat("obedience", 90, 2)
            ch_e "Yes, I imagine you have."
            ch_e "Perhaps it was more than that though. . ."
        "Yeah, it's been fun.":
            $ EmmaX.change_face("confused")
            $ EmmaX.change_stat("obedience", 90, 5)
            ch_e "Yes, \"fun.\""
            $ EmmaX.change_face("angry",Eyes="side")
            ch_e "It is fun, but I was thinking. . ."
            $ EmmaX.change_face("sly")
        "Oh, ok.":
            $ EmmaX.change_face("confused",Eyes="side")
            ch_e "Um, yes. . ."
            ch_e ". . ."
            $ EmmaX.change_face("confused")
            ch_e "I'm not sure I was clear. . ."
        "Yeah, you're a good ride.":
            $ EmmaX.change_face("angry")
            if not ApprovalCheck(EmmaX, 1600):
                $ EmmaX.change_stat("obedience", 90, -5)
                $ EmmaX.change_stat("inhibition", 90, -5)
                $ EmmaX.eyes="side"
                ch_e "Never mind, this was a bad idea."
                jump Emma_Love_End
            ch_e "Such impertinence!"
            if ApprovalCheck(EmmaX, 1000, "OI"):
                $ EmmaX.change_face("sly",2)
                $ EmmaX.change_stat("obedience", 90, 10)
                $ EmmaX.change_stat("inhibition", 90, 5)
                $ EmmaX.change_stat("lust", 70, 5)
                ch_e "I am though, yes."
                $ EmmaX.blushing = 1
            else:
                $ EmmaX.change_face("sexy")
                $ EmmaX.change_stat("obedience", 90, 5)
                $ EmmaX.change_stat("inhibition", 90, 5)
                ch_e "I suppose that's part of your charm though."

    ch_e "I certainly do care for you. . ."
    ch_e "Perhaps more than I have for anyone else in a long time."
    if ApprovalCheck(EmmaX, 1600):
        $ EmmaX.change_face("sexy",Eyes="side")
        ch_e "Perhaps more than I ever have."
    ch_e ". . ."
    ch_e "What I'm trying to say is. . ."
    $ EmmaX.change_face("sexy",Brows="sad")
    ch_e "I love you."
    menu:
        extend ""
        "I love you too, [EmmaX.petname]!":
            $ EmmaX.change_face("smile",2)
            $ EmmaX.change_stat("love", 200, 20)
            $ EmmaX.change_stat("inhibition", 90, 10)
            ch_e "I dearly hoped that you did!"
            $ EmmaX.player_petnames.append("lover")
            jump Emma_Love_End
        "Wow! That's cool.":
            $ EmmaX.change_face("confused")
            $ EmmaX.change_stat("love", 200, 5)
            ch_e "Cool?"
            ch_e "Don't you have anything else you'd like to say to me?"
            $ EmmaX.change_face("sadside",2)
        "Oh, ok.":
            $ EmmaX.change_face("confused",2)
            $ EmmaX.change_stat("obedience", 90, 5)
            $ EmmaX.change_stat("inhibition", 90, -5)
            ch_e "Ok?"
            $ EmmaX.change_face("angry")
            ch_e "Is that all the response you have for me?"
        "Ha!":
            $ EmmaX.change_face("surprised",2)
            $ EmmaX.change_stat("love", 200, -5)
            $ EmmaX.change_stat("obedience", 90, 10)
            $ EmmaX.change_stat("inhibition", 90, -5)
            ch_e "!"
            $ EmmaX.change_face("angry",2)
            ch_e "Well that's hardly the response I expected."
    ch_e "I would hope that you also love me. . ."
    menu:
        extend ""
        "Oh! Yes, of course I love you, [EmmaX.petname]!":
            $ EmmaX.nameCheck()
            $ EmmaX.change_face("smile",2)
            $ EmmaX.change_stat("love", 90, 15)
            $ EmmaX.change_stat("obedience", 90, 2)
            ch_e "I dearly hoped that you did!"
            $ EmmaX.player_petnames.append("lover")
            jump Emma_Love_End
        "Oh. Oooooh! Yeah, sure.":
            if ApprovalCheck(EmmaX, 1200, "OI"):
                $ EmmaX.change_face("sly",1)
                $ EmmaX.change_stat("love", 200, 5)
                $ EmmaX.change_stat("obedience", 90, 10)
            if ApprovalCheck(EmmaX, 1200, "OI"):
                $ EmmaX.change_face("sly",1,Brows="angry")
                $ EmmaX.change_stat("love", 200, 5)
                $ EmmaX.change_stat("obedience", 90, 5)
                $ EmmaX.change_stat("inhibition", 90, -5)
            ch_e "I'm glad to see that you caught up with the situation."
        "Oh. That's awkward.":
            $ EmmaX.change_face("angry",2)
            $ EmmaX.change_stat("love", 200, -15)
            $ EmmaX.change_stat("obedience", 90, 15)
            $ EmmaX.change_stat("inhibition", 90, -10)
            ch_e "Awkward?!"
            ch_e "This situation is about to become considerably more \"awkward.\""
            $ EmmaX.blushing = 1
            $ Line = "angry"

    ch_e "I'm giving you one last chance here."
    ch_e "This is not a time for fooling around."
    ch_e "Do you love me, or not?"
    menu:
        extend ""
        "Yes, of course I love you, [EmmaX.petname]!":
            $ EmmaX.nameCheck()
            $ EmmaX.change_face("sly",2)
            $ EmmaX.change_stat("love", 90, 5)
            $ EmmaX.change_stat("obedience", 90, 15)
            $ EmmaX.change_stat("inhibition", 90, 5)
            ch_e "Took you long enough to get there."
            $ EmmaX.player_petnames.append("lover")
            jump Emma_Love_End
        "I can't really say yet.":
            if Line != "angry" or ApprovalCheck(EmmaX, 800, "OI"):
                $ EmmaX.change_face("sadside")
                $ EmmaX.change_stat("obedience", 90, 5)
            else:
                $ EmmaX.change_face("angry")
                $ EmmaX.change_stat("love", 200, -5)
                $ EmmaX.change_stat("obedience", 90, 5)
                $ EmmaX.change_stat("inhibition", 90, -5)
            ch_e "Oh."
        "No.":
            if Line == "angry" or not ApprovalCheck(EmmaX, 800, "OI"):
                $ EmmaX.change_face("angry")
                $ EmmaX.change_stat("love", 200, -10)
                $ EmmaX.change_stat("obedience", 90, 10)
                $ EmmaX.change_stat("inhibition", 90, -5)
            else:
                $ EmmaX.change_face("sadside")
                $ EmmaX.change_stat("love", 200, -10)
                $ EmmaX.change_stat("obedience", 90, 10)
                $ EmmaX.change_stat("inhibition", 90, -5)
            ch_e "Oh."

    ch_e "Is it because of someone else?"
    $ Line = 0
    menu:
        extend ""
        "Yes, it's [RogueX.name]." if RogueX in Shipping and Shipshape < 3:
            $ Line = RogueX
        "Yes, it's [KittyX.name]." if KittyX in Shipping and Shipshape < 3:
            $ Line = KittyX
        "Yes, it's [LauraX.name]." if LauraX in Shipping and Shipshape < 3:
            $ Line = LauraX
        "Yes, it's the others" if Shipshape > 1:
            $ EmmaX.change_stat("obedience", 90, 15)
            $ EmmaX.change_stat("inhibition", 90, 5)
            $ EmmaX.change_stat("lust", 90, 5)
            ch_e "I suppose I can't blame you there."
        "There's nobody else.":
            $ EmmaX.change_face("sadside")
            $ EmmaX.change_stat("love", 200, -15)
            $ EmmaX.change_stat("obedience", 90, 15)
            $ EmmaX.change_stat("inhibition", 90, 5)
            if ApprovalCheck(EmmaX, 1000, "OI"):
                ch_e "Hmmm. . . well I suppose I can take solace in that."
            else:
                ch_e "I see."
        "It's a \"you\" problem.":
            $ EmmaX.change_face("angry")
            $ EmmaX.change_stat("love", 200, -25)
            $ EmmaX.change_stat("obedience", 90, 15)
            ch_e "Oh is it now?"
            $ EmmaX.change_stat("love", 200, -10)
            ch_e "I can think of a great many ways to make this a \"you\" problem."
            $ EmmaX.recent_history.append("angry")
            $ EmmaX.daily_history.append("angry")
    if Line:

        if EmmaX.GirlLikeCheck(Line) >= 800:
            $ EmmaX.change_stat("love", 200, 5)
            $ EmmaX.change_stat("obedience", 90, 20)
            $ EmmaX.change_stat("inhibition", 90, 5)
            $ EmmaX.change_stat("lust", 90, 5)
            ch_e "Yes, she is lovely."
        else:
            $ EmmaX.change_face("angry",Eyes="side")
            $ EmmaX.change_stat("love", 200, -5)
            $ EmmaX.change_stat("obedience", 90, 20)
            ch_e "That cow!"
            $ EmmaX.recent_history.append("angry")
            $ EmmaX.GLG(Line,800,-50,1)
    ch_e "I suppose I'll just have to let this go."
    ch_e "I'll. . . see you in a bit."
    ch_e "I need some time to consider this."


label Emma_Love_End:
    if "lover" not in EmmaX.player_petnames:
        hide Emma_Sprite with easeoutright
        call Remove_Girl (EmmaX)
        $ EmmaX.location = "hold"
        return

    "[EmmaX.name] pulls closer to you and snuggles into your arms."
    $ EmmaX.change_stat("love", 200, 25)
    $ EmmaX.change_stat("lust", 90, 5)
    ch_e "So. . . now that we have some time together. . ."
    $ EmmaX.change_stat("lust", 90, 10)

    if not EmmaX.action_counter["sex"]:
        ch_e "I think we've certainly waited long enough. . ."
    else:
        ch_e "Whatever do you intend to do about it?"
    $ Player.AddWord(1,"interruption")
    menu:
        extend ""
        "Yeah, let's do this. . . [[have sex]":
            $ EmmaX.change_stat("inhibition", 30, 20)
            $ EmmaX.change_stat("obedience", 70, 10)
            ch_e "Hmm. . ."
            call Emma_SexAct ("sex")
        "I have something else in mind. . .[[choose another activity]":
            $ EmmaX.brows = "confused"
            $ EmmaX.change_stat("obedience", 70, 25)
            ch_e "Something like. . ."
            $ approval_bonus = 20
            call Emma_SexMenu
    return

label Emma_Love_Redux:

    $ Line = 0
    $ EmmaX.daily_history.append("relationship")
    if EmmaX.Event[6] >= 25:

        ch_p "I hope you've forgiven me, I still love you."
        $ EmmaX.change_stat("love", 95, 10)
        if ApprovalCheck(EmmaX, 950, "L"):
            $ Line = "love"
        else:
            $ EmmaX.change_face("angry")
            ch_e "I don't believe you're sufficiently contrite, [EmmaX.player_petname]."
            $ EmmaX.eyes="side"
            ch_e ". . ."
            $ EmmaX.change_face("angry",Mouth="lipbite")
            ch_e "I didn't tell you to stop."
    else:
        ch_p "Remember when I told you that I didn't love you?"
        $ EmmaX.change_face("perplexed",1)
        ch_e ". . ."
        $ EmmaX.change_face("angry", Eyes="side")
        ch_e "I believe I do remember something to that effect, yes."
    if Line != "love":
        menu:
            extend ""
            "I'm sorry, I didn't mean it.":
                $ EmmaX.eyes = "surprised"
                ch_e "Oh? So you do love me?"
                ch_p "Yeah. I mean, yes, I love you, [EmmaX.name]."
                $ EmmaX.change_stat("love", 200, 10)
                if ApprovalCheck(EmmaX, 950, "L"):
                    $ Line = "love"
                else:
                    $ EmmaX.change_face("sadside")
                    ch_e "I'm not sure that I still do. . ."
            "I've changed my mind, so. . .":
                if ApprovalCheck(EmmaX, 950, "L"):
                    $ Line = "love"
                    $ EmmaX.eyes = "surprised"
                    ch_e "Oh?"
                else:
                    $ EmmaX.mouth = "sad"
                    ch_e "Oh, you've changed your mind. Lovely."
                    $ EmmaX.change_stat("inhibition", 90, 10)
                    $ EmmaX.change_face("sadside")
                    ch_e "Perhaps I have too. . ."
            "Um, never mind.":
                $ EmmaX.change_stat("love", 200, -30)
                $ EmmaX.change_stat("obedience", 50, 10)
                $ EmmaX.change_face("angry")
                ch_e "Don't you dare."
                $ EmmaX.recent_history.append("angry")
    if Line == "love":
        $ EmmaX.change_stat("love", 200, 40)
        $ EmmaX.change_stat("obedience", 90, 10)
        $ EmmaX.change_stat("inhibition", 90, 10)
        $ EmmaX.change_face("smile")
        ch_e "I couldn't be happier!"
        ch_e "I love you too, [EmmaX.player_petname]!"
        if EmmaX.Event[6] < 25:
            $ EmmaX.change_face("sly")
            "She grabs the back of your head and pulls you close."
            ch_e "You shouldn't have kept me waiting."
        $ EmmaX.player_petnames.append("lover")
    $ EmmaX.Event[6] = 25
    return



label Emma_Sub:
    $ EmmaX.DrainWord("asked meet")
    call shift_focus (EmmaX)

    if EmmaX.location != bg_current and EmmaX not in Party:
        "[EmmaX.name] shows up and says she needs to talk to you."
    else:
        "[EmmaX.name] approaches you, looking to talk."
    $ EmmaX.location = bg_current
    call set_the_scene
    call clear_the_room (EmmaX)
    call Taboo_Level
    $ EmmaX.daily_history.append("relationship")
    $ EmmaX.change_face("bemused", 1)

    $ Line = 0
    ch_e "I've been noticing, you have a sort of"
    ch_e ". . . commanding air about you, [EmmaX.player_petname]."
    menu:
        extend ""
        "I guess. That's just kind of what comes naturally for me.":
            $ EmmaX.change_stat("obedience", 200, 10)
            $ EmmaX.change_stat("inhibition", 50, 5)
        "Sorry. I didn't mean to come off like that.":
            $ EmmaX.change_face("startled", 2)
            $ EmmaX.change_stat("love", 80, 5)
            $ EmmaX.change_stat("obedience", 200, -5)
            $ EmmaX.change_stat("inhibition", 50, -5)
            ch_e "Oh, don't apologize. . ."
        "Yup. Deal with it.":
            if ApprovalCheck(EmmaX, 1000, "LO"):
                $ EmmaX.change_stat("obedience", 200, 20)
                $ EmmaX.change_stat("inhibition", 50, 10)
                ch_e "Ehem. . ."
            else:
                $ EmmaX.change_stat("love", 200, -10)
                $ EmmaX.change_stat("obedience", 200, 10)
                $ EmmaX.change_stat("inhibition", 50, 5)
                $ EmmaX.change_face("angry")
                ch_e "Well, that wasn't exactly what I had in mind."
                menu:
                    extend ""
                    "Guess you don't know me so well, huh?":
                        ch_e "I suppose that I don't."
                        $ Line = "rude"
                    "Sorry. I kind of thought you were getting into me being like that.":
                        $ EmmaX.change_face("sexy", 2)
                        $ EmmaX.eyes = "side"
                        $ EmmaX.change_stat("love", 95, 5)
                        $ EmmaX.change_stat("obedience", 200, 5)
                        $ EmmaX.change_stat("inhibition", 50, 5)
                        ch_e "Not. . . quite like that, no. . ."

    if not Line:

        ch_e "What I was getting at, is that I think that I tend to. . ."
        $ EmmaX.change_face("sly", 2)
        ch_e "-enjoy when you take a firm hand with me."
        $ EmmaX.change_face("smile", 1)
        menu:
            extend ""
            "Good. If you wanna be with me, that's how it'll be.":
                if ApprovalCheck(EmmaX, 1000, "LO"):
                    $ EmmaX.change_stat("obedience", 200, 15)
                    $ EmmaX.change_stat("inhibition", 50, 10)
                else:
                    $ EmmaX.change_face("sadside", 1)
                    $ EmmaX.change_stat("love", 200, -5)
                    $ EmmaX.change_stat("obedience", 200, 10)
                ch_e "Perhaps with a touch more class, [EmmaX.player_petname]. . ."
                menu:
                    extend ""
                    "Whatever. That's how it is. Take it or leave it.":
                        $ EmmaX.change_face("angry")
                        $ EmmaX.change_stat("love", 200, -10)
                        $ EmmaX.change_stat("obedience", 200, 5)
                        ch_e "I suppose you could use a bit more maturity first."
                        $ Line = "rude"
                    "I think I could maybe do that.":
                        $ EmmaX.change_face("bemused", 2)
                        $ EmmaX.eyes = "side"
                        $ EmmaX.change_stat("love", 95, 5)
                        $ EmmaX.change_stat("obedience", 200, 3)
                        $ EmmaX.change_stat("inhibition", 50, 5)
                        ch_e "That's good to hear."
            "Yeah? You think it's sexy?":

                $ EmmaX.change_face("bemused", 2)
                $ EmmaX.eyes = "side"
                $ EmmaX.change_stat("obedience", 200, 5)
                $ EmmaX.change_stat("inhibition", 50, 10)
            "You sure you don't want me to back off a little?":


                $ EmmaX.change_face("startled", 1)
                $ EmmaX.change_stat("obedience", 200, -5)
                menu:
                    ch_e "I wouldn't want to make you. . . uncomfortable."
                    "Only if you're okay with it.":
                        $ EmmaX.change_face("bemused", 2)
                        $ EmmaX.change_stat("love", 95, 10)
                        $ EmmaX.change_stat("inhibition", 50, 10)
                        $ Line = 0
                    "Uhm. . .yeah. I {i}do{/i} think it's weird. Sorry.":
                        $ EmmaX.change_stat("love", 200, -15)
                        $ EmmaX.change_stat("obedience", 200, -5)
                        $ EmmaX.change_stat("inhibition", 50, -10)
                        $ Line = "embarrassed"
            "I don't really care what you like. I do what I want.":

                $ EmmaX.change_stat("love", 200, -10)
                $ EmmaX.change_stat("obedience", 200, 15)
                $ EmmaX.change_face("angry")
                ch_e "Ugh. I think I may have misjudged you."
                $ Line = "rude"

    if not Line:
        $ EmmaX.change_face("bemused", 1, Eyes="side")
        ch_e "I'm more used to being in charge of the situation."
        ch_e "When you take control of things. . ."
        ch_e "I find it quite. . . exciting."
        menu:
            extend ""
            "Don't you think that relationship's kinda. . .weird?":
                $ EmmaX.change_stat("love", 200, -5)
                $ EmmaX.change_stat("inhibition", 50, -15)
                ch_e "Not at all, just perhaps a bit. . . unconventional."
            "I think I could get used to that kinda thing.":
                $ EmmaX.change_stat("obedience", 200, 5)
                $ EmmaX.change_stat("inhibition", 50, 5)
                $ EmmaX.change_face("smile", 1)

    if not Line:
        $ EmmaX.change_face("smile", 1)
        ch_e "That sounds delightful. If you don't mind, could I refer to you as. . . sir?"
        $ EmmaX.change_face("sly", 2)
        ch_e "Would you enjoy that?"
        $ EmmaX.blushing = 1
        menu:
            extend ""
            "That has a nice ring to it.":
                $ EmmaX.change_stat("love", 95, 5)
                $ EmmaX.change_stat("obedience", 200, 15)
                $ EmmaX.change_stat("inhibition", 50, 5)
                ch_e "Very well then. . .{i}sir{/i}."
                $ EmmaX.player_petname = "sir"
            "I think I'd rather stick with what we've got going.":
                $ EmmaX.change_face("confused", 2)
                ch_e "Hmm."
                $ EmmaX.change_stat("inhibition", 50, -5)
                $ EmmaX.change_face("sadside", 1)
                menu:
                    ch_e ". . . could you perhaps still take the lead in things?"
                    "I like that idea.":
                        $ EmmaX.change_stat("obedience", 200, 10)
                        $ EmmaX.change_face("smile", 1)
                        ch_e "That should do then, [EmmaX.player_petname]."
                    "This is getting really awkward.":
                        $ EmmaX.change_stat("love", 200, -10)
                        $ EmmaX.change_stat("obedience", 200, -50)
                        $ EmmaX.change_stat("inhibition", 50, -15)
                        $ Line = "embarrassed"


    $ EmmaX.history.append("sir")
    if not Line:
        $ EmmaX.blushing = 1
        $ EmmaX.player_petnames.append("sir")

    elif Line == "rude":
        hide Emma_Sprite with easeoutright
        call Remove_Girl (EmmaX)
        $ renpy.pop_call()
        "[EmmaX.name] marches out the door in a huff, leaving you alone."
    elif Line == "embarrassed":
        $ EmmaX.change_face("sad", 2)
        ch_e "Well, I. . . um. . ."
        $ EmmaX.change_face("sly", 1)
        ch_e "I was testing you. Obviously. That would be unprofessional."
        $ EmmaX.change_face("sadside", 2)
        ch_e "I should go. I think I see a student over there in need."
        $ EmmaX.blushing = 1
        hide Emma_Sprite with easeoutright
        call Remove_Girl (EmmaX)
        $ renpy.pop_call()
        "[EmmaX.name] dashes out the door, leaving you alone. It didn't look like she could get away fast enough."
    return

label Emma_Sub_Asked:
    $ Line = 0
    $ EmmaX.change_face("sadside", 1)
    ch_e "I might."
    ch_e "If I did, I would also remember that you seemed unprepared for the role."
    menu:
        extend ""
        "Well, I wanted to say I was sorry. And I was hoping maybe we could give it another shot.":
            if "sir" in EmmaX.player_petnames and ApprovalCheck(EmmaX, 850, "O"):

                pass
            elif ApprovalCheck(EmmaX, 550, "O"):

                pass
            else:
                ch_e "Perhaps when you've done a bit more soul-searching. . ."
                $ Line = "rude"

            if Line != "rude":
                $ EmmaX.change_stat("love", 90, 10)
                $ EmmaX.change_face("sly", 1)
                ch_e "I suppose I could give you another chance."
                ch_e "I appreciate that you recognize you made an error."
                ch_e "Fine, we can give it another try."
        "Listen. . .I know it's what you want. Do you want to try again, or not?":

            $ EmmaX.change_face("bemused", 1)
            if "sir" in EmmaX.player_petnames and ApprovalCheck(EmmaX, 850, "O"):
                ch_e "Ok, fine."
            elif not ApprovalCheck(EmmaX, 600, "O"):
                ch_e "Not at the moment, no."
                $ Line = "rude"
            else:

                $ EmmaX.change_face("sadside", 1)
                ch_e "You do tend to push your luck."
                $ EmmaX.eyes = "squint"
                ch_e "Perhaps you are right, but I do think an apology is still in order."
                menu:
                    extend ""
                    "Okay, I'm sorry I was so rude about it.":
                        $ EmmaX.change_stat("love", 90, 15)
                        $ EmmaX.change_stat("inhibition", 50, 10)
                        $ EmmaX.change_face("bemused", 1, Eyes="side")
                        ch_e "Apology accepted. . ."
                    "Not gonna happen.":
                        if "sir" in EmmaX.player_petnames and ApprovalCheck(EmmaX, 900, "O"):
                            $ EmmaX.change_stat("love", 200, -5)
                            $ EmmaX.change_stat("obedience", 200, 10)
                            ch_e ". . ."
                        elif ApprovalCheck(EmmaX,650, "O"):
                            $ EmmaX.change_stat("love", 200, -5)
                            $ EmmaX.change_stat("obedience", 200, 10)
                            ch_e "I- um. . .hmmm. . ."
                        else:
                            $ EmmaX.change_stat("love", 200, -10)
                            $ EmmaX.change_stat("obedience", 90, -10)
                            $ EmmaX.change_stat("obedience", 200, -10)
                            $ EmmaX.change_stat("inhibition", 50, -15)
                            "[EmmaX.name] sighs and rolls her eyes."
                            $ EmmaX.change_face("angry", 1, Eyes="side")
                            ch_e "You really don't learn, do you?"
                            $ Line = "rude"
                    "Ok, never mind then.":
                        $ EmmaX.change_face("angry", 1)
                        $ EmmaX.change_stat("love", 200, -10)
                        $ EmmaX.change_stat("obedience", 90, -10)
                        $ EmmaX.change_stat("obedience", 200, -10)
                        $ EmmaX.change_stat("inhibition", 50, -15)
                        ch_e "I don't know what I saw in you."
                        $ Line = "rude"

    $ EmmaX.recent_history.append("asked sub")
    $ EmmaX.daily_history.append("asked sub")
    if Line == "rude":

        hide Emma_Sprite with easeoutright
        call Remove_Girl (EmmaX)
        $ EmmaX.recent_history.append("angry")
        $ renpy.pop_call()
        "[EmmaX.name] marches out the door, leaving you alone. She looked pretty upset."
    elif "sir" in EmmaX.player_petnames:

        $ EmmaX.change_stat("obedience", 200, 50)
        $ EmmaX.player_petnames.append("master")
        $ EmmaX.player_petname = "master"
        $ EmmaX.eyes = "sly"
        ch_e ". . . master. . ."
    else:

        $ EmmaX.change_stat("obedience", 200, 30)
        $ EmmaX.player_petnames.append("sir")
        $ EmmaX.player_petname = "sir"
        $ EmmaX.eyes = "sly"
        ch_e ". . . sir."
    return






label Emma_Master:
    $ EmmaX.DrainWord("asked meet")
    call shift_focus (EmmaX)
    $ EmmaX.location = bg_current
    call set_the_scene
    if EmmaX.location != bg_current and EmmaX not in Party:
        "[EmmaX.name] shows up and says she needs to talk to you."
    else:
        "[EmmaX.name] approaches you, looking to talk."
    call clear_the_room (EmmaX)
    $ EmmaX.daily_history.append("relationship")
    call Taboo_Level
    $ Line = 0
    $ EmmaX.change_face("bemused", 1)
    ch_e "[EmmaX.player_petname], if you don't mind my saying so. . ."
    ch_e "I do think that your more. . . assertive direction has been quite. . ."
    ch_e ". . . exhilarating."
    menu:
        extend ""
        "I like it too.":
            $ EmmaX.change_face("sly", 1)
            ch_e "Good, good. . ."
            ch_e "That being the case, perhaps we would be able to. . ."
            ch_e "Go a bit deeper?"
            menu:
                extend ""
                "Nah. This is just about perfect.":
                    $ EmmaX.change_face("sad", 1)
                    $ EmmaX.change_stat("obedience", 200, -15)
                    $ EmmaX.change_stat("inhibition", 50, 10)
                    ch_e "Oh? I suppose. . ."
                    $ Line = "fail"
                "What'd you have in mind?":
                    $ EmmaX.eyes = "side"
                    ch_e "Hmm, well I was just considering, perhaps I could refer to you as. . ."
                    ch_e ". . . {i}master{/i}?"
                    $ EmmaX.eyes = "squint"
                    ch_e "Would you like that? Would that appeal to you?"
                    menu:
                        extend ""
                        "Oh, yeah. I'd like that.":
                            ch_e "Lovely. . ."
                        "Uhm. . .nah. That's too much.":
                            $ EmmaX.change_face("sad", 1)
                            $ EmmaX.change_stat("obedience", 200, -15)
                            $ EmmaX.change_stat("inhibition", 50, 5)
                            ch_e "Oh. Very well then, forget I said anything about it."
                            ch_e "Forget. . . forget. . . "
                            ch_e "Oh, never mind, I forgot that doesn't actually work on you."
                            ch_e "Just, be discreet."
                            $ Line = "fail"
                "Actually, I'd prefer we stopped doing it. I don't want to be too controlling.":

                    $ EmmaX.change_face("sly", 1)
                    $ EmmaX.change_stat("love", 200, 15)
                    $ EmmaX.change_stat("obedience", 200, -10)
                    $ EmmaX.change_stat("inhibition", 50, 10)
                    ch_e "Well, I suppose you must be true to your nature. . ."
                    $ Line = "fail"
                "Actually, let's stop that. It's creeping me out.":

                    $ EmmaX.change_face("perplexed", 2)
                    $ EmmaX.change_stat("love", 200, -10)
                    $ EmmaX.change_stat("obedience", 200, -50)
                    $ EmmaX.change_stat("inhibition", 50, -15)
                    ch_e "Well. We wouldn't want that now."
                    $ EmmaX.blushing = 1
                    $ Line = "embarrassed"
        "As if I care what you think, slut.":

            $ EmmaX.change_face("angry", 1)
            $ EmmaX.change_stat("love", 200, -20)
            $ EmmaX.change_stat("obedience", 200, 10)
            $ EmmaX.change_stat("inhibition", 50, -10)
            menu:
                ch_e "What was that?"
                "Sorry. I just don't care what you want.":
                    if ApprovalCheck(EmmaX, 1400, "LO"):
                        $ EmmaX.change_stat("obedience", 200, 10)
                        ch_e "That's. . ."
                        $ EmmaX.change_face("sly", 1)
                        $ EmmaX.change_stat("love", 200, 20)
                        $ EmmaX.change_stat("inhibition", 50, 15)
                        ch_e ". . .not entirely off the mark."
                    else:
                        $ EmmaX.change_stat("love", 200, -15)
                        $ EmmaX.change_stat("obedience", 200, -10)
                        $ EmmaX.change_stat("inhibition", 50, 5)
                        $ EmmaX.change_face("angry", 1)
                        ch_e "!!!"
                        $ Line = "rude"
                "Sorry. I'm just trying to do the \"control\" thing. I thought you'd like it. Too much?":

                    $ EmmaX.change_stat("love", 200, 10)
                    $ EmmaX.change_stat("obedience", 200, 10)
                    $ EmmaX.change_stat("inhibition", 50, 5)
                    ch_e "You. . . may have a bit of work to do on that."
        "Not me. It's kind of creepy.":

            $ EmmaX.change_face("sad", 2)
            $ EmmaX.change_stat("love", 200, -10)
            $ EmmaX.change_stat("obedience", 200, -20)
            $ EmmaX.change_stat("inhibition", 50, -25)
            ch_e "Oh. Well we wouldn't want that. . ."
            $ Line = "embarrassed"

    $ EmmaX.history.append("master")
    if Line == "rude":
        $ EmmaX.recent_history.append("angry")
        call Remove_Girl (EmmaX)
        $ renpy.pop_call()
        "[EmmaX.name] storms out the door in a huff."
    elif Line == "embarrassed":
        call Remove_Girl (EmmaX)
        $ renpy.pop_call()
        "[EmmaX.name] dashed out of the room, leaving you alone. She looked really embarrassed."
    elif Line != "fail":
        $ EmmaX.change_stat("obedience", 200, 50)
        $ EmmaX.player_petnames.append("master")
        $ EmmaX.player_petname = "master"
        ch_e ". . .master."
    return






label Emma_Sexfriend:
    $ EmmaX.DrainWord("asked meet")

    if EmmaX in Player.Harem:
        $ EmmaX.player_petnames.append("sex friend")
        return
    $ EmmaX.location = bg_current
    call set_the_scene
    call clear_the_room (EmmaX, 1, 1)
    $ EmmaX.daily_history.append("relationship")
    call Taboo_Level
    $ Line = 0
    "After class, the students file out of the room."
    $ EmmaX.change_face("bemused", 1)
    ch_e "[Player.name], could I have a word with you?"
    menu:
        extend ""
        "I'm in a hurry.":
            $ EmmaX.change_face("angry", 1)
            ch_e "That's. . . not an appropriate response."
            $ EmmaX.change_stat("love", 200, -20)
            $ EmmaX.change_stat("obedience", 50, 3)
            $ Line = "rude"
        "This doesn't sound good.":

            $ EmmaX.change_face("sly", 1)
            ch_e "Settle down, it's nothing. . . unpleasant."
        "Yeah. What's up?":

            pass

    if not Line:
        if ApprovalCheck(EmmaX, 850, "L"):
            $ EmmaX.change_face("sly", 1)
            ch_e "I just, enjoy spending time with you, as you're aware?"
            menu:
                extend ""
                "I thought so.":
                    $ EmmaX.change_face("sexy", 1)
                    $ EmmaX.change_stat("love", 90, 10)
                    $ EmmaX.change_stat("inhibition", 80, 5)
                    ch_e "I {i}was{/i} hoping you'd be aware, [EmmaX.player_petname]."
                "Really?":
                    $ EmmaX.change_face("perplexed", 1)
                    ch_e "Um, yes."
                "Don't complicate things.":

                    $ EmmaX.change_face("angry", 1)
                    $ EmmaX.change_stat("love", 200, -10)
                    $ EmmaX.change_stat("obedience", 50, 5)
                    $ EmmaX.change_stat("inhibition", 80, -5)
                    ch_e "I'm sorry if you find this discussion too \"complicated.\""
                    $ Line = "rude"
        elif ApprovalCheck(EmmaX, 1000, "LI"):
            $ EmmaX.change_face("sexy", 1)
            ch_e "I just thought you should know how. . . intriguing I find you."
            menu:
                extend ""
                "That's really nice of you to say.":
                    $ EmmaX.change_stat("love", 80, 5)
                    $ EmmaX.change_stat("inhibition", 80, 5)
                    ch_e "Certainly."
                "Me? You really think so?":
                    ch_e "Don't be overly modest, [EmmaX.player_petname]."
                "Are you going somewhere with this?":
                    $ EmmaX.change_face("angry")
                    ch_e "Perhaps not."
                    $ Line = "rude"
        else:
            $ EmmaX.mouth = "smile"
            $ EmmaX.brows = "sad"
            $ EmmaX.eyes = "side"
            ch_e "This may sound a bit. . . unconventional."
            menu:
                extend ""
                "Well, you've got me intrigued. Now you {i}have{/i} to tell me.":
                    ch_e "You'll keep this between the two of us?"
                    menu:
                        extend ""
                        "[EmmaX.name]. . . I really like you. I promise.":
                            $ EmmaX.change_face("smile")
                            $ EmmaX.change_stat("love", 90, 10)
                            $ EmmaX.change_stat("inhibition", 80, 5)
                            ch_e "Very well. . ."
                        "Uhm. . . okay?":
                            ch_e "Well. . ."
                        "No promises.":
                            $ EmmaX.change_face("perplexed",2)
                            $ EmmaX.change_stat("inhibition", 80, -5)
                            ch_e "Hmm. . . never mind, then."
                            $ Line = "embarrassed"
                "Uhm, I think I've had my fill of {i}weird{/i}, thanks":
                    $ EmmaX.change_face("angry",1)
                    ch_e "Live in suspense then."
                    $ Line = "rude"

    if not Line:
        ch_e "I was considering. . . "
        ch_e "Perhaps we could take our relationship a little further, if you wanted to."
        menu:
            extend ""
            "You mean. . . like, being {i}friends with benefits{/i}?":
                ch_e "I suppose you could put it that way."
                ch_e "What do you think?"
                menu:
                    extend ""
                    "Sounds amazing! Count me in.":
                        $ EmmaX.change_face("smile",1)
                        $ EmmaX.change_stat("love", 80, 10)
                        $ EmmaX.change_stat("obedience", 50, 10)
                        $ EmmaX.change_stat("inhibition", 200, 50)
                        $ EmmaX.change_stat("lust", 200, 5)
                        "[EmmaX.name] leans in and gives you a passionate kiss."
                        $ EmmaX.action_counter["kiss"] += 1
                        ch_e "I can't wait to get started, [EmmaX.player_petname]."
                    "That's pretty slutty, [EmmaX.name].":
                        if ApprovalCheck(EmmaX, 2000):
                            $ EmmaX.change_face("angry",1,Brows="confused")
                            $ EmmaX.change_stat("love", 200, -10)
                            $ EmmaX.change_stat("obedience", 50, 15)
                            ch_e "I suppose you're not wrong."
                        else:
                            $ EmmaX.change_face("angry",1)
                            $ EmmaX.change_stat("love", 200, -30)
                            $ EmmaX.change_stat("obedience", 50, 10)
                            $ EmmaX.change_stat("inhibition", 80, -20)
                            ch_e "Then I suppose I'll have to take care of that elsewhere!"
                            $ Line = "rude"
            "Uhm, to be honest, I'd rather not.":
                $ EmmaX.change_face("sadside",2)
                $ EmmaX.change_stat("obedience", 50, 15)
                $ EmmaX.change_stat("inhibition", 80, -15)
                ch_e "Oh. Suit yourself, I suppose."
                ch_e "I should be leaving."
                $ Line = "sad"

    if Line == "rude":
        $ EmmaX.change_face("angry",1)
        $ EmmaX.recent_history.append("angry")
        $ EmmaX.change_stat("love", 200, -20)
        $ EmmaX.change_stat("obedience", 50, 5)
        $ EmmaX.change_stat("inhibition", 80, -10)
        hide Emma_Sprite with easeoutright
        $ EmmaX.recent_history.append("angry")
        "[EmmaX.name] storms off in a huff. She seemed pretty mad at you."
    elif Line == "embarrassed":
        $ EmmaX.change_face("perplexed",1)
        $ EmmaX.change_stat("love", 200, -10)
        $ EmmaX.change_stat("obedience", 50, 5)
        $ EmmaX.change_stat("inhibition", 80, -20)
        hide Emma_Sprite with easeoutright
        "[EmmaX.name] dashes out of the room, leaving you alone. That was very strange."
    elif Line == "sad":
        hide Emma_Sprite with easeoutbottom
        "[EmmaX.name] wanders into the hall, leaving you alone. You think you may have hurt her feelings."
    else:
        $ EmmaX.player_petnames.append("sex friend")
        $ EmmaX.change_face("sly",2)
        $ EmmaX.change_stat("inhibition", 80, 10)
        $ EmmaX.change_stat("lust", 80, 10)
        "[EmmaX.name] leans in and carresses your body."
        "As she does so, you feel a tickle as if her mouth is surrounding your cock."
        "You look back at her and she winks."
        ch_e "I do have a few tricks up my sleeves, [EmmaX.player_petname]."
        ch_e "I'll see you later, I hope."
        hide Emma_Sprite with easeoutright
        "She leaves the room, and the phantom \"lips\" give you one final kiss. "
    call Remove_Girl (EmmaX)
    return






label Emma_Fuckbuddy:
    $ EmmaX.DrainWord("asked meet")
    $ EmmaX.daily_history.append("relationship")
    "Out of nowhere, you feel a tongue sliding across your cock."
    "Even though you're fully dressed, it definitely feels like a mouth has enveloped your cock."
    "You look down, but can't see any movement, although your cock has become diamond hard."
    "As you try to control your obvious erection, a voice tickles the back of your mind,"
    ch_e "To me, my X-Man. . ."
    "-and suddenly the pressure is gone."
    "Looking around, you don't see anyone nearby, and it doesn't look like anyone else noticed what happened."
    "Maybe you'll check up on [EmmaX.name] later. . ."
    $ EmmaX.player_petnames.append("fuck buddy")
    $ EmmaX.Event[10] += 1
    return




label Emma_Daddy:
    $ EmmaX.DrainWord("asked meet")
    $ EmmaX.daily_history.append("relationship")
    call shift_focus (EmmaX)
    call set_the_scene
    ch_e ". . ."
    if EmmaX in Player.Harem:
        ch_e "We have been dating a while, [EmmaX.player_petname],"
    else:
        ch_e "We have been enjoying ourselves,"
    if EmmaX.love > EmmaX.obedience and EmmaX.love > EmmaX.inhibition:
        ch_e "and you certainly are sweet. . ."
    elif EmmaX.obedience > EmmaX.inhibition:
        ch_e "and you know how to keep me interested. . ."
    else:
        ch_e "and I've been. . . exploring. . ."
    ch_e "I was thinking, would you mind if I call you \"daddy?\""
    menu:
        extend ""
        "Ok, go right ahead?":
            $ EmmaX.change_face("smile")
            $ EmmaX.change_stat("love", 90, 20)
            $ EmmaX.change_stat("obedience", 60, 10)
            $ EmmaX.change_stat("inhibition", 80, 30)
            ch_e "Excellent."
        "What do you mean by that?":
            $ EmmaX.change_face("bemused")
            ch_e "I just find it to be a turn-on, being your baby girl. . ."
            ch_e "I'd prefer to call you that sometimes."
            menu:
                extend ""
                "Sounds interesting, fine by me.":
                    $ EmmaX.change_face("smile")
                    $ EmmaX.change_stat("love", 90, 15)
                    $ EmmaX.change_stat("obedience", 60, 20)
                    $ EmmaX.change_stat("inhibition", 80, 25)
                    ch_e "Great!"
                    $ EmmaX.change_face("sly",2)
                    ch_e " . . . daddy."
                    $ EmmaX.change_face("sly",1)
                    $ EmmaX.player_petname = "daddy"
                "Could you not, please?":
                    $ EmmaX.change_stat("love", 90, 5)
                    $ EmmaX.change_stat("obedience", 80, 40)
                    $ EmmaX.change_stat("inhibition", 80, 20)
                    $ EmmaX.change_face("sad")
                    ch_e " . . . "
                    ch_e "Well, ok."
                "You've got some real daddy issues, uh?":
                    $ EmmaX.change_stat("love", 90, -15)
                    $ EmmaX.change_stat("obedience", 80, 45)
                    $ EmmaX.change_stat("inhibition", 70, 5)
                    $ EmmaX.change_face("angry")
                    ch_e "Let's not get into it."
        "Aren't you a bit old for that?":
            $ EmmaX.change_stat("love", 90, -15)
            $ EmmaX.change_stat("obedience", 80, 40)
            $ EmmaX.change_stat("inhibition", 70, 10)
            $ EmmaX.change_face("angry")
            ch_e "Perhaps this was a bad idea."
    $ EmmaX.player_petnames.append("daddy")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
