while True:
    user=input("you:  ")
    if user.lower() in ["bye","exit","quit"]:
        print("Bot: good bye,have a nice day")
        break
    elif user.lower()in["hello"]:
        print("hi, how are you")
    elif user.lower()in["i am fine"]:
        print("how can i help you")
    elif user.lower()in["who is our prime minister"]:
        print("narendra modi is our pm of india")
    else:
        print("data is not found")
    