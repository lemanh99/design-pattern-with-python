## Source

https://refactoring.guru/design-patterns/mediator

### Important:

> 1. Mediator is a behavioral design pattern that lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.
> 2. Defines simplified communication between classes

## Description

## Structure

![alt tag](mediator.png)

## How to use

1. Use the Mediator pattern when it’s hard to change some of the classes because they are tightly coupled to a bunch of
   other classes.
2. Use the pattern when you can’t reuse a component in a different program because it’s too dependent on other
   components.
3. Use the Mediator when you find yourself creating tons of component subclasses just to reuse some basic behavior in
   various contexts.

## How to implement

https://refactoring.guru/design-patterns/mediator#checklist

## Running

```
python main.py
python example.py
```