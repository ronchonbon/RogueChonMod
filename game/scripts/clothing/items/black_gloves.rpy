init python:

    def black_gloves():
        name = "black gloves"
        image_string = "black_gloves"
        clothing_type = "gloves"

        dialogue_lines = {
            "mall": "What about those black gloves?",
            "wardrobe": "Black gloves on, please."
            }

        return ClothingClass(name, image_string, clothing_type, dialogue_lines)
