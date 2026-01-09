from enum import IntEnum
from ..definition import SkeletonDefinition


class Coco17Joints(IntEnum):
    Nose = 0
    LeftEye = 1
    RightEye = 2
    LeftEar = 3
    RightEar = 4
    LeftShoulder = 5
    RightShoulder = 6
    LeftElbow = 7
    RightElbow = 8
    LeftWrist = 9
    RightWrist = 10
    LeftHip = 11
    RightHip = 12
    LeftKnee = 13
    RightKnee = 14
    LeftAnkle = 15
    RightAnkle = 16


class Coco17(SkeletonDefinition):
    def __init__(self):
        # The joint names from the COCO dataset.
        names = [j.name for j in Coco17Joints]

        # The parent index for each joint. -1 for root.
        # Topology assumption: Nose is root. 
        # Eyes/Shoulders -> Nose. Ears -> Eyes. 
        # Hips -> Shoulders (Torso connection).
        parents = [
            -1,  # Nose (Root)
             0,  # LeftEye -> Nose
             0,  # RightEye -> Nose
             1,  # LeftEar -> LeftEye
             2,  # RightEar -> RightEye
             0,  # LeftShoulder -> Nose
             0,  # RightShoulder -> Nose
             5,  # LeftElbow -> LeftShoulder
             6,  # RightElbow -> RightShoulder
             7,  # LeftWrist -> LeftElbow
             8,  # RightWrist -> RightElbow
             5,  # LeftHip -> LeftShoulder
             6,  # RightHip -> RightShoulder
            11,  # LeftKnee -> LeftHip
            12,  # RightKnee -> RightHip
            13,  # LeftAnkle -> LeftKnee
            14   # RightAnkle -> RightKnee
        ]

        super().__init__("Coco17", names, parents)

        # --- Standard Joint Mapping ---
        # Edit these to map your skeleton's joints to the standard set.
        
        # COCO does not have a central Hip/Pelvis or Spine joints.
        self.hips = None
        self.spine_low = None
        self.spine_mid = None
        self.spine_high = None
        self.neck = None
        
        # Nose is the closest approximation to Head
        self.head = Coco17Joints.Nose

        # Arm mappings: COCO Shoulders map directly to shoulder joints.
        # No Clavicle in COCO.
        self.l_clavicle = None
        self.l_shoulder = Coco17Joints.LeftShoulder
        self.l_elbow = Coco17Joints.LeftElbow
        self.l_wrist = Coco17Joints.LeftWrist

        self.r_clavicle = None
        self.r_shoulder = Coco17Joints.RightShoulder
        self.r_elbow = Coco17Joints.RightElbow
        self.r_wrist = Coco17Joints.RightWrist

        # Leg mappings: COCO Hips map directly to hip joints.
        self.l_hip = Coco17Joints.LeftHip
        self.l_knee = Coco17Joints.LeftKnee
        self.l_ankle = Coco17Joints.LeftAnkle
        self.l_foot = None  # No toe/foot base

        self.r_hip = Coco17Joints.RightHip
        self.r_knee = Coco17Joints.RightKnee
        self.r_ankle = Coco17Joints.RightAnkle
        self.r_foot = None


