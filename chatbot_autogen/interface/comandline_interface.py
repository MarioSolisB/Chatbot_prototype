"""Command-line interface for the real estate chatbot."""

import time
from termcolor import colored
from chatbot_autogen.config.settings import CLEAR_COMMAND, EXIT_COMMAND
from chatbot_autogen.utils.formatting import clear_screen, format_welcome_message, format_user_prompt

class ChatInterface:
    def __init__(self, user_proxy, real_estate_agent):

        self.user_proxy = user_proxy
        self.real_estate_agent = real_estate_agent
        self.chat_active = False

    def display_welcome(self):
        clear_screen()
        print(format_welcome_message())

    def start(self):
        self.display_welcome()
        self.chat_active = True

        try:
            # Initial message to start the conversation
            initial_message = "hi"
            chat_result = self.user_proxy.initiate_chat(
                self.real_estate_agent,
                message=initial_message,
                silent=True  # Prevent duplicate message printing
            )

        except KeyboardInterrupt:
            print(colored("\n\nChat session terminated by user.", "yellow"))
        except Exception as e:
            print(colored(f"\nAn error occurred: {str(e)}", "red"))
        finally:
            print(colored("\nChat session ended.", "cyan"))
            self.chat_active = False