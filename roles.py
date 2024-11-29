class RoleManager:
    """
    Provides functionalities to add and remove roles.
    """

    def __init__(self):
        super().__init__()
        # Initialize the roles registry
        self.role_permissions = {}

    def add_role(self, role, permissions=None):
        """
        Add a role or assign actions (permissions) to a role.
        """
        if permissions is None:
            raise ValueError("Permissions must be provided for the role.")

        # Validate action types
        for action in permissions:
            if action.upper() not in self.supported_actions:
                raise ValueError(f"Invalid action type: {action}")

        # Add the role to the registry
        if role not in self.role_permissions:
            self.role_permissions[role] = set()

        # Assign permissions to the role
        self.role_permissions[role].update(permissions)

    def remove_role_from_user(self, user, role):
        """
        Remove a specific role from a user.
        """
        # Validate the role exists
        if role not in self.role_permissions:
            raise KeyError(f"Role '{role}' does not exist.")

        # Remove the role from the user
        try:
            self.user_roles[user].remove(role)
        except KeyError:
            print(f"Error: Role '{role}' not found for user '{user}'.")

