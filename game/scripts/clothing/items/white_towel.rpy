init -1 python:

    def white_towel(Owner):
        name = "white towel"
        image_string = "white_towel"

        clothing_type = "top"

        dialogue_lines = {
            }

        shame = 5

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy"]

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "doggy"]

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
