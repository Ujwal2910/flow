import unittest
import os
import json

from flow.utils.rllib import parse_flow_params

from flow.benchmarks.bottleneck0 import flow_params as bottleneck0
from flow.benchmarks.bottleneck1 import flow_params as bottleneck1
from flow.benchmarks.bottleneck2 import flow_params as bottleneck2
from flow.benchmarks.figureeight0 import flow_params as figure_eight0
from flow.benchmarks.figureeight1 import flow_params as figure_eight1
from flow.benchmarks.figureeight2 import flow_params as figure_eight2
from flow.benchmarks.grid0 import flow_params as grid0
from flow.benchmarks.grid1 import flow_params as grid1
from flow.benchmarks.merge0 import flow_params as merge0
from flow.benchmarks.merge1 import flow_params as merge1
from flow.benchmarks.merge2 import flow_params as merge2

from flow.benchmarks.baselines.bottleneck0 import bottleneck0_baseline
from flow.benchmarks.baselines.bottleneck1 import bottleneck1_baseline
from flow.benchmarks.baselines.bottleneck2 import bottleneck2_baseline
from flow.benchmarks.baselines.figureeight012 import figure_eight_baseline
from flow.benchmarks.baselines.grid0 import grid0_baseline
from flow.benchmarks.baselines.grid1 import grid1_baseline
from flow.benchmarks.baselines.merge012 import merge_baseline

os.environ["TEST_FLAG"] = "True"


