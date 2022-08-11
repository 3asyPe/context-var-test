from contextvars import ContextVar
from fastapi import FastAPI
import asyncio


app = FastAPI()


class Trace:
    def __init__(self):
        self.var = ContextVar("var")

    def a(self):
        self.var.set("a")

    def b(self):
        self.var.set("b")

    @property
    def value(self):
        return self.var.get()


TRACE = Trace()


@app.get("/a")
async def a():
    while True:
        TRACE.a()
        await asyncio.sleep(1)
        print(f"a={TRACE.value}")


@app.get("/b")
async def hello():
    while True:
        TRACE.b()
        await asyncio.sleep(0.5)
        print(f"b={TRACE.value}")
