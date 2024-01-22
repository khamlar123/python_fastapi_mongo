def user_user(user) -> dict:
    return{
        "id": str(user["_id"]),
        "userName": user["userName"],
        "name": user["name"],
        "password": user["password"],
        "status": user["status"],
        "roles":role_list(user.get("roles")) 
    }

def list_users(users) -> list:
    return [user_user(user) for user in users]

def role_role(role) -> dict:
    return{
        "name": role["name"], 
        "url": role["url"],
        "icon": role["icon"],
    }

def role_list(roles) -> dict:
    return [role_role(role) for role in roles]