init -1 python:

    def black_jeans():
        name = "black jeans"
        image_string = "black_jeans"

        clothing_type = "pants"

        Owner_names = ["Kitty"]

        dialogue_lines = {
            }

        shame = -5

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

        number_of_states = 1

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
