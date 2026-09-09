from attr import dataclass


@dataclass
class ColdStartStatus:
    service: str
    message: (
        str | None
    )  # If there is a message then service failed, of None then its good
    is_critical: bool
    completed: bool = False
