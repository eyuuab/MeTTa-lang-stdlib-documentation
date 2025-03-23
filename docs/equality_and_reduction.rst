Equality and Reduction
======================

``=`` (Equality/Reduction Rule Definition)
------------------------------------------

**Description:** Defines a reduction rule for expressions. The left-hand side is a pattern, and the right-hand side is the result of the reduction.

**Parameters:**
    - Pattern: The expression to be matched.
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

``=alpha``
-----------------

**Description:** Checks the alpha equivalency of the two given atoms.

**Parameters:**
    - ExpressionAtom: First expression.
    - ExpressionAtom: Second expression.

**Return:** True if the expressions are alpha-equivalence False otherwise wise.

**Example:**

.. code-block:: metta

    !(=alpha (Father $Jhon) (Father $Bob)) ; Returns True because they differ only by variable.
    !(=alpha (Father $Jhon) (Son $Jhon)) ; Returns False because they differ structurally.

``assertEqual``
-----------------

**Description:** Compares (sets of) results of evaluation of two expressions.

**Parameters:**
    - ExpressionAtom: First expression.
    - ExpressionAtom: Second expression.

**Return:** Unit atom if both expressions after evaluation are equal, error - otherwise.

**Example:**

.. code-block:: metta

    !(assertEqual (+ 1 2) (- 6 3)) ; Returns ().
    !(assertEqual (+ 1 2) (+ 2 2)) 
    ;(Error (assertEqual (+ 1 2) (+ 2 2))
    ;Expected: [4]
    ;Got: [3]
    ;Missed results: 4
    ;Excessive results: 3)

``assertAlphaEqual``
-----------------

**Description:** Asserts the alpha-equivalency of the two given expressions.

**Parameters:**
    - ExpressionAtom: First expression.
    - ExpressionAtom: Second expression.

**Return:** Unit atom if both expressions after evaluation are alpha equal, error - otherwise.

**Example:**

.. code-block:: metta

    !(assertAlphaEqual (+ $x $y) (+ $a $b)) ; Returns ().
    !(assertAlphaEqual (+ $x $y) (- $x $y)) 
    ; Returns:
    ;(Error (assertAlphaEqual (+ $x $y) (- $x $y))
    ;Expected: [(- $x $y)]
    ;Got: [(+ $x $y)]
    ;Missed results: (- $x $y)
    ;Excessive results: (+ $x $y))

``assertEqualToResult``
-----------------

**Description:** Same as assertEqual but it doesn't reduce the second argument. Second argument is considered to be a set of values of the first argument's evaluation.

**Parameters:**
    - ExpressionAtom: First expression.
    - ExpressionAtom: Second expression.

**Return:** Unit atom if both expressions after evaluation of the first argument are equal, error - otherwise.

**Example:**

.. code-block:: metta

    !(assertEqualToResult (+ 1 2) 3) ; Returns ().
    !(assertEqualToResult (+ 1 2) (+ 1 2)) 
    ;Returns:
    ;(Error (assertEqualToResult (+ 1 2) (+ 1 2))
    ;Expected: [+, 1, 2]
    ;Got: [3]
    ;Missed results: +, 1, 2
    ;Excessive results: 3)

``assertAlphaEqualToResult``
-----------------

**Description:** Same as assertEqualToResult but for assertAlphaEqual. Checks the alpha-equivalency without reducing the second parameter.

**Parameters:**
    - ExpressionAtom: First expression.
    - ExpressionAtom: Second expression.

**Return:** Unit atom if both expressions after evaluation of the first argument are equal, error - otherwise.

**Example:**

.. code-block:: metta

    (= (add) $x)
    !(assertAlphaEqualToResult (add) ($y)) ; Returns ().
    !(assertAlphaEqualToResult (add) (add)) 
    ;Returns:
    ;(Error (assertAlphaEqualToResult (add) (add))
    ;Expected: [add]
    ;Got: [$X#66]
    ;Missed results: add
    ;Excessive results: $X#66) 
