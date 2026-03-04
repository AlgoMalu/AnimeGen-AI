from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ShotSpec:
    shot_id: int
    duration: float
    visual_desc: str
    shot_size: str
    story_beat: Optional[str] = ""
    camera_motion: Optional[str] = "Static"
    dialogue: Optional[str] = ""
    must_include: List[str] = field(default_factory=list)
    reference_image_path: Optional[str] = None

@dataclass
class Storyboard:
    title: str
    total_duration: float
    aspect_ratio: str
    style: str
    shots: List[ShotSpec]

@dataclass
class ScoreResult:
    shot_id: int
    candidate_id: str
    sharpness_score: float
    face_detected: bool
    text_alignment: float
    identity_similarity: float
    issues: List[str] = field(default_factory=list)
    total_score: float = 0.0
