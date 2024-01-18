def user_user(user) -> dict:
    return{
        "id": str(user["_id"]),
        "userName": user["userName"],
        "name": user["name"],
        "password": user["password"],
        "status": user["status"],
    }

def list_users(users) -> list:
    return [user_user(user) for user in users]