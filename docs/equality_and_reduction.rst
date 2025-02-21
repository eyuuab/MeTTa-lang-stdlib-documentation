Equality and Reduction
======================

``=`` (Equality/Reduction Rule Definition)
------------------------------------------

**Description:** Defines a reduction rule for expressions. The left-hand side is a pattern, and the right-hand side is the result of the reduction.

**Parameters:**
    - Pattern: The expression to match.
    - Result: The expression to replace the matched pattern with.

**Return:** Not reduced itself unless custom equalities over equalities are added

**Example:**

.. code-block:: metta

    (= (add 1 2) 3)

``id`` (Identity)
-----------------

**Description:** Returns its argument unchanged.

**Parameters:**
    - Input: Any atom.

**Return:** The input atom.

**Example:**

.. code-block:: metta

    !(id 5) ; Returns 5
