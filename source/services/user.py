from models.user import User, UserFilter, UserUpdate

from services.crud import CRUDService


class UserService(CRUDService):
    model = User
    update_model = UserUpdate
    filter_model = UserFilter
