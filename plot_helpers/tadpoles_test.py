import math
from .tadpoles import tail_endpoint

def test_fig_x_width_less_than_fig_y_width():
    # Figure sizes
    fig_x_width = 10
    fig_y_width = 20
    ylim_max = 10
    xlim_max = 10

    # Select a default depth and dip
    depth = 5
    dip = 5

    # Set the tail lenght such that at 45 degrees we can span 1 x and 1 y unit
    tail_length = math.sqrt(2) / 10.0

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 0,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 5)
    assert math.isclose(y_value, 5 - math.sqrt(2))
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 45,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 7)
    assert math.isclose(y_value, 4)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 90,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 5)
    assert math.isclose(y_value, 5 - math.sqrt(2))
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 135,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 7)
    assert math.isclose(y_value, 6)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 180,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 5)
    assert math.isclose(y_value, 5 - math.sqrt(2))
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 225,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 3)
    assert math.isclose(y_value, 6)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 2700,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 5)
    assert math.isclose(y_value, 5 - math.sqrt(2))
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 315,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 3)
    assert math.isclose(y_value, 4)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

def test_fig_x_width_greater_than_fig_y_width():
    # Figure sizes
    fig_x_width = 20
    fig_y_width = 10
    ylim_max = 10
    xlim_max = 10

    # Select a default depth and dip
    depth = 5
    dip = 5

    # Set the tail lenght such that at 45 degrees we can span 1 x and 1 y unit
    tail_length = math.sqrt(2) / 10.0

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 0,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 5)
    assert math.isclose(y_value, 5 - math.sqrt(2))
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 45,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 6)
    assert math.isclose(y_value, 3)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 90,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 5)
    assert math.isclose(y_value, 5 - math.sqrt(2))
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 135,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 6)
    assert math.isclose(y_value, 7)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 180,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 5)
    assert math.isclose(y_value, 5 - math.sqrt(2))
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 225,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 4)
    assert math.isclose(y_value, 7)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 270,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 5)
    assert math.isclose(y_value, 5 - math.sqrt(2))
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 315,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 4)
    assert math.isclose(y_value, 3)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

def test_fig_x_width_equal_to_fig_y_width():
    # Figure sizes
    fig_x_width = 10
    fig_y_width = 10
    ylim_max = 10
    xlim_max = 10

    # Select a default depth and dip
    depth = 5
    dip = 5

    # Set the tail lenght such that at 45 degrees we can span 1 x and 1 y unit
    tail_length = math.sqrt(2) / 10.0

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 0,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 5)
    assert math.isclose(y_value, 5 - math.sqrt(2))
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 45,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 6)
    assert math.isclose(y_value, 4)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 90,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 5 + math.sqrt(2))
    assert math.isclose(y_value, 5)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 135,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 6)
    assert math.isclose(y_value, 6)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 180,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 5)
    assert math.isclose(y_value, 5 + math.sqrt(2))
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 225,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 4)
    assert math.isclose(y_value, 6)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 270,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 5 - math.sqrt(2))
    assert math.isclose(y_value, 5)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))

    x_value, y_value = tail_endpoint(
        depth = depth,
        dipaz = 315,
        dip = dip,
        tail_length = tail_length,
        fig_x_width = fig_x_width,
        fig_y_width = fig_y_width,
        ylim_max = ylim_max,
        xlim_max = xlim_max)
    assert math.isclose(x_value, 4)
    assert math.isclose(y_value, 4)
    assert math.isclose(math.sqrt(math.pow(dip - x_value, 2) + math.pow(depth - y_value, 2)), math.sqrt(2))
