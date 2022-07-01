init -1 python:

    def grey_knee_stockings():
        name = "grey knee stockings"
        image_string = "grey_knee_stockings"

        clothing_type = "socks"

        Owner_names = ["Kitty"]

        dialogue_lines = {
            }

        shame = 1

        hides = []
        covers = ["feet"]

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
