from enum import IntEnum
from ..definition import SkeletonDefinition


class SmplJoints(IntEnum):
    """SMPL model joint indices (24 joints)."""
    Pelvis = 0
    LeftHip = 1
    RightHip = 2
    Spine1 = 3
    LeftKnee = 4
    RightKnee = 5
    Spine2 = 6
    LeftAnkle = 7
    RightAnkle = 8
    Spine3 = 9
    LeftFoot = 10
    RightFoot = 11
    Neck = 12
    LeftCollar = 13
    RightCollar = 14
    Head = 15
    LeftShoulder = 16
    RightShoulder = 17
    LeftElbow = 18
    RightElbow = 19
    LeftWrist = 20
    RightWrist = 21
    LeftHand = 22
    RightHand = 23


class Smpl(SkeletonDefinition):
    """SMPL body model skeleton definition (24 joints)."""

    def __init__(self):
        # Joint names matching the official SMPL model
        names = [
            "pelvis",
            "left_hip",
            "right_hip",
            "spine1",
            "left_knee",
            "right_knee",
            "spine2",
            "left_ankle",
            "right_ankle",
            "spine3",
            "left_foot",
            "right_foot",
            "neck",
            "left_collar",
            "right_collar",
            "head",
            "left_shoulder",
            "right_shoulder",
            "left_elbow",
            "right_elbow",
            "left_wrist",
            "right_wrist",
            "left_hand",
            "right_hand",
        ]

        # Parent indices defining the kinematic tree
        # Each index points to the parent joint, -1 for root
        parents = [
            -1,  # 0: pelvis (root)
             0,  # 1: left_hip -> pelvis
             0,  # 2: right_hip -> pelvis
             0,  # 3: spine1 -> pelvis
             1,  # 4: left_knee -> left_hip
             2,  # 5: right_knee -> right_hip
             3,  # 6: spine2 -> spine1
             4,  # 7: left_ankle -> left_knee
             5,  # 8: right_ankle -> right_knee
             6,  # 9: spine3 -> spine2
             7,  # 10: left_foot -> left_ankle
             8,  # 11: right_foot -> right_ankle
             9,  # 12: neck -> spine3
             9,  # 13: left_collar -> spine3
             9,  # 14: right_collar -> spine3
            12,  # 15: head -> neck
            13,  # 16: left_shoulder -> left_collar
            14,  # 17: right_shoulder -> right_collar
            16,  # 18: left_elbow -> left_shoulder
            17,  # 19: right_elbow -> right_shoulder
            18,  # 20: left_wrist -> left_elbow
            19,  # 21: right_wrist -> right_elbow
            20,  # 22: left_hand -> left_wrist
            21,  # 23: right_hand -> right_wrist
        ]

        super().__init__("SMPL", names, parents)

        # --- Standard Joint Mapping ---
        self.hips = SmplJoints.Pelvis
        self.spine_low = SmplJoints.Spine1
        self.spine_mid = SmplJoints.Spine2
        self.spine_high = SmplJoints.Spine3
        self.neck = SmplJoints.Neck
        self.head = SmplJoints.Head

        self.l_clavicle = SmplJoints.LeftCollar
        self.l_shoulder = SmplJoints.LeftShoulder
        self.l_elbow = SmplJoints.LeftElbow
        self.l_wrist = SmplJoints.LeftWrist

        self.r_clavicle = SmplJoints.RightCollar
        self.r_shoulder = SmplJoints.RightShoulder
        self.r_elbow = SmplJoints.RightElbow
        self.r_wrist = SmplJoints.RightWrist

        self.l_hip = SmplJoints.LeftHip
        self.l_knee = SmplJoints.LeftKnee
        self.l_ankle = SmplJoints.LeftAnkle
        self.l_foot = SmplJoints.LeftFoot

        self.r_hip = SmplJoints.RightHip
        self.r_knee = SmplJoints.RightKnee
        self.r_ankle = SmplJoints.RightAnkle
        self.r_foot = SmplJoints.RightFoot
