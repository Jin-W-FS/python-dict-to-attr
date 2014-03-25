python-dict-to-attr
===================

recursively wraps any object["NAME"] into object.NAME, as the JavaScript objects do

Mainly for transfering objects building from JSON strings.

In addition, this module offers a relatively looser way for loading JSON strings (directly eval() them in python), which may be used as a simple JSON loader without much format checkings.
