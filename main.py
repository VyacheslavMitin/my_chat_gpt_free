import g4f


def main(message):

    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": f"{message}"
        }],
        stream=True,
    )

    for message in response:
        print(message, flush=False, end='')
        print('\n')


if __name__ == '__main__':
    print("Модуль для вызова ChatGPT\n".upper())
    try:
        while True:
            request = input("🟢 Введите запрос: ")
            main(request)
    except KeyboardInterrupt:
        print("\nПрерывание работы пользователем")
