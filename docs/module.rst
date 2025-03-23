Module Management
=============================

``register-module!``
---------------

**Description:** Take a file path to module and load the module in to the runner``.

**Parameters:**
    - StringAtom: The path to the module to be loaded

**Return:** A unit atom ().

**Example:**

.. code-block:: metta

    (register-module! /path/to/module); Returns ()

``mod-space!``
----------------

**Description:** Used to get the atomspace where the given module loaded to and tries to load the module if it is not loaded into the module system.

**Parameters:**
    - StringAtom: The name of the module.

**Return:** The space where the module is uploaded.

**Example:**

.. code-block:: metta

    !(mod-space! module) ; Returns <spacename>:module

``print-mods!``
----------------

**Description:** Prints all modules with their correspondent spaces.

**Parameters:**
    - None

**Return:** unit atom.

**Example:**

.. code-block:: metta

    !(print-mods!) 
    ; Returns:
    ;top = 0
        ;├─stdlib = 2
        ;├─corelib = 1
        ;└─catalog = 3

``import!``
---------------

**Description:** Imports module using its relative path (second argument) and binds it to the token (first argument) which will represent imported atomspace. If first argument is &self then everything will be imported to current atomspace.

**Parameters:**
    - SymbolAtom: Symbol, which is turned into the token for accessing the imported module.
    - String: Module relative path (use ':')
**Return:** Unit atom.

**Example:**

.. code-block:: metta

    !(import! helper util:helpers) ; ()

``include``
---------------

**Description:** Import every thing from the given module. The same as import with &self as a first argument.

**Parameters:**
    - String: Name of metta script to import.

**Return:** Unit atom

**Example:**

.. code-block:: metta

    !(include util:helper); Returns (). The same as !(import! &self util:helper)

``bind!``
---------------

**Description:** Associate a token with a symbol(the first argument) after reducting an atom(the second argument).

**Parameters:**
    - SymbolAtom: A symbol to be used as a token name.
    - Atom: An atom whose token is be associated with a symbol.

**Return:** Unit atom

**Example:**

.. code-block:: metta

    !(bind! mySpace (new-space)); Returns (). We can access the new space using mySpace from now on.
