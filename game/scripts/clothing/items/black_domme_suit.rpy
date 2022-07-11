init -1 python:

    def black_domme_suit(Owner):
        name = "black domme suit"
        string = "black_domme_suit"

        clothing_type = "bodysuit"

        dialogue_lines = {
            }

        shame = 5

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]

        number_of_states = 1

        poses = [
            "arm pose 2"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
