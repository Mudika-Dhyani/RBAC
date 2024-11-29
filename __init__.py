#!/usr/bin/python3

# Access Control List.

from rbac.action_type import ActionType


class ACLRegistry(ActionType):
    """
    Registry for managing access control.
    This class verifies whether a user has the necessary permission
    to access a specific resource.
    """

    def __init__(self):
        super().__init__()

    def has_permission(self, user, action, resource):
        """
        Verify access permissions for a user on a resource.

        Returns:
        - False: If access is explicitly denied.
        - True: If access is explicitly allowed.
        - None: If no rule exists for the requested access.
        """

        # Ensure user and resource exist
        assert user and user in self.users, f"Invalid or missing user: {user}"
        assert resource and resource in self.resources, f"Invalid or missing resource: {resource}"

        # Retrieve user's roles
        user_roles = self.users[user]

        # Resolve the most privileged role
        primary_role = None
        if len(user_roles) == 1:
            primary_role = list(user_roles)[0]
        elif len(user_roles) > 1:
            # Prioritize roles based on hierarchy
            for role in user_roles:
                if role in {'super-admin', 'admin'}:
                    primary_role = role
                    break

        # Check for explicit deny rules
        try:
            if self.denied[primary_role, action.upper(), resource]:
                print(f"Access Denied: User '{user}' does not have '{action}' "
                      f"permission for resource '{resource}'.")
                return False
        except KeyError:
            pass

        # Check for explicit allow rules
        try:
            if self.allowed[primary_role, action.upper(), resource]:
                print(f"Access Granted: User '{user}' has '{action}' permission "
                      f"for resource '{resource}'.")
                return True
        except KeyError:
            pass

        # No matching rule found
        print(f"Access Undefined: No rules found for user '{user}' to perform '{action}' "
              f"on resource '{resource}'.")
        return None
