import g4f


def main(message):
    g4f.debug.logging = False  # Enable debug logging
    g4f.debug.check_version = False  # Disable automatic version checking
    # print(g4f.Provider.Bing.params)  # Print supported args for Bing

    # Using automatic a provider for the given model
    # Streamed completion
    # print('model="gpt-3.5-turbo"')
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{message}"}],
        stream=True,
    )

    for message in response:
        print(message, flush=True, end='')
        print('')

    # # Normal response
    # print('model=g4f.models.gpt_4')
    # response = g4f.ChatCompletion.create(
    #     model=g4f.models.gpt_4,
    #     messages=[{"role": "user", "content": f"{message}"}],
    # )  # Alternative model setting
    #
    # print(response)


if __name__ == '__main__':
    while True:
        request = input("Введите запрос: ")
        main(request)
