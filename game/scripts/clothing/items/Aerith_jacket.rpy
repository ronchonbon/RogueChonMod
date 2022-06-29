init python:

    def Aerith_jacket():
        name = "Aerith jacket"
        image_string = "Aerith_jacket"
        clothing_type = "jacket"

        dialogue_lines = {
            }

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, hides = hides, covers = covers, number_of_states = number_of_states)
