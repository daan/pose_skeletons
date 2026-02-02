from enum import IntEnum
from ..definition import SkeletonDefinition


class SmplxJoints(IntEnum):
    """SMPL-X model joint indices (144 joints: body + hands + face)."""
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
    # Face articulation (22-24)
    Jaw = 22
    LeftEyeSmplhf = 23
    RightEyeSmplhf = 24
    # Left hand fingers (25-39)
    LeftIndex1 = 25
    LeftIndex2 = 26
    LeftIndex3 = 27
    LeftMiddle1 = 28
    LeftMiddle2 = 29
    LeftMiddle3 = 30
    LeftPinky1 = 31
    LeftPinky2 = 32
    LeftPinky3 = 33
    LeftRing1 = 34
    LeftRing2 = 35
    LeftRing3 = 36
    LeftThumb1 = 37
    LeftThumb2 = 38
    LeftThumb3 = 39
    # Right hand fingers (40-54)
    RightIndex1 = 40
    RightIndex2 = 41
    RightIndex3 = 42
    RightMiddle1 = 43
    RightMiddle2 = 44
    RightMiddle3 = 45
    RightPinky1 = 46
    RightPinky2 = 47
    RightPinky3 = 48
    RightRing1 = 49
    RightRing2 = 50
    RightRing3 = 51
    RightThumb1 = 52
    RightThumb2 = 53
    RightThumb3 = 54
    # Regressed body landmarks (55-65)
    Nose = 55
    RightEye = 56
    LeftEye = 57
    RightEar = 58
    LeftEar = 59
    LeftBigToe = 60
    LeftSmallToe = 61
    LeftHeel = 62
    RightBigToe = 63
    RightSmallToe = 64
    RightHeel = 65
    # Finger tips (66-75)
    LeftThumbTip = 66
    LeftIndexTip = 67
    LeftMiddleTip = 68
    LeftRingTip = 69
    LeftPinkyTip = 70
    RightThumbTip = 71
    RightIndexTip = 72
    RightMiddleTip = 73
    RightRingTip = 74
    RightPinkyTip = 75
    # Face landmarks (76-143)
    RightEyeBrow1 = 76
    RightEyeBrow2 = 77
    RightEyeBrow3 = 78
    RightEyeBrow4 = 79
    RightEyeBrow5 = 80
    LeftEyeBrow5 = 81
    LeftEyeBrow4 = 82
    LeftEyeBrow3 = 83
    LeftEyeBrow2 = 84
    LeftEyeBrow1 = 85
    Nose1 = 86
    Nose2 = 87
    Nose3 = 88
    Nose4 = 89
    RightNose2 = 90
    RightNose1 = 91
    NoseMiddle = 92
    LeftNose1 = 93
    LeftNose2 = 94
    RightEye1 = 95
    RightEye2 = 96
    RightEye3 = 97
    RightEye4 = 98
    RightEye5 = 99
    RightEye6 = 100
    LeftEye4 = 101
    LeftEye3 = 102
    LeftEye2 = 103
    LeftEye1 = 104
    LeftEye6 = 105
    LeftEye5 = 106
    RightMouth1 = 107
    RightMouth2 = 108
    RightMouth3 = 109
    MouthTop = 110
    LeftMouth3 = 111
    LeftMouth2 = 112
    LeftMouth1 = 113
    LeftMouth5 = 114
    LeftMouth4 = 115
    MouthBottom = 116
    RightMouth4 = 117
    RightMouth5 = 118
    RightLip1 = 119
    RightLip2 = 120
    LipTop = 121
    LeftLip2 = 122
    LeftLip1 = 123
    LeftLip3 = 124
    LipBottom = 125
    RightLip3 = 126
    RightContour1 = 127
    RightContour2 = 128
    RightContour3 = 129
    RightContour4 = 130
    RightContour5 = 131
    RightContour6 = 132
    RightContour7 = 133
    RightContour8 = 134
    ContourMiddle = 135
    LeftContour8 = 136
    LeftContour7 = 137
    LeftContour6 = 138
    LeftContour5 = 139
    LeftContour4 = 140
    LeftContour3 = 141
    LeftContour2 = 142
    LeftContour1 = 143


