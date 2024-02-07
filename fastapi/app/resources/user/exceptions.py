class DuplicateUsernameError(Exception):
    def __init__(self , username , status_code ):
        self.status_code = status_code
        self.message = f"username {username} already exists, please try another."


class UserNotFound(Exception):
    def __init__(self , username ):
        self.status_code = 404
        self.message = f"username {username} does not exist, please try another."        


class CredentialError(Exception):
    def __init__(self ):
        self.status_code = 401
        self.message = "unauthorized"    
