# An example using dalaipy to make a simple chat interface

from dalaipy.src import Dalai

model = Dalai()

def repl() -> None:
    try:
        while True:
            _in = input(">> ")
            request = model.generate_request(_in, 'llama.7B')
            print(model.request(request))

    except KeyboardInterrupt as e:
        print("\nExiting...")

if __name__ == "__main__":
    print()
    print("Welcome to LLaMa Chat Interface!")
    print("crtl-c to quit")
    print()
    repl()