## Source

https://refactoring.guru/design-patterns/strategy

### Important:

> 1. Strategy is a behavioral design pattern that lets you define a family of algorithms, put each of them into a
     > separate class, and make their objects interchangeable.
> 2. Encapsulates an algorithm inside a class

## Description

## Structure

![alt tag](strategy.png)

## How to use

1. Use the Strategy pattern when you want to use different variants of an algorithm within an object and be able to
   switch from one algorithm to another during runtime.
2. Use the Strategy when you have a lot of similar classes that only differ in the way they execute some behavior.
3. Use the pattern to isolate the business logic of a class from the implementation details of algorithms that may not
   be as important in the context of that logic.
4. Use the pattern when your class has a massive conditional operator that switches between different variants of the
   same algorithm.

## How to implement

https://refactoring.guru/design-patterns/strategy#checklist

## Running

```
python main.py
python example.py
```