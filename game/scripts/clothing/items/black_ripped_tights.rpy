init -1 python:

    def black_ripped_tights():
        name = "black ripped tights"
        image_string = "black_ripped_tights"

        clothing_type = "hose"

        Owner_names = ["Rogue"]

        dialogue_lines = {
            }

        shame = 2

        hides = []
        covers = ["thighs", "feet"]

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
