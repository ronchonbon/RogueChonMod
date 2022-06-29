init python:

    def black_bra():
        name = "black bra"
        image_string = "black_bra"
        clothing_type = "bra"

        dialogue_lines = {
            "mall": "Try on the black bra.",
            "wardrobe": "Why don't you put on your black bra?"
            }

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, hides = hides, covers = covers, number_of_states = number_of_states)
