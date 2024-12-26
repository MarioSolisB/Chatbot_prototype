from typing import List, Dict
import autogen
from config.settings import GPT_MODEL, OPENAI_API_KEY

def create_llm_config(tools: List[Dict] = None) -> Dict:
    config = {
        "config_list": [{
            "model": GPT_MODEL,
            "api_key": OPENAI_API_KEY
        }],
        "temperature": 0.1
    }
    
    if tools:
        config["tools"] = tools
    
    return config