Documentation formatting functions
==============

``@doc``
-------------

**Description:** Used for documentation purposes. Functions' documentation starts with @doc key word.

**Parameters:**
    - Atom: The name of the function to be documented
    - DocDescription: A description of the function which starts with @desc.
    - DocParameters: parameters description starting with @params which should contain one or more @param symbols
    - DocReturnInformal: Optional field for the function's return value starts with @return

**Return:** Function documentation as DocInformal format.

**Example:**

.. code-block:: metta
    !(@doc =
    (@desc "A symbol used to define reduction rules for expressions.")
    (@params (
        (@param "Pattern to be matched against expression to be reduced")
        (@param "Result of reduction or transformation of the first pattern") ))
    (@return "Not reduced itself unless custom equalities over equalities are added") )
    ; Returns itself

``@desc``
------------

**Description:** Used for documentation purposes. A symbol used to define description of a function being a part of @doc.

**Parameters:**
    - String: The description of the function.

**Return:** Returns what was passed as a parameter, which is a description of the function in DocDescription format.

**Example:**

.. code-block:: metta

    !(@desc "A symbol used to define reduction rules for expressions.") ; Returns itself

``@params``
------------

**Description:** Used for documentation purposes. Contains several @param entities with description of each @param as a part of @doc.

**Parameters:**
    - Expression: Several (@param ...) entities.

**Return:** Returns parameters' description as DocParameters format.

**Example:**

.. code-block:: metta

    !(@params (
        (@param "Pattern to be matched against expression to be reduced")
        (@param "Result of reduction or transformation of the first pattern") ))
    ; Returns itself

``@param``
-------------------

**Description:** Used for documentation purposes. Description of a function parameter starts with @param as a part of @params which is a part of @doc.

**Parameters:**
    - String: The description of the function parameter.

**Return:** Returns parameter's description as DocParameterInformal format.

**Example:**

.. code-block:: metta
    
    !(@param "Pattern to be matched against expression to be reduced") ; Returns itself

``@return``
-------------------

**Description:** Used for documentation purposes. Description of what a function returns as a part of @doc.

**Parameters:**
    - String: The description of what a function returns.

**Return:** Return description of what a function returns in DocReturnInformal format, (@return description).

**Example:**

.. code-block:: metta

    !(@return "Not reduced itself unless custom equalities over equalities are added") ; Returns itself

``@doc-formal``
-------------------

**Description:** Used for documentation purposes, get-doc returns documentation starting with @doc-formal symbol.

**Parameters:**
    - DocItem: Function/Atom name for which documentation is to be displayed. Format (@item name).
    - DocKind: The kind of of entity is to be displayed. Can be either DocKindFunction (@kind function) or DocKindAtom (@kind Atom).
    - DocType: The type notation of entity to be displayed.
    - DocDescription: The description of entity to be displayed.
    - DocParameters: (Function only) the parameters of the function whose documentation is to be displayed.
    - DocReturn: (Function only) the return value of the function whose documentation is to be displayed.

**Return:** The full documentation of the function in DocFormal format.

**Example:**

.. code-block:: metta

    !(@doc-formal (@item if-error) (@kind function) (@type (-> Atom Atom Atom Atom)) (@desc "Checks if first argument is an error atom. Returns second argument if so or third argument otherwise.") (@params ((@param (@type Atom) (@desc "Atom to be checked for the error")) (@param (@type Atom) (@desc "Value to return if first argument is an error")) (@param (@type Atom) (@desc "Value to return otherwise")))) (@return (@type Atom) (@desc "Second or third argument"))) ; Returns itself

``@item``
-------------------

**Description:** Used for documentation purposes. Converts atom/function's name to DocItem.

**Parameters:**
    - Atom: The name of the function/atom to be converted to DocItem.

**Return:** The DocItem of the function/atom in DocItem format.

**Example:**

.. code-block:: metta

    !(@item if-error) ; Returns (@item if-error)

``@kind``
-------------------

**Description:** Used for documentation purposes. Converts atom/function's type to DocKindAtom/DocKindFunction.

**Parameters:**
    - Kind: Can be either DocKindFunction or DocKindAtom.

**Return:** The kind of entity to be displayed, in DocKindFunction (@kind function) or DocKindAtom (@kind Atom) format.

**Example:**

.. code-block:: metta

    !(@kind function) ; Returns (@kind function)

    !(@kind Atom) ; Returns (@kind Atom)

``@type``
-------------------

**Description:** Used for documentation purposes. Converts atom/function's type to DocType.

**Parameters:**
    - Type: The type notation of entity to be displayed.

**Return:** The type notation of entity to be displayed in DocType format, (@type Type).

**Example:**

.. code-block:: metta

    !(@type (-> Atom Atom Atom Atom)) ; Returns (@type (-> Atom Atom Atom Atom))


.. note::
    The above mentioned functions are used to generate documentation for your MeTTa code. They help in creating standardized documentation formats for different elements of your code. They are not meant to be used for getting documentation of functions/atoms. For that see below.

``get-doc``
-------------------

**Description:** Returns documentation of a given function/atom.

**Parameters:**
    - Atom: The name of the function/atom to get documentation for.

**Return:** The documentation of the function/atom in DocFormal format.

**Example:**

