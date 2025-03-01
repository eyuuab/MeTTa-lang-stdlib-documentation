Evaluation Control
==================

``return``
----------

**Description:** Returns a value from a ``function`` expression.

**Parameters:**
    - Value: The value to be returned.

**Return:** The input value.

**Example:**

.. code-block:: metta

    (function (return 5)) ; Returns 5

``function``
------------

**Description:** Evaluates the argument until it becomes ``(return <result>)``, then reduces to ``<result>``.

**Parameters:**
    - Atom: The atom to be evaluated.

**Return:** The result of the atom's evaluation.

**Example:**

.. code-block:: metta

    !(function (return (+ 1 2))) ; Returns 3 because (+ 1 2) evaluates to 3 which becomes (return 3)

``eval``
--------

**Description:** Evaluates an atom, performing one step of reduction. This can be via equality rules or grounded functions.

**Parameters:**
    - Atom: The atom to be evaluated.

**Return:** The result of the evaluation.

**Example:**

.. code-block:: metta

    (= (double $x) (+ $x $x))
    !(eval (double 5)) ; Returns (+ 5 5)
    !(eval (+ 5 5)) ; Returns 10

``evalc``
---------

**Description:** Evaluates an atom within a specific atomspace context.

**Parameters:**
    - Atom: The atom to evaluate.
    - Space: The atomspace in which to evaluate the atom.

**Return:** The result of the evaluation.

**Example:**

.. code-block:: metta

    (= (double $x) (+ $x $x))
    !(evalc (double 5) &self) ; Returns (+ 5 5) self being the working space
    !(evalc (+ 5 5) &self) ; Returns 10

``chain``
---------

**Description:** Evaluates an atom, binds the result to a variable, and then evaluates another atom containing the variable.

**Parameters:**
    - Atom: The atom to be evaluated initially.
    - Variable: The variable to bind the result to.
    - Template: The atom to evaluate after binding.

**Return:** The result of evaluating the template.

**Example:**

.. code-block:: metta

    !(chain (+ 2 3) $x (* $x 2)) ; Evaluates (+ 2 3) to 5, binds it to $x, then evaluates (* $x 2), returning 10.
