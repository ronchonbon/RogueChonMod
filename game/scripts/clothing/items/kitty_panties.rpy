init -1 python:

    def kitty_panties(Owner):
        name = "kitty panties"
        string = "kitty_panties"

        clothing_type = "underwear"

        dialogue_lines = {
            }

        shame = 1

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
