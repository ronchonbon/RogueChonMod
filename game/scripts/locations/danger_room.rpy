label training:
    if round >= 80:
        $ line = "You have a long session in the Danger Room."
    elif round >= 50:
        $ line = "You have a short workout in the Danger Room."
    else:
        $ line = "You squeeze in a quick session in the Danger Room."

    $ D20 = renpy.random.randint(1, 20)

    if D20 >= 18:
        "[line] During the exercise, Cyclops accidentally shoots you."
        "Luckily you're immune to the beams, but your clothes weren't so lucky."

        call change_Present_stat("love", 2)
        call change_Present_stat("lust", 5)
    elif D20 >= 17:
        "[line] You participate in a hand-to-hand combat class."
        "Before you begin, Cyclops explains that it’s always good to know how to defend yourself when you can’t rely on your powers."
        "It sounds like there’s a story there."
    elif D20 >= 16:
        "Some of the senior students walk over to talk about your powers."
        "Nightcrawler wonders aloud what would happen if he grabbed you and tried to teleport while you tried to disable his powers."
        "You succeed in freaking each other out."
    else:
        $ line = line + renpy.random.choice([" It was fairly boring.",
                    " You do some training with basic firearms.",
                    " You run the obstacle course.",
                    " You fight in a simulated battle against the Brotherhood.",
                    " You help take down a holographic Sentinel.",
                    " You take part in a training exercise against the Avengers. As if the X-Men and Avengers would ever fight.",
                    " You and some of the others take part in a survival exercise. . . also known as \"try to last as long as you can while Wolverine hunts you down one by one.\"",
                    " You decide to test yourself by facing off against Magneto solo. It goes about as well as you’d expect.",
                    " You use the Danger Room’s holograms to relive some of the original X-Men’s biggest battles. You learn quite a bit about teamwork.",
                    " Beast is teaching a class on parkour. You take part and pick up a few pointers. You’re no Spider-Man, but at least you pick up a few things.",
                    " You participate in an emergency drill. You pick up quite a few tips about first aid, triage, and the proper way to move injured people.",
                    " You take part in an urban emergency situation exercise. Cyclops takes the time to explain to you how to use cover to get close enough to use your powers.",
                    " You take part in a jungle simulation exercise under Wolverine. You learn some basic survival techniques, but you privately hope you never need them.",
                    " Your team fights a simulation of Magneto."])

        "[line]"

    $ Player.XP += 5 + int(round/10)

    return
