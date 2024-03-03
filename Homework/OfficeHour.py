from dataclasses import dataclass

@dataclass
class TeachingAssistant:
    name: str
    location: str
    time: str

def extract_ta_info(tas: list[TeachingAssistant]) -> tuple:
    """
    Convert list of TAs into tuple, for ease of sorting each into
    its respective assignment later.
    """
    ta_info = []
    for ta in tas:
        ta_info.append(f"{ta.name}__{ta.location}__{ta.time}")
    return tuple(ta_info)