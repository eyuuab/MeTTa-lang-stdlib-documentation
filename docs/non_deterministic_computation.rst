Non-deterministic Computation
=============================

``collapse-bind``
---------------

**Description:** Evaluates a MeTTa operation and returns an expression containing all alternative evaluations in the form ``(Atom Bindings)``.

**Parameters:**
    - Atom: The MeTTa operation to be evaluated.

**Return:** An expression of alternative evaluations with bindings.

**Example:**

.. code-block:: metta

    (= (bin) 0)
    (= (bin) 1)
    !(collapse-bind (bin)) ; Returns (0 { }), (1 { }) nondeterministically

``superpose-bind``
----------------

**Description:** Takes the result of ``collapse-bind`` and returns only the result atoms, discarding the bindings.

**Parameters:**
    - Expression: An expression in the form ``(Atom Bindings)``.

**Return:** A non-deterministic list of atoms.

**Example:**

.. code-block:: metta

    !(superpose-bind ((A (Grounded ...)) (B (Grounded ...)))) ; returns the equivalent of (superpose (A B))

``superpose``
-----------

**Description:** Turns a tuple into a nondeterministic result.

**Parameters:**
    - Tuple: Tuple to be converted.

**Return:** Argument converted to nondeterministic result

**Example:**

.. code-block:: metta

    !(superpose (A B C)) ; returns A, B, C nondeterministically

``collapse``
----------

**Description:** Converts a nondeterministic result into a tuple.

**Parameters:**
    - Atom: Atom which will be evaluated.

**Return:** Tuple

**Example:**

.. code-block:: metta

    !(collapse (superpose (A B C))) ; returns (A B C)