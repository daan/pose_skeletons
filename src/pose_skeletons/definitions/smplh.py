from enum import IntEnum
from ..definition import SkeletonDefinition


class SmplhJoints(IntEnum):
    """SMPL+H model joint indices (73 joints: 22 body + 30 hand + 21 landmarks)."""
    # Body joints (0-21)
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
    # Left hand fingers (22-36)
    LeftIndex1 = 22
    LeftIndex2 = 23
    LeftIndex3 = 24
    LeftMiddle1 = 25
    LeftMiddle2 = 26
    LeftMiddle3 = 27
    LeftPinky1 = 28
    LeftPinky2 = 29
    LeftPinky3 = 30
    LeftRing1 = 31
    LeftRing2 = 32
    LeftRing3 = 33
    LeftThumb1 = 34
    LeftThumb2 = 35
    LeftThumb3 = 36
    # Right hand fingers (37-51)
    RightIndex1 = 37
    RightIndex2 = 38
    RightIndex3 = 39
    RightMiddle1 = 40
    RightMiddle2 = 41
    RightMiddle3 = 42
    RightPinky1 = 43
    RightPinky2 = 44
    RightPinky3 = 45
    RightRing1 = 46
    RightRing2 = 47
    RightRing3 = 48
    RightThumb1 = 49
    RightThumb2 = 50
    RightThumb3 = 51
    # Regressed landmarks (52-72)
    Nose = 52
    RightEye = 53
    LeftEye = 54
    RightEar = 55
    LeftEar = 56
    LeftBigToe = 57
    LeftSmallToe = 58
    LeftHeel = 59
    RightBigToe = 60
    RightSmallToe = 61
    RightHeel = 62
    LeftThumbTip = 63
    LeftIndexTip = 64
    LeftMiddleTip = 65
    LeftRingTip = 66
    LeftPinkyTip = 67
    RightThumbTip = 68
    RightIndexTip = 69
    RightMiddleTip = 70
    RightRingTip = 71
    RightPinkyTip = 72


