init -1 python:

    def blue_skirt():
        name = "blue skirt"
        image_string = "blue_skirt"

        clothing_type = "skirt"

        Owner_names = ["Kitty"]

        dialogue_lines = {
            }

        shame = -2

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "titjob",
            "footjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, Owner_names, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
