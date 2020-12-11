from self_driving.road_polygon import RoadPolygon
from shapely.geometry import  LineString
from scipy.interpolate import splev, splprep
from numpy.ma import arange
from shapely.geometry import LineString

# Constants
rounding_precision = 3
interpolation_distance = 1
smoothness = 0
min_num_nodes = 20


def _interpolate(the_test):
    """
        Interpolate the road points using cubic splines and ensure we handle 4F tuples for compatibility
    """
    old_x_vals = [t[0] for t in the_test]
    old_y_vals = [t[1] for t in the_test]

    # This is an approximation based on whatever input is given
    test_road_lenght = LineString([(t[0], t[1]) for t in the_test]).length
    num_nodes = int(test_road_lenght / interpolation_distance)
    if num_nodes < min_num_nodes:
        num_nodes = min_num_nodes

    assert len(old_x_vals) >= 2, "You need at leas two road points to define a road"
    assert len(old_y_vals) >= 2, "You need at leas two road points to define a road"

    if len(old_x_vals) == 2:
        # With two points the only option is a straight segment
        k = 1
    elif len(old_x_vals) == 3:
        # With three points we use an arc, using linear interpolation will result in invalid road tests
        k = 2
    else:
        # Otheriwse, use cubic splines
        k = 3

    pos_tck, pos_u = splprep([old_x_vals, old_y_vals], s= smoothness, k=k)

    step_size = 1 / num_nodes
    unew = arange(0, 1 + step_size, step_size)

    new_x_vals, new_y_vals = splev(unew, pos_tck)

    # Return the 4-tuple with default z and defatul road width
    return list(zip([round(v, rounding_precision) for v in new_x_vals],
                    [round(v, rounding_precision) for v in new_y_vals],
                    [-28.0 for v in new_x_vals],
                    [8.0 for v in new_x_vals]))


class RoadTest:
    """
        This class represent a test, i.e., the road that the driving agent should follow
    """

    def __init__(self, road_points):
        assert type(road_points) is list, "You must provide a list of road points to create a RoadTest"
        assert all(len(i) == 2 for i in road_points), "Malformed list of road points"
        # The original input
        self.road_points = road_points[:]
        # The interpolated input
        self.interpolated_points = _interpolate(self.road_points)
        # The rendered road
        self.road_polygon = RoadPolygon.from_nodes(self.interpolated_points)

    def get_road_polygon(self):
        return self.road_polygon

    def get_road_length(self):
        return LineString([(t[0], t[1]) for t in self.interpolated_points]).length


class TestGenerationStatistic:
    """
        Store statistics about test generation
        TODO: Refactor using a RoadTest and RoadTestExecution
    """

    def __init__(self):
        self.test_generated = 0
        self.test_valid = 0
        self.test_invalid = 0
        self.test_passed = 0
        self.test_failed = 0
        self.test_in_error = 0
        self.obes = 0

        self.test_execution_real_times = []
        self.test_execution_simulation_times = []

        # TODO Capturing this is not that easy. We might approximate it as the time between consecutive
        #  calls to execute_test, but then we need to factor out how long it took to execute them... also
        #  it does not account for invalid tests...
        # self.last_generation_time = time.monotonic()
        # self.test_generation_times = []

    def __str__(self):
        msg = ""
        msg += "test generated: " + str(self.test_generated) + "\n"
        msg += "test valid: " + str(self.test_valid) + "\n"
        msg += "test invalid: " + str(self.test_invalid) + "\n"
        msg += "test passed: " + str(self.test_passed) + "\n"
        msg += "test failed: " + str(self.test_failed) + "\n"
        msg += "test in_error: " + str(self.test_in_error) + "\n"
        msg += "(real) time spent in execution :" + str(sum(self.test_execution_real_times)) + "\n"
        # self.test_execution_simulation_times = []
        return msg