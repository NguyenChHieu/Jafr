This application helps multiple users manage their tasks and meetings on a Unix-like OS (a popular choice of OS in industry where developers might share a computer system or host web applications).

Jafr is designed to run whenever a user opens their terminal at the beginning of their day. Users can choose to view reminders that are relevant to the current day, or make changes. Changes can include sharing reminders with other users.

There are two kinds of reminders: tasks and meetings.

**SETUP**

Jafr runs when jafr.py is executed by the Python interpreter. There is one command line argument which will contain a path (absolute or relative) to a given passwd file. More on this below.

_For example_
python3 jafr.py passwd
Jafr first displays relevant reminders (tasks followed by meetings), before showing a menu. The menu contains the following.

What would you like to do?
1. Complete tasks
2. Add a new meeting.
3. Share a task.
4. Share a meeting.
5. Change Jafr's master directory.
6. Exit

A user chooses one option only.

<menu num>
This invokes the relevant behaviour, described below. If the user enters 6, Jafr exits. After completing a behaviour, Jafr returns to the menu.

_For example_

Just a friendly reminder! You have these tasks to finish today.
- Read INFO1112 A1 specs
- Fix bug 1 inside Jafr
- Study ELEC1601

These tasks need to be finished in the next three days!
- Shower by 03/08/23
- Organise paul's brithday by 03/08/23

You have the following meetings today!
- Michael Mai's welcome party at 18:00
- Resume writing workshop at 09:00
- Jafr dev meeting at 13:30

You have the following meetings scheduled over the next week!
- Barbenheimer marathon on 06/08/23 at 17:00
- Academic advice on 02/08/23 at 14:30
- ELEC1601 group meeting on 03/08/23 at 11:00

What would you like to do?
1. Complete tasks
2. Add a new meeting.
3. Share a task.
4. Share a meeting.
5. Change Jafr's master directory.
6. Exit

**Displaying tasks**

Jafr will write two views of tasks to standard output. The first is a view of all tasks that are due today that have not been completed. The second is a view of all tasks that are due in the upcoming three days that have not been completed.

_For example_

Just a friendly reminder! You have these tasks to finish today.
- Fix bug 1 inside Jafr
- Study ELEC1601
These tasks need to be finished in the next three days!
- Shower by 03/08/23
- Organise paul's birthday by 04/08/23

**Displaying meetings**

Jafr will write two views of meetings to standard output. The first is a view of all events that are scheduled today. The second is a view of all events that are scheduled in the upcoming 7 days.

_For example_

You have the following meetings today!
- Michael Mai's welcome party at 18:00
- Resume writing workshop at 09:00
- Jafr dev meeting at 13:30
You have the following meetings scheduled over the next week!
- Barbenheimer marathon on 06/08/23 at 17:00
- Academic advice on 02/08/23 at 14:30
- ELEC1601 group meeting on 03/08/23 at 11:00

**Changing the user's master directory**

Jafr allows the user to change their chosen master directory.

Jafr will ask:

"Which directory would you like Jafr to use?"

The user enters an absolute path.

_<absolute path>_

Jafr then writes a confirmation message to standard output.

_Master directory changed to <absolute path>._

**Completing tasks**

Jafr allows the user to mark tasks as completed. The user is first prompted for which task they would like to complete. All not complete tasks are shown and numbered, in the order they appear in tasks.md.
