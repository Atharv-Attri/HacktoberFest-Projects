import random

def make_triangle(triangle_height, offset = 0, tree_cutoff = 0, triangle_background = ' ', triangle_fill = '*'):
    """
        triangle_height: how many rows the triangle will have.
        offset: how many spaces (or background fill) the triangle will have.
        triangle_cutoff: how many rows to delete from the top of the triangle. Useful when making a tree. 
        triangle_background: what character to fill the background with
        triangle_fill: what character to fill the tree with.
    """
    triangle_width = triangle_height * 2 - 1
    filler_padding = lambda i: (triangle_background * ((triangle_width - i)/2)) + triangle_background * offset

    triangle = [filler_padding(i) +  (triangle_fill * i) for i in range(1, triangle_width, 2)]
    triangle = [x for x in triangle if x.strip()]

    triangle = triangle[tree_cutoff:]
    return triangle


def make_tree(triangle_segments, trunk_segment, tree_background = ' ', tree_fill = '*'):
    """
        triangle_segments: should look like this - [[triangle_height, triangle_cutoff], [triangle_height, triangle_cutoff], ...]
        trunk_segment: a list (or tuple) with the trunk width and height. Width should be an odd number. 
        tree_background:  what character to fill the background with.
        tree_fill: what character to fill the tree with.
    """
    height_to_width = lambda h: (h * 2) - 1

    max_width = height_to_width(max([x[0] for x in triangle_segments]))

    tree = []
    for segment in triangle_segments: 
        tree += make_triangle(segment[0], offset = (max_width - height_to_width(segment[0])) / 2, tree_cutoff = segment[1], triangle_background = tree_background, triangle_fill = tree_fill)

    tree += [tree_background * ((max_width - trunk_segment[0]) / 2) + tree_fill * trunk_segment[0] + tree_background * (max_width / 2) for _ in range(trunk_segment[1])]
    return tree


def make_random_tree(segments_range = [1, 7], segment_height_range = [4, 10], trunk_height_range = [2, 5]):
    """
        segments_range: chooses a random number of segments between these values
        segment_height_range: for each segment, choose a random height between these values
        trunk_height_range: choose how long the trunk is randomly between these values
    """
    number_of_segments = random.randint(*segments_range)
    segments = [random.randint(*segment_height_range) for _ in range(number_of_segments)]
    segments = [[x, random.randint(1, x/2)] for x in segments]
    segments[0][1] = 0

    trunk_segment = [random.randint(2, segments[-1][0] - 1), random.randint(*trunk_height_range)]
    trunk_segment[0] += (1 - trunk_segment[0] % 2)

    tree = make_tree(segments, trunk_segment)
    return tree

if __name__ == '__main__' : 
    print ('\n'.join(make_random_tree()))
