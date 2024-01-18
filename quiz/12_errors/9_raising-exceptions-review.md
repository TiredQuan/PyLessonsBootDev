# RAISING EXCEPTIONS REVIEW

As you've noticed, there are many kinds of exceptions. Many specific exceptions are built into the language like IndexError and ZeroDivisionError, and (almost) all Exceptions count as the parent Exception type.

If you're interested in the official documentation on all the built-in exceptions you can find a list here.

REFER TO THE FOLLOWING CODE FOR THE QUESTION
`try:
    raise Exception('zero division')
except ZeroDivisionError as e:
    print("zero")
except Exception as e:
    print("other")`
