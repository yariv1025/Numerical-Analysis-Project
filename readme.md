![alt text](https://i.imgur.com/ZNpFSo2.png)

# User-Guide : Numerical-Analysis-Project

This project will allow the user to approximate roots of functions using several methods and to approximate results of matrix.
All roots approxmiates methods will be backup with graphs.
#### Roots approximation methods:
1. The Bisection method.
2. Newton raphson method
3. Secant method.

#### Approximation methods:
1. Poly aprox
2. Linear aprox
3. LaGrange
4. Neville
5. Cubic Spline

#### Matrix approximation methods:
1. Gauss Siedle
2. Gauss elimination
3. Jacobi
4. SOR - Successive Over Relaxation

#### Integrals approximation methods:
1. Romberg
2. Simpson
3. Trapezoid
4. Gaussian Quadrature

## Getting Started
#### Prerequisites

A work environment that supports Python3, like Pycharm, VS code etc.
_____________________

A quick introduction of the minimal setup you need to get a "Numerical-Analysis-Project" up & running.
Open folder for this project and clone this repository use follow command:
```
git@github.com:yariv1025/Numerical-Analysis-Project.git
```
After Python installion, open cmd / Terminal and navigate to project folder and run the follow command:
```
python pip install -r install.txt
```

Project Structure
------------------
The tree below displays the files and folders structure:
```
├── Docs                            # Documents of project:
|  |── Diagrams                     # Contain all relevant DFD's
|  ├── Summery                      # Short summery of the methods
|  └── Final summery                # Hackathon - final summery  
├── Lib                             # All methods files - Python
|   ├── Bisection_method.py
|   ├── GaussSiedle_SOR.py
|   ├── NewtonRephson_method
|   ├── plot_it.py
|   ├── Hackathon.py                # Unnecessary
|   ├── Poly_aprox.py
|   ├── Linear aprox.py
|   ├── CubicSpline_method.py
|   ├── LaGrange_method.py          #Unnecessary
|   ├── Lagrange
|   ├── Neville_method.py
|   ├── Romberg_method.py
|   ├── Simpson_method.py
|   ├── Trapezoid_method.py
|   ├── Gauss elimination.py
|   ├── Jacobi.py
|   ├── Main.py
|   ├── Gaussian Quadrature.py
|   └── Secant_method.py
├── readme.md                       # User guide
├── install.txt                     # text file for installation
└── .gitignore                      # Files we ignored

```
Built With
----------
* [Pycharm](https://www.jetbrains.com/pycharm/) -Python IDE.
* [Scipy, Sympy, Numpy, Matplotlib](https://www.scipy.org/) -Python-based ecosystem software for mathematics, science, and engineering.

Authors
-------
Students in the software engineering department at SCE - Sami Shamoon College:
* [Alon Gabay](https://github.com/alongabay)
* [Yariv Garala](https://github.com/yariv1025)
* [Almog Machlof](https://github.com/Almogma)
* [Elad Metudi]()
* [Tom Zeiger]()

See also the list of [contributors](https://github.com/yariv1025/Numerical_Analysis_Project/graphs/contributors) who participated in this project

License
-------
This project is licensed under the SCE License - see the [License.md](https://gist.github.com/Numerical_Analysis_Project/LICENSE.md) file for  details.

Acknowledgments
---------------
* [matplotlib](https://matplotlib.org/gallery/lines_bars_and_markers/simple_plot.html) - We used matplotlib code to export a graph for given function.
## END
