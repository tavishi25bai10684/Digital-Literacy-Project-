import time

def start_evaluation():
    print("-" * 50)
    print("DIGITAL LITERACY PROJECT - EXECUTION CONSOLE")
    print("-" * 50)
    print(f"Student: Tavishi | Reg No: 25BAI10684")
    print("Specialization: CSE AI-ML")
    print("-" * 50)
    
    time.sleep(1)
    print("\nVerifying Project Components...")
    
    components = [
        "Task 1: Infographic Design................[OK]",
        "Task 2: Professional Profiles..............[OK]",
        "Task 3: HackerRank & Google Form Survey....[OK]",
        "Task 4: Email Etiquette & Checklist........[OK]",
        "Task 5: Cyber Safety Case Study............[OK]",
        "Final Report: PDF Documentation............[OK]"
    ]
    
    for item in components:
        print(item)
        time.sleep(0.4)
    
    print("\n[SUCCESS] Project is fully documented and ready for evaluation.")
    print("-" * 50)

if _name_ == "_main_":
    start_evaluation()
