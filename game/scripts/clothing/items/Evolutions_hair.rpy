init -1 python:

    def Evolutions_hair():
        name = "Evolutions hair"
        image_string = "Evolutions_hair"

        clothing_type = "hair"

        Owner_names = ["Rogue", "Kitty"]

        dialogue_lines = {
            "wardrobe": "I like your original hairstyle."
            }

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "arm pose 1",
            "arm pose 2",
            "handjob",
            "titjob",
            "footjob",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(name, image_string, clothing_type, dialogue_lines, Owner_names, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