class Smplh(SkeletonDefinition):
    """SMPL+H body model skeleton definition (73 joints with hands)."""

    def __init__(self):
        # Joint names matching the official SMPL+H model
        names = [
            # Body (0-21)
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
            # Left hand fingers (22-36)
            "left_index1",
            "left_index2",
            "left_index3",
            "left_middle1",
            "left_middle2",
            "left_middle3",
            "left_pinky1",
            "left_pinky2",
            "left_pinky3",
            "left_ring1",
            "left_ring2",
            "left_ring3",
            "left_thumb1",
            "left_thumb2",
            "left_thumb3",
            # Right hand fingers (37-51)
            "right_index1",
            "right_index2",
            "right_index3",
            "right_middle1",
            "right_middle2",
            "right_middle3",
            "right_pinky1",
            "right_pinky2",
            "right_pinky3",
            "right_ring1",
            "right_ring2",
            "right_ring3",
            "right_thumb1",
            "right_thumb2",
            "right_thumb3",
            # Regressed landmarks (52-72)
            "nose",
            "right_eye",
            "left_eye",
            "right_ear",
            "left_ear",
            "left_big_toe",
            "left_small_toe",
            "left_heel",
            "right_big_toe",
            "right_small_toe",
            "right_heel",
            "left_thumb",
            "left_index",
            "left_middle",
            "left_ring",
            "left_pinky",
            "right_thumb",
            "right_index",
            "right_middle",
            "right_ring",
            "right_pinky",
        ]

        # Parent indices defining the kinematic tree
        parents = [
            # Body (0-21)
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
            # Left hand fingers (22-36)
            20,  # 22: left_index1 -> left_wrist
            22,  # 23: left_index2 -> left_index1
            23,  # 24: left_index3 -> left_index2
            20,  # 25: left_middle1 -> left_wrist
            25,  # 26: left_middle2 -> left_middle1
            26,  # 27: left_middle3 -> left_middle2
            20,  # 28: left_pinky1 -> left_wrist
            28,  # 29: left_pinky2 -> left_pinky1
            29,  # 30: left_pinky3 -> left_pinky2
            20,  # 31: left_ring1 -> left_wrist
            31,  # 32: left_ring2 -> left_ring1
            32,  # 33: left_ring3 -> left_ring2
            20,  # 34: left_thumb1 -> left_wrist
            34,  # 35: left_thumb2 -> left_thumb1
            35,  # 36: left_thumb3 -> left_thumb2
            # Right hand fingers (37-51)
            21,  # 37: right_index1 -> right_wrist
            37,  # 38: right_index2 -> right_index1
            38,  # 39: right_index3 -> right_index2
            21,  # 40: right_middle1 -> right_wrist
            40,  # 41: right_middle2 -> right_middle1
            41,  # 42: right_middle3 -> right_middle2
            21,  # 43: right_pinky1 -> right_wrist
            43,  # 44: right_pinky2 -> right_pinky1
            44,  # 45: right_pinky3 -> right_pinky2
            21,  # 46: right_ring1 -> right_wrist
            46,  # 47: right_ring2 -> right_ring1
            47,  # 48: right_ring3 -> right_ring2
            21,  # 49: right_thumb1 -> right_wrist
            49,  # 50: right_thumb2 -> right_thumb1
            50,  # 51: right_thumb3 -> right_thumb2
            # Regressed landmarks (52-72)
            15,  # 52: nose -> head
            15,  # 53: right_eye -> head
            15,  # 54: left_eye -> head
            15,  # 55: right_ear -> head
            15,  # 56: left_ear -> head
            10,  # 57: left_big_toe -> left_foot
            10,  # 58: left_small_toe -> left_foot
             7,  # 59: left_heel -> left_ankle
            11,  # 60: right_big_toe -> right_foot
            11,  # 61: right_small_toe -> right_foot
             8,  # 62: right_heel -> right_ankle
            36,  # 63: left_thumb (tip) -> left_thumb3
            24,  # 64: left_index (tip) -> left_index3
            27,  # 65: left_middle (tip) -> left_middle3
            33,  # 66: left_ring (tip) -> left_ring3
            30,  # 67: left_pinky (tip) -> left_pinky3
            51,  # 68: right_thumb (tip) -> right_thumb3
            39,  # 69: right_index (tip) -> right_index3
            42,  # 70: right_middle (tip) -> right_middle3
            48,  # 71: right_ring (tip) -> right_ring3
            45,  # 72: right_pinky (tip) -> right_pinky3
        ]

        super().__init__("SMPLH", names, parents)

        # --- Standard Joint Mapping ---
        self.hips = SmplhJoints.Pelvis
        self.spine_low = SmplhJoints.Spine1
        self.spine_mid = SmplhJoints.Spine2
        self.spine_high = SmplhJoints.Spine3
        self.neck = SmplhJoints.Neck
        self.head = SmplhJoints.Head

        self.l_clavicle = SmplhJoints.LeftCollar
        self.l_shoulder = SmplhJoints.LeftShoulder
        self.l_elbow = SmplhJoints.LeftElbow
        self.l_wrist = SmplhJoints.LeftWrist

        self.r_clavicle = SmplhJoints.RightCollar
        self.r_shoulder = SmplhJoints.RightShoulder
        self.r_elbow = SmplhJoints.RightElbow
        self.r_wrist = SmplhJoints.RightWrist

        self.l_hip = SmplhJoints.LeftHip
        self.l_knee = SmplhJoints.LeftKnee
        self.l_ankle = SmplhJoints.LeftAnkle
        self.l_foot = SmplhJoints.LeftFoot

        self.r_hip = SmplhJoints.RightHip
        self.r_knee = SmplhJoints.RightKnee
        self.r_ankle = SmplhJoints.RightAnkle
        self.r_foot = SmplhJoints.RightFoot
