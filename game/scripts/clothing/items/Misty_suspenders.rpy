init -1 python:

    def Misty_suspenders(Owner):
        name = "Misty's suspenders"
        image_string = "Misty_suspenders"

        clothing_type = "suspenders"

        dialogue_lines = {
            }

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob"]

        return ClothingClass(Owner, name, image_string, clothing_type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)