from dataclasses import dataclass, field
from typing import List, Optional
from enums import (
    MuscleGroup,
    EquipmentType,
    MechanicsType,
    ForceType,
    LevelType,
    CategoryType,
    MajorMuscleGroup,
)


@dataclass
class ExerciseDefinition:
    id: str
    display_name: str
    level: LevelType
    category: CategoryType

    muscle_group: MuscleGroup
    major_muscle_group: Optional[MajorMuscleGroup] = None
    
    force: Optional[ForceType] = None
    mechanics_type: Optional[MechanicsType] = None
    equipment_type: Optional[EquipmentType] = None
    
    secondary_muscles: List[MuscleGroup] = field(default_factory=list)
    instructions: str =""
    images: List[str] = field(default_factory=list)

