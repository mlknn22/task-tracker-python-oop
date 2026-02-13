from .project import Project


class TaskManager:
    def __init__(self):
        self.projects = {}

    def create_project(self, name):
        name = name.strip()
        if not name:
            raise ValueError("Project name cannot be empty")

        if name in self.projects:
            return self.projects[name]

        project = Project(name)
        self.projects[name] = project
        return project

    def get_project(self, name):
        return self.projects.get(name)

    def remove_project(self, name):
        if name in self.projects:
            del self.projects[name]
            return True
        return False

    def list_projects(self):
        return list(self.projects.keys())

    def global_stats(self):
        total = {"todo": 0, "in_progress": 0, "done": 0, "total_cost": 0}

        for project in self.projects.values():
            s = project.stats()
            total["todo"] += s["todo"]
            total["in_progress"] += s["in_progress"]
            total["done"] += s["done"]
            total["total_cost"] += s["total_cost"]

        return total
