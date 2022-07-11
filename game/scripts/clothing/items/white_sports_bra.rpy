init -1 python:

    def white_sports_bra(Owner):
        name = "white sports bra"
        string = "white_sports_bra"

        clothing_type = "bra"

        dialogue_lines = {
            }

        shame = 1

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "titjob",
            "blowjob",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
