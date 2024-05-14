#chat bot agent
class ChatBotAgent:
    def __init__(self):
        self.knowledge_base = {
            "hello": "Hello, how can I assist you?",
            "how are you": "I'm an AI, I don't have feelings, but I'm functioning as expected.",
            "bye": "Goodbye, have a nice day!"
        }

    def respond(self, user_input):
        user_input = user_input.lower()
        if user_input in self.knowledge_base:
            return self.knowledge_base[user_input]
        else:
            return "I'm sorry, I didn't understand that."

def main():
    agent = ChatBotAgent()
    while True:
        user_input = input("User: ")
        if user_input.lower() == "bye":
            print(agent.respond(user_input))
            break
        print("ChatBot: ", agent.respond(user_input))

if __name__ == "__main__":
    main()