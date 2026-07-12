from providers.gapgpt import GapGPTProvider


class ProviderManager:

    def __init__(self):

        self.providers = {
            "gapgpt": GapGPTProvider()
        }

    def get(self, provider: str = "gapgpt"):

        return self.providers[provider]


provider_manager = ProviderManager()