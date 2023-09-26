## Source

https://refactoring.guru/design-patterns/chain-of-responsibility

### Important:

> 1. Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon
     receiving a request, each handler decides either to process the request or to pass it to the next handler in the
     chain.
>
> 2. A way of passing a request between a chain of objects
> 3. Also known as: CoR, Chain of Command

## Description

## Structure

![alt tag](chain-of-responsibility.png)

## How to use

1. Use the Chain of Responsibility pattern when your program is expected to process different kinds of requests in
   various ways, but the exact types of requests and their sequences are unknown beforehand.
2. Use the pattern when it’s essential to execute several handlers in a particular order.
3. Use the CoR pattern when the set of handlers and their order are supposed to change at runtime.

## How to implement

https://refactoring.guru/design-patterns/chain-of-responsibility#checklist

## Running

```
python main.py
python example.py
```