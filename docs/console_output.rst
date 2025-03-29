
``println!``
---------------

**Description:** Prints a line of text to the console.

**Parameters:**
    - Atom: Any atom to be printed out.

**Return:** Unit atom

**Example:**

.. code-block:: metta

    !(println! "Hello world!")
    ; Prints Hello world!
    ; Returns (). 

``trace!``
---------------

**Description:** Prints its first argument and returns second. Both arguments will be evaluated before processing

**Parameters:**
    - Atom: Atom to be printed.
    - Atom: Atom to be reduced.

**Return:** The result of the second parameter

**Example:**

.. code-block:: metta

    !(trace! "Adding one and two!" (+ 1 2))
    ; Prints: Adding one and two! 
    ; Returns 3
