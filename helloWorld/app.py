print("hello_world.py")
answer = input("What is the capital of Finland? a) Turku b) Tampere c) Helsinki d) Espoo: ").strip().lower()
print("Correct!" if answer == "c" else "Wrong! The correct answer is c)")