# redblacktree
Red Black Tree Demo

### Fun with Red Black Trees

This file sets up a red black binary search tree and then runs through several demos of inserting nodes. 

To run simply go to the the directory with the file and run
```
python redBlackTree.py
```
All of the demo cases will run automatically.

### How you can play with it:
Call setup_nodes_demo with a different list of elements and see the resulting trees. Don't forget to print_tree to see results.
Call node_insert_demo with a different list of elements to see how the tree gets built element by element. 


### Ideas for future work:
I implemented print_tree method that looks at the tree and uses log calculations to determine the spacing between elements 
at the different levels of the tree. For example if you are using utilizing 32 spaces for printing each line, then 1st level should have 
16 spaces on each side whcih is 32/2^1 =  16. On the second level you would want 8 spaces on each side which is 32/2^2 = 8 and on the third level you
would want 32/2^3=4 spaces between etc. 

I was intrigued by the idea of printing mathematical structures such as these and I wonder what some tweaking could accomplish here either
for printing larger trees or adding more meta information such as connecting lines between the elements.
