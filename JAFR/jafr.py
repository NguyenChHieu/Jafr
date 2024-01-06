import os
import sys
import json
from _datetime import datetime, timedelta

FULL_DIRECTORY = "~/.jafr/user-settings.json"
FULL_DIRECTORY_OS = os.path.expanduser(FULL_DIRECTORY)
# Read data from json file.


def read_user_data():
    full_data_directory = FULL_DIRECTORY
    full_data_directory = os.path.expanduser(full_data_directory)

    try:
        with open(full_data_directory, "r") as settings:
            user_settings = json.load(settings)
            return user_settings
    # Debugging
    except FileNotFoundError:
        print("User settings file not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding json. file")


# Parse tasks_file
def implement_task(master_directory):
    task_path = os.path.join(master_directory, "tasks.md")
    # Define tasks lines as list:
    tasks_list = []

    try:  # error handling
        with open(task_path, 'r') as file_task:
            tasks_lines = file_task.readlines()  # read lines in task.md
            for line in tasks_lines:  # loop through the file to search for tasks.(error handling)
                if line.lstrip().startswith("-"):  # allow indentation in the line
                    tasks_list.append(line.strip())
    except FileNotFoundError:
        exit("Missing tasks.md or meetings.md file.")
    return tasks_list


# Parse meetings_file
def implement_meeting(master_directory):
    meeting_path = os.path.join(master_directory, "meetings.md")
    meetings_list = []
    try:  # error handling
        with open(meeting_path, 'r') as file_meeting:
            meetings_lines = file_meeting.readlines()
            for line in meetings_lines:
                if line.lstrip().startswith("-"):  # allow indentation in the line
                    meetings_list.append(line.strip())
    except FileNotFoundError:
        exit("Missing tasks.md or meetings.md file.")
    return meetings_list


def is_date_valid(date_str, format_str):
    try:
        datetime.strptime(date_str, format_str)
        return True
    except ValueError:
        return False


# Display tasks and meetings
def print_reminders(tasks_list, meetings_list):
    today = datetime.today().date()  # instantiate the date today

    # Print today tasks on terminal
    print("Just a friendly reminder! You have these tasks to finish today.")
    # Find the tasks in the file and make them in a list.
    task_today = []
    for task_line in tasks_list:
        if "Due: " in task_line and "not complete" in task_line:
            task_today.append(task_line)
    # Loop through the lines (indexes)
    for line_in_task in task_today:
        description_str = line_in_task.split("Due: ")[0].strip()  # Extract the description
        date_str = line_in_task.split("Due: ")[1].split()[0]  # Find the time in every task
        if is_date_valid(date_str, "%d/%m/%y"):
            date_formatted = datetime.strptime(date_str, "%d/%m/%y").date()  # Format the date to datetime
            if date_formatted == today:  # check whether the task is today, if yes -> print.
                print(description_str)  # print the formatted task
            else:
                continue

    # Print tasks in upcoming 3 days
    print("\nThese tasks need to be finished in the next three days!")

    task_3days = []
    for task_line in tasks_list:
        if "Due: " in task_line and "not complete" in task_line:
            task_3days.append(task_line)
    for line_in_task in task_3days:
        des_str = line_in_task.split("Due: ")[0].strip()
        date_str = line_in_task.split("Due: ")[1].split()[0]
        if is_date_valid(date_str, "%d/%m/%y"):
            date_formatted = datetime.strptime(date_str, "%d/%m/%y").date()
            if today < date_formatted <= today + timedelta(days=3):  # identify the tasks in following 3 days
                print(des_str, "by", date_str)
        else:
            continue

    # Print today meetings:
    print("\nYou have the following meetings today!")
    # Find meetings and put in a list.
    meetings_today = []
    for meeting_line in meetings_list:
        if "Scheduled: " in meeting_line:
            meetings_today.append(meeting_line)
    for meeting_line in meetings_today:
        des_str = meeting_line.split("Scheduled: ")[0].strip()
        date_str = meeting_line.split("Scheduled: ")[1].split()[1]
        time_str = meeting_line.split("Scheduled: ")[1].split()[0]
        if is_date_valid(time_str, "%H:%M") and is_date_valid(date_str, "%d/%m/%y"):
            date_formatted = datetime.strptime(date_str, "%d/%m/%y").date()
            if date_formatted == today:
                print(des_str, "at", time_str)
            else:
                continue

    # Meetings 7 days:
    print("\nYou have the following meetings scheduled over the next week!")
    meetings_7days = []
    for meeting_line in meetings_list:
        if "Scheduled: " in meeting_line:
            meetings_7days.append(meeting_line)
    for meeting in meetings_7days:
        des_str = meeting.split("Scheduled: ")[0].strip()
        time_str = meeting.split("Scheduled: ")[1].split()[0]
        date_str = meeting.split("Scheduled: ")[1].split()[1]
        if is_date_valid(time_str, "%H:%M") and is_date_valid(date_str, "%d/%m/%y"):
            date_formatted = datetime.strptime(date_str, "%d/%m/%y").date()
            if today < date_formatted <= today + timedelta(days=7):
                print(des_str, "on", date_str, "at", time_str)
            else:
                continue
    print()


