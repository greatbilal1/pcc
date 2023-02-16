\# Chapter 11: Debugging

This chapter covers debugging in Python. It covers the following topics:

-   Common errors and exceptions
-   Using the [pdb]{.title-ref} library
-   Setting breakpoints
-   Stepping through code
-   Using the [logging]{.title-ref} module
-   Debugging with [print()]{.title-ref} statements
-   Using the [assert]{.title-ref} statement

Examples are provided throughout the chapter to help you understand and
apply the concepts covered. By the end of the chapter, you will have a
solid understanding of how to debug Python code and be ready to move on
to more advanced topics.

\## Summary In this chapter, you learned to write tests for functions
and classes using tools in the pytest module. You learned to write test
functions that verify specific behaviors your functions and classes
should exhibit. You saw how fixtures can be used to efficiently create
resources that can be used in mul-tiple test functions in a test
file.Testing is an important topic that many newer programmers aren't
exposed to. You don't have to write tests for all the simple projects
you try as a new programmer. But as soon as you start to work on
projects that involve significant development effort, you should test
the critical behaviors of your functions and classes. You'll be more
confident that new work on your project won't break the parts that work,
and this will give you the free-dom to make improvements to your code.
If you accidentally break existing functionality, you'll know right
away, so you can still fix the problem easily. Responding to a failed
test that you ran is much easier than responding to a bug report from an
unhappy user.Other programmers will respect your projects more if you
include some initial tests. They'll feel more comfortable experimenting
with your code and be more willing to work with you on projects. If you
want to contribute to a project that other programmers are working on,
you'll be expected to show that your code passes existing tests and
you'll usually be expected to write tests for any new behavior you
introduce to the project.Play around with tests to become familiar with
the process of testing your code. Write tests for the most critical
behaviors of your functions and classes, but don't aim for full coverage
in early projects unless you have a specific reason to do so.
