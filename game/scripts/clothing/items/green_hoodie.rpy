init -1 python:

    def green_hoodie(Owner):
        name = "green hoodie"
        string = "green_hoodie"

        clothing_type = "jacket"

        dialogue_lines = {
            }

        shame = -2

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
