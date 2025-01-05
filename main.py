from personal_assistant import PersonalAssistant

def main():
    assistant = PersonalAssistant()
    assistant.introduce_self()
    assistant.get_user_details()
    
    print("\nLet me help you manage some tasks!")
    assistant.add_task("Set up development environment")
    assistant.add_task("Learn Python basics")
    assistant.list_tasks()
    
    print("\nThank you for working with Roundtable! We're ready to start building more features.")

if __name__ == "__main__":
    main()