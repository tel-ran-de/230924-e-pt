def greet(name):
    return f'Hello {name}!'


if __name__ == '__main__':
    print('Файл запущен напрямую')

    def greet_main(name):
        return f'Hello {name}!'

    print(greet_main('Frank'))