**Role-Based Access Control (RBAC)**

**Problem Statement**
Implement a Role-Based Authentication and Authorization (RBAC) system that:

**Assigns roles to users.**
Allows or denies access to resources based on user roles.
Supports multiple roles for a single user.
Can check if a user has permission to perform a certain action on a resource.

**Entities in the System:**
USER: Represents a system user.
ACTION TYPE: Defines the access levels (e.g., READ, WRITE, DELETE).
RESOURCE: The entity that users are trying to access (e.g., "file").
ROLES: Define the access permissions (e.g., non-admin, admin, super-admin).
Access Control:
Access to resources is controlled by user roles.
A user can have multiple roles, and each role has specific permissions.
The system should check whether the user has access to a resource based on their roles and the action type.

**Assumptions:**
There is only one system resource: file.
Roles and Permissions:
non-admin: READ access to file.
admin: READ and WRITE access to file.
super-admin: READ, WRITE, and DELETE access to file.
