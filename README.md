# Simulated annealing for the traveling salesman problem

Centrale Lille | [Anas ESSOUNAINI](https://www.linkedin.com/in/anas-essounaini-b7514014a/) |  [Ali MOURTADA](https://www.linkedin.com/in/ali-mourtada-57714214a/)

## 📝 Table of Contents

- [Description](#about)
- [Repository structure](#getting_started)
- [Authors](#usage)


## 🧐 Description <a name = "about"></a>


This project will be focused on the implementation of a basic simulated annealing algorithm to minimize a function <a href="https://www.codecogs.com/eqnedit.php?latex=f&space;:&space;E&space;\subset&space;\mathbb{N}&space;\rightarrow&space;\mathbb{R}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f&space;:&space;E&space;\subset&space;\mathbb{N}&space;\rightarrow&space;\mathbb{R}" title="f : E \subset \mathbb{N} \rightarrow \mathbb{R}" /></a>, where <a href="https://www.codecogs.com/eqnedit.php?latex=E" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E" title="E" /></a> is finite. An application to the *traveling salesman* problem will then be considered to test the algorithm implementation. 

In general, a simulated annealing algorithm can be described as follows.

---
**Simulated annealing**

Set <a href="https://www.codecogs.com/eqnedit.php?latex=x_0&space;\in&space;E" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_0&space;\in&space;E" title="x_0 \in E" /></a>, <a href="https://www.codecogs.com/eqnedit.php?latex=T_0&space;>&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_0&space;>&space;0" title="T_0 > 0" /></a>. 

<a href="https://www.codecogs.com/eqnedit.php?latex=n&space;\leftarrow&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n&space;\leftarrow&space;0" title="n \leftarrow 0" /></a>

While <a href="https://www.codecogs.com/eqnedit.php?latex=(n&space;\leq&space;N)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(n&space;\leq&space;N)" title="(n \leq N)" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=(T_n&space;>&space;T_{\min})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?(T_n&space;>&space;T_{\min})" title="(T_n > T_{\min})" /></a>

  1. Draw a point <a href="https://www.codecogs.com/eqnedit.php?latex=y&space;\sim&space;Q(x_n,&space;\cdot)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y&space;\sim&space;Q(x_n,&space;\cdot)" title="y \sim Q(x_n, \cdot)" /></a> in the neighborhood of <a href="https://www.codecogs.com/eqnedit.php?latex=x_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_n" title="x_n" /></a>, and <a href="https://www.codecogs.com/eqnedit.php?latex=u&space;\sim&space;\mathcal{U}([0,1])" target="_blank"><img src="https://latex.codecogs.com/gif.latex?u&space;\sim&space;\mathcal{U}([0,1])" title="u \sim \mathcal{U}([0,1])" /></a> (where<a href="https://www.codecogs.com/eqnedit.php?latex=\mathcal{U}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\mathcal{U}" title="\mathcal{U}" /></a> is the uniform distribution)
  
  2. Compute the acceptance probability: 

<a href="https://www.codecogs.com/eqnedit.php?latex=p(f(x_n),&space;f(y),&space;T_n)&space;=&space;\begin{cases}&space;1&space;&&space;\text{if&space;}&space;f(y)&space;<&space;f(x_n)&space;\\&space;\text{e}^{-(f(y)&space;-&space;f(x_n))/T_n}&space;&&space;\text{otherwise.}&space;\end{cases}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p(f(x_n),&space;f(y),&space;T_n)&space;=&space;\begin{cases}&space;1&space;&&space;\text{if&space;}&space;f(y)&space;<&space;f(x_n)&space;\\&space;\text{e}^{-(f(y)&space;-&space;f(x_n))/T_n}&space;&&space;\text{otherwise.}&space;\end{cases}" title="p(f(x_n), f(y), T_n) = \begin{cases} 1 & \text{if } f(y) < f(x_n) \\ \text{e}^{-(f(y) - f(x_n))/T_n} & \text{otherwise.} \end{cases}" /></a>
  
  3. Set <a href="https://www.codecogs.com/eqnedit.php?latex=x_{n&plus;1}&space;=&space;\begin{cases}&space;y&space;&&space;\text{if&space;}&space;u&space;\leq&space;p(f(x_n),&space;f(y),&space;T_n)&space;\\&space;x_n&space;&&space;\text{otherwise.}&space;\end{cases}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{n&plus;1}&space;=&space;\begin{cases}&space;y&space;&&space;\text{if&space;}&space;u&space;\leq&space;p(f(x_n),&space;f(y),&space;T_n)&space;\\&space;x_n&space;&&space;\text{otherwise.}&space;\end{cases}" title="x_{n+1} = \begin{cases} y & \text{if } u \leq p(f(x_n), f(y), T_n) \\ x_n & \text{otherwise.} \end{cases}" /></a>
  4. Set <a href="https://www.codecogs.com/eqnedit.php?latex=T_{n&plus;1}&space;=&space;\frac{T_0}{\log(n&plus;2)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?T_{n&plus;1}&space;=&space;\frac{T_0}{\log(n&plus;2)}" title="T_{n+1} = \frac{T_0}{\log(n+2)}" /></a>
  5. <a href="https://www.codecogs.com/eqnedit.php?latex=n&space;\leftarrow&space;n&plus;1" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n&space;\leftarrow&space;n&plus;1" title="n \leftarrow n+1" /></a>

Return <a href="https://www.codecogs.com/eqnedit.php?latex=x_N" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_N" title="x_N" /></a>, <a href="https://www.codecogs.com/eqnedit.php?latex=\bigl(&space;f(x_n)&space;\bigr)_{1&space;\leq&space;n&space;\leq&space;N}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\bigl(&space;f(x_n)&space;\bigr)_{1&space;\leq&space;n&space;\leq&space;N}" title="\bigl( f(x_n) \bigr)_{1 \leq n \leq N}" /></a>

> *Note*: in practice, the transition kernel <a href="https://www.codecogs.com/eqnedit.php?latex=Q" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Q" title="Q" /></a>, the neighborhood of the current point <a href="https://www.codecogs.com/eqnedit.php?latex=x_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_n" title="x_n" /></a> needs to be defined by the user, depending on the problem of interest. The definition of the other elements will be specified later for the *traveling salesman* problem.

## 🎥 Repository structure <a name = "getting_started"></a>

This repository consists in several directories with specific purposes:

- `travelling_salesman_pkg`: This directory contains the `travelling_salesman_pkg` Python Library developed exclusively for this project. It contains functions used within the scripts. To install the library, navigates to the project directory and run the following `pip` command:
  ```Shell
  cd [path_to_project_directory]
  pip install -e .
  ```
- `main.py`: test of `travelling_salesman_pkg` Library to determine the __shortest path between 16 moroccan cities__.

***
For any information, feedback or questions, please [contact us][anas-email]

















[anas-email]: mailto:essounaini97@gmail.com
[ali-email]: mailto:mourtada.ali1997@gmail.com 


