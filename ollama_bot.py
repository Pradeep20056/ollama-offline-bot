import requests

class OllamaBot:
    def __init__(self, model="mistral"):
        self.model = model

    def chat(self, prompt):
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )
            return response.json().get("response", "").strip()
        except Exception as e:
            return f"[Error] {e}"
