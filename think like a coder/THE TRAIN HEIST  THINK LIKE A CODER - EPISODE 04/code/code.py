# 1. Setup Train Position Variable:
train_position = 10

# 2. Loop through Instructions:
instructions = ['right', 'left', 'right', 'left', 'right']  # example instructions
for instruction in instructions:
    # For each instruction:
    if instruction == 'right':
        train_position -= 1  # decrease train_position by 1 for right arrow
    elif instruction == 'left':
        train_position += 1  # increase train_position by 1 for left arrow

# 3. Hit Button at Right Moment:
if train_position == 0:
    print("Hedge hits the button to lower the force field.")

# 4. Executing the Plan:
print("Ethic positions on the crane.")
print("Hedge sneaks into the engine car unnoticed.")
print("They track the train's movement based on the instructions.")

# 5. Stealing the Artifact:
artifact_position = 5  # example artifact position
if train_position == artifact_position:
    print("Adila lowers the crane.")
    print("Ethic swoops in to lift the Node of Power.")

# 6. Artifact Activation:
print("Ethic gives the artifact to Hedge for safekeeping.")
print("The artifact activates, revealing Ethic's journey to becoming chief robotics engineer and the prosperity brought by her creations.")

# 7. Next Destination:
next_destination = "198 forest"  # example next destination
if next_destination in ["198 forest", "198 forest to the southeast"]:
    print("Hedge detects the second Earth artifact in the 198 forest to the southeast.")
    print("Since the train is heading there next and has enough fuel:")
    print("Ethic and Hedge board the train for the journey ahead.")
