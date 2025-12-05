from dataclasses import dataclass
from typing import List, Optional, Set, Tuple
from anytree import Node, RenderTree


@dataclass
class SkeletonDefinition:
    name: str
    original_names: List[str]
    parents: List[int]  # -1 for root

    # --- Standard Interface (Defined Once for Autocomplete) ---
    # We initialize them to None so they are optional    
    hips: Optional[int] = None
    spine_low: Optional[int] = None
    spine_mid: Optional[int] = None
    spine_high: Optional[int] = None
    neck: Optional[int] = None
    head: Optional[int] = None

    l_clavicle: Optional[int] = None
    l_shoulder: Optional[int] = None
    l_elbow: Optional[int] = None
    l_wrist: Optional[int] = None

    r_clavicle: Optional[int] = None
    r_shoulder: Optional[int] = None
    r_elbow: Optional[int] = None
    r_wrist: Optional[int] = None

    l_hip: Optional[int] = None
    l_knee: Optional[int] = None
    l_ankle: Optional[int] = None
    l_foot: Optional[int] = None

    r_hip: Optional[int] = None
    r_knee: Optional[int] = None
    r_ankle: Optional[int] = None
    r_foot: Optional[int] = None

    def get_ordered_indices(self) -> List[int]:
        # We explicitly list the order we want
        candidates = [
            self.hips, self.spine_low, self.spine_mid, self.spine_high, 
            self.neck, self.head,
            self.l_clavicle, self.l_shoulder, self.l_elbow, self.l_wrist,
            self.r_clavicle, self.r_shoulder, self.r_elbow, self.r_wrist,
            self.l_hip, self.l_knee, self.l_ankle, self.l_foot,
            self.r_hip, self.r_knee, self.r_ankle, self.r_foot
        ]
        
        # Filter out the None values
        return [idx for idx in candidates if idx is not None]


    def get_name(self, index: int) -> str:
        return self.original_names[index]

    @property
    def bones(self) -> Set[Tuple[int, int]]:
        """
        Returns the bone hierarchy as a set of (start_index, end_index) pairs.
        Useful for drawing. Derived from the parents list.
        """
        return {
            (parent_idx, child_idx)
            for child_idx, parent_idx in enumerate(self.parents)
            if parent_idx != -1
        }

    def to_anytree(self) -> List[Node]:
        """Builds an anytree representation of the skeleton."""
        nodes = [Node(self.get_name(i)) for i in range(len(self.original_names))]
        for i, parent_idx in enumerate(self.parents):
            if parent_idx != -1:
                nodes[i].parent = nodes[parent_idx]
        return [node for node in nodes if node.is_root]

    def _get_hierarchy_string(self) -> str:
        """Renders the skeleton hierarchy to a string using anytree."""
        output = ""
        roots = self.to_anytree()
        for root in roots:
            for pre, _, node in RenderTree(root):
                output += f"{pre}{node.name}\n"
        return output

    def __repr__(self) -> str:
        """Prints a visual representation of the skeleton hierarchy."""
        return f"SkeletonDefinition(name='{self.name}')\n{self._get_hierarchy_string()}"
