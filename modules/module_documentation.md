
There are different types of modules:

### Limitations
1. Modules whose name come early in alphabetical order are loaded first.

### Information
1. Providers - they act as a base system for a set of other modules to function. For example,
    text_provider creates an editor, and basic text tools. All text related modules will require
    text_provider to perform their text-related functions.
    In short, it is like a stage for other modules to perform their functions.
2. Tools - they are the modules that perform the actual functions. For example, text_provider
    creates an editor, and basic text tools. All text related modules will require text_provider
    to perform their text-related functions. - These tools could include text generators, text
    translators, code editors, etc.