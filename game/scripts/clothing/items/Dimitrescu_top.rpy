init -1 python:

    def Dimitrescu_top(Owner):
        name = "Lady Dimitrescu's top"
        image_string = "Dimitrescu_top"

        clothing_type = "top"

        dialogue_lines = {
            }

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "titjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
