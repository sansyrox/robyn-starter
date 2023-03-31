from models.user import User, UserUpdate, UserFilter
from robyn.router import  Router
from robyn.robyn import Request

from dataclasses import asdict

router = Router()


def UserView():
    async def get(request: Request):
        import services.user
        import uuid
        id = request.queries["id"]
        print(id)
        instance = services.user.UserService().get(uuid.UUID(id))
        return "DB called"

    async def post(request):
        return "Post Hello world"

    async def patch(request):
        return "Patch Hello world"

    async def delete(request):
        return "Delete Hello world"
