"""Formatting utilities for the chat interface."""

import os
from termcolor import colored

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def format_welcome_message():
    """Format and return the welcome message.
    
    Returns:
        str: Formatted welcome message
    """
    return f"""
{colored("=== NEXUS Residence Chat Interface ===", "blue", attrs=["bold"])}

{colored("Welcome to the NEXUS Residence chat system!", "cyan")}

Instructions:
- Type your messages and press Enter to send
- Type 'exit' to end the conversation
- Type 'clear' to clear the screen

{colored("====================================", "blue")}
"""

def format_user_prompt():
    """Format the user input prompt.
    
    Returns:
        str: Formatted prompt
    """
    return colored("\nYou: ", "green")