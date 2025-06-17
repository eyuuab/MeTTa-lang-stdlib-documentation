Mathematical Operations
=======================

``pow-math``
----------

**Description:** Calculates the power of a base raised to an exponent.

**Parameters:**
    - Base: The base number.
    - Power: The exponent.

**Return:** The result of the power function.

**Example:**

.. code-block:: metta

    !(pow-math 2 3) ; Returns 8.0

``sqrt-math``
-----------

**Description:** Calculates the square root of a number.

**Parameters:**
    - Number: The number to calculate the square root of. Must be >= 0.

**Return:** The square root of the number.

**Example:**

.. code-block:: metta

    !(sqrt-math 9) ; Returns 3.0

``abs-math``
----------

**Description:** Calculates the absolute value of a number.

**Parameters:**
    - Number: The number to calculate the absolute value of.

**Return:** The absolute value of the number.

**Example:**

.. code-block:: metta

    !(abs-math -5) ; Returns 5

``log-math``
----------

**Description:** Calculates the logarithm of a number with a given base.

**Parameters:**
    - Base: The base of the logarithm.
    - Number: The number to calculate the logarithm of.

**Return:** The result of the logarithm function.

**Example:**

.. code-block:: metta

    !(log-math 10 100) ; Returns 2.0

``trunc-math``
------------

**Description:** Returns the integer part of the input value

**Parameters:**
    - Float: Input float value

**Return:** Integer part of float

**Example:**

.. code-block:: metta

    !(trunc-math 5.6) ; Returns 5.0

``ceil-math``
-----------

**Description:** Returns the smallest integer greater than or equal to the input value

**Parameters:**
    - Float: Input float value

**Return:** Integer value greater than or equal to the input

**Example:**

.. code-block:: metta

    !(ceil-math 5.2) ; Returns 6.0

``floor-math``
------------

**Description:** Returns the smallest integer less than or equal to the input value

**Parameters:**
    - Float: Input float value

**Return:** Integer value less than or equal to the input

**Example:**

.. code-block:: metta

    !(floor-math 5.8) ; Returns 5.0

``round-math``
------------

**Description:** Returns the nearest integer to the input float value

**Parameters:**
    - Float: Input float value

**Return:** Nearest integer to the input

**Example:**

.. code-block:: metta

    !(round-math 5.4) ; Returns 5.0
    !(round-math 5.6) ; Returns 6.0

``sin-math``
----------

**Description:** Returns result of the sine function for an input value in radians

**Parameters:**
    - Angle: Angle in radians

**Return:** Result of the sine function

**Example:**

.. code-block:: metta

    !(sin-math 0) ; Returns 0.0

``asin-math``
-----------

**Description:** Returns result of the arcsine function for an input value

**Parameters:**
    - Float: Input float value

**Return:** Result of the arcsine function

**Example:**

.. code-block:: metta

    !(asin-math 0) ; Returns 0.0

``cos-math``
----------

**Description:** Returns result of the cosine function for an input value in radians

**Parameters:**
    - Angle: Angle in radians

**Return:** Result of the cosine function

**Example:**

.. code-block:: metta

    !(cos-math 0) ; Returns 1.0

``acos-math``
-----------

**Description:** Returns result of the arccosine function for an input value

**Parameters:**
    - Float: Input float value

**Return:** Result of the arccosine function

**Example:**

.. code-block:: metta

    !(acos-math 1) ; Returns 0.0

``tan-math``
----------

**Description:** Returns result of the tangent function for an input value in radians

**Parameters:**
    - Angle: Angle in radians

**Return:** Result of the tangent function

**Example:**

.. code-block:: metta

    !(tan-math 0) ; Returns 0.0

``atan-math``
-----------

**Description:** Returns result of the arctangent function for an input value

**Parameters:**
    - Float: Input float value

**Return:** Result of the arctangent function

**Example:**

.. code-block:: metta

    !(atan-math 0) ; Returns 0.0

``isnan-math``
------------

**Description:** Returns True if input value is NaN. False - otherwise

**Parameters:**
    - Number: Number

**Return:** True/False

**Example:**

.. code-block:: metta

    !(isnan-math 0.0) ; Returns False

``isinf-math``
------------

**Description:** Returns True if input value is positive or negative infinity. False - otherwise

**Parameters:**
    - Number: Number

**Return:** True/False

**Example:**

.. code-block:: metta

    !(isinf-math 0.0) ; Returns False

``min-atom``
----------

**Description:** Returns atom with min value in the expression. Only numbers allowed

**Parameters:**
    - Expression: Expression which contains atoms of Number type

**Return:** Min value in the expression. Error if expression contains non-numeric value or is empty

**Example:**

.. code-block:: metta

    !(min-atom (2 6 7 4 9 3)) ; Returns 2.0

``max-atom``
----------

**Description:** Returns atom with max value in the expression. Only numbers allowed

**Parameters:**
    - Expression: Expression which contains atoms of Number type

**Return:** Max value in the expression. Error if expression contains non-numeric value or is empty

**Example:**

.. code-block:: metta

    !(max-atom (2 6 7 4 9 3)) ; Returns 9.0

``random-int``
------------

**Description:** Returns random int number from range defined by two numbers

**Parameters:**
    - Range start: Range start
    - Range end: Range end

**Return:** Random int number from defined range

**Example:**

.. code-block:: metta

    !(random-int &rng 2 9) ; Returns any int number between 2 to 9

``random-float``
--------------

**Description:** Returns random float number from range defined by two numbers

**Parameters:**
    - Range start: Range start
    - Range end: Range end

**Return:** Random float number from defined range

**Example:**

.. code-block:: metta

    !(random-float &rng 2 9) ; Returns any number in the interval [2, 9)
