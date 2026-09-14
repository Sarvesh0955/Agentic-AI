import requests
from bs4 import BeautifulSoup
from ollama import chat


def get_webpage_text(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove things that aren't useful for summarization
    for element in soup(["script", "style", "nav", "footer"]):
        element.decompose()

    return soup.get_text(" ", strip=True)


def summarize(text):
    response = chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful website summarizer. "
                    "Summarize the provided webpage clearly and concisely."
                ),
            },
            {
                "role": "user",
                "content": f"""
Summarize this webpage.

Give me:
1. A 2-3 sentence overview
2. The 5 most important points
3. The main conclusion

Webpage:

{text}
""",
            },
        ],
    )

    return response.message.content


url = input("Enter website URL: ")

text = get_webpage_text(url)

print("\nGenerating summary...\n")

summary = summarize(text)

print(summary)