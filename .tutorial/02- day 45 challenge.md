# 👉 Day 45 Challenge

Made it? Good! Let's get cracking.

Your system should:

1. Have a menu that asks if you want to add, view, move or edit a 'to do'.
2. If you choose 'add' then the system should:
   
    1. Prompt you to input what the to do is, when it is due by and the priority (high, medium or low).
    2. Add the 'to do' to the list.
       
4. 'View' should give two options:
    1. View all - shows all 'to dos' with a pretty print.
    2. View priority - allows you to search for high, medium or low priority and **only** see matching tasks.
6. 'Edit' allows you to change any of the information within one of the 'to dos'.
7. 'Remove' lets you completely remove a 'to do' when it is 'to done'.




Example:

```
🌟Life Organizer🌟

Welcome to the life organizer. Do you want to add, view, edit or remove a to do? > Add

What is the task? > Pay teachers more.
When is it due by? > 11/01/2022
What is the priority? >  High

Thanks, this task has been added.

Do you want to see the menu again or quit? > quit.
```

<details> <summary> 💡 Hints </summary>
  
- Use a separate subroutine for add, view, edit, and remove.

- Clear the console before viewing a new entry.

- Use a `while True` loop to call the subroutines and display the menu.


</details>