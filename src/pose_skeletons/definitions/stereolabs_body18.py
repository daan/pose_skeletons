from enum import IntEnum
from ..definition import SkeletonDefinition


class StereolabsBody18Joints(IntEnum):
    NOSE = 0
    NECK = 1
    RIGHT_SHOULDER = 2
    RIGHT_ELBOW = 3
    RIGHT_WRIST = 4
    LEFT_SHOULDER = 5
    LEFT_ELBOW = 6
    LEFT_WRIST = 7
    RIGHT_HIP = 8
    RIGHT_KNEE = 9
    RIGHT_ANKLE = 10
    LEFT_HIP = 11
    LEFT_KNEE = 12
    LEFT_ANKLE = 13
    RIGHT_EYE = 14
    LEFT_EYE = 15
    RIGHT_EAR = 16
    LEFT_EAR = 17


class StereolabsBody18(SkeletonDefinition):
    def __init__(self):
        # The joint names from the definition list.
        names = [j.name for j in StereolabsBody18Joints]

        # The parent index for each joint. -1 for root.
        # Topology based on ZED SDK BODY_18 hierarchy.
        parents = [
            1,   # 0  NOSE -> NECK
            -1,  # 1  NECK (Root)
            1,   # 2  RIGHT_SHOULDER -> NECK
            2,   # 3  RIGHT_ELBOW -> RIGHT_SHOULDER
            3,   # 4  RIGHT_WRIST -> RIGHT_ELBOW
            1,   # 5  LEFT_SHOULDER -> NECK
            5,   # 6  LEFT_ELBOW -> LEFT_SHOULDER
            6,   # 7  LEFT_WRIST -> LEFT_ELBOW
            2,   # 8  RIGHT_HIP -> RIGHT_SHOULDER (torso connection)
            8,   # 9  RIGHT_KNEE -> RIGHT_HIP
            9,   # 10 RIGHT_ANKLE -> RIGHT_KNEE
            5,   # 11 LEFT_HIP -> LEFT_SHOULDER (torso connection)
            11,  # 12 LEFT_KNEE -> LEFT_HIP
            12,  # 13 LEFT_ANKLE -> LEFT_KNEE
            0,   # 14 RIGHT_EYE -> NOSE
            0,   # 15 LEFT_EYE -> NOSE
            14,  # 16 RIGHT_EAR -> RIGHT_EYE
            15,  # 17 LEFT_EAR -> LEFT_EYE
        ]

        super().__init__("StereolabsBody18", names, parents)

        # --- Standard Joint Mapping ---
        # BODY_18 does not have pelvis/spine joints like BODY_34.
        self.hips = None
        self.spine_low = None
        self.spine_mid = None
        self.spine_high = None
        self.neck = StereolabsBody18Joints.NECK
        self.head = StereolabsBody18Joints.NOSE

        # Arm mappings (no clavicle in BODY_18)
        self.l_clavicle = None
        self.l_shoulder = StereolabsBody18Joints.LEFT_SHOULDER
        self.l_elbow = StereolabsBody18Joints.LEFT_ELBOW
        self.l_wrist = StereolabsBody18Joints.LEFT_WRIST

        self.r_clavicle = None
        self.r_shoulder = StereolabsBody18Joints.RIGHT_SHOULDER
        self.r_elbow = StereolabsBody18Joints.RIGHT_ELBOW
        self.r_wrist = StereolabsBody18Joints.RIGHT_WRIST

        # Leg mappings (no foot in BODY_18)
        self.l_hip = StereolabsBody18Joints.LEFT_HIP
        self.l_knee = StereolabsBody18Joints.LEFT_KNEE
        self.l_ankle = StereolabsBody18Joints.LEFT_ANKLE
        self.l_foot = None

        self.r_hip = StereolabsBody18Joints.RIGHT_HIP
        self.r_knee = StereolabsBody18Joints.RIGHT_KNEE
        self.r_ankle = StereolabsBody18Joints.RIGHT_ANKLE
        self.r_foot = None

