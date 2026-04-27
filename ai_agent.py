# Simple AI Reflection Agent

def ai_reflection():

    print("AI Reflection Assistant")
    print("-----------------------")

    reflection = input("Write a short reflection about your day: ")

    print("\nAI Suggestion:")

    if "tired" in reflection.lower():
        print("Consider taking short breaks to maintain productivity.")

    elif "distraction" in reflection.lower():
        print("Try a focused work technique like Pomodoro.")

    elif "delay" in reflection.lower():
        print("Start tasks with the smallest possible step.")

    else:
        print("Stay consistent and review your goals daily.")


ai_reflection()
