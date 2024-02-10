greeting = input("Greeting: ")
greeting = greeting.strip().lower()

index = greeting.find("h")

if index == 0 and "hello" in greeting:
    print("$0")
elif index == 0 and "hello" not in greeting:
    print("$20")
else:
    print("$100")