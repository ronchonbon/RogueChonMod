init python:

    def blue_capris():
        name = "blue capris"
        image_string = "blue_capris"
        clothing_type = "pants"

        dialogue_lines = {
            }

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

        number_of_states = 1

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, hides = hides, covers = covers, number_of_states = number_of_states)
