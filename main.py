PLACE_HOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as data:
    list_names = data.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_files:
    letter_content = letter_files.read()
    for name in list_names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACE_HOLDER, stripped_name)

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as write_data:
            write_data.write(new_letter)