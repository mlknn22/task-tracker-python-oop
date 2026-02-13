from .task_base import Task

class BugTask(Task):
    def __init__(self, title, priority, severity, deadline = None):
        super().__init__(title, priority, deadline)
        self.severity = severity

    def cost(self):
        return self.priority * self.severity


class FeatureTask(Task):
    def __init__(self, title, priority, story_points, deadline = None):
        super().__init__(title, priority, deadline)
        self.story_points = story_points


    def cost(self):
        return self.priority * self.story_points


class ChoreTask(Task):
    def __init__(self, title, priority, minutes, deadline = None):
        super().__init__(title, priority, deadline)
        self.minutes = minutes


    def cost(self):
        return self.minutes // 30 + (1 if self.minutes % 30 else 0) * self.priority


if __name__ == "__main__":
    tasks = [
        BugTask("Fix login", 3, 2),
        FeatureTask("Add profile page", 2, 5),
        ChoreTask("Clean repo", 4, 45),
    ]
    for t in tasks:
        print(t)
