from dataclasses import dataclass
from typing import ClassVar, Final, Optional

from pyqlite.model import BaseModel


@dataclass(init=True, eq=True)
class User(BaseModel):
    id: Final[int]
    name: str
    phone: str
    address: Optional[str] = None
    __table_name: ClassVar[str] = 'users'
