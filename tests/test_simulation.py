import unittest
import subprocess

class TestSimulation(unittest.TestCase):
    def run_command(self, cmd):
        # Create the shell process
        process = subprocess.Popen(cmd,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        
        # Get the return code and ensure it exits properly
        return_code = process.wait()
        self.assertEqual(return_code, 0)
        
        # Get the output
        out, err = process.communicate()
        self.assertEqual('', err.decode("utf-8"))

        return out.decode("utf-8"), err.decode("utf-8")

    def test_the_simulation_is_running(self):
        # run a command
        out, err = self.run_command('rostopic list')       
        self.assertIn('/gazebo', str(out))
    
    def test_the_simulation_has_a_robot_with_a_brick_wall(self):
        out, err = self.run_command('rostopic echo -n1 /gazebo/model_states')
        self.assertIn('brick_box_3x1x3', out)
        self.assertIn('ground_plane', out)
        self.assertIn('mobile_base', out)

    def test_the_simulation_robot_has_a_laser_scan(self):
        out, err = self.run_command('rostopic list')
        self.assertIn('laser/scan', out)
    
    def test_these_tests_must_pass_or_the_pipeline_fails(self):
        self.assertFalse(True)
