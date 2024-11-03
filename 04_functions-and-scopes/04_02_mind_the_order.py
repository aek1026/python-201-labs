# Something is wrong with the way you're calling the function below.
# Can you fix it and survive?

def skydive(step_1, step_2):
    instructions = ["For your own safety, please follow the instructions carefully:",
    f"1. {step_1}",
    f"2. {step_2}"
]
    return "\n".join(instructions)

print(skydive("JUMP!", "Take your parachute."))
