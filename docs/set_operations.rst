Set Operations
==============

``unique``
--------

**Description:** Returns unique entities from non-deterministic input.

**Parameters:**
    - Arg: Non-deterministic set of values

**Return:** Unique values from input set

**Example:**

.. code-block:: metta

    !(unique (superpose (a b c d d))) ; Returns [a, b, c, d]

``union``
-------

**Description:** Returns union of two non-deterministic inputs.

**Parameters:**
    - Arg1: Non-deterministic set of values
    - Arg2: Another non-deterministic set of values

**Return:** Union of sets

**Example:**

.. code-block:: metta

    !(union (superpose (a b b c)) (superpose (b c c d))) ; Returns [a, b, b, c, b, c, c, d]

``intersection``
--------------

**Description:** Returns intersection of two non-deterministic inputs.

**Parameters:**
    - Arg1: Non-deterministic set of values
    - Arg2: Another non-deterministic set of values

**Return:** Intersection of sets

**Example:**

.. code-block:: metta

    !(intersection (superpose (a b c c)) (superpose (b c c c d))) ; Returns [b, c, c]

``subtraction``
-------------

**Description:** Returns subtraction of two non-deterministic inputs.

**Parameters:**
    - Arg1: Non-deterministic set of values
    - Arg2: Another non-deterministic set of values

**Return:** Subtraction of sets

**Example:**

.. code-block:: metta

    !(subtraction (superpose (a b b c)) (superpose (b c c d))) ; Returns [a, b]

``unique-atom``
-------------

**Description:** Function takes tuple and returns only unique entities

**Parameters:**
    - List: List of values

**Return:** Unique values from input set

**Example:**

.. code-block:: metta

    !(unique-atom (a b c d d)) ; Returns (a b c d)

``union-atom``
------------

**Description:** Function takes two tuples and returns their union

**Parameters:**
    - List1: List of values
    - List2: List of values

**Return:** Union of sets

**Example:**

.. code-block:: metta

    !(union-atom (a b b c) (b c c d)) ; Returns (a b b c b c c d)

``intersection-atom``
-------------------

**Description:** Function takes two tuples and returns their intersection

**Parameters:**
    - List1: List of values
    - List2: List of values

**Return:** Intersection of sets

**Example:**

.. code-block:: metta

    !(intersection-atom (a b c c) (b c c c d)) ; Returns (b c c)

``subtraction-atom``
------------------

**Description:** Function takes two tuples and returns their subtraction

**Parameters:**
    - List1: List of values
    - List2: List of values

**Return:** Subtraction of sets

**Example:**

.. code-block:: metta

    !(subtraction-atom (a b b c) (b c c d)) ; Returns (a b)