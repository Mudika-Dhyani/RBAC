class ResourceManager:
    """
    Handles the addition and management of resources.
    """

    def __init__(self):
        # Initialize the resource registry
        self.resource_hierarchy = {}

    def register_resource(self, resource, parent_resources=None):
        """
        Register a resource and optionally associate it with parent resources.
        """
        if parent_resources is None:
            parent_resources = []

        # Add the resource to the registry
        if resource not in self.resource_hierarchy:
            self.resource_hierarchy[resource] = set()

        # Update parent relationships
        self.resource_hierarchy[resource].update(parent_resources)
