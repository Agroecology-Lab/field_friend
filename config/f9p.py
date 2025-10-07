"""
Example configuration for a Field Friend robot with u-blox ZED-F9P GNSS module.

This configuration demonstrates how to set up a robot to use the F9P GNSS receiver
instead of the default Septentrio receiver.

To use this configuration:
1. Ensure you have updated requirements.txt to use Agroecology-Lab/rosys fork
2. Install pyubx2: pip install pyubx2>=2.7.0
3. Add user to dialout group: sudo usermod -a -G dialout $USER
4. Connect F9P module via USB
5. Run: python main.py --robot-id robot_f9p_example
"""

from dataclasses import dataclass

from field_friend.config.configuration import (
    FieldFriendConfiguration,
    GnssConfiguration,
    # Add other necessary imports based on your robot's hardware
    # For example:
    BumperConfiguration,
    CameraConfiguration,
    CircleSightPositions,
    CropConfiguration,
    FieldFriendConfiguration,
    FlashlightConfiguration,
    GnssConfiguration,
    MeasurementsConfiguration,
    RobotBrainConfiguration,
    TornadoConfiguration,
    WheelsConfiguration,
    YStepperConfiguration,
)


@dataclass
class RobotF9PExampleConfiguration(FieldFriendConfiguration):
    """Configuration for a Field Friend robot with F9P GNSS module."""
    
    # Override the GNSS configuration to use F9P hardware
    gnss: GnssConfiguration = GnssConfiguration(
        # IMPORTANT: Adjust these values to match your antenna's position on the robot
        x=0.041,      # Forward offset from robot center (meters)
        y=-0.255,     # Lateral offset from robot center (meters)
        z=0.6225,     # Height above ground (meters)
        yaw=0.0,      # Orientation (radians)
        hardware_type='f9p'  # This tells the system to use GnssZEDF9P
    )

config = FieldFriendConfiguration(
    name='uckerbot-f9p',
    robot_brain=RobotBrainConfiguration(name='rb28',
                                        flash_params=['orin'],
                                        enable_esp_on_startup=True,
                                        use_espresso=True),
    tool='tornado',
    measurements=MeasurementsConfiguration(
        tooth_count=17,
        pitch=0.041,
        work_x=-0.0025,
    ),
    camera=CameraConfiguration(
        width=1280,
        height=720,
        crop=CropConfiguration(left=250, right=250, up=0, down=0),
    ),
    circle_sight_positions=CircleSightPositions(
        right='-2',
        left='-4',  # not sure, camera not working
        front='-3',
        back='-1',  # not sure, camera not working
    ),
    wheels=WheelsConfiguration(
        is_left_reversed=False,
        is_right_reversed=True,
        left_back_can_address=0x000,
        left_front_can_address=0x100,
        right_back_can_address=0x200,
        right_front_can_address=0x300,
        odrive_version=6,
    ),
    has_status_control=True,
    flashlight=FlashlightConfiguration(
        version='flashlight_pwm',
        pin=2,
        on_expander=True,
        rated_voltage=23.0,
    ),
    bumper=BumperConfiguration(pin_front_top=12, pin_front_bottom=22, pin_back=25),
    y_axis=YStepperConfiguration(
        axis_offset=0.0575,
        reversed_direction=False,
        end_stops_on_expander=True,
        motor_on_expander=False,
        end_stops_inverted=True,
        max_speed=30_000,
        reference_speed=5_000,
        steps_per_m=599_251,
        direction_pin=4,
        step_pin=5,
        end_left_pin=21,
        end_right_pin=19,
        name='y_axis',
        max_position=0.0575,
        min_position=-0.0575,
        version='y_axis_stepper',
        alarm_inverted=True,
        alarm_pin=13,
    ),
    z_axis=TornadoConfiguration(
        end_stops_on_expander=True,
        motor_on_expander=False,
        end_bottom_pin=5,
        end_top_pin=32,
        name='tornado',
        max_position=0.0,
        min_position=-0.09,
        version='tornado',
        ref_gear_pin=4,
        ref_knife_ground_pin=18,
        ref_knife_stop_pin=35,
        ref_motor_pin=33,
        turn_speed_limit=1.3,
        odrive_version=6,
    ),
    gnss=GnssConfiguration(),
    # TODO: IMU configuration is probably wrong. Check https://github.com/zauberzeug/field_friend/pull/361
    # imu=ImuConfiguration(offset_rotation=Rotation.from_euler(-1.570796, 0, 0)),
    imu=None,
)

