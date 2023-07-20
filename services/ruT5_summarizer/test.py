import requests


def test_skill():
    url = "http://0.0.0.0:8173/respond_batch"

    input_data = {"sentences": ["ChatGPT (Generative Pre-trained Transformer или генеративный предварительно обученный "
                                "трансформер) — чат-бот с искусственным интеллектом, разработанный компанией OpenAI и "
                                "способный работать в диалоговом режиме, поддерживающий запросы на естественных языках."
                                " ChatGPT — большая языковая модель, для тренировки которой использовались методы "
                                "обучения с учителем и обучения с подкреплением. Данный чат-бот основывается на другой "
                                "языковой модели от OpenAI — GPT-3.5 — улучшенной версии модели GPT-3. 14 марта 2023 "
                                "года была выпущена языковая модель GPT-4, доступная тестировщикам и платным "
                                "подписчикам ChatGPT Plus. В новой версии у ИИ появилась возможность обработки не "
                                "только текста, но и картинок."]}
    desired_output = ["Компания OpenAI разработала чат-бот с искусственным интеллектом ChatGPT — чат-бот с "
                      "искусственным интеллектом, способный работать в диалоговом режиме, поддерживающий запросы на "
                      "естественных языках. Это чат-бот с искусственным интеллектом, разработанный компанией OpenAI и "
                      "способный работать в диалоговом режиме, поддерживающий запросы на естественных языках."]

    result = requests.post(url, json=input_data).json()[0]['batch']

    assert result == desired_output
    print("SUCCESS!")


if __name__ == "__main__":
    test_skill()
