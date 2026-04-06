"""
users.py
--------
Implement the class hierarchy for platform users.

Classes to implement:
  - User (base class)
    - FreeUser
    - PremiumUser
    - FamilyAccountUser
    - FamilyMember
"""
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class FreeUser(User): pass
class PremiumUser(User): pass
class FamilyMember(User):
    def __init__(self, user_id, name, age):
        super().__init__(user_id, name)
        self.age = age
