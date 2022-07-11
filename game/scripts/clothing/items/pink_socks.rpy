init -1 python:

    def pink_socks(Owner):
        name = "pink socks"
        string = "pink_socks"

        clothing_type = "socks"

        dialogue_lines = {
            }

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
