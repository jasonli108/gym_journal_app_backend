from dataclasses import dataclass
from typing import Optional
from backend.src.enums import MuscleGroup, EquipmentType, MechanicsType, MyCustomGroup


@dataclass
class ExerciseDefinition:
    id: str
    display_name: str
    muscle_group: MuscleGroup
    url: Optional[str] = None
    is_popular: bool = False
    equipment_type: Optional[EquipmentType] = None
    mechanics_type: Optional[MechanicsType] = None
    my_custom_group: Optional[MyCustomGroup] = None
