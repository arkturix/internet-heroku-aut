import io
from invoke import Collection
from . import tests

ns = Collection(tests)

# Top-level tasks
ns.add_task(tests.runtests)