"""
Define a represention for a grammar of the given language along with an
interpreter that uses the representation to interpret sentences in the
language.
"""

import abc


class AbstractExpression(metaclass=abc.ABCMeta):
    """
    Declare an abstract Interpret operation that is common to all nodes
    in the abstract syntax tree.
    """

    @abc.abstractmethod
    def interpret(self):
        pass

