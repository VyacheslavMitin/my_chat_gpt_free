import g4f


def main(message):

    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": message
        }],
        stream=True,
    )

    for message in response:
        print(
            message,
            flush=True,  # для вывода в терминал сразу
            end=''
            )


if __name__ == '__main__':
    print("✨ Программа для работы с ChatGPT\n\n".upper())
    try:
        while True:
            request = input("✉️  Введите Ваш запрос: ")
            print("\n💬 Ответ на Ваш запрос: ")
            main(request)
            print('\n'*2)
    except KeyboardInterrupt:
        print("\n🔴 Прерывание работы пользователем")
