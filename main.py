import json
import os
import requests

class OllamaChat:

    def __init__(self):
        self.ollama_server = "localhost:11434"
        self.ollama_model = "llama3.2:1b"

        if "MODEL" in os.environ:
            self.ollama_model = os.environ["MODEL"]
        if "OLLAMA" in os.environ:
            self.ollama_server = os.environ["OLLAMA"]

        self.headers = {'Content-type': 'application/json'}

    def chat(self, prompt):
        response = requests.post(f"http://{self.ollama_server}/api/generate", json={'model':self.ollama_model, 'prompt': prompt})
        print(response)

        if response.status_code == 200:
            full_text = response.text

            output = ""
            for line in full_text.splitlines():
                line_json = json.loads(line)
                res_text = line_json['response']
                done = line_json['done']

                if done:
                    break
                output += res_text

            return output
        else:
            return f"{response}: Error Obtaining Response from server: {response.text}"



if __name__ == "__main__":
    oc = OllamaChat()
    answer = oc.chat("How much does a duck weigh?")
    print(answer)