[1mdiff --git a/game.py b/game.py[m
[1mindex 8dc25b8..e7e1c4f 100644[m
[1m--- a/game.py[m
[1m+++ b/game.py[m
[36m@@ -4,6 +4,10 @@[m [mprint("If you wish to quit type 'quit' into the console")[m
 while True:[m
     player_choice = input("Please enter your choice from rock, paper or scissors. ")[m
 [m
[32m+[m[32m    if player_choice.lower() == "quit" or player_choice.lower() == "q":[m
[32m+[m[32m      print("Thank you so much for playing our game")[m
[32m+[m[32m      break[m
[32m+[m
     if player_choice.lower() == "rock" or player_choice.lower() == "r":[m
         print('Chosen rock')[m
 [m
[36m@@ -14,11 +18,8 @@[m [mwhile True:[m
         print('Chosen scissors')[m
 [m
     else:[m
[31m-        print('please choose a valid input')        [m
[31m-[m
[31m-    if player_choice.lower() == "quit" or player_choice.lower() == "q":[m
[31m-      print("Thank you so much for playing our game")[m
[31m-      break[m
[32m+[m[32m        print('please choose a valid input')[m[41m  [m
[32m+[m[32m        continue[m[41m      [m
 [m
     computer_choice = random.randint(1,3)[m
     if computer_choice == 1:[m
