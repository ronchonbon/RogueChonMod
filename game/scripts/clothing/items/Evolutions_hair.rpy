init python:

    def Evolutions_hair():
        name = "Evolutions hair"
        image_string = "Evolutions_hair"
        clothing_type = "hair"

        dialogue_lines = {
            "wardrobe": "I like your original hairstyle."
            }

        return ClothingClass(name, image_string, clothing_type, dialogue_lines)
