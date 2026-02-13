from tracker.manager import TaskManager
from tracker.tasks import BugTask, FeatureTask, ChoreTask


def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: please enter an integer.")


def read_int_in_range(prompt, min_val, max_val):
    while True:
        value = read_int(prompt)
        if min_val <= value <= max_val:
            return value
        print(f"Error: value must be between {min_val} and {max_val}.")


def choose_project(manager):
    name = input("Enter project name: ").strip()
    try:
        return manager.create_project(name)
    except ValueError as e:
        print(e)
        return None


def add_task_to_project(project):
    if project is None:
        print("Please select or create a project first.")
        return

    print("\nTask type:")
    print("1) Bug")
    print("2) Feature")
    print("3) Chore")
    task_type = read_int_in_range("Choose type (1-3): ", 1, 3)

    title = input("Task title: ").strip()
    if not title:
        print("Error: title cannot be empty.")
        return

    priority = read_int_in_range("Priority (1-5): ", 1, 5)

    deadline_raw = read_int("Deadline (number, 0 = no deadline): ")
    deadline = None if deadline_raw == 0 else deadline_raw

    try:
        if task_type == 1:
            severity = read_int_in_range("Severity (1-3): ", 1, 3)
            task = BugTask(title, priority, severity, deadline)
        elif task_type == 2:
            story_points = read_int_in_range("Story points (1-13): ", 1, 13)
            task = FeatureTask(title, priority, story_points, deadline)
        else:
            minutes = read_int_in_range("Minutes (1-10000): ", 1, 10000)
            task = ChoreTask(title, priority, minutes, deadline)

        project.add_task(task)
        print("Task added:", task)
        print("Cost:", task.cost())
    except Exception as e:
        print("Error while creating task:", e)


def list_tasks(project):
    if project is None:
        print("Please select or create a project first.")
        return

    print("\nStatus filter:")
    print("0) All")
    print("1) todo")
    print("2) in_progress")
    print("3) done")
    choice = read_int_in_range("Choose (0-3): ", 0, 3)

    status = None
    if choice == 1:
        status = "todo"
    elif choice == 2:
        status = "in_progress"
    elif choice == 3:
        status = "done"

    try:
        if status is None:
            project.list_tasks()
        else:
            project.list_tasks(status=status)
    except TypeError:
        project.list_tasks()


def start_task(project):
    if project is None:
        print("Please select or create a project first.")
        return

    task_id = read_int("Enter task id: ")
    task = project.find_task(task_id)
    if task is None:
        print("Task not found.")
        return

    task.start()
    print("Task started:", task)


def finish_task(project):
    if project is None:
        print("Please select or create a project first.")
        return

    task_id = read_int("Enter task id: ")
    task = project.find_task(task_id)
    if task is None:
        print("Task not found.")
        return

    task.finish()
    print("Task completed:", task)


def project_stats(project):
    if project is None:
        print("Please select or create a project first.")
        return

    s = project.stats()
    print("\nProject statistics:", project.name)
    print("todo:", s["todo"])
    print("in_progress:", s["in_progress"])
    print("done:", s["done"])
    print("total_cost:", s["total_cost"])


def global_stats(manager: TaskManager):
    s = manager.global_stats()
    print("\nGlobal statistics")
    print("todo:", s["todo"])
    print("in_progress:", s["in_progress"])
    print("done:", s["done"])
    print("total_cost:", s["total_cost"])

def remove_task(project):
    if project is None:
        print("Please select or create a project first.")
        return

    task_id = read_int("Enter task id to remove: ")
    removed = project.remove_task(task_id)

    if removed:
        print("Task removed.")
    else:
        print("Task not found.")


def remove_project(manager, current_project):
    name = input("Enter project name to remove: ").strip()
    if not name:
        print("Error: project name cannot be empty.")
        return current_project

    removed = manager.remove_project(name)
    if removed:
        print("Project removed.")
        if current_project and current_project.name == name:
            current_project = None
    else:
        print("Project not found.")

    return current_project


def main():
    manager = TaskManager()
    current_project = None

    while True:
        print("\n===== TASK TRACKER =====")
        print("Current project:", current_project.name if current_project else "(not selected)")
        print("1) Create/select project")
        print("2) Show projects")
        print("3) Add task to current project")
        print("4) Show tasks in current project")
        print("5) Start task (by id)")
        print("6) Complete task (by id)")
        print("7) Current project statistics")
        print("8) Global statistics")
        print("9) Remove task (by id) from current project")
        print("10) Remove project (by name)")
        print("0) Exit")

        cmd = read_int_in_range("Choose command: ", 0, 10)

        if cmd == 0:
            print("Goodbye!")
            break
        elif cmd == 1:
            proj = choose_project(manager)
            if proj is not None:
                current_project = proj
                print("Selected project:", current_project.name)
        elif cmd == 2:
            names = manager.list_projects()
            if not names:
                print("No projects yet.")
            else:
                print("Projects:")
                for n in names:
                    print("-", n)
        elif cmd == 3:
            add_task_to_project(current_project)
        elif cmd == 4:
            list_tasks(current_project)
        elif cmd == 5:
            start_task(current_project)
        elif cmd == 6:
            finish_task(current_project)
        elif cmd == 7:
            project_stats(current_project)
        elif cmd == 8:
            global_stats(manager)
        elif cmd == 9:
            remove_task(current_project)
        elif cmd == 10:
            current_project = remove_project(manager, current_project)


if __name__ == "__main__":
    main()
