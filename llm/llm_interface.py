import requests
import yaml


class LLMInterface:
    def __init__(self, config_path):
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        self.endpoint_url = self.config['llm']['endpoint_url']
        self.api_key = self.config['llm']['api_key']

    def initialize_llm(self):
        """Initializes the LLM using the configuration details."""
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        # Example payload, adjust as needed
        payload = {
            'model_name': self.config['llm']['model_name'],
            'token_limit': self.config['llm']['token_limit']
        }
        response = requests.post(self.endpoint_url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': response.text}
