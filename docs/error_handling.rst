Error Handling
==============

``ErrorType``
-------------

**Description:** Type of the atom which contains an error.

**Type:** Type

``Error``
---------

**Description:** Constructs an error atom, indicating a problem during evaluation.

**Parameters:**
    - Atom: The atom where the error occurred.
    - Message: An error message, such as ``BadType`` or ``IncorrectNumberOfArguments``.

**Return:** An error atom.

**Example:**

.. code-block:: metta

    (Error (add "a" 2) BadType)

``if-error``
------------

**Description:** Checks if an atom is an error. Returns one value if it is, and another if it is not.

**Parameters:**
    - Atom: The atom to check.
    - Then: Value to return if the atom is an error.
    - Else: Value to return otherwise.

**Return:** Either the ``Then`` or ``Else`` argument.

**Example:**

.. code-block:: metta

    !(if-error (Error 5 BadType) "Error!" "No error") ; Returns "Error!"

``return-on-error``
-------------------

**Description:** Returns the first argument if it is an Empty or an error. Returns the second argument otherwise.

**Parameters:**
    - Atom: Atom to check.
    - Then: Atom for further evaluation if the first argument is not an Error or Empty.

**Return:** Return previous result if it is an error or Empty or continue evaluation.

**Example:**

.. code-block:: metta

    !(return-on-error (Error 5 BadType) 6) ; Returns (Error 5 BadType)
    !(return-on-error 5 6) ; Returns 6
