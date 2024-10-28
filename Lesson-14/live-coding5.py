def make_greeter(greeting):
    def greeter(name):
        return f'{greeting}, {name}!'
        # return greeting + ', ' + name + '!'
    return greeter


hello_greeter = make_greeter('Hello')
print(hello_greeter('Alice'))


hi_greeter = make_greeter('Hi')
print(hi_greeter('Bob'))


merhaba_greeter = make_greeter('Merhaba')
print(merhaba_greeter('Metin'))