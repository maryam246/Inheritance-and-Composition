# Inheritance-and-Composition
# What Are Inheritance and Composition?
Inheritance and composition are two major concepts in object oriented programming that model the relationship between two classes. They drive the design of an application and determine how the application should evolve as new features are added or requirements change.

Both of them enable code reuse, but they do it in different ways.
## What’s Inheritance?
Inheritance models what is called an 'is a' relationship. This means that when you have a Derived class that inherits from a Base class, you created a relationship where Derived is a specialized version of Base.
### for example:
'Hourse is a Animal.'
## What’s Composition?
Composition is a concept that models a has a relationship. It enables creating complex types by combining objects of other types. This means that a class Composite can contain an object of another class Component. This relationship means that a Composite has a Component.
### for example:
'Hourse has a tail.'
# An Overview of Inheritance in Python:
Inheritance is a required feature of every object oriented programming language. This means that Python supports inheritance, and as you’ll see later, it’s one of the few languages that supports multiple inheritance.
## Exceptions Are an Exception
Every class that you create in Python will implicitly derive from object. The exception to this rule are classes used to indicate errors by raising an exception.
## Creating Class Hierarchies
Inheritance is the mechanism you’ll use to create hierarchies of related classes. These related classes will share a common interface that will be defined in the base classes. Derived classes can specialize the interface by providing a particular implementation where applies.
## Abstract Base Classes in Python
Abstract base classes exist to be inherited, but never instantiated. Python provides the abc module to define abstract base classes.
## Implementation Inheritance vs Interface Inheritance
When you derive one class from another, the derived class inherits both:

### The base class interface: 
The derived class inherits all the methods, properties, and attributes of the base class.

### The base class implementation: 
The derived class inherits the code that implements the class interface.
## The Class Explosion Problem
If you are not careful, inheritance can lead you to a huge hierarchical structure of classes that is hard to understand and maintain. This is known as the class explosion problem.
## Inheriting Multiple Classes
Multiple inheritance is the ability to derive a class from multiple base classes at the same time.
## Flexible Designs With Composition
Composition is more flexible than inheritance because it models a loosely coupled relationship. Changes to a component class have minimal or no effects on the composite class. Designs based on composition are more suitable to change.
## Customizing Behavior With Composition
If your design relies on inheritance, you need to find a way to change the type of an object to change its behavior. With composition, you just need to change the policy the object uses.
# Choosing Between Inheritance and Composition in Python
We know how inheritance and composition work in Python.We know that derived classes inherit the interface and implementation of their base classes. We also known that composition allows you to reuse the implementation of another class.
## Inheritance to Model “Is A” Relationship
Inheritance should only be used to model an 'is a' relationship. Liskov’s substitution principle says that an object of type Derived, which inherits from Base, can replace an object of type Base without altering the desirable properties of a program.
## Mixing Features With Mixin Classes
A mixin is a class that provides methods to other classes but are not considered a base class.

A mixin allows other classes to reuse its interface and implementation without becoming a super class. 
## Composition to Model “Has A” Relationship
Composition models a has a relationship. With composition, a class Composite has an instance of class Component and can leverage its implementation. The Component class can be reused in other classes completely unrelated to the Composite.
## Composition to Change Run-Time Behavior
Inheritance, as opposed to composition, is a tightly couple relationship. With inheritance, there is only one way to change and customize behavior. Method overriding is the only way to customize the behavior of a base class. This creates rigid designs that are difficult to change.

Composition, on the other hand, provides a loosely coupled relationship that enables flexible designs and can be used to change behavior at run-time.
## Choosing Between Inheritance and Composition in Python
Python, as an object oriented programming language, supports both inheritance and composition.

Sometimes, it’s hard to see what the relationship between two classes should be, but you can follow these guidelines:

### Use inheritance over composition in Python 
To model a clear is a relationship. First, justify the relationship between the derived class and its base. Then, reverse the relationship and try to justify it. If you can justify the relationship in both directions, then you should not use inheritance between them.

### Use inheritance over composition in Python 
To leverage both the interface and implementation of the base class.

### Use inheritance over composition in Python 
To provide mixin features to several unrelated classes when there is only one implementation of that feature.

### Use composition over inheritance in Python 
To model a has a relationship that leverages the implementation of the component class.

### Use composition over inheritance in Python 
To create components that can be reused by multiple classes in your Python applications.

### Use composition over inheritance in Python 
To implement groups of behaviors and policies that can be applied interchangeably to other classes to customize their behavior.

### Use composition over inheritance in Python 
To enable run-time behavior changes without affecting existing classes.
