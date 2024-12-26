import autogen
from config.settings import USER_PROXY_NAME

def create_user_proxy():
    return autogen.UserProxyAgent(
        name=USER_PROXY_NAME,
        human_input_mode="TERMINATE",
        code_execution_config=False
    )