class Smplx(SkeletonDefinition):
    """SMPL-X body model skeleton definition (144 joints with hands and face)."""

    def __init__(self):
        # Joint names matching the official SMPL-X model
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
            # Face articulation (22-24)
            "jaw",
            "left_eye_smplhf",
            "right_eye_smplhf",
            # Left hand fingers (25-39)
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
            # Right hand fingers (40-54)
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
            # Regressed body landmarks (55-65)
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
            # Finger tips (66-75)
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
            # Face landmarks (76-143)
            "right_eye_brow1",
            "right_eye_brow2",
            "right_eye_brow3",
            "right_eye_brow4",
            "right_eye_brow5",
            "left_eye_brow5",
            "left_eye_brow4",
            "left_eye_brow3",
            "left_eye_brow2",
            "left_eye_brow1",
            "nose1",
            "nose2",
            "nose3",
            "nose4",
            "right_nose_2",
            "right_nose_1",
            "nose_middle",
            "left_nose_1",
            "left_nose_2",
            "right_eye1",
            "right_eye2",
            "right_eye3",
            "right_eye4",
            "right_eye5",
            "right_eye6",
            "left_eye4",
            "left_eye3",
            "left_eye2",
            "left_eye1",
            "left_eye6",
            "left_eye5",
            "right_mouth_1",
            "right_mouth_2",
            "right_mouth_3",
            "mouth_top",
            "left_mouth_3",
            "left_mouth_2",
            "left_mouth_1",
            "left_mouth_5",
            "left_mouth_4",
            "mouth_bottom",
            "right_mouth_4",
            "right_mouth_5",
            "right_lip_1",
            "right_lip_2",
            "lip_top",
            "left_lip_2",
            "left_lip_1",
            "left_lip_3",
            "lip_bottom",
            "right_lip_3",
            "right_contour_1",
            "right_contour_2",
            "right_contour_3",
            "right_contour_4",
            "right_contour_5",
            "right_contour_6",
            "right_contour_7",
            "right_contour_8",
            "contour_middle",
            "left_contour_8",
            "left_contour_7",
            "left_contour_6",
            "left_contour_5",
            "left_contour_4",
            "left_contour_3",
            "left_contour_2",
            "left_contour_1",
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
            # Face articulation (22-24)
            15,  # 22: jaw -> head
            15,  # 23: left_eye_smplhf -> head
            15,  # 24: right_eye_smplhf -> head
            # Left hand fingers (25-39)
            20,  # 25: left_index1 -> left_wrist
            25,  # 26: left_index2 -> left_index1
            26,  # 27: left_index3 -> left_index2
            20,  # 28: left_middle1 -> left_wrist
            28,  # 29: left_middle2 -> left_middle1
            29,  # 30: left_middle3 -> left_middle2
            20,  # 31: left_pinky1 -> left_wrist
            31,  # 32: left_pinky2 -> left_pinky1
            32,  # 33: left_pinky3 -> left_pinky2
            20,  # 34: left_ring1 -> left_wrist
            34,  # 35: left_ring2 -> left_ring1
            35,  # 36: left_ring3 -> left_ring2
            20,  # 37: left_thumb1 -> left_wrist
            37,  # 38: left_thumb2 -> left_thumb1
            38,  # 39: left_thumb3 -> left_thumb2
            # Right hand fingers (40-54)
            21,  # 40: right_index1 -> right_wrist
            40,  # 41: right_index2 -> right_index1
            41,  # 42: right_index3 -> right_index2
            21,  # 43: right_middle1 -> right_wrist
            43,  # 44: right_middle2 -> right_middle1
            44,  # 45: right_middle3 -> right_middle2
            21,  # 46: right_pinky1 -> right_wrist
            46,  # 47: right_pinky2 -> right_pinky1
            47,  # 48: right_pinky3 -> right_pinky2
            21,  # 49: right_ring1 -> right_wrist
            49,  # 50: right_ring2 -> right_ring1
            50,  # 51: right_ring3 -> right_ring2
            21,  # 52: right_thumb1 -> right_wrist
            52,  # 53: right_thumb2 -> right_thumb1
            53,  # 54: right_thumb3 -> right_thumb2
            # Regressed body landmarks (55-65)
            15,  # 55: nose -> head
            15,  # 56: right_eye -> head
            15,  # 57: left_eye -> head
            15,  # 58: right_ear -> head
            15,  # 59: left_ear -> head
            10,  # 60: left_big_toe -> left_foot
            10,  # 61: left_small_toe -> left_foot
             7,  # 62: left_heel -> left_ankle
            11,  # 63: right_big_toe -> right_foot
            11,  # 64: right_small_toe -> right_foot
             8,  # 65: right_heel -> right_ankle
            # Finger tips (66-75)
            39,  # 66: left_thumb (tip) -> left_thumb3
            27,  # 67: left_index (tip) -> left_index3
            30,  # 68: left_middle (tip) -> left_middle3
            36,  # 69: left_ring (tip) -> left_ring3
            33,  # 70: left_pinky (tip) -> left_pinky3
            54,  # 71: right_thumb (tip) -> right_thumb3
            42,  # 72: right_index (tip) -> right_index3
            45,  # 73: right_middle (tip) -> right_middle3
            51,  # 74: right_ring (tip) -> right_ring3
            48,  # 75: right_pinky (tip) -> right_pinky3
            # Face landmarks (76-143) - all parent to head
            15,  # 76: right_eye_brow1 -> head
            15,  # 77: right_eye_brow2 -> head
            15,  # 78: right_eye_brow3 -> head
            15,  # 79: right_eye_brow4 -> head
            15,  # 80: right_eye_brow5 -> head
            15,  # 81: left_eye_brow5 -> head
            15,  # 82: left_eye_brow4 -> head
            15,  # 83: left_eye_brow3 -> head
            15,  # 84: left_eye_brow2 -> head
            15,  # 85: left_eye_brow1 -> head
            15,  # 86: nose1 -> head
            15,  # 87: nose2 -> head
            15,  # 88: nose3 -> head
            15,  # 89: nose4 -> head
            15,  # 90: right_nose_2 -> head
            15,  # 91: right_nose_1 -> head
            15,  # 92: nose_middle -> head
            15,  # 93: left_nose_1 -> head
            15,  # 94: left_nose_2 -> head
            15,  # 95: right_eye1 -> head
            15,  # 96: right_eye2 -> head
            15,  # 97: right_eye3 -> head
            15,  # 98: right_eye4 -> head
            15,  # 99: right_eye5 -> head
            15,  # 100: right_eye6 -> head
            15,  # 101: left_eye4 -> head
            15,  # 102: left_eye3 -> head
            15,  # 103: left_eye2 -> head
            15,  # 104: left_eye1 -> head
            15,  # 105: left_eye6 -> head
            15,  # 106: left_eye5 -> head
            15,  # 107: right_mouth_1 -> head
            15,  # 108: right_mouth_2 -> head
            15,  # 109: right_mouth_3 -> head
            15,  # 110: mouth_top -> head
            15,  # 111: left_mouth_3 -> head
            15,  # 112: left_mouth_2 -> head
            15,  # 113: left_mouth_1 -> head
            15,  # 114: left_mouth_5 -> head
            15,  # 115: left_mouth_4 -> head
            15,  # 116: mouth_bottom -> head
            15,  # 117: right_mouth_4 -> head
            15,  # 118: right_mouth_5 -> head
            15,  # 119: right_lip_1 -> head
            15,  # 120: right_lip_2 -> head
            15,  # 121: lip_top -> head
            15,  # 122: left_lip_2 -> head
            15,  # 123: left_lip_1 -> head
            15,  # 124: left_lip_3 -> head
            15,  # 125: lip_bottom -> head
            15,  # 126: right_lip_3 -> head
            15,  # 127: right_contour_1 -> head
            15,  # 128: right_contour_2 -> head
            15,  # 129: right_contour_3 -> head
            15,  # 130: right_contour_4 -> head
            15,  # 131: right_contour_5 -> head
            15,  # 132: right_contour_6 -> head
            15,  # 133: right_contour_7 -> head
            15,  # 134: right_contour_8 -> head
            15,  # 135: contour_middle -> head
            15,  # 136: left_contour_8 -> head
            15,  # 137: left_contour_7 -> head
            15,  # 138: left_contour_6 -> head
            15,  # 139: left_contour_5 -> head
            15,  # 140: left_contour_4 -> head
            15,  # 141: left_contour_3 -> head
            15,  # 142: left_contour_2 -> head
            15,  # 143: left_contour_1 -> head
        ]

        super().__init__("SMPLX", names, parents)

        # --- Standard Joint Mapping ---
        self.hips = SmplxJoints.Pelvis
        self.spine_low = SmplxJoints.Spine1
        self.spine_mid = SmplxJoints.Spine2
        self.spine_high = SmplxJoints.Spine3
        self.neck = SmplxJoints.Neck
        self.head = SmplxJoints.Head

        self.l_clavicle = SmplxJoints.LeftCollar
        self.l_shoulder = SmplxJoints.LeftShoulder
        self.l_elbow = SmplxJoints.LeftElbow
        self.l_wrist = SmplxJoints.LeftWrist

        self.r_clavicle = SmplxJoints.RightCollar
        self.r_shoulder = SmplxJoints.RightShoulder
        self.r_elbow = SmplxJoints.RightElbow
        self.r_wrist = SmplxJoints.RightWrist

        self.l_hip = SmplxJoints.LeftHip
        self.l_knee = SmplxJoints.LeftKnee
        self.l_ankle = SmplxJoints.LeftAnkle
        self.l_foot = SmplxJoints.LeftFoot

        self.r_hip = SmplxJoints.RightHip
        self.r_knee = SmplxJoints.RightKnee
        self.r_ankle = SmplxJoints.RightAnkle
        self.r_foot = SmplxJoints.RightFoot
