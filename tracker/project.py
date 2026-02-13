class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def find_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def list_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        for task in self.tasks:
            print(task)

    def remove_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def stats(self):
        todo = 0
        in_progress = 0
        done = 0
        total_cost = 0

        for task in self.tasks:
            if task.status == "todo":
                todo += 1
            elif task.status == "in_progress":
                in_progress += 1
            elif task.status == "done":
                done += 1

            total_cost += task.cost()

        return {
            "todo": todo,
            "in_progress": in_progress,
            "done": done,
            "total_cost": total_cost
        }

