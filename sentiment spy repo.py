<<<<<<< HEAD
import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()

print(f"{Fore.YELLOW} 🐍 Welcome to Sentiment Spy! Agent 🐍{Style.RESET_ALL}")

user_name = input(f"{Fore.RED} Enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "Mystery Man"  


conversation_history = []

print(f"\n{Fore.GREEN}Hello, Agent {user_name}!")
print(f"Type a Sentence of your choice and I will analyze your sentences with TextBlob and will show you the sentiment. ")
print(f"Type {Fore.YELLOW}reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN}, "
    f"or {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.BLUE}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some valid command.{Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Farewell, Agent {user_name}! 😊{Style.RESET_ALL}")
        break

    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.BROWN}  conversation history has been cleared!{Style.RESET_ALL}")
        continue

    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                # Choose color & emoji based on sentiment
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😭"

                print(f"{idx}. {color}{emoji} {text} "
                    f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
        continue

    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.ORANGE
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.PINK
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.BLUE
        emoji = "😭"

    
    conversation_history.append((user_input, polarity, sentiment_type))

    
    print(f"{color}{emoji} {sentiment_type} The sentiment detected is "