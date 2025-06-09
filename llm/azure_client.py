from config import CONFIG
from openai import AzureOpenAI, OpenAIError

class AzureClient():

    def __init__(self, api_version,api_key,azure_endpoint,azure_deployment, model):
        self.client = AzureOpenAI(
            api_version=api_version,
            api_key=api_key,
            azure_endpoint=azure_endpoint,
            azure_deployment=azure_deployment
        )
        self.model = model
        self.conversation = []

    def append_conversation(self, role: str, content: str) -> None:
        self.conversation.append({
            'role': role,
            'content': content
        })

    def api_version(self) -> str:
        return self.client._api_version

    def clear_conversation(self) -> None:
        self.conversation = []

    def generate(self, messages: list[dict[str:str]]) -> str:
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
            )
            return completion.choices[0].message.content
        except OpenAIError as e:
            print(e)
            return None  
