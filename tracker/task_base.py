import abc

class Task(abc.ABC):
    _next_id = 1

    def __init__(self, title, priority, deadline=None):
        self.task_id = Task._next_id
        Task._next_id += 1

        self.title = title
        self.priority = priority
        self._status = "todo"
        self.deadline = deadline

    def start(self):
        self._status = "in_progress"

    def finish(self):
        self._status = "done"

    def is_overdue(self, current_day):
        if self.deadline is None:
            return False
        return current_day > self.deadline

    @abc.abstractmethod
    def cost(self):
        pass

    @property
    def status(self):
        return self._status

    def __str__(self):
        return f"[#{self.task_id}] {self.title} ({self.status}) cost={self.cost()}"


if __name__ == "__main__":
    print("task_base ok")
