/// title: Why Object Oriented Programming has no class
/// author: Edvard Thörnros
/// template: simple.html
/// first: 2021-05-06
/// last: 2021-05-06
/// short: A very controversial opinion about object oriented programming. Mostly that OOP doesn't have classes.

# Why OOP lacks class
As a student and software fanatic I've consumed a lot of media regarding
object oriented programing (OOP). In general, there's also this ~weird~ idea
that OOP is about `class`-es, and `inheritance`. But the more I learn, the less
I agree with this. I will in this short text try to explain what I mean.

## The problem with teaching
OOP is for me a way to structure programs and behaviors.
And it's often taught in, according to me, a harmful way.
The standard example I've been taught and seen is:
```python
class Animal:
    def sound():
        print("-")

class Cow:
    def sound():
        print("Moooo")

class Dog:
    def sound():
        print("Woof")
```
Now every where use an `Animal`, you can swap in a `Cow` or a `Dog` to
get different functionality.

In this very simply example, the problem is not obvious, but we've now locked
ourselves into a very rigid design pattern. We've made the assumption that
all `Animals` are _one and only one_ subclass. So we cannot have a `DogCow` with
shared functionality in a some what sane way.

Many students fall into a pit of thinking in these rigid class hierarchies,
which makes it really hard to solve some problems in a nice way.

## Going back to the roots
The original idea - which I believe is more powerful - is the idea of sending
messages according to a well defined protocol. Letting the "objects" that
send and receive be swappable gives a lot of flexibility, and is perhaps what what
the original idea should have been
[design should have been called](http://www.purl.org/stefan_ram/pub/doc_kay_oop_en).

## What to do about it
For me, personally, OOP can be done without classes and inheritance. Inheritance
is according to me an anti-pattern. The better solution for this specific problem,
would according to me be callbacks. Which would remove every single line
of code from the example.

But that's only my opinion.
