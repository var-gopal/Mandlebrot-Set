# Mandelbrot Set

"Clouds are not spheres, mountains are not cones, coastlines are not circles, and bark is not smooth, nor does lightening travel in a straight line."

~ Benoit Mandelbrot
## Aim

A fractal is a geometric shape that contains self-similar images within itself - you can zoom in on a section and it will have just as much detail as the whole fractal. Many objects in the natural world exhibit fractal behaviour. For example, the human circulatory system is a fractal. If you look at the blood vessels in your hand, they resemble the overall shape that the complete system takes on. The Mandelbrot set is also an example of a fractal - it is recursively defined and infinitely detailed.

The Mandelbrot Set is a set of complex numbers $C$ resulting from repeated iterations of the following function:

$z_n+1=z^2_n+C$

with the initial condition $z_0=0$.

A given complex number $C$ belongs to the Mandelbrot set if $|z_n|$, the magnitude of $zn$, remains bounded, i.e. does not diverge. If $|z_n|$ diverges then $C$ does not belong to the Mandelbrot set.

In fact, it can be shown that if $|z_n|>2$ for some value of $n$, it will subsequently radidly tend to infinity, i.e. diverge, meaning that $C$ is not in the Mandelbrot set.

You can also assume that if $|z_n|$ has not diverged after $255$ iterations, it will not diverge at larger values of $n$, meaning that $C$ is in the Mandelbrot set.

## Task

Write an object-oriented Python program that will give a visual representation of the Mandelbrot set.

To obtain a visual plot of the Mandelbrot set, the complex plane should be represented as a 2D grid and the value of $N$ (the number of iterations needed to reach the threshold $|z_n|>2$) calculated for complex numbers $C$ corresponding to points on the grid. As explained above, you should set an upper iteration limit of $N=255$.

The value of $N$ should then be converted to a colour and plotted on the grid.

You should explore values of $C$ in the range $x={-2.025 → 0.6}$ and $y={-1.125 → 1.125}$.
 
### How many points to plot?

As you increase the number of points on the grid, you will not only increase the resolution of the display but will also significantly increase the computation time. You should experiment with your code to determine a suitable number of points to plot, but a grid of $512×512$ points will probably give a reasonable balance between the resolution of the display and computation time.