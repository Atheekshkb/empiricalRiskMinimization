#!/usr/bin/env python3

"""
Do a local practice grading.
The score you recieve here is not an actual score,
but gives you an idea on how prepared you are to submit to the autograder.
"""

import os
import sys

import numpy

import autograder.assignment
import autograder.question
import autograder.style

class HO2(autograder.assignment.Assignment):
    def __init__(self, **kwargs):
        super().__init__(name = 'Practice Grading for Hands-On 2',
            questions = [
                T1A(1, "Task 1.A (threshold_hypothesis)"),
                T1B(1, "Task 1.B (zero_one_loss)"),
                T2A(1, "Task 2.A (expected_loss)"),
                T2B(1, "Task 2.B (index_of_minimum)"),
                T3A(4, "Task 3.A (fractions)"),
                T3B(4, "Task 3.B (rates)"),
                autograder.style.Style(kwargs.get('input_dir'), max_points = 1),
            ], **kwargs)

class T1A(autograder.question.Question):
    def score_question(self, submission):
        result = submission.__all__.threshold_hypothesis(0, 0)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, bool)):
            self.fail("Function must return a boolean value.")
            return

        self.full_credit()

class T1B(autograder.question.Question):
    def score_question(self, submission):
        result = submission.__all__.zero_one_loss(0, True, true_hypothesis, 0)
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (int, numpy.integer))):
            self.fail("Answer must be an integer.")
            return

        self.full_credit()

class T2A(autograder.question.Question):
    def score_question(self, submission):
        result = submission.__all__.expected_loss([0] * 4, [True] * 4,
                submission.__all__.zero_one_loss, true_hypothesis, 0)

        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (float, numpy.float64, numpy.float32))):
            self.fail("Answer must be a float.")
            return

        self.full_credit()

class T2B(autograder.question.Question):
    def score_question(self, submission):
        result = submission.__all__.index_of_minimum([1, 2, 3])
        if (self.check_not_implemented(result)):
            return

        if (not isinstance(result, (int, numpy.integer))):
            self.fail("Answer must be an integer.")
            return

        self.full_credit()

class T3A(autograder.question.Question):
    def score_question(self, submission):
        function_names = [
            'true_positive_fraction',
            'false_positive_fraction',
            'true_negative_fraction',
            'false_negative_fraction',
        ]

        for name in function_names:
            function = getattr(submission.__all__, name)
            result = function([0], [True], true_hypothesis, 0)

            if (isinstance(result, type(NotImplemented))):
                self.add_message("%s() not implemented." % (name))
                continue

            if (not isinstance(result, (float, numpy.float64, numpy.float32))):
                self.add_message("%s() must return a float.")
                continue

            self.add_score(1)

class T3B(autograder.question.Question):
    def score_question(self, submission):
        function_names = [
            'true_positive_rate',
            'false_positive_rate',
            'true_negative_rate',
            'false_negative_rate',
        ]

        for name in function_names:
            function = getattr(submission.__all__, name)
            result = function([0], [True], true_hypothesis, 0)

            if (isinstance(result, type(NotImplemented))):
                self.add_message("%s() not implemented." % (name))
                continue

            if (not isinstance(result, (float, numpy.float64, numpy.float32))):
                self.add_message("%s() must return a float.")
                continue

            self.add_score(1)

def true_hypothesis(feature, theta):
    return True

def main(path):
    assignment = HO2(input_dir = path)
    result = assignment.grade()
    print(result.report())

def _load_args(args):
    exe = args.pop(0)
    if (len(args) != 1 or ({'h', 'help'} & {arg.lower().strip().replace('-', '') for arg in args})):
        print("USAGE: python3 %s <submission path (.py or .ipynb)>" % (exe), file = sys.stderr)
        sys.exit(1)

    path = os.path.abspath(args.pop(0))

    return path

if (__name__ == '__main__'):
    main(_load_args(list(sys.argv)))
