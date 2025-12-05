from typing import Dict
from .definition import SkeletonDefinition

from .definitions.optitrack import Optitrack
from .definitions.xsens import Xsens

from .generate_skeleton_def import generate_skeleton_def


SKELETON_REGISTRY: Dict[str, SkeletonDefinition] = {
    "optitrack": Optitrack(),
    "xsens": Xsens(),   
}

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
    "get_skeleton_def",
    "SKELETON_REGISTRY"
]
