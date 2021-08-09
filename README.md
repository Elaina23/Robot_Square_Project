# Robot_Square_Project


This a ROS program written in Python. The Service Server takes in a custom service message "BB8CustomServiceMessage.srv" which can be found in the srv directory.The service server is programmed to move the robot(I used a BB8 robot) in diagonals which forms a square. The Service Server when called by the Service CLient performs the above mentioned movement taking into account the size and repetitions variables specified in the BB8CustomServiceMessage.srv and robot_square_client.py(Service CLient) files.
