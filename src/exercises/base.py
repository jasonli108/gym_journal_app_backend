from dataclasses import dataclass
from typing import Optional
from enums import MuscleGroup, EquipmentType, MechanicsType, MyCustomGroup, MajorMuscleGroup


@dataclass
class ExerciseDefinition:
    id: str
    display_name: str
    muscle_group: MuscleGroup
    major_muscle_group: Optional[MajorMuscleGroup] = None
    url: Optional[str] = None
    is_popular: bool = False
    equipment_type: Optional[EquipmentType] = None
    mechanics_type: Optional[MechanicsType] = None
    my_custom_group: Optional[MyCustomGroup] = None
