
# Section 02 - A Quick Refresher

##  Multi-Line Statements and Strings

Certain physical newlines are ignored in order to form a complete logical line of code.

#### Implicit Examples


```
a = [1, 
    2, 
    3]
```


```
a
```




    [1, 2, 3]



You may also add comments to the end of each physical line:


```
a = [1, #first element
    2, #second element
    3, #third element
    ]
```


```
a
```




    [1, 2, 3]



Note if you do use comments, you must close off the collection on a new line.

i.e. the following will not work since the closing ] is actually part of the comment:


```
a = [1, # first element
    2 #second element]
```


      File "<ipython-input-7-ca1d73612a61>", line 2
        2 #second element]
                          ^
    SyntaxError: unexpected EOF while parsing
    


This works the same way for tuples, sets, and dictionaries.


```
a = (1, # first element
    2, #second element
    3, #third element
    )
```


```
a
```




    (1, 2, 3)




```
a = {1, # first element
    2, #second element
    }
```


```
a
```




    {1, 2}




```
a = {'key1': 'value1', #comment,
    'key2': #comment
    'value2' #comment
    }
```


```
a
```




    {'key1': 'value1', 'key2': 'value2'}



We can also break up function arguments and parameters:


```
def my_func(a, #some comment
           b, c):
    print(a, b, c)
```


```
my_func(10, #comment
       20, #comment
       30)
```

    10 20 30
    

#### Explicit Examples

You can use the ``\`` character to explicitly create multi-line statements.


```
a = 10
b = 20
c = 30
if a > 5 \
    and b > 10 \
    and c > 20:
    print('yes!!')
```

    yes!!
    

The identation in continued-lines does not matter:


```
a = 10
b = 20
c = 30
if a > 5 \
    and b > 10 \
        and c > 20:
    print('yes!!')
```

    yes!!
    

#### Multi-Line Strings

You can create multi-line strings by using triple delimiters (single or double quotes)


```
a = '''this is
a multi-line string'''
```


```
print(a)
```

    this is
    a multi-line string
    

Note how the newline character we typed in the multi-line string was preserved. Any character you type is preserved. You can also mix in escaped characters line any normal string.


```
a = """some items:\n
    1. item 1
    2. item 2"""
```


```
print(a)
```

    some items:
    
        1. item 1
        2. item 2
    

Be careful if you indent your multi-line strings - the extra spaces are preserved!


```
def my_func():
    a = '''a multi-line string
    that is actually indented in the second line'''
    return a
```


```
print(my_func())
```

    a multi-line string
        that is actually indented in the second line
    


```
def my_func():
    a = '''a multi-line string
that is not indented in the second line'''
    return a
```


```
print(my_func())
```

    a multi-line string
    that is not indented in the second line
    

Note that these multi-line strings are **not** comments - they are real strings and, unlike comments, are part of your compiled code. They are however sometimes used to create comments, such as ``docstrings``, that we will cover later in this course.

In general, use ``#`` to comment your code, and use multi-line strings only when actually needed (like for docstrings).

Also, there are no multi-line comments in Python. You simply have to use a ``#`` on every line.


```
# this is
#    a multi-line
#    comment
```

The following works, but the above formatting is preferrable.


```
# this is
    # a multi-line
    # comment
```

##  Conditionals

A conditional is a construct that allows you to branch your code based on conditions being met (or not)

This is achieved using **if**, **elif** and **else** or the **ternary operator** (aka conditional expression)


```
a = 2
if a < 3:
    print('a < 3')
else:
    print('a >= 3')
```

    a < 3
    

**if** statements can be nested:


```
a = 15

if a < 5:
    print('a < 5')
else:
    if a < 10:
        print('5 <= a < 10')
    else:
        print('a >= 10')
```

    a >= 10
    

But the **elif** statement provides far better readability:


```
a = 15
if a < 5:
    print('a < 5')
elif a < 10:
    print('5 <= a < 10')
else:
    print('a >= 10')
```

    a >= 10
    

In Python, **elif** is the closest you'll find to the switch/case statement available in some other languages.

Python also provides a conditional expression (ternary operator):

X if (condition) else Y

returns (and evaluates) X if (condition) is True, otherwise returns (and evaluates) Y


```
a = 5
res = 'a < 10' if a < 10 else 'a >= 10'
print(res)
```

    a < 10
    


```
a = 15
res = 'a < 10' if a < 10 else 'a >= 10'
print(res)
```

    a >= 10
    

Note that **X** and **Y** can be any expression, not just literal values:


```
def say_hello():
    print('Hello!')
    
def say_goodbye():
    print('Goodbye!')
```


```
a = 5
say_hello() if a < 10 else say_goodbye()
```

    Hello!
    


```
a = 15
say_hello() if a < 10 else say_goodbye()
```

    Goodbye!
    

##  Functions

Python has many built-in functions and methods we can use

Some are available by default:


```
s = [1, 2, 3]
len(s)
```




    3



While some need to be imported:


```
from math import sqrt
```


```
sqrt(4)
```




    2.0



Entire modules can be imported:


```
import math
```


```
math.exp(1)
```




    2.718281828459045



We can define our own functions:


```
def func_1():
    print('running func1')
```


```
func_1()
```

    running func1
    

Note that to "call" or "invoke" a function we need to use the **()**.

Simply using the function name without the **()** refers to the function, but does not call it:


```
func_1
```




    <function __main__.func_1>



We can also define functions that take parameters:


```
def func_2(a, b):
    return a * b
```

Note that **a** and **b** can be any type (this is an example of polymorphism - which we will look into more detail later in this course). 

But the function will fail to run if **a** and **b** are types that are not "compatible" with the ***** operator:


```
func_2(3, 2)
```




    6




```
func_2('a', 3)
```




    'aaa'




```
func_2([1, 2, 3], 2)
```




    [1, 2, 3, 1, 2, 3]




```
func_2('a', 'b')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-16-4e1c1906827b> in <module>()
    ----> 1 func_2('a', 'b')
    

    <ipython-input-12-abd6021cc10d> in func_2(a, b)
          1 def func_2(a, b):
    ----> 2     return a * b
    

    TypeError: can't multiply sequence by non-int of type 'str'


It is possible to use **type annotations**:


```
def func_3(a: int, b:int):
    return a * b
```


```
func_3(2, 3)
```




    6




```
func_3('a', 2)
```




    'aa'



But as you can see, these do not enforce a data type! They are simply metadata that can be used by external libraries, and many IDE's.

Functions are objects, just like integers are objects, and they can be assigned to variables just as an integer can:


```
my_func = func_3
```


```
my_func('a', 2)
```




    'aa'



Functions **must** always return something. If you do not specify a return value, Python will automatically return the **None** object:


```
def func_4():
    # does something but does not return a value
    a = 2
```


```
res = func_4()
```


```
print(res)
```

    None
    

The **def** keyword is an executable piece of code that creates the function (an instance of the **function** class) and essentially assigns it to a variable name (the function **name**). 

Note that the function is defined when **def** is reached, but the code inside it is not evaluated until the function is called.

This is why we can define functions that call other functions defined later - as long as we don't call them before all the necessary functions are defined.

For example, the following will work:


```
def fn_1():
    fn_2()
    
def fn_2():
    print('Hello')
    
fn_1()
```

    Hello
    

But this will not work:


```
def fn_3():
    fn_4()

fn_3()

def fn_4():
    print('Hello')
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-32-6d843cb5e628> in <module>()
          2     fn_4()
          3 
    ----> 4 fn_3()
          5 
          6 def fn_4():
    

    <ipython-input-32-6d843cb5e628> in fn_3()
          1 def fn_3():
    ----> 2     fn_4()
          3 
          4 fn_3()
          5 
    

    NameError: name 'fn_4' is not defined


We also have the **lambda** keyword, that also creates a new function, but does not assign it to any specific name - instead it just returns the function object - which we can, if we wish, assign to a variable ourselves:


```
func_5 = lambda x: x**2
```


```
func_5
```




    <function __main__.<lambda>>




```
func_5(2)
```




    4



We'll examine lambdas in more detail later in this course.

##  While Loops

The **while** loop is a way to repeatg a block of code as long as a specified condition is met.

``while <exp is true>:
    code block``


```
i = 0
while i < 5:
    print(i)
    i += 1
```

    0
    1
    2
    3
    4
    

Note that there is no guarantee that a **while** loop will execute at all, not even once, because the condition is tested **before** the loop runs.


```
i = 5
while i < 5:
    print(i)
    i += 1
```

Some languages have a concept of a while loop that is guaranteed to execute at least once:

``do
    code block
while <exp is true>
``

There is no such thing in Python, but it's easy enough to write code that works that way.

We create an infinite loop and test the condition inside the loop and break out of the loop when the condition becomes false:


```
 i = 5

while True:
    print(i)
    if i >= 5:
        break

```

    5
    

As you can see the loop executed once (and will always execute at least once, no matter the starting value of i.)

This is a standard pattern and can be useful in a variety of scenarios.

A simple example might be getting repetitive user input until the user performs and action or provides some specific value.
For example, suppose we want to use the console to let users enter their name. We just want to make sure their name is at least 2 characters long, contains printable characters only, and only contains alphabetic characters:
We might try it this way:


```
min_length = 2

name = input('Please enter your name:')

while not(len(name) >= min_length  and name.isprintable() and name.isalpha()):
    name = input('Please enter your name:')

print('Hello, {0}'.format(name))

```

    Please enter your name:a123
    Please enter your name:a
    Please enter your name:fred
    Hello, fred
    

This works just fine, but notice that we had to write the code to elicit user input **twice** in our code. This is not good practice, and we can easily clean this up as follows:


```
min_length = 2

while True:
    name = input('Please enter your name:')
    if len(name) >= min_length  and name.isprintable() and name.isalpha():
        break

print('Hello, {0}'.format(name))
```

    Please enter your name:a
    Please enter your name:123
    Please enter your name:fred
    Hello, fred
    

We saw how the **break** statement exits the **while** loop and execution resumes on the line immediately after the while code block.

Sometimes, we just want to cut the current iteration short, but continue looping, without exiting the loop itself.

This is done using the **continue** statement:


```
a = 0
while a < 10:
    a += 1
    if a % 2:
        continue
    print(a)
```

    2
    4
    6
    8
    10
    

Note that there are much better ways of doing this! We'll cover that in later videos (comprehensions, generators, etc)

The **while** loop also can be used with an **else** clause!!

The **else** is executed if the while loop terminated without hitting a **break** statement (we say the loop terminated **normally**)

Suppose we want to test if some value is present in some list, and if not we want to append it to the list (again there are better ways of doing this):

First, here's how we might do it without the benefit of the **else** clause:


```
l = [1, 2, 3]
val = 10

found = False
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1
    
if not found:
    l.append(val)
print(l)
```

    [1, 2, 3, 10]
    

Using the **else** clause is easier:


```
l = [1, 2, 3]
val = 10

idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)

print(l)
```

    [1, 2, 3, 10]
    


```
l = [1, 2, 3]
val = 3

idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)

print(l)
```

    [1, 2, 3]
    

##  Loop Break and Continue inside a Try...Except...Finally

Recall that in a ``try`` statement, the ``finally`` clause always runs:


```
a = 10
b = 1
try:
    a / b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('this always executes')
```

    this always executes
    


```
a = 10
b = 0
try:
    a / b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('this always executes')
```

    division by 0
    this always executes
    

So, what happens when using a ``try`` statement within a ``while`` loop, and a ``continue`` or ``break`` statement is encountered?


```
a = 0
b = 2

while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        continue
    finally:
        print('{0}, {1} - always executes'.format(a, b))
        
    print('{0}, {1} - main loop'.format(a, b))
```

    -------------
    1, 1 - always executes
    1, 1 - main loop
    -------------
    2, 0 - division by 0
    2, 0 - always executes
    -------------
    3, -1 - always executes
    3, -1 - main loop
    

As you can see in the above result, the ``finally`` code still executed, even though the current iteration was cut short with the ``continue`` statement. 

This works the same with a ``break`` statement:


```
a = 0
b = 2

while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        break
    finally:
        print('{0}, {1} - always executes'.format(a, b))
        
    print('{0}, {1} - main loop'.format(a, b))
```

    -------------
    1, 1 - always executes
    1, 1 - main loop
    -------------
    2, 0 - division by 0
    2, 0 - always executes
    

We can even combine all this with the ``else`` clause:


```
a = 0
b = 2

while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        break
    finally:
        print('{0}, {1} - always executes'.format(a, b))
        
    print('{0}, {1} - main loop'.format(a, b))
else:
    print('\n\nno errors were encountered!')
```

    -------------
    1, 1 - always executes
    1, 1 - main loop
    -------------
    2, 0 - division by 0
    2, 0 - always executes
    


```
a = 0
b = 5

while a < 3:
    print('-------------')
    a += 1
    b -= 1
    try:
        res = a / b
    except ZeroDivisionError:
        print('{0}, {1} - division by 0'.format(a, b))
        res = 0
        break
    finally:
        print('{0}, {1} - always executes'.format(a, b))
        
    print('{0}, {1} - main loop'.format(a, b))
else:
    print('\n\nno errors were encountered!')
```

    -------------
    1, 4 - always executes
    1, 4 - main loop
    -------------
    2, 3 - always executes
    2, 3 - main loop
    -------------
    3, 2 - always executes
    3, 2 - main loop
    
    
    no errors were encountered!
    

##  The For Loop

In Python, an **iterable** is an **object** capable of returning values one at a time.

Many objects in Python are iterable: lists, strings, file objects and many more.

Note: Our definition of an iterable did not state it was a collection of values - we only said it is an object that can return values one at a time - that's a subtle difference that we'll examine when we look into iterators and generators.

The **for** keyword can be used to iterate an iterable.

If you come with a background in another programming language, you have probably seen **for** loops defined this way:

``for (int i=0; i < 5; i++) {
    //code block
}``

This form of the **for** loop is simply a _repetition_, very similar to a **while** loop - in fact it is equivalent to what we could write in Python as follows:


```
i = 0
while i < 5:
    #code block
    print(i)
    i += 1
i = None
```

    0
    1
    2
    3
    4
    

But that's **NOT** what the **for** statement does in Python - the **for** statement is a way to **iterate** over iterables, and has nothing to do with the **for** loop we just saw. The closest equivalent we have in Python is the **while** loop written as above.

To use the **for** loop in Python, we **require** an iterable object to work with.

A simple iterable object is generated via the ``range()`` function


```
for i in range(5):
    print(i)
```

    0
    1
    2
    3
    4
    

Many objects are iterable in Python:


```
for x in [1, 2, 3]:
    print(x)
```

    1
    2
    3
    


```
for x in 'hello':
    print(x)
```

    h
    e
    l
    l
    o
    


```
for x in ('a', 'b', 'c'):
    print(x)
```

    a
    b
    c
    

When we iterate over an iterable, each iteration returns the "next" value (or object) in the iterable:


```
for x in [(1, 2), (3, 4), (5, 6)]:
    print(x)
```

    (1, 2)
    (3, 4)
    (5, 6)
    

We can even assign the individual tuple values to specific named variables:


```
for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)
```

    1 2
    3 4
    5 6
    

We will cover iterables in a lot more detail later in this course.

The **break** and **continue** statements work just as well in **for** loops as they do in **while** loops:


```
for i in range(5):
    if i == 3:
        continue
    print(i)
```

    0
    1
    2
    4
    


```
for i in range(5):
    if i == 3:
        break
    print(i)
```

    0
    1
    2
    

The **for** loop, like the **while** loop, also supports an **else** clause which is executed if and only if the loop terminates normally (i.e. did not exit because of a **break** statement)


```
for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('No multiples of 7 encountered')
```

    1
    2
    3
    4
    No multiples of 7 encountered
    


```
for i in range(1, 8):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('No multiples of 7 encountered')
```

    1
    2
    3
    4
    5
    6
    7
    multiple of 7 found
    

Similarly to the **while** loop, **break** and **continue** work just the same in the context of a **try** statement's **finally** clause.


```
for i in range(5):
    print('--------------------')
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print('divided by 0')
        continue
    finally:
        print('always runs')
    print(i)
```

    --------------------
    always runs
    0
    --------------------
    always runs
    1
    --------------------
    always runs
    2
    --------------------
    divided by 0
    always runs
    --------------------
    always runs
    4
    

There are a number of standard techniques to iterate over iterables:


```
s = 'hello'
for c in s:
    print(c)
```

    h
    e
    l
    l
    o
    

But sometimes, for indexable iterable types (e.g. sequences), we want to also know the index of the item in the loop:


```
s = 'hello'
i = 0
for c in s:
    print(i, c)
    i += 1
```

    0 h
    1 e
    2 l
    3 l
    4 o
    

Slightly better approach might be:


```
s = 'hello'

for i in range(len(s)):
    print(i, s[i])

```

    0 h
    1 e
    2 l
    3 l
    4 o
    

or even better:


```
s = 'hello'

for i, c in enumerate(s):
    print(i, c)
```

    0 h
    1 e
    2 l
    3 l
    4 o
    

We'll come back to all these iteration techniques in a lot more detail throughout this course.

##  Custom Classes

We'll cover classes in a lot of detail in this course, but for now you should have at least some understanding of classes in Python and how to create them.

To create a custom class we use the `class` keyword, and we can initialize class attributes in the special method `__init__`.


```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
```

We create **instances** of the `Rectangle` class by calling it with arguments that are passed to the `__init__` method as the second and third arguments. The first argument (`self`) is automatically filled in by Python and contains the object being created.

Note that using `self` is just a convention (although a good one, and you shgoudl use it to make your code more understandable by others), you could really call it whatever (valid) name you choose.

But just because you can does not mean you should!


```
r1 = Rectangle(10, 20)
r2 = Rectangle(3, 5)
```


```
r1.width
```




    10




```
r2.height
```




    5



`width` and `height` are attributes of the `Rectangle` class. But since they are just values (not callables), we call them **properties**.

Attributes that are callables are called **methods**.

You'll note that we were able to retrieve the `width` and `height` attributes (properties) using a dot notation, where we specify the object we are interested in, then a dot, then the attribute we are interested in.

We can add callable attributes to our class (methods), that will also be referenced using the dot notation.

Again, we will create instance methods, which means the method will require the first argument to be the object being used when the method is called.


```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(the_referenced_object):
        return 2 * (the_referenced_object.width + the_referenced_object.height)
```


```
r1 = Rectangle(10, 20)
```


```
r1.area()
```




    200



When we ran the above line of code, our object was `r1`, so when `area` was called, Python in fact called the method `area` in the Rectangle class automatically passing `r1` to the `self` parameter.

This is why we can use a name other than self, such as in the perimeter method:


```
r1.perimeter()
```




    60



Again, I'm just illustrating a point, don't actually do that!


```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
```


```
r1 = Rectangle(10, 20)
```

Python defines a bunch of **special** methods that we can use to give our classes functionality that resembles functionality of built-in and standard library objects.

Many people refer to them as *magic* methods, but there's nothing magical about them - unlike magic, they are well documented and understood!!

These **special** methods provide us an easy way to overload operators in Python.

For example, we can obtain the string representation of an integer using the built-in `str` function:


```
str(10)
```




    '10'



What happens if we try this with our Rectangle object?


```
str(r1)
```




    '<__main__.Rectangle object at 0x000002375E7006A0>'



Not exactly what we might have expected. On the other hand, how is Python supposed to know how to display our rectangle as a string?

We could write a method in the class such as:


```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def to_str(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)
```

So now we could get a string from our object as follows:


```
r1 = Rectangle(10, 20)
r1.to_str()
```




    'Rectangle (width=10, height=20)'



But of course, using the built-in `str` function still does not work:


```
str(r1)
```




    '<__main__.Rectangle object at 0x000002375E708DA0>'



Does this mean we are out of luck, and anyone who writes a class in Python will need to provide some method to do this, and probably come up with their own name for the method too, maybe `to_str`, `make_string`, `stringify`, and who knows what else.

Fortunately, this is where these special methods come in. When we call `str(r1)`, Python will first look to see if our class (`Rectangle`) has a special method called `__str__`.

If the `__str__` method is present, then Python will call it and return that value.

There's actually another one called `__repr__` which is related, but we'll just focus on `__str__` for now.


```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)
```


```
r1 = Rectangle(10, 20)
```


```
str(r1)
```




    'Rectangle (width=10, height=20)'



However, in Jupyter (and interactive console if you are using that), look what happens here:


```
r1
```




    <__main__.Rectangle at 0x2375e716ef0>



As you can see we still get that default. That's because here Python is not converting `r1` to a string, but instead looking for a string *representation* of the object. It is looking for the `__repr__` method (which we'll come back to later).


```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
```


```
r1 = Rectangle(10, 20)
```


```
print(r1)  # uses __str__
```

    Rectangle (width=10, height=20)
    


```
r1  # uses __repr__
```




    Rectangle(10, 20)



How about the comparison operators, such as `==` or `<`?


```
r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
```


```
r1 == r2
```




    False



As you can see, Python does not consider `r1` and `r2` as equal (using the `==` operator). Again, how is Python supposed to know that two Rectangle objects with the same height and width should be considered equal?

We just need to tell Python how to do it, using the special method `__eq__`.


```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        print('self={0}, other={1}'.format(self, other))
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False
```


```
r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
```


```
r1 is r2
```




    False




```
r1 == r2
```

    self=Rectangle (width=10, height=20), other=Rectangle (width=10, height=20)
    




    True




```
r3 = Rectangle(2, 3)
```


```
r1 == r3
```

    self=Rectangle (width=10, height=20), other=Rectangle (width=2, height=3)
    




    False



And if we try to compare our Rectangle to a different type:


```
r1 == 100
```

    self=Rectangle (width=10, height=20), other=100
    




    False



Let's remove that print statement - I only put that in so you could see what the arguments were, in practice you should avoid side effects.


```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False
```

What about `<`, `>`, `<=`, etc.?

Again, Python has special methods we can use to provide that functionality.

These are methods such as `__lt__`, `__gt__`, `__le__`, etc.


```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False
    
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented
```


```
r1 = Rectangle(100, 200)
r2 = Rectangle(10, 20)
```


```
r1 < r2
```




    False




```
r2 < r1
```




    True



What about `>`?


```
r1 > r2
```




    True



How did that work? We did not define a `__gt__` method.

Well, Python cleverly decided that since `r1 > r2` was not implemented, it would give 

`r2 < r1` 

a try. And since, `__lt__` **is** defined, it worked!

Of course, `<=` is not going to magically work!


```
r1 <= r2
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-53-beabec6419b6> in <module>()
    ----> 1 r1 <= r2
    

    TypeError: '<=' not supported between instances of 'Rectangle' and 'Rectangle'


If you come from a Java background, you are probably thinking that using "bare" properties (direct access), such as `height` and `width` is a terrible design idea.

It is for Java, but not for Python.

Although you can use bare properties in Java, if you ever need to intercept the getting or setting of a property, you will need to write a method (such as `getWidth` and `setWidth`. The problem is that if you used a bare `width` property for example, a lot of your code might be using `obj.width` (as we have been doing here). The instant you make the `width` private and instead implement getters and setters, you break your code.
Hence one of the reasons why in Java we just write getters and setters for properties from the beginning.

With Python this is not the case - we can change any bare property into getters and setters without breaking the code that uses that bare property.

I'll show you a quick example here, but we'll come back to this topic in much more detail later.

Let's take our Rectangle class once again. I'll use a simplified version to keep the code short.


```
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
```


```
r1 = Rectangle(10, 20)
```


```
r1.width
```




    10




```
r1.width = 100
```


```
r1
```




    Rectangle(100, 20)



As you saw we can *get* and *set* the `width` property directly.

But let's say after this code has been released for a while and users of our class have been using it (and specifically setting and getting the `width` and `height` attribute a lot), but now we want to make sure users cannot set a non-positive value (i.e. <= 0) for width (or height, but we'll focus on width as an example).

In a language like Java, we would implement `getWidth` and `setWidth` and make `width` private - which would break any code directly accessing the `width` property.

In Python we can use some special **decorators** (more on those later) to encapsulate our property getters and setters:


```
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height
```


```
r1 = Rectangle(10, 20)
```


```
r1.width
```




    10




```
r1.width = 100
```


```
r1
```




    Rectangle(100, 20)




```
r1.width = -10
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-64-5813452c3f38> in <module>()
    ----> 1 r1.width = -10
    

    <ipython-input-59-f23b29795658> in width(self, width)
         14     def width(self, width):
         15         if width <= 0:
    ---> 16             raise ValueError('Width must be positive.')
         17         self._width = width
         18 
    

    ValueError: Width must be positive.


There are more things we should do to properly implement all this, in particular we should also be checking the positive and negative values during the `__init__` phase. We do so by using the accessor methods for height and width:


```
class Rectangle:
    def __init__(self, width, height):
        self._width = None
        self._height = None
        # now we call our accessor methods to set the width and height
        self.width = width
        self.height = height
    
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height
```


```
r1 = Rectangle(0, 10)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-66-b60d030826a5> in <module>()
    ----> 1 r1 = Rectangle(0, 10)
    

    <ipython-input-65-4c1b43452381> in __init__(self, width, height)
          4         self._height = None
          5         # now we call our accessor methods to set the width and height
    ----> 6         self.width = width
          7         self.height = height
          8 
    

    <ipython-input-65-4c1b43452381> in width(self, width)
         17     def width(self, width):
         18         if width <= 0:
    ---> 19             raise ValueError('Width must be positive.')
         20         self._width = width
         21 
    

    ValueError: Width must be positive.


There more we should be doing, like checking that the width and height being passed in are numeric types, and so on. Especially during the `__init__` phase - we would rather raise an exception when the object is being created rather than delay things and raise an exception when the user calls some method like `area` - that way the exception will be on the line that creates the object - makes debugging much easier!

There are many more of these special methods, and we'll look in detail at them later in this course.

# Section 03 - Variables and Memory

##  Variables are Memory References

We can find the memory address that a variable *references*, by using the `id()` function.

The `id()` function returns the memory address of its argument as a base-10 integer.

We can use the function `hex()` to convert the base-10 number to base-16.


```
my_var = 10
print('my_var = {0}'.format(my_var))
print('memory address of my_var (decimal): {0}'.format(id(my_var)))
print('memory address of my_var (hex): {0}'.format(hex(id(my_var))))
```

    my_var = 10
    memory address of my_var (decimal): 1968827120
    memory address of my_var (hex): 0x7559eaf0
    


```
greeting = 'Hello'
print('greeting = {0}'.format(greeting))
print('memory address of my_var (decimal): {0}'.format(id(greeting)))
print('memory address of my_var (hex): {0}'.format(hex(id(greeting))))
```

    greeting = Hello
    memory address of my_var (decimal): 1688681719264
    memory address of my_var (hex): 0x1892d4625e0
    

Note how the memory address of `my_var` is **different** from that of `greeting`.

Strictly speaking, `my_var` is not "equal" to 10. 

Instead `my_var` is a **reference** to an (*integer*) object (*containing the value 10*) located at the memory address `id(my_var)`

Similarly for the variable `greeting`.

##  Reference Counting

Method that returns the reference count for a given variable's memory address:


```
import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value
```

Let's make a variable, and check it's reference count:


```
my_var = [1, 2, 3, 4]
ref_count(id(my_var))
```




    1



There is another built-in function we can use to obtain the reference count:


```
import sys
sys.getrefcount(my_var)
```




    2



But why is this returning 2, instead of the expected 1 we obtained with the previous function?

Answer: The *sys.getrefcount()* function takes **my_var** as an argument, this means it receives (and stores) a reference to **my_var**'s memory address **also** - hence the count is off by 1. So we will use *from_address()* instead.

We make another reference to the **same** reference as `my_var`:


```
other_var = my_var
```

Let's look at the memory address of those two variables and the reference counts:


```
print(hex(id(my_var)), hex(id(other_var)))
print(ref_count(id(my_var)))
```

    0x1e43f368388 0x1e43f368388
    2
    

Force one reference to go away:


```
other_var = None
```

And we look at the reference count again:


```
print(ref_count(id(my_var)))
```

    1
    

We see that the reference count has gone back to 1.

You'll probably never need to do anything like this in Python. Memory management is completely transparent - this is just to illustrate some of what is going behind the scenes as it helps to understand upcoming concepts.

##  Garbage Collection


```
import ctypes
import gc
```

We use the same function that we used in the lesson on reference counting to calculate the number of references to a specified object (using its memory address to avoid creating an extra reference)


```
def ref_count(address):
    return ctypes.c_long.from_address(address).value
```

We create a function that will search the objects in the GC for a specified id and tell us if the object was found or not:


```
def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not found"
```

Next we define two classes that we will use to create a circular reference

Class A's constructor will create an instance of class B and pass itself to class B's constructor that will then store that reference in some instance variable.


```
class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b:{1}'.format(hex(id(self)), hex(id(self.b))))
```


```
class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))
```

We turn off the GC so we can see how reference counts are affected when the GC does not run and when it does (by running it manually).


```
gc.disable()
```

Now we create an instance of A, which will, in turn, create an instance of B which will store a reference to the calling A instance.


```
my_var = A()
```

    B: self: 0x1fc1eae44e0, a: 0x1fc1eae4908
    A: self: 0x1fc1eae4908, b:0x1fc1eae44e0
    

As we can see A and B's constructors ran, and we also see from the memory addresses that we have a circular reference.

In fact `my_var` is also a reference to the same A instance:


```
print(hex(id(my_var)))
```

    0x1fc1eae4908
    

Another way to see this:


```
print('a: \t{0}'.format(hex(id(my_var))))
print('a.b: \t{0}'.format(hex(id(my_var.b))))
print('b.a: \t{0}'.format(hex(id(my_var.b.a))))
```

    a: 	0x1fc1eae4908
    a.b: 	0x1fc1eae44e0
    b.a: 	0x1fc1eae4908
    


```
a_id = id(my_var)
b_id = id(my_var.b)
```

We can see how many references we have for `a` and `b`:


```
print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))
```

    refcount(a) = 2
    refcount(b) = 1
    a: Object exists
    b: Object exists
    

As we can see the A instance has two references (one from `my_var`, the other from the instance variable `b` in the B instance)

The B instance has one reference (from the A instance variable `a`)

Now, let's remove the reference to the A instance that is being held by `my_var`:


```
my_var= None
```


```
print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))
```

    refcount(a) = 1
    refcount(b) = 1
    a: Object exists
    b: Object exists
    

As we can see, the reference counts are now both equal to 1 (a pure circular reference), and reference counting alone did not destroy the A and B instances - they're still around. If no garbage collection is performed this would result in a memory leak.

Let's run the GC manually and re-check whether the objects still exist:


```
gc.collect()
print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))
print('a: {0}'.format(object_by_id(a_id)))
print('b: {0}'.format(object_by_id(b_id)))
```

    refcount(a) = 0
    refcount(b) = 0
    a: Not found
    b: Not found
    

##  Dynamic Typing

Python is dynamically typed.

This means that the type of a variable is simply the type of the object the variable name points to (references). The variable itself has no associated type.


```
a = "hello"
```


```
type(a)
```




    str




```
a = 10
```


```
type(a)
```




    int




```
a = lambda x: x**2
```


```
a(2)
```




    4




```
type(a)
```




    function



As you can see from the above examples, the type of the variable ``a`` changed over time - in fact it was simply the type of the object ``a`` was referencing at that time. No type was ever attached to the variable name itself.

##  Variable Re-Assignment

Notice how the memory address of **a** is different every time.


```
a = 10
hex(id(a))
```




    '0x7559eaf0'




```
a = 15
hex(id(a))
```




    '0x7559eb90'




```
a = 5
hex(id(a))
```




    '0x7559ea50'




```
a = a + 1
hex(id(a))
```




    '0x7559ea70'



However, look at this:


```
a = 10
b = 10
print(hex(id(a)))
print(hex(id(b)))
```

    0x7559eaf0
    0x7559eaf0
    

The memory addresses of both **a** and **b** are the same!! 

We'll revisit this in a bit to explain what is going on.

##  Object Mutability

Certain Python built-in object types (aka data types) are **mutable**.

That is, the internal contents (state) of the object in memory can be modified.


```
my_list = [1, 2, 3]
print(my_list)
print(hex(id(my_list)))
```

    [1, 2, 3]
    0x1cf6ab5b208
    


```
my_list.append(4)
print(my_list)
print(hex(id(my_list)))
```

    [1, 2, 3, 4]
    0x1cf6ab5b208
    

As you can see, the memory address of *my_list* has **not** changed.

But, the **contents** of *my_list* has changed from *[1, 2, 3]* to *[1, 2, 3, 4]*.

On the other hand, consider this:


```
my_list_1 = [1, 2, 3]
print(my_list_1)
print(hex(id(my_list_1)))
```

    [1, 2, 3]
    0x1cf6abd55c8
    


```
my_list_1 = my_list_1 + [4]
print(my_list_1)
print(hex(id(my_list_1)))
```

    [1, 2, 3, 4]
    0x1cf6ab56888
    

Notice here that the memory address of *my_list_1* **did** change.

This is because concatenating two lists objects *my_list_1* and *[4]* did not modify the contents of *my_list_1* - instead it created a new list object and re-assigned *my_list_1* to reference this new object.

Similarly with **dictionary** objects that are also **mutable** types.


```
my_dict = dict(key1='value 1')
print(my_dict)
print(hex(id(my_dict)))
```

    {'key1': 'value 1'}
    0x1cf6abdcdc8
    


```
my_dict['key1'] = 'modified value 1'
print(my_dict)
print(hex(id(my_dict)))
```

    {'key1': 'modified value 1'}
    0x1cf6abdcdc8
    


```
my_dict['key2'] = 'value 2'
print(my_dict)
print(hex(id(my_dict)))
```

    {'key1': 'modified value 1', 'key2': 'value 2'}
    0x1cf6abdcdc8
    

Once again we see that while we are modifying the **contents** of the dictionary, the memory address of *my_dict* has not changed.


Now consider the immutable sequence type: **tuple**

The tuple is immutable, so elements cannot be added, removed or replaced.


```
t = (1, 2, 3)
```

This tuple will **never** change at all. It has three elements, the integers 1, 2, and 3. This will remain the case as long as **t**'s reference is not changed.

But, consider the following tuple:


```
a = [1, 2]
b = [3, 4]
t = (a, b)
```

Now, **t** is still immutable, i.e. it contains a reference to the object **a** and the object **b**. **That** will never change as long as **t**'s reference is not re-assigned.

**However**, the elements **a** and **b** are, themselves, mutable.


```
a.append(3)
b.append(5)
print(t)
```

    ([1, 2, 3], [3, 4, 5])
    

Observe that the contents of **a** and **b** **did** change!

So immutability can be a little more subtle than just thinking something can never change. 

The tuple **t** did **not** change - it contains two elements, that are the references **a** and **b**. And that will not change. But, because the referenced elements are mutable themselves, it appears as though the tuple has changed.

It hasn't though - that distinction is subtle but important to understand!

##  Function Arguments and  Mutability

Consider a function that receives a *string* argument, and changes the argument in some way:


```
def process(s):
    print('initial s # = {0}'.format(hex(id(s))))
    s = s + ' world'
    print('s after change # = {0}'.format(hex(id(s))))
```


```
my_var = 'hello'
print('my_var # = {0}'.format(hex(id(my_var))))
```

    my_var # = 0x1e7e96fc420
    

Note that when *s* is received, it is referencing the same object as *my_var*.

After we "modify" *s*, *s* is pointing to a new memory address:


```
process(my_var)
```

    initial s # = 0x1e7e96fc420
    s after change # = 0x1e7e97153b0
    

And our own variable *my_var* is still pointing to the original memory address:


```
print('my_var # = {0}'.format(hex(id(my_var))))
```

    my_var # = 0x1e7e96fc420
    

Let's see how this works with mutable objects:


```
def modify_list(items):
    print('initial items # = {0}'.format(hex(id(items))))
    if len(items) > 0:
        items[0] = items[0] ** 2
    items.pop()
    items.append(5)
    print('final items # = {0}'.format(hex(id(items))))
```


```
my_list = [2, 3, 4]
print('my_list # = {0}'.format(hex(id(my_list))))
```

    my_list # = 0x1e7e972d308
    


```
modify_list(my_list)
```

    initial items # = 0x1e7e972d308
    final items # = 0x1e7e972d308
    


```
print(my_list)
print('my_list # = {0}'.format(hex(id(my_list))))
```

    [4, 3, 5]
    my_list # = 0x1e7e972d308
    

As you can see, throughout all the code, the memory address referenced by *my_list* and *items* is always the **same** (shared) reference - we are simply modifying the contents (**internal state**) of the object at that memory address.

Now, even with immutable container objects we have to be careful, e.g. a tuple containing a list (the tuple is immutable, but the list element inside the tuple **is** mutable)


```
def modify_tuple(t):
    print('initial t # = {0}'.format(hex(id(t))))
    t[0].append(100)
    print('final t # = {0}'.format(hex(id(t))))
```


```
my_tuple = ([1, 2], 'a')
```


```
hex(id(my_tuple))
```




    '0x1e7e9614288'




```
modify_tuple(my_tuple)
```

    initial t # = 0x1e7e9614288
    final t # = 0x1e7e9614288
    


```
my_tuple
```




    ([1, 2, 100], 'a')



As you can see, the first element of the tuple was mutated.

##  Shared References and Mutability

The following sets up a shared reference between the variables my_var_1 and my_var_2


```
my_var_1 = 'hello'
my_var_2 = my_var_1
print(my_var_1)
print(my_var_2)
```

    hello
    hello
    


```
print(hex(id(my_var_1)))
print(hex(id(my_var_2)))
```

    0x24c9144ca08
    0x24c9144ca08
    


```
my_var_2 = my_var_2 + ' world!'
```


```
print(hex(id(my_var_1)))
print(hex(id(my_var_2)))
```

    0x24c9144ca08
    0x24c9144fab0
    

Be careful if the variable type is mutable!

Here we create a list (*my_list_1*) and create a variable (*my_list_2*) referencing the same list object:


```
my_list_1 = [1, 2, 3]
my_list_2 = my_list_1
print(my_list_1)
print(my_list_2)
```

    [1, 2, 3]
    [1, 2, 3]
    

As we can see they have the same memory address (shared reference):


```
print(hex(id(my_list_1)))
print(hex(id(my_list_2)))
```

    0x24c9144fc48
    0x24c9144fc48
    

Now we modify the list referenced by *my_list_2*:


```
my_list_2.append(4)
```

*my_list_2* has been modified:


```
print(my_list_2)
```

    [1, 2, 3, 4]
    

And since my_list_1 references the same list object, it has also changed:


```
print(my_list_1)
```

    [1, 2, 3, 4]
    

As you can see, both variables still share the same reference:


```
print(hex(id(my_list_1)))
print(hex(id(my_list_2)))
```

    0x24c9144fc48
    0x24c9144fc48
    

### Behind the scenes with Python's memory manager
----

Recall from a few lectures back:


```
a = 10
b = 10
```


```
print(hex(id(a)))
print(hex(id(b)))
```

    0x7559eaf0
    0x7559eaf0
    

Same memory address!!

This is safe for Python to do because integer objects are **immutable**. 

So, even though *a* and *b* initially shared the same memory address, we can never modify *a*'s value by "modifying" *b*'s value. 

The only way to change *b*'s value is to change it's reference, which will never affect *a*.


```
b = 15
```


```
print(hex(id(a)))
print(hex(id(b)))
```

    0x7559eaf0
    0x7559eb90
    

However, for mutable objects, Python's memory manager does not do this, since that would **not** be safe.


```
my_list_1 = [1, 2, 3]
my_list_2 = [1, 2 , 3]
```

As you can see, although the two variables were assigned identical "contents", the memory addresses are not the same:


```
print(hex(id(my_list_1)))
print(hex(id(my_list_2)))
```

    0x24c9146c5c8
    0x24c913c6848
    

##  Variable Equality

From the previous lecture we know that **a** and **b** will have a **shared** reference:


```
a = 10
b = 10

print(hex(id(a)))
print(hex(id(b)))
```

    0x7559eaf0
    0x7559eaf0
    

When we use the **is** operator, we are comparing the memory address **references**:


```
print("a is b: ", a is b)
```

    a is b:  True
    

But if we use the **==** operator, we are comparing the **contents**:


```
print("a == b:", a == b)
```

    a == b: True
    

The following however, do not have a shared reference:


```
a = [1, 2, 3]
b = [1, 2, 3]

print(hex(id(a)))
print(hex(id(b)))
```

    0x27006f17288
    0x27006e968c8
    

Although they are not the same objects, they do contain the same "values":


```
print("a is b: ", a is b)
print("a == b", a == b)
```

    a is b:  False
    a == b True
    

Python will attempt to compare values as best as possible, for example:


```
a = 10
b = 10.0
```

These are **not** the same reference, since one object is an **int** and the other is a **float**


```
print(type(a))
print(type(b))
```

    <class 'int'>
    <class 'float'>
    


```
print(hex(id(a)))
print(hex(id(b)))
```

    0x7559eaf0
    0x270064b1870
    


```
print('a is b:', a is b)
print('a == b:', a == b)
```

    a is b: False
    a == b: True
    

So, even though *a* is an integer 10, and *b* is a float 10.0, the values will still compare as equal.

In fact, this will also have the same behavior:


```
c = 10 + 0j
print(type(c))
```

    <class 'complex'>
    


```
print('a is c:', a is c)
print('a == c:', a == c)
```

    a is c: False
    a == c: True
    

### The None Object
----

**None** is a built-in "variable" of type *NoneType*.

Basically the keyword **None** is a reference to an object instance of *NoneType*.

NoneType objects are immutable! Python's memory manager will therefore use shared references to the None object.


```
print(None)
```

    None
    


```
hex(id(None))
```




    '0x75576bc0'




```
type(None)
```




    NoneType




```
a = None
print(type(a))
print(hex(id(a)))
```

    <class 'NoneType'>
    0x75576bc0
    


```
a is None
```




    True




```
a == None
```




    True




```
b = None
hex(id(b))
```




    '0x75576bc0'




```
a is b
```




    True




```
a == b
```




    True




```
l = []
```


```
type(l)
```




    list




```
l is None
```




    False




```
l == None
```




    False



##  Everything is an Object


```
a = 10
```

**a** is an object of type **int**, i.e. **a** is an instance of the **int** class.


```
print(type(a))
```

    <class 'int'>
    

If **int** is a class, we should be able to declare it using standard class instatiation:


```
b = int(10)
```


```
print(b)
print(type(b))
```

    10
    <class 'int'>
    

We can even request the class documentation:


```
help(int)
```

    Help on class int in module builtins:
    
    class int(object)
     |  int(x=0) -> integer
     |  int(x, base=10) -> integer
     |  
     |  Convert a number or string to an integer, or return 0 if no arguments
     |  are given.  If x is a number, return x.__int__().  For floating point
     |  numbers, this truncates towards zero.
     |  
     |  If x is not a number or if base is given, then x must be a string,
     |  bytes, or bytearray instance representing an integer literal in the
     |  given base.  The literal can be preceded by '+' or '-' and be surrounded
     |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
     |  Base 0 means to interpret the base from the string as an integer literal.
     |  >>> int('0b100', base=0)
     |  4
     |  
     |  Methods defined here:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __and__(self, value, /)
     |      Return self&value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __ceil__(...)
     |      Ceiling of an Integral returns itself.
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __float__(self, /)
     |      float(self)
     |  
     |  __floor__(...)
     |      Flooring an Integral returns itself.
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __format__(...)
     |      default object formatter
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __index__(self, /)
     |      Return self converted to an integer, if self is suitable for use as an index into a list.
     |  
     |  __int__(self, /)
     |      int(self)
     |  
     |  __invert__(self, /)
     |      ~self
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lshift__(self, value, /)
     |      Return self<<value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __or__(self, value, /)
     |      Return self|value.
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rand__(self, value, /)
     |      Return value&self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rlshift__(self, value, /)
     |      Return value<<self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __ror__(self, value, /)
     |      Return value|self.
     |  
     |  __round__(...)
     |      Rounding an Integral returns itself.
     |      Rounding with an ndigits argument also returns an integer.
     |  
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |  
     |  __rrshift__(self, value, /)
     |      Return value>>self.
     |  
     |  __rshift__(self, value, /)
     |      Return self>>value.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __rxor__(self, value, /)
     |      Return value^self.
     |  
     |  __sizeof__(...)
     |      Returns size in memory, in bytes
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  __trunc__(...)
     |      Truncating an Integral returns itself.
     |  
     |  __xor__(self, value, /)
     |      Return self^value.
     |  
     |  bit_length(...)
     |      int.bit_length() -> int
     |      
     |      Number of bits necessary to represent self in binary.
     |      >>> bin(37)
     |      '0b100101'
     |      >>> (37).bit_length()
     |      6
     |  
     |  conjugate(...)
     |      Returns self, the complex conjugate of any int.
     |  
     |  from_bytes(...) from builtins.type
     |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
     |      
     |      Return the integer represented by the given array of bytes.
     |      
     |      The bytes argument must be a bytes-like object (e.g. bytes or bytearray).
     |      
     |      The byteorder argument determines the byte order used to represent the
     |      integer.  If byteorder is 'big', the most significant byte is at the
     |      beginning of the byte array.  If byteorder is 'little', the most
     |      significant byte is at the end of the byte array.  To request the native
     |      byte order of the host system, use `sys.byteorder' as the byte order value.
     |      
     |      The signed keyword-only argument indicates whether two's complement is
     |      used to represent the integer.
     |  
     |  to_bytes(...)
     |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
     |      
     |      Return an array of bytes representing an integer.
     |      
     |      The integer is represented using length bytes.  An OverflowError is
     |      raised if the integer is not representable with the given number of
     |      bytes.
     |      
     |      The byteorder argument determines the byte order used to represent the
     |      integer.  If byteorder is 'big', the most significant byte is at the
     |      beginning of the byte array.  If byteorder is 'little', the most
     |      significant byte is at the end of the byte array.  To request the native
     |      byte order of the host system, use `sys.byteorder' as the byte order value.
     |      
     |      The signed keyword-only argument determines whether two's complement is
     |      used to represent the integer.  If signed is False and a negative integer
     |      is given, an OverflowError is raised.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  denominator
     |      the denominator of a rational number in lowest terms
     |  
     |  imag
     |      the imaginary part of a complex number
     |  
     |  numerator
     |      the numerator of a rational number in lowest terms
     |  
     |  real
     |      the real part of a complex number
    
    

As we see from the docs, we can even create an **int** using an overloaded constructor:


```
b = int('10', base=2)
```


```
print(b)
print(type(b))
```

    2
    <class 'int'>
    

### Functions are Objects too
---


```
def square(a):
    return a ** 2
```


```
type(square)
```




    function



In fact, we can even assign them to a variable:


```
f = square
```


```
type(f)
```




    function




```
f is square
```




    True




```
f(2)
```




    4




```
type(f(2))
```




    int



A function can return a function


```
def cube(a):
    return a ** 3
```


```
def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube
```


```
f = select_function(1)
print(hex(id(f)))
print(hex(id(square)))
print(hex(id(cube)))
print(type(f))
print('f is square: ', f is square)
print('f is cube: ', f is cube)
print(f)
print(f(2))
```

    0x21257457b70
    0x21257457b70
    0x21255fab8c8
    <class 'function'>
    f is square:  True
    f is cube:  False
    <function square at 0x0000021257457B70>
    4
    


```
f = select_function(2)
print(hex(id(f)))
print(hex(id(square)))
print(hex(id(cube)))
print(type(f))
print('f is square: ', f is square)
print('f is cube: ', f is cube)
print(f)
print(f(2))
```

    0x21255fab8c8
    0x21257457b70
    0x21255fab8c8
    <class 'function'>
    f is square:  False
    f is cube:  True
    <function cube at 0x0000021255FAB8C8>
    8
    

We could even call it this way:


```
select_function(1)(5)
```




    25



A Function can be passed as an argument to another function

(This example is pretty useless, but it illustrates the point effectively)


```
def exec_function(fn, n):
    return fn(n)
```


```
result = exec_function(cube, 2)
print(result)
```

    8
    

We will come back to functions as arguments **many** more times throughout this course!

##  Python Optimizations: Interning

Earlier, we saw shared references being created automatically by Python:


```
a = 10
b = 10
print(id(a))
print(id(b))
```

    1968827120
    1968827120
    

Note how `a` and `b` reference the same object.

But consider the following example:


```
a = 500
b = 500
print(id(a))
print(id(b))
```

    1935322088624
    1935322089008
    

As you can see, the variables `a` and `b` do **not** point to the same object!

This is because Python pre-caches integer objects in the range [-5, 256]

So for example:


```
a = 256
b = 256
print(id(a))
print(id(b))
```

    1968834992
    1968834992
    

and


```
a = -5
b = -5
print(id(a))
print(id(b))
```

    1968826640
    1968826640
    

do have the same reference.

This is called **interning**: Python **interns** the integers in the range [-5, 256].

The integers in the range [-5, 256] are essentially **singleton** objects.


```
a = 10
b = int(10)
c = int('10')
d = int('1010', 2)
```


```
print(a, b, c, d)
```

    10 10 10 10
    


```
a is b
```




    True




```
a is c
```




    True




```
a is d
```




    True



As you can see, all these variables were created in different ways, but since the integer object with value 10 behaves like a singleton, they all ended up pointing to the **same** object in memory.

##  Python Optimizations: String Interning

Python will automatically intern *certain* strings.

In particular all the identifiers (variable names, function names, class names, etc) are interned (singleton objects created).

Python will also intern string literals that look like identifiers.

For example:


```
a = 'hello'
b = 'hello'
print(id(a))
print(id(b))
```

    1342722069536
    1342722069536
    

But not the following:


```
a = 'hello, world!'
b = 'hello, world!'
print(id(a))
print(id(b))
```

    1342722047024
    1342722170928
    

However, because the following literals resemble identifiers, even though they are quite long, Python will still automatically intern them:


```
a = 'hello_world'
b = 'hello_world'
print(id(a))
print(id(b))
```

    1342722047856
    1342722047856
    

And even longer:


```
a = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
b = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
print(id(a))
print(id(b))
```

    1342721886784
    1342721886784
    

Even if the string starts with a digit:


```
a = '1_hello_world'
b = '1_hello_world'
print(id(a))
print(id(b))
```

    1342722046256
    1342722046256
    

That was interned (pointer is the same), but look at this one:


```
a = '1 hello world'
b = '1 hello world'
print(id(a))
print(id(b))
```

    1342722046832
    1342722172592
    

Interning strings (making them singleton objects) means that testing for string equality can be done faster by comparing the memory address:


```
a = 'this_is_a_long_string'
b = 'this_is_a_long_string'
print('a==b:', a == b)
print('a is b:', a is b)
```

    a==b: True
    a is b: True
    

#### <font color="orange">Note: Remember, using `is` ONLY works if the strings were interned!</font>

Here's where this technique fails:


```
a = 'hello world'
b = 'hello world'
print('a==b:', a==b)
print('a is b:', a is b)
```

    a==b: True
    a is b: False
    

You *can* force strings to be interned (but only use it if you have a valid performance optimization need):


```
import sys
```


```
a = sys.intern('hello world')
b = sys.intern('hello world')
c = 'hello world'
print(id(a))
print(id(b))
print(id(c))
```

    1342722172080
    1342722172080
    1342722174896
    

Notice how `a` and `b` are pointing to the same object, but `c` is **NOT**.

So, since both `a` and `b` were interned we can use `is` to test for equality of the two strings:


```
print('a==b:', a==b)
print('a is b:', a is b)
```

    a==b: True
    a is b: True
    

So, does interning really make a big speed difference?

Yes, but only if you are performing a *lot* of comparisons.

Let's run some quick and dirty benchmarks:


```
def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
        if a == b:
            pass
```


```
def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    for i in range(n):
        if a is b:
            pass
```


```
import time

start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()

print('equality: ', end-start)

```

    equality:  2.965451618090112
    


```
start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()

print('identity: ', end-start)
```

    identity:  0.28690104431129626
    

As you can see, the performance difference, especially for long strings, and for many comparisons, can be quite radical!

##  Python Peephole Optimizations

Peephole optimizations refer to a certain class of optimization strategies Python employs during any compilation phases.

#### Constant Expressions

Let's see how Python reduces constant expressions for optimization purposes:


```
def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 10
    f = [1, 2] * 5

```


```
my_func.__code__.co_consts
```




    (None,
     24,
     60,
     1,
     2,
     5,
     'abc',
     3,
     'ab',
     11,
     'the quick brown fox',
     10,
     1440,
     (1, 2),
     (1, 2, 1, 2, 1, 2, 1, 2, 1, 2),
     'abcabcabc')



As you can see in the example above, `24 * 60` was pre-calculated and cached as a constant (`1440`).

Similarly, `(1, 2) * 5` was cached as `(1, 2, 1, 2, 1, 2, 1, 2, 1, 2)` and `'abc' * 3` was cached as `abcabcabc`.

On the other hand, note how `'the quick brown fox' * 10` was **not** pre-calculated (too long).

Similarly `[1, 2] * 5` was not pre-calculated either since a list is *mutable*, and hence not a *constant*.

#### Membership Tests

In membership testing, optimizations are applied as can be seen below:


```
def my_func():
    if e in [1, 2, 3]:
        pass
```


```
my_func.__code__.co_consts
```




    (None, 1, 2, 3, (1, 2, 3))



As you can see, the mutable list `[1, 2, 3]` was converted to an immutable tuple. 

It is OK to do this here, since we are testing membership of the list **at that point in time**, hence it is safe to convert it to a tuple, which is more efficient than testing membership of a list.

In the same way, set membership will be converted to frozen set membership:


```
def my_func():
    if e in {1, 2, 3}:
        pass
```


```
my_func.__code__.co_consts
```




    (None, 1, 2, 3, frozenset({1, 2, 3}))



In general, when you are writing your code, if you can use **set** membership testing, prefer that over a list or tuple - it is quite a bit more efficient.

Let's do a small quick (and dirty) benchmark of this:


```
import string
import time 

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

print(char_list)
print()
print(char_tuple)
print()
print(char_set)
```

    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    
    {'l', 'p', 'x', 'R', 'j', 'S', 's', 'T', 'W', 'Y', 'Z', 'P', 'g', 'O', 'b', 'u', 'H', 'G', 'v', 'e', 'M', 'n', 'w', 't', 'Q', 'E', 'N', 'X', 'C', 'i', 'A', 'B', 'F', 'V', 'a', 'm', 'r', 'f', 'h', 'U', 'D', 'c', 'y', 'z', 'J', 'd', 'o', 'I', 'L', 'K', 'k', 'q'}
    


```
def membership_test(n, container):
    for i in range(n):
        if 'p' in container:
            pass
```


```
start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print('list membership: ', end-start)
```

    list membership:  2.6035404184015434
    


```
start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print('tuple membership: ', end-start)
```

    tuple membership:  2.602491734651276
    


```
start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print('set membership: ', end-start)
```

    set membership:  0.3743007599607324
    

As you can see, set membership tests run quite a bit faster - which is not surprising since they are basically dictionary-like objects, so hash maps are used for looking up an item to determine membership.

# Section 04 - Numeric Types

##  Integers

Integers are objects - instances of the ``int`` class.


```
print(type(100))
```

    <class 'int'>
    

They are a variable length data type that can theoretically handle any integer magnitude. This will take up a variable amount of memory that depends on the particular size of the integer.


```
import sys
```

Creating an integer object requires an overhead of 24 bytes:


```
sys.getsizeof(0)
```




    24



Here we see that to store the number 1 required 4 bytes (32 bits) on top of the 24 byte overhead:


```
sys.getsizeof(1)
```




    28



Larger numbers will require more storage space:


```
sys.getsizeof(2**1000)
```




    160



Larger integers will also slow down calculations.


```
import time
```


```
def calc(a):
    for i in range(10000000):
        a * 2
```

We start with a small integer value for a (10):


```
start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)
```

    0.3565246949777869
    

Now we set a to something larger (2<sup>100</sup>):


```
start = time.perf_counter()
calc(2**100)
end = time.perf_counter()
print(end - start)
```

    0.6125349575326144
    

Finally we set a to some really large value (2<sup>10,000</sup>):


```
start = time.perf_counter()
calc(2**10000)
end = time.perf_counter()
print(end - start)
```

    5.023413039975091
    

##  Integers - Operations

Addition, subtraction, multiplication and exponentiation of integers always result in an integer. (In the case of exponentiation this holds only for positive integer exponents.)


```
type(2 + 3)
```




    int




```
type(3 - 10)
```




    int




```
type(3 * 5)
```




    int




```
type(3 ** 4)
```




    int



But the standard division operator `/` **always** results in a float value.


```
type(2 / 3)
```




    float




```
type(10 / 2)
```




    float



The `math.floor()` method will return the floor of any number.


```
import math
```

For non-negative values (>= 0), the floor of the value is the same as the integer portion of the value (truncation)


```
math.floor(3.15)
```




    3




```
math.floor(3.9999999)
```




    3



However, this is not the case for negative values:


```
math.floor(-3.15)
```




    -4




```
math.floor(-3.0000001)
```




    -4



#### The Floor Division Operator

The floor division operator `a//b` is the floor of `a / b`

i.e. `a // b = math.floor(a / b)`

This is true whether `a` and `b` are positive or negative.


```
a = 33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))
```

    2.0625
    2
    2
    

For positive numbers, `a//b` is basically the same as truncating (taking the integer portion) of `a / b`.

But this is **not** the case for negative numbers.


```
a = -33
b = 16
print('{0}/{1} = {2}'.format(a, b, a/b))
print('trunc({0}/{1}) = {2}'.format(a, b, math.trunc(a/b)))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('floor({0}//{1}) = {2}'.format(a, b, math.floor(a/b)))
```

    -33/16 = -2.0625
    trunc(-33/16) = -2
    -33//16 = -3
    floor(-33//16) = -3
    


```
a = 33
b = -16
print('{0}/{1} = {2}'.format(a, b, a/b))
print('trunc({0}/{1}) = {2}'.format(a, b, math.trunc(a/b)))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('floor({0}//{1}) = {2}'.format(a, b, math.floor(a/b)))
```

    33/-16 = -2.0625
    trunc(33/-16) = -2
    33//-16 = -3
    floor(33//-16) = -3
    

#### The Modulo Operator

The modulo operator and the floor division operator will always satisfy the following equation:

``a = b * (a // b) + a % b``


```
a = 13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)
```

    13/4 = 3.25
    13//4 = 3
    13%4 = 1
    True
    


```
a = -13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)
```

    -13/4 = -3.25
    -13//4 = -4
    -13%4 = 3
    True
    


```
a = 13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)
```

    13/-4 = -3.25
    13//-4 = -4
    13%-4 = -3
    True
    


```
a = -13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)
```

    -13/-4 = 3.25
    -13//-4 = 3
    -13%-4 = -1
    True
    

##  Integers - Constructors and Bases

#### Constructors

The ``int`` class has two constructors


```
help(int)
```

    Help on class int in module builtins:
    
    class int(object)
     |  int(x=0) -> integer
     |  int(x, base=10) -> integer
     |  
     |  Convert a number or string to an integer, or return 0 if no arguments
     |  are given.  If x is a number, return x.__int__().  For floating point
     |  numbers, this truncates towards zero.
     |  
     |  If x is not a number or if base is given, then x must be a string,
     |  bytes, or bytearray instance representing an integer literal in the
     |  given base.  The literal can be preceded by '+' or '-' and be surrounded
     |  by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
     |  Base 0 means to interpret the base from the string as an integer literal.
     |  >>> int('0b100', base=0)
     |  4
     |  
     |  Methods defined here:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __and__(self, value, /)
     |      Return self&value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __ceil__(...)
     |      Ceiling of an Integral returns itself.
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __float__(self, /)
     |      float(self)
     |  
     |  __floor__(...)
     |      Flooring an Integral returns itself.
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __format__(...)
     |      default object formatter
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __index__(self, /)
     |      Return self converted to an integer, if self is suitable for use as an index into a list.
     |  
     |  __int__(self, /)
     |      int(self)
     |  
     |  __invert__(self, /)
     |      ~self
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lshift__(self, value, /)
     |      Return self<<value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __or__(self, value, /)
     |      Return self|value.
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rand__(self, value, /)
     |      Return value&self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rlshift__(self, value, /)
     |      Return value<<self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __ror__(self, value, /)
     |      Return value|self.
     |  
     |  __round__(...)
     |      Rounding an Integral returns itself.
     |      Rounding with an ndigits argument also returns an integer.
     |  
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |  
     |  __rrshift__(self, value, /)
     |      Return value>>self.
     |  
     |  __rshift__(self, value, /)
     |      Return self>>value.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __rxor__(self, value, /)
     |      Return value^self.
     |  
     |  __sizeof__(...)
     |      Returns size in memory, in bytes
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  __trunc__(...)
     |      Truncating an Integral returns itself.
     |  
     |  __xor__(self, value, /)
     |      Return self^value.
     |  
     |  bit_length(...)
     |      int.bit_length() -> int
     |      
     |      Number of bits necessary to represent self in binary.
     |      >>> bin(37)
     |      '0b100101'
     |      >>> (37).bit_length()
     |      6
     |  
     |  conjugate(...)
     |      Returns self, the complex conjugate of any int.
     |  
     |  from_bytes(...) from builtins.type
     |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
     |      
     |      Return the integer represented by the given array of bytes.
     |      
     |      The bytes argument must be a bytes-like object (e.g. bytes or bytearray).
     |      
     |      The byteorder argument determines the byte order used to represent the
     |      integer.  If byteorder is 'big', the most significant byte is at the
     |      beginning of the byte array.  If byteorder is 'little', the most
     |      significant byte is at the end of the byte array.  To request the native
     |      byte order of the host system, use `sys.byteorder' as the byte order value.
     |      
     |      The signed keyword-only argument indicates whether two's complement is
     |      used to represent the integer.
     |  
     |  to_bytes(...)
     |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
     |      
     |      Return an array of bytes representing an integer.
     |      
     |      The integer is represented using length bytes.  An OverflowError is
     |      raised if the integer is not representable with the given number of
     |      bytes.
     |      
     |      The byteorder argument determines the byte order used to represent the
     |      integer.  If byteorder is 'big', the most significant byte is at the
     |      beginning of the byte array.  If byteorder is 'little', the most
     |      significant byte is at the end of the byte array.  To request the native
     |      byte order of the host system, use `sys.byteorder' as the byte order value.
     |      
     |      The signed keyword-only argument determines whether two's complement is
     |      used to represent the integer.  If signed is False and a negative integer
     |      is given, an OverflowError is raised.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  denominator
     |      the denominator of a rational number in lowest terms
     |  
     |  imag
     |      the imaginary part of a complex number
     |  
     |  numerator
     |      the numerator of a rational number in lowest terms
     |  
     |  real
     |      the real part of a complex number
    
    


```
int(10)
```




    10




```
int(10.9)
```




    10




```
int(-10.9)
```




    -10




```
from fractions import Fraction
```


```
a = Fraction(22, 7)
```


```
a
```




    Fraction(22, 7)




```
int(a)
```




    3



We can use the second constructor to generate integers (base 10) from strings in any base.


```
int("10")
```




    10




```
int("101", 2)
```




    5




```
int("101", base=2)
```




    5



Python uses ``a-z`` for bases from 11 to 36.

Note that the letters are not case sensitive.


```
int("F1A", base=16)
```




    3866




```
int("f1a", base=16)
```




    3866



Of course, the string must be a valid number in whatever base you specify.


```
int('B1A', base=11)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-28-d0cf8657e90a> in <module>()
    ----> 1 int('B1A', base=11)
    

    ValueError: invalid literal for int() with base 11: 'B1A'



```
int('B1A', 12)
```

#### Base Representations

##### Built-ins


```
bin(10)
```


```
oct(10)
```


```
hex(10)
```

Note the `0b`, `0o` and `0x` prefixes

You can use these in your own strings as well, and they correspond to prefixes used in integer literals as well.


```
a = int('1010', 2)
b = int('0b1010', 2)
c = 0b1010
```


```
print(a, b, c)
```


```
a = int('f1a', 16)
b = int('0xf1a', 16)
c = 0xf1a
```


```
print(a, b, c)
```

For literals, the ``a-z`` characters are not case-sensitive either


```
a = 0xf1a
b = 0xF1a
c = 0xF1A
```


```
print(a, b, c)
```

#### Custom Rebasing

Python only provides built-in function to rebase to base 2, 8 and 16.

For other bases, you have to provide your own algorithm (or leverage some 3rd party library of your choice)


```
def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        # m = n % b
        # n = n // b
        # which is the same as:
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits
```


```
from_base10(10, 2)
```


```
from_base10(255, 16)
```

Next we may want to encode the digits into strings using different characters for each digit in the base


```
def encode(digits, digit_map):
    # we require that digit_map has at least as many
    # characters as the max number in digits
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode digits")
    
    # we'll see this later, but the following would be better:
    encoding = ''.join([digit_map[d] for d in digits])
    return encoding
    
```

Now we can encode any list of digits:


```
encode([1, 0, 1], "FT")
```


```
encode([1, 10, 11], '0123456789AB')
```

And we can combine both functions into a single one for easier use:


```
def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    # we store the sign of number and make it positive
    # we'll re-insert the sign at the end
    sign = -1 if number < 0 else 1
    number *= sign
    
    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding
```


```
e = rebase_from10(10, 2)
print(e)
print(int(e, 2))
```


```
e = rebase_from10(-10, 2)
print(e)
print(int(e, 2))
```


```
rebase_from10(131, 11)
```


```
rebase_from10(4095, 16)
```


```
rebase_from10(-4095, 16)
```

##  Rational Numbers


```
from fractions import Fraction
```

We can get some info on the Fraction class:


```
help(Fraction)
```

    Help on class Fraction in module fractions:
    
    class Fraction(numbers.Rational)
     |  This class implements rational numbers.
     |  
     |  In the two-argument form of the constructor, Fraction(8, 6) will
     |  produce a rational number equivalent to 4/3. Both arguments must
     |  be Rational. The numerator defaults to 0 and the denominator
     |  defaults to 1 so that Fraction(3) == 3 and Fraction() == 0.
     |  
     |  Fractions can also be constructed from:
     |  
     |    - numeric strings similar to those accepted by the
     |      float constructor (for example, '-2.3' or '1e10')
     |  
     |    - strings of the form '123/456'
     |  
     |    - float and Decimal instances
     |  
     |    - other Rational instances (including integers)
     |  
     |  Method resolution order:
     |      Fraction
     |      numbers.Rational
     |      numbers.Real
     |      numbers.Complex
     |      numbers.Number
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __abs__(a)
     |      abs(a)
     |  
     |  __add__(a, b)
     |      a + b
     |  
     |  __bool__(a)
     |      a != 0
     |  
     |  __ceil__(a)
     |      Will be math.ceil(a) in 3.0.
     |  
     |  __copy__(self)
     |  
     |  __deepcopy__(self, memo)
     |  
     |  __eq__(a, b)
     |      a == b
     |  
     |  __floor__(a)
     |      Will be math.floor(a) in 3.0.
     |  
     |  __floordiv__(a, b)
     |      a // b
     |  
     |  __ge__(a, b)
     |      a >= b
     |  
     |  __gt__(a, b)
     |      a > b
     |  
     |  __hash__(self)
     |      hash(self)
     |  
     |  __le__(a, b)
     |      a <= b
     |  
     |  __lt__(a, b)
     |      a < b
     |  
     |  __mod__(a, b)
     |      a % b
     |  
     |  __mul__(a, b)
     |      a * b
     |  
     |  __neg__(a)
     |      -a
     |  
     |  __pos__(a)
     |      +a: Coerces a subclass instance to Fraction
     |  
     |  __pow__(a, b)
     |      a ** b
     |      
     |      If b is not an integer, the result will be a float or complex
     |      since roots are generally irrational. If b is an integer, the
     |      result will be rational.
     |  
     |  __radd__(b, a)
     |      a + b
     |  
     |  __reduce__(self)
     |      helper for pickle
     |  
     |  __repr__(self)
     |      repr(self)
     |  
     |  __rfloordiv__(b, a)
     |      a // b
     |  
     |  __rmod__(b, a)
     |      a % b
     |  
     |  __rmul__(b, a)
     |      a * b
     |  
     |  __round__(self, ndigits=None)
     |      Will be round(self, ndigits) in 3.0.
     |      
     |      Rounds half toward even.
     |  
     |  __rpow__(b, a)
     |      a ** b
     |  
     |  __rsub__(b, a)
     |      a - b
     |  
     |  __rtruediv__(b, a)
     |      a / b
     |  
     |  __str__(self)
     |      str(self)
     |  
     |  __sub__(a, b)
     |      a - b
     |  
     |  __truediv__(a, b)
     |      a / b
     |  
     |  __trunc__(a)
     |      trunc(a)
     |  
     |  limit_denominator(self, max_denominator=1000000)
     |      Closest Fraction to self with denominator at most max_denominator.
     |      
     |      >>> Fraction('3.141592653589793').limit_denominator(10)
     |      Fraction(22, 7)
     |      >>> Fraction('3.141592653589793').limit_denominator(100)
     |      Fraction(311, 99)
     |      >>> Fraction(4321, 8765).limit_denominator(10000)
     |      Fraction(4321, 8765)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  from_decimal(dec) from abc.ABCMeta
     |      Converts a finite Decimal instance to a rational number, exactly.
     |  
     |  from_float(f) from abc.ABCMeta
     |      Converts a finite float to a rational number, exactly.
     |      
     |      Beware that Fraction.from_float(0.3) != Fraction(3, 10).
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(cls, numerator=0, denominator=None, *, _normalize=True)
     |      Constructs a Rational.
     |      
     |      Takes a string like '3/2' or '1.5', another Rational instance, a
     |      numerator/denominator pair, or a float.
     |      
     |      Examples
     |      --------
     |      
     |      >>> Fraction(10, -8)
     |      Fraction(-5, 4)
     |      >>> Fraction(Fraction(1, 7), 5)
     |      Fraction(1, 35)
     |      >>> Fraction(Fraction(1, 7), Fraction(2, 3))
     |      Fraction(3, 14)
     |      >>> Fraction('314')
     |      Fraction(314, 1)
     |      >>> Fraction('-35/4')
     |      Fraction(-35, 4)
     |      >>> Fraction('3.1415') # conversion from numeric string
     |      Fraction(6283, 2000)
     |      >>> Fraction('-47e-2') # string may include a decimal exponent
     |      Fraction(-47, 100)
     |      >>> Fraction(1.47)  # direct construction from float (exact conversion)
     |      Fraction(6620291452234629, 4503599627370496)
     |      >>> Fraction(2.25)
     |      Fraction(9, 4)
     |      >>> Fraction(Decimal('1.47'))
     |      Fraction(147, 100)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  denominator
     |  
     |  numerator
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __abstractmethods__ = frozenset()
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from numbers.Rational:
     |  
     |  __float__(self)
     |      float(self) = self.numerator / self.denominator
     |      
     |      It's important that this conversion use the integer's "true"
     |      division rather than casting one side to float before dividing
     |      so that ratios of huge integers convert without overflowing.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from numbers.Real:
     |  
     |  __complex__(self)
     |      complex(self) == complex(float(self), 0)
     |  
     |  __divmod__(self, other)
     |      divmod(self, other): The pair (self // other, self % other).
     |      
     |      Sometimes this can be computed faster than the pair of
     |      operations.
     |  
     |  __rdivmod__(self, other)
     |      divmod(other, self): The pair (self // other, self % other).
     |      
     |      Sometimes this can be computed faster than the pair of
     |      operations.
     |  
     |  conjugate(self)
     |      Conjugate is a no-op for Reals.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from numbers.Real:
     |  
     |  imag
     |      Real numbers have no imaginary component.
     |  
     |  real
     |      Real numbers are their real component.
    
    

We can create Fraction objects in a variety of ways:

Using integers:


```
Fraction(1)
```




    Fraction(1, 1)




```
Fraction(1, 3)
```




    Fraction(1, 3)



Using rational numbers:


```
x = Fraction(2, 3)
y = Fraction(3, 4)
# 2/3 / 3/4 --> 2/3 * 4/3 --> 8/9
Fraction(x, y)
```




    Fraction(8, 9)



Using floats:


```
Fraction(0.125)
```




    Fraction(1, 8)




```
Fraction(0.5)
```




    Fraction(1, 2)



Using strings:


```
Fraction('10.5')
```




    Fraction(21, 2)




```
Fraction('22/7')
```




    Fraction(22, 7)



Fractions are automatically reduced:


```
Fraction(8, 16)
```




    Fraction(1, 2)



Negative sign is attached to the numerator:


```
Fraction(1, -4)
```




    Fraction(-1, 4)



Standard arithmetic operators are supported:


```
Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3)
```




    Fraction(1, 1)




```
Fraction(1, 2) * Fraction(1, 4)
```




    Fraction(1, 8)




```
Fraction(1, 2) / Fraction(1, 3)
```




    Fraction(3, 2)



We can recover the numerator and denominator (integers):


```
x = Fraction(22, 7)
print(x.numerator)
print(x.denominator)
```

    22
    7
    

Since floats have **finite** precision, any float can be converted to a rational number:


```
import math
x = Fraction(math.pi)
print(x)
print(float(x))
```

    884279719003555/281474976710656
    3.141592653589793
    


```
x = Fraction(math.sqrt(2))
print(x)
```

    6369051672525773/4503599627370496
    

Note that these rational values are approximations to the irrational numbers $\pi$ and $\sqrt{2}$

**Beware!!**

Float number representations (as we will examine in future lessons) do not always have an exact representation.

The number 0.125 (1/8) **has** an exact representation:


```
Fraction(0.125)
```




    Fraction(1, 8)



and so we see the expected equivalent fraction.

But, 0.3 (3/10) does **not** have an exact representation:


```
Fraction(3, 10)
```




    Fraction(3, 10)



but


```
Fraction(0.3)
```




    Fraction(5404319552844595, 18014398509481984)



We will study this in upcoming lessons.

But for now, let's just see a quick explanation:


```
x = 0.3
```


```
print(x)
```

    0.3
    

Everything looks ok here - why am I saying 0.3 (float) is just an approximation?

Python is trying to format the displayed value for readability - so it rounds the number for a better display format!

We can instead choose to display the value using a certain number of digits:


```
format(x, '.5f')
```




    '0.30000'



At 5 digits after the decimal, we might still think 0.3 is an exact representation.

But let's display a few more digits:


```
format(x, '.15f')
```




    '0.300000000000000'



Hmm... 15 digits and still looking good!

How about 25 digits...


```
format(x, '.25f')
```




    '0.2999999999999999888977698'



Now we see that **x** is not quite 0.3...

In fact, we can quantify the delta this way:


```
delta = Fraction(0.3) - Fraction(3, 10)
```

Theoretically, delta should be 0, but it's not:


```
delta == 0
```




    False




```
delta
```




    Fraction(-1, 90071992547409920)



**delta** is a very small number, the above fraction...

As a float:


```
float(delta)
```




    -1.1102230246251566e-17



#### Constraining the denominator


```
x = Fraction(math.pi)
print(x)
print(format(float(x), '.25f'))
```

    884279719003555/281474976710656
    3.1415926535897931159979635
    


```
y = x.limit_denominator(10)
print(y)
print(format(float(y), '.25f'))
```

    22/7
    3.1428571428571427937015414
    


```
y = x.limit_denominator(100)
print(y)
print(format(float(y), '.25f'))
```

    311/99
    3.1414141414141414365701621
    


```
y = x.limit_denominator(500)
print(y)
print(format(float(y), '.25f'))
```

    355/113
    3.1415929203539825209645642
    

##  Floats - Internal Representation

The ``float`` class can be used to represent real numbers.


```
help(float)
```

    Help on class float in module builtins:
    
    class float(object)
     |  float(x) -> floating point number
     |  
     |  Convert a string or number to a floating point number, if possible.
     |  
     |  Methods defined here:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __float__(self, /)
     |      float(self)
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __format__(...)
     |      float.__format__(format_spec) -> string
     |      
     |      Formats the float according to format_spec.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getformat__(...) from builtins.type
     |      float.__getformat__(typestr) -> string
     |      
     |      You probably don't want to use this function.  It exists mainly to be
     |      used in Python's test suite.
     |      
     |      typestr must be 'double' or 'float'.  This function returns whichever of
     |      'unknown', 'IEEE, big-endian' or 'IEEE, little-endian' best describes the
     |      format of floating point numbers used by the C type named by typestr.
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __int__(self, /)
     |      int(self)
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __round__(...)
     |      Return the Integral closest to x, rounding half toward even.
     |      When an argument is passed, work like built-in round(x, ndigits).
     |  
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __setformat__(...) from builtins.type
     |      float.__setformat__(typestr, fmt) -> None
     |      
     |      You probably don't want to use this function.  It exists mainly to be
     |      used in Python's test suite.
     |      
     |      typestr must be 'double' or 'float'.  fmt must be one of 'unknown',
     |      'IEEE, big-endian' or 'IEEE, little-endian', and in addition can only be
     |      one of the latter two if it appears to match the underlying C reality.
     |      
     |      Override the automatic determination of C-level floating point type.
     |      This affects how floats are converted to and from binary strings.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  __trunc__(...)
     |      Return the Integral closest to x between 0 and x.
     |  
     |  as_integer_ratio(...)
     |      float.as_integer_ratio() -> (int, int)
     |      
     |      Return a pair of integers, whose ratio is exactly equal to the original
     |      float and with a positive denominator.
     |      Raise OverflowError on infinities and a ValueError on NaNs.
     |      
     |      >>> (10.0).as_integer_ratio()
     |      (10, 1)
     |      >>> (0.0).as_integer_ratio()
     |      (0, 1)
     |      >>> (-.25).as_integer_ratio()
     |      (-1, 4)
     |  
     |  conjugate(...)
     |      Return self, the complex conjugate of any float.
     |  
     |  fromhex(...) from builtins.type
     |      float.fromhex(string) -> float
     |      
     |      Create a floating-point number from a hexadecimal string.
     |      >>> float.fromhex('0x1.ffffp10')
     |      2047.984375
     |      >>> float.fromhex('-0x1p-1074')
     |      -5e-324
     |  
     |  hex(...)
     |      float.hex() -> string
     |      
     |      Return a hexadecimal representation of a floating-point number.
     |      >>> (-0.1).hex()
     |      '-0x1.999999999999ap-4'
     |      >>> 3.14159.hex()
     |      '0x1.921f9f01b866ep+1'
     |  
     |  is_integer(...)
     |      Return True if the float is an integer.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  imag
     |      the imaginary part of a complex number
     |  
     |  real
     |      the real part of a complex number
    
    

The ``float`` class has a single constructor, which can take a number or a string and will attempt to convert it to a float.


```
float(10)
```




    10.0




```
float(3.14)
```




    3.14




```
float('0.1')
```




    0.1



However, strings that represent fractions cannot be converted to floats, unlike the Fraction class we saw earlier.


```
float('22/7')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-5-32cff4369993> in <module>()
    ----> 1 float('22/7')
    

    ValueError: could not convert string to float: '22/7'


If you really want to get a float from a string such as ``'22/7'``, you could first create a ``Fraction``, then create a ``float`` from that:


```
from fractions import Fraction
```


```
float(Fraction('22/7'))
```

Floats do not always have an exact representation:


```
print(0.1)
```

Although this looks like ``0.1`` exactly, we need to reveal more digits after the decimal point to see what's going on:


```
format(0.1, '.25f')
```

However, certain numbers can be represented exactly in a binary fraction expansion:


```
format(0.125, '.25f')
```

This is because 0.125 is precisely 1/8, or 1/(2^3)

##  Floats - Equality Testing

Because not all real numbers have an exact ``float`` representation, equality testing can be tricky.


```
x = 0.1 + 0.1 + 0.1
y = 0.3
x == y
```




    False



This is because ``0.1`` and ``0.3`` do not have exact representations:


```
print('0.1 --> {0:.25f}'.format(0.1))
print('x --> {0:.25f}'.format(x))
print('y --> {0:.25f}'.format(y))
```

    0.1 --> 0.1000000000000000055511151
    x --> 0.3000000000000000444089210
    y --> 0.2999999999999999888977698
    

However, in some (limited) cases where all the numbers involved do have an exact representation, it will work:


```
x = 0.125 + 0.125 + 0.125
y = 0.375
x == y
```




    True




```
print('0.125 --> {0:.25f}'.format(0.125))
print('x --> {0:.25f}'.format(x))
print('y --> {0:.25f}'.format(y))
```

    0.125 --> 0.1250000000000000000000000
    x --> 0.3750000000000000000000000
    y --> 0.3750000000000000000000000
    

One simple way to get around this is to round to a specific number of digits and then compare


```
x = 0.1 + 0.1 + 0.1
y = 0.3
round(x, 5) == round(y, 5)
```




    True



We can also use a more flexible technique implemented by the ``isclose`` method in the ``math`` module


```
from math import isclose
```


```
help(isclose)
```

    Help on built-in function isclose in module math:
    
    isclose(...)
        isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0) -> bool
        
        Determine whether two floating point numbers are close in value.
        
           rel_tol
               maximum difference for being considered "close", relative to the
               magnitude of the input values
            abs_tol
               maximum difference for being considered "close", regardless of the
               magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    


```
x = 0.1 + 0.1 + 0.1
y = 0.3
isclose(x, y)
```




    True



The ``isclose`` method takes two optional parameters, ``rel_tol`` and ``abs_tol``.

``rel_tol`` is a relative tolerance that will be relative to the magnitude of the largest of the two numbers being compared. Useful when we want to see if two numbers are close to each other as a percentage of their magnitudes.

``abs_tol`` is an absolute tolerance that is independent of the magnitude of the numbers we are comparing - this is useful for numbers that are close to zero.

In this situation we might consider x and y to be close to each other:


```
x = 123456789.01
y = 123456789.02
```

but not in this case:


```
x = 0.01
y = 0.02
```

In both these cases the difference between the two numbers was ``0.01``, yet in one case we considered the numbers "equal" and in the other, not "equal". Relative tolerances are useful to handle these scenarios.


```
isclose(123456789.01, 123456789.02, rel_tol=0.01)
```




    True




```
isclose(0.01, 0.02, rel_tol=0.01)
```




    False



On the other hand, we have to be careful with relative tolerances when working with values that are close to zero:


```
x = 0.0000001
y = 0.0000002
isclose(x, y, rel_tol=0.01)
```




    False



So, we could use an absolute tolerance here:


```
isclose(x, y, abs_tol=0.0001, rel_tol=0)
```




    True



In general, we can combine the use of both relative and absolute tolerances in this way:


```
x = 0.0000001
y = 0.0000002

a = 123456789.01
b = 123456789.02

print('x = y:', isclose(x, y, abs_tol=0.0001, rel_tol=0.01))
print('a = b:', isclose(a, b, abs_tol=0.0001, rel_tol=0.01))
```

    x = y: True
    a = b: True
    

##  Coercing Floats to Integers

#### Truncation


```
from math import trunc
```


```
trunc(10.3), trunc(10.5), trunc(10.6)
```




    (10, 10, 10)




```
trunc(-10.6), trunc(-10.5), trunc(-10.3)
```




    (-10, -10, -10)



The **int** constructor uses truncation when a float is passed in:


```
int(10.3), int(10.5), int(10.6)
```




    (10, 10, 10)




```
int(-10.5), int(-10.5), int(-10.4)
```




    (-10, -10, -10)



#### Floor


```
from math import floor
```


```
floor(10.4), floor(10.5), floor(10.6)
```




    (10, 10, 10)




```
floor(-10.4), floor(-10.5), floor(-10.6)
```




    (-11, -11, -11)



#### Ceiling


```
from math import ceil
```


```
ceil(10.4), ceil(10.5), ceil(10.6)
```




    (11, 11, 11)




```
ceil(-10.4), ceil(-10.5), ceil(-10.6)
```




    (-10, -10, -10)



##  Rounding


```
help(round)

```

    Help on built-in function round in module builtins:
    
    round(...)
        round(number[, ndigits]) -> number
        
        Round a number to a given precision in decimal digits (default 0 digits).
        This returns an int when called with one argument, otherwise the
        same type as the number. ndigits may be negative.
    
    

#### n = 0


```
a = round(1.5)
a, type(a)
```




    (2, int)




```
a = round(1.5, 0)
a, type(b)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-356ec769b541> in <module>()
          1 a = round(1.5, 0)
    ----> 2 a, type(b)
    

    NameError: name 'b' is not defined


#### n > 0


```
round(1.8888, 3), round(1.8888, 2), round(1.8888, 1), round(1.8888, 0)
```

#### n < 0


```
round(888.88, 1), round(888.88, 0), \
round(888.88, -1), round(888.88, -2), \
round(888.88, -3)
```

#### Ties


```
round(1.25, 1)
```


```
round(1.35, 1)
```

This is rounding to nearest, with ties to nearest number with even least significant digit, aka Banker's Rounding.

Works similarly with **n** negative.


```
round(15, -1)
```


```
round(25, -1)
```

#### Rounding to closest, ties away from zero

This is traditionally the type of rounding taught in school, which is different from the Banker's Rounding implemented in Python (and in many other programming languages)

1.5 --> 2 <br>
2.5 --> 3 <br>

-1.5 --> -2 <br>
-2.5 --> -3 <br>

To do this type of rounding (to nearest 1) we can add (for positive numbers) or subtract (for negative numbers) 0.5 and then truncate the resulting number.


```
def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))
```


```
round(1.5), _round(1.5)
```


```
round(2.5), _round(2.5)
```

##  Decimals


```
import decimal
```


```
from decimal import Decimal
```

Decimals have context, that can be used to specify rounding and precision (amongst other things)

Contexts can be local (temporary contexts) or global (default)

#### Global Context


```
g_ctx  = decimal.getcontext()
```


```
g_ctx.prec
```




    28




```
g_ctx.rounding
```




    'ROUND_HALF_EVEN'



We can change settings in the global context:


```
g_ctx.prec = 6
```


```
g_ctx.rounding = decimal.ROUND_HALF_UP
```

And if we read this back directly from the global context:


```
decimal.getcontext().prec
```




    6




```
decimal.getcontext().rounding
```




    'ROUND_HALF_UP'



we see that the global context was indeed changed.

#### Local Context

The ``localcontext()`` function will return a context manager that we can use with a ``with`` statement:


```
with decimal.localcontext() as ctx:
    print(ctx.prec)
    print(ctx.rounding)
```

    6
    ROUND_HALF_UP
    

Since no argument was specified in the ``localcontext()`` call, it provides us a context manager that uses a copy of the global context.

Modifying the local context has no effect on the global context


```
with decimal.localcontext() as ctx:
    ctx.prec = 10
    print('local prec = {0}, global prec = {1}'.format(ctx.prec, g_ctx.prec))
```

    local prec = 10, global prec = 6
    

#### Rounding


```
decimal.getcontext().rounding
```




    'ROUND_HALF_UP'



The rounding mechanism is ROUND_HALF_UP because we set the global context to that earlier in this notebook. Note that normally the default is ROUND_HALF_EVEN.

So we first reset our global context rounding to that:


```
decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
```


```
x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1))
print(round(y, 1))
```

    1.2
    1.4
    

Let's change the rounding mechanism in the global context to ROUND_HALF_UP:


```
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
```


```
x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1))
print(round(y, 1))
```

    1.3
    1.4
    

As you may have realized, changing the global context is a pain if you need to constantly switch between different precisions and rounding algorithms. Also, it could introduce bugs if you forget that you changed the global context somewhere further up in your module.

For this reason, it is usually better to use a local context manager instead:

First we reset our global context rounding to the default:


```
decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN
```


```
x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1), round(y, 1))
with decimal.localcontext() as ctx:
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1), round(y, 1))
print(round(x, 1), round(y, 1))
```

    1.2 1.4
    1.3 1.4
    1.2 1.4
    

##  Decimals: Constructors and Contexts

The **Decimal** constructor can handle a variety of data types


```
import decimal
from decimal import Decimal
```

#### Integers


```
Decimal(10)
```




    Decimal('10')




```
Decimal(-10)
```




    Decimal('-10')



#### Strings


```
Decimal('0.1')
```




    Decimal('0.1')




```
Decimal('-3.1415')
```




    Decimal('-3.1415')



#### Tuples


```
Decimal ((0, (3,1,4,1,5), -4))
```




    Decimal('3.1415')




```
Decimal((1, (1,2,3,4), -3))
```




    Decimal('-1.234')




```
Decimal((0, (1,2,3), 3))
```




    Decimal('1.23E+5')



#### But don't use Floats


```
format(0.1, '.25f')
```




    '0.1000000000000000055511151'




```
Decimal(0.1)
```




    Decimal('0.1000000000000000055511151231257827021181583404541015625')



As you can see, since we passed an approximate binary float to the Decimal constructor it did it's best to represent that binary float **exactly**!!

So, instead, use strings or tuples in the Decimal constructor.

#### Context Precision and the Constructor

The context precision does nto affect the precision used when creating a Decimal object - those are independent of each other.

Let's set our global (default) context to a precision of 2


```
decimal.getcontext().prec = 2
```

Now we can create decimal numbers of higher precision than that:


```
a = Decimal('0.12345')
b = Decimal('0.12345')
```


```
a
```




    Decimal('0.12345')




```
b
```




    Decimal('0.12345')



But when we add those two numbers up, the context precision will matter:


```
a+b
```




    Decimal('0.25')



As you can see, we ended up with a sum that was rounded to 2 digits after the decimal point (precision = 2)

#### Local and Global Contexts are Independent


```
decimal.getcontext().prec = 6
```


```
decimal.getcontext().rounding
```




    'ROUND_HALF_EVEN'




```
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a + b)
with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print('c within local context: {0}'.format(c))
print('c within global context: {0}'.format(c))
```

    0.24690
    c within local context: 0.25
    c within global context: 0.25
    

Since **c** was created within the local context by adding **a** and **b**, and the local context had a precision of 2, **c** was rounded to 2 digits after the decimal point.

Once the local context is destroyed (after the **with** block), the variable **c** still exists, and its precision is **still** just 2 - it doesn't magically suddenly get the global context's precision of 6.

##  Decimals - Math Operations

#### Div and Mod

The // and % operators (and consequently, the divmod() function) behave differently for integers and Decimals.

This is because integer division for Decimals is performed differently, and results in a truncated division, whereas integers use a floored division.

These differences are only when negative numbers are involved. If all numbers involved are positive, then integer and Decimal div and mod operations are equal.

But in both cases the // and % operators satisfy the equation:

``n = d * (n // d) + (n % d)``


```
import decimal
from decimal import Decimal
```


```
x = 10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print( x == y * (x//y) + x % y)
```

    3 1
    (3, 1)
    True
    


```
a = Decimal('10')
b = Decimal('3')
print(a//b, a%b)
print(divmod(a, b))
print( a == b * (a//b) + a % b)
```

    3 1
    (Decimal('3'), Decimal('1'))
    True
    

As we can see, the // and % operators had the same result when both numbers were positive.


```
x = -10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print( x == y * (x//y) + x % y)
```

    -4 2
    (-4, 2)
    True
    


```
a = Decimal('-10')
b = Decimal('3')
print(a//b, a%b)
print(divmod(a, b))
print( a == b * (a//b) + a % b)
```

    -3 -1
    (Decimal('-3'), Decimal('-1'))
    True
    

On the other hand, we see that in this case the // and % operators did not result in the same values, although the equation was satisfied in both instances.

#### Other Mathematical Functions

The Decimal class implements a variety of mathematical functions.


```
a = Decimal('1.5')
print(a.log10())  # base 10 logarithm
print(a.ln())     # natural logarithm (base e)
print(a.exp())    # e**a
print(a.sqrt())   # square root
```

    0.1760912590556812420812890085
    0.4054651081081643819780131155
    4.481689070338064822602055460
    1.224744871391589049098642037
    

Although you can use the math function of the math module, be aware that the math module functions will cast the Decimal numbers to floats when it performs the various operations. So, if the precision is important (which it probably is if you decided to use Decimal numbers in the first place), choose the math functions of the Decimal class over those of the math module.


```
x = 2
x_dec = Decimal(2)
```


```
import math
```


```
root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()
```


```
print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)
```

    1.414213562373095145474621859
    1.414213562373095145474621859
    1.414213562373095048801688724
    


```
print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)
```

    2.000000000000000444089209850
    2.000000000000000444089209850
    1.999999999999999999999999999
    


```
x = 0.01
x_dec = Decimal('0.01')

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)
```

    0.100000000000000005551115123
    0.100000000000000005551115123
    0.1
    


```
print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)
```

    0.010000000000000001942890293
    0.010000000000000001942890293
    0.01
    

##  Decimals: Performance Considerations

#### Memory Footprint

Decimals take up a lot more memory than floats.


```
import sys
from decimal import Decimal
```


```
a = 3.1415
b = Decimal('3.1415')
```


```
sys.getsizeof(a)
```




    24



24 bytes are used to store the float 3.1415


```
sys.getsizeof(b)
```




    104



104 bytes are used to store the Decimal 3.1415

#### Computational Performance

Decimal arithmetic is also much slower than float arithmetic (on a CPU, and even more so if using a GPU)

We can do some rough timings to illustrate this.

First we look at the performance difference creating floats vs decimals:


```
import time
from decimal import Decimal

def run_float(n=1):
    for i in range(n):
        a = 3.1415
        
def run_decimal(n=1):
    for i in range(n):
        a = Decimal('3.1415')

```

Timing float and Decimal operations:


```
n = 10000000
```


```
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)
```

    float:  0.21406484986433047
    decimal:  2.1353148079910156
    

We make a slight variant here to see how addition compares between the two types:


```
def run_float(n=1):
    a = 3.1415
    for i in range(n):
        a + a
        
def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a + a
        
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)
```

    float:  0.1875864573764936
    decimal:  0.3911394302055555
    

How about square roots:

(We drop the n count a bit)


```
n = 5000000

import math

def run_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)
        
def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a.sqrt()
        
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)
```

    float:  0.673833850211659
    decimal:  14.73112183459776
    

##  Complex Numbers

Python's built-in class provides support for complex numbers.

Complex numbers are defined in rectangular coordinates (real and imaginary parts) using either the constructor or a literal expression.

The complex number 1 + 2j can be defined in either of these ways:


```
a = complex(1, 2)
b = 1 + 2j
```


```
a == b
```




    True



Note that the real and imaginary parts are defined as floats, and can be retrieved as follows:


```
a.real, type(a.real)
```




    (1.0, float)




```
a.imag, type(a.imag)
```




    (2.0, float)



The complex conjugate can be calculated as follows:


```
a.conjugate()
```




    (1-2j)



The standard arithmetic operatots are polymorphic and defined for complex numbers


```
a = 1 + 2j
b = 3 - 4j
c = 5j
d = 10
```


```
a + b
```




    (4-2j)




```
b * c
```




    (20+15j)




```
c / d
```




    0.5j




```
d - a
```




    (9-2j)



The // and % operators, although also polymorphic, are not defined for complex numbers:


```
a // b
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-11-d3400ddfd09e> in <module>()
    ----> 1 a // b
    

    TypeError: can't take floor of complex number.



```
a % b
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-209a85c6b5ad> in <module>()
    ----> 1 a % b
    

    TypeError: can't mod complex numbers.


The == and != operators support complex numbers - but since the real and imaginary parts of complex numbers are floats, the same problems comparing floats using == and != also apply to complex numbers.


```
a = 0.1j
a + a + a == 0.3j
```




    False



In addition, the standard comparison operators (<, <=, >, >=) are not defined for complex numbers.


```
a = 1 + 1j
b = 100 + 100j
a < b
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-15-a9748a0ff9df> in <module>()
          1 a = 1 + 1j
          2 b = 100 + 100j
    ----> 3 a < b
    

    TypeError: '<' not supported between instances of 'complex' and 'complex'


#### Math Functions

The **cmath** module provides complex alternatives to the standard **math** functions.

In addition, the **cmath** module provides the complex implementation of the **isclose()** method available for floats.


```
import cmath

a = 1 + 5j
print(cmath.sqrt(a))
```

    (1.7462845577958914+1.4316108957382214j)
    

The standard **math** module functions will not work with complex numbers:


```
import math
print(math.sqrt(a))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-18-77a8fdd31911> in <module>()
          1 import math
    ----> 2 print(math.sqrt(a))
    

    TypeError: can't convert complex to float


#### Polar / Rectangular Conversions

The **cmath.phase()** function can be used to return the phase (or argument) of  any complex number.

The standard **abs()** function supports complex numbers and will return the magnitude (euclidean norm) of the complex number.


```
a = 1 + 1j
```


```
r = abs(a)
phi = cmath.phase(a)
print('{0} = ({1},{2})'.format(a, r, phi))
```

    (1+1j) = (1.4142135623730951,0.7853981633974483)
    

Complex numbers in polar coordinates can be converted to rectangular coordinates using the **math.rect()** function:


```
r = math.sqrt(2)
phi = cmath.pi/4
print(cmath.rect(r, phi))
```

    (1.0000000000000002+1.0000000000000002j)
    

#### Euler's Identity and the **isclose()** function

e<sup>i &pi;</sup> + 1 = 0


```
RHS = cmath.exp(cmath.pi * 1j) + 1
print(RHS)
```

    1.2246467991473532e-16j
    

Which, because of limited precision is not quite zero.

However, the result is very close to zero.

We can use the **isclose()** method of the **cmath** module, which behaves similarly to the **math.isclose()** method. Since we are testing for closeness of two numbers close to zero, we need to make sure an absolute tolerance is also specified:


```
cmath.isclose(RHS, 0, abs_tol=0.00001)
```




    True



If we had not specified an absolute tolerance:


```
cmath.isclose(RHS, 0)
```




    False



##  Booleans

The **bool** class is used to represent boolean values.

The **bool** class inherits from the **int** class.


```
issubclass(bool, int)
```




    True



Two built-in constants, **True** and **False** are singleton instances of the bool class with underlying int values of 1 and 0 respectively.


```
type(True), id(True), int(True)
```




    (bool, 1658060976, 1)




```
type(False), id(False), int(False)
```




    (bool, 1658061008, 0)



These two values are instances of the **bool** class, and by inheritance are also **int** objects.


```
isinstance(True, bool)
```




    True




```
isinstance(True, int)
```




    True



Since **True** and **False** are singletons, we can use either the **is** operator, or the **==** operator to compare them to **any** boolean expression.


```
id(True), id(1 < 2)
```




    (1658060976, 1658060976)




```
id(False), id(1 == 3)
```




    (1658061008, 1658061008)




```
(1 < 2) is True, (1 < 2) == True
```




    (True, True)




```
(1 == 2) is False, (1 == 2) == False
```




    (True, True)



Be careful with that last comparison, the parentheses are necessary!


```
1 == 2 == False
```




    False




```
(1 == 2) == False
```




    True



We'll look into this in detail later, but, for now, this happens because a chained comparison such as **a == b == c** is actually evaluated as **a == b and b == c**

So **1 == 2 == False ** is the same as **1 == 2 and 2 == False**


```
1 == 2, 2 == False, 1==2 and 2==False
```




    (False, False, False)



But, 


```
(1 == 2)
```




    False



So **(1 == 2) == False** evaluates to True

But since **False** is also **0**, we get the following:


```
(1 == 2) == 0
```




    True



The underlying integer values of True and False are:


```
int(True), int(False)
```




    (1, 0)



So, using an equality comparison:


```
1 == True, 0 == False
```




    (True, True)



But, from an object perspective 1 and True are not the same (similarly with 0 and False)


```
1 == True, 1 is True
```




    (True, False)




```
0 == False, 0 is False
```




    (True, False)



Any integer can be cast to a boolean, and follows the rule:

bool(x) = True for any x except for zero which returns False


```
bool(0)
```




    False




```
bool(1), bool(100), bool(-1)
```




    (True, True, True)



Since booleans are subclassed from integers, they can behave like integers, and because of polymorphism all the standard integer operators, properties and methods apply


```
True > False
```




    True




```
True + 2
```




    3




```
False // 2
```




    0




```
True + True + True
```




    3




```
(True + True + True) % 2
```




    1




```
-True
```




    -1




```
100 * False
```




    0



I certainly **do not** recommend you write code like that shown above, but be aware that it does work.

##  Booleans: Truth Values

All objects in Python have an associated **truth value**, or **truthyness**

We saw in a previous lecture that integers have an inherent truth value:


```
bool(0)
```




    False




```
bool(1), bool(-1), bool(100)
```




    (True, True, True)



This truthyness has nothing to do with the fact that **bool** is a subclass of **int**.

Instead, it has to do with the fact that the **int** class implements a `__bool__()` method:


```
help(bool)
```

    Help on class bool in module builtins:
    
    class bool(int)
     |  bool(x) -> bool
     |  
     |  Returns True when the argument x is true, False otherwise.
     |  The builtins True and False are the only two instances of the class bool.
     |  The class bool is a subclass of the class int, and cannot be subclassed.
     |  
     |  Method resolution order:
     |      bool
     |      int
     |      object
     |  
     |  Methods defined here:
     |  
     |  __and__(self, value, /)
     |      Return self&value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __or__(self, value, /)
     |      Return self|value.
     |  
     |  __rand__(self, value, /)
     |      Return value&self.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __ror__(self, value, /)
     |      Return value|self.
     |  
     |  __rxor__(self, value, /)
     |      Return value^self.
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  __xor__(self, value, /)
     |      Return self^value.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from int:
     |  
     |  __abs__(self, /)
     |      abs(self)
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __bool__(self, /)
     |      self != 0
     |  
     |  __ceil__(...)
     |      Ceiling of an Integral returns itself.
     |  
     |  __divmod__(self, value, /)
     |      Return divmod(self, value).
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __float__(self, /)
     |      float(self)
     |  
     |  __floor__(...)
     |      Flooring an Integral returns itself.
     |  
     |  __floordiv__(self, value, /)
     |      Return self//value.
     |  
     |  __format__(...)
     |      default object formatter
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getnewargs__(...)
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __index__(self, /)
     |      Return self converted to an integer, if self is suitable for use as an index into a list.
     |  
     |  __int__(self, /)
     |      int(self)
     |  
     |  __invert__(self, /)
     |      ~self
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __lshift__(self, value, /)
     |      Return self<<value.
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mod__(self, value, /)
     |      Return self%value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __neg__(self, /)
     |      -self
     |  
     |  __pos__(self, /)
     |      +self
     |  
     |  __pow__(self, value, mod=None, /)
     |      Return pow(self, value, mod).
     |  
     |  __radd__(self, value, /)
     |      Return value+self.
     |  
     |  __rdivmod__(self, value, /)
     |      Return divmod(value, self).
     |  
     |  __rfloordiv__(self, value, /)
     |      Return value//self.
     |  
     |  __rlshift__(self, value, /)
     |      Return value<<self.
     |  
     |  __rmod__(self, value, /)
     |      Return value%self.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __round__(...)
     |      Rounding an Integral returns itself.
     |      Rounding with an ndigits argument also returns an integer.
     |  
     |  __rpow__(self, value, mod=None, /)
     |      Return pow(value, self, mod).
     |  
     |  __rrshift__(self, value, /)
     |      Return value>>self.
     |  
     |  __rshift__(self, value, /)
     |      Return self>>value.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rtruediv__(self, value, /)
     |      Return value/self.
     |  
     |  __sizeof__(...)
     |      Returns size in memory, in bytes
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __truediv__(self, value, /)
     |      Return self/value.
     |  
     |  __trunc__(...)
     |      Truncating an Integral returns itself.
     |  
     |  bit_length(...)
     |      int.bit_length() -> int
     |      
     |      Number of bits necessary to represent self in binary.
     |      >>> bin(37)
     |      '0b100101'
     |      >>> (37).bit_length()
     |      6
     |  
     |  conjugate(...)
     |      Returns self, the complex conjugate of any int.
     |  
     |  from_bytes(...) from builtins.type
     |      int.from_bytes(bytes, byteorder, *, signed=False) -> int
     |      
     |      Return the integer represented by the given array of bytes.
     |      
     |      The bytes argument must be a bytes-like object (e.g. bytes or bytearray).
     |      
     |      The byteorder argument determines the byte order used to represent the
     |      integer.  If byteorder is 'big', the most significant byte is at the
     |      beginning of the byte array.  If byteorder is 'little', the most
     |      significant byte is at the end of the byte array.  To request the native
     |      byte order of the host system, use `sys.byteorder' as the byte order value.
     |      
     |      The signed keyword-only argument indicates whether two's complement is
     |      used to represent the integer.
     |  
     |  to_bytes(...)
     |      int.to_bytes(length, byteorder, *, signed=False) -> bytes
     |      
     |      Return an array of bytes representing an integer.
     |      
     |      The integer is represented using length bytes.  An OverflowError is
     |      raised if the integer is not representable with the given number of
     |      bytes.
     |      
     |      The byteorder argument determines the byte order used to represent the
     |      integer.  If byteorder is 'big', the most significant byte is at the
     |      beginning of the byte array.  If byteorder is 'little', the most
     |      significant byte is at the end of the byte array.  To request the native
     |      byte order of the host system, use `sys.byteorder' as the byte order value.
     |      
     |      The signed keyword-only argument determines whether two's complement is
     |      used to represent the integer.  If signed is False and a negative integer
     |      is given, an OverflowError is raised.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from int:
     |  
     |  denominator
     |      the denominator of a rational number in lowest terms
     |  
     |  imag
     |      the imaginary part of a complex number
     |  
     |  numerator
     |      the numerator of a rational number in lowest terms
     |  
     |  real
     |      the real part of a complex number
    
    

If you scroll down in the documentation you shoudl reach a section that looks like this:

`` 
|  __bool__(self, /)
|      self != 0
``

So, when we write:


```
bool(100)
```




    True



Python is actually calling 100.__bool__() and returning that:


```
(100).__bool__()
```




    True




```
(0).__bool__()
```




    False



Most objects will implement either the `__bool__()` or `__len__()` methods. If they don't, then their associated value will be **True** always.

#### Numeric Types

Any non-zero numeric value is truthy. Any zero numeric value is falsy:


```
from fractions import Fraction
from decimal import Decimal
bool(10), bool(1.5), bool(Fraction(3, 4)), bool(Decimal('10.5'))
```




    (True, True, True, True)




```
bool(0), bool(0.0), bool(Fraction(0,1)), bool(Decimal('0')), bool(0j)
```




    (False, False, False, False, False)



#### Sequence Types

An empty sequence type object is Falsy, a non-empty one is truthy:


```
bool([1, 2, 3]), bool((1, 2, 3)), bool('abc'), bool(1j)
```




    (True, True, True, True)




```
bool([]), bool(()), bool('')
```




    (False, False, False)



#### Mapping Types

Similarly, an empty mapping type will be falsy, a non-empty one truthy:


```
bool({'a': 1}), bool({1, 2, 3})
```




    (True, True)




```
bool({}), bool(set())
```




    (False, False)



#### The None Object

The singleton **None** object is always falsy:


```
bool(None)
```




    False



#### One Application of Truth Values

Any conditional expression which involves objects other than **bool** types, will use the associated truth value as the result of the conditional expression.


```
a = [1, 2, 3]
if a:
    print(a[0])
else:
    print('a is None, or a is empty')
```

    1
    


```
a = []
if a:
    print(a[0])
else:
    print('a is None, or a is empty')
```

    a is None, or a is empty
    


```
a = 'abc'
if a:
    print(a[0])
else:
    print('a is None, or a is empty')
```

    a
    


```
a = ''
if a:
    print(a[0])
else:
    print('a is None, or a is empty')
```

    a is None, or a is empty
    

We could write this using a more lengthy expression:


```
a = 'abc'
if a is not None and len(a) > 0:
    print(a[0])
else:
    print('a is None, or a is empty')
```

    a
    

Doing the following would break our code in some instances:


```
a = 'abc'
if a is not None:
    print(a[0])
```

    a
    

works, but:


```
a = ''
if a is not None:
    print(a[0])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-44-47991d9c7397> in <module>()
          1 a = ''
          2 if a is not None:
    ----> 3     print(a[0])
    

    IndexError: string index out of range

or even:

```
a = None
if len(a) > 0:
    print(a[0])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-45-92ec20435e20> in <module>()
          1 a = None
    ----> 2 if len(a) > 0:
          3     print(a[0])
    

    TypeError: object of type 'NoneType' has no len()


To be torough we would need to write:


```
a = None
if a is not None and len(a) > 0:
    print(a[0])
```

Also, the order of the boolean expressions matter here!

We'll discuss this and short-circuit evaluations in an upcoming video.

For example:


```
a = None
if len(a) > 0 and a is not None:
    print(a[0])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-47-0842480c6625> in <module>()
          1 a = None
    ----> 2 if len(a) > 0 and a is not None:
          3     print(a[0])
    

    TypeError: object of type 'NoneType' has no len()


##  Booleans: Precedence and Short-Circuiting


```
True or True and False
```




    True



this is equivalent, because of ``and`` having higer precedence than ``or``, to:


```
True or (True and False)
```




    True



This is not the same as:


```
(True or True) and False
```




    False



#### Short-Circuiting


```
a = 10
b = 2

if a/b > 2:
    print('a is at least double b')
```

    a is at least double b
    


```
a = 10
b = 0

if a/b > 2:
    print('a is at least double b')
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-12-98ac73a1accd> in <module>()
          2 b = 0
          3 
    ----> 4 if a/b > 2:
          5     print('a is at least double b')
    

    ZeroDivisionError: division by zero



```
a = 10
b = 0

if b and a/b > 2:
    print('a is at least double b')
```

Can also be useful to deal with null or empty strings in a database:


```
import string
```


```
help(string)
```

    Help on module string:
    
    NAME
        string - A collection of string constants.
    
    DESCRIPTION
        Public module variables:
        
        whitespace -- a string containing all ASCII whitespace
        ascii_lowercase -- a string containing all ASCII lowercase letters
        ascii_uppercase -- a string containing all ASCII uppercase letters
        ascii_letters -- a string containing all ASCII letters
        digits -- a string containing all ASCII decimal digits
        hexdigits -- a string containing all ASCII hexadecimal digits
        octdigits -- a string containing all ASCII octal digits
        punctuation -- a string containing all ASCII punctuation characters
        printable -- a string containing all ASCII characters considered printable
    
    CLASSES
        builtins.object
            Formatter
            Template
        
        class Formatter(builtins.object)
         |  Methods defined here:
         |  
         |  check_unused_args(self, used_args, args, kwargs)
         |  
         |  convert_field(self, value, conversion)
         |  
         |  format(*args, **kwargs)
         |  
         |  format_field(self, value, format_spec)
         |  
         |  get_field(self, field_name, args, kwargs)
         |      # given a field_name, find the object it references.
         |      #  field_name:   the field being looked up, e.g. "0.name"
         |      #                 or "lookup[3]"
         |      #  used_args:    a set of which args have been used
         |      #  args, kwargs: as passed in to vformat
         |  
         |  get_value(self, key, args, kwargs)
         |  
         |  parse(self, format_string)
         |      # returns an iterable that contains tuples of the form:
         |      # (literal_text, field_name, format_spec, conversion)
         |      # literal_text can be zero length
         |      # field_name can be None, in which case there's no
         |      #  object to format and output
         |      # if field_name is not None, it is looked up, formatted
         |      #  with format_spec and conversion and then used
         |  
         |  vformat(self, format_string, args, kwargs)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
        
        class Template(builtins.object)
         |  A string class for supporting $-substitutions.
         |  
         |  Methods defined here:
         |  
         |  __init__(self, template)
         |      Initialize self.  See help(type(self)) for accurate signature.
         |  
         |  safe_substitute(*args, **kws)
         |  
         |  substitute(*args, **kws)
         |  
         |  ----------------------------------------------------------------------
         |  Data descriptors defined here:
         |  
         |  __dict__
         |      dictionary for instance variables (if defined)
         |  
         |  __weakref__
         |      list of weak references to the object (if defined)
         |  
         |  ----------------------------------------------------------------------
         |  Data and other attributes defined here:
         |  
         |  delimiter = '$'
         |  
         |  flags = <RegexFlag.IGNORECASE: 2>
         |  
         |  idpattern = '[_a-z][_a-z0-9]*'
         |  
         |  pattern = re.compile('\n    \\$(?:\n      (?P<escaped>\\$)..._a-z][_a-...
    
    FUNCTIONS
        capwords(s, sep=None)
            capwords(s [,sep]) -> string
            
            Split the argument into words using split, capitalize each
            word using capitalize, and join the capitalized words using
            join.  If the optional second argument sep is absent or None,
            runs of whitespace characters are replaced by a single space
            and leading and trailing whitespace are removed, otherwise
            sep is used to split and join the words.
    
    DATA
        __all__ = ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'cap...
        ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'
        hexdigits = '0123456789abcdefABCDEF'
        octdigits = '01234567'
        printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
        punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        whitespace = ' \t\n\r\x0b\x0c'
    
    FILE
        c:\users\fbapt\anaconda3\envs\deepdive\lib\string.py
    
    
    


```
string.digits
```




    '0123456789'




```
string.ascii_letters
```




    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'




```
name = ''
if name[0] in string.digits:
    print('Name cannot start with a digit!')
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-19-b6d1fe6f1f39> in <module>()
          1 name = ''
    ----> 2 if name[0] in string.digits:
          3     print('Name cannot start with a digit!')
    

    IndexError: string index out of range



```
name = ''
if name and name[0] in string.digits:
    print('Name cannot start with a digit!')
```


```
name = None
if name and name[0] in string.digits:
    print('Name cannot start with a digit!')
```


```
name = 'Bob'
if name and name[0] in string.digits:
    print('Name cannot start with a digit!')
```


```
name = '1Bob'
if name and name[0] in string.digits:
    print('Name cannot start with a digit!')
```

    Name cannot start with a digit!
    

##  Booleans: Boolean Operators

The way the Boolean operators ``and``, ``or`` actually work is a littel different in Python:

#### or

``X or Y``: If X is falsy, returns Y, otherwise evaluates and returns X


```
'' or 'abc'
```




    'abc'




```
0 or 100
```




    100




```
[] or [1, 2, 3]
```




    [1, 2, 3]




```
[1, 2] or [1, 2, 3]
```




    [1, 2]



You should note that the truth value of ``Y`` is never even considered when evaluating the ``or`` result!

Only the left operand matters.

Of course, Y will be evaluated if it is being returned - but its truth value does not affect how the ``or`` is being calculated.

You probably will notice that this means ``Y`` is not evaluated if ``X`` is returned - short-circuiting!!!

We could (almost!) write the ``or`` operator ourselves in this way:


```
def _or(x, y):
    if x:
        return x
    else:
        return y
```


```
print(_or(0, 100) == (0 or 100))
print(_or(None, 'n/a') == (None or 'n/a'))
print(_or('abc', 'n/a') == ('abc' or 'n/a'))
```

    True
    True
    True
    

Why did I say almost?

Unlike the ``or`` operator, our ``_or`` function will always evaluate x and y (they are passed as arguments) - so we do not have short-circuiting!


```
1 or 1/0
```




    1




```
_or(1, 1/0)
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-32-7b66dcdf3d9c> in <module>()
    ----> 1 _or(1, 1/0)
    

    ZeroDivisionError: division by zero


#### and

`X and Y`: If X is falsy, returns X, otherwise evaluates and returns Y

Once again, note that the truth value of Y is never considered when evaluating `and`, and that ``Y`` is only evaluated if it needs to be returned (short-circuiting)


```
s1 = None
s2 = ''
s3 = 'abc'
```


```
print(s1 and s1[0])
print(s2 and s2[0])
print(s3 and s3[0])
```

    None
    
    a
    


```
print((s1 and s1[0]) or '')
print((s2 and s2[0]) or '')
print((s3 and s3[0]) or '')
```

    
    
    a
    

This technique will also work to return any default value if ``s`` is an empty string or None:


```
print((s1 and s1[0]) or 'n/a')
print((s2 and s2[0]) or 'n/a')
print((s3 and s3[0]) or 'n/a')
```

    n/a
    n/a
    a
    

The ``not`` function


```
not 'abc'
```




    False




```
not []
```




    True




```
bool(None)
```




    False




```
not None
```




    True



##  Comparison Operators

#### Identity and Membership Operators

The **is** and **is not** operators will work with any data type since they are comparing the memory addresses of the objects (which are integers)


```
0.1 is (3+4j)
```




    False




```
'a' is [1, 2, 3]
```




    False



The **in** and **not in** operators are used with iterables and test membership:


```
1 in [1, 2, 3]
```




    True




```
[1, 2] in [1, 2, 3]
```




    False




```
[1, 2] in [[1,2], [2,3], 'abc']
```




    True




```
'key1' in {'key1': 1, 'key2': 2}
```




    True




```
1 in {'key1': 1, 'key2': 2}
```




    False



We'll come back to these operators in later sections on iterables and mappings.

#### Equality Operators

The **==** and **!=** operators are value comparison operators. 

They will work with mixed types that are comparable in some sense.

For example, you can compare Fraction and Decimal objects, but it would not make sense to compare string and integer objects.


```
1 == '1'
```




    False




```
from decimal import Decimal
from fractions import Fraction
```


```
Decimal('0.1') == Fraction(1, 10)
```




    True




```
1 == 1 + 0j
```




    True




```
True == Fraction(2, 2)
```




    True




```
False == 0j
```




    True



#### Ordering Comparisons

Many, but not all data types have an ordering defined.

For example, complex numbers do not.


```
1 + 1j < 2 + 2j
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-16-82ffa8a7b757> in <module>()
    ----> 1 1 + 1j < 2 + 2j
    

    TypeError: '<' not supported between instances of 'complex' and 'complex'


Mixed type ordering comparisons is supported, but again, it needs to make sense:


```
1 < 'a'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-17-ca85dbce74b5> in <module>()
    ----> 1 1 < 'a'
    

    TypeError: '<' not supported between instances of 'int' and 'str'



```
Decimal('0.1') < Fraction(1, 2)
```




    True



#### Chained Comparisons

It is possible to chain comparisons.

For example, in **a < b < c**, Python simply **ands** the pairwise comparisons: **a < b and b < c**


```
1 < 2 < 3
```




    True




```
1 < 2 > -5 < 50 > 4
```




    True




```
1 < 2 == Decimal('2.0')
```




    True




```
import string
'A' < 'a' < 'z' > 'Z' in string.ascii_letters 
```




    True



# Section 05 - Function Parameters

##  Positional Arguments


```
def my_func(a, b, c):
    print("a={0}, b={1}, c={2}".format(a, b, c))
```


```
my_func(1, 2, 3)
```

    a=1, b=2, c=3
    

#### Default Values


```
def my_func(a, b=2, c=3):
    print("a={0}, b={1}, c={2}".format(a, b, c))
```

Note that once a parameter is assigned a default value, **all** parameters thereafter **must** be asigned a default value too!

For example, this will not work:


```
def fn(a, b=2, c):
    print(a, b, c)
```


      File "<ipython-input-4-2180ec769037>", line 1
        def fn(a, b=2, c):
              ^
    SyntaxError: non-default argument follows default argument
    



```
def my_func(a, b=2, c=3):
    print("a={0}, b={1}, c={2}".format(a, b, c))
```


```
my_func(10, 20, 30)
```

    a=10, b=20, c=30
    


```
my_func(10, 20)
```

    a=10, b=20, c=3
    


```
my_func(10)
```

    a=10, b=2, c=3
    

Since **a** does not have a default value, it **must** be specified:


```
my_func()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-9-d82eda95de40> in <module>()
    ----> 1 my_func()
    

    TypeError: my_func() missing 1 required positional argument: 'a'


#### Keyword Arguments (named arguments)

Positional arguments, can **optionally**, be specified using their corresponding parameter name.

This allows us to pass the arguments without using the positional assignment:


```
def my_func(a, b=2, c=3):
    print("a={0}, b={1}, c={2}".format(a, b, c))
```


```
my_func(c=30, b=20, a=10)
```

    a=10, b=20, c=30
    


```
my_func(10, c=30, b=20)
```

    a=10, b=20, c=30
    

Note that once a keyword argument has been used, **all** arguments thereafter **must** also be named:


```
my_func(10, b=20, 30)
```


      File "<ipython-input-13-ea05eeab2151>", line 1
        my_func(10, b=20, 30)
                         ^
    SyntaxError: positional argument follows keyword argument
    


However, if a parameter has a default value, it *can* be omitted from the argument list, named or not:


```
my_func(10, c=30)
```

    a=10, b=2, c=30
    


```
my_func(a=30, c=10)
```

    a=30, b=2, c=10
    


```
my_func(c=10, a=30)
```

    a=30, b=2, c=10
    

##  Unpacking Iterables

#### Side Note on Tuples

This is a tuple:


```
a = (1, 2, 3)
```


```
type(a)
```




    tuple



This is also a tuple:


```
a = 1, 2, 3
```


```
type(a)
```




    tuple



In fact what defines a tuple is not **()**, but the **,** (comma)

To create a tuple with a single element:


```
a = (1)
```

will not work!!


```
type(a)
```




    int



Instead, we have to use a comma:


```
a = (1,)
```


```
type(a)
```




    tuple



And in fact, we don't even need the **()**:


```
a = 1,
```


```
type(a)
```




    tuple



The only exception is to create an empty tuple:


```
a = ()
```


```
type(a)
```




    tuple



Or we can use the tuple constructor:


```
a = tuple()
```


```
type(a)
```




    tuple



#### Unpacking

Unpacking is a way to split an iterable object into individual variables contained in a list or tuple: 


```
l = [1, 2, 3, 4]
```


```
a, b, c, d = l
```


```
print(a, b, c, d)
```

    1 2 3 4
    

Strings are iterables too:


```
a, b, c = 'XYZ'
print(a, b, c)
```

    X Y Z
    

#### Swapping Two Variables

Here's a quick application of unpacking to swap the values of two variables.

First we look at the "traditional" way you would have to do it in other languages such as Java:


```
a = 10
b = 20
print("a={0}, b={1}".format(a, b))

tmp = a
a = b
b = tmp
print("a={0}, b={1}".format(a, b))
```

    a=10, b=20
    a=20, b=10
    

But using unpacking we can simplify this:


```
a = 10
b = 20
print("a={0}, b={1}".format(a, b))

a, b = b, a
print("a={0}, b={1}".format(a, b))
```

    a=10, b=20
    a=20, b=10
    

In fact, we can even simplify the initial assignment of values to a and b as follows:


```
a, b = 10, 20
print("a={0}, b={1}".format(a, b))

a, b = b, a
print("a={0}, b={1}".format(a, b))
```

    a=10, b=20
    a=20, b=10
    

#### Unpacking Unordered Objects


```
dict1 = {'p': 1, 'y': 2, 't': 3, 'h': 4, 'o': 5, 'n': 6}
```


```
dict1
```




    {'h': 4, 'n': 6, 'o': 5, 'p': 1, 't': 3, 'y': 2}




```
for c in dict1:
    print(c)
```

    p
    y
    t
    h
    o
    n
    


```
a, b, c, d, e, f = dict1
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
```

    p
    y
    t
    h
    o
    n
    

Note that this order is not guaranteed. You can always use an OrderedDict if that is a requirement.

The same applies to sets.


```
s = {'p', 'y', 't', 'h', 'o', 'n'}
```


```
type(s)
```




    set




```
print(s)
```

    {'p', 't', 'y', 'n', 'o', 'h'}
    


```
for c in s:
    print(c)
```

    p
    t
    y
    n
    o
    h
    


```
a, b, c, d, e, f = s
```


```
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
```

    p
    t
    y
    n
    o
    h
    

##  Extended Unpacking

Let's see how we might split a list into it's first element, and "everything else" using slicing:


```
l = [1, 2, 3, 4, 5, 6]
```


```
a = l[0]
b = l[1:]
print(a)
print(b)
```

    1
    [2, 3, 4, 5, 6]
    

We can even use unpacking to simplify this slightly:


```
a, b = l[0], l[1:]
print(a)
print(b)
```

    1
    [2, 3, 4, 5, 6]
    

But we can use the **\*** operator to achieve the same result:


```
a, *b = l
print(a)
print(b)
```

    1
    [2, 3, 4, 5, 6]
    

Note that the **\*** operator can only appear **once**!

Like standard unpacking, this extended unpacking will work with any iterable.

With tuples:


```
a, *b = -10, 5, 2, 100
print(a)
print(b)
```

    -10
    [5, 2, 100]
    

With strings:


```
a, *b = 'python'
print(a)
print(b)
```

    p
    ['y', 't', 'h', 'o', 'n']
    

What about extracting the first, second, last elements and *the rest*.

Again we can use slicing:


```
s = 'python'

a, b, c, d = s[0], s[1], s[2:-1], s[-1]
print(a)
print(b)
print(c)
print(d)
```

    p
    y
    tho
    n
    

But we can just as easily do it this way using unpacking:


```
a, b, *c, d = s
print(a)
print(b)
print(c)
print(d)
```

    p
    y
    ['t', 'h', 'o']
    n
    

As you can see though, **c** is a list of characters, not a string.

It that's a problem we can easily fix it this way:


```
print(c)
c = ''.join(c)
print(c)
```

    ['t', 'h', 'o']
    tho
    

We can also use unpacking on the right hand side of an assignment expression:


```
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)
```

    [1, 2, 3, 4, 5, 6]
    


```
l1 = [1, 2, 3]
s = 'ABC'
l = [*l1, *s]
print(l)
```

    [1, 2, 3, 'A', 'B', 'C']
    

This unpacking works with unordered types such as sets and dictionaries as well.

The only thing is that it may not be very useful considering there is no particular ordering, so a first or last element has no real useful meaning.


```
s = {10, -99, 3, 'd'}
```


```
for c in s:
    print(c)
```

    10
    3
    d
    -99
    

As you can see, the order of the elements when we created the set was not retained!


```
s = {10, -99, 3, 'd'}
a, b, *c = s
print(a)
print(b)
print(c)
```

    10
    3
    ['d', -99]
    

So unpacking this way is of limited use.

However consider this:


```
s = {10, -99, 3, 'd'}
*a, = s
print(a)
```

    [10, 3, 'd', -99]
    

At first blush, this doesn't look terribly exciting - we simply unpacked the set values into a list.

But this is actually quite useful in both sets and dictionaries to combine things (although to be sure, there are alternative ways to do this as well - which we'll cover later in this course)


```
s1 = {1, 2, 3}
s2 = {3, 4, 5}
```

How can we combine both these sets into a single merged set?


```
s1 + s2
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-22-1659087814e1> in <module>()
    ----> 1 s1 + s2
    

    TypeError: unsupported operand type(s) for +: 'set' and 'set'


Well, **+** doesn't work...

We could use the built-in method for unioning sets:


```
help(set)
```

    Help on class set in module builtins:
    
    class set(object)
     |  set() -> new empty set object
     |  set(iterable) -> new set object
     |  
     |  Build an unordered collection of unique elements.
     |  
     |  Methods defined here:
     |  
     |  __and__(self, value, /)
     |      Return self&value.
     |  
     |  __contains__(...)
     |      x.__contains__(y) <==> y in x.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __iand__(self, value, /)
     |      Return self&=value.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __ior__(self, value, /)
     |      Return self|=value.
     |  
     |  __isub__(self, value, /)
     |      Return self-=value.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __ixor__(self, value, /)
     |      Return self^=value.
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __or__(self, value, /)
     |      Return self|value.
     |  
     |  __rand__(self, value, /)
     |      Return value&self.
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __ror__(self, value, /)
     |      Return value|self.
     |  
     |  __rsub__(self, value, /)
     |      Return value-self.
     |  
     |  __rxor__(self, value, /)
     |      Return value^self.
     |  
     |  __sizeof__(...)
     |      S.__sizeof__() -> size of S in memory, in bytes
     |  
     |  __sub__(self, value, /)
     |      Return self-value.
     |  
     |  __xor__(self, value, /)
     |      Return self^value.
     |  
     |  add(...)
     |      Add an element to a set.
     |      
     |      This has no effect if the element is already present.
     |  
     |  clear(...)
     |      Remove all elements from this set.
     |  
     |  copy(...)
     |      Return a shallow copy of a set.
     |  
     |  difference(...)
     |      Return the difference of two or more sets as a new set.
     |      
     |      (i.e. all elements that are in this set but not the others.)
     |  
     |  difference_update(...)
     |      Remove all elements of another set from this set.
     |  
     |  discard(...)
     |      Remove an element from a set if it is a member.
     |      
     |      If the element is not a member, do nothing.
     |  
     |  intersection(...)
     |      Return the intersection of two sets as a new set.
     |      
     |      (i.e. all elements that are in both sets.)
     |  
     |  intersection_update(...)
     |      Update a set with the intersection of itself and another.
     |  
     |  isdisjoint(...)
     |      Return True if two sets have a null intersection.
     |  
     |  issubset(...)
     |      Report whether another set contains this set.
     |  
     |  issuperset(...)
     |      Report whether this set contains another set.
     |  
     |  pop(...)
     |      Remove and return an arbitrary set element.
     |      Raises KeyError if the set is empty.
     |  
     |  remove(...)
     |      Remove an element from a set; it must be a member.
     |      
     |      If the element is not a member, raise a KeyError.
     |  
     |  symmetric_difference(...)
     |      Return the symmetric difference of two sets as a new set.
     |      
     |      (i.e. all elements that are in exactly one of the sets.)
     |  
     |  symmetric_difference_update(...)
     |      Update a set with the symmetric difference of itself and another.
     |  
     |  union(...)
     |      Return the union of sets as a new set.
     |      
     |      (i.e. all elements that are in either set.)
     |  
     |  update(...)
     |      Update a set with the union of itself and others.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    
    


```
print(s1)
print(s2)
s1.union(s2)
```

    {1, 2, 3}
    {3, 4, 5}
    




    {1, 2, 3, 4, 5}



What about joining 4 different sets?


```
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}
print(s1.union(s2).union(s3).union(s4))
print(s1.union(s2, s3, s4))
```

    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    

Or we could use unpacking in this way:


```
{*s1, *s2, *s3, *s4}
```




    {1, 2, 3, 4, 5, 6, 7, 8, 9}



What we did here was to unpack each set directly into another set!

The same works for dictionaries - just remember that **\*** for dictionaries unpacks the keys only.


```
d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key3': 3}
[*d1, *d2]
```




    ['key1', 'key2', 'key2', 'key3']



So, is there anything to unpack the key-value pairs for dictionaries instead of just the keys?

Yes - we can use the **\*\*** operator:


```
d1 = {'key1': 1, 'key2': 2}
d2 = {'key2': 3, 'key3': 3}

{**d1, **d2}
```




    {'key1': 1, 'key2': 3, 'key3': 3}



Notice what happened to the value of **key2**. The value for the second occurrence of **key2** was retained (overwritten).

In fact, if we write the unpacking reversing the order of d1 and d2:


```
{**d2, **d1}
```




    {'key1': 1, 'key2': 2, 'key3': 3}



we see that the value of **key2** is now **2**, since it was the second occurrence.

Of course, we can unpack a dictionary into a dictionary as seen above, but we can mix in our own key-value pairs as well - it is just a dictionary literal after all.


```
{'a': 1, 'b': 2, **d1, **d2, 'c':3}
```




    {'a': 1, 'b': 2, 'c': 3, 'key1': 1, 'key2': 3, 'key3': 3}



Again, if we have the same keys, only the "latest" value of the key is retained:


```
{'key1': 100, **d1, **d2, 'key3': 200}
```




    {'key1': 1, 'key2': 3, 'key3': 200}



#### Nested Unpacking

Python even supports nested unpacking:


```
a, b, (c, d) = [1, 2, ['X', 'Y']]
print(a)
print(b)
print(c)
print(d)
```

    1
    2
    X
    Y
    

In fact, since a string is an iterable, we can even write:


```
a, b, (c, d) = [1, 2, 'XY']
print(a)
print(b)
print(c)
print(d)
```

    1
    2
    X
    Y
    

We can even write something like this:


```
a, b, (c, d, *e) = [1, 2, 'python']
print(a)
print(b)
print(c)
print(d)
print(e)
```

    1
    2
    p
    y
    ['t', 'h', 'o', 'n']
    

Remember when we said that we can use a * only **once**...

How about this then?


```
a, *b, (c, d, *e) = [1, 2, 3, 'python']
print(a)
print(b)
print(c)
print(d)
print(e)
```

    1
    [2, 3]
    p
    y
    ['t', 'h', 'o', 'n']
    

We can break down what happened here in multiple steps:


```
a, *b, tmp = [1, 2, 3, 'python']
print(a)
print(b)
print(tmp)
```

    1
    [2, 3]
    python
    


```
c, d, *e = tmp
print(c)
print(d)
print(e)
```

    p
    y
    ['t', 'h', 'o', 'n']
    

So putting it together we get our original line of code:


```
a, *b, (c, d, *e) = [1, 2, 3, 'python']
print(a)
print(b)
print(c)
print(d)
print(e)
```

    1
    [2, 3]
    p
    y
    ['t', 'h', 'o', 'n']
    

If we wanted to do the same thing using slicing:


```
l = [1, 2, 3, 'python']
l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
```




    (1, [2, 3], 'p', 'y', ['t', 'h', 'o', 'n'])




```
l = [1, 2, 3, 'python']
a, b, c, d, e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a)
print(b)
print(c)
print(d)
print(e)
```

    1
    [2, 3]
    p
    y
    ['t', 'h', 'o', 'n']
    

Of course, this works for arbitrary lengths and indexable sequence types:


```
l = [1, 2, 3, 4, 'unladen swallow']
a, b, c, d, e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a)
print(b)
print(c)
print(d)
print(e)
```

    1
    [2, 3, 4]
    u
    n
    ['l', 'a', 'd', 'e', 'n', ' ', 's', 'w', 'a', 'l', 'l', 'o', 'w']
    

or even:


```
l = [1, 2, 3, 4, ['a', 'b', 'c', 'd']]
a, b, c, d, e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a)
print(b)
print(c)
print(d)
print(e)
```

    1
    [2, 3, 4]
    a
    b
    ['c', 'd']
    

##  \*args

Recall from iterable unpacking:


```
a, b, *c = 10, 20, 'a', 'b'
```


```
print(a, b)
```

    10 20
    


```
print(c)
```

    ['a', 'b']
    

We can use a similar concept in function definitions to allow for arbitrary numbers of **positional** parameters/arguments:


```
def func1(a, b, *args):
    print(a)
    print(b)
    print(args)
```


```
func1(1, 2, 'a', 'b')
```

    1
    2
    ('a', 'b')
    

A few things to note:

1. Unlike iterable unpacking, **\*args** will be a **tuple**, not a list.

2. The name of the parameter **args** can be anything you prefer

3. You cannot specify positional arguments **after** the **\*args** parameter - this does something different that we'll cover in the next lecture.


```
def func1(a, b, *my_vars):
    print(a)
    print(b)
    print(my_vars)
```


```
func1(10, 20, 'a', 'b', 'c')
```

    10
    20
    ('a', 'b', 'c')
    


```
def func1(a, b, *c, d):
    print(a)
    print(b)
    print(c)
    print(d)
```


```
func1(10, 20, 'a', 'b', 100)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-18-50a3343cf093> in <module>()
    ----> 1 func1(10, 20, 'a', 'b', 100)
    

    TypeError: func1() missing 1 required keyword-only argument: 'd'


Let's see how we might use this to calculate the average of an arbitrary number of parameters.


```
def avg(*args):
    count = len(args)
    total = sum(args)
    return total/count
```


```
avg(2, 2, 4, 4)
```




    3.0



But watch what happens here:


```
avg()
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-21-867ab4243063> in <module>()
    ----> 1 avg()
    

    <ipython-input-19-03b621c670aa> in avg(*args)
          2     count = len(args)
          3     total = sum(args)
    ----> 4     return total/count
    

    ZeroDivisionError: division by zero


The problem is that we passed zero arguments.

We can fix this in one of two ways:


```
def avg(*args):
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    else:
        return total/count
```


```
avg(2, 2, 4, 4)
```




    3.0




```
avg()
```




    0



But we may not want to allow specifying zero arguments, in which case we can split our parameters into a required (non-defaulted) positional argument, and the rest:


```
def avg(a, *args):
    count = len(args) + 1
    total = a + sum(args)
    return total/count
```


```
avg(2, 2, 4, 4)
```




    3.0




```
avg()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-27-867ab4243063> in <module>()
    ----> 1 avg()
    

    TypeError: avg() missing 1 required positional argument: 'a'


As you can see, an exception occurs if we do not specify at least one argument.

#### Unpacking an iterable into positional arguments


```
def func1(a, b, c):
    print(a)
    print(b)
    print(c)
```


```
l = [10, 20, 30]
```

This will **not** work:


```
func1(l)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-30-3255f48773bf> in <module>()
    ----> 1 func1(l)
    

    TypeError: func1() missing 2 required positional arguments: 'b' and 'c'


The function expects three positional arguments, but we only supplied a single one (albeit a list).

But we could unpack the list, and **then** pass it to as the function arguments:


```
*l,
```




    (10, 20, 30)




```
func1(*l)
```

    10
    20
    30
    

What about mixing positional and keyword arguments with this?


```
def func1(a, b, c, *d):
    print(a)
    print(b)
    print(c)
    print(d)
```


```
func1(10, c=20, b=10, 'a', 'b')
```


      File "<ipython-input-34-f5236a91cb18>", line 1
        func1(10, c=20, b=10, 'a', 'b')
                             ^
    SyntaxError: positional argument follows keyword argument
    


Recall that once a keyword argument is used in a function call, we **cannot** use positional arguments after that. 

However, in the next lecture we'll look at how to address this issue.

##  Keyword Arguments

Recall: positional parameters defined in functions can also be passed as named (keyword) arguments.


```
def func1(a, b, c):
    print(a, b, c)
```


```
func1(10, 20, 30)
```

    10 20 30
    


```
func1(b=20, c=30, a=10)
```

    10 20 30
    


```
func1(10, c=30, b=20)
```

    10 20 30
    

Using a named argument is optional and up to the caller.

What if we wanted to force calls to our function to use named arguments?

We can do so by **exhausting** all the positional arguments, and then adding some additional parameters in teh function definition:


```
def func1(a, b, *args, d):
    print(a, b, args, d)
```

Now we will need at least two positional arguments, an optional (possibly even zero) number of additional arguments, and this extra argument which is supposed to go into **d**. This argument can **only** be passed to the function using a named (keyword) argument:

So, this will not work:


```
func1(10, 20, 'a', 'b', 100)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-50a3343cf093> in <module>()
    ----> 1 func1(10, 20, 'a', 'b', 100)
    

    TypeError: func1() missing 1 required keyword-only argument: 'd'


But this will:


```
func1(10, 20, 'a', 'b', d=100)
```

As you can see, **d** took the keyword argument, while the remaining arguments were handled as positional parameters.

We can even define a function that has only optional positional arguments and mandatory keyword arguments:


```
def func1(*args, d):
    print(args)
    print(d)
```


```
func1(1, 2, 3, d='hello')
```

We can of course, not pass any positional arguments:


```
func1(d='hello')
```

but the positional argument is mandatory (since no default was provided in the function definition):


```
func1()
```

To make the keyword argument optional, we just need to specify a default value in the function definition:


```
def func1(*args, d='n/a'):
    print(args)
    print(d)
```


```
func1(1, 2, 3)
```


```
func1()
```

Sometimes we want **only** keyword arguments, in which case we still have to exhaust the positional arguments first - but we can use the following syntax if we do not want any positional parameters passed in:


```
def func1(*, d='hello'):
    print(d)
```


```
func1(10, d='bye')
```


```
func1(d='bye')
```

Of course, if we do not provide a default value for the keyword argument, then we effectively are forcing the caller to provide the keyword argument:


```
def func1(*, a, b):
    print(a)
    print(b)
```


```
func1(a=10, b=20)
```

but, the following would not work:


```
func1(10, 20)
```

Unlike positional parameters, keyword arguments do not have to be defined with non-defaulted and then defaulted arguments:


```
def func1(a, *, b='hello', c):
    print(a, b, c)
```


```
func1(5, c='bye')
```

We can also include positional non-defaulted (first), positional defaulted (after positional non-defaulted) followed lastly (after exhausting positional arguments) by keyword args (defaulted or non-defaulted in any order)


```
def func1(a, b=20, *args, d=0, e='n/a'):
    print(a, b, args, d, e)
```


```
func1(5, 4, 3, 2, 1, d=0, e='all engines running')
```


```
func1(0, 600, d='goooood morning', e='python!')
```


```
func1(11, 'm/s', 24, 'mph', d='unladen', e='swallow')
```

As you can see, defining parameters and passing arguments is extremely flexible in Python! Even more so, when you account for the fact that the parameters are not statically typed!

In the next video, we'll look at one more thing we can do with function parameters!

##  **kwargs


```
def func(**kwargs):
    print(kwargs)
```


```
func(x=100, y=200)
```

    {'x': 100, 'y': 200}
    

We can also use it in conjunction with **\*args**: 


```
def func(*args, **kwargs):
    print(args)
    print(kwargs)
```


```
func(1, 2, a=100, b=200)
```

    (1, 2)
    {'a': 100, 'b': 200}
    

Note: You cannot do the following:


```
def func(*, **kwargs):
    print(kwargs)
```


      File "<ipython-input-9-330c63b7f22e>", line 1
        def func(*, **kwargs):
                   ^
    SyntaxError: named arguments must follow bare *
    


There is no need to even do this, since **\*\*kwargs** essentially indicates no more positional arguments.


```
def func(a, b, **kwargs):
    print(a)
    print(b)
    print(kwargs)
```


```
func(1, 2, x=100, y=200)
```

    1
    2
    {'x': 100, 'y': 200}
    

Also, you cannot specify parameters **after** **\*\*kwargs** has been used:


```
def func(a, b, **kwargs, c):
    pass
```


      File "<ipython-input-12-ffdc3153243b>", line 1
        def func(a, b, **kwargs, c):
                                 ^
    SyntaxError: invalid syntax
    


If you want to specify both specific keyword-only arguments and **\*\*kwargs** you will need to first get to a point where you can define a keyword-only argument (i.e. exhaust the positional arguments, using either **\*args** or just **\***)


```
def func(*, d, **kwargs):
    print(d)
    print(kwargs)
```


```
func(d=1, x=100, y=200)
```

    1
    {'x': 100, 'y': 200}
    

##  Putting it all Together

Positionals Only: no extra positionals, no defaults (all positionals required)


```
def func(a, b):
    print(a, b)
```


```
func('hello', 'world')
```

    hello world
    


```
func(b='world', a='hello')
```

    hello world
    

Positionals Only: no extra positionals, defaults (some positionals optional)


```
def func(a, b='world', c=10):
    print(a, b, c)
```


```
func('hello')
```

    hello world 10
    


```
func('hello', c='!')
```

    hello world !
    

Positionals Only: extra positionals, no defaults (all positionals required)


```
def func(a, b, *args):
    print(a, b, args)
```


```
func(1, 2, 'x', 'y', 'z')
```

    1 2 ('x', 'y', 'z')
    

Note that we cannot call the function this way:


```
func(b=2, a=1, 'x', 'y', 'z')
```


      File "<ipython-input-9-f1b0ffb3b67d>", line 1
        func(b=2, a=1, 'x', 'y', 'z')
                      ^
    SyntaxError: positional argument follows keyword argument
    


Keywords Only: no positionals, no defaults (all keyword args required)


```
def func(*, a, b):
    print(a, b)
```


```
func(a=1, b=2)
```

    1 2
    

Keywords Only: no positionals, some defaults (not all keyword args required)


```
def func(*, a=1, b):
    print(a, b)
```


```
func(a=10, b=20)
```

    10 20
    


```
func(b=2)
```

    1 2
    

Keywords and Positionals: some positionals (no defaults), keywords (no defaults)


```
def func(a, b, *, c, d):
    print(a, b, c, d)
```


```
func(1, 2, c=3, d=4)
```

    1 2 3 4
    


```
func(1, 2, d=4, c=3)
```

    1 2 3 4
    


```
func(1, c=3, d=4, b=2)
```

    1 2 3 4
    

Keywords and Positionals: some positional defaults


```
def func(a, b=2, *, c, d=4):
    print(a, b, c, d)
```


```
func(1, c=3)
```

    1 2 3 4
    


```
func(c=3, a=1)
```

    1 2 3 4
    


```
func(1, 2, c=3, d=4)
```

    1 2 3 4
    


```
func(c=3, a=1, b=2, d=4)
```

    1 2 3 4
    

Keywords and Positionals: extra positionals


```
def func(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)
```


```
func(1, 2, 'x', 'y', 'z', c=3, d=4)
```

    1 2 ('x', 'y', 'z') 3 4
    

Note that if we are going to use the extra arguments, then we cannot actually use a default value for b:


```
func(1, 'x', 'y', 'z', c=3, d=4)
```

    1 x ('y', 'z') 3 4
    

as you can see, **b** was assigned the value **x**

Keywords and Positionals: no extra positionals, extra keywords


```
def func(a, b, *, c, d=4, **kwargs):
    print(a, b, c, d, kwargs)
```


```
func(1, 2, c=3, x=100, y=200, z=300)
```

    1 2 3 4 {'x': 100, 'y': 200, 'z': 300}
    


```
func(x=100, y=200, z=300, c=3, b=2, a=1)
```

    1 2 3 4 {'x': 100, 'y': 200, 'z': 300}
    

Keywords and Positionals: extra positionals, extra keywords


```
def func(a, b, *args, c, d=4, **kwargs):
    print(a, b, args, c, d, kwargs)
```


```
func(1, 2, 'x', 'y', 'z', c=3, d=5, x=100, y=200, z=300)
```

    1 2 ('x', 'y', 'z') 3 5 {'x': 100, 'y': 200, 'z': 300}
    

Keywords and Positionals: only extra positionals and extra keywords


```
def func(*args, **kwargs):
    print(args, kwargs)
```


```
func(1, 2, 3, x=100, y=200, z=300)
```

    (1, 2, 3) {'x': 100, 'y': 200, 'z': 300}
    

#### The Print Function


```
help(print)
```

    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    
    


```
print(1, 2, 3)
```

    1 2 3
    


```
print(1, 2, 3, sep='--')
```

    1--2--3
    


```
print(1, 2, 3, end='***\n')
```

    1 2 3***
    


```
print(1, 2, 3, sep='\t', end='\t***\t')
print(4, 5, 6, sep='\t', end='\t***\n')
```

    1	2	3	***	4	5	6	***
    

#### Another Use Case


```
def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = int(bool(args)) and min(args)
    avg = (hi + lo)/2
    if log_to_console:
        print("high={0}, low={1}, avg={2}".format(hi, lo, avg))
    return avg
```


```
avg = calc_hi_lo_avg(1, 2, 3, 4, 5)
print(avg)
```

    3.0
    


```
avg = calc_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=True)
print(avg)
```

    high=5, low=1, avg=3.0
    3.0
    

##  A Simple Function Timer

We want to create a simple function that can time how fast a function runs.

We want this function to be generic in the sense that it can be used to time any function (along with it's positional and keyword arguments), as well as specifying the number of the times the function should be timed, and the returns the average of the timings.

We'll call our function **time_it**, and it will need to have the following parameters:

* the function we want to time
* the positional arguments of the function we want to time (if any)
* the keyword-only arguments of the function we want to time (if any)
* the number of times we want to run this function


```
import time
```


```
def time_it(fn, *args, rep=5, **kwargs):
    print(args, rep, kwargs)
```

Now we could the function this way:


```
time_it(print, 1, 2, 3, sep='-')
```

    (1, 2, 3) 5 {'sep': '-'}
    

Let's modify our function to actually run the print function with any positional and keyword args (except for rep) passed to it:


```
def time_it(fn, *args, rep=5, **kwargs):
    for i in range(rep):
        fn(*args, **kwargs)
```


```
time_it(print, 1, 2, 3, sep='-')
```

    1-2-3
    1-2-3
    1-2-3
    1-2-3
    1-2-3
    

As you can see **1, 2, 3** was passed to the **print** function's positional parameters, and the keyword_only arg **sep** was also passed to it. 

We can even add more arguments:


```
time_it(print, 1, 2, 3, sep='-', end=' *** ', rep=3)
```

    1-2-3 *** 1-2-3 *** 1-2-3 *** 

Now all that's really left for us to do is to time the function and return the average time:


```
def time_it(fn, *args, rep=5, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep
```

Let's write a few functions we might want to time:

We'll create three functions that all do the same thing: calculate powers of n**k for k in some range of integer values


```
def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results
```


```
def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]
```


```
def compute_powers_3(n, *, start=1, end):
    # using a generator expression
    return (n**i for i in range(start, end))
```

Let's run these functions and see the results:


```
compute_powers_1(2, end=5)
```




    [2, 4, 8, 16]




```
compute_powers_2(2, end=5)
```




    [2, 4, 8, 16]




```
list(compute_powers_3(2, end=5))
```




    [2, 4, 8, 16]



Finally let's run these functions through our **time_it** function and see the results:


```
time_it(compute_powers_1, n=2, end=20000, rep=4)
```




    2.5798198230283234




```
time_it(compute_powers_2, 2, end=20000, rep=4)
```




    2.3151767636341347




```
time_it(compute_powers_3, 2, end=20000, rep=4)
```




    3.0854032573301993e-06



Although the **compute_powers_3** function appears to be **much** faster than the other two, it doesn't quite do the same thing! 

We'll cover generators in detail later in this course.

##  Default Values - Beware!


```
from datetime import datetime
```


```
print(datetime.utcnow())
```

    2017-08-22 04:04:17.700303
    


```
def log(msg, *, dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt, msg))
```


```
log('message 1')
```

    2017-08-22 04:04:18.406943: message 1
    


```
log('message 2', dt='2001-01-01 00:00:00')
```

    2001-01-01 00:00:00: message 2
    


```
log('message 3')
```

    2017-08-22 04:04:18.406943: message 3
    


```
log('message 4')
```

    2017-08-22 04:04:18.406943: message 4
    

As you can see, the default for **dt** is calculated when the function is **defined** and is **NOT** re-evaluated when the function is called.

#### Solution Pattern

Here is one pattern we can use to achieve the desired result:

We actually set the default to None - this makes the argument optional, and we can then test for None **inside** the function and default to the current time if it is None.


```
def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    # above is equivalent to:
    #if not dt:
    #    dt = datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))    
```


```
log('message 1')
```

    2017-08-22 04:15:11.797640: message 1
    


```
log('message 2')
```

    2017-08-22 04:15:14.529496: message 2
    


```
log('message 3', dt='2001-01-01 00:00:00')
```

    2001-01-01 00:00:00: message 3
    


```
log('message 4')
```

    2017-08-22 04:15:18.045607: message 4
    

##  Parameter Defaults - Beware 2

Another gotcha with parameter defaults comes with mutable types, and is an easy trap to fall into.

Again, you have to remember that function parameter defaults are evaluated once, when the function is defined (i.e. when the module is loaded, or in this Jupyter notebook, when we "execute" the function definition), and not every time the function is called.

Consider the following scenario.

We are creating a grocery list, and we want our list to contain consistently formatted data with name, quantity and measurement unit:

``
bananas (2 units)
grapes (1 bunch)
milk (1 liter)
python (1 medium-rare)
``

To make sure the data is consistent, we want to use a function that we can call to add the item to our list.

So we'll need to provide it our current grocery list as well as the item information to be added:


```
def add_item(name, quantity, unit, grocery_list):
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list
```

We have two stores we want to visit, so we set up two grocery lists:


```
store_1 = []
store_2 = []
```


```
add_item('bananas', 2, 'units', store_1)
add_item('grapes', 1, 'bunch', store_1)
add_item('python', 1, 'medium-rare', store_2)
```




    ['python (1 medium-rare)']




```
store_1
```




    ['bananas (2 units)', 'grapes (1 bunch)']




```
store_2
```




    ['python (1 medium-rare)']



Ok, working great. But let's make the function a little easier to use - if the user does not supply an existing grocery list to append the item to, let's just go ahead and default our `grocery_list` to an empty list hence starting a new shopping list:


```
def add_item(name, quantity, unit, grocery_list=[]):
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list
```


```
store_1 = add_item('bananas', 2, 'units')
add_item('grapes', 1, 'bunch', store_1)
```




    ['bananas (2 units)', 'grapes (1 bunch)']




```
store_1
```




    ['bananas (2 units)', 'grapes (1 bunch)']



OK, so that seems to be working as expected.

Let's start our second list:


```
store_2 = add_item('milk', 1, 'gallon')
```


```
print(store_2)
```

    ['bananas (2 units)', 'grapes (1 bunch)', 'milk (1 gallon)']
    

??? What's going on? Our second list somehow contains the items that are in the first list.

What happened is that the returned value in the first call we made was the default grocery list - but remember that the list was created once and for all when the function was **created** not called. So everytime we call the function, that is the **same** list being used as the default. 

When we started out first list, we were adding item to that default list.

When we started our second list, we were adding items to the **same** default list (since it is the same object).

We can avoid this problem using the same pattern as in the previous example we had with the default date time value. We use None as a default value instead, and generate a new empty list (hence starting a new list) if none was provided.


```
def add_item(name, quantity, unit, grocery_list=None):
    if not grocery_list:
        grocery_list = []
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list
```


```
store_1 = add_item('bananas', 2, 'units')
add_item('grapes', 1, 'bunch', store_1)
```




    ['bananas (2 units)', 'grapes (1 bunch)']




```
store_2 = add_item('milk', 1, 'gallon')
store_2
```




    ['milk (1 gallon)']



Issue resolved!

However, there are legitimate use cases (well, almost legitimate, often we're better off using a different approach that we'll see when we look at closures), but here's a simple one.

We want our function to cache results, so that we don't recalculate something more than once.

Let's say we have a factorial function, that can be defined recursively as:

`n! = n * (n-1)!`


```
def factorial(n):
    if n < 1:
        return 1
    else:
        print('calculating {0}!'.format(n))
        return n * factorial(n-1)
```


```
factorial(3)
```

    calculating 3!
    calculating 2!
    calculating 1!
    




    6




```
factorial(3)
```

    calculating 3!
    calculating 2!
    calculating 1!
    




    6



As you can see we had to recalculate all those factorials the second time around.

Let's cache the results leveraging what we saw in the previous example:


```
def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n-1)
        cache[n] = result
        return result
```


```
factorial(3)
```

    calculating 3!
    calculating 2!
    calculating 1!
    




    6




```
factorial(3)
```




    6



Now as you can see, the second time around we did not have to recalculate all the factorials. In fact, to calculate higher factorials, you'll notice that we don't need to re-run *all* the recursive calls:


```
factorial(5)
```

    calculating 5!
    calculating 4!
    




    120



`5!` and `4!` was calculated since they weren't cached, but since `3!` was already cached we didn't have to recalculate it - it was a quick lookup instead.

This technique is something called memoization, and we'll come back to it in much more detail when we discuss closures and decorators.

# Section 06 - First-Class Functions

##  Docstrings and Annotations

#### Docstrings

When we call **help()** on a class, function, module, etc, Python will typically display some information:


```
help(print)
```

    Help on built-in function print in module builtins:
    
    print(...)
        print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
        
        Prints the values to a stream, or to sys.stdout by default.
        Optional keyword arguments:
        file:  a file-like object (stream); defaults to the current sys.stdout.
        sep:   string inserted between values, default a space.
        end:   string appended after the last value, default a newline.
        flush: whether to forcibly flush the stream.
    
    

We can define such help using docstrings and annotations.


```
def my_func(a, b):
    return a*b
```


```
help(my_func)
```

    Help on function my_func in module __main__:
    
    my_func(a, b)
    
    

Pretty bare! So let's add some additional help:


```
def my_func(a, b):
    'Returns the product of a and b'
    return a*b
```


```
help(my_func)
```

    Help on function my_func in module __main__:
    
    my_func(a, b)
        Returns the product of a and b
    
    

Docstrings can span multiple lines using a multi-line string literal:


```
def fact(n):
    '''Calculates n! (factorial function)
    
    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''
    
    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n-1)
    
    
```


```
help(fact)
```

    Help on function fact in module __main__:
    
    fact(n)
        Calculates n! (factorial function)
        
        Inputs:
            n: non-negative integer
        Returns:
            the factorial of n
    
    

Docstrings, when found, are simply attached to the function in the `__doc__` property:


```
fact.__doc__
```




    'Calculates n! (factorial function)\n    \n    Inputs:\n        n: non-negative integer\n    Returns:\n        the factorial of n\n    '



And the Python **help()** function simply returns the contents of `__doc__`

#### Annotations

We can also add metadata annotations to a function's parameters and return. These metadata annotations can be any **expression** (string, type, function call, etc)


```
def my_func(a:'annotation for a', 
            b:'annotation for b')->'annotation for return':
    
    return a*b
```


```
help(my_func)
```

    Help on function my_func in module __main__:
    
    my_func(a:'annotation for a', b:'annotation for b') -> 'annotation for return'
    
    

The annotations can be any expression, not just strings:


```
x = 3
y = 5
def my_func(a: str) -> 'a repeated ' + str(max(3, 5)) + ' times':
	return a*max(x, y)
```


```
help(my_func)
```

    Help on function my_func in module __main__:
    
    my_func(a:str) -> 'a repeated 5 times'
    
    

Note that these annotations do **not** force a type on the parameters or the return value - they are simply there for documentation purposes within Python and **may** be used by external applications and modules, such as IDE's.

Just like docstrings are stored in the `__doc__` property, annotations are stored in the `__annotations__` property - a dictionary whose keys are the parameter names, and values are the annotation.


```
my_func.__annotations__
```




    {'a': str, 'return': 'a repeated 5 times'}



Of course we can combine both docstrings and annotations:


```
def fact(n: 'int >= 0')->int:
    '''Calculates n! (factorial function)
    
    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''
    
    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n-1)
```


```
help(fact)
```

    Help on function fact in module __main__:
    
    fact(n:'int >= 0') -> int
        Calculates n! (factorial function)
        
        Inputs:
            n: non-negative integer
        Returns:
            the factorial of n
    
    

Annotations will work with default parameters too: just specify the default **after** the annotation:


```
def my_func(a:str='a', b:int=1)->str:
    return a*b
```


```
help(my_func)
```

    Help on function my_func in module __main__:
    
    my_func(a:str='a', b:int=1) -> str
    
    


```
my_func()
```




    'a'




```
my_func('abc', 3)
```




    'abcabcabc'




```
def my_func(a:int=0, *args:'additional args'):
    print(a, args)
```


```
my_func.__annotations__
```




    {'a': int, 'args': 'additional args'}




```
help(my_func)
```

    Help on function my_func in module __main__:
    
    my_func(a:int=0, *args:'additional args')
    
    

##  Lambda Expressions


```
lambda x: x**2
```




    <function __main__.<lambda>>



As you can see, the above expression just created a function.

#### Assigning to a Variable


```
func = lambda x: x**2
```


```
type(func)
```




    function




```
func(3)
```




    9



We can specify arguments for lambdas just like we would for any function created using **def**, except for annotations:


```
func_1 = lambda x, y=10: (x, y)
```


```
func_1(1, 2)
```




    (1, 2)




```
func_1(1)
```




    (1, 10)



We can even use \* and \*\*:


```
func_2 = lambda x, *args, y, **kwargs: (x, *args, y, {**kwargs})
```


```
func_2(1, 'a', 'b', y=100, a=10, b=20)
```




    (1, 'a', 'b', 100, {'a': 10, 'b': 20})



#### Passing as an Argument

Lambdas are functions, and can therefore be passed to any other function as an argument (or returned from another function)


```
def apply_func(x, fn):
    return fn(x)
```


```
apply_func(3, lambda x: x**2)
```




    9




```
apply_func(3, lambda x: x**3)
```




    27



Of course we can make this even more generic:


```
def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)
```


```
apply_func(lambda x, y: x+y, 1, 2)
```




    3




```
apply_func(lambda x, *, y: x+y, 1, y=2)
```




    3




```
apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5)
```




    15



Of course in the example above, we really did not need to create a lambda!


```
apply_func(sum, (1, 2, 3, 4, 5))
```




    15



Of course, we don't have to use lambdas when calling **apply_func**, we can also pass in a function defined using a **def** statement:


```
def multiply(x, y):
    return x * y
```


```
apply_func(multiply, 'a', 5)
```




    'aaaaa'




```
apply_func(lambda x, y: x*y, 'a', 5)
```




    'aaaaa'



##  Lambdas and Sorting

Python has a built-in **sorted** method that can be used to sort any iterable. It will use the default ordering of the particular items, but sometimes you may want to (or need to) specify a different criteria for sorting.

Let's start with a simple list:


```
l = ['a', 'B', 'c', 'D']
```


```
sorted(l)
```




    ['B', 'D', 'a', 'c']



As you can see there is a difference between upper and lower-case characters when sorting strings.

What if we wanted to make a case-insensitive sort?

Python's **sorted** function has a keyword-only argument that allows us to modify the values that are used to sort the list.


```
sorted(l, key=str.upper)
```




    ['a', 'B', 'c', 'D']



We could have used a lambda here (but you should not, this is just to illustrate using a lambda in this case):


```
sorted(l, key = lambda s: s.upper())
```




    ['a', 'B', 'c', 'D']



Let's look at how we might create a sorted list from a dictionary:


```
d = {'def': 300, 'abc': 200, 'ghi': 100}
```


```
d
```




    {'abc': 200, 'def': 300, 'ghi': 100}




```
sorted(d)
```




    ['abc', 'def', 'ghi']



What happened here? 

Remember that iterating dictionaries actually iterates the keys - so we ended up with tyhe keys sorted alphabetically.

What if we want to return the keys sorted by their associated value instead?


```
sorted(d, key=lambda k: d[k])
```




    ['ghi', 'abc', 'def']



Maybe we want to sort complex numbers based on their distance from the origin:


```
def dist(x):
    return (x.real)**2 + (x.imag)**2
```


```
l = [3+3j, 1+1j, 0]
```

Trying to sort this list directly won't work since Python does not have an ordering defined for complex numbers:


```
sorted(l)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-11-5ed0ddfda5a6> in <module>()
    ----> 1 sorted(l)
    

    TypeError: '<' not supported between instances of 'complex' and 'complex'


Instead, let's try to specify the key using the distance:


```
sorted(l, key=dist)
```




    [0, (1+1j), (3+3j)]



Of course, if we're only going to use the **dist** function once, we can just do the same thing this way:


```
sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2)
```




    [0, (1+1j), (3+3j)]



And here's another example where we want to sort a list of strings based on the **last character** of the string:


```
l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']
```


```
sorted(l)
```




    ['Chapman', 'Cleese', 'Gilliam', 'Idle', 'Jones', 'Palin']




```
sorted(l, key=lambda s: s[-1])
```




    ['Cleese', 'Idle', 'Gilliam', 'Palin', 'Chapman', 'Jones']



##  Challenge: Randomizing an Iterable using Sorted


```
import random
```


```
help(random.random)
```

    Help on built-in function random:
    
    random(...) method of random.Random instance
        random() -> x in the interval [0, 1).
    
    


```
random.random()
```




    0.8655691916467607




```
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```


```
sorted(l, key=lambda x: random.random())
```




    [5, 7, 2, 1, 3, 10, 9, 6, 8, 4]



Of course, this works for any iterable:


```
sorted('abcdefg', key = lambda x: random.random())
```




    ['b', 'd', 'g', 'e', 'a', 'c', 'f']



And to get a string back instead of just a list:


```
''.join(sorted('abcdefg', key = lambda x: random.random()))
```




    'adfegbc'



##  Function Introspection


```
def fact(n: "some non-negative integer") -> "n! or 0 if n < 0":
    """Calculates the factorial of a non-negative integer n
    
    If n is negative, returns 0.
    """
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return n * fact(n-1)
```

Since functions are objects, we can add attributes to a function:


```
fact.short_description = "factorial function"
```


```
print(fact.short_description)
```

    factorial function
    

We can see all the attributes that belong to a function using the **dir** function:


```
dir(fact)
```




    ['__annotations__',
     '__call__',
     '__class__',
     '__closure__',
     '__code__',
     '__defaults__',
     '__delattr__',
     '__dict__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__get__',
     '__getattribute__',
     '__globals__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__kwdefaults__',
     '__le__',
     '__lt__',
     '__module__',
     '__name__',
     '__ne__',
     '__new__',
     '__qualname__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'short_description']



We can see our **short_description** attribute, as well as some attributes we have seen before: **__annotations__** and **__doc__**:


```
fact.__doc__
```




    'Calculates the factorial of a non-negative integer n\n    \n    If n is negative, returns 0.\n    '




```
fact.__annotations__
```




    {'n': 'some non-negative integer', 'return': 'n! or 0 if n < 0'}



We'll revisit some of these attributes later in this course, but let's take a look at a few here:


```
def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass
```

Let's assign my_func to another variable:


```
f = my_func
```

The **__name__** attribute holds the function's name:


```
my_func.__name__
```




    'my_func'




```
f.__name__
```




    'my_func'



The **__defaults__** attribute is a tuple containing any positional parameter defaults:


```
my_func.__defaults__
```




    (2, 3)




```
my_func.__kwdefaults__
```




    {'kw2': 2}



Let's create a function with some local variables:


```
def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b
```


```
my_func('a', 100)
```




    'aaaaaaaaaa'



The **__code__** attribute contains a **code** object:


```
my_func.__code__
```




    <code object my_func at 0x0000016640E71300, file "<ipython-input-13-785cf1a800f4>", line 1>



This **code** object itself has various properties:


```
dir(my_func.__code__)
```




    ['__class__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'co_argcount',
     'co_cellvars',
     'co_code',
     'co_consts',
     'co_filename',
     'co_firstlineno',
     'co_flags',
     'co_freevars',
     'co_kwonlyargcount',
     'co_lnotab',
     'co_name',
     'co_names',
     'co_nlocals',
     'co_stacksize',
     'co_varnames']



Attribute **__co_varnames__** is a tuple containing the parameter names and local variables:


```
my_func.__code__.co_varnames
```




    ('a', 'b', 'args', 'kwargs', 'i')



Attribute **co_argcount** returns the number of arguments (minus any \* and \*\* args)


```
my_func.__code__.co_argcount
```




    2



#### The **inspect** module

It is much easier to use the **inspect** module!


```
import inspect
```


```
inspect.isfunction(my_func)
```




    True



By the way, there is a difference between a function and a method! A method is a function that is bound to some object:


```
inspect.ismethod(my_func)
```




    False




```
class MyClass:
    def f_instance(self):
        pass
    
    @classmethod
    def f_class(cls):
        pass
    
    @staticmethod
    def f_static():
        pass
```

**Instance methods** are bound to the **instance** of a class (not the class itself)

**Class methods** are bound to the **class**, not instances

**Static methods** are no bound either to the class or its instances


```
inspect.isfunction(MyClass.f_instance), inspect.ismethod(MyClass.f_instance)
```




    (True, False)




```
inspect.isfunction(MyClass.f_class), inspect.ismethod(MyClass.f_class)
```




    (False, True)




```
inspect.isfunction(MyClass.f_static), inspect.ismethod(MyClass.f_static)
```




    (True, False)




```
my_obj = MyClass()
```


```
inspect.isfunction(my_obj.f_instance), inspect.ismethod(my_obj.f_instance)
```




    (False, True)




```
inspect.isfunction(my_obj.f_class), inspect.ismethod(my_obj.f_class)
```




    (False, True)




```
inspect.isfunction(my_obj.f_static), inspect.ismethod(my_obj.f_static)
```




    (True, False)



If you just want to know if something is a function or method:


```
inspect.isroutine(my_func)
```




    True




```
inspect.isroutine(MyClass.f_instance)
```




    True




```
inspect.isroutine(my_obj.f_class)
```




    True




```
inspect.isroutine(my_obj.f_static)
```




    True



We'll revisit this in more detail in section on OOP.

#### Introspecting Callable Code

We can get back the source code of our function using the **getsource()** method:


```
inspect.getsource(fact)
```




    'def fact(n: "some non-negative integer") -> "n! or 0 if n < 0":\n    """Calculates the factorial of a non-negative integer n\n    \n    If n is negative, returns 0.\n    """\n    if n <= 1:\n        return 1\n    else:\n        return n * fact(n-1)\n'




```
print(inspect.getsource(fact))
```

    def fact(n: "some non-negative integer") -> "n! or 0 if n < 0":
        """Calculates the factorial of a non-negative integer n
        
        If n is negative, returns 0.
        """
        if n <= 1:
            return 1
        else:
            return n * fact(n-1)
    
    


```
inspect.getsource(MyClass.f_instance)
```




    '    def f_instance(self):\n        pass\n'




```
inspect.getsource(my_obj.f_instance)
```




    '    def f_instance(self):\n        pass\n'



We can also find out where the function was defined:


```
inspect.getmodule(fact)
```




    <module '__main__'>




```
inspect.getmodule(print)
```




    <module 'builtins' (built-in)>




```
import math
```


```
inspect.getmodule(math.sin)
```




    <module 'math' (built-in)>




```
# setting up variable
i = 10

# comment line 1
# comment line 2
def my_func(a, b=1):
    # comment inside my_func
    pass
```


```
inspect.getcomments(my_func)
```




    '# comment line 1\n# comment line 2\n'




```
print(inspect.getcomments(my_func))
```

    # comment line 1
    # comment line 2
    
    

#### Introspecting Callable Signatures


```
# TODO: Provide implementation
def my_func(a: 'a string', 
            b: int = 1, 
            *args: 'additional positional args', 
            kw1: 'first keyword-only arg', 
            kw2: 'second keyword-only arg' = 10,
            **kwargs: 'additional keyword-only args') -> str:
    """does something
       or other"""
    pass
```


```
inspect.signature(my_func)
```




    <Signature (a:'a string', b:int=1, *args:'additional positional args', kw1:'first keyword-only arg', kw2:'second keyword-only arg'=10, **kwargs:'additional keyword-only args') -> str>




```
type(inspect.signature(my_func))
```




    inspect.Signature




```
sig = inspect.signature(my_func)
```


```
dir(sig)
```




    ['__class__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__le__',
     '__lt__',
     '__module__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__setstate__',
     '__sizeof__',
     '__slots__',
     '__str__',
     '__subclasshook__',
     '_bind',
     '_bound_arguments_cls',
     '_hash_basis',
     '_parameter_cls',
     '_parameters',
     '_return_annotation',
     'bind',
     'bind_partial',
     'empty',
     'from_builtin',
     'from_callable',
     'from_function',
     'parameters',
     'replace',
     'return_annotation']




```
for param_name, param in sig.parameters.items():
    print(param_name, param)
```

    a a:'a string'
    b b:int=1
    args *args:'additional positional args'
    kw1 kw1:'first keyword-only arg'
    kw2 kw2:'second keyword-only arg'=10
    kwargs **kwargs:'additional keyword-only args'
    


```
def print_info(f: "callable") -> None:
    print(f.__name__)
    print('=' * len(f.__name__), end='\n\n')
    
    print('{0}\n{1}\n'.format(inspect.getcomments(f), 
                              inspect.cleandoc(f.__doc__)))
    
    print('{0}\n{1}'.format('Inputs', '-'*len('Inputs')))
    
    sig = inspect.signature(f)
    for param in sig.parameters.values():
        print('Name:', param.name)
        print('Default:', param.default)
        print('Annotation:', param.annotation)
        print('Kind:', param.kind)
        print('--------------------------\n')
        
    print('{0}\n{1}'.format('\n\nOutput', '-'*len('Output')))
    print(sig.return_annotation)
```


```
print_info(my_func)
```

    my_func
    =======
    
    # TODO: Provide implementation
    
    does something
    or other
    
    Inputs
    ------
    Name: a
    Default: <class 'inspect._empty'>
    Annotation: a string
    Kind: POSITIONAL_OR_KEYWORD
    --------------------------
    
    Name: b
    Default: 1
    Annotation: <class 'int'>
    Kind: POSITIONAL_OR_KEYWORD
    --------------------------
    
    Name: args
    Default: <class 'inspect._empty'>
    Annotation: additional positional args
    Kind: VAR_POSITIONAL
    --------------------------
    
    Name: kw1
    Default: <class 'inspect._empty'>
    Annotation: first keyword-only arg
    Kind: KEYWORD_ONLY
    --------------------------
    
    Name: kw2
    Default: 10
    Annotation: second keyword-only arg
    Kind: KEYWORD_ONLY
    --------------------------
    
    Name: kwargs
    Default: <class 'inspect._empty'>
    Annotation: additional keyword-only args
    Kind: VAR_KEYWORD
    --------------------------
    
    
    
    Output
    ------
    <class 'str'>
    

#### A Side Note on Positional Only Arguments

Some built-in callables have arguments that are positional only (i.e. cannot be specified using a keyword).

However, Python does not currently have any syntax that allows us to define callables with positional only arguments.

In general, the documentation uses a **/** character to indicate that all preceding arguments are positional-only. But not always :-(


```
help(divmod)
```

    Help on built-in function divmod in module builtins:
    
    divmod(x, y, /)
        Return the tuple (x//y, x%y).  Invariant: div*y + mod == x.
    
    

Here we see that the **divmod** function takes two positional-only parameters:


```
divmod(10, 3)
```




    (3, 1)




```
divmod(x=10, y=3)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-55-c637b01eef33> in <module>()
    ----> 1 divmod(x=10, y=3)
    

    TypeError: divmod() takes no keyword arguments


Similarly, the string **replace** function also takes positional-only arguments, however, the documentation does not indicate this!


```
help(str.replace)
```

    Help on method_descriptor:
    
    replace(...)
        S.replace(old, new[, count]) -> str
        
        Return a copy of S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count occurrences are replaced.
    
    


```
'abcdefg'.replace('abc', 'xyz')
```




    'xyzdefg'




```
'abcdefg'.replace(old='abc', new='xyz')
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-58-9d61ac657cae> in <module>()
    ----> 1 'abcdefg'.replace(old='abc', new='xyz')
    

    TypeError: replace() takes no keyword arguments


##  Callables

A callable is an object that can be called (using the **()** operator), and always returns a value.

We can check if an object is callable by using the built-in function **callable**

##### Functions and Methods are callable


```
callable(print)
```




    True




```
callable(len)
```




    True




```
l = [1, 2, 3]
callable(l.append)
```




    True




```
s = 'abc'
callable(s.upper)
```




    True



##### Callables **always** return a value:


```
result = print('hello')
print(result)
```

    hello
    None
    


```
l = [1, 2, 3]
result = l.append(4)
print(result)
print(l)
```

    None
    [1, 2, 3, 4]
    


```
s = 'abc'
result = s.upper()
print(result)
```

    ABC
    

##### Classes are callable:


```
from decimal import Decimal
```


```
callable(Decimal)
```




    True




```
result = Decimal('10.5')
print(result)
```

    10.5
    

##### Class instances may be callable:


```
class MyClass:
    def __init__(self):
        print('initializing...')
        self.counter = 0
    
    def __call__(self, x=1):
        self.counter += x
        print(self.counter)
```


```
my_obj = MyClass()
```

    initializing...
    


```
callable(my_obj.__init__)
```




    True




```
callable(my_obj.__call__)
```




    True




```
my_obj()
```

    1
    


```
my_obj()
```

    2
    


```
my_obj(10)
```

    12
    

##  Higher-Order Functions: Map and Filter

**Definition**: A function that takes a function as an argument, and/or returns a function as its return value

For example, the **sorted** function is a higher-order function as we saw in an earlier video.

#### Map

The **map** built-in function is a higher-order function that applies a function to an iterable type object:


```
help(map)
```

    Help on class map in module builtins:
    
    class map(object)
     |  map(func, *iterables) --> map object
     |  
     |  Make an iterator that computes the function using arguments from
     |  each of the iterables.  Stops when the shortest iterable is exhausted.
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
    
    


```
def fact(n):
    return 1 if n < 2 else n * fact(n-1)
```


```
fact(3)
```




    6




```
fact(4)
```




    24




```
map(fact, [1, 2, 3, 4, 5])
```




    <map at 0x23b123a3978>



The **map** function returns a **map** object, which is an **iterable** - we can either convert that to a list or enumerate it:


```
l = list(map(fact, [1, 2, 3, 4, 5]))
print(l)
```

    [1, 2, 6, 24, 120]
    

We can also use it this way:


```
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]

f = lambda x, y: x+y

m = map(f, l1, l2)
list(m)
```




    [11, 22, 33, 44, 55]



#### Filter


```
help(filter)
```

    Help on class filter in module builtins:
    
    class filter(object)
     |  filter(function or None, iterable) --> filter object
     |  
     |  Return an iterator yielding those items of iterable for which function(item)
     |  is true. If function is None, return the items that are true.
     |  
     |  Methods defined here:
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __next__(self, /)
     |      Implement next(self).
     |  
     |  __reduce__(...)
     |      Return state information for pickling.
    
    

The **filter** function is a function that filters an iterable based on the truthyness of the elements, or the truthyness of the elements after applying a function to them. Like the **map** function, the **filter** function returns an iterable that we can view by generating a list from it, or simply enumerating in a for loop.


```
l = [0, 1, 2, 3, 4, 5, 6]
for e in filter(None, l):
    print(e)
```

    1
    2
    3
    4
    5
    6
    

Notice how **0** was eliminated from the list, since **0** is **falsy**.

We can use a function for this filtering.

Suppose we want to filter out all odd values, only retaining even values:

We could first define a function to return True if the value is even, and False otherwise:


```
def is_even(n):
    return n % 2 == 0
```


```
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(is_even, l)
print(list(result))
```

    [2, 4, 6, 8]
    

Of course, we could just use a lambda expression instead:


```
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(lambda x: x % 2 == 0, l)
print(list(result))
```

    [2, 4, 6, 8]
    

#### Alternatives to **map** and **filter** using Comprehensions

We'll cover comprehensions in much more detail later, but, for now, just be aware that we can use comprehensions instead of the **map** and **filter** functions - you decide which one you find more readable and enjoyable to write.

##### Map using a list comprehension:

* factorial example


```
l = [1, 2, 3, 4, 5]
result = [fact(i) for i in l]
print(result)
```

    [1, 2, 6, 24, 120]
    

* two iterables example

Before we do this example we need to know about the **zip** function.

The **zip** built-in function will take one or more iterables, and generate an iterable of tuples where each tuple contains one element from each iterable:


```
l1 = 1, 2, 3
l2 = 'a', 'b', 'c'
list(zip(l1, l2))
```




    [(1, 'a'), (2, 'b'), (3, 'c')]




```
l1 = 1, 2, 3
l2 = [10, 20, 30]
l3 = ('a', 'b', 'c')
list(zip(l1, l2, l3))
```




    [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]




```
l1 = [1, 2, 3]
l2 = (10, 20, 30)
l3 = 'abc'
list(zip(l1, l2, l3))
```




    [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]




```
l1 = range(100)
l2 = 'python'
list(zip(l1, l2))
```




    [(0, 'p'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]



Using the **zip** function we can now add our two lists element by element as follows:


```
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
result = [i + j for i,j in zip(l1,l2)]
print(result)
```

    [11, 22, 33, 44, 55]
    

##### Filtering using a comprehension

We can very easily filter an iterable using a comprehension as follows:


```
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [i for i in l if i % 2 == 0]
print(result)
```

    [2, 4, 6, 8]
    

As you can see, we did not even need a lambda expression!

#### Combining **map** and **filter**


```
list(filter(lambda y: y < 25, map(lambda x: x**2, range(10))))
```




    [0, 1, 4, 9, 16]



Alternatively, we can use a list comprehension to do the same thing:


```
[x**2 for x in range(10) if x**2 < 25]
```




    [0, 1, 4, 9, 16]



We will come back, in more detail, to comprehensions and generators later in this course.

##  Reducing Functions in Python

#### Maximum and Minimum

Suppose we want to find the maximum value in a list:


```
l = [5, 8, 6, 10, 9]
```

We can solve this problem using a **for** loop.

First we define a function that returns the maximum of two arguments:


```
_max = lambda a, b: a if a > b else b
```


```
def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result
```


```
max_sequence(l)
```




    10



To calculate the minimum, all we need to do is to change the function that is repeatedly applied:


```
_min = lambda a, b: a if a < b else b
```


```
def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result
```


```
print(l)
print(min_sequence(l))
```

    [5, 8, 6, 10, 9]
    5
    

In general we could write it like this:


```
def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result
```


```
_reduce(_max, l)
```




    10




```
_reduce(_min, l)
```




    5



We could even just use a lambda directly in the call to **\_reduce**:


```
_reduce(lambda a, b: a if a > b else b, l)
```




    10




```
_reduce(lambda a, b: a if a < b else b, l)
```




    5



Using the same approach, we could even add all the elements of a sequence together:


```
print(l)
```

    [5, 8, 6, 10, 9]
    


```
_reduce(lambda a, b: a + b, l)
```




    38



Python actually implements a reduce function, which is found in the **functools** module. Unlike our **\_reduce** function, it can handle any iterable, not just sequences.


```
from functools import reduce
```


```
l
```




    [5, 8, 6, 10, 9]




```
reduce(lambda a, b: a if a > b else b, l)
```




    10




```
reduce(lambda a, b: a if a < b else b, l)
```




    5




```
reduce(lambda a, b: a + b, l)
```




    38



Finding the max and min of an iterable is such a common thing that Python provides a built-in function to do just that:


```
max(l), min(l)
```




    (10, 5)



Finding the sum of all the elements in an iterable is also common enough that Python implements the **sum** function:


```
sum(l)
```




    38



#### The **any** and **all** built-ins

Python provides two additional built-in reducing functions: **any** and **all**.

The **any** function will return **True** if any element in the iterable is truthy:


```
l = [0, 1, 2]
any(l)
```




    True




```
l = [0, 0, 0]
any(l)
```




    False



On the other hand, **all** will return True if **every** element of the iterable is truthy:


```
l = [0, 1, 2]
all(l)
```




    False




```
l = [1, 2, 3]
all(l)
```




    True



We can implement these functions ourselves using **reduce** if we choose to - simply use the Boolean **or** or **and** operators as the function passed to **reduce** to implement **any** and **all** respectively.

#### any


```
l = [0, 1, 2]
reduce(lambda a, b: bool(a or b), l)
```




    True




```
l = [0, 0, 0]
reduce(lambda a, b: bool(a or b), l)
```




    False



#### all


```
l = [0, 1, 2]
reduce(lambda a, b: bool(a and b), l)
```




    False




```
l = [1, 2, 3]
reduce(lambda a, b: bool(a and b), l)
```




    True



#### Products

Sometimes we may want to find the product of every element of an iterable.

Python does not provide us a built-in method to do this, so we have to either use a procedural approach, or we can use the **reduce** function.

We start by defining a function that multiplies two arguments together:


```
def mult(a, b):
    return a * b
```

Then we can use the **reduce** function:


```
l = [2, 3, 4]
reduce(mult, l)
```




    24



Remember what this did:

    step 1: result = 2
    step 2: result = mult(result, 3) = mult(2, 3) = 6
    step 3: result = mult(result, 4) = mult(6, 4) = 24
    step 4: l exhausted, return result --> 24

Of course, we can also just use a lambda:


```
reduce(lambda a, b: a * b, l)
```




    24



#### Factorials

##### Factorials

A special case of the product we just did would be calculating the factorial of some number (**n!**):

Recall:

    n! = 1 * 2 * 3 * ... * n

In other words, we are calculating the product of a sequence containing consecutive integers from 1 to n (inclusive)

We can easily write this using a simple for loop:


```
def fact(n):
    if n <= 1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result
```


```
fact(1), fact(2), fact(3), fact(4), fact(5)
```




    (1, 2, 6, 24, 120)



We could also write this using a recursive function:


```
def fact(n):
    if n <=1:
        return 1
    else:
        return n * fact(n-1)
```


```
fact(1), fact(2), fact(3), fact(4), fact(5)
```




    (1, 2, 6, 24, 120)



Finally we can also write this using **reduce** as follows:


```
n = 5
reduce(lambda a, b: a * b, range(1, n+1))
```




    120



As you can see, the **reduce** approach, although concise, is sometimes more difficult to understand than the plain loop or recursive approach.

#### **reduce** initializer

Suppose we want to provide some sort of default when we claculate the product of the elements of an iterable if that iterable is empty:


```
l = [1, 2, 3]
reduce(lambda x, y: x*y, l)
```




    6



but if **l** is empty:


```
l = []
reduce(lambda x, y: x*y, l)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-39-09fa1e2b48dc> in <module>()
          1 l = []
    ----> 2 reduce(lambda x, y: x*y, l)
    

    TypeError: reduce() of empty sequence with no initial value


To fix this, we can provide an initializer. In this case, we will use **1** since that will not affect the result of the product, and still allow us to return a value for an empty iterable.


```
l = []
reduce(lambda x, y: x*y, l, 1)
```




    1



##  Partial Functions


```
from functools import partial
```


```
def my_func(a, b, c):
    print(a, b, c)
```


```
f = partial(my_func, 10)
```


```
f(20, 30)
```

    10 20 30
    

We could have done this using another function (or a lambda) as well:


```
def partial_func(b, c):
    return my_func(10, b, c)
```


```
partial_func(20, 30)
```

    10 20 30
    

or, using a lambda:


```
fn = lambda b, c: my_func(10, b, c)
```


```
fn(20, 30)
```

    10 20 30
    

Any of these ways is fine, but sometimes partial is just a cleaner more consise way to do it.

Also, it is quite flexible with parameters:


```
def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)
```


```
f = partial(my_func, 10, k1='a')
```


```
f(20, 30, 40, k2='b', k3='c')
```

    10 20 (30, 40) a b {'k3': 'c'}
    

We can of course do the same thing using a regular function too:


```
def f(b, *args, k2, **kwargs):
    return my_func(10, b, *args, k1='a', k2=k2, **kwargs)
```


```
f(20, 30, 40, k2='b', k3='c')
```

    10 20 (30, 40) a b {'k3': 'c'}
    

As you can see in this case, using **partial** seems a lot simpler.

Also, you are not stuck having to specify the first argument in your partial:


```
def power(base, exponent):
    return base ** exponent
```


```
power(2, 3)
```




    8




```
square = partial(power, exponent=2)
```


```
square(4)
```




    16




```
cube = partial(power, exponent=3)
```


```
cube(2)
```




    8



You can even call it this way:


```
cube(base=3)
```




    27



#### Caveat

We can certainly use variables instead of literals when creating partials, but we have to be careful.


```
def my_func(a, b, c):
    print(a, b, c)
```


```
a = 10
f = partial(my_func, a)
```


```
f(20, 30)
```

    10 20 30
    

Now let's change the value of the variable **a** and see what happens:


```
a = 100
```


```
f(20, 30)
```

    10 20 30
    

As you can see, the value for **a** is fixed once the partial has been created.

In fact, the memory address of **a** is baked in to the partial, and **a** is immutable.

If we use a mutable object, things are different:


```
a = [10, 20]
f = partial(my_func, a)
```


```
f(100, 200)
```

    [10, 20] 100 200
    


```
a.append(30)
```


```
f(100, 200)
```

    [10, 20, 30] 100 200
    

#### Use Cases

We tend to use partials in situation where we need to call a function that actually requires more parameters than we can supply.

Often this is because we are working with exiting libraries or code, and we have a special case.

For example, suppose we have points (represented as tuples), and we want to sort them based on the distance of the point from some other fixed point:


```
origin = (0, 0)
```


```
l = [(1,1), (0, 2), (-3, 2), (0,0), (10, 10)]
```


```
dist2 = lambda x, y: (x[0]-y[0])**2 + (x[1]-y[1])**2
```


```
dist2((0,0), (1,1))
```




    2




```
sorted(l, key = lambda x: dist2((0,0), x))
```




    [(0, 0), (1, 1), (0, 2), (-3, 2), (10, 10)]




```
sorted(l, key=partial(dist2, (0,0)))
```




    [(0, 0), (1, 1), (0, 2), (-3, 2), (10, 10)]



Another use case is when using **callback** functions. Usually these are used when running asynchronous operations, and you provide a callable to another callable which will be called when the first callable completes its execution.

Very often, the asynchronous callable will specify the number of variables that the callback function must have - this may not be what we want, maybe we want to add some additional info.

We'll look at asynchronous processing later in this course.

Often we can also use partial functions to make our life a bit easier.

Consider a situation where we have some generic `email()` function that can be used to notify someone when various things happen in our application. But depending on what is happening we may want to notify different people. Let's see how we may do this:


```
def sendmail(to, subject, body):
    # code to send email
    print('To:{0}, Subject:{1}, Body:{2}'.format(to, subject, body))
```

Now, we may haver different email adresses we want to send notifications to, maybe defined in a config file in our app. Here, I'll just use hardcoded variables:


```
email_admin = 'palin@python.edu'
email_devteam = 'idle@python.edu;cleese@python.edu'
```

Now when we want to send emails we would have to write things like:


```
sendmail(email_admin, 'My App Notification', 'the parrot is dead.')
sendmail(';'.join((email_admin, email_devteam)), 'My App Notification', 'the ministry is closed until further notice.')
```

    To:palin@python.edu, Subject:My App Notification, Body:the parrot is dead.
    To:palin@python.edu;idle@python.edu;cleese@python.edu, Subject:My App Notification, Body:the ministry is closed until further notice.
    

We could simply our life a little using partials this way:


```
send_admin = partial(sendmail, email_admin, 'For you eyes only')
send_dev = partial(sendmail, email_devteam, 'Dear IT:')
send_all = partial(sendmail, ';'.join((email_admin, email_devteam)), 'Loyal Subjects')
```


```
send_admin('the parrot is dead.')
send_all('the ministry is closed until further notice.')
```

    To:palin@python.edu, Subject:For you eyes only, Body:the parrot is dead.
    To:palin@python.edu;idle@python.edu;cleese@python.edu, Subject:Loyal Subjects, Body:the ministry is closed until further notice.
    

Finally, let's make this a little more complex, with a mixture of positional and keyword-only arguments:


```
def sendmail(to, subject, body, *, cc=None, bcc=email_devteam):
    # code to send email
    print('To:{0}, Subject:{1}, Body:{2}, CC:{3}, BCC:{4}'.format(to, 
                                                                  subject, 
                                                                  body, 
                                                                  cc, 
                                                                  bcc))
```


```
send_admin = partial(sendmail, email_admin, 'General Admin')
send_admin_secret = partial(sendmail, email_admin, 'For your eyes only', cc=None, bcc=None)
```


```
send_admin('and now for something completely different')
```

    To:palin@python.edu, Subject:General Admin, Body:and now for something completely different, CC:None, BCC:idle@python.edu;cleese@python.edu
    


```
send_admin_secret('the parrot is dead!')
```

    To:palin@python.edu, Subject:For your eyes only, Body:the parrot is dead!, CC:None, BCC:None
    


```
send_admin_secret('the parrot is no more!', bcc=email_devteam)
```

    To:palin@python.edu, Subject:For your eyes only, Body:the parrot is no more!, CC:None, BCC:idle@python.edu;cleese@python.edu
    


```
def pow(base, exponent):
    return base ** exponent
```


```
cube = partial(pow, exponent=3)
```


```
cube(2)
```




    8




```
cube(2, 4)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-54-725d549b8104> in <module>()
    ----> 1 cube(2, 4)
    

    TypeError: pow() got multiple values for argument 'exponent'



```
cube(2, exponent=4)
```




    16



##  The **operator** Module


```
import operator
```


```
dir(operator)
```




    ['__abs__',
     '__add__',
     '__all__',
     '__and__',
     '__builtins__',
     '__cached__',
     '__concat__',
     '__contains__',
     '__delitem__',
     '__doc__',
     '__eq__',
     '__file__',
     '__floordiv__',
     '__ge__',
     '__getitem__',
     '__gt__',
     '__iadd__',
     '__iand__',
     '__iconcat__',
     '__ifloordiv__',
     '__ilshift__',
     '__imatmul__',
     '__imod__',
     '__imul__',
     '__index__',
     '__inv__',
     '__invert__',
     '__ior__',
     '__ipow__',
     '__irshift__',
     '__isub__',
     '__itruediv__',
     '__ixor__',
     '__le__',
     '__loader__',
     '__lshift__',
     '__lt__',
     '__matmul__',
     '__mod__',
     '__mul__',
     '__name__',
     '__ne__',
     '__neg__',
     '__not__',
     '__or__',
     '__package__',
     '__pos__',
     '__pow__',
     '__rshift__',
     '__setitem__',
     '__spec__',
     '__sub__',
     '__truediv__',
     '__xor__',
     '_abs',
     'abs',
     'add',
     'and_',
     'attrgetter',
     'concat',
     'contains',
     'countOf',
     'delitem',
     'eq',
     'floordiv',
     'ge',
     'getitem',
     'gt',
     'iadd',
     'iand',
     'iconcat',
     'ifloordiv',
     'ilshift',
     'imatmul',
     'imod',
     'imul',
     'index',
     'indexOf',
     'inv',
     'invert',
     'ior',
     'ipow',
     'irshift',
     'is_',
     'is_not',
     'isub',
     'itemgetter',
     'itruediv',
     'ixor',
     'le',
     'length_hint',
     'lshift',
     'lt',
     'matmul',
     'methodcaller',
     'mod',
     'mul',
     'ne',
     'neg',
     'not_',
     'or_',
     'pos',
     'pow',
     'rshift',
     'setitem',
     'sub',
     'truediv',
     'truth',
     'xor']



#### Arithmetic Operators

A variety of arithmetic operators are implemented.


```
operator.add(1, 2)
```




    3




```
operator.mul(2, 3)
```




    6




```
operator.pow(2, 3)
```




    8




```
operator.mod(13, 2)
```




    1




```
operator.floordiv(13, 2)
```




    6




```
operator.truediv(3, 2)
```




    1.5



These would have been very handy in our previous section:


```
from functools import reduce
```


```
reduce(lambda x, y: x*y, [1, 2, 3, 4])
```




    24



Instead of defining a lambda, we could simply use **operator.mul**:


```
reduce(operator.mul, [1, 2, 3, 4])
```




    24



#### Comparison and Boolean Operators

Comparison and Boolean operators are also implemented as functions:


```
operator.lt(10, 100)
```




    True




```
operator.le(10, 10)
```




    True




```
operator.is_('abc', 'def')
```




    False



We can even get the truthyness of an object:


```
operator.truth([1,2])
```




    True




```
operator.truth([])
```




    False




```
operator.and_(True, False)
```




    False




```
operator.or_(True, False)
```




    True



#### Element and Attribute Getters and Setters

We generally select an item by index from a sequence by using **[n]**:


```
my_list = [1, 2, 3, 4]
my_list[1]
```




    2



We can do the same thing using:


```
operator.getitem(my_list, 1)
```




    2



If the sequence is mutable, we can also set or remove items:


```
my_list = [1, 2, 3, 4]
my_list[1] = 100
del my_list[3]
print(my_list)
```

    [1, 100, 3]
    


```
my_list = [1, 2, 3, 4]
operator.setitem(my_list, 1, 100)
operator.delitem(my_list, 3)
print(my_list)
```

    [1, 100, 3]
    

We can also do the same thing using the **operator** module's **itemgetter** function.

The difference is that this returns a callable:


```
f = operator.itemgetter(2)
```

Now, **f(my_list)** will return **my_list[2]**


```
f(my_list)
```




    3




```
x = 'python'
f(x)
```




    't'



Furthermore, we can pass more than one index to **itemgetter**:


```
f = operator.itemgetter(2, 3)
```


```
my_list = [1, 2, 3, 4]
f(my_list)
```




    (3, 4)




```
x = 'pytyhon'
f(x)
```




    ('t', 'y')



Similarly, **operator.attrgetter** does the same thing, but with object attributes.


```
class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        
    def test(self):
        print('test method running...')
```


```
obj = MyClass()
```


```
obj.a, obj.b, obj.c
```




    (10, 20, 30)




```
f = operator.attrgetter('a')
```


```
f(obj)
```




    10




```
my_var = 'b'
operator.attrgetter(my_var)(obj)
```




    20




```
my_var = 'c'
operator.attrgetter(my_var)(obj)
```




    30




```
f = operator.attrgetter('a', 'b', 'c')
```


```
f(obj)
```




    (10, 20, 30)



Of course, attributes can also be methods.

In this case, **attrgetter** will return the object's **test** method - a callable that can then be called using **()**:


```
f = operator.attrgetter('test')
```


```
obj_test_method = f(obj)
```


```
obj_test_method()
```

    test method running...
    

Just like lambdas, we do not need to assign them to a variable name in order to use them:


```
operator.attrgetter('a', 'b')(obj)
```




    (10, 20)




```
operator.itemgetter(2, 3)('python')
```




    ('t', 'h')



Of course, we can achieve the same thing using functions or lambdas:


```
f = lambda x: (x.a, x.b, x.c)
```


```
f(obj)
```




    (10, 20, 30)




```
f = lambda x: (x[2], x[3])
```


```
f([1, 2, 3, 4])
```




    (3, 4)




```
f('python')
```




    ('t', 'h')



##### Use Case Example: Sorting

Suppose we want to sort a list of complex numbers based on the real part of the numbers:


```
a = 2 + 5j
a.real
```




    2.0




```
l = [10+1j, 8+2j, 5+3j]
sorted(l, key=operator.attrgetter('real'))
```




    [(5+3j), (8+2j), (10+1j)]



Or if we want to sort a list of string based on the last character of the strings:


```
l = ['aaz', 'aad', 'aaa', 'aac']
sorted(l, key=operator.itemgetter(-1))
```




    ['aaa', 'aac', 'aad', 'aaz']



Or maybe we want to sort a list of tuples based on the first item of each tuple:


```
l = [(2, 3, 4), (1, 2, 3), (4, ), (3, 4)]
sorted(l, key=operator.itemgetter(0))
```




    [(1, 2, 3), (2, 3, 4), (3, 4), (4,)]



#### Slicing


```
l = [1, 2, 3, 4]
```


```
l[0:2]
```




    [1, 2]




```
l[0:2] = ['a', 'b', 'c']
print(l)
```

    ['a', 'b', 'c', 3, 4]
    


```
del l[3:5]
print(l)
```

    ['a', 'b', 'c']
    

We can do the same thing this way:


```
l = [1, 2, 3, 4]
```


```
operator.getitem(l, slice(0,2))
```




    [1, 2]




```
operator.setitem(l, slice(0,2), ['a', 'b', 'c'])
print(l)
```

    ['a', 'b', 'c', 3, 4]
    


```
operator.delitem(l, slice(3, 5))
print(l)
```

    ['a', 'b', 'c']
    

#### Calling another Callable


```
x = 'python'
x.upper()
```




    'PYTHON'




```
operator.methodcaller('upper')('python')
```




    'PYTHON'



Of course, since **upper** is just an attribute of the string object **x**, we could also have used:


```
operator.attrgetter('upper')(x)()
```




    'PYTHON'



If the callable takes in more than one parameter, they can be specified as additional arguments in **methodcaller**:


```
class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def do_something(self, c):
        print(self.a, self.b, c)
```


```
obj = MyClass()
```


```
obj.do_something(100)
```

    10 20 100
    


```
operator.methodcaller('do_something', 100)(obj)
```

    10 20 100
    


```
class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
    
    def do_something(self, *, c):
        print(self.a, self.b, c)
```


```
obj.do_something(c=100)
```

    10 20 100
    


```
operator.methodcaller('do_something', c=100)(obj)
```

    10 20 100
    

More information on the **operator** module can be found here:

https://docs.python.org/3/library/operator.html

# Section 07 - Scopes, Closures and Decorators

##  Global and Local Scopes

In Python the **global** scope refers to the **module** scope.

The scope of a variable is normally defined by **where** it is (lexically) defined in the code.


```
a = 10
```

In this case, **a** is defined inside the main module, so it is a global variable.


```
def my_func(n):
    c = n ** 2
    return c
```

In this case, **c** was defined inside the function **my_func**, so it is **local** to the function **my_func**. In this example, **n** is also **local** to **my_func**

Global variables can be accessed from any inner scope in the module, for example:


```
def my_func(n):
    print('global:', a)
    c = a ** n
    return c
```


```
my_func(2)
```

    global: 10
    




    100



As you can see, **my_func** was able to reference the global variable **a**.

But remember that the scope of a variable is determined by where it is assigned. In particular, any variable defined (i.e. assigned a value) inside a function is local to that function, even if the variable name happens to be global too!


```
def my_func(n):
    a = 2
    c = a ** 2
    return c
```


```
print(a)
print(my_func(3))
print(a)
```

    10
    4
    10
    

In order to change the value of a global variable within an inner scope, we can use the **global** keyword as follows:


```
def my_func(n):
    global a
    a = 2
    c = a ** 2
    return c
```


```
print(a)
print(my_func(3))
print(a)
```

    10
    4
    2
    

As you can see, the value of the global variable **a** was changed from within **my_func**.

In fact, we can **create** global variables from within an inner function - Python will simply create the variable and place it in the **global** scope instead of the **local scope**:


```
def my_func(n):
    global var
    var = 'hello world'
    return n ** 2
```

Now, **var** does not exist yet, since the function has not run:


```
print(var)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-10-571cba235a7f> in <module>()
    ----> 1 print(var)
    

    NameError: name 'var' is not defined


Once we call the function though, it will create that global **var**:


```
my_func(2)
```




    4




```
print(var)
```

    hello world
    

#### Beware!!

Remember that whenever you assign a value to a variable without having specified the variable as **global**, it is **local** in the current scope. **Moreover**, it does not matter **where** the assignment in the code takes place, the variable is considered local in the **entire** scope - Python determines the scope of objects at compile-time, not at run-time.

Let's see an example of this:


```
a = 10
b = 100
```


```
def my_func():
    print(a)
    print(b)
    
```


```
my_func()
```

    10
    100
    

So, this works as expected - **a** and **b** are taken from the global scope since they are referenced **before** being assigned a value in the local scope.

But now consider the following example:


```
a = 10
b = 100

def my_func():
    print(a)
    print(b)
    b = 1000
```


```
my_func()
```

    10
    


    ---------------------------------------------------------------------------

    UnboundLocalError                         Traceback (most recent call last)

    <ipython-input-17-d82eda95de40> in <module>()
    ----> 1 my_func()
    

    <ipython-input-16-a2b60f95cac1> in my_func()
          4 def my_func():
          5     print(a)
    ----> 6     print(b)
          7     b = 1000
    

    UnboundLocalError: local variable 'b' referenced before assignment


As you can see, **b** in the line ``print(b)`` is considered a **local** variable - that's because the **next** line **assigns** a value to **b** - hence **b** is scoped as local by Python for the **entire** function.

Of course, functions are also objects, and scoping applies equally to function objects too. For example, we can "mask" the built-in `print` Python function:


```
print = lambda x: 'hello {0}!'.format(x)

def my_func(name):
	return print(name)

my_func('world')

```




    'hello world!'



You may be wondering how we get our **real** ``print`` function back!


```
del print
```


```
print('hello')
```

    hello
    

Yay!!

If you have experience in some other programming languages you may be wondering if loops and other code "blocks" have their own local scope too. For example in Java, the following would not work:

``for (int i=0; i<10; i++) {
    int x = 2 * i;
}
system.out.println(x);
``

But in Python it works perfectly fine:


```
for i in range(10):
    x = 2 * i
print(x)
```

    18
    

In this case, when we assigned a value to `x`, Python put it in the global (module) scope, so we can reference it after the `for` loop has finished running.

##  Nonlocal Scopes

Functions defined inside anther function can reference variables from that enclosing scope, just like functions can reference variables from the global scope.


```
def outer_func():
    x = 'hello'
    
    def inner_func():
        print(x)
    
    inner_func()
```


```
outer_func()
```

    hello
    

In fact, any level of nesting is supported since Python just keeps looking in enclosing scopes until it finds what it needs (or fails to find it by the time it finishes looking in the built-in scope, in which case a runtime error occurrs.)


```
def outer_func():
    x = 'hello'
    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()
```


```
outer_func()
```

    hello
    

But if we **assign** a value to a variable, it is considered part of the local scope, and potentially **masks** enclsogin scope variable names:


```
def outer():
    x = 'hello'
    def inner():
        x = 'python'
    inner()
    print(x)
```


```
outer()
```

    hello
    

As you can see, **x** in **outer** was not changed.

To achieve this, we can use the **nonlocal** keyword:


```
def outer():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python'
    inner()
    print(x)
```


```
outer()
```

    python
    

Of course, this can work at any level as well:


```
def outer():
    x = 'hello'
    
    def inner1():
        def inner2():
            nonlocal x
            x = 'python'
        inner2()
    inner1()
    print(x)
```


```
outer()
```

    python
    

How far Python looks up the chain depends on the first occurrence of the variable name in an enclosing scope.

Consider the following example:


```
def outer():
    x = 'hello'
    def inner1():
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        print('inner1 (before):', x)
        inner2()
        print('inner1 (after):', x)
    inner1()
    print('outer:', x)
```


```
outer()
```

    inner1 (before): python
    inner1 (after): monty
    outer: hello
    

What happened here, is that `x` in `inner1` **masked** `x` in `outer`. But `inner2` indicated to Python that `x` was nonlocal, so the first local variable up in the enclosing scope chain Python found was the one in `inner1`, hence `x` in `inner2` is actually referencing `x` that is local to `inner1`

We can change this behavior by making the variable `x` in `inner` nonlocal as well:


```
def outer():
    x = 'hello'
    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        print('inner1 (before):', x)
        inner2()
        print('inner1 (after):', x)
    inner1()
    print('outer:', x)
```


```
outer()
```

    inner1 (before): python
    inner1 (after): monty
    outer: monty
    


```
x = 100
def outer():
    x = 'python'  # masks global x
    def inner1():
        nonlocal x  # refers to x in outer
        x = 'monty' # changed x in outer scope
        def inner2():
            global x  # refers to x in global scope
            x = 'hello'
        print('inner1 (before):', x)
        inner2()
        print('inner1 (after):', x)
    inner1()
    print('outer', x)    
```


```
outer()
print(x)
```

    inner1 (after): monty
    outer monty
    100
    

But this will not work. In `inner` Python is looking for a local variable called `x`. `outer` has a label called `x`, but it is a global variable, not a local one - hence Python does not find a local variable in the scope chain.


```
x = 100
def outer():
    global x
    x = 'python'
    
    def inner():
        nonlocal x
        x = 'monty'
    inner()
```


      File "<ipython-input-17-3ccaec905318>", line 7
        nonlocal x
        ^
    SyntaxError: no binding for nonlocal 'x' found
    


##  Closures

Let's examine that concept of a cell to create an indirect reference for variables that are in multiple scopes.


```
def outer():
    x = 'python'
    def inner():
        print(x)
    return inner
```


```
fn = outer()
```


```
fn.__code__.co_freevars
```




    ('x',)



As we can see, `x` is a free variable in the closure.


```
fn.__closure__
```




    (<cell at 0x0000015F5299B4C8: str object at 0x0000015F51092068>,)



Here we see that the free variable x is actually a reference to a cell object that is itself a reference to a string object.

Let's see what the memory address of `x` is in the outer function and the inner function. To be sure string interning does not play a role, I am going to use an object that we know Python will not automatically intern, like a list.


```
def outer():
    x = [1, 2, 3]
    print('outer:', hex(id(x)))
    def inner():
        print('inner:', hex(id(x)))
        print(x)
    return inner
```


```
fn = outer()
```

    outer: 0x15f52907988
    


```
fn.__closure__
```




    (<cell at 0x0000015F5299B768: list object at 0x0000015F52907988>,)




```
fn()
```

    inner: 0x15f52907988
    [1, 2, 3]
    

As you can see, each the memory address of `x` in `outer`, `inner` and the cell all point to the same object.

#### Modifying the Free Variable

We know we can modify nonlocal variables by using the `nonlocal` keyword. So the following will work:


```
def counter():
    count = 0 # local variable
    
    def inc():
        nonlocal count  # this is the count variable in counter
        count += 1
        return count
    return inc
```


```
c = counter()
```


```
c()
```




    1




```
c()
```




    2



##### Shared Extended Scopes

As we saw in the lecture, we can set up nonlocal variables in different inner functionsd that reference the same outer scope variable, i.e. we have a free variable that is shared between two closures. This works because both non local variables and the outer local variable all point back to the same cell object.


```
def outer():
    count = 0
    def inc1():
        nonlocal count
        count += 1
        return count
    
    def inc2():
        nonlocal count
        count += 1
        return count
    
    return inc1, inc2
```


```
fn1, fn2 = outer()
```


```
fn1.__closure__, fn2.__closure__
```




    ((<cell at 0x0000015F5299B738: int object at 0x00000000506FEC50>,),
     (<cell at 0x0000015F5299B738: int object at 0x00000000506FEC50>,))



As you can see here, the `count` label points to the same cell.


```
fn1()
```




    1




```
fn1()
```




    2




```
fn2()
```




    3



### Multiple Instances of Closures

Recall that **every** time a function is called, a **new** local scope is created.


```
from time import perf_counter

def func():
    x = perf_counter()
    print(x, id(x))
```


```
func()
```

    2.7089464582150425e-07 1508916709680
    


```
func()
```

    0.011222623387093279 1508916709680
    

The same thing happens with closures, they have their own extended scope every time the closure is created:


```
def pow(n):
    # n is local to pow
    def inner(x):
        # x is local to inner
        return x ** n
    return inner
```

In this example, `n`, in the function `inner` is a free variable, so we have a closure that contains `inner` and the free variable `n`


```
square = pow(2)
```


```
square(5)
```




    25




```
cube = pow(3)
```


```
cube(5)
```




    125



We can see that the cell used for the free variable in both cases is **different**:


```
square.__closure__
```




    (<cell at 0x0000015F5299B8B8: int object at 0x00000000506FEC90>,)




```
cube.__closure__
```




    (<cell at 0x0000015F5299BAC8: int object at 0x00000000506FECB0>,)



In fact, these functions (`square` and `cube`) are **not** the same functions, even though they were "created" from the same `power` function:


```
id(square), id(cube)
```




    (1508919294560, 1508919295784)



### Beware!

Remember when I said the captured variable is a reference established when the closure is created, but the value is looked up only once the function is called?

This can create very subtle bugs in your program.

Consider the following example where we want to create some functions that can add 1, 2, 3, 4 and to whatever is passed to them.

We could do the following:


```
def adder(n):
    def inner(x):
        return x + n
    return inner
```


```
add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)
add_4 = adder(4)
```


```
add_1(10), add_2(10), add_3(10), add_4(10)
```




    (11, 12, 13, 14)



But suppose we want to get a little fancier and do it as follows:


```
def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x: x + n)
    return adders
```


```
adders = create_adders()
```

Now technically we have 4 functions in the `adders` list:


```
adders
```




    [<function __main__.create_adders.<locals>.<lambda>>,
     <function __main__.create_adders.<locals>.<lambda>>,
     <function __main__.create_adders.<locals>.<lambda>>,
     <function __main__.create_adders.<locals>.<lambda>>]



The first one should add 1 to the value we pass it, the second should add 2, and so on.


```
adders[3](10)
```




    14



Yep, that works for the 4th function.


```
adders[0](10)
```




    14



Uh Oh - what happened? In fact we get the same behavior from every one of those functions:


```
adders[0](10), adders[1](10), adders[2](10), adders[3](10)
```




    (14, 14, 14, 14)



Remember what I said about when the variable is captured and when the value is looked up?

When the lambdas are **created** their `n` is the `n` used in the loop - the **same** `n`!!


```
adders[0].__code__.co_freevars
```




    ('n',)




```
adders[0].__closure__
```




    (<cell at 0x0000015F5299B3D8: int object at 0x00000000506FECD0>,)




```
adders[1].__closure__
```




    (<cell at 0x0000015F5299B3D8: int object at 0x00000000506FECD0>,)




```
adders[2].__closure__
```




    (<cell at 0x0000015F5299B3D8: int object at 0x00000000506FECD0>,)




```
adders[3].__closure__
```




    (<cell at 0x0000015F5299B3D8: int object at 0x00000000506FECD0>,)



So, by the time we call `adder[i]`, the free variable `n` (shared between all adders) is set to 4.


```
hex(id(4))
```




    '0x506fecd0'



As we can see the memory address of the singleton integer 4, is what that cell is pointint to.

If you want to use a loop to do this and not end up using the same cell for each of the free variables, we can use a simple trick that forces the evaluation of `n` at the time the closure is **created**, instead of when the closure function is evaluated.

We can do this by creating a parameter for `n` in our lambda whose default value is the current value of `n` - remember from an earlier video that parameter defaults are avaluated when the function is created, not called.


```
def create_adders():
    adders = []
    for n in range(1, 5):
        adders.append(lambda x, step=n: x + step)
    return adders
```


```
adders = create_adders()
```


```
adders[0].__closure__
```

Why aren't we getting anything in the closure? What about free variables?


```
adders[0].__code__.co_freevars
```




    ()



Hmm, nothing either... Why?

Well, look at the lambda in that loop. Does it reference the variable `n` (other than in the default value)? No. Hence, `n` is **not** a free variable in this case, and our lambda is just a plain lambda, not a closure.

And this code will now work as expected:


```
adders[0](10)
```




    11




```
adders[1](10)
```




    12




```
adders[2](10)
```




    13




```
adders[3](10)
```




    14



You just need to understand that since the default values are evaluated when the function (lambda in this case) is **created**, the then-current `n` value is assigned to the local variable `step`. So `step` will not change every time the lambda is called, and since n is not referenced inside the function (and therefore evaluated when the lambda is called), `n` is not a free variable.

#### Nested Closures

We can also nest closures, as can be seen in this example:


```
def incrementer(n):
    def inner(start):
        current = start
        def inc():
            a = 10  # local var
            nonlocal current
            current += n
            return current
        return inc
    return inner
        
```


```
fn = incrementer(2)
```


```
fn
```




    <function __main__.incrementer.<locals>.inner>




```
fn.__code__.co_freevars
```




    ('n',)




```
fn.__closure__
```




    (<cell at 0x0000015F5299B798: int object at 0x00000000506FEC90>,)




```
inc_2 = fn(100)
```


```
inc_2
```




    <function __main__.incrementer.<locals>.inner.<locals>.inc>




```
inc_2.__code__.co_freevars
```




    ('current', 'n')




```
inc_2.__closure__
```




    (<cell at 0x0000015F5299B318: int object at 0x00000000506FF8D0>,
     <cell at 0x0000015F5299B798: int object at 0x00000000506FEC90>)



Here you can see that the second free variable `n`, is pointing to the same cell as the free variable in `fn`.

Note that **a** is a local variable, and is not considered a free variable.

And we can call the closures as follows:


```
inc_2()
```




    102




```
inc_2()
```




    104




```
inc_3 = incrementer(3)(200)
```


```
inc_3()
```




    203




```
inc_3()
```




    206



##  Closure Applications (Part 1)

In this example we are going to build an averager function that can average multiple values.

The twist is that we want to simply be able to feed numbers to that function and get a running average over time, not average a list which requires performing the same calculations (sum and count) over and over again.


```
class Averager:
    def __init__(self):
        self.numbers = []
    
    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count
```


```
a = Averager()
```


```
a.add(10)
```




    10.0




```
a.add(20)
```




    15.0




```
a.add(30)
```




    20.0



We can do this using a closure as follows:


```
def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add
```


```
a = averager()
```


```
a(10)
```




    10.0




```
a(20)
```




    15.0




```
a(30)
```




    20.0



Now, instead of storing a list and reclaculating `total` and `count` every time wer need the new average, we are going to store the running total and count and update each value each time a new value is added to the running average, and then return `total / count`.

Let's start with a class approach first, where we will use instance variables to store the running total and count and provide an instance method to add a new number and return the current average.


```
class Averager:
    def __init__(self):
        self._count = 0
        self._total = 0
    
    def add(self, value):
        self._total += value
        self._count += 1
        return self._total / self._count
```


```
a = Averager()
```


```
a.add(10)
```




    10.0




```
a.add(20)
```




    15.0




```
a.add(30)
```




    20.0



Now, let's see how we might use a closure to achieve the same thing.


```
def averager():
    total = 0
    count = 0
    
    def add(value):
        nonlocal total, count
        total += value
        count += 1
        return 0 if count == 0 else total / count
    
    return add
        
```


```
a = averager()
```


```
a(10)
```




    10.0




```
a(20)
```




    15.0




```
a(30)
```




    20.0



#### Generalizing this example

We saw that we were essentially able to convert a class to an equivalent functionality using closures. This is actually true in a much more general sense - very often, classes that define a single method (other than initializers) can be implemented using a closure instead.

Let's look at another example of this.

Suppose we want something that can keep track of the running elapsed time in seconds.


```
from time import perf_counter
```


```
class Timer:
    def __init__(self):
        self._start = perf_counter()
    
    def __call__(self):
        return (perf_counter() - self._start)
```


```
a = Timer()
```

Now wait a bit before running the next line of code:


```
a()
```




    0.011695334544051804



Let's start another "timer":


```
b = Timer()
```


```
print(a())
print(b())
```

    0.03528294403966765
    0.011656054820407689
    

Now let's rewrite this using a closure instead:


```
def timer():
    start = perf_counter()
    
    def elapsed():
        # we don't even need to make start nonlocal 
        # since we are only reading it
        return perf_counter() - start
    
    return elapsed
```


```
x = timer()
```


```
x()
```




    0.011068213438975016




```
y = timer()
```


```
print(x())
print(y())
```

    0.03419096772236116
    0.01164738619174141
    


```
print(a())
print(b())
print(x())
print(y())
```

    0.10822159832175349
    0.08475345336494494
    0.0462381944113351
    0.023573252079387305
    

##  Closure Applications (Part 2)

#### Example 1

Let's write a small function that can increment a counter for us - we don't have an incrementor in Python (the ++ operator in Java or C++ for example):


```
def counter(initial_value):
    # initial_value is a local variable here
    
    def inc(increment=1):
        nonlocal initial_value
        # initial_value is a nonlocal (captured) variable here
        initial_value += increment
        return initial_value
    
    return inc
```


```
counter1 = counter(0)
```


```
print(counter1(0))
```

    0
    


```
print(counter1())
```

    1
    


```
print(counter1())
```

    2
    


```
print(counter1(8))
```

    10
    


```
counter2 = counter(1000)
```


```
print(counter2(0))
```

    1000
    


```
print(counter2(1))
```

    1001
    


```
print(counter2())
```

    1002
    


```
print(counter2(220))
```

    1222
    

As you can see, each closure maintains a reference to the **initial_value** variable that was created when the **counter** function was **called** - each time that function was called, a new local variable **initial_value** was created (with a value assigned from the argument), and it became a nonlocal (captured) variable in the inner scope.

#### Example 2

Let's modify this example to now build something that can run, and maintain a count of how many times we have run some function.


```
def counter(fn):
    cnt = 0  # initially fn has been run zero times
    
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    
    return inner
```


```
def add(a, b):
    return a + b
```


```
counted_add = counter(add)
```

And the free variables are:


```
counted_add.__code__.co_freevars
```




    ('cnt', 'fn')



We can now call the `counted_add` function:


```
counted_add(1, 2)
```

    add has been called 1 times
    




    3




```
counted_add(2, 3)
```

    add has been called 2 times
    




    5




```
def mult(a, b, c):
    return a * b * c
```


```
counted_mult = counter(mult)
```


```
counted_mult(1, 2, 3)
```

    mult has been called 1 times
    




    6




```
counted_mult(2, 3, 4)
```

    mult has been called 2 times
    




    24



#### Example 3

Let's take this one step further, and actually store the function name and the number of calls in a global dictionary instead of just printing it out all the time.


```
counters = dict()

def counter(fn):
    cnt = 0  # initially fn has been run zero times
    
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt  # counters is global
        return fn(*args, **kwargs)
    
    return inner
```


```
counted_add = counter(add)
counted_mult = counter(mult)
```

Note that `counters` is a **global** variable, and therefore **not** a free variable:


```
counted_add.__code__.co_freevars
```




    ('cnt', 'fn')




```
counted_mult.__code__.co_freevars
```




    ('cnt', 'fn')



We can now call out functions:


```
counted_add(1, 2)
```




    3




```
counted_add(2, 3)
```




    5




```
counted_mult(1, 2, 'a')
```




    'aa'




```
counted_mult(2, 3, 'b')
```




    'bbbbbb'




```
counted_mult(1, 1, 'abc')
```




    'abc'




```
print(counters)
```

    {'add': 2, 'mult': 3}
    

Of course this relies on us creating the **counters** global variable first and making sure we are naming it that way, so instead, we're going to pass it as an argument to the **counter** function:


```
def counter(fn, counters):
    cnt = 0  # initially fn has been run zero times
    
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt  # counters is nonlocal
        return fn(*args, **kwargs)
    
    return inner
```


```
func_counters = dict()
counted_add = counter(add, func_counters)
counted_mult = counter(mult, func_counters)
```


```
counted_add.__code__.co_freevars
```




    ('cnt', 'counters', 'fn')



As you can see, `counters` is now a free variable.

We can now call our functions:


```
for i in range(5):
    counted_add(i, i)

for i in range(10):
    counted_mult(i, i, i)
```


```
print(func_counters)
```

    {'add': 5, 'mult': 10}
    

Of course, we don't have to assign the "counted" version of our functions a new name - we can simply assign it to the same name!


```
def fact(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product
```


```
fact = counter(fact, func_counters)
```


```
fact(0)
```




    1




```
fact(3)
```




    6




```
fact(4)
```




    24




```
print(func_counters)
```

    {'add': 5, 'mult': 10, 'fact': 3}
    

Notice, how we essentially **added** some functionality to our `fact` function, without modifying what the `fact` function actually returns.

This leads us straight into our next topic: decorators!

##  Decorators (Part 1)

Recall the example in the last section where we wrote a simple closure to count how many times a function had been run:


```
def counter(fn):
    count = 0
    
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner
```


```
def add(a, b=0):
    """
    returns the sum of a and b
    """
    return a + b
```


```
help(add)
```

    Help on function add in module __main__:
    
    add(a, b=0)
        returns the sum of a and b
    
    

Here's the memory address that `add` points to:


```
id(add)
```




    2352389334696



Now we create a closure using the `add` function as an argument to the `counter` function:


```
add = counter(add)
```

And you'll note that `add` is no longer the same function as before. Indeed the memory address `add` points to is no longer the same:


```
id(add)
```




    2352404346128




```
add(1, 2)
```

    Function add was called 1 times
    




    3




```
add(2, 2)
```

    Function add was called 2 times
    




    4



What happened is that we put our **add** function 'through' the **counter** function - we usually say that we **decorated** our function **add**.

And we call that **counter** function a **decorator**.

There is a shorthand way of decorating our function without having to type:

``func = counter(func)``


```
@counter
def mult(a: float, b: float=1, c: float=1) -> float:
    """
    returns the product of a, b, and c
    """
    return a * b * c
```


```
mult(1, 2, 3)
```

    Function mult was called 1 times
    




    6




```
mult(2, 2, 2)
```

    Function mult was called 2 times
    




    8



Let's do a little bit of introspection on our two decorated functions:


```
add.__name__
```




    'inner'




```
mult.__name__
```




    'inner'



As you can see, the name of the function is no longer **add** or **mult**, but instead it is the name of that **inner** function in our decorator.


```
help(add)
```

    Help on function inner in module __main__:
    
    inner(*args, **kwargs)
    
    


```
help(mult)
```

    Help on function inner in module __main__:
    
    inner(*args, **kwargs)
    
    

As you can see, we've also lost our docstring and parameter annotations!

What about introspecting the parameters of **add** and **mult**:


```
import inspect
```


```
inspect.getsource(add)
```




    "    def inner(*args, **kwargs):\n        nonlocal count\n        count += 1\n        print('Function {0} was called {1} times'.format(fn.__name__, count))\n        return fn(*args, **kwargs)\n"




```
inspect.getsource(mult)
```




    "    def inner(*args, **kwargs):\n        nonlocal count\n        count += 1\n        print('Function {0} was called {1} times'.format(fn.__name__, count))\n        return fn(*args, **kwargs)\n"



Even the signature is gone:


```
inspect.signature(add)
```




    <Signature (*args, **kwargs)>




```
inspect.signature(mult)
```




    <Signature (*args, **kwargs)>



Even the parameter defaults documentation is are gone:


```
inspect.signature(add).parameters
```




    mappingproxy({'args': <Parameter "*args">, 'kwargs': <Parameter "**kwargs">})



In general, when we create decorated functions, we end up "losing" a lot of the metadata of our original function!

However, we **can** put that information back in - it can get quite complicated.

Let's see how we might be able to do that for some simple things, like the docstring and the function name.


```
def counter(fn):
    count = 0
    
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner
```


```
@counter
def add(a: int, b: int=10) -> int:
    """
    returns sum of two integers
    """
    return a + b
```


```
help(add)
```

    Help on function add in module __main__:
    
    add(*args, **kwargs)
        returns sum of two integers
    
    


```
add.__name__
```




    'add'



At least we have the docstring and function name back... But what about the parameters? Our real **add** function takes two positional parameters, but because the closure used a generic way of accepting **\*args** and **\*\*kwargs**, we lose this information

We can use a special function in the **functools** module, called **wraps**. In fact, that function is a decorator itself!


```
from functools import wraps
```


```
def counter(fn):
    count = 0
    
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))

    return inner
```


```
@counter
def add(a: int, b: int=10) -> int:
    """
    returns sum of two integers
    """
    return a + b
```


```
help(add)
```

    Help on function add in module __main__:
    
    add(a:int, b:int=10) -> int
        returns sum of two integers
    
    

Yay!!! Everything is back to normal.


```
inspect.getsource(add)
```




    '@counter\ndef add(a: int, b: int=10) -> int:\n    """\n    returns sum of two integers\n    """\n    return a + b\n'




```
inspect.signature(add)
```




    <Signature (a:int, b:int=10) -> int>




```
inspect.signature(add).parameters
```




    mappingproxy({'a': <Parameter "a:int">, 'b': <Parameter "b:int=10">})



##  Decorators Application (Timing)

Here we go back to an example we have seen in the past - timing how long it takes to run a certain function.


```
def timed(fn):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        
        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__, 
                                                         args_str,
                                                         elapsed))
        return result
    
    return inner
```

Let's write a function that calculates the n-th Fibonacci number:

`1, 1, 2, 3, 5, 8, ...`

We will implement this using three different methods:
1. recursion
2. a loop
3. functional programming (reduce)

We use a 1-based system, e.g. first Fibonnaci number has index 1, etc.

#### Using Recursion



```
def calc_recursive_fib(n):
    if n <=2:
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)
```


```
calc_recursive_fib(3)
```




    2




```
calc_recursive_fib(6)
```




    8




```
@timed
def fib_recursed(n):
    return calc_recursive_fib(n)
```


```
fib_recursed(33)
```

    fib_recursed(33) took 1.060477s to run.
    




    3524578




```
fib_recursed(34)
```

    fib_recursed(34) took 1.715229s to run.
    




    5702887




```
fib_recursed(35)
```

    fib_recursed(35) took 2.773638s to run.
    




    9227465



There's a reason we did not decorate our recursive function directly!


```
@timed
def fib_recursed_2(n):
    if n <=2:
        return 1
    else:
        return fib_recursed_2(n-1) + fib_recursed_2(n-2)
```


```
fib_recursed_2(10)
```

    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000001s to run.
    fib_recursed_2(3) took 0.000409s to run.
    fib_recursed_2(2) took 0.000001s to run.
    fib_recursed_2(4) took 0.000460s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000038s to run.
    fib_recursed_2(5) took 0.000535s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000038s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(4) took 0.000075s to run.
    fib_recursed_2(6) took 0.000646s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000036s to run.
    fib_recursed_2(2) took 0.000001s to run.
    fib_recursed_2(4) took 0.000071s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000035s to run.
    fib_recursed_2(5) took 0.000143s to run.
    fib_recursed_2(7) took 0.000837s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000001s to run.
    fib_recursed_2(3) took 0.000036s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(4) took 0.000072s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000036s to run.
    fib_recursed_2(5) took 0.000142s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000037s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(4) took 0.000073s to run.
    fib_recursed_2(6) took 0.000251s to run.
    fib_recursed_2(8) took 0.001125s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000041s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(4) took 0.000076s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000035s to run.
    fib_recursed_2(5) took 0.000146s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000001s to run.
    fib_recursed_2(3) took 0.000036s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(4) took 0.000072s to run.
    fib_recursed_2(6) took 0.000253s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000001s to run.
    fib_recursed_2(3) took 0.000048s to run.
    fib_recursed_2(2) took 0.000001s to run.
    fib_recursed_2(4) took 0.000085s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000036s to run.
    fib_recursed_2(5) took 0.000156s to run.
    fib_recursed_2(7) took 0.000444s to run.
    fib_recursed_2(9) took 0.001604s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000001s to run.
    fib_recursed_2(3) took 0.000036s to run.
    fib_recursed_2(2) took 0.000001s to run.
    fib_recursed_2(4) took 0.000071s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000036s to run.
    fib_recursed_2(5) took 0.000142s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000036s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(4) took 0.000071s to run.
    fib_recursed_2(6) took 0.000248s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000040s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(4) took 0.000075s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000036s to run.
    fib_recursed_2(5) took 0.000145s to run.
    fib_recursed_2(7) took 0.000429s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000035s to run.
    fib_recursed_2(2) took 0.000001s to run.
    fib_recursed_2(4) took 0.000075s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000035s to run.
    fib_recursed_2(5) took 0.000145s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(1) took 0.000000s to run.
    fib_recursed_2(3) took 0.000041s to run.
    fib_recursed_2(2) took 0.000000s to run.
    fib_recursed_2(4) took 0.000076s to run.
    fib_recursed_2(6) took 0.000256s to run.
    fib_recursed_2(8) took 0.000720s to run.
    fib_recursed_2(10) took 0.002367s to run.
    




    55



Since we are calling the function recursively, we are actually calling the **decorated** function recursively. In this case I wanted the total time to calculate the n-th number, not the time for each recursion.

You will notice from the above how inefficient the recursive method is: the same fibonacci numbers are calculated repeatedly! This is why as the value of `n` start increasing beyond 30 we start seeing considerable slow downs.

#### Using a Loop


```
@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2               
```


```
fib_loop(3)
```

    fib_loop(3) took 0.000003s to run.
    




    2




```
fib_loop(6)
```

    fib_loop(6) took 0.000002s to run.
    




    8




```
fib_loop(34)
```

    fib_loop(34) took 0.000004s to run.
    




    5702887




```
fib_loop(35)
```

    fib_loop(35) took 0.000005s to run.
    




    9227465



As you can see this method is much more efficient!

#### Using  Reduce

We first need to understand how we are going to calculate the Fibonnaci sequence using reduce: 

<pre>
n=1:
(1, 0) --> (1, 1)

n=2:
(1, 0) --> (1, 1) --> (1 + 1, 1) = (2, 1)  : result = 2 

n=3
(1, 0) --> (1, 1) --> (2, 1) --> (2+1, 2) = (3, 2)  : result = 3

n=4
(1, 0) --> (1, 1) --> (2, 1) --> (3, 2) --> (5, 3)  : result = 5
</pre>

In general each step in the reduction is as follows:

<pre>
previous value = (a, b)
new value = (a+b, a)
</pre>

If we start our reduction with an initial value of `(1, 0)`, we need to run our "loop" n times.

We therefore use a "dummy" sequence of length `n` to create `n` steps in our reduce.



```
from functools import reduce

@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n-1)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), 
                   dummy, 
                   initial)
    return fib_n[0]                  
```


```
fib_reduce(3)
```

    fib_reduce(3) took 0.000004s to run.
    




    2




```
fib_reduce(6)
```

    fib_reduce(6) took 0.000005s to run.
    




    8




```
fib_reduce(34)
```

    fib_reduce(34) took 0.000013s to run.
    




    5702887




```
fib_reduce(35)
```

    fib_reduce(35) took 0.000014s to run.
    




    9227465



Now we can run a quick comparison between the various timed implementations:


```
fib_recursed(35)
fib_loop(35)
fib_reduce(35)
```

    fib_recursed(35) took 2.771373s to run.
    fib_loop(35) took 0.000007s to run.
    fib_reduce(35) took 0.000013s to run.
    




    9227465



Even though the recursive algorithm is by far the easiest to understand, it is also the slowest. We'll see how to fix this in an upcoming video using a technique called **memoization**.

First let's focus on the loop and reduce variants. Our timing is not very effective since we only time a single calculation for each - there could be some variance if we run these tests multiple times:


```
for i in range(10):
    result =  fib_loop(10000)
```

    fib_loop(10000) took 0.002114s to run.
    fib_loop(10000) took 0.002109s to run.
    fib_loop(10000) took 0.002072s to run.
    fib_loop(10000) took 0.002072s to run.
    fib_loop(10000) took 0.002075s to run.
    fib_loop(10000) took 0.002078s to run.
    fib_loop(10000) took 0.002049s to run.
    fib_loop(10000) took 0.002064s to run.
    fib_loop(10000) took 0.002533s to run.
    fib_loop(10000) took 0.002109s to run.
    


```
for i in range(10):
    result = fib_reduce(10000)
```

    fib_reduce(10000) took 0.004234s to run.
    fib_reduce(10000) took 0.003961s to run.
    fib_reduce(10000) took 0.004363s to run.
    fib_reduce(10000) took 0.004459s to run.
    fib_reduce(10000) took 0.003895s to run.
    fib_reduce(10000) took 0.003847s to run.
    fib_reduce(10000) took 0.004342s to run.
    fib_reduce(10000) took 0.003908s to run.
    fib_reduce(10000) took 0.003970s to run.
    fib_reduce(10000) took 0.003970s to run.
    

In general it is better to time the same function call multiple times and generate and average of the run times.

We'll see in an upcoming video how we can do this from within our decorator.

In the meantime observe that the simple loop approach seems to perform about twice as fast as the reduce approach!!

The moral of this side note is that simply because you **can** do something in  Python using some fancy or cool technique does not mean you **should**!

We technically could write our reduce-based function as a one liner:


```
from functools import reduce 

fib_1 = timed(lambda n: reduce(lambda prev, n: (prev[0] + prev[1], prev[0]),
                               range(n), 
                               (0, 1))[0])
```


```
fib_loop(100)
```

    fib_loop(100) took 0.000009s to run.
    




    354224848179261915075




```
fib_1(100)
```

    <lambda>(100) took 0.000031s to run.
    




    354224848179261915075



So yes, it's cool that you can write this using a single line of code, but consider two things here:
1. Is it as efficient as another method?
2. Is the code **readable**?

Code readability is something I cannot emphasize enough. Given similar efficiencies (cpu / memory), give preference to code that is more easily understandable!

Sometimes, if the efficiency is not greatly impacted (or does not matter in absolute terms), I might even give preference to less efficient, but more readable (i.e. understanbdable), code.

But enough of the soapbox already :-)

##  Decorators Application (Logger, Stacked Decorators)

In this example we're going to create a utility decorator that will log function calls (to the console, but in practice you would be writing your logs to a file (e.g. using Python's built-in logger), or to a database, etc.


```
def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    
    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(fn.__name__, run_dt))
        return result
        
    return inner
```


```
@logged
def func_1():
    pass
```


```
@logged
def func_2():
    pass
```


```
func_1()
```

    func_1: called 2017-12-10 00:09:19.443657+00:00
    


```
func_2()
```

    func_2: called 2017-12-10 00:09:19.460691+00:00
    

Now we may additionaly also want to time the function. We can certainly include the code to do so in our `logged` decorator, but we could also just use the `@timed` decorator we already wrote by **stacking** our decorators.


```
def timed(fn):
    from functools import wraps
    from time import perf_counter
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print('{0} ran for {1:.6f}s'.format(fn.__name__, end-start))
        return result
    
    return inner
```


```
@timed
@logged
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))
```


```
factorial(10)
```

    factorial: called 2017-12-10 00:09:19.496762+00:00
    factorial ran for 0.000130s
    




    3628800



Note that the order in which we stack the decorators can make a difference!

Remember that this is because our stacked decorators essentially amounted to:


```
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))

factorial = timed(logged(factorial))
```

So in this case the `timed` decorator will be called first, followed by the `logged` decorator.

You may wonder why the printed output seems reversed. Look at how the decorators were defined - they first ran the function passed in, and **then** printed the result.

So in the above example, a simplified look at what happens in each decorator:

* `timed(fn)(*args, **kwargs)`:
    1. calls `fn(*args, **kwargs)`
    2. prints timing
    
    
* `logged(fn)(*args, **kwargs)`:
    1. calls `fn(*args, **kwargs)`
    2. prints log info

So, calling
`factorial = timed(logged(factorial))`

is equivalent to:

<pre>
fn = logged(factorial)
factorial = timed(fn)

factorial(n) --> call timed(fn)(n)
             --> call fn(n), then print timing
             --> call logged(original_factorial)(n), then print timing
             --> call original_factorial(n), then log, then print timing
</pre>

So as you can see, the `timed` decorator ran first, but it called the logged decorated function first, then printed the result - hence why the print output seems reversed.


```
factorial(10)
```

    factorial: called 2017-12-10 00:09:19.525820+00:00
    factorial ran for 0.000147s
    




    3628800



But in the following case, the `logged` decorator will run first, followed by the `timed` decorator:


```
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))

factorial = logged(timed(factorial))
```


```
factorial(10)
```

    factorial ran for 0.000015s
    factorial: called 2017-12-10 00:09:19.547866+00:00
    




    3628800



Or, using the **@** notation:


```
@logged
@timed
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))
```


```
factorial(10)
```

    factorial ran for 0.000016s
    factorial: called 2017-12-10 00:09:19.572914+00:00
    




    3628800




```
@timed
@logged
def factorial(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))
```


```
factorial(10)
```

    factorial: called 2017-12-10 00:09:19.608237+00:00
    factorial ran for 0.000153s
    




    3628800



To make this clearer, let's write two very simple decorators as follows:


```
def dec_1(fn):
    def inner():
        print('running dec_1')
        return fn()
    return inner
```


```
def dec_2(fn):
    def inner():
        print('running dec_2')
        return fn()
    return inner
```


```
@dec_1
@dec_2
def my_func():
    print('running my_func')
```


```
my_func()
```

    running dec_1
    running dec_2
    running my_func
    

But if we change the order of the decorators:


```
@dec_2
@dec_1
def my_func():
    print('running my_func')
```


```
my_func()
```

    running dec_2
    running dec_1
    running my_func
    

You may wonder whether this really matters in practice. And yes, it can.

Consider an API that contains various functions that can be called. However, endpoints are secured and can only be run by authenticated users who have some specific role(s). If they do not have the role you want to return an unauthorized error. But if they do, then you want to log that they called the endpoint.

In this case you may have one decorator that is used to check authentication and permissions (and immediately return an unauthorized error from the API if applicable), and the other to log the call. 

If you decorated it this way:

<pre>
@log
@authorize
def my_endpoint():
    pass
</pre>

then the call would always be logged.

But, in this instance:

<pre>
@authorize
@log
def my_endpoint():
    pass
</pre>

your endpoint would only get logged if the user passed the `authorize` test.

##  Decorators Application (Memoization)

Let's go back to our Fibonacci example:


```
def fib(n):
    print ('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)
```

When we run this, we see that it is quite inefficient, as the same Fibonacci numbers get calculated multiple times:


```
fib(6)
```

    Calculating fib(6)
    Calculating fib(5)
    Calculating fib(4)
    Calculating fib(3)
    Calculating fib(2)
    Calculating fib(1)
    Calculating fib(2)
    Calculating fib(3)
    Calculating fib(2)
    Calculating fib(1)
    Calculating fib(4)
    Calculating fib(3)
    Calculating fib(2)
    Calculating fib(1)
    Calculating fib(2)
    




    8



It would be better if we could somehow "store" these results, so if we have calculated `fib(4)` and `fib(3)` before, we could simply recall the these values when calculating `fib(5) = fib(4) + fib(3)` instead of recalculating them.

This concept of improving the efficiency of our code by caching pre-calculated values so they do not need to be re-calcualted every time, is called "memoization"

We can approach this using a simple class and a dictionary that stores any Fibonacci number that's already been calculated:


```
class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}
    
    def fib(self, n):
        if n not in self.cache:
            print('Calculating fib({0})'.format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]
```


```
f = Fib()
```


```
f.fib(1)
```




    1




```
f.fib(6)
```

    Calculating fib(6)
    Calculating fib(5)
    Calculating fib(4)
    Calculating fib(3)
    




    8




```
f.fib(7)
```

    Calculating fib(7)
    




    13



Let's see how we could rewrite this using a closure:


```
def fib():
    cache = {1: 1, 2: 2}
    
    def calc_fib(n):
        if n not in cache:
            print('Calculating fib({0})'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    
    return calc_fib
```


```
f = fib()
```


```
f(10)
```

    Calculating fib(10)
    Calculating fib(9)
    Calculating fib(8)
    Calculating fib(7)
    Calculating fib(6)
    Calculating fib(5)
    Calculating fib(4)
    Calculating fib(3)
    




    89



Now let's see how we would implement this using a decorator:


```
from functools import wraps

def memoize_fib(fn):
    cache = dict()
    
    @wraps(fn)
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    
    return inner
```


```
@memoize_fib
def fib(n):
    print ('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)
```


```
fib(3)
```

    Calculating fib(3)
    Calculating fib(2)
    Calculating fib(1)
    




    2




```
fib(10)
```

    Calculating fib(10)
    Calculating fib(9)
    Calculating fib(8)
    Calculating fib(7)
    Calculating fib(6)
    Calculating fib(5)
    Calculating fib(4)
    




    55




```
fib(6)
```




    8



As you can see, we are hitting the cache when the values are available.

Now, we made our memoization decorator "hardcoded" to single argument functions - we could make it more generic.

For example, to handle an arbitrary number of positional arguments and keyword-only arguments we could do the following:


```
def memoize(fn):
    cache = dict()
    
    @wraps(fn)
    def inner(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    
    return inner
```


```
@memoize
def fib(n):
    print ('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)
```


```
fib(6)
```

    Calculating fib(6)
    Calculating fib(5)
    Calculating fib(4)
    Calculating fib(3)
    Calculating fib(2)
    Calculating fib(1)
    




    8




```
fib(7)
```

    Calculating fib(7)
    




    13



Of course, with this rather generic memoization decorator we can memoize other functions too:


```
def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n < 2 else n * fact(n-1)
```


```
fact(5)
```

    Calculating 5!
    Calculating 4!
    Calculating 3!
    Calculating 2!
    Calculating 1!
    




    120




```
fact(5)
```

    Calculating 5!
    Calculating 4!
    Calculating 3!
    Calculating 2!
    Calculating 1!
    




    120



And memoizing it:


```
@memoize
def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n < 2 else n * fact(n-1)
```


```
fact(6)
```

    Calculating 6!
    Calculating 5!
    Calculating 4!
    Calculating 3!
    Calculating 2!
    Calculating 1!
    




    720




```
fact(6)
```




    720



Our simple memoizer has a drawback however:
* the cache size is unbounded - probably not a good thing! In general we want to limit the cache to a certain number of entries, balancing computational efficiency vs memory utilization.
* we are not handling **kwargs

Memoization is such a common thing to do that Python actually has a memoization decorator built for us!

It's in the, you guessed it, **functools** module, and is called **lru_cache** and is going to be quite a bit more efficient compared to the rudimentary memoization example we did above.

[LRU Cache = Least Recently Used caching: since the cache is not unlimited, at some point cached entries need to be discarded, and the least recently used entries are discarded first]


```
from functools import lru_cache
```


```
@lru_cache()
def fact(n):
    print("Calculating fact({0})".format(n))
    return 1 if n < 2 else n * fact(n-1)
```


```
fact(5)
```

    Calculating fact(5)
    Calculating fact(4)
    Calculating fact(3)
    Calculating fact(2)
    Calculating fact(1)
    




    120




```
fact(4)
```




    24



As you can see, `fact(4)` was returned via a cached entry!

Same thing with our Fibonacci function:


```
@lru_cache()
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)
```


```
fib(6)
```

    Calculating fib(6)
    Calculating fib(5)
    Calculating fib(4)
    Calculating fib(3)
    Calculating fib(2)
    Calculating fib(1)
    




    8




```
fib(5)
```




    5



Recall from a few videos back that we timed the calculation for Fibonacci numbers. Calculating fib(35) took several seconds - every time...


```
from time import perf_counter
```


```
def fib_no_memo(n):
    return 1 if n < 3 else fib_no_memo(n-1) + fib_no_memo(n-2)
```


```
start = perf_counter()
result = fib_no_memo(35)
print("result={0}, elapsed: {1}s".format(result, perf_counter() - start))
```

    result=9227465, elapsed: 2.939012289158911s
    


```
@lru_cache()
def fib_memo(n):
    return 1 if n < 3 else fib_memo(n-1) + fib_memo(n-2)
```


```
start = perf_counter()
result = fib_memo(35)
print("result={0}, elapsed: {1}s".format(result, perf_counter() - start))
```

    result=9227465, elapsed: 9.83349429017899e-05s
    

And if we make the calls again:


```
start = perf_counter()
result = fib_no_memo(35)
print("result={0}, elapsed: {1}s".format(result, perf_counter() - start))
```

    result=9227465, elapsed: 2.782454120518548s
    


```
start = perf_counter()
result = fib_memo(35)
print("result={0}, elapsed: {1}s".format(result, perf_counter() - start))
```

    result=9227465, elapsed: 5.6617088337596044e-05s
    

You may have noticed that the `lru_cache` decorator was implemented using `()` - we'll see more on this later, but that's because decorators can themselves have parameters (beyond the function being decorated).

One of the arguments to the `lru_cache` decorator is the size of the cache - it defaults to 128 items, but we can easily change this - for performance reasons use powers of 2 for the cache size (or None for unbounded cache):


```
@lru_cache(maxsize=8)
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)
```


```
fib(10)
```

    Calculating fib(10)
    Calculating fib(9)
    Calculating fib(8)
    Calculating fib(7)
    Calculating fib(6)
    Calculating fib(5)
    Calculating fib(4)
    Calculating fib(3)
    Calculating fib(2)
    Calculating fib(1)
    




    55




```
fib(20)
```

    Calculating fib(20)
    Calculating fib(19)
    Calculating fib(18)
    Calculating fib(17)
    Calculating fib(16)
    Calculating fib(15)
    Calculating fib(14)
    Calculating fib(13)
    Calculating fib(12)
    Calculating fib(11)
    




    6765




```
fib(10)
```

    Calculating fib(10)
    Calculating fib(9)
    Calculating fib(8)
    Calculating fib(7)
    Calculating fib(6)
    Calculating fib(5)
    Calculating fib(4)
    Calculating fib(3)
    Calculating fib(2)
    Calculating fib(1)
    




    55



You'll not how Python had to recalculate `fib` for `10, 9,` etc. This is because the cache can only contain 10 items, so when we calculated `fib(20)`, it stored fib for `20, 19, ..., 11` (10 items) and therefore the oldest items fib `10, 9, ..., 1` were removed from the cache to make space.

##  Decorators 2

We have seen how to create some simple and not so simple decorators.

However we have also been using built-in decorators that can accept parameters, such as `wraps` and `lru_cache`.

This can be quite useful and we can accomplish the same thing ourselves.

First recall our original timer decorator from an earlier video (Decorator Application - Timer):


```
def timed(fn):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start
        print('Run time: {0:.6f}s'.format(elapsed))
        return result
    
    return inner
```


```
def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-1) + calc_fib_recurse(n-2)

def fib(n):
    return calc_fib_recurse(n)
```

We can decorate our Fibonacci function using the **@** syntax, or the longer syntax as follows:


```
fib = timed(fib)
```


```
fib(30)
```

    Run time: 0.255260s
    




    832040



Let's modify this so the timer runs the function multiple times and calculates the average run time:


```
def timed(fn):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / 10
        print('Avg Run time: {0:.6f}s'.format(avg_elapsed))
        return result
    
    return inner
```

And again we decorate it using the long syntax:


```
def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib)
```


```
fib(28)
```

    Avg Run time: 0.098860s
    




    317811



But that value of 10 has been hardcoded. Let's make it a parameter instead.


```
def timed(fn, num_reps):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(num_reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / num_reps
        print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                        num_reps))
        return result
    
    return inner
```

Now to decorate our Fibonacci function we **have** to use the long syntax (as we saw in the lecture, the **@** syntax will not work):


```
def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib, 5)
```


```
fib(28)
```

    Avg Run time: 0.095708s (5 reps)
    




    317811



The problem is that we cannot use the `@` decorator syntax because when using that syntax Python passes a **single** argument to the decorator: the function we are decorating - nothing else.

Of course we could just use what we did above, but the decorator syntax is kind of neat, so it would be nice to retain the ability to use it.

We just need to change our thinking a little bit to do this:

First, when we see the following syntax:

`
@dec
def my_func():
    pass
`

we see that `dec` must be a function that takes a single argument, the function being decorated.

You'll note that `dec` is just a function, but we do not **call** `dec` when we decorate `my_func`, we simply use the label `dec`.

Then Python does:

`
my_func = dec(my_func)
`

Let's try a concrete example:


```
def dec(fn):
    print ("running dec")
    
    def inner(*args, **kwargs):
        print("running inner")
        return fn(*args, **kwargs)
              
    return inner
```


```
@dec
def my_func():
    print('running my_func')
```

    running dec
    

As we can see, when we decorated `my_func`, the `dec` function was **called** at that time.

(Because Python did this: 

`my_func = dec(my_func)` 

so `dec` was called)

And when we now call `my_func`, we see that the `inner` function is called, followed by the original `my_func`


```
my_func()
```

    running inner
    running my_func
    

But what if `dec` was not the decorator itself, but instead created and returned a decorator?

Let's see how we might do this:


```
def dec_factory():
    print('running dec_factory')
    def dec(fn):
        print('running dec')
        def inner(*args, **kwargs):
            print('running inner')
            return fn(*args, **kwargs)
        return inner
    return dec
```

So as you can see, calling `dec_generator()` will return that `dec` function which is our decorator:


```
@dec_factory()
def my_func(a, b):
    print(a, b)
```

    running dec_factory
    running dec
    

You can see that both `dec_generator` and `dec` were already called.


```
my_func(10, 20)
```

    running inner
    10 20
    

And there you go, all we did is basically create a decorator by calling a function (`dec_factory`) and use the return value of that call (the `dec` function) as our actual decorator.

We could have done the decoration this way too:


```
dec = dec_factory()
```

    running dec_factory
    


```
@dec
def my_func():
    print('running my_func')
```

    running dec
    


```
my_func()
```

    running inner
    running my_func
    

Or even this way:


```
dec = dec_factory()

def my_func():
    print('running my_func')

my_func = dec(my_func)
```

    running dec_factory
    running dec
    


```
my_func()
```

    running inner
    running my_func
    

Of course we could even decorate it this way using a single statement:


```
def my_func():
    print('running my_func')

my_func = dec_factory()(my_func)
```

    running dec_factory
    running dec
    


```
my_func()
```

    running inner
    running my_func
    

OK, so now we have decorated our function using, not a decorator, but a decorator factory as follows:


```
def dec_factory():
    def dec(fn):
        def inner(*args, **kwargs):
            print('running decorator inner')
            return fn(*args, **kwargs)
        return inner
    return dec
```


```
@dec_factory()
def my_func(a, b):
    return a + b
```


```
my_func(10, 20)
```

    running decorator inner
    




    30



You should note that in this approach, we are **calling** `dec_factory()`, [note the parentheses `()`], and **then** using the return value (a decorator) to decorate our function.

So, we could pass arguments as we do so without affecting the final outcome. In fact we can even access them from anywhere inside `dec_factory`, including any of the nested functions! 

Let's try this:


```
def dec_factory(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('running decorator inner')
            print('free vars: ', a, b)  # a and b are free variables!
            return fn(*args, **kwargs)
        return inner
    return dec
```


```
@dec_factory(10, 20)
def my_func():
    print('python rocks')
```


```
my_func()
```

    running decorator inner
    free vars:  10 20
    python rocks
    

And this is how we can create decorators with parameters. We do not directly create a decorator, instead we use an outer function that returns a decorator when called, and pass arguments to that outer function, which the decorator and its inner function can of course access as nonlocal (free) variables.

So now, let's go back to our original problem where we wanted our timing decorator to run a number of loops which could be specified as a parameter when decorating the function we want to time.

Here it is again:


```
def timed(fn, num_reps):
    from time import perf_counter
    
    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(num_reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (perf_counter() - start)
        avg_elapsed = total_elapsed / num_reps
        print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                        num_reps))
        return result
    
    return inner
```

So, all we need to do is create an outer function around our timed decorator, and pass the `num_reps` argument to that outer function instead:


```
def timed_factory(num_reps=1):
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / num_reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                            num_reps))
            return result
        return inner
    return timed    
```


```
@timed_factory(5)
def fib(n):
    return calc_fib_recurse(n)
```


```
fib(30)
```

    Avg Run time: 0.249934s (5 reps)
    




    832040



Just to put the finishing touch on this, we probably don't want to have our outer function named the way it is (`timed_factory`). Instead we probably just want to call it `timed`. So lets just do this final part:


```
from functools import wraps

def timed(num_reps=1):
    def decorator(fn):
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / num_reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                            num_reps))
            return result
        return inner
    return decorator  
```


```
@timed(5)
def fib(n):
    return calc_fib_recurse(n)
```


```
fib(30)
```

    Avg Run time: 0.253744s (5 reps)
    




    832040



##  Decorator Application (Decorator Class)

If you recalls how we wrote a parameterized decorator, we had to write a decorator factory that took in the arguments for our decorator and then returned the decorator (which could reference the arguments as free variables).

Very simply:


```
def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('decorated function called: a={0}, b={1}'.format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec
```


```
@my_dec(10, 20)
def my_func(s):
    print('hello {0}'.format(s))
```


```
my_func('world')
```

    decorated function called: a=10, b=20
    hello world
    

So, our decorator factory was passed some arguments, and returned a callable which took one single parameter, the function being decorated, but also had access to the arguments passed to the factory.

Now, recall that we can make our class instances callable, simply by implementing the `__call__` method.

Here's a simple example:


```
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __call__(self):
        print('MyClass instance called: a={0}, b={1}'.format(self.a, self.b))
```


```
my_class = MyClass(10, 20)
```


```
my_class()
```

    MyClass instance called: a=10, b=20
    

So let's modify this just a bit, and have the `__call__` method be our decorator!


```
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('MyClass instance called: a={0}, b={1}'.format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner
```

So, we can decorate our functions this way:


```
@MyClass(10, 20)
def my_func(s):
    print('Hello {0}!'.format(s))
```

Remember that `@MyClass(10, 20)` returned an object of type `MyClass`. But  that object is itself callable, so we could do something like:

``
my_func = MyClass(10, 20)(my_func)
``

or, more simply

``
@MyClass(10, 20)
def my_func(s):
    print(s)
``


```
my_func('Python')
```

    MyClass instance called: a=10, b=20
    Hello Python!
    

So as you can see, we can also use callable classes to decorate functions!

##  Decorator Application: Decorating Classes

We have so far worked with decorating functions. This means we can decorate functions defined with a `def` statement (we can use the `@` syntax, or the long form). Since class methods are functions, they can be decorated too. Lambda expressions can also be decorated (using the long form).

But if you think about how our decorators work, they take a single parameter, a function, and return some other function - usually a closure that uses the original function that was passed as an argument.

We could use the same concept to accept, not a function, but a class instead. We could reference that class inside our decorator, modify it, and then return that modified class.

First we look at something called **monkey patching**. It boils down to modifying or extending our code at **run time**.

For example we can modify or add attributes to classes at run time. Modules too.

In Python, many of the classes we use can be modified at run time 
(built-ins like strings, lists, and so on, cannot).

But classes written in Python, such as the ones we write, and even library classes, as long as they are written in Python, not C, can. For example `Fraction` in the `fractions` module can be monkey patched.

Just because we can do something however, does not mean we should! Monkey patching can be extremely useful, but don't do it just because you can - as always there should be a real reason to do it, as we'll see in a bit.

Also, in general it is a bad idea to monkey patch the special methods `__???__` (such as `__len__`) as this will often not work due to how these methods are searched for by Python.


```
from fractions import Fraction
```


```
Fraction.speak = lambda self: 'This is a late parrot.'
```


```
f = Fraction(2, 3)
```


```
f
```




    Fraction(2, 3)




```
f.speak()
```




    'This is a late parrot.'



Yes, this is obviously nonsense, but you get the idea that you can add attributes to classes even if you do not have direct control over the class, or after your class has been defined.

If you want a more useful method, how about one that tells us if the Fraction is an integral number? (i.e. denominator is `1`)


```
Fraction.is_integral = lambda self: self.denominator == 1
```


```
f1 = Fraction(1, 2)
f2 = Fraction(10, 5)
```


```
f1.is_integral()
```




    False




```
f2.is_integral()
```




    True



Now, we can make this change to the class by calling a function to do it instead:


```
def dec_speak(cls):
    cls.speak = lambda self: 'This is a very late parrot.'
    return cls
```


```
Fraction = dec_speak(Fraction)
```

_(Hopefully the above code reminds you of decorators.)_


```
f = Fraction(10, 2)
```


```
f.speak()
```




    'This is a very late parrot.'



We can use that function to decorate our custom classes too, using the short **@** syntax too.


```
@dec_speak
class Parrot:
    def __init__(self):
        self.state = 'late'
```


```
polly = Parrot()
```


```
polly.speak()
```




    'This is a very late parrot.'



Using this technique we could for example add a useful *reciprocal* attribute to the Fraction class, but of course since it would probably be a one time kind of thing (how many Fraction classes are there that you will want to add a reciprocal to after all), there's no need for decorators. Decorators  are useful when they are able to be reused in more general ways.


```
Fraction.recip = lambda self: Fraction(self.denominator, self.numerator)
```


```
f = Fraction(2,3)
```


```
f
```




    Fraction(2, 3)




```
f.recip()
```




    Fraction(3, 2)



These example are quite trivial, and not very useful. 

So why bring this up? 

Because this same technique can be used for more interesting things.

As a first example, let's say you typically like to inspect various properties of an object for debugging purposes, maybe the memory address, it's current state (property values), and the time at which the debug info was generated.


```
from datetime import datetime, timezone
```


```
def debug_info(cls):
    def info(self):
        results = []
        results.append('time: {0}'.format(datetime.now(timezone.utc)))
        results.append('class: {0}'.format(self.__class__.__name__))
        results.append('id: {0}'.format(hex(id(self))))
        
        if vars(self):
            for k, v in vars(self).items():
                results.append('{0}: {1}'.format(k, v))
        
        # we have not covered lists, the extend method and generators,
        # but note that a more Pythonic way to do this would be:
        #if vars(self):
        #    results.extend('{0}: {1}'.format(k, v) 
        #                   for k, v in vars(self).items())
        
        return results
    
    cls.debug = info
    
    return cls
```


```
@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        
    def say_hi():
        return 'Hello there!'
```


```
p1 = Person('John', 1939)
```


```
p1.debug()
```




    ['time: 2018-02-09 04:44:02.893951+00:00',
     'class: Person',
     'id: 0x2dfe29a4630',
     'name: John',
     'birth_year: 1939']



And of course we can decorate other classes this way too, not just a single class:


```
@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed_mph):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed_mph = top_speed_mph
        self.current_speed = 0
    
    @property
    def speed(self):
        return self.current_speed
    
    @speed.setter
    def speed(self, new_speed):
        self.current_speed = new_speed
```


```
s = Automobile('Ford', 'Model T', 1908, 45)
```


```
s.debug()
```




    ['time: 2018-02-09 04:44:03.562898+00:00',
     'class: Automobile',
     'id: 0x2dfe29b3a58',
     'make: Ford',
     'model: Model T',
     'year: 1908',
     'top_speed_mph: 45',
     'current_speed: 0']




```
s.speed = 20
```


```
s.debug()
```




    ['time: 2018-02-09 04:44:03.898085+00:00',
     'class: Automobile',
     'id: 0x2dfe29b3a58',
     'make: Ford',
     'model: Model T',
     'year: 1908',
     'top_speed_mph: 45',
     'current_speed: 20']


Let's look at another example where decorating an entire class could be useful.

```
from math import sqrt
```


```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __repr__(self):
        return 'Point({0},{1})'.format(self.x, self.y)
```


```
p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0,0)
```


```
abs(p1)
```




    3.605551275463989




```
p1, p2
```




    (Point(2,3), Point(2,3))




```
p1 == p2
```




    False



Hmm, we probably would have expected `p1` to be equal to `p2` since it has the same coordinates. But by default Python will compare memory addresses, since our class does not implement the `__eq__` method used for `==` comparisons.


```
p2, p3
```




    (Point(2,3), Point(0,0))




```
p2 > p3
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-38-b46639986960> in <module>()
    ----> 1 p2 > p3
    

    TypeError: '>' not supported between instances of 'Point' and 'Point'


So, that class does not support the comparison operators such as `<`, `<=`, etc. 

Even `==` does not work as expected - it will use the memory address instead of using a comparison of the `x` and `y` coordinates as we might probably expect.

For the `<` operator, we need our class to implement the `__lt__` method, and for `==` we need the `__eq__` method.

Other comparison operators are supported by implementing a variety of functions such as `__le__` (`<=`), `__gt__` (`>`), `__ge__` (`>=`).

We are going to add the `__lt__` and `__eq__` methods to our Point class.

We will consider a Point object to be smaller than another one if it is closer to the origin (i.e. smaller magnitude).


```
del Point

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented
            
    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented
        
    def __repr__(self):
        return '{0}({1},{2})'.format(self.__class__.__name__, self.x, self.y)
```


```
p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0,0)
```


```
p1, p2, p1==p2
```




    (Point(2,3), Point(2,3), True)




```
p2, p3, p2==p3
```




    (Point(2,3), Point(0,0), False)



As we can see, `==` now works as expected


```
p4 = Point(1, 2)
```


```
abs(p1), abs(p4), p1 < p4
```




    (3.605551275463989, 2.23606797749979, False)



Great, so now we have `<` and `==` implemented. What about the rest of the operators: `<=`, `>`, `>=`?


```
p1 > p4
```




    True



Ooh, since we have implemented `<` and `==`, does this mean Python magically implemented a `>` operator (i.e. not < and not ==)?

Not exactly! What happened is that since `p1` and `p4` are both points, running the comparison `p1 > p4` is really the same as evaluating `p4 < p1` - and Python did do that automatically for us.

But it has not implemented any of the others, such as `>=` and `<=`:


```
p1 <= p4
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-46-80f9ea228203> in <module>()
    ----> 1 p1 <= p4
    

    TypeError: '<=' not supported between instances of 'Point' and 'Point'


Now, although we could proceed in a similar way and define `>=`, `<=` and `>` using the same technique, observe that if `<` and `==` is defined then:

* `a <= b` iff `a < b or a == b`
* `a > b` iff `not(a<b) and a != b`
* `a >= b` iff `not(a<b)`

So, to be quite generic we could create a decorator that will implement these last three operators as long as `==` and `<` are defined. We could then decorate **any** class that implements just those two operators.


```
def complete_ordering(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not(self < other) and not (self == other)
        cls.__ge__ = lambda self, other: not (self < other)
    return cls
```

In reality, the code above is **NOT** a good implementation at all. We are not checking that the types are compatible and returning a `NotImplemented` result if appropriate. I am also using inline operators (`<` and `==`) instead of the dunder functions (`__lt__` and `__eq__`). I just kept it simple because we'll use a better alternative in a bit.

For example, a better way to implement `__ge__` would be as follows:


```
def ge_from_lt(self, other):
    # self >= other iff not(other < self)
    result = self.__lt__(other)
    if result is NotImplemented:
        return NotImplemented
    else:
        return not result
```

You may be wondering why I used `__lt__` instead of just using the `<` operator. This is because I want to actually look at the result of the operation without raising an exception if the operation is not implemented. The way I have the total ordering decorator implemented could cause an infinite loop because when I evaluate `self < other`, if an exception is raised, Python will reflect the evaluation to `other > self`, and if that raises an error as well, Python will try to reflect that operation too, and we get into an infinite loop (which eventually terminates in a stack overflow). This was actually a bug in Python's standard library implementation of a `complete_ordering` decorator (called `total_ordering`) that was resolved in 3.4.


```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return NotImplemented
            
    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented
        
    def __repr__(self):
        return '{0}({1},{2})'.format(self.__class__, self.x, self.y)
```


```
Point = complete_ordering(Point)        
```


```
p1, p2, p3 = Point(1, 1), Point(3, 4), Point(3, 4)
```


```
abs(p1), abs(p2), abs(p3)
```




    (1.4142135623730951, 5.0, 5.0)




```
p1 < p2, p1 <= p2, p1 > p2, p1 >= p2, p2 > p2, p2 >= p3
```




    (True, True, False, False, False, True)



Now the `complete_ordering` decorator can also be directly applied to any class that defines `__eq__` and `__lt__`.


```
@complete_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)
     
    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)
    
    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent < other.score_percent
        else:
            return NotImplemented
        
```


```
g1 = Grade(10, 100)
g2 = Grade(20, 30)
g3 = Grade(5, 50)
```


```
g1 <= g2, g1 == g3, g2 > g3
```




    (True, True, True)



Often, given the `==` operator and just **one** of the other comparison operators (`<`, `<=`, `>`, `>=`), then all the rest can be derived.

Our decorator insisted on `==` and `<`. but we could make it better by insisting on `==` and any one of the other operators. This will of course make our decorator more complicated, and in fact, Python has this precise functionality built in to the, you guessed it, `functools` module!

It is a decorator called `total_ordering`. 

Let's see it in action:


```
from functools import total_ordering
```


```
@total_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)
     
    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)
    
    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented
    
    def __lt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent < other.score_percent
        else:
            return NotImplemented
```


```
g1, g2 = Grade(80, 100), Grade(60, 100)
```


```
g1 >= g2, g1 > g2
```




    (True, True)



Or we could also do it this way:


```
@total_ordering
class Grade:
    def __init__(self, score, max_score):
        self.score = score
        self.max_score = max_score
        self.score_percent = round(score / max_score * 100)
     
    def __repr__(self):
        return 'Grade({0}, {1})'.format(self.score, self.max_score)
    
    def __eq__(self, other):
        if isinstance(other, Grade):
            return self.score_percent == other.score_percent
        else:
            return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Grade):
            return self.score_percent > other.score_percent
        else:
            return NotImplemented
```


```
g1, g2 = Grade(80, 100), Grade(60, 100)
```


```
g1 >= g2, g1 > g2, g1 <= g2, g1 < g2
```




    (True, True, False, False)



##  Decorator Application: Single Dispatch Generic Functions

Consider an application where we want to provide similar functionality but that varies slightly depending on the argument types passed in.

In this set of examples we consider this problem where functionality differs based on a single argument's type (hence single dispatch) instead of the type of multiple arguments (which would be multi dispatch)

If you have a background in some other OO languages such as Java or C#, you'll know that we can easily do something like this by basically **overloading** functions: using a different data type for the function parameter, hence changing the function signature. Then although the name of the function is the same, calling `do_something(100)` and `do_something('java')` would call a different function, the first one would call the `do_something(int)` function, and the second would call the `do_something(String)` function.

Of course, Python is not statically typed, so even if Python had function overloading built-in, we would not be able to make such a distinction in our function signatures since there is nothing that says that a parameter must be of a specific type, so in a best case scenario we would have to "distinguish" functions with the same name only by the number of parameters they take. And then we'd have to somehow deal with variable numbers of positional and keyword arguments too... Uuugh!
In any event, single dispatch could never work.

Instead we have to come up with a different solution.

Let's say we want to display various data types in html format, with different presentations for integers (we want both base 10 and hex values), floats (we always want it rounded to 2 decimal points), strings (we want the string html-escaped, and all newline characters replaced by `<br/>`), lists and tuples should be implemented using bulleted lists, and the same with dictionaries except we want the name/value pair to be displayed in the bulleted list.

For starters, let's just implement individual functions to do each of those things.

I am going to keep the functions very simple, but in practice you should handle situations like None objects, empty lists and dictionaries, possibly the wrong type being passed to the function, etc.


```
from html import escape

def html_escape(arg):
    return escape(str(arg))
                      
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))
                                  
def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')
                                  
def html_list(l):
    items = ('<li>{0}</li>'.format(html_escape(item)) 
             for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
                                  
def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(html_escape(k), html_escape(v)) 
             for k, v in d.items())    
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
```


```
print(html_str("""this is 
a multi line string
with special characters: 10 < 100"""))
```

    this is <br/>
    a multi line string<br/>
    with special characters: 10 &lt; 100
    


```
print(html_int(255))
```

    255(<i>0xff</i)
    


```
print(html_escape(3+10j))
```

    (3+10j)
    

Ideally we would want to just have to call a single function, maybe `htmlize` that would figure out which particular flavor of the `html_xxx` function to call depending on the argument type.

We could try it as follows:


```
from decimal import Decimal

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        # default behavior - just html escape string representation
        return html_escape(str(arg))
```

Now we can essentially use the same function call to handle different types - the `htmlize` function is a dispatcher - it dispatches the request to a different function based on the argument type. (There's a much better way to do some of this, but we'll have to wait until we cover abstract base classes to do so).


```
print(htmlize([1, 2, 3]))
```

    <ul>
    <li>1</li>
    <li>2</li>
    <li>3</li>
    </ul>
    


```
print(htmlize(dict(key1=1, key2=2)))
```

    <ul>
    <li>key1=1</li>
    <li>key2=2</li>
    </ul>
    


```
print(htmlize(255))
```

    255(<i>0xff</i)
    

But there are a number of shortcomings here:


```
print(htmlize(["""first element is 
a multi-line string""", (1, 2, 3)]))
```

    <ul>
    <li>first element is 
    a multi-line string</li>
    <li>(1, 2, 3)</li>
    </ul>
    

As you can see, the multi-line string did not get the newline characters replaced, the tuple was not rendered as an html list, and the integers do not have their hex representation.

So we just need to redefine the `html_list` and `html_dict` functions to use the `htmlize` function:


```
def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
```


```
def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
```


```
print(htmlize(["""first element is 
a multi-line string""", (1, 2, 3)]))
```

    <ul>
    <li>first element is <br/>
    a multi-line string</li>
    <li><ul>
    <li>1(<i>0x1</i)</li>
    <li>2(<i>0x2</i)</li>
    <li>3(<i>0x3</i)</li>
    </ul></li>
    </ul>
    

Much better, but hopefully you spotted something that might seem problematic!

Do we not have a circular reference?

In order to define `html_list` and `html_dict` we needed to call `htmlize`, but in order to define `htmlize` we needed to call `html_list` and `html_dict`.

Remember that in Python we can reference a function **inside** the body of another function **before** the function has been defined, as long as by the time we **call** the first function, the second one has been defined. SO this is actually OK.

If you don't believe me and want to make sure of this yourself, go ahead and reset your Kernel (click on the Kernel | Restart menu option), and run the following code without running anything prior to this.

The `htmlize` function body makes calls to other functions such as `html_escape`, `html_int`, etc that have not actually been defined yet


```
from html import escape
from decimal import Decimal

def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        # default behavior - just html escape string representation
        return html_escape(str(arg))
```

Now we define all the functions that `htmlize` uses before we actually call `htmlize` and all is good:


```
def html_escape(arg):
    return escape(str(arg))
                      
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))
                                  
def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')
                                  
def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
                                  
def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
```


```
print(htmlize(["""first element is 
a multi-line string""", (1, 2, 3)]))
```

    <ul>
    <li>first element is <br/>
    a multi-line string</li>
    <li><ul>
    <li>1(<i>0x1</i)</li>
    <li>2(<i>0x2</i)</li>
    <li>3(<i>0x3</i)</li>
    </ul></li>
    </ul>
    

As you can see this works just fine.

But we still have something undesirable. You'll notice that the dispatch function `htmlize` needs to have this big `if...elif...else` statement that will just keep growing as we need to handle more and more types (including potentially custom types).

This will just get unwieldy, and not very flexible (every time someone creates a new type that has to have a special html representation they will need to go into the `htmlize` function and modify it.

So instead, we are going to try a more flexible approach using decorators.

The way we are going to approach this is to create a dispatcher function, and then separately "register" each type-specific function with the dispatcher.

First, we are going to create a decorator that will do something that may seem kind of silly - it is going to take the decorated function and store it in a dictionary, using a key consisting of the **type** `object`.

Then when the returned closure is called, the closure will call the function stored in that dictionary.


```
def singledispatch(fn):
    registry = dict()
    registry[object] = fn
    
    def inner(arg):
        return registry[object](arg)

    return inner
```


```
@singledispatch
def htmlizer(arg):
    return escape(str(arg))
```


```
htmlizer('a < 10')
```




    'a &lt; 10'



Next, we are going to add some functions to that `registry` dictionary, and modify our inner function to choose the correct function from the registry, or pick a default based on the type of the argument:


```
def singledispatch(fn):
    registry = dict()
    
    registry[object] = fn
    registry[int] = lambda arg: '{0}(<i>{1}</i)'.format(arg, str(hex(arg)))
    registry[float] = lambda arg: '{0:.2f}'.format(round(arg, 2))
    
    def inner(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)
    return inner
```


```
@singledispatch
def htmlize(a):
    return escape(str(a))
```


```
htmlize(10)
```




    '10(<i>0xa</i)'




```
htmlize(3.1415)
```




    '3.14'



Now, we want a way to add the specialized functions to the `registry` dictionary from **outside** the `singledispatch` function - to do so we will create a parametrized decorator that will (1) take the type as a parameter, and (2) return a closure that will decorate the function associated with the type:


```
def singledispatch(fn):
    registry = dict()
    
    registry[object] = fn
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
        return inner
        
    
    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)
    
    return decorator
```

But of course this is not good enough - how do we get a hold of the `register` function from outside `singledispatch`? Remember, `singledispatch` is a decorator that returns the `decorated` closure, not the `register` closure.

We can do this by adding the `register` function as an **attribute** of the `decorated` function before we return it. 

While we're at it we're also going to:

* add the `registry` dictionary as an attribute as so we can look into it to see what it contains.

* add another function that given a type will return the function associated with that type (or the default function if the type is not found in the dictionary)


```
def singledispatch(fn):
    registry = dict()
    
    registry[object] = fn
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn  # we do this so we can stack register decorators!
        return inner
   
    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)
    
    def dispatch(type_):
        return registry.get(type_, registry[object])

    decorator.register = register
    decorator.registry = registry.keys()
    decorator.dispatch = dispatch
    return decorator
```


```
@singledispatch
def htmlize(arg):
    return escape(str(arg))
```

And we can see that `htmlize` (that returned `inner`) function has an attribute called `register`:


```
htmlize.register
```




    <function __main__.singledispatch.<locals>.register>



as well as that `registry` attribute that we put in just we could see what keys are in the `registry` dictionary:


```
htmlize.registry
```




    dict_keys([<class 'object'>])



We can also ask it what function it is going to use for any specific type (currently we only have one registered, the default, for the most general `object` type):


```
htmlize.dispatch(str)
```




    object



And you'll note that the extended scope of `register` and `dispatch` is the same as the extended scope of `htmlize`.

So now we can register some functions (it will store the function with associated data type in the `registry` dictionary):


```
@htmlize.register(int)
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))
```

We can peek into the registered types:


```
htmlize.registry
```




    dict_keys([<class 'object'>, <class 'int'>])



and we can ask the decorated `htmlize` function what function it is going to use for the `int` type:


```
htmlize.dispatch(int)
```




    <function __main__.html_int>



and we can actually call it as well:


```
htmlize(100)
```




    '100(<i>0x64</i)'



The huge advantage now is that we can keep registering new handlers from anywhere in our module, or even from outside our module!


```
@htmlize.register(float)
def html_real(a):
    return '{0:.2f}'.format(round(a, 2))

@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')

@htmlize.register(tuple)
@htmlize.register(list)
def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

@htmlize.register(dict)
def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(htmlize(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
```


```
htmlize.registry
```




    dict_keys([<class 'object'>, <class 'int'>, <class 'float'>, <class 'str'>, <class 'list'>, <class 'tuple'>, <class 'dict'>])




```
print(htmlize([1, 2, 3]))
```

    <ul>
    <li>1(<i>0x1</i)</li>
    <li>2(<i>0x2</i)</li>
    <li>3(<i>0x3</i)</li>
    </ul>
    


```
print(htmlize((1, 2, 3)))
```

    <ul>
    <li>1(<i>0x1</i)</li>
    <li>2(<i>0x2</i)</li>
    <li>3(<i>0x3</i)</li>
    </ul>
    


```
print(htmlize("""this
is a multi line string with
a < 10"""))
```

    this<br/>
    is a multi line string with<br/>
    a &lt; 10
    

Our single dispatch decorator works quite well - but it has some limitations. For example it cannot handle functions that take in more than one argument (in which case dispatching would be based on the type of the **first** argument), and we also are not allowing for types based on parent classes - for example, integers and booleans are both integral numbers - i.e. they both inherit from the Integral base class. Similarly lists and tuples are both more generic Sequence types. We'll see this in more detail when we get to the topic of abstract base classes (ABC's).


```
from numbers import Integral
```


```
isinstance(100, Integral)
```




    True




```
isinstance(True, Integral)
```




    True




```
isinstance(100.5, Integral)
```




    False




```
type(100) is Integral
```




    False




```
type(True) is Integral
```




    False




```
(100).__class__
```




    int




```
(True).__class__
```




    bool



The way we have implement our decorator, if we register an Integral generic function, it won't pick up either integers or Booleans.

We can certainly fix this shortcoming ourselves, but of course...

We can can use Python's built-in single dispatch support, in ...

you guessed it!

the `functools` module.


```
from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence
```


```
@singledispatch
def htmlize(a):
    return escape(str(a))
```

The `singledispatch` returned closure has a few attributes we can use:
1. A `register` decorator (just like ours did)
2. A `registry` property that is the registry dictionary
3. A `dispatch` function that can be used to determine which registry key (registered type) it will use for the specified type.


```
@htmlize.register(Integral)
def htmlize_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a))) 
```


```
htmlize.dispatch(int)
```




    <function __main__.htmlize_int>




```
htmlize.dispatch(bool)
```




    <function __main__.htmlize_int>




```
htmlize(100)
```




    '100(<i>0x64</i)'




```
htmlize(True)
```




    'True(<i>0x1</i)'




```
@htmlize.register(Sequence)
def html_sequence(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
```


```
htmlize.dispatch(list)
```




    <function __main__.html_sequence>




```
htmlize.dispatch(tuple)
```




    <function __main__.html_sequence>




```
htmlize.dispatch(str)
```




    <function __main__.html_sequence>



You'll note that a string is also a sequence type, hence our dispatcher will call the `html_sequence` function on a string.

In fact, at this point things would not even run properly.

If we were to call

`htmlize('abc')`

we'd get an infinite recursion!

The call to `htmlize` the string `abc` would treat it as a sequence, which would call `htmlize` character by character. But each character is itself just a string of length 1, so it will `htmlize` for that single character, which would treat it as a sequence, which would call `htmlize` for that single character again, and so on, in an infinite loop. 


```
htmlize('abc')
```


    ---------------------------------------------------------------------------

    RecursionError                            Traceback (most recent call last)

    <ipython-input-57-d6479a8af936> in <module>()
    ----> 1 htmlize('abc')
    

    D:\Users\fbapt\Anaconda3\envs\deepdive\lib\functools.py in wrapper(*args, **kw)
        801 
        802     def wrapper(*args, **kw):
    --> 803         return dispatch(args[0].__class__)(*args, **kw)
        804 
        805     registry[object] = func
    

    <ipython-input-53-50c13b0d81b3> in html_sequence(l)
          1 @htmlize.register(Sequence)
          2 def html_sequence(l):
    ----> 3     items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
          4     return '<ul>\n' + '\n'.join(items) + '\n</ul>'
    

    <ipython-input-53-50c13b0d81b3> in <listcomp>(.0)
          1 @htmlize.register(Sequence)
          2 def html_sequence(l):
    ----> 3     items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
          4     return '<ul>\n' + '\n'.join(items) + '\n</ul>'
    

    ... last 3 frames repeated, from the frame below ...
    

    D:\Users\fbapt\Anaconda3\envs\deepdive\lib\functools.py in wrapper(*args, **kw)
        801 
        802     def wrapper(*args, **kw):
    --> 803         return dispatch(args[0].__class__)(*args, **kw)
        804 
        805     registry[object] = func
    

    RecursionError: maximum recursion depth exceeded


Instead, we are going to register a string handler specifically - that way we will avoid that problem entirely:


```
@htmlize.register(str)
def html_str(s):
    return escape(s).replace('\n', '<br/>\n')
```


```
htmlize.dispatch(str)
```




    <function __main__.html_str>



So, even though a string is both an `str` instance and in general a sequence type, the "closest" type will be picked by the dispatcher (again something our own implementation did not do).

This means, we have something for generic sequences, but something specific for more specialized strings.


```
htmlize('abc')
```




    'abc'



We can do the same thing with sequences - right now `html_sequence` will be used for both lists and tuples. 

But suppose we want slightly different handling of tuples:


```
@htmlize.register(tuple)
def html_tuple(t):
    items = [escape(str(item)) for item in t]
    return '({0})'.format(', '.join(items))
```


```
htmlize.dispatch(list)
```




    <function __main__.html_sequence>




```
htmlize.dispatch(tuple)
```




    <function __main__.html_tuple>




```
print(htmlize(['a', 100, 3.14]))
```

    <ul>
    <li>a</li>
    <li>100(<i>0x64</i)</li>
    <li>3.14</li>
    </ul>
    


```
print(htmlize(('a', 100, 3.14)))
```

    (a, 100, 3.14)
    

One thing of note is that we started our decoration with a `@singledispatch` decorator - you'll notice that no specific type was indicated here - and in fact this means the dispatcher will use the generic `object` type.

This means that any object type not specifically handled by our dispatcher will fall back on that `object` key - hence you can think of it as the default for the dispatcher.


```
type(None)
```




    NoneType




```
htmlize.dispatch(type(None))
```




    <function __main__.htmlize>




```
type(1+1j)
```




    complex




```
htmlize.dispatch(complex)
```




    <function __main__.htmlize>




```
type(3)
```




    int




```
htmlize.dispatch(int)
```




    <function __main__.htmlize_int>



Lastly, because the name of the individual specialized functions does not really matter to us (the dispatcher will pick the appropriate function), it is quite common for an underscore character ( \_ ) to be used for the function name - the memory address of each specialized function will be stored in the `registry` dictionary, and the function name does not matter - in fact we can even add lambdas to the registry.


```
@singledispatch
def htmlize(a):
    return escape(str(a))
```


```
@htmlize.register(int)
def _(a):
    return '{0}({1})'.format(a, str(hex(a)))
```


```
@htmlize.register(str)
def _(s):
    return escape(s).replace('\n', '<br/>\n')
```


```
htmlize.register(float)(lambda f: '{0:.2f}'.format(f))
```




    <function __main__.<lambda>>




```
htmlize.registry
```




    mappingproxy({object: <function __main__.htmlize>,
                  int: <function __main__._>,
                  str: <function __main__._>,
                  float: <function __main__.<lambda>>})



But note that the `__main__._` function for `int` and `str` are not the same functions (even tough they have the same name):


```
id(htmlize.registry[str])
```




    3104966916432




```
id(htmlize.registry[int])
```




    3104967451784



And everything works as expected:


```
htmlize(100)
```




    '100(0x64)'




```
htmlize(3.1415)
```




    '3.14'




```
print(htmlize("""this
is a multi-line string
a < 10"""))
```

    this<br/>
    is a multi-line string<br/>
    a &lt; 10
    

If this same name but different function thing has you confused, look at it this way:


```
def my_func():
    print('my_func initial')
```


```
id(my_func)
```




    3104966916296




```
f = my_func
```


```
id(f)
```




    3104966916296



So, `f` and `my_func` point to the same function in memory.

Let's go ahead and "redefine" the function `my_func`:


```
def my_func():
    print('second my_func')
```

In fact, we did not "redefine" the previous `my_func`, it still exists in memory (and `f` still points to it). Instead we have re-assigned the function that `my_func` points to:


```
id(my_func)
```




    3104966914800



But the original `my_func` is still around, and 'f' still has a reference to it:


```
id(f)
```




    3104966916296



So, we can call each one:


```
f()
```

    my_func initial
    


```
my_func()
```

    second my_func
    

But the function `__name__` have the same value:


```
f.__name__
```




    'my_func'




```
my_func.__name__
```




    'my_func'



Just always keep in mind that labels point to something in memory, it is not the object itself. So in this case we have two distinct objects (functions) which happen to have the same name, but are two very different objects - `f` points to the first one we created, and `my_func` points to the second.

# Section 08 - Tuples as Data Records

##  Tuples as Data Structures

Tuples are an immutable container type.

They contain a collection of objects. The tuple is a sequence type - this means order matters (and is preserved) and elements can be accessed by index (zero based), slicing, or iteration.

Other common sequence types in Python include lists and strings. Strings, like tuples are immutable, whereas lists are mutable.

Tuples are sometimes presented as immutable lists, but in fact, they could be compared more closely to strings with one major difference: strings are homogeneous sequences, while tuples can be heterogeneous.

A tuple literal is often presented as:


```
('a', 10, True)
```




    ('a', 10, True)



But the parentheses are not what indicate a tuple - it is the commas:


```
a = ('a', 10, True)
b = 'b', 20, False
```


```
type(a)
```




    tuple




```
type(b)
```




    tuple



Sometimes however, the parentheses are *required* to remove any ambiguity.

For example, consider this function that expects a tuple (or other iterable) as its argument:


```
def iterate(t):
    for element in t:
        print(element)
```

If we call the function this way, Python will interpret it as three arguments:


```
iterate(1, 2, 3)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-868649c3b72b> in <module>()
    ----> 1 iterate(1, 2, 3)
    

    TypeError: iterate() takes 1 positional argument but 3 were given


Instead, we now **have** to use the parentheses to indicate we are packing a tuple:


```
iterate((1, 2, 3))
```

    1
    2
    3
    

Since tuples are sequence types, we can access items by index:


```
a = 'a', 10, True
```


```
a[2]
```




    True



Or we can even slice them:


```
a = 1, 2, 3, 4, 5
a[2:4]
```




    (3, 4)



We can iterate over them:


```
a = 1, 2, 3, 4, 5
for element in a:
    print(element)
```

    1
    2
    3
    4
    5
    

We can also use unpacking:


```
point = 10, 20, 30
```


```
x, y, z = point
```


```
print(x)
print(y)
print(z)
```

    10
    20
    30
    

Tuples are immutable, in the sense that we cannot change the reference of an object in the container and we cannot add or remove objects from the container. This is the same as strings.


```
a = 10, 'python', True
```


```
a[0] = 20
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-16-90c4006d224a> in <module>()
    ----> 1 a[0] = 20
    

    TypeError: 'tuple' object does not support item assignment


We can however 'extend' tuples, but just as with strings, we are actually just creating a new tuple:


```
a = 1, 2, 3
```


```
id(a)
```




    2726988303960




```
a = a + (4, 5, 6)
```


```
a
```




    (1, 2, 3, 4, 5, 6)




```
id(a)
```




    2726964089000



As you can see we no longer have the same memory address for `a`.

We have to be careful when we think about immutability of tuples. The tuple, as a container is immutable, but the elements contained in the tuple may very well be mutable.

Let's define a simple point class to store the x and y coordinates of a point in 2D space:


```
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'
```


```
a = Point2D(0, 0), Point2D(10, 10), Point2D(20, 20)
```


```
a
```




    (Point2D(x=0, y=0), Point2D(x=10, y=10), Point2D(x=20, y=20))



Although the tuple `a` is immutable, its contained elements are mutable:

So we cannot do this:


```
a[0] = Point2D(-10, -10)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-25-e869cf518b45> in <module>()
    ----> 1 a[0] = Point2D(-10, -10)
    

    TypeError: 'tuple' object does not support item assignment


But we can modify the contents of the first element:


```
a[0].x = -10
```


```
a
```




    (Point2D(x=-10, y=0), Point2D(x=10, y=10), Point2D(x=20, y=20))



#### Tuples as Data Records

We can interpret tuples as lightweight data structures where, by convention, the position of the element in the tuple has meaning.

For example, we may elect to represent a point as a tuple, and not use the class approach we just did:


```
pt1 = (0, 0)
pt2 = (10, 10)
```

Here, we simply decide that the first position of the tuple represents the x=coordinate while the second element represents the y-coordinate of a point in 2D space.

We could also decide that we are going to represent a city using a tuple, where the first position will the city name, the second position will be the country, and the the third position will be the population:


```
london = 'London', 'UK', 8_780_000
new_york = 'New York', 'USA', 8_500_000
beijing = 'Beijing', 'China', 21_000_000
```

We can even have a list of these tuples:


```
cities = london, new_york, beijing
```

We can obtain a list of all the cities in the list using a simple list comprehension and the fact that the city name is the first element (index 0) of each tuple:


```
city_names = [t[0] for t in cities]
print(city_names)
```

    ['London', 'New York', 'Beijing']
    

We could even calculate the total population of all these cities.

We start with a simple loop to do this:


```
total = 0
for city in cities:
    total += city[2]
print (f'total={total}')
```

    total=38280000
    

You will note that the reason this worked is because the `cities` list contained **only** city tuples. The list was homogeneous. The tuples on the other hand are heterogeneous.

This is often a key difference between lists and tuples, especially when we consider tuples as data structures. The tuples are heterogeneous, while the list needs to be homogeneous so we can apoply the same calculations to each element of the list.

The above example would break if one of the elements in the `cities` list was an integer for example.

Back to our example calculating the total population. There is a more Pythonic way of doing this.

First we use a comprehension to extract just the population from each city :


```
[city[2] for city in cities]
```




    [8780000, 8500000, 21000000]



Next we simply sum up the population values:


```
sum([city[2] for city in cities])
```




    38280000



In fact (and we'll cover this in detail later in this course), we don't even need the square brackets in the sum:


```
sum(city[2] for city in cities)
```




    38280000



Now, since tuples are sequence types, and hence iterable, we can also use unpacking to extract values from the tuple:


```
city, country, population = new_york
```


```
print(city)
print(country)
print(population)
```

    New York
    USA
    8500000
    

We can also use extended unpacking:


```
record = 'DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072
```

Where the structure is: symbol, year, month, day, open, high low, close

We could then unpack the record using straight unpacking:


```
symbol, year, month, day, open_, high, low, close = record
```


```
print(symbol)
print(close)
```

    DJIA
    26072
    

But suppose we are only interested in the symbol, year, month, day and close. Then we could use extended unpacking as follows:


```
symbol, year, month, day, *others, close = record
```


```
print(symbol, year, month, day, close)
```

    DJIA 2018 1 19 26072
    


```
print(others)
```

    [25987, 26072, 25942]
    

A convetion often used in Python when we are not particularly interested in something, is to use an underscore as a variable name:


```
symbol, year, month, day, *_, close = record
```

There's nothing special about the underscore here, it's just a legal variable name (in an interactive Python session, the underscore is actually used to store the results of the last calculation)


```
print(_)
```

    [25987, 26072, 25942]
    

By the way do not write code like this to do the unpacking we just did:


```
symbol, year, close = record[0], record[1], record[7]
```

Although this works, it is not very readable code, plus you are packing a new tuple (the right hand side) and then unpacking it into the variables on the left. Much better to do this:


```
symbol, year, *_, close = record
```

If you only need to pick a few elements out of the tuple (like in our example where we just wanted the population to sum it up), then by all means access it directly using the index.

But did you know that you can also unpack tuples directly in the loop?


```
for element in cities:
    print(element)
```

    ('London', 'UK', 8780000)
    ('New York', 'USA', 8500000)
    ('Beijing', 'China', 21000000)
    

As you can see, each element is a tuple, and we can actually unpack it at the same time as the loop this way:


```
for city, country, population in cities:
    print(f'city={city}, population={population}')
```

    city=London, population=8780000
    city=New York, population=8500000
    city=Beijing, population=21000000
    

This, by the way, is how we can use the `enumerate` function in Python. The enumerate function produces an iterable from another iterable but contains the index number. Values are returned as tuples, where the first position is the index value, and the second position is the value (here we also see how a tuple was used as a data structure). So that tuple can be unpacked as follows:


```
for index, value in enumerate(beijing):
    print(f'{index}: {value}')
```

    0: Beijing
    1: China
    2: 21000000
    

Of course, since we are not interested in the country in this case, we might write it this way as well:


```
for city, _, population in cities:
    print(f'city={city}, population={population}')
```

    city=London, population=8780000
    city=New York, population=8500000
    city=Beijing, population=21000000
    

Another frequent application of usign tuples as data structures is for returning multiple values from a function.


```
from random import uniform
from math import sqrt

def random_shot(radius):
    '''Generates a random 2D coordinate within 
    the bounds [-radius, radius] * [-radius, radius]
    (a square of area 4)
    and also determines if it falls within 
    a circle centered at the origin 
    with specified radius'''
    
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False
    
    return random_x, random_y, is_in_circle
```


```
num_attempts = 1_000_000
count_inside = 0
for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

print(f'Pi is approximately: {4 * count_inside / num_attempts}')
```

    Pi is approximately: 3.14294
    

##  Named Tuples

The ``namedtuple`` function in ``collections`` allows us to create a tuple that also has names attached to each field (aka property). This can be handy to reference data in the tuple structure by name instead of just relying on position.

The ``namedtuple`` function is basically a class factory that creates a new type of class that uses a tuple as its underlying data storage (in fact, named tuples inherit from `tuple`), but layers in field names to each position and makes a property out of the field name.

The ``namedtuple`` function creates a **class**, and we then use that class to instantiate our instances of named tuples.

To use the ``namedtuple`` function we therefore need to select a class **name**, as well as indicate the **property** names, in the order in which they will be stored and accessed in the tuple.

Note that a ``namedtuple``, like the regular ``tuple`` is an **immutable** data structure. (In fact, named tuples inherit from tuples - we'll revisit this in our section on metaclasses)

If you find yourself writing code such as:


```
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
```

Forget it! You seriously need to use named tuples! Not only can you shorten the amount of code you need to write, but you get some additional functionality for "free", such as `__repr__` and `__eq__` that you do not have to implement yourself!

#### Creating Named Tuples

We are going to create a ``Point`` named tuple that will contain an x-coordinate and a y-coordinate.


```
from collections import namedtuple
```


```
Point2D = namedtuple('Point2D', ('x', 'y'))
```

Note that we have two different uses of `Point2D` here. The label we are assigning the return value of the call to ``namedtuple`` and the **name** of the class generated by calling ``namedtuple``.

We could also have done the following:


```
Pt = namedtuple('Point2D', ('x', 'y'))
```

The ``namedtuple`` class name is `Point2D`, but the label we `Pt` simply points to that class, so we would then create instances of the `Point2D` class as follows:


```
pt1 = Pt(10, 20)
```

And we can see what `pt1` is:


```
pt1
```




    Point2D(x=10, y=20)



As you can see we have an object of type `Point2D`, and it has two properties, `x` and `y` with respective values `10` and `20`.

The only weird thing here is that we are using `Pt` to generate our instances of the `Point2D` class.

That's why we usually always created `namedtuple` generated classes this way:


```
Point2D = namedtuple('Point2D', ('x', 'y'))
```

Then the following makes more sense:


```
pt1 = Point2D(10, 20)
```


```
pt1
```




    Point2D(x=10, y=20)



This is not different than doing this:


```
Pt3 = Point3D  # class we defined earlier
```


```
pt3 = Pt3(10, 20, 30)
```


```
pt3
```




    <__main__.Point3D at 0x27408e1fa90>



As you can see above, we used another label `Pt3` as a label that also references the `Point3D` class. It would be weird to do it this way here, and its weird for tuples as well. Of course, you may run into circumstances where you need to do this - just not as a general rule.

Note that all named tuples  are honest to goodness **classes**, just as if you had used a `class` definition such as with `Point3D`. 

The `namedtuple` function **generates** classes for us - it is a **class factory**.


```
type(Point3D)
```




    type




```
type(Point2D)
```




    type



However, `Point2D` is a subclass of `tuple`, while `Point3D` is not:


```
isinstance(pt1, tuple)
```




    True




```
isinstance(pt3, tuple)
```




    False



So, when we create an instance of a class, we are in fact calling the `__new__` method with our initial values. It's just a callable that has the **field names** we used to generate our named tuple class as its parameters. This means we can use keyword arguments when instantiating our named tuples!


```
pt4 = Point2D(y=20, x=10)
```


```
pt4
```




    Point2D(x=10, y=20)



#### What did we get for free using a named tuple vs our own class?

First using a named tuple for our 2D point:


```
pt2d_1 = Point2D(10, 20)
pt2d_2 = Point2D(10, 20)
```


```
pt2d_1
```




    Point2D(x=10, y=20)




```
pt2d_1 == pt2d_2
```




    True



Now using our 3D class:


```
pt3d_1 = Point3D(10, 20, 30)
pt3d_2 = Point3D(10, 20, 30)
```


```
pt3d_1
```




    <__main__.Point3D at 0x27408e1f9e8>



Oh, we probably need to implement the `__repr__` method in our class


```
pt3d_1 == pt3d_2
```




    False



And we would also need to implement the __eq__ method!

Let's do that:


```
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f"Point3D(x={self.x}, y={self.y}, z={self.z})"
    
    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False
```


```
pt3d_1 = Point3D(10, 20, 30)
pt3d_2 = Point3D(10, 20, 30)
```


```
pt3d_1
```




    Point3D(x=10, y=20, z=30)




```
pt3d_1 == pt3d_2
```




    True



How about finding the largest coordinate in the point?

That's easy for `Point2D` since it is a tuple, but not the case for `Point3D`:


```
max(pt2d_1)
```




    20




```
max(pt3d_1)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-30-e803e2758ff1> in <module>()
    ----> 1 max(pt3d_1)
    

    TypeError: 'Point3D' object is not iterable


How about calculating the dot product of two points (considering them as vectors starting at the origin)?

The formula would be:
a.b = a.x * b.x + a.y + b.y + a.z * b.z

For the 3D point we would need to do the following:


```
def dot_product_3d(a, b):
    return a.x * b.x + a.y * b.y + a.z + b.z
```


```
dot_product_3d(pt3d_1, pt3d_2)
```




    560



But for our 2D point, which, remember is a tuple as well, we can write a generic function that would work equally well with a 3D named tuple too:


```
def dot_product(a, b):
    return sum(e[0] * e[1] for e in  zip(a, b))
```

Here's a break down of how we implemented the dot product:

First we zip up the components of `a` and `b` to get an iterable of tuples containing the x-coordinates in the 1st element, and the y-coordinates in the second tuple. Our zip will contain as many elements as there are dimensions.


```
a = Point2D(1, 2)
b = Point2D(10, 20)
print(a)
print(b)
print(tuple(a))
print(tuple(b))
print(list(zip(a, b)))
```

    Point2D(x=1, y=2)
    Point2D(x=10, y=20)
    (1, 2)
    (10, 20)
    [(1, 10), (2, 20)]
    

Note that if we had more dimensions this would work equally well.

Suppose we had 3 dimensions:


```
u = (1, 2, 3)
v = (10, 20, 30)
list(zip(u, v))
```




    [(1, 10), (2, 20), (3, 30)]



Then we create a comprehension that multiplies the components together:


```
[e[0] * e[1] for e in zip(a, b)]
```




    [10, 40]



Then we simply add those up:


```
sum([e[0] * e[1] for e in zip(a, b)])
```




    50




```
dot_product(a, b)
```




    50



And if we defined a 4D point named tuple:


```
Point4D = namedtuple('Point4D', ['i', 'j', 'k', 'l'])
```


```
pt4d_1 = (1, 1, 1, 10)
pt4d_2 = (2, 2, 2, 10)
```


```
dot_product(pt4d_1, pt4d_2)
```




    106



As you can see we got the correct dot product. We could not have done this using our `Point3D` class!

#### Other Ways to Specify Field Names

There are a number of ways we can specify the field names for the named tuple:

* we can provide a sequence of strings containing each property name
* we can provide a single string with property names separated by whitespace or a comma


```
Circle = namedtuple('Circle', ['center_x', 'center_y', 'radius'])
```


```
circle_1 = Circle(0, 0, 10)
circle_2 = Circle(center_x=10, center_y=20, radius=100)
```


```
circle_1
```




    Circle(center_x=0, center_y=0, radius=10)




```
circle_2
```




    Circle(center_x=10, center_y=20, radius=100)



Or we can do it this way:


```
City = namedtuple('City', 'name country population')
```


```
new_york = City('New York', 'USA', 8_500_000)
```


```
new_york
```




    City(name='New York', country='USA', population=8500000)



This would work equally well:


```
Stock = namedtuple('Stock', 'symbol, year, month, day, open, high, low, close')
```


```
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
```


```
djia
```




    Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)



In fact, since whitespace can be used we can even use a multi-line string!


```
Stock = namedtuple('Stock', '''symbol
                               year month day
                               open high low close''')
```


```
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
```


```
djia
```




    Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)



#### Accessing Items in a Named Tuple

The major advantage of named tuples are that, as the name suggests, we can access the properties (fields) of the tuple by name:


```
pt1
```




    Point2D(x=10, y=20)




```
pt1.x
```




    10




```
circle_1
```




    Circle(center_x=0, center_y=0, radius=10)




```
circle_1.radius
```




    10



Now named tuples *are* tuples, so elements can be accessed by index, unpacked, and iterated.


```
circle_1[2]
```




    10




```
for item in djia:
    print(item)
```

    DJIA
    2018
    1
    25
    26313
    26458
    26260
    26393
    

We can also unpack named tuples just like ordinary tuples:


```
pt1
```




    Point2D(x=10, y=20)




```
x, y = pt1
```


```
print(x, y)
```

    10 20
    

We can also use extended unpacking:


```
djia
```




    Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)




```
symbol, *_, close = djia
```


```
print(symbol, close)
```

    DJIA 26393
    

And remember that the `_` we use in the unpacking is just a regular variable:


```
print(_)
```

    [2018, 1, 25, 26313, 26458, 26260]
    

The field names for these named tuples can be any valid variable name **except** that they cannot start with an underscore. 

For example the following would not be valid:


```
Person = namedtuple('Person', ['firstname', 'lastname', '_age', 'ssn'])
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-68-cc651156ccc1> in <module>()
    ----> 1 Person = namedtuple('Person', ['firstname', 'lastname', '_age', 'ssn'])
    

    D:\Users\fbapt\Anaconda3\envs\deepdive\lib\collections\__init__.py in namedtuple(typename, field_names, verbose, rename, module)
        409         if name.startswith('_') and not rename:
        410             raise ValueError('Field names cannot start with an underscore: '
    --> 411                              '%r' % name)
        412         if name in seen:
        413             raise ValueError('Encountered duplicate field name: %r' % name)
    

    ValueError: Field names cannot start with an underscore: '_age'


We can also choose to let the `namedtuple` function replace invalid field names automatically for us, by using the keyword argument `rename`. When we set that argument to `True` (it is `False` by default) it will replace the invalid name using the position (index) of the field, preceded by an underscore:


```
Person = namedtuple('Person', ['firstname', 'lastname', '_age', 'ssn'], rename=True)
```


```
eric = Person('Eric', 'Idle', 42, 'unknown')
```


```
eric
```




    Person(firstname='Eric', lastname='Idle', _2=42, ssn='unknown')



As you can see the invalid field name `_y` was replaced by `_1` since it was the second element (i.e. index of `1`)

#### Named Tuple Internals

We can easily find out the fields in a named tuple using the `_fields` property:


```
Point2D._fields
```




    ('x', 'y')




```
Stock._fields
```




    ('symbol', 'year', 'month', 'day', 'open', 'high', 'low', 'close')



There is also a property, `_source` that allows us to see exactly the class that was generated by calling `namedtuple` (remember that `namedtuple` is a class **factory**):


```
print(Point2D._source)
```

    from builtins import property as _property, tuple as _tuple
    from operator import itemgetter as _itemgetter
    from collections import OrderedDict
    
    class Point2D(tuple):
        'Point2D(x, y)'
    
        __slots__ = ()
    
        _fields = ('x', 'y')
    
        def __new__(_cls, x, y):
            'Create new instance of Point2D(x, y)'
            return _tuple.__new__(_cls, (x, y))
    
        @classmethod
        def _make(cls, iterable, new=tuple.__new__, len=len):
            'Make a new Point2D object from a sequence or iterable'
            result = new(cls, iterable)
            if len(result) != 2:
                raise TypeError('Expected 2 arguments, got %d' % len(result))
            return result
    
        def _replace(_self, **kwds):
            'Return a new Point2D object replacing specified fields with new values'
            result = _self._make(map(kwds.pop, ('x', 'y'), _self))
            if kwds:
                raise ValueError('Got unexpected field names: %r' % list(kwds))
            return result
    
        def __repr__(self):
            'Return a nicely formatted representation string'
            return self.__class__.__name__ + '(x=%r, y=%r)' % self
    
        def _asdict(self):
            'Return a new OrderedDict which maps field names to their values.'
            return OrderedDict(zip(self._fields, self))
    
        def __getnewargs__(self):
            'Return self as a plain tuple.  Used by copy and pickle.'
            return tuple(self)
    
        x = _property(_itemgetter(0), doc='Alias for field number 0')
    
        y = _property(_itemgetter(1), doc='Alias for field number 1')
    
    
    

And of course this will be slightly different for another named tuple generated class:


```
print(Person._source)
```

    from builtins import property as _property, tuple as _tuple
    from operator import itemgetter as _itemgetter
    from collections import OrderedDict
    
    class Person(tuple):
        'Person(firstname, lastname, _2, ssn)'
    
        __slots__ = ()
    
        _fields = ('firstname', 'lastname', '_2', 'ssn')
    
        def __new__(_cls, firstname, lastname, _2, ssn):
            'Create new instance of Person(firstname, lastname, _2, ssn)'
            return _tuple.__new__(_cls, (firstname, lastname, _2, ssn))
    
        @classmethod
        def _make(cls, iterable, new=tuple.__new__, len=len):
            'Make a new Person object from a sequence or iterable'
            result = new(cls, iterable)
            if len(result) != 4:
                raise TypeError('Expected 4 arguments, got %d' % len(result))
            return result
    
        def _replace(_self, **kwds):
            'Return a new Person object replacing specified fields with new values'
            result = _self._make(map(kwds.pop, ('firstname', 'lastname', '_2', 'ssn'), _self))
            if kwds:
                raise ValueError('Got unexpected field names: %r' % list(kwds))
            return result
    
        def __repr__(self):
            'Return a nicely formatted representation string'
            return self.__class__.__name__ + '(firstname=%r, lastname=%r, _2=%r, ssn=%r)' % self
    
        def _asdict(self):
            'Return a new OrderedDict which maps field names to their values.'
            return OrderedDict(zip(self._fields, self))
    
        def __getnewargs__(self):
            'Return self as a plain tuple.  Used by copy and pickle.'
            return tuple(self)
    
        firstname = _property(_itemgetter(0), doc='Alias for field number 0')
    
        lastname = _property(_itemgetter(1), doc='Alias for field number 1')
    
        _2 = _property(_itemgetter(2), doc='Alias for field number 2')
    
        ssn = _property(_itemgetter(3), doc='Alias for field number 3')
    
    
    

#### Converting Named Tuples to Dictionaries

The `namedtuple` generated class also provides us an instance method, `_asdict()` that will create a dictionary from all the fields in the named tuple:


```
eric._asdict()
```




    OrderedDict([('firstname', 'Eric'),
                 ('lastname', 'Idle'),
                 ('_2', 42),
                 ('ssn', 'unknown')])



Technically, it is an `OrderedDict` which we will cover in later section. Basically an `OrderedDict` is a dictionary that, unlike the standard built-in `Dictionary` is **guaranteed** to preserve the order of the keys.

[**Note** that as of Python 3.6, regular dictionaries **do** preserve the order of the keys, but until just recently it was not **guaranteed** and was bascially an implementation detail.

**However, this has now changed!!** Guido van Rossum has now agreed that this is no longer an implementation detail, and starting in Python 3.7 dictionary order is guaranteed. Since it is actually already the case in Python 3.6, you can now safely assume this fact - as long as you are running your code under Python 3.6 or higher. Your code will break if you rely on dictionary order prior to 3.6, in that case, still use an `OrderedDict`]

#### Overhead of Named Tuples

At this point you may be wondering whether there's more overhead to using a named tuple vs a regular tuple.

There is, but it is tiny. The field names are stored in the **class**, not every instance of the named tuples.
This means that the overhead incurred by the field names for one instance of the named tuple vs 1000 instances is the same. Otherwise, the instances are tuples, so you can access contained objects using indexing, slicing and iteration just as if it were a plain tuple. No overhead there either. Looking up values by name do have some overhead of course, but no more than if you had created a custom class.

##  Named Tuples - Modifying and Extending


```
from collections import namedtuple
```


```
Point2D = namedtuple('Point2D', 'x y')
```

The objects generated by `namedtuple` generated classes are **immutable**.

In other words the following will not work:


```
origin = Point2D(10,0)
```


```
origin.x = 0
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-4-ebd2d3bb5d60> in <module>()
    ----> 1 origin.x = 0
    

    AttributeError: can't set attribute


However, we may want to "change" the value of one of the coordinates of our `origin` variable.

This is just like strings, we have to create a new version of the tuple, and assign it to the same label.

Suppose we want to change the x-coordinate of our `origin` to something else, but retain whatever the y-coordinate was.

We could do it as follows:


```
origin = Point2D(0, origin.y)
```


```
origin
```




    Point2D(x=0, y=0)



Of course this could become quite unwieldy when we have a larger number of properties and we only need to change a single item:


```
Stock = namedtuple('Stock', 'symbol year month day open high low close')
```


```
djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
```

To update the `close` property for example, we could write:


```
djia = Stock(djia.symbol, djia.year, djia.month, djia.day, 
                  djia.open, djia.high, djia.low, 26_394)
```

Now that was quite painful!

We can be a bit more clever about this and use tuple unpacking and argument unpacking as follows:


```
*values, _ = djia
```

We didn't care about the `close` price since we are replacing it, hence the underscore variable name.

And we now have everything else in a list:


```
values
```




    ['DJIA', 2018, 1, 25, 26313, 26458, 26260]



And now we are going to use the `*` again, but this time to unpack the list into separate arguments when we call the `Stock` initializer:


```
djia = Stock(*values, 26_393)
```


```
djia
```




    Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)



This is much better than our first attempt!

But this approach does not always work, what happens if we want to change a values somewhere in the middle? Or two values?

We cannot do: 
`*first, month, *last = djia`

That would make no sense whatsoever! (and Python will tell you so!)

Maybe slicing and unpacking can work here...


```
djia
```




    Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)



We could try **slicing**:


```
djia[:3]
```




    ('DJIA', 2018, 1)




```
djia[:3] + (26,) + djia[4:]
```




    ('DJIA', 2018, 1, 26, 26313, 26458, 26260, 26393)



So now we could use this to create a new StockPrice instance:


```
djia2 = Stock(*(djia[:3] + (26,) + djia[4:]))
```


```
djia2
```




    Stock(symbol='DJIA', year=2018, month=1, day=26, open=26313, high=26458, low=26260, close=26393)



This works, but that's quite cumbersome...

And it gets worse - suppose we want to modify the year and day using this approach:


```
djia
```




    Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)




```
values = djia[0:1] + (2019,) + djia[2:3] + (26,) + djia[4:]
```


```
values
```




    ('DJIA', 2019, 1, 26, 26313, 26458, 26260, 26393)




```
djia3 = Stock(*values)
```


```
djia3
```




    Stock(symbol='DJIA', year=2019, month=1, day=26, open=26313, high=26458, low=26260, close=26393)



Or, if you want to avoid unpacking the `values` into the multiple positional arguments required by the `Stock` constructor, we can make us of the `_make` class method that can use an iterable:


```
djia4 = Stock._make(values)
```


```
djia4
```




    Stock(symbol='DJIA', year=2019, month=1, day=26, open=26313, high=26458, low=26260, close=26393)



This is really getting too complex.

Fortunately there's a better way!

The namedtuple implementation also provides another instance method called `_replace` which takes keyword-only arguments. That method will make a copy of the current tuple and substitute property values based on the keyword-only arguments passed in.


```
djia
```




    Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)




```
id(djia)
```




    2785020879400




```
djia5 = djia._replace(year=2019, day=26)
```


```
djia5
```




    Stock(symbol='DJIA', year=2019, month=1, day=26, open=26313, high=26458, low=26260, close=26393)




```
djia
```




    Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)




```
id(djia5)
```




    2785020880480



Much better!!

#### Extending Named Tuples

Sometimes we may want to add one or more properties to an existing class without modifying the code for the custom class itself.

Using inheritance is one way to go about it so you may be tempted to do this with named tuples as well, but it's not easy, and there's a cleaner way to do this if all you're after is additional data fields.

Let's say we have a Point class that is for 2D problems:


```
Point2D = namedtuple('Point2D', 'x y')
```

We could easily create a 3D point class as follows:


```
Point3D = namedtuple('Point3D', 'x y z')
```

But if our named tuple has many fields, such as our `Stock` named tuple that's a little more difficult:


```
djia
```




    Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)



Suppose we want to create a new class, say `StockExt`, it would take some effort:


```
StockExt = namedtuple('StockExt', 
                      '''symbol year month day open high low 
                      close previous_close''')
```

Instead we can leverage that `_fields` property:


```
Stock._fields
```




    ('symbol', 'year', 'month', 'day', 'open', 'high', 'low', 'close')



Remember that the `namedtuple` initializer can handle a list or tuple containing the field names. For example, the one we just retrieved from `_fields`.

Now all we need to do is create a new tuple that contains those fields along with whatever extras we want:


```
new_fields = Stock._fields + ('previous_close',)
```


```
new_fields
```




    ('symbol',
     'year',
     'month',
     'day',
     'open',
     'high',
     'low',
     'close',
     'previous_close')



And now we can create our new named tuple this way:


```
StockExt = namedtuple('StockExt', Stock._fields + ('previous_close',))
```


```
StockExt._fields
```




    ('symbol',
     'year',
     'month',
     'day',
     'open',
     'high',
     'low',
     'close',
     'previous_close')



If you did not want to use tuple concatenation for some reason, you could also do it using strings:


```
' '.join(Stock._fields) + ' previous_close'
```




    'symbol year month day open high low close previous_close'




```
StockExt = namedtuple('StockExt', 
                      ' '.join(Stock._fields) + ' previous_close')
```


```
StockExt._fields
```




    ('symbol',
     'year',
     'month',
     'day',
     'open',
     'high',
     'low',
     'close',
     'previous_close')



Now, with this newly extended class, we may want to take one of the "old" named tuple instance (`djia`) and create the extended version of it using the `StockExt` class.

This is also quite simple to do, since named tuples are tuples, and can therefore be unpacked in the arguments of a function call.


```
djia
```




    Stock(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393)




```
djia_ext = StockExt(*djia, 25_000)
```


```
djia_ext
```




    StockExt(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393, previous_close=25000)



or, we can use the `_make` method:


```
djia_ext = StockExt._make(djia + (25_000, ))
```


```
djia_ext
```




    StockExt(symbol='DJIA', year=2018, month=1, day=25, open=26313, high=26458, low=26260, close=26393, previous_close=25000)



##  Named Tuples - DocStrings and Default Values


```
from collections import namedtuple
```

#### Adding DocStrings to Named Tuples

This is easy to do, both with the generated class, as well as it's properties.


```
Point2D = namedtuple('Point2D', 'x y')
```


```
Point2D.__doc__ = 'Represents a 2D Cartesian coordinate'
```

And we can even add docstrings to the properties:


```
Point2D.x.__doc__ = 'x-coordinate'
Point2D.y.__doc__ = 'y-coordinate'
```


```
help(Point2D)
```

    Help on class Point2D in module __main__:
    
    class Point2D(builtins.tuple)
     |  Represents a 2D Cartesian coordinate
     |  
     |  Method resolution order:
     |      Point2D
     |      builtins.tuple
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __getnewargs__(self)
     |      Return self as a plain tuple.  Used by copy and pickle.
     |  
     |  __repr__(self)
     |      Return a nicely formatted representation string
     |  
     |  _asdict(self)
     |      Return a new OrderedDict which maps field names to their values.
     |  
     |  _replace(_self, **kwds)
     |      Return a new Point2D object replacing specified fields with new values
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  _make(iterable, new=<built-in method __new__ of type object at 0x00000000595CB160>, len=<built-in function len>) from builtins.type
     |      Make a new Point2D object from a sequence or iterable
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(_cls, x, y)
     |      Create new instance of Point2D(x, y)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  x
     |      x-coordinate
     |  
     |  y
     |      y-coordinate
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  _fields = ('x', 'y')
     |  
     |  _source = "from builtins import property as _property, tupl..._itemget...
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.tuple:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(self, key, /)
     |      Return self[key].
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __hash__(self, /)
     |      Return hash(self).
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.n
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __rmul__(self, value, /)
     |      Return self*value.
     |  
     |  count(...)
     |      T.count(value) -> integer -- return number of occurrences of value
     |  
     |  index(...)
     |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
     |      Raises ValueError if the value is not present.
    
    

#### Adding Default Values to Named Tuples

#### Using a Prototype

This technique is in the Python docs, and uses the concept of creating a prototype object that has the default values set:


```
Vector = namedtuple('Vector', 'x1 y1 x2 y2 origin_x origin_y')
```


```
vector_zeroorigin = Vector(x1=None, y1=None, x2=None, y2=None, origin_x=0, origin_y=0)
```


```
vector_zeroorigin
```




    Vector(x1=None, y1=None, x2=None, y2=None, origin_x=0, origin_y=0)



The named tuple `vector_zeroorigin` is now a prototype of a vector with zero origin.

To create new vectors using that origin as a default, we no longer use the `Vector` class, but instead use `_replace` as follows:


```
v1 = vector_zeroorigin._replace(x1=1, y1=1, x2=10, y2=10)
```


```
v1
```




    Vector(x1=1, y1=1, x2=10, y2=10, origin_x=0, origin_y=0)



This certainly works, and can be useful in cases where you may want more than one prototype (e.g. `vector_zeroorigin` and `vector_otherorigin`)

#### Using `__defaults__`

There is an alternative way of doing this. And, in my opinion, a much cleaner alternative.

In Python the default values for a function's parameters are stored as a tuple in the `__defaults__` attribute.




```
def func(a, b=20, c=30):
    print(a, b, c)
```


```
func.__defaults__
```




    (20, 30)




```
func(10)
```

    10 20 30
    

But the `__defaults__` property is writable:


```
func.__defaults__ = (200, 300)
```


```
func(10)
```

    10 200 300
    

In this case, the function we are interested in specifying default values for, is the named tuple class constructor, i.e. `__new__`.

So, we will simply need to set `Vector.__new__.__defaults__` to the desired tuple of default values.

The only thing to note is that if you specify less default values (say `m` values) than the total number of arguments (say `n` values, where `m < n`), then the defaults will apply to the **last** `m` values. Think of it as writing out your field names and default values on two lines, and right-aligning them. (If you specify more, then the values at the beginning are effectively ignored)


```
Vector.__new__.__defaults__ = (0, 0)
```

Here I am basically setting default values for the last two elements only, i.e. `origin_x` and `origin_y`.


```
v1 = Vector(0, 0, 10, 10, -10, -10)
```


```
v1
```




    Vector(x1=0, y1=0, x2=10, y2=10, origin_x=-10, origin_y=-10)




```
v2 = Vector(5, 5, 20, 20)
```


```
v2
```




    Vector(x1=5, y1=5, x2=20, y2=20, origin_x=0, origin_y=0)




```
v3 = Vector(x1=1, y1=1, x2=10, y2=10)
```


```
v3
```




    Vector(x1=1, y1=1, x2=10, y2=10, origin_x=0, origin_y=0)



An even simpler way to set default values if you want **all** the defaults to be the same:


```
Vector.__new__.__defaults__ = (0,) * len(Vector._fields)
```


```
v5 = Vector()
```


```
v5
```




    Vector(x1=0, y1=0, x2=0, y2=0, origin_x=0, origin_y=0)



Of course, the usual admonishment of not using mutable default values holds here as well.

##  Named Tuples - Application - Alternative to Dictionaries

First an important caveat: all this really only works for dictionaries with **string** keys. Dictionary keys can be other hashable data types, (including tuples, as long as they contain hashable types in turn), and these examples will not work with those types of dictionaries.


```
from collections import namedtuple
```


```
data_dict = dict(key1=100, key2=200, key3=300)
```


```
Data = namedtuple('Data', data_dict.keys())
```


```
Data._fields
```




    ('key1', 'key2', 'key3')



Now we can create an instance of the `Data` named tuple using the data in the `data_dict` dictionary. 

We could try the following (bad idea):


```
d1 = Data(*data_dict.values())
```


```
d1
```




    Data(key1=100, key2=200, key3=300)



This looks like it worked. 

But consider this second dictionary, where we do not create the keys in the same order:


```
data_dict_2 = dict(key1=100, key3=300, key2=200)
```


```
d2 = Data(*data_dict_2.values())
```


```
d2
```




    Data(key1=100, key2=300, key3=200)



Obviously this went terribly wrong!

We cannot guarantee that the order of `values()` will be in the same order as the keys (in our named tuple and in the dictionary).

Instead, we should unpack the dictionary itself, resulting in keyword arguments that will be passed to the `Data` constructor:


```
d2 = Data(**data_dict_2)
```


```
d2
```




    Data(key1=100, key2=200, key3=300)



So, the pattern to create a named tuple out of a single dictionary is straightforward:

For any dictionary `d` we can created a named tuple class and insert the data into it as follows:

`1. Struct = namedtuple('Struct', d.keys())`

`2. data = Struct(**d)`

Because dictionaries now preserve key order, the order of the fields in the named tuple structure will be the same. If you want your fields to be sorted in a different way, just sort the keys when you create the named tuple class. For example, to have keys sorted alphabetically we could do:


```
data_dict = dict(first_name='John', last_name='Cleese', age=42, complaint='dead parrot')
```


```
data_dict.keys()
```




    dict_keys(['first_name', 'last_name', 'age', 'complaint'])




```
sorted(data_dict.keys())
```




    ['age', 'complaint', 'first_name', 'last_name']




```
Struct = namedtuple('Struct', sorted(data_dict.keys()))
```


```
Struct._fields
```




    ('age', 'complaint', 'first_name', 'last_name')



Of course we can still put in the correct values from the dictionary into the correct slots in the tuple by unpacking the dictionary instead of just the values:


```
d1 = Struct(**data_dict)
```


```
d1
```




    Struct(age=42, complaint='dead parrot', first_name='John', last_name='Cleese')



And of course, since this is now a named tuple we can access the data using the field name:


```
d1.complaint
```




    'dead parrot'



instead of how we would have done it with the dictionary:


```
data_dict['complaint']
```




    'dead parrot'



I also want to point out that with dictionaries we often end up with code where the key is stored in some variable and then referenced this way:


```
key_name = 'age'
data_dict[key_name]
```




    42



We cannot use this approach directly with named tuples however. For example this will not work:


```
key_name = 'age'
d1.key_name
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-54-f110bbdbc0a7> in <module>()
          1 key_name = 'age'
    ----> 2 d1.key_name
    

    AttributeError: 'Struct' object has no attribute 'key_name'


However, we can use the `getattr` function that we have seen before:


```
key_name = 'age'
getattr(d1, key_name)
```




    42



We also have the `get` method on dictionaries that can specify a default value to return if the key does not exist:


```
data_dict.get('age', None), data_dict.get('invalid_key', None)
```




    (42, None)



And we can do the same with the `getattr` function:


```
getattr(d1, 'age', None), getattr(d1, 'invalid_field', None)
```




    (42, None)



Now this is not very useful if you are only working with a single instance of a dictionary that has the same set of keys. Kind of pointless really.

You also do not want to create a new named tuple for every instance of a dictionary - that would just be way too much overhead.

But in cases where you have a collection of dictionaries that share a common set of keys, this can be really useful, as long as you are willing to live with the fact that you now have immutable structures.

Let's suppose we have this data list:


```
data_list = [
    {'key1': 1, 'key2': 2},
    {'key1': 3, 'key2': 4},
    {'key1': 5, 'key2': 6, 'key3': 7},
    {'key2': 100}
]
```

The first thing to note is that we need to figure out all the possible keys that have been used in the dictionaries in this list.

The easiest way to do this is to extract all the keys of all the dictionaries and then make a `set` out of them, to eliminate duplicate key names:

We could do it this way, using a simple loop:


```
keys = set()
for d in data_list:
    for key in d.keys():
        keys.add(key)
```


```
keys
```




    {'key1', 'key2', 'key3'}



But actually a more efficient way would be to use a comprehension:


```
keys = {key for dict_ in data_list for key in dict_.keys()}
```


```
keys
```




    {'key1', 'key2', 'key3'}



In fact, we can also use the fact that we can union multiple sets (we'll cover this in detail later) by unpacking all the keys and creating a union of them:


```
keys = set().union(*(dict_.keys() for dict_ in data_list))
```


```
keys
```




    {'key1', 'key2', 'key3'}



However you do it, we end up with a set of all the possible keys used in our list of dictionaries.

Now we can go ahead and create a named tuple with all those keys as fields:


```
Struct = namedtuple('Struct', keys)
```


```
Struct._fields
```




    ('key3', 'key2', 'key1')



As you can see, sets do not preserve order, so in this case we'll probably sort the keys to create our named tuple:


```
Struct = namedtuple('Struct', sorted(keys))
```


```
Struct._fields
```




    ('key1', 'key2', 'key3')



Now, we're also going to provide default values, since not all dictionaries have all the keys in them. In this case I'm going to set the default to `None` if the key is missing:


```
Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
```

Now we're ready to load up all these dictionaries into a new list of named tuples:


```
tuple_list = [Struct(**dict_) for dict_ in data_list]
```


```
tuple_list
```




    [Struct(key1=1, key2=2, key3=None),
     Struct(key1=3, key2=4, key3=None),
     Struct(key1=5, key2=6, key3=7),
     Struct(key1=None, key2=100, key3=None)]



So lastly, let's just package this all up neatly into a single function that will take an iterable of dictionaries, or an arbitrary number of dictionaries as positional arguments, and return a list of named tuples:


```
def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', keys)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]
```


```
tuplify_dicts(data_list)
```




    [Struct(key1=1, key2=2, key3=None),
     Struct(key1=3, key2=4, key3=None),
     Struct(key1=5, key2=6, key3=7),
     Struct(key1=None, key2=100, key3=None)]



Isn't Python wonderful? :-)

##  Named Tuples - Application - Returning Multiple Values

We already know that we can easily return multiple values from a function by using a tuple:


```
from random import randint, random

def random_color():
    red = randint(0, 255)
    green = randint(0,255)
    blue = randint(0, 255)
    alpha = round(random(), 2)
    return red, green, blue, alpha
```


```
random_color()
```




    (97, 254, 97, 0.06)



So of course, we could call the function this and unpack the results at the same time:


```
red, green, blue, alpha = random_color()
```


```
print(f'red={red}, green={green}, blue={blue}, alpha={alpha}')
```

    red=42, green=178, blue=69, alpha=0.7
    

But it might be nicer to use a named tuple:


```
from collections import namedtuple
```


```
Color = namedtuple('Color', 'red green blue alpha')

def random_color():
    red = randint(0, 255)
    green = randint(0,255)
    blue = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red, green, blue, alpha)
```


```
color = random_color()
```


```
color.red
```




    5




```
color
```




    Color(red=5, green=210, blue=143, alpha=0.06)



# Section 09 - Modules, Packages and Namespaces

##  What is a Module?

A module is simply another data type. And the modules we use are instances of that data type.


```
import math
```

That word `math` is simply a label (think variable name) in our (global) namespace that points to some object in memory that is the `math` module.

Let's see what is in our global namespace:


```
globals()
```




    {'In': ['', 'import math', 'globals()'],
     'Out': {},
     '_': '',
     '__': '',
     '___': '',
     '__builtin__': <module 'builtins' (built-in)>,
     '__builtins__': <module 'builtins' (built-in)>,
     '__doc__': 'Automatically created module for IPython interactive environment',
     '__loader__': None,
     '__name__': '__main__',
     '__package__': None,
     '__spec__': None,
     '_dh': ['d:\\fbapt\\Dropbox\\Python Deep Dive\\Section 09 - Modules, Packages and Namespaces\\02 - What is a Module'],
     '_i': 'import math',
     '_i1': 'import math',
     '_i2': 'globals()',
     '_ih': ['', 'import math', 'globals()'],
     '_ii': '',
     '_iii': '',
     '_oh': {},
     'exit': <IPython.core.autocall.ZMQExitAutocall at 0x1ae10cb5550>,
     'get_ipython': <bound method InteractiveShell.get_ipython of <ipykernel.zmqshell.ZMQInteractiveShell object at 0x000001AE10373208>>,
     'math': <module 'math' (built-in)>,
     'quit': <IPython.core.autocall.ZMQExitAutocall at 0x1ae10cb5550>}




```
globals()['math']
```




    <module 'math' (built-in)>




```
type(math)
```




    module




```
math
```




    <module 'math' (built-in)>



It's just an object of type `module`, and it even has a memory address:


```
id(math)
```




    1847086390312



Take note of this memory address, we'll want to refer to it later!

Let me show you what happens if I set the `math` **label** to `None` (I could even use `del globals()['math']`:


```
math = None
```


```
type(math)
```




    NoneType




```
id(math)
```




    1800367120



As you can see the label `math` now points to something else.

Let me re-import it:


```
import math
```

And now we can see:


```
math
```




    <module 'math' (built-in)>




```
id(math)
```




    1847086390312



You'll notice that the label `math` now is the **same** memory address as the first time we ran the import.

**NOTE**: Please do not do this in your code. You never what side effects you may encounter - I just showed you this to make a point - when I ran the import the second time, I obtained a label that pointed to the **same** object.

What happens is that when you import a module, it is not actually loaded into the module's namespace only. Instead, the module is loaded into an overarching global system dictionary that contains the module name and the reference to the module object. The name we see here is "copied" into our namespace from that system namespace.

If we had a project with multiple modules that each imported `math`, Python will load the `math` module the first time it is requested and put it into memory.

The next time the `math` module is imported (in some different module), Python always looks at the system modules first - if it is there it simply copies that reference into our module's namespace and sets the label accordingly.

Let's take a look at the system modules:


```
import sys
```


```
type(sys.modules)
```




    dict



The `sys.modules` currently contains a **lot** of entries, so I'm just going to look at the one we're interested in - the `math` module:


```
sys.modules['math']
```




    <module 'math' (built-in)>



Aha! The `sys.modules` dictionary contains a key for `math` and as you saw it is the `math` module. In fact we can look at the memory address once more:


```
id(sys.modules['math'])
```




    1847086390312



Compare that to the `id` of the `math` module in our own (main) module - the same!

Now that we have established that a module is just an instance of the `module` type, and where it lives (in memory) with references to it maintained in the `sys.modules` dictionary as well as in any module namespace that imported it, let's see how we could create a module dynamically!

If it's an object, let's inspect it...


```
math.__name__
```




    'math'




```
math.__dict__
```




    {'__doc__': 'This module is always available.  It provides access to the\nmathematical functions defined by the C standard.',
     '__loader__': _frozen_importlib.BuiltinImporter,
     '__name__': 'math',
     '__package__': '',
     '__spec__': ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in'),
     'acos': <function math.acos>,
     'acosh': <function math.acosh>,
     'asin': <function math.asin>,
     'asinh': <function math.asinh>,
     'atan': <function math.atan>,
     'atan2': <function math.atan2>,
     'atanh': <function math.atanh>,
     'ceil': <function math.ceil>,
     'copysign': <function math.copysign>,
     'cos': <function math.cos>,
     'cosh': <function math.cosh>,
     'degrees': <function math.degrees>,
     'e': 2.718281828459045,
     'erf': <function math.erf>,
     'erfc': <function math.erfc>,
     'exp': <function math.exp>,
     'expm1': <function math.expm1>,
     'fabs': <function math.fabs>,
     'factorial': <function math.factorial>,
     'floor': <function math.floor>,
     'fmod': <function math.fmod>,
     'frexp': <function math.frexp>,
     'fsum': <function math.fsum>,
     'gamma': <function math.gamma>,
     'gcd': <function math.gcd>,
     'hypot': <function math.hypot>,
     'inf': inf,
     'isclose': <function math.isclose>,
     'isfinite': <function math.isfinite>,
     'isinf': <function math.isinf>,
     'isnan': <function math.isnan>,
     'ldexp': <function math.ldexp>,
     'lgamma': <function math.lgamma>,
     'log': <function math.log>,
     'log10': <function math.log10>,
     'log1p': <function math.log1p>,
     'log2': <function math.log2>,
     'modf': <function math.modf>,
     'nan': nan,
     'pi': 3.141592653589793,
     'pow': <function math.pow>,
     'radians': <function math.radians>,
     'sin': <function math.sin>,
     'sinh': <function math.sinh>,
     'sqrt': <function math.sqrt>,
     'tan': <function math.tan>,
     'tanh': <function math.tanh>,
     'tau': 6.283185307179586,
     'trunc': <function math.trunc>}



Notice how all the methods and "constants" (such as pi) are just members of a dictionary with values being functions or values:


```
math.sqrt is math.__dict__['sqrt']
```




    True



So, when we write `math.sqrt` we are basically just retrieving the function stored in the `math.__dict__` dictionary at that key (`sqrt`).

Now the `math` module is a little special - it is written in C and actually a built-in.

Let's look at another module from the standard library:


```
import fractions
```


```
fractions.__dict__
```




    {'Decimal': decimal.Decimal,
     'Fraction': fractions.Fraction,
     '_PyHASH_INF': 314159,
     '_PyHASH_MODULUS': 2305843009213693951,
     '_RATIONAL_FORMAT': re.compile(r'\n    \A\s*                      # optional whitespace at the start, then\n    (?P<sign>[-+]?)            # an optional sign, then\n    (?=\d|\.\d)                # lookahead for digit or .digit\n    (?P<num>\d*)               # numerator (possibly empty)\n    (?:                        # followed by\n       (?:/(?P<denom>\d+))?    # an optional denominator\n    |                          # or\n       (?:\.(?P<decimal>\d*))? # an optional fractional part\n       (?:E(?P<exp>[-+]?\d+))? # and optional exponent\n    )\n    \s*\Z                      # and optional whitespace to finish\n',
     re.IGNORECASE|re.UNICODE|re.VERBOSE),
     '__all__': ['Fraction', 'gcd'],
     '__builtins__': {'ArithmeticError': ArithmeticError,
      'AssertionError': AssertionError,
      'AttributeError': AttributeError,
      'BaseException': BaseException,
      'BlockingIOError': BlockingIOError,
      'BrokenPipeError': BrokenPipeError,
      'BufferError': BufferError,
      'BytesWarning': BytesWarning,
      'ChildProcessError': ChildProcessError,
      'ConnectionAbortedError': ConnectionAbortedError,
      'ConnectionError': ConnectionError,
      'ConnectionRefusedError': ConnectionRefusedError,
      'ConnectionResetError': ConnectionResetError,
      'DeprecationWarning': DeprecationWarning,
      'EOFError': EOFError,
      'Ellipsis': Ellipsis,
      'EnvironmentError': OSError,
      'Exception': Exception,
      'False': False,
      'FileExistsError': FileExistsError,
      'FileNotFoundError': FileNotFoundError,
      'FloatingPointError': FloatingPointError,
      'FutureWarning': FutureWarning,
      'GeneratorExit': GeneratorExit,
      'IOError': OSError,
      'ImportError': ImportError,
      'ImportWarning': ImportWarning,
      'IndentationError': IndentationError,
      'IndexError': IndexError,
      'InterruptedError': InterruptedError,
      'IsADirectoryError': IsADirectoryError,
      'KeyError': KeyError,
      'KeyboardInterrupt': KeyboardInterrupt,
      'LookupError': LookupError,
      'MemoryError': MemoryError,
      'ModuleNotFoundError': ModuleNotFoundError,
      'NameError': NameError,
      'None': None,
      'NotADirectoryError': NotADirectoryError,
      'NotImplemented': NotImplemented,
      'NotImplementedError': NotImplementedError,
      'OSError': OSError,
      'OverflowError': OverflowError,
      'PendingDeprecationWarning': PendingDeprecationWarning,
      'PermissionError': PermissionError,
      'ProcessLookupError': ProcessLookupError,
      'RecursionError': RecursionError,
      'ReferenceError': ReferenceError,
      'ResourceWarning': ResourceWarning,
      'RuntimeError': RuntimeError,
      'RuntimeWarning': RuntimeWarning,
      'StopAsyncIteration': StopAsyncIteration,
      'StopIteration': StopIteration,
      'SyntaxError': SyntaxError,
      'SyntaxWarning': SyntaxWarning,
      'SystemError': SystemError,
      'SystemExit': SystemExit,
      'TabError': TabError,
      'TimeoutError': TimeoutError,
      'True': True,
      'TypeError': TypeError,
      'UnboundLocalError': UnboundLocalError,
      'UnicodeDecodeError': UnicodeDecodeError,
      'UnicodeEncodeError': UnicodeEncodeError,
      'UnicodeError': UnicodeError,
      'UnicodeTranslateError': UnicodeTranslateError,
      'UnicodeWarning': UnicodeWarning,
      'UserWarning': UserWarning,
      'ValueError': ValueError,
      'Warning': Warning,
      'WindowsError': OSError,
      'ZeroDivisionError': ZeroDivisionError,
      '__IPYTHON__': True,
      '__build_class__': <function __build_class__>,
      '__debug__': True,
      '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.",
      '__import__': <function __import__>,
      '__loader__': _frozen_importlib.BuiltinImporter,
      '__name__': 'builtins',
      '__package__': '',
      '__spec__': ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>),
      'abs': <function abs>,
      'all': <function all>,
      'any': <function any>,
      'ascii': <function ascii>,
      'bin': <function bin>,
      'bool': bool,
      'bytearray': bytearray,
      'bytes': bytes,
      'callable': <function callable>,
      'chr': <function chr>,
      'classmethod': classmethod,
      'compile': <function compile>,
      'complex': complex,
      'copyright': Copyright (c) 2001-2017 Python Software Foundation.
      All Rights Reserved.
      
      Copyright (c) 2000 BeOpen.com.
      All Rights Reserved.
      
      Copyright (c) 1995-2001 Corporation for National Research Initiatives.
      All Rights Reserved.
      
      Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
      All Rights Reserved.,
      'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
          for supporting Python development.  See www.python.org for more information.,
      'delattr': <function delattr>,
      'dict': dict,
      'dir': <function dir>,
      'display': <function IPython.core.display.display>,
      'divmod': <function divmod>,
      'enumerate': enumerate,
      'eval': <function eval>,
      'exec': <function exec>,
      'filter': filter,
      'float': float,
      'format': <function format>,
      'frozenset': frozenset,
      'get_ipython': <bound method InteractiveShell.get_ipython of <ipykernel.zmqshell.ZMQInteractiveShell object at 0x000001AE10373208>>,
      'getattr': <function getattr>,
      'globals': <function globals>,
      'hasattr': <function hasattr>,
      'hash': <function hash>,
      'help': Type help() for interactive help, or help(object) for help about object.,
      'hex': <function hex>,
      'id': <function id>,
      'input': <bound method Kernel.raw_input of <ipykernel.ipkernel.IPythonKernel object at 0x000001AE10352EB8>>,
      'int': int,
      'isinstance': <function isinstance>,
      'issubclass': <function issubclass>,
      'iter': <function iter>,
      'len': <function len>,
      'license': See https://www.python.org/psf/license/,
      'list': list,
      'locals': <function locals>,
      'map': map,
      'max': <function max>,
      'memoryview': memoryview,
      'min': <function min>,
      'next': <function next>,
      'object': object,
      'oct': <function oct>,
      'open': <function io.open>,
      'ord': <function ord>,
      'pow': <function pow>,
      'print': <function print>,
      'property': property,
      'range': range,
      'repr': <function repr>,
      'reversed': reversed,
      'round': <function round>,
      'set': set,
      'setattr': <function setattr>,
      'slice': slice,
      'sorted': <function sorted>,
      'staticmethod': staticmethod,
      'str': str,
      'sum': <function sum>,
      'super': super,
      'tuple': tuple,
      'type': type,
      'vars': <function vars>,
      'zip': zip},
     '__cached__': 'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\lib\\__pycache__\\fractions.cpython-36.pyc',
     '__doc__': 'Fraction, infinite-precision, real numbers.',
     '__file__': 'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\lib\\fractions.py',
     '__loader__': <_frozen_importlib_external.SourceFileLoader at 0x1ae10e4cf98>,
     '__name__': 'fractions',
     '__package__': '',
     '__spec__': ModuleSpec(name='fractions', loader=<_frozen_importlib_external.SourceFileLoader object at 0x000001AE10E4CF98>, origin='D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\lib\\fractions.py'),
     '_gcd': <function fractions._gcd>,
     'gcd': <function fractions.gcd>,
     'math': <module 'math' (built-in)>,
     'numbers': <module 'numbers' from 'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\lib\\numbers.py'>,
     'operator': <module 'operator' from 'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\lib\\operator.py'>,
     're': <module 're' from 'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\lib\\re.py'>,
     'sys': <module 'sys' (built-in)>}



Notice a few properties here that look interesting:


```
fractions.__file__
```




    'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\lib\\fractions.py'



That's where the `fractions` module source code resides. I am using a virtual environment (conda), and the module `fractions.py` resides in that directory.

So a module is an object that is:
- loaded from file (maybe! we'll see that in a second)
- has a namespace
- is a container of global variables (that `__dict__` we saw)
- is an execution environment (we'll see that in an upcoming video)

Of course, modules are just specific data types, and like any other data type in Python (think classes, functions, etc) we can create them dynamically - they do not have to be loaded from file (though that is how we do it most of the time).


```
import types
```


```
isinstance(fractions, types.ModuleType)
```




    True



So, modules are instances of the `ModuleType` class.


```
help(ModuleType)
```

    Help on class module in module builtins:
    
    class module(object)
     |  module(name[, doc])
     |  
     |  Create a module object.
     |  The name must be a string; the optional doc argument can have any type.
     |  
     |  Methods defined here:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __dir__(...)
     |      __dir__() -> list
     |      specialized dir() implementation
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
    
    

Let's go ahead and create a new module:


```
mod = types.ModuleType('point', 'A module for handling points.')
```


```
mod
```




    <module 'point'>




```
help(mod)
```

    Help on module point:
    
    NAME
        point - A module for handling points.
    
    FILE
        (built-in)
    
    
    

OK, so now let's add some functionality to it by simply setting some attributes:


```
from collections import namedtuple
mod.Point = namedtuple('Point', 'x y')
```


```
def points_distance(pt1, pt2):
    return math.sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)
```


```
mod.distance = points_distance
```


```
mod.__dict__
```




    {'Point': __main__.Point,
     '__doc__': 'A module for handling points.',
     '__loader__': None,
     '__name__': 'point',
     '__package__': None,
     '__spec__': None,
     'distance': <function __main__.points_distance>}




```
p1 = mod.Point(0, 0)
p2 = mod.Point(1, 1)
```


```
mod.distance(p1, p2)
```




    1.4142135623730951



As you can see it behaves just like an ordinary module.

However, one major difference here is that it is not located in the `sys.modules` dictionary - so another module in our program would not know anything about it.

But we can fix that! We'll see this in one of the next videos.

But first we'll need to take a peek at how Python imports a module from file. COming right up!

##  Imports and `importlib`

In the last video we saw how we could, in a simplistic manner, mimic Python's import.

There is absolutely no need to do this since Python itself provides that functionality, both as a built-in function (`import`) and in the standard library module `importlib`.

In fact, if you want to see how imports are done in pure Python code you can always look at the source code for that library (you should now know where to find that on your local machine - you have to first identify a Pythyon environment (`sys.exec_prefix`) and then look in the `lib` folder:


```
import sys
```


```
sys.exec_prefix
```

Or you can import `importlib` and look at the `__file__` property to get an exact location:


```
import importlib
```


```
importlib.__file__
```

or just see the string representation of the `importlib` object:


```
importlib
```




    <module 'importlib' from 'D:\\Users\\fbapt\\Anaconda3\\lib\\importlib\\__init__.py'>



You'll find something a little different - `importlib` is not actually a pure module (it's still a module type object) - it's actually a package - more on that later.

You should then use the `import_module` function to load a module.

For example, we can load the `fractions` module as follows:


```
importlib.import_module('fractions')
```




    <module 'fractions' from 'D:\\Users\\fbapt\\Anaconda3\\lib\\fractions.py'>



The problem doing it this way is that **our** module namespace does not have a symbol for `fractions` (but it **is** in `sys.modules`):


```
f = fractions.Fraction(2, 3)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-92ac4b49f1a5> in <module>()
    ----> 1 f = fractions.Fraction(2, 3)
    

    NameError: name 'fractions' is not defined


So instead we would have to do it the same way we did it with our own custom importer:


```
fractions = importlib.import_module('fractions')
```

And now we have a symbol for the `fractions` object.


```
f = fractions.Fraction(2, 3)
```


```
f
```




    Fraction(2, 3)



One thing I briefly alluded to earlier, we can import from a variety of "sources".

Often it is from file, such as with `fractions`:


```
fractions
```




    <module 'fractions' from 'D:\\Users\\fbapt\\Anaconda3\\lib\\fractions.py'>



Sometimes it is built in to Python directly:


```
import math
```


```
math
```




    <module 'math' (built-in)>



In Python there are a number of files that are "code" files, such as

* `.py`: basic text file containing Python code
* `.pyc`: compiled Python code (bytecode)
* `.so`, `.pyd`: think DLL's (Linux / Windows)

amongst others. Furthermore, Python can reach inside `zip` archives for code (as well as other packaged distribution files such as those used by Egg or Wheel).

In very broad terms the import system, once the "source" code has been located works as we saw in the last video.

A lot of the complexity comes from locating a module when we try to import it.

Conceptually Python divides the work between **finders** and **loaders**.

The **finders** are responsible for finding the module/package and returning the module spec, while the **loaders**, are responsible for "loading" the source code that is then used in the final steps to compile, execute and cache the module object. An object that implements both is called an **importer** - but they are still two separate concepts.

Python provides a number of standard finders and importers, such as:

* built-in modules
* frozen modules
* import path finder (finds source code files on the import path - for example the `sys.path` entries we have seen before)

What's interesting about the import path finder and loader is that they can search (and load from) zip archives.

In fact it can even be extended to search other resources, including url's, databases, etc. You could theoretically store code in a Mongo or Redis database and import directly from there!

Let's look at the module spec for `fractions`:


```
fractions.__spec__
```




    ModuleSpec(name='fractions', loader=<_frozen_importlib_external.SourceFileLoader object at 0x00000154B83757F0>, origin='D:\\Users\\fbapt\\Anaconda3\\lib\\fractions.py')



As you can see the finder determined where the source code was located, and also indicated that the loader to be used is the SourceFileLoader.

How does Python know which finder to use in the first place?

It doesn't really - it will go through a bunch of finders, one by one, until one returns a module spec - if it exhausts all the registered finders and finds nothing, then we get the module not found exception:


```
import foo
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-15-34d390fb3acc> in <module>()
    ----> 1 import foo
    

    ModuleNotFoundError: No module named 'foo'


Here are the finders currently registered on my system:


```
sys.meta_path
```




    [_frozen_importlib.BuiltinImporter,
     _frozen_importlib.FrozenImporter,
     _frozen_importlib_external.PathFinder,
     <six._SixMetaPathImporter at 0x154b64d0198>,
     <pkg_resources.extern.VendorImporter at 0x154b7148f98>,
     <pkg_resources._vendor.six._SixMetaPathImporter at 0x154b72a5518>]



When we import our custom file-based modules, the `PathFinder` will be used to find the file.

We can also use `importlib` to find the spec for a particular module:


```
importlib.util.find_spec('math')
```




    ModuleSpec(name='math', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')




```
importlib.util.find_spec('fractions')
```




    ModuleSpec(name='fractions', loader=<_frozen_importlib_external.SourceFileLoader object at 0x00000154B83757F0>, origin='D:\\Users\\fbapt\\Anaconda3\\lib\\fractions.py')



Let's write out a small source file to disk, called module1.py:


```
with open('module1.py', 'w') as code_file:
    code_file.write("print('running module1.py...')\n")
    code_file.write('a = 100\n')
```

Now that we have the module on disk, we can ask `importlib` for the module spec:


```
importlib.util.find_spec('module1')
```




    ModuleSpec(name='module1', loader=<_frozen_importlib_external.SourceFileLoader object at 0x00000154B8435390>, origin='d:\\fbapt\\Dropbox\\Python Deep Dive\\Section 09 - Modules, Packages and Namespaces\\04 - Imports and importlib\\module1.py')



As you can see, it found the file and indicated it would be imported using the SourceFileLoader.

Now let's go ahead and actually import it:


```
import module1
```

    running module1.py...
    


```
module1.a
```




    100



Now let's go ahead and write a file somewhere other than our source folder - you'll have to change this code to specify your path where you want that module file to be created:


```
import os

# you can use this for Mac/Linux:
# ext_module_path = os.environ['HOME']

# you can use this in Windows 10
#ext_module_path = os.environ['HOMEPATH']

# or you can just hard code some path
# ext_module_path = 'c:\\temp' 

ext_module_path = os.environ.get('HOME', os.environ['HOMEPATH'])
```


```
ext_module_path
```




    '\\Users\\fbapt'




```
file_abs_path = os.path.join(ext_module_path, 'module2.py')
with open(file_abs_path, 'w') as code_file:
    code_file.write("print('running module2.py...')\n")
    code_file.write("x = 'python'\n")
```

Let's see if Python can figure the module spec:


```
importlib.util.find_spec('module2')
```

Nothing came back - it was not able to locate that module anywhere...


```
import module2
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    <ipython-input-27-4fbab195dd19> in <module>()
    ----> 1 import module2
    

    ModuleNotFoundError: No module named 'module2'


As expected, the import failed.

By the way, you can use `try...except` for your imports!


```
try:
    import module2
except ModuleNotFoundError:
    # could not find module
    # maybe import an alternative module instead??
    # e.g. import module1 as module2
    # but please do not just silence the exception!
    # if you're importing the module most likely you are
    # using it somewhere in your code - so raise an 
    # exception at the precise location where the root cause
    # occurred!
    # so the following is BAD!!
    print('Module was not found.')
```

    Module was not found.
    

The module was not found because `sys.path` knows nothing about `ext_module_path`.


```
ext_module_path in sys.path
```




    False



So, let's add it!


```
sys.path.append(ext_module_path)
```

Now let's try finding the module spec again:


```
importlib.util.find_spec('module2')
```




    ModuleSpec(name='module2', loader=<_frozen_importlib_external.SourceFileLoader object at 0x00000154B84356A0>, origin='\\Users\\fbapt\\module2.py')



Hurray! Our import should now work...


```
import module2
```

    running module2.py...
    


```
module2.x
```




    'python'



We can "hack" the `sys.path` list by adding our own entries directly - but this means we would have to hard code these paths in our code, or potentially read them from a configuration file.

It's perfectly fine to do that, but you may prefer using `.pth` files for that.

I'm not going to get into the details of this - the Python docs are located here:

https://docs.python.org/3/library/site.html

##  Import Variants and Misconceptions

I would like to briefly discuss the various import variants such as:

* `import math`
* `from math import sqrt, abs`
* `from math import *`
* `import math as r_math`
* `from math import sqrt as r_sqrt`

##### import math

* loads the entire module (`math`) in memory if it's not already there
* adds a reference to it in `sys.modules` with a key of `math`
* adds a symbol of the same name (`math`) in our current namespace referencing the `math` object

##### import math as r_math

* loads the entire module (`math`) in memory if it's not already there
* adds a reference to it in `sys.modules` with a key of `math`
* adds the symbol `r_math` to our current namespace referencing the `math` object

##### from math import sqrt

* loads the entire module (`math`) in memory if it's not already there
* adds a reference to it in `sys.modules` with a key of `math`
* adds the symbol `sqrt` to our current namespace referencing the `math.sqrt` function
* it **does not** add the symbol `math` to our current namespace

##### from math import sqrt as r_sqrt

* loads the entire module (`math`) in memory if it's not already there
* adds a reference to it in `sys.modules` with a key of `math`
* adds the symbol `r_sqrt` to our current namespace referencing the `math.sqrt` function
* it **does not** add the symbol `math` to our current namespace

##### from math import *

* loads the entire module (`math`) in memory if it's not already there
* adds a reference to it in `sys.modules` with a key of `math`
* adds symbols for all exported symbols in the `math` module directly to our name space (we'll see how what is exported from a module/package can be controlled using underscores or `__all__` later)
* it **does not** add the symbol `math` to our current namespace

As you can see, in **every** instance, the module is imported and a reference to it is added to `sys.modules`. The variants really have to do with what is injected into our current **namespace**: the module name, an alias to it, just the specified symbols from the module, or all the exported symbols from the module.

#### Misconceptions

This leads to the first misconception:

"You should use

`from math import sqrt, abs`

rather than 

`import math`

because that way you only import what you need and you're not having Python load the entire module?"

For `math` that's just not true. In fact for any *simple* module.

For *packages* that have subpackages, that may or may not be true - we'll see that later.

Let's actually test this out.

We have to be a little careful, because Jupyter imports a ton of modules and packages:


```
import sys
for key in sorted(sys.modules.keys()):
    print(key)
```

    IPython
    IPython.core
    IPython.core.alias
    IPython.core.application
    IPython.core.autocall
    IPython.core.builtin_trap
    IPython.core.compilerop
    IPython.core.completer
    IPython.core.completerlib
    IPython.core.crashhandler
    IPython.core.debugger
    IPython.core.display
    IPython.core.display_trap
    IPython.core.displayhook
    IPython.core.displaypub
    IPython.core.error
    IPython.core.events
    IPython.core.excolors
    IPython.core.extensions
    IPython.core.formatters
    IPython.core.getipython
    IPython.core.history
    IPython.core.hooks
    IPython.core.inputsplitter
    IPython.core.inputtransformer
    IPython.core.interactiveshell
    IPython.core.latex_symbols
    IPython.core.logger
    IPython.core.macro
    IPython.core.magic
    IPython.core.magic_arguments
    IPython.core.magics
    IPython.core.magics.auto
    IPython.core.magics.basic
    IPython.core.magics.code
    IPython.core.magics.config
    IPython.core.magics.display
    IPython.core.magics.execution
    IPython.core.magics.extension
    IPython.core.magics.history
    IPython.core.magics.logging
    IPython.core.magics.namespace
    IPython.core.magics.osm
    IPython.core.magics.pylab
    IPython.core.magics.script
    IPython.core.oinspect
    IPython.core.page
    IPython.core.payload
    IPython.core.payloadpage
    IPython.core.prefilter
    IPython.core.profiledir
    IPython.core.pylabtools
    IPython.core.release
    IPython.core.shadowns
    IPython.core.shellapp
    IPython.core.splitinput
    IPython.core.ultratb
    IPython.core.usage
    IPython.display
    IPython.extensions
    IPython.extensions.storemagic
    IPython.lib
    IPython.lib.backgroundjobs
    IPython.lib.clipboard
    IPython.lib.deepreload
    IPython.lib.display
    IPython.lib.pretty
    IPython.lib.security
    IPython.paths
    IPython.terminal
    IPython.terminal.debugger
    IPython.terminal.embed
    IPython.terminal.interactiveshell
    IPython.terminal.ipapp
    IPython.terminal.magics
    IPython.terminal.prompts
    IPython.terminal.pt_inputhooks
    IPython.terminal.ptutils
    IPython.terminal.shortcuts
    IPython.testing
    IPython.testing.skipdoctest
    IPython.utils
    IPython.utils.PyColorize
    IPython.utils._process_common
    IPython.utils._process_win32
    IPython.utils._sysinfo
    IPython.utils._tokenize_py3
    IPython.utils.capture
    IPython.utils.colorable
    IPython.utils.coloransi
    IPython.utils.contexts
    IPython.utils.data
    IPython.utils.decorators
    IPython.utils.dir2
    IPython.utils.encoding
    IPython.utils.frame
    IPython.utils.generics
    IPython.utils.importstring
    IPython.utils.io
    IPython.utils.ipstruct
    IPython.utils.module_paths
    IPython.utils.openpy
    IPython.utils.path
    IPython.utils.process
    IPython.utils.py3compat
    IPython.utils.sentinel
    IPython.utils.signatures
    IPython.utils.strdispatch
    IPython.utils.sysinfo
    IPython.utils.syspathcontext
    IPython.utils.tempdir
    IPython.utils.terminal
    IPython.utils.text
    IPython.utils.timing
    IPython.utils.tokenize2
    IPython.utils.tokenutil
    IPython.utils.ulinecache
    IPython.utils.wildcard
    __future__
    __main__
    __mp_main__
    _ast
    _bisect
    _blake2
    _bootlocale
    _bz2
    _codecs
    _collections
    _collections_abc
    _compat_pickle
    _compression
    _ctypes
    _cython_0_25_1
    _datetime
    _frozen_importlib
    _frozen_importlib_external
    _functools
    _hashlib
    _heapq
    _imp
    _io
    _json
    _locale
    _lsprof
    _lzma
    _multiprocessing
    _opcode
    _operator
    _pickle
    _random
    _sha3
    _signal
    _sitebuiltins
    _socket
    _sqlite3
    _sre
    _stat
    _string
    _strptime
    _struct
    _thread
    _warnings
    _weakref
    _weakrefset
    _win32sysloader
    _winapi
    abc
    argparse
    array
    ast
    atexit
    base64
    bdb
    binascii
    bisect
    builtins
    bz2
    cProfile
    calendar
    cmd
    code
    codecs
    codeop
    collections
    collections.abc
    colorama
    colorama.ansi
    colorama.ansitowin32
    colorama.initialise
    colorama.win32
    colorama.winterm
    concurrent
    concurrent.futures
    concurrent.futures._base
    concurrent.futures.process
    concurrent.futures.thread
    contextlib
    copy
    copyreg
    ctypes
    ctypes._endian
    ctypes.util
    ctypes.wintypes
    datetime
    dateutil
    dateutil._common
    dateutil.parser
    dateutil.relativedelta
    dateutil.tz
    dateutil.tz._common
    dateutil.tz.tz
    dateutil.tz.win
    decorator
    dis
    email
    email._parseaddr
    email._policybase
    email.base64mime
    email.charset
    email.encoders
    email.errors
    email.feedparser
    email.header
    email.parser
    email.quoprimime
    email.utils
    encodings
    encodings.aliases
    encodings.cp1252
    encodings.cp437
    encodings.latin_1
    encodings.utf_8
    enum
    errno
    faulthandler
    fnmatch
    functools
    gc
    genericpath
    getopt
    getpass
    gettext
    glob
    hashlib
    heapq
    hmac
    html
    html.entities
    imp
    importlib
    importlib._bootstrap
    importlib._bootstrap_external
    importlib.abc
    importlib.machinery
    importlib.util
    inspect
    io
    ipykernel
    ipykernel._version
    ipykernel.codeutil
    ipykernel.comm
    ipykernel.comm.comm
    ipykernel.comm.manager
    ipykernel.connect
    ipykernel.datapub
    ipykernel.displayhook
    ipykernel.heartbeat
    ipykernel.iostream
    ipykernel.ipkernel
    ipykernel.jsonutil
    ipykernel.kernelapp
    ipykernel.kernelbase
    ipykernel.parentpoller
    ipykernel.pickleutil
    ipykernel.serialize
    ipykernel.zmqshell
    ipython_genutils
    ipython_genutils._version
    ipython_genutils.encoding
    ipython_genutils.importstring
    ipython_genutils.path
    ipython_genutils.py3compat
    ipython_genutils.text
    ipywidgets
    ipywidgets._version
    ipywidgets.widgets
    ipywidgets.widgets.domwidget
    ipywidgets.widgets.interaction
    ipywidgets.widgets.trait_types
    ipywidgets.widgets.valuewidget
    ipywidgets.widgets.widget
    ipywidgets.widgets.widget_bool
    ipywidgets.widgets.widget_box
    ipywidgets.widgets.widget_button
    ipywidgets.widgets.widget_color
    ipywidgets.widgets.widget_controller
    ipywidgets.widgets.widget_core
    ipywidgets.widgets.widget_date
    ipywidgets.widgets.widget_float
    ipywidgets.widgets.widget_image
    ipywidgets.widgets.widget_int
    ipywidgets.widgets.widget_layout
    ipywidgets.widgets.widget_link
    ipywidgets.widgets.widget_output
    ipywidgets.widgets.widget_selection
    ipywidgets.widgets.widget_selectioncontainer
    ipywidgets.widgets.widget_string
    ipywidgets.widgets.widget_style
    itertools
    json
    json.decoder
    json.encoder
    json.scanner
    jupyter_client
    jupyter_client._version
    jupyter_client.adapter
    jupyter_client.blocking
    jupyter_client.blocking.channels
    jupyter_client.blocking.client
    jupyter_client.channels
    jupyter_client.channelsabc
    jupyter_client.client
    jupyter_client.clientabc
    jupyter_client.connect
    jupyter_client.jsonutil
    jupyter_client.kernelspec
    jupyter_client.launcher
    jupyter_client.localinterfaces
    jupyter_client.manager
    jupyter_client.managerabc
    jupyter_client.multikernelmanager
    jupyter_client.session
    jupyter_core
    jupyter_core.paths
    jupyter_core.version
    keyword
    linecache
    locale
    logging
    logging.handlers
    lzma
    marshal
    math
    mimetypes
    msvcrt
    multiprocessing
    multiprocessing.connection
    multiprocessing.context
    multiprocessing.process
    multiprocessing.reduction
    multiprocessing.util
    nt
    ntpath
    numbers
    opcode
    operator
    optparse
    os
    os.path
    pathlib
    pdb
    pickle
    pickleshare
    pkg_resources
    pkg_resources._vendor
    pkg_resources._vendor.packaging.__about__
    pkg_resources._vendor.six
    pkg_resources._vendor.six.moves
    pkg_resources.extern
    pkg_resources.extern.appdirs
    pkg_resources.extern.packaging
    pkg_resources.extern.packaging._compat
    pkg_resources.extern.packaging._structures
    pkg_resources.extern.packaging.markers
    pkg_resources.extern.packaging.requirements
    pkg_resources.extern.packaging.specifiers
    pkg_resources.extern.packaging.version
    pkg_resources.extern.pyparsing
    pkg_resources.extern.six
    pkg_resources.extern.six.moves
    pkg_resources.extern.six.moves.urllib
    pkgutil
    platform
    plistlib
    posixpath
    pprint
    profile
    prompt_toolkit
    prompt_toolkit.application
    prompt_toolkit.auto_suggest
    prompt_toolkit.buffer
    prompt_toolkit.buffer_mapping
    prompt_toolkit.cache
    prompt_toolkit.clipboard
    prompt_toolkit.clipboard.base
    prompt_toolkit.clipboard.in_memory
    prompt_toolkit.completion
    prompt_toolkit.document
    prompt_toolkit.enums
    prompt_toolkit.eventloop
    prompt_toolkit.eventloop.base
    prompt_toolkit.eventloop.callbacks
    prompt_toolkit.filters
    prompt_toolkit.filters.base
    prompt_toolkit.filters.cli
    prompt_toolkit.filters.types
    prompt_toolkit.filters.utils
    prompt_toolkit.history
    prompt_toolkit.input
    prompt_toolkit.interface
    prompt_toolkit.key_binding
    prompt_toolkit.key_binding.bindings
    prompt_toolkit.key_binding.bindings.basic
    prompt_toolkit.key_binding.bindings.completion
    prompt_toolkit.key_binding.bindings.emacs
    prompt_toolkit.key_binding.bindings.named_commands
    prompt_toolkit.key_binding.bindings.scroll
    prompt_toolkit.key_binding.bindings.vi
    prompt_toolkit.key_binding.defaults
    prompt_toolkit.key_binding.digraphs
    prompt_toolkit.key_binding.input_processor
    prompt_toolkit.key_binding.manager
    prompt_toolkit.key_binding.registry
    prompt_toolkit.key_binding.vi_state
    prompt_toolkit.keys
    prompt_toolkit.layout
    prompt_toolkit.layout.containers
    prompt_toolkit.layout.controls
    prompt_toolkit.layout.dimension
    prompt_toolkit.layout.lexers
    prompt_toolkit.layout.margins
    prompt_toolkit.layout.menus
    prompt_toolkit.layout.mouse_handlers
    prompt_toolkit.layout.processors
    prompt_toolkit.layout.prompt
    prompt_toolkit.layout.screen
    prompt_toolkit.layout.toolbars
    prompt_toolkit.layout.utils
    prompt_toolkit.mouse_events
    prompt_toolkit.output
    prompt_toolkit.reactive
    prompt_toolkit.renderer
    prompt_toolkit.search_state
    prompt_toolkit.selection
    prompt_toolkit.shortcuts
    prompt_toolkit.styles
    prompt_toolkit.styles.base
    prompt_toolkit.styles.defaults
    prompt_toolkit.styles.from_dict
    prompt_toolkit.styles.from_pygments
    prompt_toolkit.styles.utils
    prompt_toolkit.terminal
    prompt_toolkit.terminal.conemu_output
    prompt_toolkit.terminal.vt100_output
    prompt_toolkit.terminal.win32_input
    prompt_toolkit.terminal.win32_output
    prompt_toolkit.token
    prompt_toolkit.utils
    prompt_toolkit.validation
    prompt_toolkit.win32_types
    pstats
    pydoc
    pyexpat
    pyexpat.errors
    pyexpat.model
    pygments
    pygments.filter
    pygments.filters
    pygments.formatter
    pygments.formatters
    pygments.formatters._mapping
    pygments.formatters.html
    pygments.lexer
    pygments.lexers
    pygments.lexers._mapping
    pygments.lexers.python
    pygments.modeline
    pygments.plugin
    pygments.regexopt
    pygments.style
    pygments.styles
    pygments.styles.default
    pygments.token
    pygments.unistring
    pygments.util
    pythoncom
    pywintypes
    queue
    quopri
    random
    re
    reprlib
    runpy
    select
    selectors
    shlex
    shutil
    signal
    simplegeneric
    site
    six
    six.moves
    socket
    sqlite3
    sqlite3.dbapi2
    sre_compile
    sre_constants
    sre_parse
    stat
    storemagic
    string
    struct
    subprocess
    sys
    sysconfig
    tempfile
    textwrap
    threading
    time
    timeit
    token
    tokenize
    tornado
    tornado.concurrent
    tornado.escape
    tornado.ioloop
    tornado.log
    tornado.platform
    tornado.platform.auto
    tornado.platform.common
    tornado.platform.interface
    tornado.platform.windows
    tornado.speedups
    tornado.stack_context
    tornado.util
    traceback
    traitlets
    traitlets._version
    traitlets.config
    traitlets.config.application
    traitlets.config.configurable
    traitlets.config.loader
    traitlets.log
    traitlets.traitlets
    traitlets.utils
    traitlets.utils.bunch
    traitlets.utils.getargspec
    traitlets.utils.importstring
    traitlets.utils.sentinel
    types
    typing
    typing.io
    typing.re
    unicodedata
    urllib
    urllib.parse
    uuid
    warnings
    wcwidth
    wcwidth.table_wide
    wcwidth.table_zero
    wcwidth.wcwidth
    weakref
    win32api
    win32com
    win32com.gen_py
    win32com.shell
    winreg
    xml
    xml.parsers
    xml.parsers.expat
    xml.parsers.expat.errors
    xml.parsers.expat.model
    zipfile
    zipimport
    zlib
    zmq
    zmq.backend
    zmq.backend.cython
    zmq.backend.cython._device
    zmq.backend.cython._poll
    zmq.backend.cython._version
    zmq.backend.cython.constants
    zmq.backend.cython.context
    zmq.backend.cython.error
    zmq.backend.cython.message
    zmq.backend.cython.socket
    zmq.backend.cython.utils
    zmq.backend.select
    zmq.error
    zmq.eventloop
    zmq.eventloop.ioloop
    zmq.eventloop.zmqstream
    zmq.libzmq
    zmq.sugar
    zmq.sugar.attrsettr
    zmq.sugar.constants
    zmq.sugar.context
    zmq.sugar.frame
    zmq.sugar.poll
    zmq.sugar.socket
    zmq.sugar.stopwatch
    zmq.sugar.tracker
    zmq.sugar.version
    zmq.utils
    zmq.utils.constant_names
    zmq.utils.jsonapi
    zmq.utils.strtypes
    

so they're already loaded and in the `sys.modules` dictionary.


Fortunately `cmath` is not one of them, so we'll use that one.


```
'cmath' in sys.modules
```




    False



Let's go ahead and just import a single symbol from `cmath`, the `exp` function:


```
from cmath import exp
```

Now let's see if `cmath` and `exp` are in our module (global) namespace:


```
'cmath' in globals()
```




    False




```
'exp' in globals()
```




    True



OK, so basically what that import did was create a symbol for `exp` in our namespace, but not for `cmath`.

Does this mean that `cmath` was only "partially" loaded?

How can Python "partially" load a (simple) module? How would it even know what to load up? Sure, maybe it could do some fancy kind of introspection and determine all the dependencies the symbols we are importing require. But it does not.

It simply imports the entire module (using the techniques we have been covering in the last few videos)

If we really want to partially load something, we would use a package, which, while still a `module` type, can be composed of several sub-packages. More on that later.

In, fact let's look at it in `sys.modules`:


```
sys.modules['cmath']
```




    <module 'cmath' (built-in)>



Yep, it's there...

We can even get a handle to the `cmath` module:


```
cmath = sys.modules['cmath']
```


```
cmath
```




    <module 'cmath' (built-in)>



And now we can use `cmath` just as if we had done 

`import cmath`

But you'll note that in this case we did not import the module, we did `from cmath import exp` only.

So we can use `exp` directly because of how we imported that specific symbol:


```
exp(2+3j)
```




    (-7.315110094901103+1.0427436562359045j)



But we can also use the `cmath` module directly now that we retrieved it from `sys.modules`:


```
cmath.sqrt(1+1j)
```




    (1.09868411346781+0.45508986056222733j)



So, the **entire** `cmath` module was loaded when we ran `from cmath import exp`, not just a portion of it!

The only thing that happened is that Python put `cmath` in `sys.modules`, but **did not** add a `cmath` symbol to our module namespace, and **only added** the function `exp` to our namespace.

What about doing something like this:

`from cmath import *`

This is often frowned upon, and sometimes for good reason - but this is not a universal truth either.

Let's see why, in our current context, it's maybe not such a good thing.

First let's see what our global namespace looks like:


```
globals()
```




    {'In': ['',
      'import sys\nfor key in sorted(sys.modules.keys()):\n    print(key)',
      "'cmath' in sys.modules",
      'from cmath import exp',
      "'cmath' in globals()",
      "'exp' in globals()",
      "sys.modules['cmath']",
      "cmath = sys.modules['cmath']",
      'cmath',
      'exp(2+3j)',
      'cmath.sqrt(1+1j)',
      'globals()'],
     'Out': {2: False,
      4: False,
      5: True,
      6: <module 'cmath' (built-in)>,
      8: <module 'cmath' (built-in)>,
      9: (-7.315110094901103+1.0427436562359045j),
      10: (1.09868411346781+0.45508986056222733j)},
     '_': (1.09868411346781+0.45508986056222733j),
     '_10': (1.09868411346781+0.45508986056222733j),
     '_2': False,
     '_4': False,
     '_5': True,
     '_6': <module 'cmath' (built-in)>,
     '_8': <module 'cmath' (built-in)>,
     '_9': (-7.315110094901103+1.0427436562359045j),
     '__': (-7.315110094901103+1.0427436562359045j),
     '___': <module 'cmath' (built-in)>,
     '__builtin__': <module 'builtins' (built-in)>,
     '__builtins__': <module 'builtins' (built-in)>,
     '__doc__': 'Automatically created module for IPython interactive environment',
     '__loader__': None,
     '__name__': '__main__',
     '__package__': None,
     '__spec__': None,
     '_dh': ['d:\\fbapt\\Dropbox\\Python Deep Dive\\Section 09 - Modules, Packages and Namespaces\\05 - Import Variants and Misconceptions'],
     '_i': 'cmath.sqrt(1+1j)',
     '_i1': 'import sys\nfor key in sorted(sys.modules.keys()):\n    print(key)',
     '_i10': 'cmath.sqrt(1+1j)',
     '_i11': 'globals()',
     '_i2': "'cmath' in sys.modules",
     '_i3': 'from cmath import exp',
     '_i4': "'cmath' in globals()",
     '_i5': "'exp' in globals()",
     '_i6': "sys.modules['cmath']",
     '_i7': "cmath = sys.modules['cmath']",
     '_i8': 'cmath',
     '_i9': 'exp(2+3j)',
     '_ih': ['',
      'import sys\nfor key in sorted(sys.modules.keys()):\n    print(key)',
      "'cmath' in sys.modules",
      'from cmath import exp',
      "'cmath' in globals()",
      "'exp' in globals()",
      "sys.modules['cmath']",
      "cmath = sys.modules['cmath']",
      'cmath',
      'exp(2+3j)',
      'cmath.sqrt(1+1j)',
      'globals()'],
     '_ii': 'exp(2+3j)',
     '_iii': 'cmath',
     '_oh': {2: False,
      4: False,
      5: True,
      6: <module 'cmath' (built-in)>,
      8: <module 'cmath' (built-in)>,
      9: (-7.315110094901103+1.0427436562359045j),
      10: (1.09868411346781+0.45508986056222733j)},
     '_sh': <module 'IPython.core.shadowns' from 'D:\\Users\\fbapt\\Anaconda3\\lib\\site-packages\\IPython\\core\\shadowns.py'>,
     'cmath': <module 'cmath' (built-in)>,
     'exit': <IPython.core.autocall.ZMQExitAutocall at 0x1b7b61ecb00>,
     'exp': <function cmath.exp>,
     'get_ipython': <bound method InteractiveShell.get_ipython of <ipykernel.zmqshell.ZMQInteractiveShell object at 0x000001B7B61A84A8>>,
     'key': 'zmq.utils.strtypes',
     'quit': <IPython.core.autocall.ZMQExitAutocall at 0x1b7b61ecb00>,
     'sys': <module 'sys' (built-in)>}



Now let's do that import:


```
from cmath import *
```

And let's see our namespace now:


```
globals()
```




    {'In': ['',
      'import sys\nfor key in sorted(sys.modules.keys()):\n    print(key)',
      "'cmath' in sys.modules",
      'from cmath import exp',
      "'cmath' in globals()",
      "'exp' in globals()",
      "sys.modules['cmath']",
      "cmath = sys.modules['cmath']",
      'cmath',
      'exp(2+3j)',
      'cmath.sqrt(1+1j)',
      'globals()',
      'from cmath import *',
      'globals()'],
     'Out': {2: False,
      4: False,
      5: True,
      6: <module 'cmath' (built-in)>,
      8: <module 'cmath' (built-in)>,
      9: (-7.315110094901103+1.0427436562359045j),
      10: (1.09868411346781+0.45508986056222733j),
      11: {...}},
     '_': {...},
     '_10': (1.09868411346781+0.45508986056222733j),
     '_11': {...},
     '_2': False,
     '_4': False,
     '_5': True,
     '_6': <module 'cmath' (built-in)>,
     '_8': <module 'cmath' (built-in)>,
     '_9': (-7.315110094901103+1.0427436562359045j),
     '__': (1.09868411346781+0.45508986056222733j),
     '___': (-7.315110094901103+1.0427436562359045j),
     '__builtin__': <module 'builtins' (built-in)>,
     '__builtins__': <module 'builtins' (built-in)>,
     '__doc__': 'Automatically created module for IPython interactive environment',
     '__loader__': None,
     '__name__': '__main__',
     '__package__': None,
     '__spec__': None,
     '_dh': ['d:\\fbapt\\Dropbox\\Python Deep Dive\\Section 09 - Modules, Packages and Namespaces\\05 - Import Variants and Misconceptions'],
     '_i': 'from cmath import *',
     '_i1': 'import sys\nfor key in sorted(sys.modules.keys()):\n    print(key)',
     '_i10': 'cmath.sqrt(1+1j)',
     '_i11': 'globals()',
     '_i12': 'from cmath import *',
     '_i13': 'globals()',
     '_i2': "'cmath' in sys.modules",
     '_i3': 'from cmath import exp',
     '_i4': "'cmath' in globals()",
     '_i5': "'exp' in globals()",
     '_i6': "sys.modules['cmath']",
     '_i7': "cmath = sys.modules['cmath']",
     '_i8': 'cmath',
     '_i9': 'exp(2+3j)',
     '_ih': ['',
      'import sys\nfor key in sorted(sys.modules.keys()):\n    print(key)',
      "'cmath' in sys.modules",
      'from cmath import exp',
      "'cmath' in globals()",
      "'exp' in globals()",
      "sys.modules['cmath']",
      "cmath = sys.modules['cmath']",
      'cmath',
      'exp(2+3j)',
      'cmath.sqrt(1+1j)',
      'globals()',
      'from cmath import *',
      'globals()'],
     '_ii': 'globals()',
     '_iii': 'cmath.sqrt(1+1j)',
     '_oh': {2: False,
      4: False,
      5: True,
      6: <module 'cmath' (built-in)>,
      8: <module 'cmath' (built-in)>,
      9: (-7.315110094901103+1.0427436562359045j),
      10: (1.09868411346781+0.45508986056222733j),
      11: {...}},
     '_sh': <module 'IPython.core.shadowns' from 'D:\\Users\\fbapt\\Anaconda3\\lib\\site-packages\\IPython\\core\\shadowns.py'>,
     'acos': <function cmath.acos>,
     'acosh': <function cmath.acosh>,
     'asin': <function cmath.asin>,
     'asinh': <function cmath.asinh>,
     'atan': <function cmath.atan>,
     'atanh': <function cmath.atanh>,
     'cmath': <module 'cmath' (built-in)>,
     'cos': <function cmath.cos>,
     'cosh': <function cmath.cosh>,
     'e': 2.718281828459045,
     'exit': <IPython.core.autocall.ZMQExitAutocall at 0x1b7b61ecb00>,
     'exp': <function cmath.exp>,
     'get_ipython': <bound method InteractiveShell.get_ipython of <ipykernel.zmqshell.ZMQInteractiveShell object at 0x000001B7B61A84A8>>,
     'inf': inf,
     'infj': infj,
     'isclose': <function cmath.isclose>,
     'isfinite': <function cmath.isfinite>,
     'isinf': <function cmath.isinf>,
     'isnan': <function cmath.isnan>,
     'key': 'zmq.utils.strtypes',
     'log': <function cmath.log>,
     'log10': <function cmath.log10>,
     'nan': nan,
     'nanj': nanj,
     'phase': <function cmath.phase>,
     'pi': 3.141592653589793,
     'polar': <function cmath.polar>,
     'quit': <IPython.core.autocall.ZMQExitAutocall at 0x1b7b61ecb00>,
     'rect': <function cmath.rect>,
     'sin': <function cmath.sin>,
     'sinh': <function cmath.sinh>,
     'sqrt': <function cmath.sqrt>,
     'sys': <module 'sys' (built-in)>,
     'tan': <function cmath.tan>,
     'tanh': <function cmath.tanh>,
     'tau': 6.283185307179586}



Some people say the namespace was "polluted". In a way I guess that's true, but it does mean I can now access **all** attributes in `cmath` without prefixing them with `cmath` all the time: 


```
sqrt(2+2j)
```




    (1.5537739740300374+0.6435942529055826j)




```
pi
```




    3.141592653589793




```
sin(2-3j)
```




    (9.15449914691143+4.168906959966565j)



In and of itself, there's nothing wrong with that...

But a couple of issues:

The first one is that when I call `sin` just like that, someone reading my code does not immediately know where that function came from. Was it a function I implemented in my module? some other custom module? the `cmath` module? the `math` module?

The second one is that you can run into serious problems if you also need to import the `math` module:

Currently the `sqrt` symbol is the `cmath.sqrt` function:


```
sqrt
```




    <function cmath.sqrt>




```
from math import *
```

What just happened to the `sqrt` function that was in our namespace?


```
sqrt
```




    <function math.sqrt>



As you can see, the symbol `sqrt` in our namespace no longer refers to the `sqrt` function in `cmath` but rather to the one in `math`.

It just got replaced by the `sqrt` function in the `math` module because it has the same name (`sqrt`).

This is one of the reasons why `from ... import *` is sometimes frowned upon.

But the same problem can happen if you use a `from` import this way:


```
from cmath import sqrt
from math import sqrt
```

Same thing happened here, the `math.sqrt` function just clobbered the `cmath.sqrt` function.

One option here is to use:


```
import cmath
import math
```


```
math.sqrt(2)
```




    1.4142135623730951




```
cmath.sqrt(2+2j)
```




    (1.5537739740300374+0.6435942529055826j)



But Python also allows us to alias our imports using the `as` keyword.

We can alias either the entire module, or just the symbols being imported from the module:


```
import math as r_math
import cmath as c_math
```


```
r_math
```




    <module 'math' (built-in)>




```
c_math
```




    <module 'cmath' (built-in)>




```
r_math.sqrt(2)
```




    1.4142135623730951




```
c_math.sqrt(2)
```




    (1.4142135623730951+0j)



By the way, this is the **exact** same result as doing:


```
import importlib
```


```
r_math = importlib.import_module('math')
c_math = importlib.import_module('cmath')
```


```
r_math
```




    <module 'math' (built-in)>




```
c_math
```




    <module 'cmath' (built-in)>



We can also alias symbols from the imported module:


```
from math import sqrt as r_sqrt
from cmath import sqrt as c_sqrt
```


```
r_sqrt
```




    <function math.sqrt>




```
c_sqrt
```




    <function cmath.sqrt>



Again, we can reproduce this using the following:


```
r_sqrt = importlib.import_module('math').sqrt
c_sqrt = importlib.import_module('cmath').sqrt
```


```
r_sqrt
```




    <function math.sqrt>




```
c_sqrt
```




    <function cmath.sqrt>



At the end of the day, the module is always loaded and cached (`sys.modules`), these different variants of the `import` statement merely determine what symbols are added to our module (global) namespace. That's it.

It's a little different for packages as we'll see later.

#### Efficiency

The final thing we need to look at is often mentioned in various blog posts and online discussions.

`import variant #1` is more "efficient" than `import variant #2`

Maybe so, but realistically by how much?

Or even how the following is terribly wrong because it re-imports the `math` module **every** time `my_func` is called:


```
def my_func(a):
    import math
    return math.sqrt(a)
```

From a readability standpoint, yes, that is **not** a good idea. Much better to put all your imports at the top of the module once in a location where any reader can easily see all your module dependencies.

But as far as reloading the module, you should now understand that's absolutely not true. Instead, it has to do a dictionary lookup in the `sys.modules` dictionary, not reload the entire module after the first load has occurred!

Dictionary lookups are blazingly fast in Python - so, yes, there is some overhead, but not as much as you may think.

So, let's write some timing code to test these things and see how they compare.

We shoudl consider both relative speed differences as well as absilute speed differences.

If you try to optimize your code and end up reducing that code's speed by 50% that sounds good. But what if the original code ran in `1`s. Now it runs in `0.5`s. How long does the total program run? Down from `30`s to `29.5`s? Things are relative...


```
from time import perf_counter
```

Yes, I'm using a `from` import - for readability and typing reasons. How many other modules are out there where I run the risk of clobbering `perf_counter`? I can't think of one. Certainly not in any imports I'm going to be using here. It's such a unique name, I feel pretty safe!

I'm also going to write a small utility function that compares two timings to each other:


```
from collections import namedtuple

Timings = namedtuple('Timings', 'timing_1 timing_2 abs_diff rel_diff_perc')
def compare_timings(timing1, timing2):
    rel_diff = (timing2 - timing1)/timing1 * 100
    
    timings = Timings(round(timing1, 1),
                     round(timing2, 1),
                     round(timing2 - timing1, 2),
                     round(rel_diff, 2))
    return timings
```

##### Timing using fully qualified `module.symbol` 


```
test_repeats = 10_000_000
```


```
import math

start = perf_counter()
for _ in range(test_repeats):
    math.sqrt(2)
end = perf_counter()
elapsed_fully_qualified = end - start
print(f'Elapsed: {elapsed_fully_qualified}')
```

    Elapsed: 2.057656398357829
    

##### Timing using a directly imported symbol name:


```
from math import sqrt

start = perf_counter()
for _ in range(test_repeats):
    sqrt(2)
end = perf_counter()
elapsed_direct_symbol = end - start
print(f'Elapsed: {elapsed_direct_symbol}')
```

    Elapsed: 1.603430354697538
    

Let's see the relative and absolute time differences:


```
compare_timings(elapsed_fully_qualified, elapsed_direct_symbol)
```




    Timings(timing_1=2.1, timing_2=1.6, abs_diff=-0.45, rel_diff_perc=-22.07)



Definitely faster - but in absolute terms I really did not save a whole lot - over `10,000,000` iterations!

##### Timing using a function (fully qualified symbol)


```
import math

def func():
    math.sqrt(2)
    
start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_func_fully_qualified = end - start
print(f'Elapsed: {elapsed_func_fully_qualified}') 
```

    Elapsed: 3.2668947610088703
    


```
compare_timings(elapsed_fully_qualified, elapsed_func_fully_qualified)
```




    Timings(timing_1=2.1, timing_2=3.3, abs_diff=1.21, rel_diff_perc=58.77)



That was slower because of the function call overhead, but not by much in absolute terms considering I called `func()` `10,000,000` times!

##### Timing using a function (direct symbol)


```
from math import sqrt

def func():
    sqrt(2)
    
start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_func_direct_symbol = end - start
print(f'Elapsed: {elapsed_func_direct_symbol}')
```

    Elapsed: 2.80123663975316
    


```
compare_timings(elapsed_func_fully_qualified, elapsed_func_direct_symbol)
```




    Timings(timing_1=3.3, timing_2=2.8, abs_diff=-0.47, rel_diff_perc=-14.25)



Slower, but again not by much in absolute terms considering this was for `10,000,000` iterations.

##### Timing using a nested import (fully qualified symbol)


```
def func():
    import math
    math.sqrt(2)
    
start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_fully_qualified = end - start
print(f'Elapsed: {elapsed_nested_fully_qualified}')
```

    Elapsed: 5.041648347331877
    


```
compare_timings(elapsed_func_fully_qualified, elapsed_nested_fully_qualified)
```




    Timings(timing_1=3.3, timing_2=5.0, abs_diff=1.77, rel_diff_perc=54.33)



So definitely slower. But in absolute terms, for `10,000,000` iterations?

##### Timing using a nested import (direct symbol)


```
def func():
    from math import sqrt
    sqrt(2)
    
start = perf_counter()
for _ in range(test_repeats):
    func()
end = perf_counter()
elapsed_nested_direct_symbol = end - start
print(f'Elapsed: {elapsed_nested_direct_symbol}')
```

    Elapsed: 14.60262281403945
    


```
compare_timings(elapsed_nested_fully_qualified, elapsed_nested_direct_symbol)
```




    Timings(timing_1=5.0, timing_2=14.6, abs_diff=9.56, rel_diff_perc=189.64)



That was significantly slower! Even in absolute terms this is starting to get sloooow.

So does this mean you should put imports inside functions?

No, of course not - follow the convention, it makes code far more readable, and of course optimize your code only once you have identified the bottlenecks. 

Does this mean you shouldn't care at all about the performance of your code based on the import variants?

Again, of course not - you absolutely should.

But, there is absolutely no reason to re-write your code from 

`import math
math.sqrt(2)`

to 

`from math import sqrt
sqrt(2)
`

for **speed** reasons if during the entire lifetime of your application you only call that function `100` times... or `10,000,000` times.

Really depends on your circumstance - be aware of it, but don't try to optimize code until you know **where** you **need** to optimize!

*[I've seen people refactor parts of their code for sub-second improvements, when, in fact, the largest bottleneck was that they were opening and closing database connections at every read and write instead of pooling connections or something like that]*

And

`from module import *`

has its uses as we'll see later when we discuss packages.

It's not evil, just not very safe - again depends on your circumstance.

##  Reloading Modules

Reloading modules is something you may find yourself wanting to do if you modify the code for a module while your program is running.

Although you technically can do so, and I'll show you two ways of doing it, it's not recommended. Let me show you how to do it first, and then the pitfalls with both methods.

The safest is just to make your code changes, and restart your app.

Even if you are trying to monkey patch (change at run-time) a code module and you want everyone who uses that module to "see" the change, they very well may not, depending on how they are accessing your module.

As usual, working with external modules in Jupyter is not the easiest thing in the world, so I'm just going to create simple modules right from inside the notebook. You can just create files in the same folder as your notebook/main app instead.


```
import os

def create_module_file(module_name, **kwargs):
    '''Create a module file named <module_name>.py.
    Module has a single function (print_values) that will print
    out the supplied (stringified) kwargs.
    '''
    
    module_file_name = f'{module_name}.py'
    module_rel_file_path = module_file_name
    module_abs_file_path = os.path.abspath(module_rel_file_path)
    
    with open(module_abs_file_path, 'w') as f:
        f.write(f'# {module_name}.py\n\n')
        f.write(f"print('running {module_file_name}...')\n\n")
        f.write(f'def print_values():\n')
        for key, value in kwargs.items():
            f.write(f"\tprint('{str(key)}', '{str(value)}')\n")    
```


```
create_module_file('test', k1=10, k2='python')
```

This should have resulted in the creation of a file named `test.py` in your notebook/project directory that should look like this:

`# test.py`

`print('running test.py...')`

``def print_values():
	print('k1', '10')
	print('k2', 'python')
``

Now let's go ahead and import it using a plain `import`:


```
import test
```

    running test.py...
    


```
test
```




    <module 'test' from '/Users/fbaptiste/Desktop/Notebooks/test.py'>



And we can now call the `print_values` function:


```
test.print_values()
```

    k1 10
    k2 python
    

Now suppose, we modify the module by adding an extra key:


```
create_module_file('test', k1=10, k2='python', k3='cheese')
```


```
test.print_values()
```

    k1 10
    k2 python
    

Nope, nothing changed...

Maybe we can just re-import it?? You shoudl know the answer to that one...


```
import test
```


```
test.print_values()
```

    k1 10
    k2 python
    


```
id(test)
```




    4532635512



The module object is the same one we initially loaded - our namespace and `sys.modules` still points to that old one. Somehow we have to force Python to *reload* the module.

At this point, I hope you're thinking "let's just remove it from `sys.modules`, this way Python will not see it in the cache and rerun the import.

That's a good idea - let's try that.


```
import sys
del sys.modules['test']
```


```
import test
```

    running test.py...
    


```
test.print_values()
```

    k1 10
    k2 python
    k3 cheese
    

and, in fact, the `id` has also changed:


```
id(test)
```




    4532720568



That worked!

But here's the problem with that approach.

Suppose some other module in your program has already loaded that module using 

`import test`.

What is in their namespace? A variable (symbol) called `test` that points to which object? The one that was first loaded, not the second one we just put back into the `sys.modules` dict.

In other words, they have no idea the module changed and they'll just keep using the old object at the original memory address.

Fortunately, `importlib` has a way to reload the contents of the module object without affecting the memory address.

That is already much better.

Let's try it:


```
id(test)
```




    4532720568




```
test.print_values()
```

    k1 10
    k2 python
    k3 cheese
    


```
create_module_file('test', k1=10, k2='python', 
                   k3='cheese', k4='parrots')
```


```
import importlib

importlib.reload(test)
```

    running test.py...
    




    <module 'test' from '/Users/fbaptiste/Desktop/Notebooks/test.py'>



As we can see the module was executed...

what about the `id`?


```
id(test)
```




    4532720568



Stayed the same...

So now, let's call that function:


```
test.print_values()
```

    k1 10
    k2 python
    k3 cheese
    k4 parrots
    

As you can see, we have the correct output. And we did not have to reimport the module, which means any other module that had imported the old object, now is going to automatically be using the new "version" of the same object (same memory address)

So, all's well that ends well...

Not quite. :-)

Consider this example instead, were we use a `from` style import:


```
create_module_file('test2', k1='python')
```


```
from test2 import print_values
```

    running test2.py...
    


```
print_values()
```

    k1 python
    

Works great.

What's the `id` of `print_values`?


```
id(print_values)
```




    4532625752



Now let's modify `test2.py`:


```
create_module_file('test2', k1='python', k2='cheese')
```

And reload it using `importlib.reload`:


```
importlib.reload(test2)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-26-7b4c6fe87427> in <module>()
    ----> 1 importlib.reload(test2)
    

    NameError: name 'test2' is not defined


Ok, so we don't have `test2` in our namespace... Easy enough, let's import it directly (or get it out of `sys.modules`):


```
import test2
```


```
test2.print_values()
```

    k1 python
    


```
id(test2.print_values)
```




    4532625752




```
id(print_values)
```




    4532625752



Now let's try the reload:


```
importlib.reload(test2)
```

    running test2.py...
    




    <module 'test2' from '/Users/fbaptiste/Desktop/Notebooks/test2.py'>



OK, the module was re-imported...

Now let's run the `print_values` function:


```
test2.print_values()
```

    k1 python
    k2 cheese
    

But remember how we actually imported `print_values` from `test2`?


```
print_values()
```

    k1 python
    

Ouch - that's not right!

Let's look at the `id`s of those two functions, and compare them to what we had before we ran the reload:


```
id(test2.print_values)
```




    4533545976




```
id(print_values)
```




    4532625752



As you can see the `test2.print_values` function is a new object, but `print_values` **still** points to the old function that exists in the first "version" of `test2`.

And that is why reloading is just not safe.

If someone using your module binds directly to an attribute in your module, either via how they import:

`from test2 import print_values`

or even by doing something like this:

`pv = test2.print_values`

their binding is now set to a specific memory address.

When you reload the module, the object `test2` has ben mutated, and the `print_values` function is now a new object, but any bindings to the "old" version of the function remain.

So, in general, stay away from reloading modules dynamically.

##  How does Python import Modules?

When we run a statement such as 

`import fractions`

what is Python actually doing?

The first thing to note is that Python is doing the import at **run time**, i.e. while your code is actually running.

This is different from traditional compiled languages such as C where modules are compiled and linked at compile time.

In both cases though, the system needs to know **where** those code files exist.

Python uses a relatively complex system of how to find and load modules. I'm not going to even attempt to describe this in detail, but we'll take a brief look at the main points.

The `sys` module has a few properties that define where Python is going to look for modules (either built-in or standard library as well as our own or 3rd party):


```
import sys
```

Where is Python installed?


```
sys.prefix
```




    'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive'



Where are the compiled C binaries located?


```
sys.exec_prefix
```




    'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive'



These two properties are how virtual environments are basically able to work with different environments. Python is installed to a different set of directories, and these prefixes are manipulated to reflect the current Python location.

Where does Python look for imports?


```
sys.path
```




    ['',
     'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\python36.zip',
     'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\DLLs',
     'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\lib',
     'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive',
     'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\lib\\site-packages',
     'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\lib\\site-packages\\setuptools-27.2.0-py3.6.egg',
     'D:\\Users\\fbapt\\Anaconda3\\envs\\deepdive\\lib\\site-packages\\IPython\\extensions',
     'C:\\Users\\fbapt\\.ipython']



Basically when we import a module, Python will search for the module in the paths contained in `sys.path`. 

If it does not find the module in one of those paths, the import will fail.

So if you ever run into a problem where Python is not able to import a module or package, you should check this first to make sure the path to your module/package is in that list.

At a high level, this is how Python imports a module from file:

* checks the `sys.modules` cache to see if the module has already been imported - if so it simply uses the reference in there, otherwise:
* creates a new module object (`types.ModuleType`)
* loads the source code from file
* adds an entry to `sys.modules` with name as key and the newly created
* compiles and executes the source code

One thing that's really to important to note is that when a module is imported, the module code is **executed**.

Let's switch over to PyCharm (or your favorite IDE, which may well be VI/emacs and the command line!). All the files are included in the lecture resources or my github repository.

#### Example 1

This example shows that when we import a module, the module code is actually **executed**.

Furthermore, that module now has its own namespace that can be seen in `__dict__`.

#### Example 2

In this example, we can see that when we `import` a module, Python first looks for it in `sys.modules`.

To make the point, we put a key/value pair in `sys.modules` ourselves, and then import it.

In fact we put a function in there instead of a module, and import that.

Please **DO NOT** this, I'm just making the point that `import` will first look in the cache and immediately just return the object if the name is found, basically just as if we had written:

`
module = sys.modules['module']
`


```
sys.modules['test'] = lambda: 'Testing module caching'
```


```
import test
```

See, it got the "module" from sys...


```
test
```




    <function __main__.<lambda>>




```
test()
```




    'Testing module caching'



#### Example 3a

In this example we look at a simplified view of how Python imports a module.

We use two built-in functions, `compile` and `exec`.

The `compile` function compiles source (e.g. text) into a code object.

The `exec` function is used to execute a code object. Optionally we can specify what dictionary should be used to store global symbols.

In our case we are going to want to use our module's `__dict__`.

#### Example 3b

This is essentially the same as example 3a, except we make our importer into a function and use it to show how we technically should look for a cached version of the module first.

# Section 10 - Extras

##  What's New in Python 3.6

Here are just a few highlights.

For the full monty (python), read it here:

`https://docs.python.org/3/whatsnew/3.6.html`

I will create some additional videos looking at each of these in more detail.

#### Dictionaries maintain sort order

Dictionaries will maintain their key order based on when items were inserted. 
This is an implementation detail in 3.6 (i.e. the behavior happens because of the new implementation of dicts, but not guaranteed in the sense that a future release could change that). However, there seems to be official confirmation from GvR that starting in 3.7 it will be guaranteed.
If you use `prettyprint` be careful as that sorts the dictionary keys lexicographically before printing and this will still be the case in 3.7 (after much debate over it in the Python dev community!)

#### Preserving Order of **kwargs in Function Arguments

This is actually unrelated to the dict key order preservation. 
The order in which `**kwarg` arguments are passed to a function is retained when you iterate the `kwarg` parameter inside the called function.

This is actually a big deal. I'll show you how this allows us to easily create a named tuple factory function with default values for example.

#### Underscores in Numeric Literals

This one is also really nice to help readability. You can now use underscores in numeric literals.

For example:


```
1_000_000
```




    1000000




```
0x_FFFF_FFFF
```




    4294967295



#### f-Strings

A much simpler string interpolation. You can embed Python expressions directly into strings (including multi-line) as well as the usual string formatting directives just by preceding the string with an `f` or `F`.

For example:


```
numerator = 10
denominator = 3
response = f'{numerator}/{denominator} = {numerator / denominator:0.3f}'
print(response)
```

    10/3 = 3.333
    

#### Type Annotations

Basically allows us to provide type information to function arguments, class variables, etc.

More info in PEP 484 and PEP 526.

According to PEP 484:

"It should also be emphasized that **Python will remain a dynamically typed language, and the authors have no desire to ever make type hints mandatory, even by convention**."

Tools that make use of these type annotations include `mypy`, `PyCharm`. Probably others too.

Here's an example of type annotations:


```
from typing import List
```


```
def squares(l: List[int]) -> List[int]:
    return [e ** 2 for e in l]
```


```
my_list: List[int] = [1, 2, 3, 4]
```


```
my_list, squares(my_list)
```




    ([1, 2, 3, 4], [1, 4, 9, 16])



But Python does not use those annotations - here I am passing a dictionary to the function (with integer keys so the function still works properly). Obviously dictionaries are not lists!


```
d = {1: 'a', 2: 'b', 3:'c', 4:'d'}
squares(d)
```




    [1, 4, 9, 16]



The type annotations **do not affect** Python itself - it is simply a set of syntactic additions that allows **external** tools such as `mypy` or `PyCharm` to perform static type checking.

#### Asynchronous Enhancements

This is beyond the scope of Part 1, but really useful additions worth at least mentioning have been added to the Python language to better support asynchronous programming (I'll cover that in detail in subsequent parts of the course series - most likely Part 4)

#### Plus a LOT more

There's a lot more to really love in 3.6, and you can read all about it here:

`https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep526`

##  Python 3.6 - Dictionary Ordering

Python 3.6 sees a new implementation of the standard `dict` that preserves key ordering (based on the order in which new keys are added into or removed from the dictionary)

Although this is an implementation detail in 3.6, it is supposed to become official in Python 3.7. 

`https://mail.python.org/pipermail/python-dev/2017-December/151283.html`

So it should be safe to now assume dictionary keys will retain order , and using an `OrderedDict` might no longer be needed for certain cases. I'll come back to `OrderedDict` in a bit...

**Use for Python 3.6 and higher only!**

If you use that ordering feature with standard `dict` objects and then try to run your code in a prior version, things will break :-)



Also means that `keys()` (that iterate from left to right) preserves order as does `values()`. On the other hand `popitem()` will pop right-most element from dictionary. Sounds like stack behavior to me - but does not mean you should use it as such - I'm pretty sure that's not going to be as efficient as say using a list!.

Let's see some of this (just make sure you're running 3.6 or higher)


```
from sys import version_info
```


```
version_info
```




    sys.version_info(major=3, minor=6, micro=2, releaselevel='final', serial=0)




```
d = {'a': 1, 'b': 2}
```


```
d.keys(), d.values(), d.items()
```




    (dict_keys(['a', 'b']), dict_values([1, 2]), dict_items([('a', 1), ('b', 2)]))




```
d['x'] = 3
```


```
d.keys(), d.values(), d.items()
```




    (dict_keys(['a', 'b', 'x']),
     dict_values([1, 2, 3]),
     dict_items([('a', 1), ('b', 2), ('x', 3)]))




```
del d['b']
```


```
d.keys(), d.values(), d.items()
```




    (dict_keys(['a', 'x']), dict_values([1, 3]), dict_items([('a', 1), ('x', 3)]))




```
d['b'] = 4
```


```
d.keys(), d.values(), d.items()
```




    (dict_keys(['a', 'x', 'b']),
     dict_values([1, 3, 4]),
     dict_items([('a', 1), ('x', 3), ('b', 4)]))



What about replacing a value for an existing key?


```
d['x'] =100
```


```
d.keys(), d.values(), d.items()
```




    (dict_keys(['a', 'x', 'b']),
     dict_values([1, 100, 4]),
     dict_items([('a', 1), ('x', 100), ('b', 4)]))



Order maintained...

And if we pop:


```
d.popitem()
```




    ('b', 4)



We popped the last item.

So now I'm left wondering how to pick a *random* item from the dictionary?
(Not that we could before - it might have looked random when we popped an item but it wasn't)

Sounds like another video :-)

**Important note:** Be careful of Jupyter notebooks - something I just realized - take a look:


```
d = {'x': 1, 'a': 2}
```


```
print(d)
```

    {'x': 1, 'a': 2}
    


```
d
```




    {'a': 2, 'x': 1}



Notice how just letting Jupyter display `d` changed the display order of the keys? (I'm guessing its doing something similar to `prettyprint` (or maybe even using it), which changes the displayed key order to be lexicographical.

What about using `update` to update one dict based on another (inserting missing keys, and updating common ones - but especially the insertion bit) - I'm guessing the order is retained with any insertions appearing at the end and ordered according to the dict being merged in. Let's see:


```
d1 = {'a': 1, 'b': 200}
d2 = {'a': 100, 'd':300, 'c':400}
```


```
d1.update(d2)
```


```
print(d1)
```

    {'a': 100, 'b': 200, 'd': 300, 'c': 400}
    

Back to `OrderedDict` for a second:

`OrderedDict` has a few methods that afaik have no equivalent (yet) in standard dicts:
* `move_to_end(key, last=True)` - either move to front or back
* `popitem(last=True)` - that can pop either from front or back of dict
* supports reverse iteration using `reversed()`

Let's take each one of those one by one:

**move to end:**


```
d = {'a':1, 'b':2, 'c':3}
print('start:', d)
d['a'] = d.pop('a')
print('moved a to end:',d)
```

    start: {'a': 1, 'b': 2, 'c': 3}
    moved a to end: {'b': 2, 'c': 3, 'a': 1}
    

**move to front:**

That's one not so easy, the only option I can think of is to move all the keys around to re-order. Maybe something like this:


```
d = {'a':1, 'b':2, 'c':3, 'x':100, 'y':200}
print('start:', d)
d['c'] = d.pop('c')
print('moved c to end:', d)

for i in range(len(d)-1):
    key = next(iter(d.keys()))
    d[key] = d.pop(key)
print('moved c to front:', d)
```

    start: {'a': 1, 'b': 2, 'c': 3, 'x': 100, 'y': 200}
    moved c to end: {'a': 1, 'b': 2, 'x': 100, 'y': 200, 'c': 3}
    moved c to front: {'c': 3, 'a': 1, 'b': 2, 'x': 100, 'y': 200}
    

**pop last item:**

That one's trivial - just use `popitem`:


```
d = {'a':1, 'b':2, 'c':3, 'x':100, 'y':200}
print('start:', d)
d.popitem()
print('pop last item:', d)
```

    start: {'a': 1, 'b': 2, 'c': 3, 'x': 100, 'y': 200}
    pop last item: {'a': 1, 'b': 2, 'c': 3, 'x': 100}
    

**pop first item:**

Not too difficult - we just need to identify the *first* key, and pop it.


```
d = {'a':1, 'b':2, 'c':3, 'x':100, 'y':200}
print('start:', d)
key = next(iter(d.keys()))
d.pop(key)
print('pop first item:', d)
```

    start: {'a': 1, 'b': 2, 'c': 3, 'x': 100, 'y': 200}
    pop first item: {'b': 2, 'c': 3, 'x': 100, 'y': 200}
    

If you're interested, here's Raymond Hettinger's pure Python "version" of his C dict implementation:
`http://code.activestate.com/recipes/578375/`

##  Python 3.6: Preserved Order of **kwargs

PEP468 was accepted into 3.6, and this means that the order in which keyword arguments are collected into `**kwargs` is now maintained.

Why does that matter you ask?

Well, how about a function that takes in kwargs and needs to build an ordered type based on the *order* of the kwargs. In the past you would have had to use some workaround (often using an ordered dict) instead of the far more convenient `**kwargs` approach.

Let me show you what I mean:

Suppose we want to write a `namedtuple` factory of our own where we can specify default values:
    


```
from collections import namedtuple

def defaulted_namedtuple(class_name, **fields):
    Struct = namedtuple(class_name, fields.keys())
    Struct.__new__.__defaults__ = tuple(fields.values())
    return Struct    
```


```
Vector2D = defaulted_namedtuple('Vector2D', 
                                x1=None, y1=None,
                                x2=None, y2=None,
                                origin_x=0, origin_y=0)
```


```
Vector2D._fields
```




    ('x1', 'y1', 'x2', 'y2', 'origin_x', 'origin_y')




```
v1 = Vector2D(10, 10, 20, 20)
```


```
v1
```




    Vector2D(x1=10, y1=10, x2=20, y2=20, origin_x=0, origin_y=0)



This only works if the order of the keyword arguments passed to the function is retained in the `fields` dictionary!

##  Python 3.6 - Underscores in Numeric Literals

We can now intersperse underscores (`_`) in numeric literals.

Makes things easier to read:

`10_000_000` vs `10000000`

Works for floats as well:


```
30_000.05
```




    30000.05



But don't lead or end with the underscore!

Works for hex numbers too:


```
0x_FF_FFFF, 0x_F_F_F_F_F_F
```




    (16777215, 16777215)



(Just to show it does not matter how many digits are between the underscores)

By the way, string formatting now supports that too - thousand separators for decimal integers and floats and every 4 digits for binary(`b`), octal(`o`), and hex(`x`, `X`).


```
'{:_}'.format(10000)
```




    '10_000'




```
'{:_X}'.format(16777215)
```




    'FF_FFFF'



Works in string conversions too:


```
int('FF_FF', 16)
```




    65535




```
int('0b_1_0000_0000', 2)
```




    256



Pretty cool!

##  Python 3.6 - f-Strings

Last highlight I want to mention are the new f-strings. For more details see PEP498.

f-Strings is short for *formatted string literals*

You should already know how to format strings using the `format` method:


```
# Using {}
'{} % {} = {}'.format(10, 3, 10 % 3)
```




    '10 % 3 = 1'




```
# Using {number}
'{1} % {2} = {0}'.format(10 % 3, 10, 3)
```




    '10 % 3 = 1'




```
# Using {name}
'{a} % {b} = {mod}'.format(a=10, b=3, mod=10 % 3)
```




    '10 % 3 = 1'



But now we can also do this:


```
a = 10
b = 3
f'{a} % {b} = {a % b}'
```




    '10 % 3 = 1'



Basically in f-strings you can use expressions and reference variables inside your string which Python will then interpolate. Also uses all the existing string formatting options (`:0.5f` for example):


```
a = 10 / 3

f'{a:0.5f}'
```




    '3.33333'



So now, instead of writing:


```
name = 'Python'
'{name} rocks'.format(name=name)
```




    'Python rocks'



which used the word `name` **three** times, we can simply say:


```
name = 'Python'
f'{name} rocks!'
```




    'Python rocks!'



Much more concise!

How about with closures?


```
def outer():
    name = 'Python'
    
    def inner():
        return f'{name} rocks!'
    
    return inner
```


```
print(outer()())
```

    Python rocks!
    

Woohoo!! That works too - note that we did not have to reference `name` (to make it a free variable in `inner`) before using it **inside** the f-string.

I can see this open to abuse though...


```
sq = lambda x: x**2
a = 10
b=1
print(f'{sq(a) if b > 5 else a}')

b=10
print(f'{sq(a) if b > 5 else a}')
```

    10
    100
    

Or even this:


```
a = 10
b = 1
print(f'{(lambda x: x**2)(a) if b > 5 else a}')

b=10
print(f'{(lambda x: x**2)(a) if b > 5 else a}')
```

    10
    100
    

Lord help us... :-)

##  Random Seeds

The `random` module provides a variety of functions related to (pseudo) random numbers.

The problem when you use random numbers in your code is that it can be difficult to debug because the same random number sequence is not the same from run to run of your program. If your code fails somewhere in the middle of a run it is difficult to make the problem **repeatable**. Debugging intermittent and non-repeatable failures is one of the worst things to do!

Fortunately, when using the `random` module, we can set the `seed` for the random underlying random number generator.

Random numbers are not truly random - they are generated in such a way that the numbers *appear* random and evenly distributed, but in fact they are being generated using a specific algorithm.

That algorithm depends on a **seed** value. That seed value will determine the exact sequence of randomly generated numbers (so as you can see, it's not truly random). Setting different seeds will result in different random sequences, but setting the seed to the same value will result in the same sequence being generated.

By default, the seed uses the system time, hence every time you run your program a different seed is set. But we can easily set the seed to something specific - very useful for debugging purposes.


```
import random
```


```
for _ in range(10):
    print(random.randint(10, 20), random.random())
```

    15 0.2744539473546337
    13 0.8696250242406662
    14 0.3697144258854075
    18 0.5945778682818538
    15 0.7694636962835182
    17 0.820862450549917
    10 0.6467347679589829
    20 0.8048988506681894
    12 0.5880472380199475
    20 0.8715275342775027
    


```
for _ in range(10):
    print(random.randint(10, 20), random.random())
```

    14 0.931305656287958
    10 0.23039405306234007
    12 0.8337388005835649
    18 0.4590462920405187
    10 0.36743475564890316
    13 0.7100875772566404
    12 0.9750441656612154
    12 0.7442020027100001
    18 0.23667309950795434
    20 0.41553858798609267
    

As you can see the sequence of numbers is not the same (and even restarting the kernel will result in different numbers).

We can set the **seed** as follows:


```
random.seed(0)
for i in range(10):
    print(random.randint(10, 20), random.random())
```

    16 0.7579544029403025
    16 0.04048437818077755
    18 0.48592769656281265
    14 0.9677999949201714
    15 0.5833820394550312
    13 0.5046868558173903
    14 0.1397457849666789
    11 0.6183689966753316
    14 0.9872592010330129
    18 0.9827854760376531
    

If we run this code again, the sequence will still be different:


```
for i in range(10):
    print(random.randint(10, 20), random.random())
```

    19 0.9021659504395827
    14 0.09876334465914771
    11 0.8988382879679935
    20 0.33019721859799855
    18 0.1007012080683658
    16 0.31619669952159346
    20 0.9130110532378982
    18 0.47700977655271704
    18 0.2604923103919594
    18 0.9159944803568847
    

Instead what we have to do is reset the seed (which happens if you set the seed to a specific number at the start of running your program - then evey random number generated will be repeatable from run to run).

Here, we just need to reset the seed before running that loop to get the same effect:


```
random.seed(0)
for i in range(20):
    print(random.randint(10, 20), random.random())
```

    16 0.7579544029403025
    16 0.04048437818077755
    18 0.48592769656281265
    14 0.9677999949201714
    15 0.5833820394550312
    13 0.5046868558173903
    14 0.1397457849666789
    11 0.6183689966753316
    14 0.9872592010330129
    18 0.9827854760376531
    19 0.9021659504395827
    14 0.09876334465914771
    11 0.8988382879679935
    20 0.33019721859799855
    18 0.1007012080683658
    16 0.31619669952159346
    20 0.9130110532378982
    18 0.47700977655271704
    18 0.2604923103919594
    18 0.9159944803568847
    


```
random.seed(0)
for i in range(20):
    print(random.randint(10, 20), random.random())
```

    16 0.7579544029403025
    16 0.04048437818077755
    18 0.48592769656281265
    14 0.9677999949201714
    15 0.5833820394550312
    13 0.5046868558173903
    14 0.1397457849666789
    11 0.6183689966753316
    14 0.9872592010330129
    18 0.9827854760376531
    19 0.9021659504395827
    14 0.09876334465914771
    11 0.8988382879679935
    20 0.33019721859799855
    18 0.1007012080683658
    16 0.31619669952159346
    20 0.9130110532378982
    18 0.47700977655271704
    18 0.2604923103919594
    18 0.9159944803568847
    

As you can see, the sequence of random numbers generated is now the same every time.

What's interesting is that even functions like `shuffle` will shuffle in the same order!

Let's see this:


```
def generate_random_stuff(seed=None):
    random.seed(seed)
    results = []
    
    # randint will generate the same sequence (for same seed)
    for _ in range(5):
        results.append(random.randint(0, 5))
    
    # even shuffling generates in the same way (for same seed)
    characters = ['a', 'b', 'c']
    random.shuffle(characters)
    results.append(characters)
    
    # same with the Gaussian distribution
    for _ in range(5):
        results.append(random.gauss(0, 1))
        
    return results
```


```
print(generate_random_stuff())
```

    [4, 3, 2, 0, 5, ['b', 'c', 'a'], 0.2753548343351636, -0.5989933403172317, -0.6515943978936821, 1.7412073870280294, 0.24161779723044724]
    


```
print(generate_random_stuff())
```

    [3, 5, 1, 5, 3, ['c', 'a', 'b'], -0.6334510789171736, -0.3564859849845763, 0.46562328656890606, -2.1891281426767746, -1.1983958517185107]
    

Now let's use a seed value:


```
print(generate_random_stuff(0))
```

    [3, 3, 0, 2, 4, ['a', 'c', 'b'], 1.6391095109274887, -0.9249345372119703, 0.9223306019157185, -0.1891931090669293, 0.5456115709634167]
    


```
print(generate_random_stuff(0))
```

    [3, 3, 0, 2, 4, ['a', 'c', 'b'], 1.6391095109274887, -0.9249345372119703, 0.9223306019157185, -0.1891931090669293, 0.5456115709634167]
    

As long as we use the same seed value the results are repeatable. But if we set different seed values the sequences will be different (but still be the same for the same seed):


```
print(generate_random_stuff(100))
```

    [1, 3, 3, 1, 5, ['a', 'c', 'b'], -1.639893943131093, 0.7278930291928233, -0.4000719319137612, -0.08390378703116254, -0.3013546798244102]
    


```
print(generate_random_stuff(100))
```

    [1, 3, 3, 1, 5, ['a', 'c', 'b'], -1.639893943131093, 0.7278930291928233, -0.4000719319137612, -0.08390378703116254, -0.3013546798244102]
    

Lastly let's see how we would calculate the frequency of randomly generated integers, just to see how even the distribution is.

Basically, given a sequence of random integers, we are going to create a dictionary that contains the integers as keys, and the values will the frequency of each:


```
def freq_analysis(lst):
    return {k: lst.count(k) for k in set(lst)}
```


```
lst = [random.randint(0, 10) for _ in range(100)]
```


```
print(lst)
```

    [7, 8, 6, 1, 6, 1, 2, 6, 7, 9, 1, 5, 4, 6, 1, 9, 4, 10, 5, 5, 4, 0, 8, 3, 1, 7, 7, 3, 6, 1, 8, 0, 5, 7, 3, 5, 0, 7, 6, 1, 4, 9, 3, 6, 9, 4, 3, 2, 5, 0, 1, 6, 5, 7, 9, 1, 0, 5, 6, 2, 10, 2, 4, 0, 2, 1, 8, 9, 7, 3, 5, 7, 2, 10, 4, 8, 1, 10, 4, 10, 6, 10, 0, 5, 8, 8, 10, 7, 4, 8, 10, 3, 9, 8, 3, 9, 3, 5, 8, 8]
    


```
random.seed(0)
freq_analysis(lst)
```




    {0: 7, 1: 11, 2: 6, 3: 9, 4: 9, 5: 11, 6: 10, 7: 10, 8: 11, 9: 8, 10: 8}




```
random.seed(0)
freq_analysis([random.randint(0, 10) for _ in range(1_000_000)])
```




    {0: 90935,
     1: 91184,
     2: 91002,
     3: 91042,
     4: 90766,
     5: 91072,
     6: 90678,
     7: 90985,
     8: 90409,
     9: 91383,
     10: 90544}



Of course, it usually pays to know what's in the standard library :-)

The collections library has a Counter class that can be used to do this precise thing!


```
from collections import Counter
```


```
random.seed(0)
Counter([random.randint(0, 10) for _ in range(1_000_000)])
```




    Counter({0: 90935,
             1: 91184,
             2: 91002,
             3: 91042,
             4: 90766,
             5: 91072,
             6: 90678,
             7: 90985,
             8: 90409,
             9: 91383,
             10: 90544})



##  Random Choices

How would you pick a random element from a list?

You might be tempted to use the `random` library to pick a random index (integer) and use that random index to retrieve the element from the list (or more genrally sequence).

Something like this:


```
import random
```

I'm going to set a seed so we always generate the same random sequences:


```
random.seed(0)
```


```
l = [10, 20, 30, 40, 50, 60]
```


```
random_index = random.randrange(len(l))
```


```
l[random_index]
```




    40



So to do this 10 times we would write:


```
random.seed(0)
for i in range(10):
    print(l[random.randrange(len(l))])
```

    40
    40
    10
    30
    50
    40
    40
    30
    40
    30
    

Although this certainly works, it's not very Pythonic. Instead we can use the `choice` function in the `random` module that picks a random element from any given sequence. (Again I'm going to set a seed so we can generate the same random sequence).


```
random.seed(0)
for _ in range(10):
    print(random.choice(l))
```

    40
    40
    10
    30
    50
    40
    40
    30
    40
    30
    

Wasn't that much cleaner code?

But still, there has to be a better way to generate 10 random choices without resorting to a "common" loop :-)

The `random` module also has a `choices` method which allows us to choose multiple random choices (as opposed to `choice` which only picks one).

The thing is, `choices` has a few more advanced features built in.

Let's start with the basics.

Suppose I want to choose n elements randomly from some sequence:


```
list_1 = list(range(1000))
```


```
random.choices(list_1, k=5)
```




    [583, 908, 504, 281, 755]




```
for _ in range(5):
    print(random.choices(list_1, k=3))
```

    [618, 250, 909]
    [982, 810, 902]
    [310, 729, 898]
    [683, 472, 100]
    [434, 610, 913]
    

Now the thing about `choices` is that it does the selection *with replacement*. This means that the same item could show up more than once in the same call to `choices`. To see this, let's use a shorter list:


```
list_2 = ['a', 'b', 'c']
```


```
random.seed(0)
for _ in range(10):
    print(random.choices(list_2, k=2))
```

    ['c', 'c']
    ['b', 'a']
    ['b', 'b']
    ['c', 'a']
    ['b', 'b']
    ['c', 'b']
    ['a', 'c']
    ['b', 'a']
    ['c', 'c']
    ['c', 'c']
    

As you can see we have some results that contain the same element twice.

What this means, is that we can make the sample size *larger* than the population:


```
list_2
```




    ['a', 'b', 'c']




```
for _ in range(10):
    print(random.choices(list_2, k=5))
```

    ['a', 'c', 'c', 'c', 'b']
    ['a', 'b', 'b', 'c', 'c']
    ['b', 'c', 'a', 'c', 'b']
    ['a', 'c', 'b', 'c', 'c']
    ['a', 'b', 'c', 'a', 'a']
    ['c', 'a', 'b', 'a', 'c']
    ['c', 'b', 'a', 'a', 'b']
    ['c', 'a', 'b', 'c', 'b']
    ['c', 'b', 'c', 'b', 'b']
    ['b', 'b', 'b', 'b', 'a']
    

In addition, we can also specify a weight for each item in the population. This essentially allows us to have certain items be picked more often than others. The weight list must be the same length as the population.


```
weights_2 = [10, 1, 1]
```


```
for _ in range(10):
    print(random.choices(list_2, k=5, weights=weights_2))
```

    ['a', 'a', 'a', 'a', 'a']
    ['a', 'a', 'b', 'c', 'b']
    ['b', 'c', 'a', 'a', 'a']
    ['a', 'a', 'b', 'b', 'a']
    ['c', 'a', 'a', 'a', 'c']
    ['c', 'a', 'a', 'a', 'a']
    ['a', 'b', 'a', 'a', 'a']
    ['a', 'a', 'a', 'a', 'a']
    ['a', 'a', 'a', 'a', 'b']
    ['a', 'a', 'a', 'a', 'a']
    

As you can see, we see a whole lot more of `a` than the other characters.

We can skew the results even more, simply by increasing the weight for `a`:


```
weights_2 = [100, 1, 1]
```


```
for _ in range(10):
    print(random.choices(list_2, k=5, weights=weights_2))
```

    ['a', 'a', 'a', 'b', 'a']
    ['a', 'a', 'a', 'a', 'a']
    ['a', 'a', 'a', 'a', 'a']
    ['a', 'a', 'a', 'a', 'a']
    ['a', 'a', 'a', 'b', 'a']
    ['a', 'a', 'a', 'a', 'a']
    ['a', 'a', 'a', 'a', 'a']
    ['a', 'a', 'a', 'a', 'a']
    ['a', 'a', 'a', 'a', 'a']
    ['a', 'a', 'a', 'a', 'a']
    

Let's see if we can count the frequency of each element that is returned by `choices`.

To do that we are going to use a comprehension. While we're at it we'll calculate also the relative frequency of each item.


```
from collections import namedtuple

Freq = namedtuple('Freq', 'count freq')

def freq_counts(list_):
    total = len(list_)
    return {k: Freq(list_.count(k), 100 * list_.count(k)/total) for k in set(list_)}
```


```
freq_counts(random.choices(list_2, k=1000))
```




    {'c': Freq(count=335, freq=33.5),
     'b': Freq(count=334, freq=33.4),
     'a': Freq(count=331, freq=33.1)}



As you can see, the distribution is pretty even. Now let's skew thing a little:


```
random.seed(0)
freq_counts(random.choices(list_2, k=1_000, weights=(8, 1, 1)))
```




    {'c': Freq(count=104, freq=10.4),
     'b': Freq(count=86, freq=8.6),
     'a': Freq(count=810, freq=81.0)}



And the relative frequency of `a` is:

Which matches what we would expect since we gave `a` a weight of `8` out of a total sum of weights of `10` - so 80%.

Of course, the more elements we pick, the closer this value should get to the theoretical:


```
freq_counts(random.choices(list_2, k=10_000, weights=(8, 1, 1)))
```




    {'c': Freq(count=942, freq=9.42),
     'b': Freq(count=1062, freq=10.62),
     'a': Freq(count=7996, freq=79.96)}



You can also specify the weights as cumulative weights:

So instead of `8, 1, 1` as weights, we could provide cumulative weights as `8, 9, 10`:


```
random.seed(0)
freq_counts(random.choices(list_2, k=1_000, cum_weights = (8, 9, 10)))
```




    {'c': Freq(count=104, freq=10.4),
     'b': Freq(count=86, freq=8.6),
     'a': Freq(count=810, freq=81.0)}



And we get the same thing.

As a bonus, how would we go about generating 50 evenly distributed random numbers between 0 and 100 (inclusive) say?

We could certainly use the `randint` function and put that into a loop 50 times:


```
l = []
for _ in range(50):
    l.append(random.randrange(101))
print(l)
```

    [85, 84, 99, 32, 95, 78, 24, 8, 70, 54, 35, 22, 67, 21, 8, 84, 81, 20, 74, 14, 64, 80, 69, 77, 49, 96, 55, 34, 39, 36, 1, 54, 99, 91, 35, 33, 68, 67, 70, 40, 43, 24, 90, 100, 55, 18, 0, 96, 65, 19]
    

But we could just use the `choices` method instead with a range(101):


```
l = random.choices(range(101), k=50)
print(l)
```

    [79, 70, 78, 38, 46, 3, 92, 64, 80, 76, 90, 36, 99, 16, 19, 35, 70, 1, 74, 57, 24, 18, 76, 42, 57, 23, 72, 87, 90, 81, 10, 19, 44, 6, 43, 39, 27, 44, 76, 35, 33, 31, 49, 77, 20, 40, 43, 64, 67, 70]
    

Only caution here is if you are generating random things on multiple threads - in which case you don't know when what thread is going to run and in that case you very well may end up with different random results from the various threads from run to run - even if you use a specific seed.

Here's one practical application of being able to skew random selections.

Let's say you want to know what's more efficient - guarding a divide by zero exception using a LBYL (look before you leap) approach, or EAFP (easier to ask for forgiveness than permission):


```
from time import perf_counter
```


```
denominators = random.choices([0, 1], k=1_000_000)
```


```
start = perf_counter()
for denominator in denominators:
    if denominator == 0:
        continue
    else:
        10 / denominator
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)}')   
```

    Avg elapsed time: 1.5108646599946952e-07
    


```
start = perf_counter()
for denominator in denominators:
    try:
        10 / denominator
    except ZeroDivisionError:
        continue

end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)}')
```

    Avg elapsed time: 3.9199999800075604e-07
    

As we can see it looks like the `try... except...` appeoach is slower.

But in reality, we expect that a zero will only occur 10% of the time.

So now we can test this using a skewed set of random denominators:


```
denominators = random.choices([0, 1], k=1_000_000, weights=[1, 9])
```


```
start = perf_counter()
for denominator in denominators:
    if denominator == 0:
        continue
    else:
        10 / denominator
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)}')
```

    Avg elapsed time: 1.9064371899912659e-07
    


```
start = perf_counter()
for denominator in denominators:
    try:
        10 / denominator
    except ZeroDivisionError:
        continue
        
end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denominators)}')
```

    Avg elapsed time: 1.7348390699953599e-07
    

##  Random Samples

I just want to show you a variant on `random.choices` that we saw in the previous video.

`choices` chooses `k` random elements from some sequence, **with replacement**.

This means we could create a random selection containing more elements than we started off with:


```
import random
```


```
random.choices(list('abc'), k=10)
```




    ['c', 'c', 'a', 'c', 'c', 'b', 'b', 'b', 'b', 'c']



Sometimes however, we do not want that replacement - instead we want a population sample (so once an element has been randomly selected, it cannot be selected again).

This is where the `sample` function comes in - it does exactly that. Of course, we can no longer pick more elements than we have in our population. Also, picking a sample equal in size to the population basically returns a "shuffled" population.


```
l = range(20)
```


```
random.sample(l, k=10)
```




    [15, 6, 3, 14, 17, 2, 13, 10, 12, 1]



We can even set the sample size equal to the population size:


```
random.sample(l, k=20)
```




    [8, 12, 2, 5, 0, 11, 13, 15, 6, 10, 14, 16, 1, 9, 19, 18, 17, 7, 4, 3]



But no larger than the population size:


```
random.sample(l, 50)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-13-68df5ccfcccb> in <module>()
    ----> 1 random.sample(l, 50)
    

    D:\Users\fbapt\Anaconda3\envs\deepdive\lib\random.py in sample(self, population, k)
        315         n = len(population)
        316         if not 0 <= k <= n:
    --> 317             raise ValueError("Sample larger than population or is negative")
        318         result = [None] * k
        319         setsize = 21        # size of a small set minus size of an empty list
    

    ValueError: Sample larger than population or is negative


Also worth pointing out is that if you set a specific seed, you will get repeatability of your sample selection:


```
random.seed(0)
random.sample(l, k=5)
```




    [12, 13, 1, 8, 15]




```
random.seed(0)
random.sample(l, k=5)
```




    [12, 13, 1, 8, 15]



Let's see how we might use this to select some cards from a deck - obviously we don't want replacement here - once a card has ben picked from a deck it's no longer available for a second random pick.


```
suits = 'C', 'D', 'H', 'A'
ranks = tuple(range(2,11)) + tuple('JQKA')
```


```
suits
```




    ('C', 'D', 'H', 'A')




```
ranks
```




    (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')



Now we have to combine suits and ranks to form a deck.


```
deck = [str(rank) + suit for suit in suits for rank in ranks]
```


```
print(deck)
```

    ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH', '2A', '3A', '4A', '5A', '6A', '7A', '8A', '9A', '10A', 'JA', 'QA', 'KA', 'AA']
    

Let's import `Counter` from the collections module to make sure we have no repitition when we pull a sample vs when we use `choices`.


```
from collections import Counter
```


```
Counter(random.sample(deck, k=20))
```




    Counter({'10C': 1,
             '10D': 1,
             '10H': 1,
             '2A': 1,
             '2D': 1,
             '3A': 1,
             '5D': 1,
             '6A': 1,
             '6C': 1,
             '6H': 1,
             '7D': 1,
             '8C': 1,
             '8D': 1,
             '8H': 1,
             'AD': 1,
             'JC': 1,
             'JD': 1,
             'KA': 1,
             'KH': 1,
             'QA': 1})



But if we used `choices` most likely we'll get some repetitions:


```
Counter(random.choices(deck, k=20))
```




    Counter({'10A': 1,
             '10H': 1,
             '2C': 2,
             '2D': 1,
             '4A': 1,
             '4H': 1,
             '5A': 1,
             '7A': 1,
             '7C': 1,
             '7H': 1,
             '8A': 1,
             '9D': 1,
             'AC': 1,
             'AD': 1,
             'JD': 1,
             'KA': 1,
             'KD': 2,
             'KH': 1})



##  Timing code using timeit

When we were looking at decorators we wrote a timing decorator. It could even take a number of repititions as a parameter. This can be handy to time functions directly in your code without affecting the result of the function. But it wrote the results out to the console, and sometimes we just want to access the timing data right inside our Python code.

The `timeit` module in Python is an alternative that works well for some things. It is a little more complicated to use because it runs 'outside' of our local namespace, and you have to pass just small snippets of code to it (well you pass multi-line chunks of code, but it gets tedious), and you also have to make it aware of you global or local scope if that's needed by the code you want to time. One thing it does that we did not do was *temporarily disable* the garbage collector. Still, there are a lot of pitfalls to benchmarking, and this approach like ours, is good enough for most cases. YMMV.

It has the advantage that it can also be run directly from the command line.

Let's take a look at it.


```
from timeit import timeit
```

We look at the `timeit` function. There are a few others but this is the main one and the remaining are slight variations that you may find useful, so check out the Python docs for more info.

Basically the `timeit` function needs to know a few things:

- the Python statement to run (the **stmt** argument)
- how many times to run the same code (the **number** argument - watch out, the default is `1_000_000` times!)
- any setup code (like imports) (the **setup** argument)
- an optional scope that acts like a global scope to the statement (the **globals** argument)

It will then execute the test `number` of times and return the **total** time elapsed (not an average per test).

Let's start with a simple example, where we want to time how long it takes to run the `sqrt` function in the `math` module using two different ways of importing it:

The first case we want to time is the following:


```
import math
math.sqrt(2)
```




    1.4142135623730951



vs


```
from math import sqrt
sqrt(2)
```




    1.4142135623730951



As you can see in the first example we have to specify `name.sqrt` every time we want to call the `sqrt` function. Is there a time difference between those two approaches?

Let's timeit!


```
timeit(stmt='math.sqrt(2)')
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-1d802ee02f1d> in <module>()
    ----> 1 timeit(stmt='math.sqrt(2)')
    

    D:\Users\fbapt\Anaconda3\envs\deepdive\lib\timeit.py in timeit(stmt, setup, timer, number, globals)
        231            number=default_number, globals=None):
        232     """Convenience function to create Timer object and call timeit method."""
    --> 233     return Timer(stmt, setup, timer, globals).timeit(number)
        234 
        235 def repeat(stmt="pass", setup="pass", timer=default_timer,
    

    D:\Users\fbapt\Anaconda3\envs\deepdive\lib\timeit.py in timeit(self, number)
        176         gc.disable()
        177         try:
    --> 178             timing = self.inner(it, self.timer)
        179         finally:
        180             if gcold:
    

    D:\Users\fbapt\Anaconda3\envs\deepdive\lib\timeit.py in inner(_it, _timer)
    

    NameError: name 'math' is not defined


UhOh... we get an exception. Basically `timeit` has no idea what the `math` module is! Remember what I said that it runs inside its own name space?

We can fix this in three ways:

**First** way we can simply add the import to the statement we want to time.


```
timeit(stmt = 'import math\nmath.sqrt(2)')
```




    0.31814690955189917



This is bad for two reasons: readability obviously, but also the timing is now going to include timing the `import math` statement **every time** as well. That's not how our imports work in Python. We import once and then use that imported module over and over again. 

**Second** way is to use the `setup` argument - basically that allows us to setup the runtime environment of whatever code snippet we want to run. That setup code is only run once, not for every test:


```
timeit(stmt = 'math.sqrt(2)', setup='import math')
```




    0.15629067671147823



As you can see this ran faster than importing at every test.

**Third** way is to provide `timeit` with a global namespace that already contains the import - as we have in our case. Our `global` namespace already has the import:


```
timeit(stmt='math.sqrt(2)', globals=globals())
```




    0.16592102572019485



As you can see that was a little less efficient (but what's about `0.01` seconds over `1_000_000` repetitions between friends...)

So let's go with the `setup` approach and now time the difference between using the two import styles:


```
result_1 = timeit(stmt='math.sqrt(2)', setup='import math')
result_2 = timeit(stmt='sqrt(2)', setup='from math import sqrt')
print(f'Result 1 = {result_1}')
print(f'Result 2 = {result_2}')
```

    Result 1 = 0.1496401825296516
    Result 2 = 0.10674273423342129
    

As you can see the `from math import sqrt` was slightly more efficient. But again, what's a about `0.4` seconds over `1_000_000` iterations. 

If that's what you're optimizing before you even profile your application you're doing things wrong!

Explicit is better than implicit.

So when someone sees `math.sqrt` they know `sqrt` comes from the `math` module. If they see `sqrt` they have to look at your imports to double check which module `sqrt` came from.

If the module name is long and you don't want to always type it, you can always alias it. Or use the `from` style of import. Whatever reads best since optimization is not really a concern at that point.

One last thing, what if the statement(s) you want to time require something from the scope in which it is running? How do you "pass" that variable to the `timeit` statement?

That's where the `globals` argument comes in - we already saw it in action for the imports, but the `globals()` and `locals()` functions can reference the global and local name spaces.


```
globals()
```




    {'In': ['',
      'import math\nmath.sqrt(2)',
      'from math import sqrt\nsqrt(2)',
      'get_ipython().magic("timeit (stmt=\'math.sqrt(2)\')")',
      'help(timeit)',
      'from timeit import timeit',
      'help(timeit)',
      "timeit(stmt='math.sqrt(2)')",
      "timeit(stmt='math.sqrt(2)', globals=globals())",
      "timeit(stmt = 'import math' 'math.sqrt(2)')",
      "timeit(stmt = 'import math\\nmath.sqrt(2)')",
      "timeit(stmt = 'math.sqrt(2)', setup='import math')",
      "timeit(stmt='math.sqrt(2)', globals=globals())",
      "timeit(stmt = 'math.sqrt(2)', setup='import math', number=2_000_000)",
      "timeit(stmt = 'math.sqrt(2)', setup='import math')",
      "timeit(stmt = 'import math\\nmath.sqrt(2)')",
      "timeit(stmt = 'math.sqrt(2)', setup='import math')",
      "timeit(stmt='math.sqrt(2)', globals=globals())",
      "result_1 = timeit(stmt='math.sqrt(2)', setup='import math')\nresult_2 = timeit(stmt='sqrt(2)', setup='from math import sqrt')\nprint(f'Result 1 = {result_1}')\nprint(f'Result 2 = {result_2}')",
      'globals()'],
     'Out': {1: 1.4142135623730951,
      2: 1.4142135623730951,
      8: 0.1674586308108843,
      10: 0.3324981612941258,
      11: 0.15236431163322095,
      12: 0.1631630346299744,
      13: 0.3154899626299539,
      14: 0.15821755920092073,
      15: 0.31814690955189917,
      16: 0.15629067671147823,
      17: 0.16592102572019485},
     '_': 0.16592102572019485,
     '_1': 1.4142135623730951,
     '_10': 0.3324981612941258,
     '_11': 0.15236431163322095,
     '_12': 0.1631630346299744,
     '_13': 0.3154899626299539,
     '_14': 0.15821755920092073,
     '_15': 0.31814690955189917,
     '_16': 0.15629067671147823,
     '_17': 0.16592102572019485,
     '_2': 1.4142135623730951,
     '_8': 0.1674586308108843,
     '__': 0.15629067671147823,
     '___': 0.31814690955189917,
     '__builtin__': <module 'builtins' (built-in)>,
     '__builtins__': <module 'builtins' (built-in)>,
     '__doc__': 'Automatically created module for IPython interactive environment',
     '__loader__': None,
     '__name__': '__main__',
     '__package__': None,
     '__spec__': None,
     '_dh': ['d:\\fbapt\\Dropbox\\Python Deep Dive\\Section 09 - Extras\\10 - Timing things using timeit'],
     '_i': "result_1 = timeit(stmt='math.sqrt(2)', setup='import math')\nresult_2 = timeit(stmt='sqrt(2)', setup='from math import sqrt')\nprint(f'Result 1 = {result_1}')\nprint(f'Result 2 = {result_2}')",
     '_i1': 'import math\nmath.sqrt(2)',
     '_i10': "timeit(stmt = 'import math\\nmath.sqrt(2)')",
     '_i11': "timeit(stmt = 'math.sqrt(2)', setup='import math')",
     '_i12': "timeit(stmt='math.sqrt(2)', globals=globals())",
     '_i13': "timeit(stmt = 'math.sqrt(2)', setup='import math', number=2_000_000)",
     '_i14': "timeit(stmt = 'math.sqrt(2)', setup='import math')",
     '_i15': "timeit(stmt = 'import math\\nmath.sqrt(2)')",
     '_i16': "timeit(stmt = 'math.sqrt(2)', setup='import math')",
     '_i17': "timeit(stmt='math.sqrt(2)', globals=globals())",
     '_i18': "result_1 = timeit(stmt='math.sqrt(2)', setup='import math')\nresult_2 = timeit(stmt='sqrt(2)', setup='from math import sqrt')\nprint(f'Result 1 = {result_1}')\nprint(f'Result 2 = {result_2}')",
     '_i19': 'globals()',
     '_i2': 'from math import sqrt\nsqrt(2)',
     '_i3': "timeit(stmt='math.sqrt(2)')",
     '_i4': 'help(timeit)',
     '_i5': 'from timeit import timeit',
     '_i6': 'help(timeit)',
     '_i7': "timeit(stmt='math.sqrt(2)')",
     '_i8': "timeit(stmt='math.sqrt(2)', globals=globals())",
     '_i9': "timeit(stmt = 'import math' 'math.sqrt(2)')",
     '_ih': ['',
      'import math\nmath.sqrt(2)',
      'from math import sqrt\nsqrt(2)',
      'get_ipython().magic("timeit (stmt=\'math.sqrt(2)\')")',
      'help(timeit)',
      'from timeit import timeit',
      'help(timeit)',
      "timeit(stmt='math.sqrt(2)')",
      "timeit(stmt='math.sqrt(2)', globals=globals())",
      "timeit(stmt = 'import math' 'math.sqrt(2)')",
      "timeit(stmt = 'import math\\nmath.sqrt(2)')",
      "timeit(stmt = 'math.sqrt(2)', setup='import math')",
      "timeit(stmt='math.sqrt(2)', globals=globals())",
      "timeit(stmt = 'math.sqrt(2)', setup='import math', number=2_000_000)",
      "timeit(stmt = 'math.sqrt(2)', setup='import math')",
      "timeit(stmt = 'import math\\nmath.sqrt(2)')",
      "timeit(stmt = 'math.sqrt(2)', setup='import math')",
      "timeit(stmt='math.sqrt(2)', globals=globals())",
      "result_1 = timeit(stmt='math.sqrt(2)', setup='import math')\nresult_2 = timeit(stmt='sqrt(2)', setup='from math import sqrt')\nprint(f'Result 1 = {result_1}')\nprint(f'Result 2 = {result_2}')",
      'globals()'],
     '_ii': "timeit(stmt='math.sqrt(2)', globals=globals())",
     '_iii': "timeit(stmt = 'math.sqrt(2)', setup='import math')",
     '_oh': {1: 1.4142135623730951,
      2: 1.4142135623730951,
      8: 0.1674586308108843,
      10: 0.3324981612941258,
      11: 0.15236431163322095,
      12: 0.1631630346299744,
      13: 0.3154899626299539,
      14: 0.15821755920092073,
      15: 0.31814690955189917,
      16: 0.15629067671147823,
      17: 0.16592102572019485},
     'exit': <IPython.core.autocall.ZMQExitAutocall at 0x1e343645518>,
     'get_ipython': <bound method InteractiveShell.get_ipython of <ipykernel.zmqshell.ZMQInteractiveShell object at 0x000001E3434E31D0>>,
     'math': <module 'math' (built-in)>,
     'quit': <IPython.core.autocall.ZMQExitAutocall at 0x1e343645518>,
     'result_1': 0.1496401825296516,
     'result_2': 0.10674273423342129,
     'sqrt': <function math.sqrt>,
     'timeit': <function timeit.timeit>}




```
locals()
```




    {'In': ['',
      'import math\nmath.sqrt(2)',
      'from math import sqrt\nsqrt(2)',
      'get_ipython().magic("timeit (stmt=\'math.sqrt(2)\')")',
      'help(timeit)',
      'from timeit import timeit',
      'help(timeit)',
      "timeit(stmt='math.sqrt(2)')",
      "timeit(stmt='math.sqrt(2)', globals=globals())",
      "timeit(stmt = 'import math' 'math.sqrt(2)')",
      "timeit(stmt = 'import math\\nmath.sqrt(2)')",
      "timeit(stmt = 'math.sqrt(2)', setup='import math')",
      "timeit(stmt='math.sqrt(2)', globals=globals())",
      "timeit(stmt = 'math.sqrt(2)', setup='import math', number=2_000_000)",
      "timeit(stmt = 'math.sqrt(2)', setup='import math')",
      "timeit(stmt = 'import math\\nmath.sqrt(2)')",
      "timeit(stmt = 'math.sqrt(2)', setup='import math')",
      "timeit(stmt='math.sqrt(2)', globals=globals())",
      "result_1 = timeit(stmt='math.sqrt(2)', setup='import math')\nresult_2 = timeit(stmt='sqrt(2)', setup='from math import sqrt')\nprint(f'Result 1 = {result_1}')\nprint(f'Result 2 = {result_2}')",
      'globals()',
      'locals()'],
     'Out': {1: 1.4142135623730951,
      2: 1.4142135623730951,
      8: 0.1674586308108843,
      10: 0.3324981612941258,
      11: 0.15236431163322095,
      12: 0.1631630346299744,
      13: 0.3154899626299539,
      14: 0.15821755920092073,
      15: 0.31814690955189917,
      16: 0.15629067671147823,
      17: 0.16592102572019485,
      19: {...}},
     '_': {...},
     '_1': 1.4142135623730951,
     '_10': 0.3324981612941258,
     '_11': 0.15236431163322095,
     '_12': 0.1631630346299744,
     '_13': 0.3154899626299539,
     '_14': 0.15821755920092073,
     '_15': 0.31814690955189917,
     '_16': 0.15629067671147823,
     '_17': 0.16592102572019485,
     '_19': {...},
     '_2': 1.4142135623730951,
     '_8': 0.1674586308108843,
     '__': 0.16592102572019485,
     '___': 0.15629067671147823,
     '__builtin__': <module 'builtins' (built-in)>,
     '__builtins__': <module 'builtins' (built-in)>,
     '__doc__': 'Automatically created module for IPython interactive environment',
     '__loader__': None,
     '__name__': '__main__',
     '__package__': None,
     '__spec__': None,
     '_dh': ['d:\\fbapt\\Dropbox\\Python Deep Dive\\Section 09 - Extras\\10 - Timing things using timeit'],
     '_i': 'globals()',
     '_i1': 'import math\nmath.sqrt(2)',
     '_i10': "timeit(stmt = 'import math\\nmath.sqrt(2)')",
     '_i11': "timeit(stmt = 'math.sqrt(2)', setup='import math')",
     '_i12': "timeit(stmt='math.sqrt(2)', globals=globals())",
     '_i13': "timeit(stmt = 'math.sqrt(2)', setup='import math', number=2_000_000)",
     '_i14': "timeit(stmt = 'math.sqrt(2)', setup='import math')",
     '_i15': "timeit(stmt = 'import math\\nmath.sqrt(2)')",
     '_i16': "timeit(stmt = 'math.sqrt(2)', setup='import math')",
     '_i17': "timeit(stmt='math.sqrt(2)', globals=globals())",
     '_i18': "result_1 = timeit(stmt='math.sqrt(2)', setup='import math')\nresult_2 = timeit(stmt='sqrt(2)', setup='from math import sqrt')\nprint(f'Result 1 = {result_1}')\nprint(f'Result 2 = {result_2}')",
     '_i19': 'globals()',
     '_i2': 'from math import sqrt\nsqrt(2)',
     '_i20': 'locals()',
     '_i3': "timeit(stmt='math.sqrt(2)')",
     '_i4': 'help(timeit)',
     '_i5': 'from timeit import timeit',
     '_i6': 'help(timeit)',
     '_i7': "timeit(stmt='math.sqrt(2)')",
     '_i8': "timeit(stmt='math.sqrt(2)', globals=globals())",
     '_i9': "timeit(stmt = 'import math' 'math.sqrt(2)')",
     '_ih': ['',
      'import math\nmath.sqrt(2)',
      'from math import sqrt\nsqrt(2)',
      'get_ipython().magic("timeit (stmt=\'math.sqrt(2)\')")',
      'help(timeit)',
      'from timeit import timeit',
      'help(timeit)',
      "timeit(stmt='math.sqrt(2)')",
      "timeit(stmt='math.sqrt(2)', globals=globals())",
      "timeit(stmt = 'import math' 'math.sqrt(2)')",
      "timeit(stmt = 'import math\\nmath.sqrt(2)')",
      "timeit(stmt = 'math.sqrt(2)', setup='import math')",
      "timeit(stmt='math.sqrt(2)', globals=globals())",
      "timeit(stmt = 'math.sqrt(2)', setup='import math', number=2_000_000)",
      "timeit(stmt = 'math.sqrt(2)', setup='import math')",
      "timeit(stmt = 'import math\\nmath.sqrt(2)')",
      "timeit(stmt = 'math.sqrt(2)', setup='import math')",
      "timeit(stmt='math.sqrt(2)', globals=globals())",
      "result_1 = timeit(stmt='math.sqrt(2)', setup='import math')\nresult_2 = timeit(stmt='sqrt(2)', setup='from math import sqrt')\nprint(f'Result 1 = {result_1}')\nprint(f'Result 2 = {result_2}')",
      'globals()',
      'locals()'],
     '_ii': "result_1 = timeit(stmt='math.sqrt(2)', setup='import math')\nresult_2 = timeit(stmt='sqrt(2)', setup='from math import sqrt')\nprint(f'Result 1 = {result_1}')\nprint(f'Result 2 = {result_2}')",
     '_iii': "timeit(stmt='math.sqrt(2)', globals=globals())",
     '_oh': {1: 1.4142135623730951,
      2: 1.4142135623730951,
      8: 0.1674586308108843,
      10: 0.3324981612941258,
      11: 0.15236431163322095,
      12: 0.1631630346299744,
      13: 0.3154899626299539,
      14: 0.15821755920092073,
      15: 0.31814690955189917,
      16: 0.15629067671147823,
      17: 0.16592102572019485,
      19: {...}},
     'exit': <IPython.core.autocall.ZMQExitAutocall at 0x1e343645518>,
     'get_ipython': <bound method InteractiveShell.get_ipython of <ipykernel.zmqshell.ZMQInteractiveShell object at 0x000001E3434E31D0>>,
     'math': <module 'math' (built-in)>,
     'quit': <IPython.core.autocall.ZMQExitAutocall at 0x1e343645518>,
     'result_1': 0.1496401825296516,
     'result_2': 0.10674273423342129,
     'sqrt': <function math.sqrt>,
     'timeit': <function timeit.timeit>}



Let's use globals first:


```
import random
```


```
l = random.choices(list('python'), k=500)
```

The variable `l` is now in our global name space.


```
'l' in globals()
```




    True



And technically in our local name space too:


```
'l' in locals()
```




    True




```
timeit(stmt='random.choice(l)', setup='import random', globals=globals())
```




    1.1323987425012092



As you can see the statement was able to access `l` from the `globals()` that as passed to the `global` argument.

Sometimes though you may have to use the local namespace, for exampele inside a function:


```
def random_choices():
    randoms = random.choices(list('python'), k=500)
    
    return timeit(stmt='random.choice(randoms)', 
                  setup='import random', 
                  globals=locals())
```


```
random_choices()
```




    1.0808561935605212



I hope you saw that running the code using a local `randoms` ran slightly faster than using it from the global scope!

We'll come back to that in a later video, but in fact running code from the global namespace (i.e. at the module level) is slightly slower in general than running it in a local namespace (i.e. inside a function).

If we had passed it `globals()` instead it would not have worked since `randoms` is not in the global namespace:


```
'randoms' in globals()
```




    False




```
def random_choices():
    randoms = random.choices(list('python'), k=500)
    
    return timeit(stmt='random.choice(randoms)', 
                  setup='import random', 
                  globals=globals())
```


```
random_choices()
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-34-9e88504addca> in <module>()
    ----> 1 random_choices()
    

    <ipython-input-33-2aaae2461319> in random_choices()
          4     return timeit(stmt='random.choice(randoms)', 
          5                   setup='import random',
    ----> 6                   globals=globals())
    

    D:\Users\fbapt\Anaconda3\envs\deepdive\lib\timeit.py in timeit(stmt, setup, timer, number, globals)
        231            number=default_number, globals=None):
        232     """Convenience function to create Timer object and call timeit method."""
    --> 233     return Timer(stmt, setup, timer, globals).timeit(number)
        234 
        235 def repeat(stmt="pass", setup="pass", timer=default_timer,
    

    D:\Users\fbapt\Anaconda3\envs\deepdive\lib\timeit.py in timeit(self, number)
        176         gc.disable()
        177         try:
    --> 178             timing = self.inner(it, self.timer)
        179         finally:
        180             if gcold:
    

    <timeit-src> in inner(_it, _timer)
    

    NameError: name 'randoms' is not defined


One more thing to point out is that functions defined at the module level are actually in our global namespace as well:


```
def pick_random(lst):
    return random.choice(lst)
```


```
'pick_random' in globals()
```




    True



This means that technically we can write the function we want to time in our global/local scope, and pass the scope in and then reference the function from that scope in our statement. It will be slower though since it has to find the function in the scope first - but you could do it to test relative performance differences:


```
timeit(stmt='pick_random(l)', globals=globals())
```




    1.216267840187811



And there you go, `timeit` was able to access both `pick_random` and the variable `l`.

##  Don't Use *args and **kwargs Names Blindly

In most of the code we have been working with we used `*args` and `**kwargs`. But these were small code snippets where the argument names did not necessarily have meaning, or were used very generically such as with decorators.

In your code, if those variable positional and keyword-only arguments have meaning, then use a meaningful name instead of just `*args` and `**kwargs`.

#### Example 1

Here, using the conventional names `args` and `kwargs` makes sense since we have no idea what those are - we are simply using them as a pass through to call another function in our decorator:


```
def audit(f):
    def inner(*args, **kwargs):
        print(f'Called {f.__name__}')
        return f(*args, **kwargs)
    return inner
```

But for the following `product` function, it makes more sense to use `*values` than `*args`.


```
@audit
def say_hello(name):
    return f'Hello {name}'

from operator import mul
from functools import reduce

@audit
def product(*values):
    return reduce(mul, values)
```


```
say_hello('Polly')
```

    Called say_hello
    




    'Hello Polly'




```
product(1, 2, 3, 4)
```

    Called product
    




    24



#### Example 2

Same thing here - using `*item_values` makes more sense than `*args`:


```
def count_multi(lst, *item_values):
    return sum(lst.count(value) for value in item_values)
```


```
l = 1, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10
```


```
count_multi(l, 1, 6, 7)
```




    5



#### Example 3

Suppose we want our class init to allow people to send in additional arbitrary (custom) instance attributes:


```
class Person:
    def __init__(self, name, age, **custom_attributes):
        self.name = name
        self.age = age
        for attr_name, attr_value in custom_attributes.items():
            setattr(self, attr_name, attr_value)        
```


```
parrot = Person('Polly', 101, status='stiff', vooms=False)
```


```
print(vars(parrot))
```

    {'name': 'Polly', 'age': 101, 'status': 'stiff', 'vooms': False}
    


```
michael = Person('Michael', 42, role='shopkeeper', crooked=True)
```


```
print(vars(michael))
```

    {'name': 'Michael', 'age': 42, 'role': 'shopkeeper', 'crooked': True}
    

##  Sentinel Values for Parameter Defaults

Often we specify the default for a function parameter as `None`. This allows to determine if the user specified an argument for that parameter or not. 

There's a potential issue here!

What happens if we need to differentiate between the following:
* a non-`None` value was provided for the argument
* a `None` value *was* provided for the argument
* the argument was not provided at all

Obviously, if we write our function this way, it will not work as intended:


```
def validate(a=None):
    if a is not None:
       print('Argument was provided')
    else:
        print('Argument was not provided')
```


```
validate(100)
```

    Argument was provided
    


```
validate()
```

    Argument was not provided
    


```
validate(None)
```

    Argument was not provided
    

Instead, we need to use a different **sentinel** value. But which one?

How can we **guarantee** that whatever sentinel we use will not be explicitly passed in by the user?

For example we could try to use something like an unlikely string or integer. But that does not guarantee that the caller won't use that precise sentinel value at some point.

The easiest thing to do is to create an instance of the `object` class. This is guaranteed to result in an object that the user cannot pass to us (they have no way of getting their hands on that object - or at least not without the absolute intention to do so). (remember that Python will always allow us to shoot ourselves in the foot if we try hard enough :-) )


```
_sentinel = object()

def validate(a=_sentinel):
    if a is not _sentinel:
        print('Argument was provided')
    else:
        print('Argument was not provided')
```


```
validate(100)
```

    Argument was provided
    


```
validate(None)
```

    Argument was provided
    


```
validate()
```

    Argument was not provided
    


```
validate(object())
```

    Argument was provided
    

Now, instead of using a separate variable to hold the sentinel value (`_sentinel`), we can introspect the function to find out what the default sentinel value is:


```
def validate(a=object()):
    default_a = validate.__defaults__[0]
    if a is not default_a:
        print('Argument was provided')
    else:
        print('Argument was not provided')
    
    
```


```
validate(100)
```

    Argument was provided
    


```
validate(None)
```

    Argument was provided
    


```
validate()
```

    Argument was not provided
    


```
validate(object())
```

    Argument was provided
    

We can expand this to several parameters as well if we need to, using either method:


```
def validate(a=object(), b=object(), *, kw=object()):
    default_a = validate.__defaults__[0]
    default_b = validate.__defaults__[1]
    default_kw = validate.__kwdefaults__['kw']
    
    if a is not default_a:
        print('Argument a was provided')
    else:
        print('Argument a was not provided')
        
    if b is not default_b:
        print('Argument b was provided')
    else:
        print('Argument b was not provided')
        
    if kw is not default_kw:
        print('Argument kw was provided')
    else:
        print('Argument kw was not provided')
```


```
validate(100, 200, kw=None)
```

    Argument a was provided
    Argument b was provided
    Argument kw was provided
    


```
validate(100, 200)
```

    Argument a was provided
    Argument b was provided
    Argument kw was not provided
    


```
validate(b=100)
```

    Argument a was not provided
    Argument b was provided
    Argument kw was not provided
    


```
validate()
```

    Argument a was not provided
    Argument b was not provided
    Argument kw was not provided
    

##  Simulating a simple Switch in Python

This is based on a few questions I've received regarding a `switch` statement in Python.

Python does not have a switch statement, but it is possible to have similar functionality in a variety of ways.

Here I'm going to assume a simple `switch` statement where each `case` has a `break` (in other words, no fall through), and is based on a single value.

You can see a PEP that discussed adding a `switch` statement to Python, proposed by Guido, but ultimately rejected (by Guido as well):
https://www.python.org/dev/peps/pep-3103/

A simple Java example would be something like this:

```
switch (dow) {
    case 1: dowString = 'Monday';
            break;
    case 2: dowString = 'Tuesday';
            break;
    case 3: dowString = 'Wednesday';
            break;
    case 4: dowString = 'Thursday';
            break;
    case 5: dowString = 'Friday';
            break;
    case 6: dowString = 'Saturday';
            break;
    case 7: dowString = 'Sunday';
            break;
    default: dowString = 'Invalid day of week';
}
```

The simplest approach here is to simply use an `if...elif...else` structure.

To make it slightly more interesting, I'm not going to set a variable for each case statement, I'm going to return a function - to keep it simple I'll just call the `print()` function, but it could be anything really.


```
def dow_switch_fn(dow):
    if dow == 1:
        fn = lambda: print('Monday')
    elif dow == 2:
        fn = lambda: print('Tuesday')
    elif dow == 3:
        fn = lambda: print('Wednesday')
    elif dow == 4:
        fn = lambda: print('Thursday')
    elif dow == 5:
        fn = lambda: print('Friday')
    elif dow == 6:
        fn = lambda: print('Saturday')
    elif dow == 7:
        fn = lambda: print('Sunday')
    else:
        fn = lambda: print('Invalid day of week')
    
    return fn()
```


```
dow_switch_fn(1)
```

    Monday
    


```
dow_switch_fn(100)
```

    Invalid day of week
    

Now, dictionaries could also be used quite effectively here:


```
def dow_switch_dict(dow):
    dow_dict = {
        1: lambda: print('Monday'),
        2: lambda: print('Tuesday'),
        3: lambda: print('Wednesday'),
        4: lambda: print('Thursday'),
        5: lambda: print('Friday'),
        6: lambda: print('Saturday'),
        7: lambda: print('Sunday'),
        'default': lambda: print('Invalid day of week')
    }
    
    return dow_dict.get(dow, dow_dict['default'])()
```


```
dow_switch_dict(1)
```

    Monday
    


```
dow_switch_dict(100)
```

    Invalid day of week
    

One advantage of using a dictionary (as an associative array), is that you can add and remove elements from the dictionary at run time. Of course you cannot do that with the `if...elif...else` - you need to know at compile time how many branches your "switch" has (just like a regular `switch` would, that is also fixed once the code has been compiled+
).

But the downside of this approach compared to `if...elif...else` is that the dictionary values are relatively simple and cannot contain nested if statements or anything else. In the case of `if...elif...else` your code blocks for each of these statement can contain as many lines of code as you want.

So the choice is yours, and depends on what you are trying to accomplish.

Now, there is also another way to do this, and it is based on the concepts I discuss in the decorator videos on the single dispatch generic functions.

We cannot use the standard library's `@singledispatch` decorator, but we can adapt the approach I showed you to create a `switch` function where we can register each `case` of the `switch`.

First, let's recall our own implementation of the `@singledispatch` decorator:


```
def singledispatch(fn):
    registry = dict()
    registry[object] = fn
    
    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn  # we do this so we can stack register decorators!
        return inner
   
    def decorator(arg):
        fn = registry.get(type(arg), registry[object])
        return fn(arg)

    decorator.register = register
    return decorator
```

With this decorator, we are dispatching based on the type. But if you think of our `switch` statement, we really just want to dispatch based on a value (like the `dow` value).

So let's tweak the decorator to no longer use a type, but an arbitrary value instead:


```
def switcher(fn):
    registry = dict()
    registry['default'] = fn
    
    def register(case):
        def inner(fn):
            registry[case] = fn
            return fn  # we do this so we can stack register decorators!
        return inner
   
    def decorator(case):
        fn = registry.get(case, registry['default'])
        return fn()

    decorator.register = register
    return decorator
```

And that's all we need to change!

We can now use it as follows:


```
@switcher
def dow():
    print('Invalid day of week')
    
@dow.register(1)
def dow_1():
    print('Monday')
    
dow.register(2)(lambda: print('Tuesday'))
dow.register(3)(lambda: print('Wednesday'))
dow.register(4)(lambda: print('Thursday'))
dow.register(5)(lambda: print('Friday'))
dow.register(6)(lambda: print('Saturday'))
dow.register(7)(lambda: print('Sunday'))
```




    <function __main__.<lambda>>



And we can now use it this way:


```
dow(1)
```

    Monday
    


```
dow(2)
```

    Tuesday
    


```
dow(100)
```

    Invalid day of week
    

Of course you'll notice that our decorator is simply using the same dictionary / associative array approach we just looked at - except we can use decorators to do that work.
