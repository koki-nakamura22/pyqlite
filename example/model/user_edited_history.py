from dataclasses import dataclass, field
from typing import ClassVar, Final, List, Optional

from example.model import BaseModel


@dataclass(init=True, eq=True, frozen=True)
class UserEditedHistory(BaseModel):
    datetime: str
    note: Optional[str] = None
    table_name: ClassVar[str] = 'user_edited_histories'
    pks: ClassVar[List[str]] = []