class TestBenchmarkEnvironments(unittest.TestCase):
    """Ensures that the benchmark environments are as stated in the paper.

    These tests are meant to ensure that the "flow_params" objects generated
    within each benchmark are frozen and properly parametrized. Since these
    parameters are static, and not meant to change, it seems reasonable for
    there to exist a test that simply checks that the lines of code have not
    changed.

    In order to perform this test, each benchmark is previously serialized in
    the fashion that it is for RLlib experiments, and then during the testing
    period, the "flow_params" object is collected from each benchmark and
    compared with its previously serialized parametrization. If these tests
    fail, this would suggest that some may have (inadvertently) change a
    benchmark, and it needs to be reset to its original form before the PR can
    be accepted.
    """

    def test_bottleneck0(self):
        """
        Tests flow/benchmarks/bottleneck0.py
        """
        cur = os.path.dirname(os.path.abspath(__file__))
        with open(cur + "/test_files/bottleneck0.txt", "rb") as f:
            params_dict = json.load(f)
        previous_params = parse_flow_params(params_dict)

        # test that this inflows are correct
        self.assertTrue(bottleneck0["net"].inflows.__dict__ ==
                        previous_params["net"].inflows.__dict__)
        bottleneck0["net"].inflows = None
        previous_params["net"].inflows = None

        # check that each of the parameter match
        # self.assertEqual(bottleneck0["env"].__dict__,  # FIXME: tuple -> list
        #                  previous_params["env"].__dict__)
        self.assertEqual(bottleneck0["sumo"].__dict__,
                         previous_params["sumo"].__dict__)
        self.assertEqual(bottleneck0["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(bottleneck0["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(bottleneck0["initial"].__dict__,
                         previous_params["initial"].__dict__)
        self.assertEqual(bottleneck0["env_name"],
                         previous_params["env_name"])
        self.assertEqual(bottleneck0["scenario"],
                         previous_params["scenario"])

    def test_bottleneck1(self):
        """
        Tests flow/benchmarks/bottleneck1.py
        """
        cur = os.path.dirname(os.path.abspath(__file__))
        with open(cur + "/test_files/bottleneck1.txt", "rb") as f:
            params_dict = json.load(f)
        previous_params = parse_flow_params(params_dict)

        # test that this inflows are correct
        self.assertTrue(bottleneck1["net"].inflows.__dict__ ==
                        previous_params["net"].inflows.__dict__)
        bottleneck1["net"].inflows = None
        previous_params["net"].inflows = None

        # check that each of the parameter match
        # self.assertEqual(bottleneck1["env"].__dict__,  # FIXME: tuple -> list
        #                  previous_params["env"].__dict__)
        self.assertEqual(bottleneck1["sumo"].__dict__,
                         previous_params["sumo"].__dict__)
        self.assertEqual(bottleneck1["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(bottleneck1["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(bottleneck1["initial"].__dict__,
                         previous_params["initial"].__dict__)
        self.assertEqual(bottleneck1["env_name"],
                         previous_params["env_name"])
        self.assertEqual(bottleneck1["scenario"],
                         previous_params["scenario"])

    def test_bottleneck2(self):
        """
        Tests flow/benchmarks/bottleneck2.py
        """
        cur = os.path.dirname(os.path.abspath(__file__))
        with open(cur + "/test_files/bottleneck2.txt", "rb") as f:
            params_dict = json.load(f)
        previous_params = parse_flow_params(params_dict)

        # test that this inflows are correct
        self.assertTrue(bottleneck2["net"].inflows.__dict__ ==
                        previous_params["net"].inflows.__dict__)
        bottleneck2["net"].inflows = None
        previous_params["net"].inflows = None

        # check that each of the parameter match
        # self.assertEqual(bottleneck2["env"].__dict__,  # FIXME: tuple -> list
        #                  previous_params["env"].__dict__)
        self.assertEqual(bottleneck2["sumo"].__dict__,
                         previous_params["sumo"].__dict__)
        self.assertEqual(bottleneck2["tls"].__dict__,
                         previous_params["tls"].__dict__)
        self.assertEqual(bottleneck2["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(bottleneck2["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(bottleneck2["initial"].__dict__,
                         previous_params["initial"].__dict__)
        self.assertEqual(bottleneck2["env_name"],
                         previous_params["env_name"])
        self.assertEqual(bottleneck2["scenario"],
                         previous_params["scenario"])

    def test_figure_eight0(self):
        """
        Tests flow/benchmarks/figureeight0.py
        """
        cur = os.path.dirname(os.path.abspath(__file__))
        with open(cur + "/test_files/figureeight0.txt", "rb") as f:
            params_dict = json.load(f)
        previous_params = parse_flow_params(params_dict)

        # test that this inflows are correct
        self.assertTrue(figure_eight0["net"].inflows.__dict__ ==
                        previous_params["net"].inflows.__dict__)
        figure_eight0["net"].inflows = None
        previous_params["net"].inflows = None

        # check that each of the parameter match
        self.assertEqual(figure_eight0["env"].__dict__,
                         previous_params["env"].__dict__)
        self.assertEqual(figure_eight0["sumo"].__dict__,
                         previous_params["sumo"].__dict__)
        self.assertEqual(figure_eight0["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(figure_eight0["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(figure_eight0["initial"].__dict__,
                         previous_params["initial"].__dict__)
        self.assertEqual(figure_eight0["env_name"],
                         previous_params["env_name"])
        self.assertEqual(figure_eight0["scenario"],
                         previous_params["scenario"])

    def test_figure_eight1(self):
        """
        Tests flow/benchmarks/figureeight1.py
        """
        cur = os.path.dirname(os.path.abspath(__file__))
        with open(cur + "/test_files/figureeight1.txt", "rb") as f:
            params_dict = json.load(f)
        previous_params = parse_flow_params(params_dict)

        # test that this inflows are correct
        self.assertTrue(figure_eight1["net"].inflows.__dict__ ==
                        previous_params["net"].inflows.__dict__)
        figure_eight1["net"].inflows = None
        previous_params["net"].inflows = None

        # check that each of the parameter match
        self.assertEqual(figure_eight1["env"].__dict__,
                         previous_params["env"].__dict__)
        self.assertEqual(figure_eight1["sumo"].__dict__,
                         previous_params["sumo"].__dict__)
        self.assertEqual(figure_eight1["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(figure_eight1["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(figure_eight1["initial"].__dict__,
                         previous_params["initial"].__dict__)
        self.assertEqual(figure_eight1["env_name"],
                         previous_params["env_name"])
        self.assertEqual(figure_eight1["scenario"],
                         previous_params["scenario"])

    def test_figure_eight2(self):
        """
        Tests flow/benchmarks/figureeight2.py
        """
        cur = os.path.dirname(os.path.abspath(__file__))
        with open(cur + "/test_files/figureeight2.txt", "rb") as f:
            params_dict = json.load(f)
        previous_params = parse_flow_params(params_dict)

        # test that this inflows are correct
        self.assertTrue(figure_eight2["net"].inflows.__dict__ ==
                        previous_params["net"].inflows.__dict__)
        figure_eight2["net"].inflows = None
        previous_params["net"].inflows = None

        # check that each of the parameter match
        self.assertEqual(figure_eight2["env"].__dict__,
                         previous_params["env"].__dict__)
        self.assertEqual(figure_eight2["sumo"].__dict__,
                         previous_params["sumo"].__dict__)
        self.assertEqual(figure_eight2["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(figure_eight2["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(figure_eight2["initial"].__dict__,
                         previous_params["initial"].__dict__)
        self.assertEqual(figure_eight2["env_name"],
                         previous_params["env_name"])
        self.assertEqual(figure_eight2["scenario"],
                         previous_params["scenario"])

    def test_grid0(self):
        """
        Tests flow/benchmarks/grid0.py
        """
        cur = os.path.dirname(os.path.abspath(__file__))
        with open(cur + "/test_files/grid0.txt", "rb") as f:
            params_dict = json.load(f)
        previous_params = parse_flow_params(params_dict)

        # test that this inflows are correct
        self.assertTrue(grid0["net"].inflows.__dict__ ==
                        previous_params["net"].inflows.__dict__)
        grid0["net"].inflows = None
        previous_params["net"].inflows = None

        # check that each of the parameter match
        self.assertEqual(grid0["env"].__dict__,
                         previous_params["env"].__dict__)
        self.assertEqual(grid0["sumo"].__dict__,
                         previous_params["sumo"].__dict__)
        self.assertEqual(grid0["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(grid0["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(grid0["initial"].__dict__,
                         previous_params["initial"].__dict__)
        self.assertEqual(grid0["env_name"],
                         previous_params["env_name"])
        self.assertEqual(grid0["scenario"],
                         previous_params["scenario"])

    def test_grid1(self):
        """
        Tests flow/benchmarks/grid1.py
        """
        cur = os.path.dirname(os.path.abspath(__file__))
        with open(cur + "/test_files/grid1.txt", "rb") as f:
            params_dict = json.load(f)
        previous_params = parse_flow_params(params_dict)

        # test that this inflows are correct
        self.assertTrue(grid1["net"].inflows.__dict__ ==
                        previous_params["net"].inflows.__dict__)
        grid1["net"].inflows = None
        previous_params["net"].inflows = None

        # check that each of the parameter match
        self.assertEqual(grid1["env"].__dict__,
                         previous_params["env"].__dict__)
        self.assertEqual(grid1["sumo"].__dict__,
                         previous_params["sumo"].__dict__)
        self.assertEqual(grid1["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(grid1["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(grid1["initial"].__dict__,
                         previous_params["initial"].__dict__)
        self.assertEqual(grid1["env_name"],
                         previous_params["env_name"])
        self.assertEqual(grid1["scenario"],
                         previous_params["scenario"])

    def test_merge0(self):
        """
        Tests flow/benchmarks/merge0.py
        """
        cur = os.path.dirname(os.path.abspath(__file__))
        with open(cur + "/test_files/merge0.txt", "rb") as f:
            params_dict = json.load(f)
        previous_params = parse_flow_params(params_dict)

        # test that this inflows are correct
        self.assertTrue(merge0["net"].inflows.__dict__ ==
                        previous_params["net"].inflows.__dict__)
        merge0["net"].inflows = None
        previous_params["net"].inflows = None

        # check that each of the parameter match
        self.assertEqual(merge0["env"].__dict__,
                         previous_params["env"].__dict__)
        self.assertEqual(merge0["sumo"].__dict__,
                         previous_params["sumo"].__dict__)
        self.assertEqual(merge0["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(merge0["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(merge0["initial"].__dict__,
                         previous_params["initial"].__dict__)
        self.assertEqual(merge0["env_name"],
                         previous_params["env_name"])
        self.assertEqual(merge0["scenario"],
                         previous_params["scenario"])

    def test_merge1(self):
        """
        Tests flow/benchmarks/merge1.py
        """
        cur = os.path.dirname(os.path.abspath(__file__))
        with open(cur + "/test_files/merge1.txt", "rb") as f:
            params_dict = json.load(f)
        previous_params = parse_flow_params(params_dict)

        # test that this inflows are correct
        self.assertTrue(merge1["net"].inflows.__dict__ ==
                        previous_params["net"].inflows.__dict__)
        merge1["net"].inflows = None
        previous_params["net"].inflows = None

        # check that each of the parameter match
        self.assertEqual(merge1["env"].__dict__,
                         previous_params["env"].__dict__)
        self.assertEqual(merge1["sumo"].__dict__,
                         previous_params["sumo"].__dict__)
        self.assertEqual(merge1["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(merge1["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(merge1["initial"].__dict__,
                         previous_params["initial"].__dict__)
        self.assertEqual(merge1["env_name"],
                         previous_params["env_name"])
        self.assertEqual(merge1["scenario"],
                         previous_params["scenario"])

    def test_merge2(self):
        """
        Tests flow/benchmarks/merge2.py
        """
        cur = os.path.dirname(os.path.abspath(__file__))
        with open(cur + "/test_files/merge2.txt", "rb") as f:
            params_dict = json.load(f)
        previous_params = parse_flow_params(params_dict)

        # test that this inflows are correct
        self.assertTrue(merge2["net"].inflows.__dict__ ==
                        previous_params["net"].inflows.__dict__)
        merge2["net"].inflows = None
        previous_params["net"].inflows = None

        # check that each of the parameter match
        self.assertEqual(merge2["env"].__dict__,
                         previous_params["env"].__dict__)
        self.assertEqual(merge2["sumo"].__dict__,
                         previous_params["sumo"].__dict__)
        self.assertEqual(merge2["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(merge2["net"].__dict__,
                         previous_params["net"].__dict__)
        self.assertEqual(merge2["initial"].__dict__,
                         previous_params["initial"].__dict__)
        self.assertEqual(merge2["env_name"],
                         previous_params["env_name"])
        self.assertEqual(merge2["scenario"],
                         previous_params["scenario"])


class TestBaselines(unittest.TestCase):
    """
    Tests that the baselines in the benchmarks folder are running and
    returning expected values (i.e. values that match those in the CoRL paper
    reported on the website, or other).
    """

    def test_bottleneck0(self):
        """
        Tests flow/benchmark/baselines/bottleneck0.py
        """
        # run the bottleneck to make sure it runs
        bottleneck0_baseline(num_runs=1, render=False)

        # TODO: check that the performance measure is within some range

    def test_bottleneck1(self):
        """
        Tests flow/benchmark/baselines/bottleneck1.py
        """
        # run the bottleneck to make sure it runs
        bottleneck1_baseline(num_runs=1, render=False)

        # TODO: check that the performance measure is within some range

    def test_bottleneck2(self):
        """
        Tests flow/benchmark/baselines/bottleneck2.py
        """
        # run the bottleneck to make sure it runs
        bottleneck2_baseline(num_runs=1, render=False)

        # TODO: check that the performance measure is within some range

    def test_figure_eight(self):
        """
        Tests flow/benchmark/baselines/figureeight{0,1,2}.py
        """
        # run the bottleneck to make sure it runs
        figure_eight_baseline(num_runs=1, render=False)

        # TODO: check that the performance measure is within some range

    def test_grid0(self):
        """
        Tests flow/benchmark/baselines/grid0.py
        """
        # run the bottleneck to make sure it runs
        grid0_baseline(num_runs=1, render=False)

        # TODO: check that the performance measure is within some range

    def test_grid1(self):
        """
        Tests flow/benchmark/baselines/grid1.py
        """
        # run the bottleneck to make sure it runs
        grid1_baseline(num_runs=1, render=False)

        # TODO: check that the performance measure is within some range

    def test_merge(self):
        """
        Tests flow/benchmark/baselines/merge{0,1,2}.py
        """
        # run the bottleneck to make sure it runs
        merge_baseline(num_runs=1, render=False)

        # TODO: check that the performance measure is within some range


if __name__ == '__main__':
    unittest.main()
