# # Prompt user to enter text(message)
# def check_answer(message):
#     if message ==" Hallo" or message.lower() == "Hallo,Newman":
#         return " $0 "
#     else:
#         if message == "How are you doing?":
#             return "$20"
#         if message == "What is happenning?":
#             return "$100"
        

# user_message = input(message)
# result = check_answer(user_message)
# print(result)
# if __name__ == "__main__":
#     main()


def main():
    greeting = input("Greeting: ")
    reward = compute_reward(greeting)
    print(reward)

def compute_reward(greeting):
    if greeting.lower().startswith("hello"):
        return "$0"
    elif greeting.lower().startswith("h") and greeting != "hello":
        return "$20"
    else:
        return "$100"    
    
if __name__ == "__main__":
    main()