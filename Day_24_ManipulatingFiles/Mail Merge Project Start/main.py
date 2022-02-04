# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Letters/starting_letter.txt", mode="r") as starting_letter:
    initial_letter = starting_letter.read()
    with open("./Input/Names/invited_names.txt") as invited_names:
        invitees = invited_names.readlines()
        for invitee in invitees:
            invitee = invitee.strip('\n')
            edited_letter = initial_letter.replace("[name]", invitee)
            with open(f"./Output/ReadyToSend/{invitee}", mode="w") as output_folder:
                output_folder.write(edited_letter)

