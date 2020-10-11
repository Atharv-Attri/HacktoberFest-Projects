# Introduction
Beam Deflection Calculator is a simple program designed to calculate and plot the deflection of a beam using Euler–Bernoulli beam theory. Structural/mechanical engineers or students might find this useful. 

# Features
The program can currently calculate and plot the deflection of a single fixed end beam with a single point load.

# Requirements
Python is required to run the program. The following libraries are required:
- NumPy
- Matplotlib

# Usage Instructions
Run the script using Python.

For a single fixed end beam with a single point load, the user has to input the following:
- Point load **F**, in N
- Length of beam **L**, in m
- Distance of point load from support **a**, in m
- Young's modulus of beam **E**, in GPa
- Second moment of area **I**, in mm⁴
- Location on the beam **x**, in m

The following diagram illustrates some of the above variables.
<pre>
|                        F
|                        |
|                       \|/
|---------------------------------
| x-->
|<----------a----------->
|<---------------L--------------->
|
|
</pre>

# Future Work
Other beam support and loading configurations may be considered for future work.
