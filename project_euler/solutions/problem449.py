from math import pi, sqrt


def get_answer(a=3, b=1):
    """
    This question is made tricky because the surrounding chocolate covering is not an ellipsoid
    and (I believe) cannot be represented in closed form.
    What I did was let y = 0, and x >= 0, giving me an ellipse in the x-z plane.
    I then parameterized the ellipse, and using the normal vector, calculated various points
    on the edge of the new chocolate covering curve.
    Using a solid of revolution, I was then able to calculate the volume
    of the chocolate coating minus the candy.
    """
    area = 0
    h = 0.000001
    x0 = -b - 1
    y0 = 0
    xelip = -b + h
    yelip = a / b * sqrt(b * b - xelip * xelip)
    while xelip < 0 + h/2:
        nx, ny = get_normal(b, a, xelip)
        x1 = xelip + nx
        y1 = yelip + ny
        area += trap_individual_sum(x1 - x0, pow(y1, 2), pow(y0, 2))
        x0 = x1
        y0 = y1
        xelip += h
        yelip = a / b * sqrt(b * b - xelip * xelip)
    return str(round(pi * 2 * area - area_of_revolution_eclipse(b, a), 8))


def get_normal(a, b, x):
    """
    This gives the negative normal vector N-hat.
    Letting r(x) = <x, b/a sqrt(a^2 - x^2)>,
    then T-hat = r'/|r'|, and N-hat = T' / |T'|.

    """
    bsq = b * b
    asq = a * a
    xsq = x * x
    nx = (- bsq * x) / \
        (pow(xsq - asq, 2) * pow((bsq * xsq)/(asq * (asq - xsq)) + 1, 3 / 2))
    ny = (- a * b) / \
         (pow(asq - xsq, 3 / 2) * pow((bsq * xsq) / (asq * (asq - xsq)) + 1, 3 / 2))
    nx, ny = nx / sqrt(nx * nx + ny * ny), ny / sqrt(nx * nx + ny * ny)
    return -nx, -ny


def area_of_revolution_eclipse(a, b):
    return (4 / 3) * pi * a * pow(b, 2)


def trap_individual_sum(h, b1, b2):
    """
    An individual sum using the trapezoid rule.
    The midpoint rule (or simpsons rule) cannot easily be used because the step size is different
    every time.
    """
    return 1/2 * h * (b1 + b2)
