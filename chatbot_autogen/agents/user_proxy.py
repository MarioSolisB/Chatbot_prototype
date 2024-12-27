import autogen
from chatbot_autogen.config.settings import USER_PROXY_NAME

def create_user_proxy():
    return autogen.UserProxyAgent(
        name=USER_PROXY_NAME,
        human_input_mode="ALWAYS", 
        code_execution_config=False,
        default_auto_reply=None  # Ensure no auto-replies
    )