.. code-block:: metta

    !(get-doc or) 
    ; Returns (@doc-formal (@item or) (@kind function) (@type (-> Bool Bool Bool)) (@desc "Logical disjunction of two arguments") (@params ((@param (@type Bool) (@desc "First argument")) (@param (@type Bool) (@desc "Second argument")))) (@return (@type Bool) (@desc "True if any of input arguments is True, False - otherwise")))

``get-doc-single-atom``
-------------------

**Description:** Function used by get-doc to get documentation on either function or atom. It checks if input name is the name of function or atom and calls correspondent function.

**Parameters:**
    - Atom: The name of the atom to get documentation for.

**Return:** Documentation for the given atom/function in DocFormal format.

**Example:**

.. code-block:: metta

    !(get-doc-single-atom or) 
    ; Calls get-doc-function and return (@doc-formal (@item or) (@kind function) (@type (-> Bool Bool Bool)) (@desc "Logical disjunction of two arguments") (@params ((@param (@type Bool) (@desc "First argument")) (@param (@type Bool) (@desc "Second argument")))) (@return (@type Bool) (@desc "True if any of input arguments is True, False - otherwise")))

``get-doc-function``
-------------------

**Description:** Function used by get-doc-single-atom to get documentation on a function. 

**Parameters:**
    - Atom: The name of the function to get documentation for.
    - Type: The type notation of the function to get documentation for.

**Return:** Documentation on the function in DocFormal format if it exists or default documentation with no description otherwise.

**Example:**

.. code-block:: metta

    !(get-doc-function or (-> Bool Bool Bool))
    ; Returns (@doc-formal (@item or) (@kind function) (@type (-> Bool Bool Bool)) (@desc "Logical disjunction of two arguments") (@params ((@param (@type Bool) (@desc "First argument")) (@param (@type Bool) (@desc "Second argument")))) (@return (@type Bool) (@desc "True if any of input arguments is True, False - otherwise")))

    !(get-doc-function not-defined (-> Atom Atom))
    ; Returns (@doc-formal (@item not-defined) (@kind function) (@type (-> Atom Atom)) (@desc "No documentation"))

``get-doc-atom``
-------------------

**Description:** Function used by get-doc-single-atom to get documentation on an atom.

**Parameters:**
    - Atom: The name of the atom to get documentation for.

**Return:** Documentation on the atom in DocFormal format.

**Example:**

.. code-block:: metta

    !(get-doc-atom true)
    ; Returns (@doc-formal (@item True) (@kind atom) (@type Bool) (@desc "No documentation")) as there is not description provided for Bool type

    !(get-doc-atom unified-atom)
    ; Returns (@doc-formal (@item unified-atom) (@kind atom) (@type %Undefined%) (@desc "No documentation")). As this atom is not defined, its type is Undefined

``undefined-doc-function-type``
-------------------

**Description:** Function used by get-doc-single-atom in case of undefined type for function.

**Parameters:**
    - Expression: List of parameters for the function we want to get documentation for.

**Return:** List of %Undefined% number of which depends on input list size. So for two parameters function will return (%Undefined% %Undefined% %Undefined%), the last one is for the return type.

**Example:**

.. code-block:: metta

    !(undefined-doc-function-type (Atom Atom Atom))
    ; Returns (%Undefined% %Undefined% %Undefined% %Undefined%)

``get-doc-params``
-------------------

**Description:** Function used by get-doc-function to convert the DocInformal format, e.g (@param "Atom to be evaluated") to DocFormal format, e.g (@param (@type Atom) (@desc "Atom to be evaluated")).

**Parameters:**
    - Expression: List of parameters in form of ((@param Description) (@param Description)...).
    - Atom: Return value's description in form of (@return Description).
    - Expression: Type notation without '->' starting symbol e.g. (Atom Atom Atom)

**Return:** United list of params and return value each augmented with its type in DocFormal format. 

**Example:**

.. code-block:: metta

    !(get-doc-params ((@param "Atom to be evaluated") (@param "Atom to be evaluated"))(@return "Atom to be evaluated") (Atom Atom Atom))
    ; Returns (((@param (@type Atom) (@desc "Atom to be evaluated")) (@param (@type Atom) (@desc "Atom to be evaluated"))) (@return (@type Atom) (@desc "Atom to be evaluated")))

``help!``
-------------------

**Description:** Function prints documentation for the input atom. Without parameters prints the list of the stdlib functions.

**Parameters:**
    - Atom: The name of the atom to get documentation for.

**Return:** Unit atom.

**Example:**

.. code-block:: metta

    !(help! or)
    ; prints: 
    ; Function or: (-> Bool Bool Bool) Logical disjunction of two arguments
    ; Parameters:
    ; (type Bool) First argument
    ; (type Bool) Second argument
    ; Return: (type Bool) True if any of input arguments is True, False - otherwise


    ; Then it returns: ()

``help-param!``
-------------------

**Description:** Function used by function help! to output parameters using println!.

**Parameters:**
    - Atom: Parameters list.

**Return:** Unit atom.

**Example:**

.. code-block:: metta

    !(help-param! ((@param (@type Bool) (@desc "First argument")) (@param (@type Bool) (@desc "Second argument"))))
    ; Prints: (type Bool) First argument 
    ; (type Bool) Second argument
    ; Then it returns: ()
