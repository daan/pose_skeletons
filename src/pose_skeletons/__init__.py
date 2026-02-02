from typing import Dict, List, Optional
from .definition import SkeletonDefinition

from .definitions.optitrack import Optitrack
from .definitions.xsens import Xsens
from .definitions.mediapipe33 import MediaPipe33
from .definitions.coco17 import Coco17
from .definitions.stereolabs_body18 import StereolabsBody18
from .definitions.stereolabs_body34 import StereolabsBody34

from .generate_skeleton_def import generate_skeleton_def


SKELETON_REGISTRY: Dict[str, SkeletonDefinition] = {
    "optitrack": Optitrack(),
    "xsens": Xsens(),
    "mediapipe33": MediaPipe33(),
    "coco17": Coco17(),
    "stereolabs_body18": StereolabsBody18(),
    "stereolabs_body34": StereolabsBody34(),
}


def detect_skeleton(joint_names: List[str]) -> Optional[str]:
    """
    Auto-detect skeleton type from joint names.

    Args:
        joint_names: List of joint names to match against registered skeletons.

    Returns:
        The skeleton name if an exact match is found, None otherwise.
    """
    joint_set = set(joint_names)

    for name, skeleton in SKELETON_REGISTRY.items():
        if joint_set == set(skeleton.original_names):
            return name

    return None


def get_skeleton_def(name: str) -> SkeletonDefinition:
    """
    Fetches a SkeletonDefinition from the registry by its common name.
    """
    normalized_name = name.lower().strip()
    if normalized_name not in SKELETON_REGISTRY:
        raise ValueError(f"Unknown skeleton definition: '{name}'. "
                         f"Available: {list(SKELETON_REGISTRY.keys())}")
    return SKELETON_REGISTRY[normalized_name]

__all__ = [
    "SkeletonDefinition",
    "detect_skeleton",
    "get_skeleton_def",
    "SKELETON_REGISTRY",
]
