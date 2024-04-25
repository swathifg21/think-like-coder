# Define settlers with their characteristics
settlers = [
    {"name": "Alice", "eye_color": "green", "hair_color": "red", "wearing_glasses": True},
    {"name": "Bob", "eye_color": "blue", "hair_color": "brown", "wearing_glasses": False},
    {"name": "Charlie", "eye_color": "green", "hair_color": "red", "wearing_glasses": True},
    {"name": "Diana", "eye_color": "brown", "hair_color": "blonde", "wearing_glasses": False},
    {"name": "Eve", "eye_color": "green", "hair_color": "red", "wearing_glasses": False},
]

# Initialize resistance leader variable
resistance_leader = None

# 1. Gather Information:
def has_green_eyes(settler):
    return settler["eye_color"] == "green"

def has_red_hair_with_double_letter(settler):
    hair = settler["hair_color"]
    return hair == "red" and any(hair[i] == hair[i+1] for i in range(len(hair)-1))

def has_correct_vowels(settler):
    name = settler["name"]
    num_vowels = sum(1 for char in name if char.lower() in "aeiou")
    if settler["wearing_glasses"]:
        return num_vowels == 2
    else:
        return num_vowels == 3

# 2. Examine Settlers:
for settler in settlers:
    if has_green_eyes(settler):
        if has_red_hair_with_double_letter(settler) and has_correct_vowels(settler):
            resistance_leader = settler
            break

# 3. Identify the Resistance Leader:
if resistance_leader:
    print(f"The resistance leader is {resistance_leader['name']}.")

    # 4. Engage with the Resistance Leader:
    print(f"Discuss plans and objectives with {resistance_leader['name']}.")
    print(f"Agree to terms and conditions for assistance with {resistance_leader['name']}.")
    print(f"Proceed with agreed-upon actions with {resistance_leader['name']}.")
else:
    print("Resistance leader not found.")
