#!/usr/bin/python3

"""
Lets define a function: tokenizer in this module
"""
import re
import shlex


def tokenizer(line):
    """
    Function: tokenizer

    Arguments: input line, line
    """

    # Let us perform a serach operation on input line
    # based on a regular expression.

    # the variable curly_braces contains the result of a search operation
    # based on a patticular pattern; "{..}"
    curly_braces = re.search(r"\{(.*?)\}", line)

    # lets also search for '[..]'
    brackets = re.search(r"\[(.*?)\]", line)
    # if neither pattern is found, they will both be None

    if curly_braces is None:
        if brackets is None:
            # let us use split to split according to Unix Shell syntax.
            # Then clean the tokens by removing trailing or leading commas

            return [token.strip(",") for token in shlex.split(line)]
        else:
            # if '[]' is found
            # brackets.span()[0] returns the start index of the
            # first match of the square brackets in line

            # arg[:brackets.span()[0]]
            # then we slice line to extract the substring before the []

            args = shlex.split(line[:brackets.span()[0]])

            # then iterate over each arg in args and
            # remove trailing/leading whitespaces
            arg_list = [arg.strip(",") for arg in args]

            # then we append the square brackets and their contents to arg_list
            # brackets.group() is the entire matched
            # substring found by the regular expression pattern.
            arg_list.append(brackets.group())

            return arg_list
    else:
        # if "{}" is found
        args = shlex.split(line[:curly_braces.span()[0]])

        arg_list = [arg.strip(",") for arg in args]

        arg_list.append(curly_braces.group())

        return arg_list
