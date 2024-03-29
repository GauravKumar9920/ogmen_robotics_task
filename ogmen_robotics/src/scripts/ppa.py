import rospy
from geometry_msgs.msg import Point
from nav_msgs.msg import Path

#!/usr/bin/env python


def path_planning_node():
    rospy.init_node('path_planning_node', anonymous=True)
    path_pub = rospy.Publisher('path', Path, queue_size=10)

    # Define the start and goal points
    start_point = Point(-6.29, -2.96, 0)
    goal_point = Point(0.477, 1.55, 0)

    # Compute the optimal path between the start and goal points
    path = compute_path(start_point, goal_point)

    # Create a Path message and publish it
    path_msg = Path()
    path_msg.header.stamp = rospy.Time.now()
    path_msg.header.frame_id = 'map'
    path_msg.poses = path
    path_pub.publish(path_msg)

    rospy.spin()

def compute_path(start_point, goal_point):
    # Implement your path planning algorithm here
    # This is where you would compute the optimal path between the start and goal points
    # You can use any path planning algorithm of your choice, such as A* or Dijkstra's algorithm
    

    # For now, let's assume a simple straight line path
    path = [start_point, goal_point]

    return path

if __name__ == '__main__':
    try:
        path_planning_node()
    except rospy.ROSInterruptException:
        pass