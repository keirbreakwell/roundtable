class PersonalAssistant:
    def __init__(self, assistant_name="Round"):
        self.name = assistant_name
        self.user_name = None
        self.tasks = []
        self.calendar = {}
        
    def introduce_self(self):
        introduction = f"""
Hello! I'm {self.name}, your AI Personal Assistant at Roundtable.
I'm here to help manage your tasks, calendar, and communications.
        """
        print(introduction)
        
    def get_user_details(self):
        print("\nLet's get to know each other better!")
        self.user_name = input("What should I call you? ")
        print(f"\nThank you, {self.user_name}! I've stored your name in my memory.")
        
    def add_task(self, task_description):
        self.tasks.append(task_description)
        print(f"\nI've added the task: {task_description}")
        print(f"Current task count: {len(self.tasks)}")

    def list_tasks(self):
        if not self.tasks:
            print("\nNo tasks currently scheduled.")
            return
            
        print("\nCurrent Tasks:")
        for index, task in enumerate(self.tasks, 1):
            print(f"{index}. {task}")