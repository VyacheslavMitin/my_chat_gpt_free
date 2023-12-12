import g4f


def main(message):

    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{message}"}],
        stream=True,
    )

    for message in response:
        print(message, flush=True, end='')
        print('')


if __name__ == '__main__':
    while True:
        request = input("Введите запрос: ")
        main(request)
