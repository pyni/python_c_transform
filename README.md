# python_transform

1)基本变换：

transform among rotation matrix, euler angles and quaternion

写程序经常遇到各种欧拉角，矩阵，四元数转化，这个包还有下面的网址也许可以帮到你

本文中的euler2rotm是相对于静态坐标系的，如果是动态坐标系可以直接用ROS的API：


tf.transformations.euler_matrix(r,p,y,axes='rxyz')#动态


tf.transformations.euler_matrix(r,p,y,axes='sxyz')#静态


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

...

And i recommend you to read:
http://docs.ros.org/jade/api/tf/html/python/transformations.html#tf.transformations.euler_matrix


写的有点乱，也没指望谁能看懂，我看的懂就行

2)已知目标转换的平移和其的三个轴线(x,y,z)的方向向量，或两个轴线(x,y)的方向向量，求该转换相对于绝对坐标的变换（下面举了一个已知两个轴线方向的例子）：
下面的程序视为，先移动，解决目标的平移问题，然后再旋转（但是是绕自己本身旋转）

    new_transformationtrans = np.identity(4)
    new_transformationtrans[0,3]=已知给定
    new_transformationtrans[1,3]=已知给定
    new_transformationtrans[2,3]=已知给定
    
    xaxis= 已知给定
    yaxis= 已知给定
    xaxis= xaxis/np.linalg.norm(xaxis)
    yaxis=yaxis/np.linalg.norm(yaxis)
    zaxis=np.cross(xaxis, yaxis)#叉乘求z方向

    new_transformationrot= np.identity(4)
    new_transformationrot[0:3,0]=xaxis
    new_transformationrot[0:3,1]=yaxis
    new_transformationrot[0:3,2]=zaxis#不确定是不是这个，感觉应该是

    current_transformation=np.dot(new_transformationtrans,new_transformationrot) #相对于自身变换，所以是右乘






# c_transform
C++的变换大多以eigen为主：
可参见：https://www.cc.gatech.edu/classes/AY2015/cs4496_spring/Eigen.html
一些值得注意的用法，如：

１）矩阵转四元数：

Matrix3f mat;
Quaternionf q(mat);
或者：
Quaternionf q;
q = mat;

２）四元数取值：q.x(),q.y()...

3) 四元数转矩阵：

Eigen::Matrix3f mat3 = Eigen::Quaternionf(W, X, Y, Z).toRotationMatrix();
Eigen::Matrix4f mat4 = Eigen::Matrix4f::Identity();
mat4.block(0,0,3,3) = mat3;

4) RPY转矩阵：

Eigen::AngleAxisf rollAngle(0, Eigen::Vector3f::UnitX());
Eigen::AngleAxisf pitchAngle(0, Eigen::Vector3f::UnitY());
Eigen::AngleAxisf yawAngle(0, Eigen::Vector3f::UnitZ()); 
Eigen::Quaternionf  q = yawAngle * pitchAngle * rollAngle; 
Eigen::Matrix3f mat3_humanpredefined = q.matrix();  
transform_humanpredefined.block(0,0,3,3) = mat3_humanpredefined;

5) 两队点用SVD求R，T变换（这两队点变换前后要相互对应）：

opttest.py

