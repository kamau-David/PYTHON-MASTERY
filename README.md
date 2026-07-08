# Python Mastery: Beginner to Advanced

A hands-on Python curriculum covering core language fundamentals, backend/API
development, and data & AI — the same three tracks you'd need to go from
"knows Python syntax" to "can ship a backend service with a data/ML layer."

## Structure

Each module is self-contained: a `README.md` explaining the concept, runnable
code, and (where relevant) a `requirements.txt`. Work through them in order —
later modules assume earlier ones.

### Track 1 — Core Python
| # | Module | Covers |
|---|--------|--------|
| 01 | python-fundamentals | variables, types, operators, control flow |
| 02 | data-structures | lists, dicts, sets, tuples, comprehensions |
| 03 | functions-modules | functions, *args/**kwargs, modules, imports |
| 04 | oop-basics | classes, inheritance, dunder methods |
| 05 | file-io-exceptions | file handling, exceptions, context managers |
| 06 | advanced-oop | dataclasses, ABCs, mixins, properties |
| 07 | functional-decorators | lambda, map/filter/reduce, decorators, generators |
| 08 | testing-debugging | unittest, pytest, logging, debugging |
| 09 | concurrency-async | threading, multiprocessing, asyncio |
| 10 | packaging-project-structure | venv, pip, project layout, building a package |

### Track 2 — Backend & APIs
| # | Module | Covers |
|---|--------|--------|
| 11 | flask-web-basics | routes, templates, request handling |
| 12 | fastapi-rest-apis | FastAPI, Pydantic, CRUD endpoints |
| 13 | databases-sqlalchemy | ORM models, sessions, migrations |
| 14 | auth-security | password hashing, JWT auth, protected routes |

### Track 3 — Data & AI
| # | Module | Covers |
|---|--------|--------|
| 15 | data-analysis-pandas-numpy | arrays, DataFrames, cleaning, aggregation |
| 16 | machine-learning-sklearn | train/test split, regression, classification, evaluation |

### Capstone
| # | Module | Covers |
|---|--------|--------|
| 17 | capstone-fastapi-ml-service | a FastAPI service that serves predictions from a trained sklearn model |

## Setup

Each module with external dependencies has its own `requirements.txt`.
From inside a module folder:

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Modules 01–09 use only the standard library — no install needed, just run
the `.py` files directly.
