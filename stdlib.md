# MeTTa Standard Library Documentation

This document details the built-in functions and atoms available in the MeTTa standard library.

## Table of Contents

1.  [Equality and Reduction](#equality-and-reduction)
2.  [Error Handling](#error-handling)
3.  [Evaluation Control](#evaluation-control)
4.  [Expression Manipulation](#expression-manipulation)
5.  [Mathematical Operations](#mathematical-operations)
6.  [Non-deterministic Computation](#non-deterministic-computation)
7.  [Type System](#type-system)
8.  [List Manipulation](#list-manipulation)
9.  [Logic Operations](#logic-operations)
10. [Atomspace Interaction](#atomspace-interaction)
11. [Quoting](#quoting)
12. [Set Operations](#set-operations)
13. [Documentation](#documentation)

---

## 1. Equality and Reduction <a name="equality-and-reduction"></a>

### `=` (Equality/Reduction Rule Definition)

*   **Description:** Defines a reduction rule for expressions. The left-hand side is a pattern, and the right-hand side is the result of the reduction.
*   **Parameters:**
    *   Pattern: The expression to be matched.
    *   Result: The expression to replace the matched pattern with.
*   **Return:** Not reduced itself unless custom equalities over equalities are added
*   **Example:**

    ```metta
    (= (add 1 2) 3) | (add 1 2) will be reduced to 3
    ```

### `id` (Identity)

*   **Description:** Returns its argument unchanged.
*   **Parameters:**
    *   Input: Any atom.
*   **Return:** The input atom.
*   **Example:**

    ```metta
    !(id 5) ; Returns 5
    ```

---

## 2. Error Handling <a name="error-handling"></a>

### `ErrorType`

*   **Description:** Type of the atom which contains error.
*   **Type:** Type

### `Error`

*   **Description:** Constructs an error atom, indicating a problem during evaluation.
*   **Parameters:**
    *   Atom: The atom where the error occurred.
    *   Message: An error message, such as `BadType` or `IncorrectNumberOfArguments`.
*   **Return:** An error atom.
*   **Example:**

    ```metta
    (Error (add "a" 2) BadType)
    ```

### `if-error`

*   **Description:** Checks if an atom is an error. Returns one value if it is, and another if it is not.
*   **Parameters:**
    *   Atom: The atom to be checked.
    *   Then: Value to return if the atom is an error.
    *   Else: Value to return otherwise.
*   **Return:** Either the `Then` or `Else` argument.
*   **Example:**

    ```metta
    !(if-error (Error 5 BadType) "Error!" "No error") ; Returns "Error!"
    ```

### `return-on-error`

*   **Description:** Returns the first argument if the argument is an Empty or an error. Returns the second argument otherwise.
*   **Parameters:**
    *   Atom: Atom to be checked.
    *   Then: Atom for further evaluation if first argumet is not an Error or Empty.
*   **Return:** Return previous result if it is an error or Empty. If not it continues the evaluation
*   **Example:**

    ```metta
    !(return-on-error (Error 5 BadType) 6) ; Returns (Error 5 BadType)
    !(return-on-error 5 6) ; Returns 6
    ```

---

## 3. Evaluation Control <a name="evaluation-control"></a>

### `return`

*   **Description:** Returns a value from a `function` expression.
*   **Parameters:**
    *   Value: The value to be returned.
*   **Return:** The input value.
*   **Example:**

    ```metta
    ! (function (return 5)) ; Returns 5
    ```

### `function`

*   **Description:** Evaluates the argument until it becomes `(return <result>)`, then reduces to `<result>`.
*   **Parameters:**
    *   Atom: The atom to be evaluated.
*   **Return:** The result of the atom's evaluation.
*   **Example:**

    ```metta
    !(function (return (+ 1 2))) ; Returns 3 because (+ 1 2) evaluates to 3 which becomes (return 3)
    ```

### `eval`

*   **Description:** Evaluates an atom, performing one step of reduction.  This can be via equality rules or grounded functions.
*   **Parameters:**
    *   Atom: The atom to be evaluated.
*   **Return:** The result of the evaluation.
*   **Example:**

    ```metta
    (= (double $x) (+ $x $x))
    !(eval (double 5)) ; Returns (+ 5 5)
    !(eval (+ 5 5)) ; Returns 10
    ```

### `evalc`

*   **Description:** Evaluates an atom within a specific atomspace context.
*   **Parameters:**
    *   Atom: The atom to be evaluated.
    *   Space: The atomspace to evaluate the atom in it's context.
*   **Return:** The result of the evaluation.
*   **Example:**

    ```metta
    (= (double $x) (+ $x $x))
    !(evalc (double 5) &self) ; Returns (+ 5 5) self being the working space
    !(evalc (+ 5 5) &self) ; Returns 10
    ```

### `chain`

*   **Description:** Evaluates an atom, binds the result to a variable, and then evaluates another atom containing the variable.
*   **Parameters:**
    *   Atom: The atom to be evaluated initially.
    *   Variable: The variable to bind the result to.
    *   Template: The atom to evaluate after binding.
*   **Return:** The result of evaluating the template.
*   **Example:**

    ```metta
    !(chain (+ 2 3) $x (* $x 2)) ; Evaluates (+ 2 3) to 5, binds it to $x, then evaluates (* $x 2), returning 10.
    ```

### `unify`

*   **Description:** Attempts to unify two atoms. If successful, returns one value; otherwise, returns another.
*   **Parameters:**
    *   Atom1: The first atom to be unified.
    *   Atom2: The second atom to unified.
    *   Then: The value to be returned if unification succeeds.
    *   Else: The value to be returned if unification fails.
*   **Return:** Either the `Then` or `Else` argument.
*   **Example:**

    ```metta
    !(unify A A "Matched!" "Didn't match") ; Returns "Matched!"
    !(unify A B "Matched!" "Didn't match") ; Returns "Didn't match"
    ```

### `switch`

*   **Description:** Subsequently tests multiple pattern-matching conditions for the given value.
*   **Parameters:**
    *   Atom: Atom to be matched with patterns
    *   Cases: Tuple of pairs mapping condition patterns to results.
*   **Return:** Result which corresponds to the pattern which is matched with the passed atom first
*   **Example:**

    ```metta
    !(switch 2 ((1 "one") (2 "two") (3 "three"))) ; Returns "two"
    ```

### `case`

*   **Description:** Subsequently tests multiple pattern-matching conditions for the given value.
*   **Parameters:**
    *   Atom: Atom to be matched with patterns. Note that this atom will be evaluated.
    *   Cases: Tuple of pairs mapping condition patterns to results.
*   **Return:** Result of evaluating of Atom bound to met condition.
*   **Example:**

    ```metta
    !(case 2 ((1 "one") (2 "two") (3 "three"))) ; Returns "two"
    ```

### `let`

*   **Description:** Unifies two atoms and apply result of the unification on the third argument. Second argument is evaluated before unification.
*   **Parameters:**
    *   Pattern: First atom to be unified.
    *   Atom: Second atom to be unified.
    *   Template: Expression which will be evaluated if two first arguments can be unified.
*   **Return:** Third argument or Empty
*   **Example:**

    ```metta
    !(let $x 5 (+ $x 2)) ; Returns 7
    ```

### `let*`

*   **Description:** Same as let but inputs list of pairs of atoms to be unified.
*   **Parameters:**
    *   Pairs: List of pairs, atoms in each pair to be unified.
    *   Template: Expression which will be evaluated if each pair can be unified.
*   **Return:** Second argument or Empty
*   **Example:**

    ```metta
    !(let* (($x 5) ($y 10)) (+ $x $y)) ; Returns 15
    ```

### `if`

*   **Description:** Replace itself by one of the arguments depending on condition.
*   **Parameters:**
    *   Condition: Boolean condition
    *   Then: Result when condition is True
    *   Else: Result when condition is False
*   **Return:** Second or third argument
*   **Example:**

    ```metta
    !(if True 5 10) ; Returns 5
    !(if False 5 10) ; Returns 10
    ```

---

## 4. Expression Manipulation <a name="expression-manipulation"></a>

### `cons-atom`

*   **Description:** Constructs an expression (list) by adding an atom to the head of another expression.
*   **Parameters:**
    *   Head: The atom to be added to the beginning.
    *   Tail: The expression to be added the atom to.
*   **Return:** A new expression formed from the head and the tail.
*   **Example:**

    ```metta
    !(cons-atom 1 (2 3)) ; Returns (1 2 3)
    ```

### `decons-atom`

*   **Description:** Deconstructs an expression into its head and tail.
*   **Parameters:**
    *   Expression: The expression to be deconstructed.
*   **Return:** An expression containing the head and tail: `(Head Tail)`.
*   **Example:**

    ```metta
    !(decons-atom (1 2 3)) ; Returns ((1) (2 3))
    ```

### `car-atom`

*   **Description:** Extracts the first atom of an expression.
*   **Parameters:**
    *   Expression: The expression to extract the first atom from.
*   **Return:** The first atom of the expression.
*   **Example:**

    ```metta
    !(car-atom (1 2 3)) ; Returns 1
    ```

### `cdr-atom`

*   **Description:** Extracts the tail of an expression (all atoms except the first).
*   **Parameters:**
    *   Expression: The expression to extract the tail from.
*   **Return:** The tail of the expression.
*   **Example:**

    ```metta
    !(cdr-atom (1 2 3)) ; Returns (2 3)
    ```

### `size-atom`

*   **Description:** Returns size of an expression.
*   **Parameters:**
    *   Expression: The expression whose size is to be determined.
*   **Return:** Size of an expression.
*   **Example:**

    ```metta
    !(size-atom (1 2 3)) ; Returns 3
    ```

### `index-atom`

*   **Description:** Returns atom from an expression using index or error if the index is out of bounds
*   **Parameters:**
    *   Expression: The expression to extract from.
    *   Index: The index of the target atom.
*   **Return:** Atom from an expression in the position defined by index. Error if index is out of bounds
*   **Example:**

    ```metta
    !(index-atom (1 2 3) 1) ; Returns 2
    ```

---

## 5. Mathematical Operations <a name="mathematical-operations"></a>

### `pow-math`

*   **Description:** Calculates the power of a base raised to an exponent.
*   **Parameters:**
    *   Base: The base number.
    *   Power: The exponent.
*   **Return:** The result of the power function.
*   **Example:**

    ```metta
    !(pow-math 2 3) ; Returns 8.0
    ```

### `sqrt-math`

*   **Description:** Calculates the square root of a number.
*   **Parameters:**
    *   Number: The number to calculate the square root of. Must be >= 0.
*   **Return:** The square root of the number.
*   **Example:**

    ```metta
    !(sqrt-math 9) ; Returns 3.0
    ```

### `abs-math`

*   **Description:** Calculates the absolute value of a number.
*   **Parameters:**
    *   Number: The number to calculate the absolute value of.
*   **Return:** The absolute value of the number.
*   **Example:**

    ```metta
    !(abs-math -5) ; Returns 5
    ```

### `log-math`

*   **Description:** Calculates the logarithm of a number with a given base.
*   **Parameters:**
    *   Base: The base of the logarithm.
    *   Number: The number to calculate the logarithm of.
*   **Return:** The result of the logarithm function.
*   **Example:**

    ```metta
    !(log-math 10 100) ; Returns 2.0
    ```

### `trunc-math`

*   **Description:** Returns the integer part of the input value
*   **Parameters:**
    *   Float: Input float value
*   **Return:** Integer part of the float
*   **Example:**

    ```metta
    !(trunc-math 5.6) ; Returns 5.0
    ```

### `ceil-math`

*   **Description:** Returns the smallest integer greater than or equal to the input value
*   **Parameters:**
    *   Float: Input float value
*   **Return:** Integer value greater than or equal to the input
*   **Example:**

    ```metta
    !(ceil-math 5.2) ; Returns 6.0
    ```

### `floor-math`

*   **Description:** Returns the smallest integer less than or equal to the input value
*   **Parameters:**
    *   Float: Input float value
*   **Return:** Integer value less than or equal to the input
*   **Example:**

    ```metta
    !(floor-math 5.8) ; Returns 5.0
    ```

### `round-math`

*   **Description:** Returns the nearest integer to the input float value
*   **Parameters:**
    *   Float: Input float value
*   **Return:** Nearest integer to the input
*   **Example:**

    ```metta
    !(round-math 5.4) ; Returns 5.0
    !(round-math 5.6) ; Returns 6.0
    ```

### `sin-math`

*   **Description:** Returns result of the sine function for an input value in radians
*   **Parameters:**
    *   Angle: Angle in radians
*   **Return:** Result of the sine function
*   **Example:**

    ```metta
    !(sin-math 0) ; Returns 0.0
    ```

### `asin-math`

*   **Description:** Returns result of the arcsine function for an input value
*   **Parameters:**
    *   Float: Input float value
*   **Return:** Result of the arcsine function
*   **Example:**

    ```metta
    !(asin-math 0) ; Returns 0.0
    ```

### `cos-math`

*   **Description:** Returns result of the cosine function for an input value in radians
*   **Parameters:**
    *   Angle: Angle in radians
*   **Return:** Result of the cosine function
*   **Example:**

    ```metta
    !(cos-math 0) ; Returns 1.0
    ```

### `acos-math`

*   **Description:** Returns result of the arccosine function for an input value
*   **Parameters:**
    *   Float: Input float value
*   **Return:** Result of the arccosine function
*   **Example:**

    ```metta
    !(acos-math 1) ; Returns 0.0
    ```

### `tan-math`

*   **Description:** Returns result of the tangent function for an input value in radians
*   **Parameters:**
    *   Angle: Angle in radians
*   **Return:** Result of the tangent function
*   **Example:**

    ```metta
    !(tan-math 0) ; Returns 0.0
    ```

### `atan-math`

*   **Description:** Returns result of the arctangent function for an input value
*   **Parameters:**
    *   Float: Input float value
*   **Return:** Result of the arctangent function
*   **Example:**

    ```metta
    !(atan-math 0) ; Returns 0.0
    ```

### `isnan-math`

*   **Description:** Returns True if input value is NaN. False - otherwise
*   **Parameters:**
    *   Number: Number
*   **Return:** True/False
*   **Example:**

    ```metta
    !(isnan-math 0.0) ; Returns False
    ```

### `isinf-math`

*   **Description:** Returns True if input value is positive or negative infinity. False - otherwise
*   **Parameters:**
    *   Number: Number
*   **Return:** True/False
*   **Example:**

    ```metta
    !(isinf-math 0.0) ; Returns False
    ```

### `min-atom`

*   **Description:** Returns atom with min value in the expression. Only numbers allowed
*   **Parameters:**
    *   Expression: Expression which contains atoms of Number type
*   **Return:** Min value in the expression. Error if expression contains non-numeric value or is empty
*   **Example:**

    ```metta
    !(min-atom (2 6 7 4 9 3)) ; Returns 2.0
    ```

### `max-atom`

*   **Description:** Returns atom with max value in the expression. Only numbers allowed
*   **Parameters:**
    *   Expression: Expression which contains atoms of Number type
*   **Return:** Max value in the expression. Error if expression contains non-numeric value or is empty
*   **Example:**

    ```metta
    !(max-atom (2 6 7 4 9 3)) ; Returns 9.0
    ```

### `random-int`

*   **Description:** Returns random int number from range defined by two numbers
*   **Parameters:**
    *   Range start: Range start
    *   Range end: Range end
*   **Return:** Random int number from defined range. Raise Range is empty error if start >= end
*   **Example:**

    ```metta
    !(random-int 2 9) ; Returns any int number between 2 to 9
    ```

### `random-float`

*   **Description:** Returns random float number from range defined by two numbers
*   **Parameters:**
    *   Range start: Range start
    *   Range end: Range end
*   **Return:** Random float number from defined range. Raise Range is empty error if start >= end
*   **Example:**

    ```metta
    !(random-float 2 9) ; Returns any number in the interval [2, 9)
    ```

---

## 6. Non-deterministic Computation <a name="non-deterministic-computation"></a>

### `collapse-bind`

*   **Description:** Evaluates a MeTTa operation and returns an expression containing all alternative evaluations in the form `(Atom Bindings)`.
*   **Parameters:**
    *   Atom: The MeTTa operation to be evaluated.
*   **Return:** An expression of alternative evaluations with bindings.
*   **Example:**

    ```metta
    (= (bin) 0)
    (= (bin) 1)
    !(collapse-bind (bin)) ; Returns (0 { }), (1 { }) nondeterministically
    ```

### `superpose-bind`

*   **Description:** Takes the result of `collapse-bind` and returns only the result atoms, discarding the bindings.
*   **Parameters:**
    *   Expression: An expression in the form `(Atom Bindings)`.
*   **Return:** A non-deterministic list of atoms.
*   **Example:**
    ```metta
    !(superpose-bind ((A (Grounded ...)) (B (Grounded ...)))) ; returns the equivalent of (superpose (A B))
    ```

### `superpose`

*   **Description:** Turns a tuple into a nondeterministic result.
*   **Parameters:**
    *   Tuple: Tuple to be converted.
*   **Return:** Argument converted to nondeterministic result
*   **Example:**
    ```metta
    !(superpose (A B C)) ; returns A, B, C nondeterministically
    ```

### `collapse`

*   **Description:** Converts a nondeterministic result into a tuple.
*   **Parameters:**
    *   Atom: Atom which will be evaluated.
*   **Return:** Tuple
*   **Example:**
    ```metta
    !(collapse (superpose (A B C))) ; returns (A B C)
    ```

---

## 7. Type System <a name="type-system"></a>

### `is-function`

*   **Description:** Checks if a type is a function type.
*   **Parameters:**
    *   Type: The type atom to be checked.
*   **Return:** `True` if the type is a function type, `False` otherwise.
*   **Example:**

    ```metta
    !(is-function (-> Atom Atom)) ; Returns True
    !(is-function Atom) ; Returns False
    ```

### `type-cast`

*   **Description:** Attempts to cast an atom to a specific type within an atomspace context.
*   **Parameters:**
    *   Atom: The atom to be casted.
    *   Type: The target type.
    *   Space: The atomspace to be used as context.
*   **Return:** The atom if the casting is successful, or an `Error` atom if not.
*   **Example:**

    ```metta
    (: type1 Type)
    !(type-cast A type1 &self) ; A
    !(type-cast 1 type1 &self) ; Error 1 BasType
    ```

### `match-types`

*   **Description:** Checks if two types can be unified and returns one value if so, another - otherwise.
*   **Parameters:**
    *   Type1: The first type.
    *   Type2: The second type.
    *   Then: Atom to be returned if types can be unified.
    *   Else: Atom to be returned if types cannot be unified.
*   **Return:** Third or fourth argument
*   **Example:**

    ```metta
    !(match-types Atom Atom "Matched!" "Didn't match") ; Returns "Matched!"
    !(match-types Bool Number "Matched!" "Didn't match") ; Returns "Didn't match"
    ```

### `first-from-pair`

*   **Description:** Gets a pair as a first argument and returns first atom from pair.
*   **Parameters:**
    *   Pair: Pair.
*   **Return:** First atom from a pair.
*   **Example:**

    ```metta
    !(first-from-pair (A B)) ; Returns A
    ```

### `match-type-or`

*   **Description:** Checks if two types can be unified and returns result of OR operation between first argument and type checking result.
*   **Parameters:**
    *   Folded: Boolean value
    *   Next: First type.
    *   Type: Second type.
*   **Return:** True or False
*   **Example:**

    ```metta
    !(match-type-or True Number Number) ; Returns True
    !(match-type-or False Number Number) ; Returns True
    !(match-type-or True Number Bool) ; Returns True
    !(match-type-or False Number Bool) ; Returns False
    
    ```

---

## 8. List Manipulation <a name="list-manipulation"></a>

### `filter-atom`

*   **Description:** Filters a list of atoms based on a predicate.
*   **Parameters:**
    *   List: The list of atoms to filter.
    *   Variable: The variable to use in the predicate.
    *   Filter: The predicate to apply (an expression that returns `True` or `False`).
*   **Return:** A new list containing only the atoms that satisfy the predicate.
*   **Example:**

    ```metta
    !(filter-atom (1 2 3 4 5) $x (> $x 3)) ; Returns (4 5)
    ```

### `map-atom`

*   **Description:** Applies a function to each atom in a list, creating a new list with the results.
*   **Parameters:**
    *   List: The list of atoms to map over.
    *   Variable: The variable to use in the mapping expression.
    *   Map: The expression to apply to each atom.
*   **Return:** A new list with the mapped values.
*   **Example:**

    ```metta
    !(map-atom (1 2 3) $x (+ $x 1)) ; Returns (2 3 4)
    ```

### `foldl-atom`

*   **Description:** Folds (reduces) a list of values into a single value, using a binary operation.  This is a left fold.
*   **Parameters:**
    *   List: The list of values to be folded.
    *   Init: The initial value.
    *   A: The variable to hold the accumulated value.
    *   B: The variable to hold the current element of the list.
    *   Op: The binary operation to apply (an expression using `A` and `B`).
*   **Return:** The final accumulated value.
*   **Example:**

    ```metta
    !(foldl-atom (1 2 3 4) 0 $acc $x (+ $acc $x)) ; Returns 10 (1+2+3+4)
    ```

---

## 9. Logic Operations <a name="logic-operations"></a>

### `or`

*   **Description:** Logical disjunction of two arguments.
*   **Parameters:**
    *   Arg1: First argument
    *   Arg2: Second argument
*   **Return:** True if any of input arguments is True, False - otherwise
*   **Example:**

    ```metta
    !(or True False) ; Returns True
    ```

### `and`

*   **Description:** Logical conjunction of two arguments
*   **Parameters:**
    *   Arg1: First argument
    *   Arg2: Second argument
*   **Return:** Returns True if both arguments are True, False - otherwise
*   **Example:**

    ```metta
    !(and True False) ; Returns False
    !(and True True) ; Returns True
    ```

### `not`

*   **Description:** Logical negation.
*   **Parameters:**
    *   Arg: Argument
*   **Return:** Negates boolean input argument (False -> True, True -> False)
*   **Example:**

    ```metta
    !(not True) ; Returns False
    !(not False) ; Returns True
    ```

### `xor`

*   **Description:** Logical exclusive or.
*   **Parameters:**
    *   Arg1: First argument
    *   Arg2: Second argument
*   **Return:** Returns True if one and only one of the inputs is True
*   **Example:**

    ```metta
    !(xor True False) ; Returns True
    !(xor True True) ; Returns False
    ```

### `flip`

*   **Description:** Random boolean value.
*   **Parameters:**
    *   None
*   **Return:** Returns uniformly distributed random boolean value
*   **Example:**

    ```metta
    !(flip) ; Returns True or False
    ```

---

## 10. Atomspace Interaction <a name="atomspace-interaction"></a>

### `add-reduct`

*   **Description:** Reduces an atom and adds it to the atomspace.
*   **Parameters:**
    *   Space: The atomspace to add the atom to.
    *   Atom: The atom to add.
*   **Return:** Unit atom
*   **Example:**

    ```metta
    !(add-reduct &self (= (add) (+ 1 3))); This will add (= (add) 4) to the working space, &self
    ```

### `add-atom`

*   **Description:** Adds an atom into the atomspace without reducing it.
*   **Parameters:**
    *   Space: Atomspace to add atom into
    *   Atom: Atom to be added
*   **Return:** Unit atom
*   **Example:**

    ```metta
    !(add-atom &self (= (add) (+ 1 3))); This will add (= (add) (+ 1 3)) to the working space, &self
    ```

### `get-type`

*   **Description:** Returns type notation of input atom.
*   **Parameters:**
    *   Atom: Atom to get type for
*   **Return:** Type notation or %Undefined% if there is no type for input Atom
*   **Example:**

    ```metta
    !(get-type 1); Returns Number
    ```

### `get-type-space`

*   **Description:** Returns type notation of input Atom relative to a specified atomspace.
*   **Parameters:**
    *   Space: Atomspace where type notation for input atom will be searched
    *   Atom: Atom to get type for
*   **Return:** Type notation or %Undefined% if there is no type for input Atom in provided atomspace
*   **Example:**

    ```metta
    (: a A)
    !(get-type-space &self a); Returns A because we defined the type of a to be A in the working space, &self
    ```

### `get-metatype`

*   **Description:** Returns metatype of the input atom
*   **Parameters:**
    *   Atom: Atom to get metatype for
*   **Return:** Metatype of input atom
*   **Example:**

    ```metta
    !(get-metatype True); Returns Grounded
    ! (get-metatype (a b)); Return Expression
    ```

### `if-equal`

*   **Description:** Checks if first two arguments are equal and evaluates third argument if equal, fourth argument - otherwise.
*   **Parameters:**
    *   Arg1: First argument
    *   Arg2: Second argument
    *   Then: Atom to be evaluated if arguments are equal
    *   Else: Atom to be evaluated if arguments are not equal
*   **Return:** Evaluated third or fourth argument
*   **Example:**

    ```metta
    !(if-equal 1 1 "Equal" "Not Equal"); Returns "Equal"
    !(if-equal 1 2 "Equal" "Not Equal"); Returns "Not Equal"
    ```

### `new-space`

*   **Description:** Creates new Atomspace which could be used further in the program as a separate from &self Atomspace
*   **Parameters:** None
*   **Return:** Reference to a new space
*   **Example:**

    ```metta
    !(new-space); Returns reference to the new space
    ```

### `remove-atom`

*   **Description:** Removes atom from the input Atomspace
*   **Parameters:**
    *   Space: Reference to the space from which the Atom needs to be removed
    *   Atom: Atom to be removed
*   **Return:** Unit atom
*   **Example:**

    ```metta
    !(remove-atom &self (= (add) 4)); Removes (= (add) 4) from the working space, &self
    ```

### `get-atoms`

*   **Description:** Shows all atoms in the input Atomspace
*   **Parameters:**
    *   Space: Reference to the space
*   **Return:** List of all atoms in the input space
*   **Example:**

    ```metta
    !(get-atoms &self); Returns all atoms inside &self
    ```

### `match`

*   **Description:** Searches for all declared atoms corresponding to the given pattern inside space and returns the output template
*   **Parameters:**
    *   Space: Atomspace to search pattern
    *   Pattern: Pattern atom to be searched
    *   Output: Output template typically containing variables from the input pattern
*   **Return:** If match was successfull it outputs template with filled variables using matched pattern. Empty - otherwise
*   **Example:**

    ```metta
    (= (add) (+ 1 2))
    (= (add) (+ 4 2))
    !(match &self (= (add) (+ $x $y)) $x); Returns 1, 4
    ```

---

## 11. Quoting <a name="quoting"></a>

### `quote`

*   **Description:** Prevents an atom from being reduced.
*   **Parameters:**
    *   Atom: The atom to be quoted.
*   **Return:** The quoted atom (which will not be evaluated).
*   **Example:**

    ```metta
    !(quote (+ 1 2)) ; Returns (quote (+ 1 2)) instead of 3
    ```

### `unquote`

*   **Description:** Removes the quote from a quoted atom.
*   **Parameters:**
    *   QuotedAtom: The atom to be unquoted.
*   **Return:** The original, unquoted atom.
*   **Example:**

    ```metta
    !(unquote (quote (+ 1 2))) ; Returns 3
    ```

### `noreduce-eq`

*   **Description:** Checks equality of two atoms without reducing them.
*   **Parameters:**
    *   A: First atom
    *   B: Second atom
*   **Return:** True if not reduced atoms are equal, False - otherwise
*   **Example:**

    ```metta
    !(noreduce-eq (+ 1 2) (+ 1 2)) ; Returns True
    !(noreduce-eq (+ 1 2) 3) ; Returns False
    ```

---

## 12. Set Operations <a name="set-operations"></a>

### `unique`

*   **Description:** Returns unique entities from non-deterministic input.
*   **Parameters:**
    *   Arg: Non-deterministic set of values
*   **Return:** Unique values from input set
*   **Example:**

    ```metta
    !(unique (superpose (a b c d d))) ; Returns [a, b, c, d]
    ```

### `union`

*   **Description:** Returns union of two non-deterministic inputs.
*   **Parameters:**
    *   Arg1: Non-deterministic set of values
    *   Arg2: Another non-deterministic set of values
*   **Return:** Union of sets
*   **Example:**

    ```metta
    !(union (superpose (a b b c)) (superpose (b c c d))) ; Returns [a, b, b, c, b, c, c, d]
    ```

### `intersection`

*   **Description:** Returns intersection of two non-deterministic inputs.
*   **Parameters:**
    *   Arg1: Non-deterministic set of values
    *   Arg2: Another non-deterministic set of values
*   **Return:** Intersection of sets
*   **Example:**

    ```metta
    !(intersection (superpose (a b c c)) (superpose (b c c c d))) ; Returns [b, c, c]
    ```

### `subtraction`

*   **Description:** Returns subtraction of two non-deterministic inputs.
*   **Parameters:**
    *   Arg1: Non-deterministic set of values
    *   Arg2: Another non-deterministic set of values
*   **Return:** Subtraction of sets
*   **Example:**

    ```metta
    !(subtraction (superpose (a b b c)) (superpose (b c c d))) ; Returns [a, b]
    ```

### `unique-atom`

*   **Description:** Function takes tuple and returns only unique entities
*   **Parameters:**
    *   List: List of values
*   **Return:** Unique values from input set
*   **Example:**

    ```metta
    !(unique-atom (a b c d d)) ; Returns (a b c d)
    ```

### `union-atom`

*   **Description:** Function takes two tuples and returns their union
*   **Parameters:**
    *   List1: List of values
    *   List2: List of values
*   **Return:** Union of sets
*   **Example:**

    ```metta
    !(union-atom (a b b c) (b c c d)) ; Returns (a b b c b c c d)
    ```

### `intersection-atom`

*   **Description:** Function takes two tuples and returns their intersection
*   **Parameters:**
    *   List1: List of values
    *   List2: List of values
*   **Return:** Intersection of sets
*   **Example:**

    ```metta
    !(intersection-atom (a b c c) (b c c c d)) ; Returns (b c c)
    ```

### `subtraction-atom`

*   **Description:** Function takes two tuples and returns their subtraction
*   **Parameters:**
    *   List1: List of values
    *   List2: List of values
*   **Return:** Subtraction of sets
*   **Example:**

    ```metta
    !(subtraction-atom (a b b c) (b c c d)) ; Returns (a b)
    ```

---

## 13. Documentation <a name="documentation"></a>

### `@doc
