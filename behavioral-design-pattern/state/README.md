## Source

https://refactoring.guru/design-patterns/state

### Important:

> 1.State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It
> appears as if the object changed its class.
> 2. Alter an object's behavior when its state changes

## Description

## Structure

![alt tag](state.png)

## How to use

1. Use the State pattern when you have an object that behaves differently depending on its current state, the number of
   states is enormous, and the state-specific code changes frequently.
2. Use the pattern when you have a class polluted with massive conditionals that alter how the class behaves according
   to the current values of the class’s fields.
3. Use State when you have a lot of duplicate code across similar states and transitions of a condition-based state
   machine.

## How to implement

https://refactoring.guru/design-patterns/state#checklist

## Running

```
python main.py
python example.py
```