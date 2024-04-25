print("Ethic wakes up in a prison cell without remembering anything.")
print("Ethic meets Hedge, who wants to save the world.")
print("Hedge explains the lock: a dial with 100 positions.")
print("Ethic can't steal keys, so Hedge suggests specific instructions.")
print("Hedge needs clear instructions for Ethic to give.")

position = int(input("Enter your position:"))  # Moved input outside the loop
for i in range(100):  # Removed redundant variable assignment
    if position == 41:
        print("The cell door opens at position 41, and they escape.")
        break
    position = int(input("Try again. Enter your position:"))  # Ask for input inside the loop
else:
    print("Failed to open the cell door.")

print("Ethic runs, and Hedge opens the outer door at position 93.")
print("Hedge explains they need three artifacts to restore order.")
print("Ethic's goal is to return to the world machine to fix things.")
