from typing import Optional
from odmantic import Field, Model


class Person(Model):
    name: str
    age: int = Field(ge=0)
    email: Optional[str] = None