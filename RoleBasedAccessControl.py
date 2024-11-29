from rbac.acl import Registry

# Define access levels for each role
ACCESS_LEVELS = {
    'super-admin': ['READ', 'WRITE', 'DELETE'],
    'admin': ['READ', 'WRITE'],
    'non-admin': ['READ']
}

# Resources (Currently, only one resource: 'file')
RESOURCES = ['file']


class RoleBasedAccessControl:
    """
    Implements the Role-Based Access Control (RBAC) system.
    The system should be able to assign roles to users, remove users from roles, 
    and check if a user has access to a resource based on their assigned role.
    """

    def __init__(self):
        # Initialize the Access Control List (ACL)
        self.acl = Registry()

    def define_roles(self):
        """Defines and adds roles with their respective access levels."""
        # Adding roles with predefined access levels (READ, WRITE, DELETE)
        for role, permissions in ACCESS_LEVELS.items():
            self.acl.addRole(role, permissions)

    def define_resources(self):
        """Adds resources to the system (currently only 'file')."""
        for resource in RESOURCES:
            self.acl.addResource(resource)

    def set_allowed_permissions(self):
        """Sets allowed permissions based on role access levels."""
        for role, permissions in ACCESS_LEVELS.items():
            for permission in permissions:
                self.acl.allow(role, permission, RESOURCES)

    def set_denied_permissions(self):
        """Sets denied permissions based on the super-admin role's access."""
        for role, permissions in ACCESS_LEVELS.items():
            # Deny permissions that super-admin has but other roles don't
            for permission in ACCESS_LEVELS['super-admin']:
                if permission not in permissions:
                    self.acl.deny(role, permission, RESOURCES)

    def add_users_with_roles(self):
        """Adds users to the system with their corresponding roles."""
        self.acl.addUser('hrishi', ['non-admin', 'admin'])
        self.acl.addUser('user', ['super-admin'])

    def execute_permission_checks(self):
        """Checks if users have permission for specific actions on resources."""
        # Check access before role removal
        self.acl.isAllowed('hrishi', 'READ', 'file')
        self.acl.isAllowed('hrishi', 'WRITE', 'file')

        # Remove a role from a user
        self.acl.deleteRole('hrishi', 'admin')

        # Check access after role removal
        self.acl.isAllowed('hrishi', 'READ', 'file')
        self.acl.isAllowed('hrishi', 'WRITE', 'file')


if __name__ == "__main__":
    # Initialize RBAC system
    rbac_system = RoleBasedAccessControl()
    rbac_system.define_roles()
    rbac_system.define_resources()
    rbac_system.set_allowed_permissions()
    rbac_system.set_denied_permissions()
    rbac_system.add_users_with_roles()
    rbac_system.execute_permission_checks()
