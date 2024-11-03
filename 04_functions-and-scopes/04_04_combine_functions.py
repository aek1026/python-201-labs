# Combine the `greet()` function that you developed in the course materials
# with the `write_letter()` function from the previous exercise.
# Write both functions in this script and call `greet()` within `write_letter()`
# to let `greet()` take care of creating the greeting string.
def greet(greeting, name):
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

def write_letter(greeting, name, text):
    greeting_message = greet(greeting,name)
    instructions = [greeting_message, f"{text} {name},", f"Goodbye {name}."]

    return "\n".join(instructions)

print(write_letter("Hello","Dodger","I hope you are doing well"))

