init python:

    def Aerith_skirt():
        name = "Aerith skirt"
        image_string = "Aerith_skirt"
        clothing_type = "skirt"

        dialogue_lines = {
            }

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

        number_of_states = 2

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, hides = hides, covers = covers, number_of_states = number_of_states)
