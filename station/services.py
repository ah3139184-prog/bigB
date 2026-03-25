import requests


class AIService:

    def analyze(self, data):
        sample = data["rows"][:10]

        prompt = f"""
You are a data analyst.

Dataset:
Columns: {data['columns']}
Sample: {sample}

Give:
- 3 key insights
- 1-2 recommendations
- Keep it simple
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3:mini",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]
    

    def chat(self, data, question, analysis=None, history=None):
        sample = data["rows"][:10]

        history_text = ""
        if history:
            for q in history:
                history_text += f"User: {q.question}\nAI: {q.answer}\n"

                prompt = f"""
        You are a data analyst assistant.

        Dataset:
        Columns: {data['columns']}
        Sample: {sample}

        Previous analysis:
        {analysis}

        Conversation history:
        {history_text}

        User question:
        {question}

        Answer clearly and briefly.
        """

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi3:mini",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]