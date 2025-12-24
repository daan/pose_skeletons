from enum import IntEnum
from ..definition import SkeletonDefinition


class StereolabsBody34Joints(IntEnum):
    PELVIS = 0
    NAVAL_SPINE = 1
    CHEST_SPINE = 2
    NECK = 3
    LEFT_CLAVICLE = 4
    LEFT_SHOULDER = 5
    LEFT_ELBOW = 6
    LEFT_WRIST = 7
    LEFT_HAND = 8
    LEFT_HANDTIP = 9
    LEFT_THUMB = 10
    RIGHT_CLAVICLE = 11
    RIGHT_SHOULDER = 12
    RIGHT_ELBOW = 13
    RIGHT_WRIST = 14
    RIGHT_HAND = 15
    RIGHT_HANDTIP = 16
    RIGHT_THUMB = 17
    LEFT_HIP = 18
    LEFT_KNEE = 19
    LEFT_ANKLE = 20
    LEFT_FOOT = 21
    RIGHT_HIP = 22
    RIGHT_KNEE = 23
    RIGHT_ANKLE = 24
    RIGHT_FOOT = 25
    HEAD = 26
    NOSE = 27
    LEFT_EYE = 28
    LEFT_EAR = 29
    RIGHT_EYE = 30
    RIGHT_EAR = 31
    LEFT_HEEL = 32
    RIGHT_HEEL = 33


class StereolabsBody34(SkeletonDefinition):
    def __init__(self):
        # The joint names from the definition list.
        names = [j.name for j in StereolabsBody34Joints]

        # The parent index for each joint. -1 for root.
        # Topology based on ZED SDK BODY_34 hierarchy.
        parents = [
            -1,  # 0  PELVIS (Root)
            0,   # 1  NAVAL_SPINE -> PELVIS
            1,   # 2  CHEST_SPINE -> NAVAL_SPINE
            2,   # 3  NECK -> CHEST_SPINE
            2,   # 4  LEFT_CLAVICLE -> CHEST_SPINE
            4,   # 5  LEFT_SHOULDER -> LEFT_CLAVICLE
            5,   # 6  LEFT_ELBOW -> LEFT_SHOULDER
            6,   # 7  LEFT_WRIST -> LEFT_ELBOW
            7,   # 8  LEFT_HAND -> LEFT_WRIST
            8,   # 9  LEFT_HANDTIP -> LEFT_HAND
            7,   # 10 LEFT_THUMB -> LEFT_WRIST (Alternative: 8)
            2,   # 11 RIGHT_CLAVICLE -> CHEST_SPINE
            11,  # 12 RIGHT_SHOULDER -> RIGHT_CLAVICLE
            12,  # 13 RIGHT_ELBOW -> RIGHT_SHOULDER
            13,  # 14 RIGHT_WRIST -> RIGHT_ELBOW
            14,  # 15 RIGHT_HAND -> RIGHT_WRIST
            15,  # 16 RIGHT_HANDTIP -> RIGHT_HAND
            14,  # 17 RIGHT_THUMB -> RIGHT_WRIST (Alternative: 15)
            0,   # 18 LEFT_HIP -> PELVIS
            18,  # 19 LEFT_KNEE -> LEFT_HIP
            19,  # 20 LEFT_ANKLE -> LEFT_KNEE
            20,  # 21 LEFT_FOOT -> LEFT_ANKLE
            0,   # 22 RIGHT_HIP -> PELVIS
            22,  # 23 RIGHT_KNEE -> RIGHT_HIP
            23,  # 24 RIGHT_ANKLE -> RIGHT_KNEE
            24,  # 25 RIGHT_FOOT -> RIGHT_ANKLE
            3,   # 26 HEAD -> NECK
            26,  # 27 NOSE -> HEAD
            26,  # 28 LEFT_EYE -> HEAD
            26,  # 29 LEFT_EAR -> HEAD
            26,  # 30 RIGHT_EYE -> HEAD
            26,  # 31 RIGHT_EAR -> HEAD
            20,  # 32 LEFT_HEEL -> LEFT_ANKLE
            24,  # 33 RIGHT_HEEL -> RIGHT_ANKLE
        ]

        super().__init__("StereolabsBody34", names, parents)

        # --- Standard Joint Mapping ---
        self.hips = StereolabsBody34Joints.PELVIS
        self.spine_low = StereolabsBody34Joints.NAVAL_SPINE
        self.spine_mid = StereolabsBody34Joints.CHEST_SPINE
        self.spine_high = StereolabsBody34Joints.NECK
        self.neck = StereolabsBody34Joints.NECK
        self.head = StereolabsBody34Joints.HEAD

        # Arm mappings
        self.l_clavicle = StereolabsBody34Joints.LEFT_CLAVICLE
        self.l_shoulder = StereolabsBody34Joints.LEFT_SHOULDER
        self.l_elbow = StereolabsBody34Joints.LEFT_ELBOW
        self.l_wrist = StereolabsBody34Joints.LEFT_WRIST
        self.l_hand = StereolabsBody34Joints.LEFT_HAND

        self.r_clavicle = StereolabsBody34Joints.RIGHT_CLAVICLE
        self.r_shoulder = StereolabsBody34Joints.RIGHT_SHOULDER
        self.r_elbow = StereolabsBody34Joints.RIGHT_ELBOW
        self.r_wrist = StereolabsBody34Joints.RIGHT_WRIST
        self.r_hand = StereolabsBody34Joints.RIGHT_HAND

        # Leg mappings
        self.l_hip = StereolabsBody34Joints.LEFT_HIP
        self.l_knee = StereolabsBody34Joints.LEFT_KNEE
        self.l_ankle = StereolabsBody34Joints.LEFT_ANKLE
        self.l_foot = StereolabsBody34Joints.LEFT_FOOT

        self.r_hip = StereolabsBody34Joints.RIGHT_HIP
        self.r_knee = StereolabsBody34Joints.RIGHT_KNEE
        self.r_ankle = StereolabsBody34Joints.RIGHT_ANKLE
        self.r_foot = StereolabsBody34Joints.RIGHT_FOOT