def change_directory():
    print("Which directory would you like Jafr to use?")
    new_absolute_path = input()  # ask the input of the user
    user_settings = read_user_data()
    user_settings["master"] = new_absolute_path  # change the value assigned to "master" key

    with open(FULL_DIRECTORY_OS, "w") as settings_file:
        json.dump(user_settings, settings_file)  # write the path into the "user_settings" dictionary

    print(f"Master directory changed to {new_absolute_path}.")


def complete_task(master_directory):

    # Read tasks from tasks.md
    task_path_file = os.path.join(master_directory, 'tasks.md')
    with open(task_path_file, 'r') as tasks_file:
        all_task_uncompleted = tasks_file.readlines()

    # Sort the uncompleted task
    uncompleted_tasks = []
    for task in all_task_uncompleted:
        if 'not complete' in task:
            if 'Due: ' in task:
                uncompleted_tasks.append(task)

    # Check if uncompleted_tasks list is empty or not
    if len(uncompleted_tasks) >= 1:
        print('Which task(s) would you like to mark as completed?')
        # Display tasks
        for index, task in enumerate(uncompleted_tasks, start=1):
            task_des = task.split('Due: ')[0].strip().split('- ')[1]
            date_str = task.split("Due: ")[1].split()[0]
            print(f"{index}. {task_des} by {date_str}")

        # loop created to prompt the user if they entered invalid value
        while True:
            # User input
            tasks_user = input()

            tasks_user_processed = []
            invalid_indices = []  # for debugging purpose

            # Split the input by spaces and process each index
            for index in tasks_user.split():
                stripped_index = index.strip()
                if stripped_index.isdigit():
                    # make the index 0-based
                    processed_index = int(stripped_index) - 1
                    if 0 <= processed_index < len(uncompleted_tasks):
                        tasks_user_processed.append(processed_index)
                    else:
                        invalid_indices.append(index)
                else:
                    invalid_indices.append(index)

            if not invalid_indices:  # No invalid indices found
                # Update the chosen task(s)
                for index in tasks_user_processed:
                    task = uncompleted_tasks[index]
                    task = task.replace('not complete', 'complete')
                    # Find the correct index of the chosen task in the file
                    found_index = all_task_uncompleted.index(uncompleted_tasks[index])
                    # Update the task
                    all_task_uncompleted[found_index] = task

                # Update the file
                with open(task_path_file, 'w') as tasks_file:
                    tasks_file.writelines(all_task_uncompleted)
                print("Marked as complete.")
                break
            else:
                print("Invalid task number(s) entered. Please enter valid task number(s).")
    else:
        print('No tasks to complete!')


def add_meeting(meetings_list, master_directory):

    # Handle invalid description
    print("Please enter a meeting description:")
    while True:
        meeting_des = input()
        # Check the des
        if meeting_des.strip():
            break
        else:
            print("Invalid meeting description.")

    # Handle invalid date
    print("Please enter a date:")
    while True:
        date_from_user = input()
        try:
            # Try parse the date
            datetime.strptime(date_from_user, "%d/%m/%y").date()
            break
        except ValueError:
            print("Invalid date format. (example: 20/08/23)")

    # Handle invalid time
    print("Please enter a time:")
    while True:
        time_from_user = input()
        try:
            # Try parse the time
            datetime.strptime(time_from_user, "%H:%M")
            break  # Exit the loop if the time is valid
        except ValueError:
            print("Invalid time format")

    # prompt
    meeting_addition = f"- {meeting_des} Scheduled: {time_from_user} {date_from_user}\n"

    # append to the meeting list
    meetings_list.append(meeting_addition)

    # construct the path
    task_file_path = os.path.join(master_directory, "meetings.md")

    # update the meeting to the file
    with open(task_file_path, "a") as meeting_file:
        meeting_file.write("\n##### added by you\n")
        meeting_file.write(meeting_addition)
    print(f"Ok, I have added {meeting_des} on {date_from_user} at {time_from_user}.")

    # share
    print("Would you like to share this meeting? [y/n]: ", end="")
    share_meeting_response = input()
    # Share extension
    if share_meeting_response == "y":
        user_dict = read_passwd_file()
        user_dict1 = get_user_home_dir()
        current_username = os.environ.get("USER")

        print("Who would you like to share with?")
        for uid, username in user_dict.items():
            print(f"{uid} {username}")
        # choosing other user
        sharing_others = input().split()

        while not check_valid_input(sharing_others, user_dict):
            print("Invalid input")
            sharing_others = input().split()

        # loop through the selected users from input
        for targeted_user_id in sharing_others:
            # check if the user is in user dict
            if targeted_user_id in user_dict:
                user_home_directory = user_dict1[targeted_user_id]
                user_path = os.path.expanduser(f"{user_home_directory}/.jafr/user-settings.json")

                with open(user_path, "r") as directory:
                    user_dir = json.load(directory)
                    # get user master directory
                    user_master_dir = user_dir.get("master")

                    if user_master_dir:
                        user_task_file_path = os.path.join(user_master_dir, "meetings.md")
                        with open(user_task_file_path, "a") as meeting_file:
                            meeting_file.write("\n##### shared by " + current_username + "\n")
                            meeting_file.write(meeting_addition)

        print(f"Meeting shared.")
    else:
        pass


