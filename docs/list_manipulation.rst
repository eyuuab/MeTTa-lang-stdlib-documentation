List Manipulation
=================

``filter-atom``
-------------

**Description:** Filters a list of atoms based on a predicate.

**Parameters:**
    - List: The list of atoms to filter.
    - Variable: The variable to use in the predicate.
    - Filter: The predicate to apply (an expression that returns ``True`` or ``False``).

**Return:** A new list containing only the atoms that satisfy the predicate.

**Example:**

.. code-block:: metta

    !(filter-atom (1 2 3 4 5) $x (> $x 3)) ; Returns (4 5)

``map-atom``
----------

**Description:** Applies a function to each atom in a list, creating a new list with the results.

**Parameters:**
    - List: The list of atoms to map over.
    - Variable: The variable to use in the mapping expression.
    - Map: The expression to apply to each atom.

**Return:** A new list with the mapped values.

**Example:**

.. code-block:: metta

    !(map-atom (1 2 3) $x (+ $x 1)) ; Returns (2 3 4)

``foldl-atom``
------------

**Description:** Folds (reduces) a list of values into a single value, using a binary operation.  This is a left fold.

**Parameters:**
    - List: The list of values to fold.
    - Init: The initial value.
    - A: The variable to hold the accumulated value.
    - B: The variable to hold the current element of the list.
    - Op: The binary operation to apply (an expression using ``A`` and ``B``).

**Return:** The final accumulated value.

**Example:**

.. code-block:: metta

    !(foldl-atom (1 2 3 4) 0 $acc $x (+ $acc $x)) ; Returns 10 (1+2+3+4)