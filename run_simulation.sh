# Print the current working directory and list its contents
  pwd
  ls -al

  # Show the environment variables that contain the text 'ROS'
  env | grep ROS

  # Start the ROS script that MOVES the robot around in the background
  # Capture the process ID of that script in MOVE_ID
  # Wait for 30 seconds and then kill the process
  roslaunch publisher_example move.launch &
  MOVE_ID=$!
  sleep 30s
  kill $MOVE_ID

  # Start the ROS script that STOPS the robot in the background
  # Capture the process ID of that script in STOP_ID
  # Wait for 5 seconds and then kill the process
  roslaunch publisher_example stop.launch &
  STOP_ID=$!
  sleep 5s
  kill $STOP_ID

  # Call the Gazebo service that resets the simulation
  rosservice call /gazebo/reset_simulation "{}"

  # Print the text that indicates that we are done here
  echo "Job finished"