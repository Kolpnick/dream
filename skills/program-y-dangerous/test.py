import requests


def to_dialogs(sentences):
    utters = [{"text": sent, "user": {"user_type": "human"}} for sent in ["hi"] + sentences]
    return {"dialogs": [{"utterances": utters, "bot_utterances": utters, "human_utterances": utters}]}


def main_test():
    url = 'http://0.0.0.0:8022/api/rest/v1.0/ask'
    sentences = ['fuck you', 'you suck', 'I hate you']
    for sent in sentences:
        data = to_dialogs([sent])
        response = requests.post(url, json=data).json()[0][0]
        assert "Let me tell you something you already know." in response, print(sent, '.', response)
    print("Success")


if __name__ == '__main__':
    main_test()
