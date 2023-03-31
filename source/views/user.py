from models.user import User, UserUpdate, UserFilter
from services.user import UserService
from uuid import UUID

def UserView():
    async def get(request):
        return "Cool"

    async def post(request):
        return "Post Hello world"

    async def patch(request):
        return "Patch Hello world"

    async def delete(request):
        return "Delete Hello world"

