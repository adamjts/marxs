from __future__ import division

import numpy as np


def get_color(d):
    '''Look for color information in dictionary.

    If missing, return white.
    This function checks if the `d['color']` is a valid RGB tuple and if
    not it imports a `matplotlib.colors.ColorConverter` to convert any
    matplotlib compatible string to an RGB tuple.

    Parameters
    ----------
    d : dict
        Color information should be present in ``d['color']``.

    Returns
    -------
    color : tuple
        RGB tuple with each element in the range 0..1
    '''
    if 'color' not in d:
        return (1., 1., 1.)
    else:
        c = d['color']
        # check if this is a tuple of three floats n the range 0..1
        # or can be converted to one
        try:
            cout = tuple(c)
            if len(cout) != 3:
                raise TypeError
            for a in cout:
                if not isinstance(a, float) or (a < 0.) or (a > 1.):
                    raise TypeError
            return cout
        except TypeError:
            # It's a hex or string. Let matplotlib deal with that.
            import matplotlib.colors
            return matplotlib.colors.colorConverter.to_rgb(c)


def plane_with_hole(outer, inner):
    '''Triangulation of a plane with an inner hole

    This function constructs a triangulation for a plane with an inner hole, e.g.
    a rectangular plane where an inner circle is cut out.

    Parameters
    ----------
    outer, inner : np.ndarray of shape (n, 3)
        Coordinates in x,y,z of points that define the inner and outer boundary.
        ``outer`` and ``inner`` can have a different number of points,
        but points need to be listed in the same orientation (e.g. clockwise)
        for both and the starting points need to have a similar angle as seen from the
        center (e.g. for a plane with z=0, both ``outer`` and ``inner`` could list
        a point close to the y-axis first.

    Returns
    -------
    xyz : nd.array
        stacked ``outer`` and ``inner``.
    triangles : nd.array
        List of the indices. Each row has the index of three points in ``xyz``.

    Example
    -------
    In this example, we make a square and cut out a smaller square in the middle.

    >>> import numpy as np
    >>> from marxs.visualization.utils import plane_with_hole
    >>> outer = np.array([[-1, -1, 1, 1], [-1, 1, 1, -1], [0,0,0,0]]).T
    >>> inner = 0.5 * outer
    >>> xyz, triangles = plane_with_hole(outer, inner)
    >>> triangles
    array([[0, 4, 5],
       [0, 1, 5],
       [1, 5, 6],
       [1, 2, 6],
       [2, 6, 7],
       [2, 3, 7],
       [3, 7, 4],
       [3, 0, 4]])
    '''
    n_out = outer.shape[0]
    n_in = inner.shape[0]
    n = n_out + n_in

    triangles = np.zeros((n, 3), dtype=int)
    xyz = np.vstack([outer, inner])

    i_in = 0
    i_out = 0
    for i in range(n_out + n_in):
        if i/n >= i_in/n_in:
            triangles[i, :] = [i_out, n_out + i_in, n_out + ((i_in + 1) % n_in)]
            i_in += 1
        else:
            triangles[i, :] = [i_out, (i_out + 1) % n_out, n_out + (i_in % n_in)]
            i_out = (i_out + 1) % n_out
    return xyz, triangles
