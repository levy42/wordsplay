from ReMineder.models import User


def register_user(user):
    user_obj = User(name=user.name, password=user.password)

def delete_user(id):
    pass

def edit_user(id):
    pass


user = User(name="vitaliy", password="pass")