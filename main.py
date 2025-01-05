from personal_assistant import PersonalAssistant
from datetime import date, timedelta

def main():
    assistant = PersonalAssistant()
    assistant.introduce_self()
    assistant.get_user_details()
    
    print("\nLet me help you manage your tasks more effectively!")
    
    tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
    next_week = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")
    
    assistant.add_task(
        title="Complete project setup",
        description="Finish setting up development environment and basic structure",
        priority="High",
        due_date=tomorrow,
        category="Setup"
    )
    
    assistant.add_task(
        title="Learn Python basics",
        description="Study core Python concepts and practice coding",
        priority="Medium",
        due_date=next_week,
        category="Learning"
    )
    
    assistant.update_task_status(1, "In Progress")
    
    assistant.list_tasks()
    
    print("\nHigh Priority Tasks:")
    assistant.list_tasks(priority="High")

if __name__ == "__main__":
    main()