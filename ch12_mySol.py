
from enum import Flag, auto
import os

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

class User:
    USER_ROLES = {
        "admin": Permission.READ | Permission.WRITE | Permission.EXECUTE,
        "user": Permission.READ,
        "manager": Permission.READ | Permission.WRITE,
        "support": Permission.EXECUTE,
    }

    def __init__(self, name, user_role):
        self.name = name
        self.user_role = user_role
        self.permissions = self._infer_permission()
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', user_role='{self.user_role}')"
    
    def _infer_permission(self):
        permissions = Permission.READ

        if self.user_role in self.USER_ROLES:
            permissions = self.USER_ROLES.get(self.user_role)
        elif type(self.user_role) == int:
            # try tries to catch an error and if it gets caught except block
            # is executed otherwise else block is executed
            try:
                Permission(self.user_role)
            except ValueError:
                pass
            else:
                permissions = self.user_role
        
        return Permission(permissions)

    def _validate_permission(self, permission):
        if permission not in self.permissions:
            raise PermissionError(f"User does not have {permission.name} permission")
        
    def write(self, file, content):
        self._validate_permission(Permission.WRITE)
        
        with open(file, 'w') as file:
                file.write(content)

    def read(self, file):
        self._validate_permission(Permission.READ)
        if os.path.isfile(file):  # Check if it's a file (not a directory)
            with open(file, 'r') as file:
                return(f'{file.read()}')
        else:
            raise AttributeError("No file of that name exists in the current directory")

    def execute(self, file):
        self._validate_permission(Permission.EXECUTE)
        exec(open(file).read())


if __name__ == "__main__":

    u1 = User(name="Aaron", user_role="user")
    u1 # User(name='Aaron', user_role='user')

    u2 = User("Andrew", "admin")
    u2.permissions # <Permission.EXEC|WRITE|READ: 7>

    u2.write(file="script.py", content="for i in range(10): print(i)")
    u2.execute(file="script.py")
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

    u1.read(file="script.py") # 'for i in range(10): print(i)'

    u1.execute(file="script.py") # PermissionError: User does not have EXEC permission

    u3 = User("Joseph", 6)
    u3.permissions # <Permission.EXEC|WRITE: 6>
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

    u3.execute(file="script.py")

    u1 = User(name="Aaron", user_role="user")
    u1 # User(name='Aaron', user_role='user')

    u2 = User("Andrew", "admin")
    u2.permissions # <Permission.EXEC|WRITE|READ: 7>

    u2.write(file="script.py", content="for i in range(10): print(i)")
    u2.execute()
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

    u1.read(file="script.py") # 'for i in range(10): print(i)'

    u1.execute(file="script.py") # PermissionError: User does not have EXEC permission

    u3 = User("Joseph", 6)
    u3.permissions # <Permission.EXEC|WRITE: 6>

    u3.execute(file="script.py")
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9

