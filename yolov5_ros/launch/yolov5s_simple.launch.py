import os
import launch
import launch_ros.actions
from launch.substitutions import LaunchConfiguration
from launch.substitutions import LaunchConfiguration,PythonExpression
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition

def generate_launch_description():

    image_topic    = LaunchConfiguration('image_topic', default = "image_raw")
    weights        = LaunchConfiguration('weights', default = "")
    data           = LaunchConfiguration('data', default = "")
    imagez_height  = LaunchConfiguration('imagez_height', default = "640")
    imagez_width   = LaunchConfiguration('imagez_width', default = "480")
    conf_thres     = LaunchConfiguration('conf_thres', default = "0.25")
    iou_thres      = LaunchConfiguration('iou_thres', default = "0.45")
    max_det        = LaunchConfiguration('max_det', default = "1000")
    device         = LaunchConfiguration('device', default = "")
    view_img       = LaunchConfiguration('view_img', default = True)
    agnostic_nms   = LaunchConfiguration('agnostic_nms', default = False)
    line_thickness = LaunchConfiguration('line_thickness', default = "2")
    half           = LaunchConfiguration('half', default = False)
    dnn            = LaunchConfiguration('dnn', default = False)
    open_webcam    = LaunchConfiguration('open_webcam', default = True)

    declare_image_topic_cmd = DeclareLaunchArgument(
            'image_topic',
            default_value=image_topic,
    )

    declare_weights_cmd = DeclareLaunchArgument(
            'weights',
            default_value=weights,
    )

    declare_data_cmd = DeclareLaunchArgument(
            'data',
            default_value=data,
    )

    declare_imagez_height_cmd = DeclareLaunchArgument(
            'imagez_height',
            default_value=imagez_height,
    )

    declare_imagez_width_cmd = DeclareLaunchArgument(
            'imagez_width',
            default_value=imagez_width,
    )

    declare_conf_thres_cmd = DeclareLaunchArgument(
            'conf_thres',
            default_value=conf_thres,
    )

    declare_iou_thres_cmd = DeclareLaunchArgument(
            'iou_thres',
            default_value=iou_thres,
    )

    declare_max_det_cmd = DeclareLaunchArgument(
            'max_det',
            default_value=max_det,
    )

    declare_device_cmd = DeclareLaunchArgument(
            'device',
            default_value=device,
    )

    declare_view_img_cmd = DeclareLaunchArgument(
            'view_img',
            default_value=view_img,
    )

    declare_agnostic_nms_cmd = DeclareLaunchArgument(
            'agnostic_nms',
            default_value=agnostic_nms,
    )

    declare_line_thickness_cmd = DeclareLaunchArgument(
            'line_thickness',
            default_value=line_thickness,
    )

    declare_half_cmd = DeclareLaunchArgument(
            'half',
            default_value=half,
    )

    declare_dnn_cmd = DeclareLaunchArgument(
            'dnn',
            default_value=dnn,
    )

    webcam_node = launch_ros.actions.Node(
        condition=IfCondition(open_webcam),
        package="v4l2_camera", executable="v4l2_camera_node",
        parameters=[
            {"image_size": [640,480]},
        ],
    )

    yolov5_ros_node = launch_ros.actions.Node(
        package="yolov5_ros", executable="yolov5_ros",
            parameters=[
                {'image_topic'    : image_topic},
                {'weights'        : weights},
                {'data'           : data},
                {'imagez_height'  : imagez_height},
                {'imagez_width'   : imagez_width},
                {'conf_thres'     : conf_thres},
                {'iou_thres'      : iou_thres},
                {'max_det'        : max_det},
                {'device'         : device},
                {'view_img'       : view_img},
                {'agnostic_nms'   : agnostic_nms},
                {'line_thickness' : line_thickness},
                {'half'           : half},
                {'dnn'            : dnn},                   
        ],
    )

    return launch.LaunchDescription([
        declare_image_topic_cmd,
        declare_weights_cmd,
        declare_data_cmd,
        declare_imagez_height_cmd,
        declare_imagez_width_cmd,
        declare_conf_thres_cmd,
        declare_iou_thres_cmd,
        declare_max_det_cmd,
        declare_device_cmd,
        declare_view_img_cmd,
        declare_agnostic_nms_cmd,
        declare_line_thickness_cmd,
        declare_half_cmd,
        declare_dnn_cmd,

        webcam_node,
        yolov5_ros_node,
    ])