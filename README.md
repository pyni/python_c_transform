# numpy_transform
transform among rotation matrix, euler angles and quaternion

Some function can be provided by ROS.
Some ROS api are also provided here:
For example:
1) quaternion to euler:
q = (msg.pose.pose.orientation.x,
     msg.pose.pose.orientation.y,
     msg.pose.pose.orientation.z,
     msg.pose.pose.orientation.w) 
tf.transformations.euler_from_quaternion(q)

2) euler to quaternion:
tf.transformations.quaternion_from_euler(r,p,y)


And i recommand you to read:
http://docs.ros.org/jade/api/tf/html/python/transformations.html#tf.transformations.euler_matrix

