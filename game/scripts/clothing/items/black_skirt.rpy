init python:

    def black_skirt():
        name = "black skirt"
        image_string = "black_skirt"
        clothing_type = "skirt"

        dialogue_lines = {
            }

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

        number_of_states = 2

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, hides = hides, covers = covers, number_of_states = number_of_states)
