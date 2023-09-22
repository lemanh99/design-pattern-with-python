"""
Source: https://refactoring.guru/design-patterns/adapter/python/example
"""


class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


class Client:
    def req_data(self, target: Target) -> None:
        print(target.request(), end="")

if __name__ == "__main__":
    client = Client()
    target = Target()
    print(target.request(), end="\n\n")
    adaptee = Adaptee()
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
    print("Client: I can work just fine with the Target objects:")
    client.req_data(target)
    print("\n")
    adapter = Adapter()
    print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
    print(f"Adaptee: {adapter.specific_request()}", end="\n\n")
    print("Client: But I can work with it via the Adapter:")
    client.req_data(adapter)