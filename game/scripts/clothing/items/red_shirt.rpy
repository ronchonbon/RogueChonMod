init -1 python:

    def red_shirt():
        name = "red shirt"
        image_string = "red_shirt"

        clothing_type = "top"

        Owner_names = ["Kitty"]

        dialogue_lines = {
            }

        shame = -5

        hides = ["breasts"]
        covers = ["breasts"]

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
