"""@dataclass auto-generates __init__, __repr__, and __eq__ for simple
data-holding classes - no more writing that boilerplate by hand."""

from dataclasses import dataclass, field

@dataclass
class Task:
    title: str
    done: bool = False
    tags: list = field(default_factory=list)   # mutable defaults need field()

t1 = Task("Write README")
t2 = Task("Write README")
t1.tags.append("docs")

print(t1)             # auto-generated __repr__
print(t1 == t2)        # auto-generated __eq__ (compares by value, not identity)

@dataclass(frozen=True)
class Point:
    x: float
    y: float

p = Point(1, 2)
try:
    p.x = 99   # frozen=True makes instances immutable
except Exception as e:
    print(f"can't mutate frozen dataclass: {type(e).__name__}")
