## Design Pattern With Python

Source: https://refactoring.guru/

Email: lexuanmanhdut101199@gmail.com

## Catalog of Design Pattern

1. [Creational Design Patterns](creational-design-pattern)
    - [Factory Method](creational-design-pattern/factory-method)
    - [Abstract Factory](creational-design-pattern/abstract-factory)
    - [Builder](creational-design-pattern/builder)
    - [Prototype](creational-design-pattern/prototype)
    - [Singleton](creational-design-pattern/singleton)
2. [Structural Design Patterns](structural-design-pattern)
    - [Adapter](structural-design-pattern/adapter)
    - [Bridge](structural-design-pattern/bridge)
    - [Composite](structural-design-pattern/composite)
    - [Decorator](structural-design-pattern/decorator)
    - [Facade](structural-design-pattern/facade)
    - [Flyweight](structural-design-pattern/flyweight)
    - [Proxy](structural-design-pattern/proxy)
3. Behavior Design Patterns
    - Chain of Responsibility
    - Command
    - Iterator
    - Mediator
    - Memento
    - Observer
    - State
    - Strategy
    - Template Method
    - Visitor

| Attribute         | Creational Design Pattern                                                                                                                                                                   | Structural Design Pattern                                                                                                                                                                                                                   | Behavioral Design Pattern                                                                                                                                                                                              |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Purpose**       | Object creation                                                                                                                                                                             | Structure creation                                                                                                                                                                                                                          | Managing object interactions                                                                                                                                                                                           |
| **Use Cases**     | - When you want to hide object creation logic.<br> - When you want to control object creation.<br> - When you want to share existing objects instead of creating new ones.                  | - When you want to create complex structures by composing objects.<br> - When you want to change an object's interface without modifying the source code (Adapter).                                                                         | - When you want to manage how objects interact with each other.<br> - When you want to define how objects send messages to each other.                                                                                 |
| **Examples**      | - Singleton<br> - Factory Method<br> - Abstract Factory<br> - Builder<br> - Prototype                                                                                                       | - Adapter<br> - Bridge<br> - Composite<br> - Decorator<br> - Facade<br> - Proxy                                                                                                                                                             | - Observer<br> - Strategy<br> - Command<br> - State<br> - Visitor<br> - Memento                                                                                                                                        |
| **Applications**  | - Resource management (e.g., database connections, threads, graphical entities).<br> - Ensuring a class has only one object instance (Singleton).                                           | - In graphical systems.<br> - When you want to switch between different versions of an object without modifying the source code (Adapter).                                                                                                  | - Implementing various user interaction interfaces (Command).<br> - Notifying objects about changes (Observer).                                                                                                        |
| **Relationships** | - Provides ways to create objects.<br> - Primary responsibility is object creation.<br> - Sometimes combined with creational algorithms (e.g., Singleton can be implemented using Builder). | - Creates complex data structures from existing objects.<br> - Interacts with objects by encapsulating them in a new structure.<br> - Sometimes combined with creational patterns (e.g., Adapter can use Factory Method to create objects). | - Manages how objects interact with each other.<br> - Defines how objects send messages and handles them.<br> - Sometimes uses creational patterns to create objects involved in interactions (e.g., Command Pattern). |

## Directory

```
$ Design Pattern
.
├── ceational-design-pattern
│   ├── factory-method
│       ├── README.md
│       ├── README-VI.md
│       ├── main.py
│       ├── example.py
│   ├── abstract-method
│       ├── README.md
│       ├── README-VI.md
│       ├── main.py
│       ├── example.py
│   ├── builder
│       ├── README.md
│       ├── README-VI.md
│       ├── main.py
│       ├── example.py
│   ├── prototype
│       ├── README.md
│       ├── README-VI.md
│       ├── main.py
│       ├── example.py
│   ├── singleton
│       ├── README.md
│       ├── README-VI.md
│       ├── main.py
│       ├── example.py
├── structural-design-pattern
│   ├── adapter
│       ├── README.md
│       ├── README-VI.md
│       ├── main.py
│       ├── example.py
│   ├── bridge
│       ├── README.md
│       ├── README-VI.md
│       ├── main.py
│       ├── example.py
│   ├── composite
│       ├── README.md
│       ├── README-VI.md
│       ├── main.py
│       ├── example.py
│   ├── decorator
│       ├── README.md
│       ├── README-VI.md
│       ├── main.py
│       ├── example.py
│   ├── facade
│       ├── README.md
│       ├── README-VI.md
│       ├── main.py
│       ├── example.py
│   ├── flyweight
│       ├── README.md
│       ├── README-VI.md
│       ├── main.py
│       ├── example.py
│   ├── proxy
│       ├── README.md
│       ├── README-VI.md
│       ├── main.py
│       ├── example.py
├── behavior-design-pattern
└── README.md
```

