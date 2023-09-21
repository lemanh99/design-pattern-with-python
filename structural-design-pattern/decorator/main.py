class Component:
    def execute(self):
        pass


class ConcreteComponent(Component):
    def execute(self):
        print("Executing ConcreteComponent")


class BaseDecorator(Component):
    _component: Component = None

    def __init__(self, component):
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def execute(self):
        self._component.execute()


class ConcreteDecorator(BaseDecorator):
    def execute(self):
        print("Executing ConcreteDecorator")
        self.component.execute()


class ClientCode:
    def __init__(self, component):
        self.component = component

    def execute(self):
        print("Executing ClientCode:")
        self.component.execute()


if __name__ == "__main__":
    component = ConcreteComponent()
    decorator = ConcreteDecorator(component)
    client = ClientCode(decorator)
    client.execute()
