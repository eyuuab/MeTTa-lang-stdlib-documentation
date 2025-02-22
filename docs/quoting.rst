Quoting
=======

``quote``
-------

**Description:** Prevents an atom from being reduced.

**Parameters:**
    - Atom: The atom to quote.

**Return:** The quoted atom (which will not be evaluated).

**Example:**

.. code-block:: metta

    !(eval (quote (+ 1 2))) ; Returns (+ 1 2) instead of 3

``unquote``
---------

**Description:** Removes the quote from a quoted atom.

**Parameters:**
    - QuotedAtom: The atom to unquote.

**Return:** The original, unquoted atom.

**Example:**

.. code-block:: metta

    !(unquote (quote (+ 1 2))) ; Returns (+ 1 2)

``noreduce-eq``
-------------

**Description:** Checks equality of two atoms without reducing them.

**Parameters:**
    - A: First atom
    - B: Second atom

**Return:** True if not reduced atoms are equal, False - otherwise

**Example:**

.. code-block:: metta

    !(noreduce-eq (+ 1 2) (+ 1 2)) ; Returns True
    !(noreduce-eq (+ 1 2) 3) ; Returns False