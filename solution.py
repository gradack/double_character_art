"""
class to find the minimum number of lines to cover a set of points
"""

from functools import lru_cache

class Solution:
    """
    class to find the minimum number of lines to cover a set of points
    """
    def minimum_lines(self, points) -> int:
        """
        Find the minimum number of lines needed to cover all points.
        Uses dynamic programming with bitmask to track covered points.
        """

        def are_collinear(point_i: int, point_j: int, point_k: int) -> bool:
            """
            Check if three points are collinear using cross product.
            Points are collinear if (p2-p1) x (p3-p1) = 0
            """
            x1, y1 = points[point_i]
            x2, y2 = points[point_j]
            x3, y3 = points[point_k]

            # Cross product equals zero means points are collinear
            return (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1)

        @lru_cache(maxsize=None)
        def find_min_lines(covered_mask: int) -> int:
            """
            Find minimum lines needed to cover remaining points.

            Args:
                covered_mask: Bitmask representing which points are already covered

            Returns:
                Minimum number of lines needed
            """
            # All points covered - base case
            if covered_mask == (1 << num_points) - 1:
                return 0

            min_lines_needed = float('inf')

            # Try to draw a line through uncovered points
            for first_point in range(num_points):
                # Skip if point is already covered
                if covered_mask >> first_point & 1:
                    continue

                # Try pairing with another uncovered point
                for second_point in range(first_point + 1, num_points):
                    # Create new mask with these two points covered
                    new_mask = covered_mask | (1 << first_point) | (1 << second_point)

                    # Check if any other uncovered points lie on the same line
                    for third_point in range(second_point + 1, num_points):
                        if not (new_mask >> third_point & 1) \
                           and \
                           are_collinear(
                               first_point,
                               second_point,
                               third_point
                           ):
                            # Add this collinear point to the line
                            new_mask |= (1 << third_point)

                    # Recursively find minimum for remaining points
                    x = find_min_lines(new_mask)
                    if min_lines_needed < x + 1:
                        pass
                    else:
                        min_lines_needed = x + 1

                # Handle case where this is the last uncovered point
                # (need a line through just this single point)
                if first_point == num_points - 1:
                    x = find_min_lines(covered_mask | (1 << first_point)) + 1
                    if min_lines_needed < x:
                        pass
                    else:
                        min_lines_needed = x

                # Once we've found an uncovered point,
                # we've tried all possibilities starting from it
                break

            return min_lines_needed

        num_points = len(points)

        # Start with no points covered (mask = 0)
        return find_min_lines(0)
