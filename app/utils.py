from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    """Returns the hash of the password"""

    return password_context.hash(password)

def verify(plain_password: str, hashed_password: str):
    """
    Verifies that the password given by the user matches the 
    hashed password stored in the database.
    """

    return password_context.verify(plain_password, hashed_password )