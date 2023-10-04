## Source

https://refactoring.guru/design-patterns/template-method

### Important:

> 1. Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets
     subclasses override specific steps of the algorithm without changing its structure.
> 2. Defer the exact steps of an algorithm to a subclass

## Description

## Structure

![alt tag](template-method.png)

## How to use

1. Use the Template Method pattern when you want to let clients extend only particular steps of an algorithm, but not
   the whole algorithm or its structure.
2. Use the pattern when you have several classes that contain almost identical algorithms with some minor differences.
   As a result, you might need to modify all classes when the algorithm changes.

## How to implement

https://refactoring.guru/design-patterns/template-method#checklist

## Running

```
python main.py
python example.py
```