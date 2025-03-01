Expression Manipulation
=======================

``cons-atom``
-------------

**Description:** Constructs an expression (list) by adding an atom to the head of another expression.

**Parameters:**
    - Head: The atom to be added to the beginning.
    - Tail: The expression to add the atom on.

**Return:** A new expression.

**Example:**

.. code-block:: metta

    !(cons-atom 1 (2 3)) ; Returns (1 2 3)

``decons-atom``
---------------

**Description:** Deconstructs an expression into its head and tail.

**Parameters:**
    - Expression: The expression to be deconstructed.

**Return:** An expression containing the head and tail: ``(Head Tail)``.

**Example:**

.. code-block:: metta

    !(decons-atom (1 2 3)) ; Returns ((1) (2 3))

``car-atom``
----------

**Description:** Extracts the first atom of an expression.

**Parameters:**
    - Expression: The expression to extract the first atom from.

**Return:** The first atom of the expression.

**Example:**

.. code-block:: metta

    !(car-atom (1 2 3)) ; Returns 1

``cdr-atom``
----------

**Description:** Extracts the tail of an expression (all atoms except the first).

**Parameters:**
    - Expression: The expression to extract the tail from.

**Return:** The tail of the expression.

**Example:**

.. code-block:: metta

    !(cdr-atom (1 2 3)) ; Returns (2 3)

``size-atom``
-----------

**Description:** Returns size of an expression.

**Parameters:**
    - Expression: The expression whose size is to be determined..

**Return:** Size of an expression.

**Example:**

.. code-block:: metta

    !(size-atom (1 2 3)) ; Returns 3

``index-atom``
------------

**Description:** Returns atom from an expression using index or error if index is out of bounds

**Parameters:**
    - Expression: The expression to extract from.
    - Index: The index of the target atom.

**Return:** Atom from an expression in the position defined by index. Error if index is out of bounds

**Example:**

.. code-block:: metta

    !(index-atom (1 2 3) 1) ; Returns 2