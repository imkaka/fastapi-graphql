import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from .schema import Mutation, Query

app = FastAPI()

app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation)))


@app.get("/")
async def ping():
    return {
        "ping": "pong!"
    }
