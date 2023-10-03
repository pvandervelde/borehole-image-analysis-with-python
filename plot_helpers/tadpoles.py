
import math

def tail_endpoints(depths, dipazs, dips, tail_length, fig_x_width, fig_y_width, ylim_max, xlim_max):
    """
    Calculate and return the x and y coordinates for the tadpole tail endpoints.

    Parameters:
    - depths (list or array): List of depths for each data point.
    - dipazs (list or array): List of dip azimuths for each data point.
    - dips (list or array): List of dip angles for each data point.
    - tail_length (float): The length of the tail as a decimal percentage of the axis scale.
    - fig_x_width (float): Width of the figure in inches.
    - fig_y_width (float): Height of the figure in inches.
    - ylim_max (float): Maximum depth of the plot.
    - xlim_max (float): Maximum dip of the plot.

    Returns:
    - tuple: A tuple containing two lists, the first with x coordinates of tail endpoints
             and the second with y coordinates of tail endpoints.

    Notes:
    - fig_x_width and fig_y_width are the values passed in when making the figure (fig_size=(x,y))
      and these widths determine the aspect ratio of the plot (n pixels in each direction).
    - fig_ratio is a multiplier on y or x axis tail length depending on which plot axis has more pixels
    """
    tail_endpoints_y = []
    tail_endpoints_x = []

    for depth, dipaz, dip in zip(depths, dipazs, dips):

        x_value, y_value = tail_endpoint(depth, dipaz, dip, tail_length, fig_x_width, fig_y_width, ylim_max, xlim_max)
        tail_endpoints_y.append(y_value)
        tail_endpoints_x.append(x_value)

    return tail_endpoints_x, tail_endpoints_y

def tail_endpoint(depth: float, dipaz: float, dip: float, tail_length: float, fig_x_width: float, fig_y_width: float, ylim_max: float, xlim_max: float):
    x_value = 0
    y_value = 0

    if fig_x_width < fig_y_width:
        fig_ratio = fig_y_width / fig_x_width # this is the ratio of y to x inches (pixels)
        y_value = depth - (ylim_max * tail_length) * math.cos(math.radians(dipaz))
        x_value = dip + (xlim_max * tail_length * fig_ratio) * math.sin(math.radians(dipaz))
    else:
        fig_ratio = fig_x_width / fig_y_width
        y_value = depth - (ylim_max * tail_length * fig_ratio) * math.cos(math.radians(dipaz))
        x_value = dip + (xlim_max * tail_length) * math.sin(math.radians(dipaz))

    return x_value, y_value
