from datetime import datetime, date

class PersonalAssistant:
    def __init__(self, assistant_name="Round"):
        self.name = assistant_name
        self.user_name = None
        self.tasks = {}
        self.task_counter = 1
        self.calendar = {}

    def add_task(self, title, description=None, priority="Medium", due_date=None, category=None):
        if priority not in ["High", "Medium", "Low"]:
            priority = "Medium"
            
        task_due_date = None
        if due_date:
            try:
                task_due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD. Due date set to None.")
                
        task = {
            "title": title,
            "description": description,
            "priority": priority,
            "due_date": task_due_date,
            "category": category,
            "status": "Not Started",
            "created_date": date.today(),
            "completed_date": None
        }
        
        self.tasks[self.task_counter] = task
        task_id = self.task_counter
        self.task_counter += 1
        
        print(f"\nTask added successfully!")
        print(f"Task ID: {task_id}")
        print(f"Title: {title}")
        print(f"Priority: {priority}")
        if task_due_date:
            print(f"Due Date: {task_due_date}")
            
        return task_id
    def update_task_status(self, task_id, new_status):
        valid_statuses = ["Not Started", "In Progress", "Completed"]
        
        if task_id not in self.tasks:
            print(f"Task ID {task_id} not found.")
            return False
            
        if new_status not in valid_statuses:
            print(f"Invalid status. Please use: {', '.join(valid_statuses)}")
            return False
            
        self.tasks[task_id]["status"] = new_status
        if new_status == "Completed":
            self.tasks[task_id]["completed_date"] = date.today()
            
        print(f"Task {task_id} status updated to: {new_status}")
        return True
    
    def list_tasks(self, status=None, priority=None, category=None):
        if not self.tasks:
            print("\nNo tasks currently scheduled.")
            return
            
        print("\nCurrent Tasks:")
        print("-" * 50)
        
        for task_id, task in self.tasks.items():
            if status and task["status"] != status:
                continue
            if priority and task["priority"] != priority:
                continue
            if category and task["category"] != category:
                continue
                
            print(f"\nTask ID: {task_id}")
            print(f"Title: {task['title']}")
            if task["description"]:
                print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print(f"Priority: {task['priority']}")
            if task["due_date"]:
                print(f"Due Date: {task['due_date']}")
            if task["category"]:
                print(f"Category: {task['category']}")
                
            print("-" * 30)