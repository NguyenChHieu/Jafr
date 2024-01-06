# Tests notes

**SUPER IMPORTANT - the file was worked locally so in order to make the verifying works, I just have
to delete the excessive part "/Users/nguyenhung/Downloads" in the user-settings.json of every user
in order to make it work on Ed.**


  **#1: About general**
  - If the verify process did not work out, I think we have to export the HOME and USER for every user to test.
  - I place the .bashrc (for test users) in the /tests dir
  - I placed jafr.py at /Users/nguyenhung/Downloads/home in my computer
  - Also, the cmd line to start jafr.py in my computer is:
  python3 /Users/nguyenhung/Downloads/home/jafr.py /Users/nguyenhung/Downloads/home/tests/passwd
                absolute path to jafr.py                    absolute path to passwd
  

  - **#2: About the tests**

  - I've created 4 new different users in the /tests dir
  - All of them are tested locally in my computer.
  - They are tested on 30/08/2023, and the tests are put inside each user's file correspondingly.
    - The new passwd file has been rewritten, including 4 new users(the bold part of path is after removing the local part)
      - chieu - master dir: "dzai" - /Users/nguyenhung/Downloads **/home/tests/chieu/dzai**
      - chihieu - master dir: "dzaivcl" - /Users/nguyenhung/Downloads **/home/tests/chihieu/dzaivcl**
      - newuser - master dir: "masterdir" - /Users/nguyenhung/Downloads **/home/tests/newuser/masterdir**
      -anotheruser - master dir: "masterdir" - /Users/nguyenhung/Downloads **/home/tests/newuser/master**
  
  - **The tests for every user:**
  
  - **Display tasks and meetings (testing user: "chieu")**
  - this user will have meetings.md and task.md inside the directory "dzai"

    + tests:
      - **test1**: check the display of the task and meetings, and in both .md files 
      I've included some "notadate" or "notatime" in the task and meetings to test the
      error handling function.
    
  - **Complete task (testing user: "chihieu" and "anotheruser")**
  - "chihieu" user will have meetings.md and task.md inside the directory "dzaivcl"
  - "anotheruser" user will have meetings.md and task.md inside the directory "master"

    + tests:
      - **test2**: check the normal function of complete_task, and picking
      2 uncompleted tasks to mark complete.
      - **test3**: check the debugging function of complete_task user enter invalid num(s)
      - **test3.1** - using testing user "anotheruser" - check the function "No task to complete" when all task are finished
  
  - **Add meeting (testing user: "newuser")**
    - this user will have meetings.md and task.md inside the directory "masterdir"
    - simce I add all the meetings in these 4 tests the same format "- Hello on 31/08/23 at 11:30" so there's 3 duplications of this meeting :P
      - **test4**: check the normal function of add meeting.
      - **test5**: check the debug for invalid description case.
      - **test6**: check the debug for invalid date case.
      - **test7**: check the debug for invalid time case.

          
