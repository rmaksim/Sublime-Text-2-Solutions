inc_dec_number.py
=======================================

Increase/Decrease number by delta_value
Support Multiple Selections

![blame screenshot](https://github.com/rmaksim/Sublime-Text-2-Solutions/raw/master/inc_dec_number.gif)


Example of the correct values:
------------------------------

    * positive and negative numbers

    ... -2, -1, 0, 1, 2, ...

    * positive and negative numbers and any text after them

    12px, -5em, 100%, 42sometext, (24), [12, -13], {77: -88}


Not supported:
--------------

    * numbers in the text and after
    qwe42asd, text42


Default (Linux).sublime-keymap
--------------------------------------------------------------------------------

    [
        { "keys": ["alt+up"],  "command": "inc_dec_number", "args": { "delta": 1} },
        { "keys": ["alt+down"], "command": "inc_dec_number", "args": { "delta": -1} },
        { "keys": ["super+up"],  "command": "inc_dec_number", "args": { "delta": 10} },
        { "keys": ["super+down"], "command": "inc_dec_number", "args": { "delta": -10} }
    ]