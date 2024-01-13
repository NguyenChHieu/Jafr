**Derived from an assignment 1 - USYD mid year entry 2023**

This application helps multiple users manage their tasks and meetings on a Unix-like OS (a popular choice of OS in industry where developers might share a computer system or host web applications).

Jafr is designed to run whenever a user opens their terminal at the beginning of their day. Users can choose to view reminders that are relevant to the current day, or make changes. Changes can include sharing reminders with other users.

There are two kinds of reminders: tasks and meetings.

**SETUP**

Jafr runs when jafr.py is executed by the Python interpreter. There is one command line argument which will contain a path (absolute or relative) to a given passwd file. 

**Displaying tasks**

Jafr will write two views of tasks to standard output. The first is a view of all tasks that are due today that have not been completed. The second is a view of all tasks that are due in the upcoming three days that have not been completed.

**Changing the user's master directory**

Jafr allows the user to change their chosen master directory.

Jafr will ask:
_"Which directory would you like Jafr to use?"_

The user enters an absolute path.
<absolute path>

Jafr then writes a confirmation message to standard output.
Master directory changed to <absolute path>.

**Completing tasks**

Jafr allows the user to mark tasks as completed. The user is first prompted for which task they would like to complete. All not complete tasks are shown and numbered, in the order they appear in tasks.md.

Which task(s) would you like to mark as completed?
1. <task description> by <due date:DD/MM/YY>
2. <task description> by <due date:DD/MM/YY>
[...]

The user then selects task(s) by their number, separated by whitespace.
_<task num> [<task num> ... <task num>]_

Jafr should modify tasks.md appropriately and write a message to standard output. Tasks inside tasks.md are modified in place (in the same line).
_Marked as complete._

**Adding new meetings**

Jafr allows users to add meetings. The user is first prompted for a meeting description, then a date, then a time.

Please enter a meeting description:
<meeting description>

Please enter a date:
<scheduled date>

Please enter a time:
<scheduled time>

Ok, I have added <meeting description> on <scheduled date> at <scheduled time>.

Jafr should then modify meetings.md appropriately. A meeting is appended to the bottom of meetings.md as follows.

##### added by you

- <meeting>
The user is also prompted to optionally enter people to share the meeting with.

Would you like to share this meeting? [y/n]:
Who would you like to share with?
<user ID> <user name>
<user ID> <user name>
[...]

**Sharing tasks and meetings**

Jafr allows users to share tasks or meetings from their own tasks.md and meetings.md files with other users.
The user is first prompted for which task (or meeting) they would like to share. They are shown all tasks (or meetings) regardless of completion or scheduled date.
