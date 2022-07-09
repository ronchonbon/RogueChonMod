label first_kiss:
    $ RogueX.blushing = "_blush2"

    call kiss_launch(RogueX)

    $ RogueX.History.update("kiss")

    "She leans in for a kiss."
    "You lean in and your lips meet [RogueX.name]'s."

    $ RogueX.eyes = "surprised"
    call change_Girl_stat(RogueX, "love", 15)
    call change_Girl_stat(RogueX, "love", 30)

    "A slight spark passes between you and her eyes widen with surprise."

    call change_Girl_stat(RogueX, "lust", 5)

    ch_r "Wow, [RogueX.player_petname], that was really something. . ."

    $ RogueX.change_face("bemused", blushing = 1)

    ch_r "Not the kind of zap I'm used to."

    call change_Girl_stat(RogueX, "obedience", 20)
    call change_Girl_stat(RogueX, "inhibition", 30)

    call show_full_body(RogueX)

    return
