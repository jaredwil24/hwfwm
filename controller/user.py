from fastapi import APIRouter
import strawberry
from api.api import Query
from strawberry.asgi import GraphQL
user = APIRouter()
schema = strawberry.Schema(Query)
graphql_app = GraphQL(schema)
user.add_route('/graphql', graphql_app)
