# comment.py
A quick productivity script to cut down on repetitive typing while commenting on student essays. It's a multi copy-paste script where you can have a "repository" of structural parts of a comment (with things commonly given as feedback), and it would allow you to get a skeleton comment quickly which you could fill in in with specifics. So I have it set up with building blocks relating to my blocaks of feedback I gave my students for project #1 final draft. Usage is on the command line, either terminal on mac or powershell on Windows. An example comment might be 

	python comment.py "excellent" "good evidence" "improve counterargument"

That would give the following on the clipboard that you could paste into a text editor and edit -- especially the parts with the {brackets}

	I appreciate and applaud your hard work so far in this course. Congratulations on arriving at a final draft. You should be proud. Overall this is an excellent academic essay. 
	One well executed aspect of your project is the good evidence that supports your thesis. It’s clear you’re following along with the readings. Using strong evidence is an excellent first step to writing an argumentative persuasive paper. You use {describe evidence}. 
	One aspect of your project on which you can improve is your counterargument.  Using a persuasive counterargument can show the reader that you are a reasonable, credible source and that your essay takes other perspectives into account. {describe problem with counterargument}


You can edit the variable "TEXT" to include you own blocks of feedback with your own handles. So if you give feedback under the umbrella of "good introduction for audience." Basically when you edit text it would have to have this formatting

	TEXT{
	"handle1": """ text feedback1 """,
	"handle2": """ text feedback2 """,
	"handle3": """ text feedback3 """
	}
	
Then you could call your handle on the command line like this

	python comment.py "handle1" "handle2" "handle3"

and that would give you

	text feedback1
	text feedback2
	text feedback3


I adapted a similar program from "automate the boring stuff with python," Chapter 6: "Project: Multi-Clipboard Automatic Messages"