def read_passwd_file():
    user_dict = {}
    passwd_file_path = sys.argv[1]
    current_username = os.environ.get("USER")

    with open(passwd_file_path, "r") as passwd_file:
        for line in passwd_file:
            parts = line.strip().split(":")
            if len(parts) >= 3:
                user_id = parts[2]
                username = parts[0]
                if username != current_username:
                    user_dict[user_id] = username

    return user_dict


def get_user_home_dir():
    user_dict1 = {}
    passwd_file_path = sys.argv[1]  # Update the path accordingly
    current_username = os.environ.get("USER")

    with open(passwd_file_path, "r") as passwd_file:
        for line in passwd_file:
            parts = line.strip().split(":")
            if len(parts) >= 3:
                user_id = parts[2]
                user_home_dir = parts[5]
                username = parts[0]
                if username != current_username:
                    user_dict1[user_id] = user_home_dir

    return user_dict1


# Debug for share meeting and share task
def check_valid_input(lists, dictionary):
    for item in lists:
        if item not in dictionary:
            return False
    return True


def share_task(tasks_list):
    uncompleted_tasks = []

    for task in tasks_list:
        if "not complete" in task or "complete" in task:
            uncompleted_tasks.append(task)
    # debug
    if not uncompleted_tasks:
        print("No tasks available to share")
        return

    # display task
    print("Which task would you like to share?")
    # The same as printing task above but using enumerate is so much better =)
    valid_task_indices = []
    for index, task in enumerate(uncompleted_tasks, start=1):
        description = task.split("Due: ")[0].strip().lstrip("- ")
        time_task_str = task.split("Due: ")[1].split()[0].strip()
        if is_date_valid(time_task_str, "%d/%m/%y"):
            valid_task_indices.append(index)
            time_task_formatted = datetime.strptime(time_task_str, "%d/%m/%y")
            print(f"{index}. {description} by {time_task_formatted.strftime('%d/%m/%y')}")

    # debug
    if not valid_task_indices:
        print("No valid tasks available to share")
        return

    # user task input + data validation
    while True:
        user_selection = input()
        if user_selection.isdigit():
            # make index 0-started
            selected_task_index = int(user_selection) - 1
            if 0 <= selected_task_index < len(uncompleted_tasks):  # if the index exist
                break
            else:
                print("Invalid task number.")
        else:
            print("Invalid task number")

    # refer to the selected task
    task_selected_share = uncompleted_tasks[selected_task_index]

    # SHARING

    # Get user info from the dictionary
    user_dict = read_passwd_file()
    user_dict1 = get_user_home_dir()
    current_username = os.environ.get("USER")

    print("Who would you like to share with?")
    for uid, username in user_dict.items():
        print(f"{uid} {username}")

    # choosing other user
    sharing_others = input().split()
    
    # check invalid id
    while not check_valid_input(sharing_others, user_dict):
        print("Invalid input")
        sharing_others = input().split()

    # loop through the selected users from input
    for targeted_user_id in sharing_others:
        # check if the user is in user dict
        if targeted_user_id in user_dict:
            user_home_directory = user_dict1[targeted_user_id]
            user_path = os.path.expanduser(f"{user_home_directory}/.jafr/user-settings.json")

            with open(user_path, "r") as directory:
                user_dir = json.load(directory)
                # get user master directory
                user_master_dir = user_dir.get("master")

                if user_master_dir:
                    user_task_file_path = os.path.join(user_master_dir, "tasks.md")
                    with open(user_task_file_path, 'a') as task_file:
                        task_file.write("\n##### shared by " + current_username + "\n")
                        task_file.write(task_selected_share + "\n")

    print(f"Task shared.")


