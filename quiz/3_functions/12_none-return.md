# None Return

When no return value is specified in a function, (for example, maybe it's a function that prints some text to the console, but doesn't explicitly return a value) it will automatically return None. The following code snippets all return the same value, None:

`def my_func():
print("I do nothing")
return None
`
`def my_func():
print("I do nothing")
return`
`
def my_func():
print("I do nothing")`

##### What happens if there is no 'return' line in a function?

The program crashes
It returns no value, an attempt to capture a return value will result in errors
Alan Turing rolls over his grave

> It returns None
