init -1 python:

    def black_bra():
        name = "black bra"
        image_string = "black_bra"

        clothing_type = "bra"

        Owner_names = ["Rogue"]

        dialogue_lines = {
            "mall": "Try on the black bra.",
            "wardrobe": "Why don't you put on your black bra?"
            }

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 2

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