def share_meeting(meetings_list):
    all_meetings = []
    for meeting in meetings_list:
        if "Scheduled: " in meeting:
            all_meetings.append(meeting)

    # debug
    if not all_meetings:
        print("No meetings to share")

    # sort meetings
    print("Which meeting would you like to share?")
    valid_meeting_indices = []
    for index, meeting in enumerate(all_meetings, start=1):
        meeting_des = meeting.split("Scheduled: ")[0].strip().lstrip("- ")
        time_str = meeting.split("Scheduled: ")[1].split()[0]
        date_str = meeting.split("Scheduled: ")[1].split()[1]
        if is_date_valid(time_str, "%H:%M") and is_date_valid(date_str, "%d/%m/%y"):
            valid_meeting_indices.append(index)
            date_formatted = datetime.strptime(date_str, "%d/%m/%y").date()
            time_formatted = datetime.strptime(time_str, "%H:%M")
            print(f"{index}. {meeting_des} on {datetime.strftime(date_formatted,'%d/%m/%y')} "
                  f"at {datetime.strftime(time_formatted,'%H:%M')}")

    if not valid_meeting_indices:
        print("No valid meetings available to share")
        return

    # user input
    while True:
        user_meeting_selection = input()
        if user_meeting_selection.isdigit():
            user_selected_meeting_index = int(user_meeting_selection) - 1
            if 0 <= user_selected_meeting_index < len(valid_meeting_indices):
                break
            else:
                print("Invalid meeting number.")
        else:
            print("Invalid meeting number.")

        # refer to the selected meeting
    selected_meeting_to_share = all_meetings[user_selected_meeting_index]

    # SHARE AGAIN :(

    # Get user info from the dictionary
    user_dict = read_passwd_file()
    user_dict1 = get_user_home_dir()
    current_username = os.environ.get("USER")

    print("Who would you like to share with?")
    for uid, username in user_dict.items():
        print(f"{uid} {username}")
    
    # choosing other user
    sharing_others = input().split()
    # check invalid user
    while not check_valid_input(sharing_others, user_dict):
        print("Invalid input")
        sharing_others = input().split()

    # loop through the selected users from input
    for targeted_user_id in sharing_others:
        # check if the user is in user dict
        if targeted_user_id in user_dict:
            user_home_directory = user_dict1[targeted_user_id]
            user_path = os.path.expanduser(f"{user_home_directory}/.jafr/user-settings.json")

            with open(user_path, "r") as directory:
                user_dir = json.load(directory)
                # get user master directory
                user_master_dir = user_dir.get("master")

                if user_master_dir:
                    user_task_file_path = os.path.join(user_master_dir, "meetings.md")
                    with open(user_task_file_path, "a") as meeting_file:
                        meeting_file.write("\n##### shared by " + current_username + "\n")
                        meeting_file.write(selected_meeting_to_share + "\n")

    print(f"Meeting shared.")


def main():
    # Access the master directory
    user = read_user_data()
    if user:
        master_directory = user.get("master")

        # check master directory exists
        if not os.path.exists(master_directory):
            # print the error in stderr instead of stdout
            print("Jafr's chosen master directory does not exist.", file=sys.stderr)
            exit()

        # Get master directory
        if master_directory:
            parse_tasks = implement_task(master_directory)
            parse_meetings = implement_meeting(master_directory)
            print_reminders(parse_tasks, parse_meetings)

            # print menu:
            while True:
                print("What would you like to do?\n"
                        "1. Complete tasks\n"
                        "2. Add a new meeting.\n"
                        "3. Share a task.\n"
                        "4. Share a meeting.\n"
                        "5. Change Jafr's master directory.\n"
                        "6. Exit")

                user_input = input()

                # Complete task
                if user_input == "1":
                    complete_task(master_directory)
                # Add and share meeting
                elif user_input == "2":
                    add_meeting(parse_meetings, master_directory)
                # Share task
                elif user_input == "3":
                    share_task(parse_tasks)
                # Share meeting
                elif user_input == "4":
                    share_meeting(parse_meetings)
                # Change directory
                elif user_input == "5":
                    change_directory()
                # Exit
                elif user_input == "6":
                    exit()
                else:
                    exit()


if __name__ == '__main__':
    main()
