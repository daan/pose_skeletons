from enum import IntEnum
from ..definition import SkeletonDefinition


class MediaPipe33Joints(IntEnum):
    Nose = 0
    LeftEyeInner = 1
    LeftEye = 2
    LeftEyeOuter = 3
    RightEyeInner = 4
    RightEye = 5
    RightEyeOuter = 6
    LeftEar = 7
    RightEar = 8
    MouthLeft = 9
    MouthRight = 10
    LeftShoulder = 11
    RightShoulder = 12
    LeftElbow = 13
    RightElbow = 14
    LeftWrist = 15
    RightWrist = 16
    LeftPinky = 17
    RightPinky = 18
    LeftIndex = 19
    RightIndex = 20
    LeftThumb = 21
    RightThumb = 22
    LeftHip = 23
    RightHip = 24
    LeftKnee = 25
    RightKnee = 26
    LeftAnkle = 27
    RightAnkle = 28
    LeftHeel = 29
    RightHeel = 30
    LeftFootIndex = 31
    RightFootIndex = 32


class MediaPipe33(SkeletonDefinition):
    def __init__(self):
        # The joint names from MediaPipe Pose Landmarker
        names = [j.name for j in MediaPipe33Joints]

        # The parent index for each joint. -1 for root.
        # Topology: Nose is root. Face landmarks connect to nose/eyes.
        # Shoulders connect to nose (no neck joint).
        # Hips connect to shoulders (torso connection).
        parents = [
            -1,  # 0: Nose (Root)
             0,  # 1: LeftEyeInner -> Nose
             1,  # 2: LeftEye -> LeftEyeInner
             2,  # 3: LeftEyeOuter -> LeftEye
             0,  # 4: RightEyeInner -> Nose
             4,  # 5: RightEye -> RightEyeInner
             5,  # 6: RightEyeOuter -> RightEye
             3,  # 7: LeftEar -> LeftEyeOuter
             6,  # 8: RightEar -> RightEyeOuter
             0,  # 9: MouthLeft -> Nose
             0,  # 10: MouthRight -> Nose
             0,  # 11: LeftShoulder -> Nose
             0,  # 12: RightShoulder -> Nose
            11,  # 13: LeftElbow -> LeftShoulder
            12,  # 14: RightElbow -> RightShoulder
            13,  # 15: LeftWrist -> LeftElbow
            14,  # 16: RightWrist -> RightElbow
            15,  # 17: LeftPinky -> LeftWrist
            16,  # 18: RightPinky -> RightWrist
            15,  # 19: LeftIndex -> LeftWrist
            16,  # 20: RightIndex -> RightWrist
            15,  # 21: LeftThumb -> LeftWrist
            16,  # 22: RightThumb -> RightWrist
            11,  # 23: LeftHip -> LeftShoulder
            12,  # 24: RightHip -> RightShoulder
            23,  # 25: LeftKnee -> LeftHip
            24,  # 26: RightKnee -> RightHip
            25,  # 27: LeftAnkle -> LeftKnee
            26,  # 28: RightAnkle -> RightKnee
            27,  # 29: LeftHeel -> LeftAnkle
            28,  # 30: RightHeel -> RightAnkle
            29,  # 31: LeftFootIndex -> LeftHeel
            30,  # 32: RightFootIndex -> RightHeel
        ]

        super().__init__("MediaPipe33", names, parents)

        # --- Standard Joint Mapping ---
        # MediaPipe does not have central Hip/Pelvis or Spine joints.
        self.hips = None
        self.spine_low = None
        self.spine_mid = None
        self.spine_high = None
        self.neck = None

        # Nose is the closest approximation to Head
        self.head = MediaPipe33Joints.Nose

        # Arm mappings: No Clavicle in MediaPipe
        self.l_clavicle = None
        self.l_shoulder = MediaPipe33Joints.LeftShoulder
        self.l_elbow = MediaPipe33Joints.LeftElbow
        self.l_wrist = MediaPipe33Joints.LeftWrist

        self.r_clavicle = None
        self.r_shoulder = MediaPipe33Joints.RightShoulder
        self.r_elbow = MediaPipe33Joints.RightElbow
        self.r_wrist = MediaPipe33Joints.RightWrist

        # Leg mappings
        self.l_hip = MediaPipe33Joints.LeftHip
        self.l_knee = MediaPipe33Joints.LeftKnee
        self.l_ankle = MediaPipe33Joints.LeftAnkle
        self.l_foot = MediaPipe33Joints.LeftFootIndex

        self.r_hip = MediaPipe33Joints.RightHip
        self.r_knee = MediaPipe33Joints.RightKnee
        self.r_ankle = MediaPipe33Joints.RightAnkle
        self.r_foot = MediaPipe33Joints.RightFootIndex
