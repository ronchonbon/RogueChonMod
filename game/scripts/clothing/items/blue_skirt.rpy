init python:

    def blue_skirt():
        name = "blue skirt"
        image_string = "blue_skirt"
        clothing_type = "skirt"

        dialogue_lines = {
            }

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 2

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, hides = hides, covers = covers, number_of_states = number_of_states)
