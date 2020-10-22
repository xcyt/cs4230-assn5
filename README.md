# cs4230-assn5

The main program input from a file, and passes three (signed) integers to a function that computes the type of triangle. Besides writing the whole program, your task is to test the function using white box testing techniques.

Have the program prompt for a file name, and read sets of three numbers from the file, reporting on triangle types until the file ends.

You may assume the following:

The file exists
All the inputs are integers. However, they might be negative
The file contains the proper number of entries (a multiple of 3)
The file contains three numbers per line.
Lines that begin with a “#” are comments, and should simply be echoed.
Results are sent to the standard out. (The function does the output.)
For the function that computes the triangle type, do the following:

Draw a flow graph.
Calculate the cyclomatic complexity, and show how you did it.
Generate a set of test cases from the flow graph. 
Turn in the test cases in a file in the above format. The test case file can be used as input to such a program (both yours and mine!) Expected results shall be documented with a comment line before each test case.
