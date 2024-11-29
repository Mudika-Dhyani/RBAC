from rbac.users import Users
from rbac.roles import Roles
from rbac.resources import Resources


class AccessControl(Users, Roles, Resources):
    """
    Manages allow and deny rules for access control.
    Supports operations such as granting or revoking permissions 
    based on action levels (READ, WRITE, DELETE).
    """

    def __init__(self):
        super().__init__()
        # Define supported action types
        self.supported_actions = ['READ', 'WRITE', 'DELETE']
        self.permission_grants = {}
        self.permission_rejects = {}

    def grant_permission(self, role, action, resource_list=None):
        """
        Add a rule to allow access to specific resources for a given role.
        """
        if resource_list is None:
            resource_list = []

        # Validate the role and action
        if role not in self.roles:
            raise ValueError(f"Invalid role: {role}")
        if action.upper() not in self.supported_actions:
            raise ValueError(f"Invalid action type: {action}")

        # Grant permissions for each resource
        for resource in resource_list:
            if resource not in self.resources:
                raise ValueError(f"Invalid resource: {resource}")
            self.permission_grants[(role, action.upper(), resource)] = True

    def revoke_permission(self, role, action, resource_list=None):
        """
        Add a rule to deny access to specific resources for a given role.
        """
        if resource_list is None:
            resource_list = []

        # Validate the role and action
        if role not in self.roles:
            raise ValueError(f"Invalid role: {role}")
        if action.upper() not in self.supported_actions:
            raise ValueError(f"Invalid action type: {action}")

        # Deny permissions for each resource
        for resource in resource_list:
            if resource not in self.resources:
                raise ValueError(f"Invalid resource: {resource}")
            self.permission_rejects[(role, action.upper(), resource)] = True
