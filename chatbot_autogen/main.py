"""Main entry point for the real estate chatbot."""

import os
from agents.real_estate import create_real_estate_agent
from agents.user_proxy import create_user_proxy
from interface.comandline_interface import ChatInterface

def main():
    # Get API key if not set in environment
    if not os.getenv('OPENAI_API_KEY'):
        api_key = input("Please enter your OpenAI API key: ")
        os.environ['OPENAI_API_KEY'] = api_key
    
    # Create agents
    real_estate_agent = create_real_estate_agent()
    user_proxy = create_user_proxy()
    
    # Create and start interface
    chat_interface = ChatInterface(user_proxy, real_estate_agent)
    chat_interface.start()

if __name__ == "__main__":
    main()