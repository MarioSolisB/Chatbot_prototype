"""Command-line interface for the real estate chatbot."""

import time
from termcolor import colored
from config.settings import CLEAR_COMMAND, EXIT_COMMAND
from utils.formatting import clear_screen, format_welcome_message, format_user_prompt

class ChatInterface: 
    def __init__(self, user_proxy, real_estate_agent):
        self.user_proxy = user_proxy
        self.real_estate_agent = real_estate_agent

    def display_welcome(self):
        clear_screen()
        print(format_welcome_message())

    def start(self):
        self.display_welcome()

        try:
            while True:
                user_input = input(format_user_prompt())

                if user_input.lower() == EXIT_COMMAND:
                    print(colored("\nThank you for using NEXUS Residence chat system. Goodbye!", "cyan"))
                    break
                elif user_input.lower() == CLEAR_COMMAND:
                    clear_screen()
                    continue

                chat_result = self.user_proxy.initiate_chat(
                    self.real_estate_agent,
                    message=user_input,
                )
                time.sleep(0.5)

        except KeyboardInterrupt:
            print(colored("\n\nChat session terminated by user.", "yellow"))
        except Exception as e:
            print(colored(f"\nAn error occurred: {str(e)}", "red"))
        finally:
            print(colored("\nChat session ended.", "cyan"))