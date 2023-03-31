from robyn import Robyn
from views.user import UserView

application = Robyn(__name__)

application.add_view("/user/", UserView)

application.start(url="127.0.0.1", port=8080)
