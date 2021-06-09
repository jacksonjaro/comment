# comment.py
A quick productivity script to cut down on repetitive typing while commenting on student essays. It's a multi copy-paste script where you can have a "repository" of structural parts of a comment (with things commonly given as feedback), and it would allow you to get a skeleton comment quickly which you could fill in in with specifics. So I have it set up with building blocks relating to project #1 final draft. Usage is on the command line. An example comment might be 

python comment.py "excellent" "good evidence" "improve counterargument"

That would give the following on the clipboard that you couldpaste into a text editor and edit -- especially the parts with the <brackets>

I appreciate and applaud your hard work so far in this course. Congratulations on arriving at a final draft. You should be proud. Overall this is an excellent academic essay.
One well executed aspect of your project is the good evidence that supports your thesis. It’s clear you’re following along with the readings. Using strong evidence is an excellent first step to writing an argumentative persuasive paper. You use <describe evidence>. 
One aspect of your project on which you can improve is your counterargument.  Using a persuasive counterargument can show the reader that you are a reasonable, credible source and that your essay takes other perspectives into account. <describe problem with counterargument>

I adapted a similar program from "automate the boring stuff with python," Chapter 6: "Project: Multi-Clipboard Automatic Messages"
