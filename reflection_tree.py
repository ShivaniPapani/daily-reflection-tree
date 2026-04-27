def daily_reflection():

    print("Daily Reflection System")
    print("----------------------")

    goal = input("Did you complete your main goal today? (yes/no): ")

    if goal.lower() == "yes":

        success = input(
            "What helped you succeed? (planning/focus/support): "
        )

        print("\nInsight:")
        print("Great work! Try to repeat this strategy tomorrow.")

    elif goal.lower() == "no":

        reason = input(
            "What prevented you from completing the task? (time/distraction/clarity): "
        )

        print("\nSuggestion:")

        if reason == "time":
            print("Use time blocking to allocate focused work periods.")

        elif reason == "distraction":
            print("Try reducing distractions such as phone notifications.")

        elif reason == "clarity":
            print("Break the task into smaller manageable steps.")

        else:
            print("Reflect on the main obstacle and plan ahead.")

    improvement = input(
        "\nWhat is one improvement you will apply tomorrow? "
    )

    print("\nReflection saved. Keep improving!")

daily_reflection()
