
from agents.manager import ask_ai
from agents.planner import create_plan


# ==========================================
# AUTONOMOUS AI SOFTWARE ENGINEER
# ==========================================

def display_banner():

    print("\n" + "=" * 55)
    print("          AUTONOMOUS AI SOFTWARE ENGINEER")
    print("=" * 55)
    print(" AI-powered Software Development Assistant")
    print("=" * 55)


# ==========================================
# 1. MANAGER AGENT
# ==========================================

def manager_agent():

    print("\n--- MANAGER AGENT ---")

    user_input = input("\nEnter your question or requirement: ")

    if not user_input.strip():
        print("Please enter a valid requirement.")
        return

    try:

        print("\nAI Engineer is thinking...")

        response = ask_ai(user_input)

        print("\n--- AI ENGINEER RESPONSE ---")
        print(response)

    except Exception as e:

        print("\nError in Manager Agent:", e)


# ==========================================
# 2. PLANNER AGENT
# ==========================================

def planner_agent():

    print("\n--- PLANNER AGENT ---")

    requirements = input("\nEnter project requirements: ")

    if not requirements.strip():
        print("Please enter valid project requirements.")
        return

    try:

        print("\nPlanner is creating development tasks...")

        plan = create_plan(requirements)

        print("\n--- PROJECT DEVELOPMENT PLAN ---")
        print("=" * 55)
        print(plan)
        print("=" * 55)

    except Exception as e:

        print("\nError in Planner Agent:", e)


# ==========================================
# MAIN APPLICATION
# ==========================================

def main():

    display_banner()

    while True:

        print("\n========== MAIN MENU ==========")

        print("1. Ask AI Software Engineer")
        print("2. Generate Project Development Plan")
        print("3. Exit")

        print("=" * 32)

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            manager_agent()

        elif choice == "2":

            planner_agent()

        elif choice == "3":

            print("\nThank you for using Autonomous AI Software Engineer!")
            print("Application stopped.")
            break

        else:

            print("\nInvalid choice! Please select 1, 2 or 3.")


# ==========================================
# APPLICATION ENTRY POINT
# ==========================================

if __name__ == "__main__":

    main()
