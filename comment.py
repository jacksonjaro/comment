#! python3
# commenting.py - a multi-clipbord.

TEXT = {

'excellent': """I appreciate and applaud your hard work so far in this course. Congratulations on arriving at a final draft. You should be proud. Overall this is an excellent academic essay.""",

'successful': """I appreciate and applaud your hard work so far in this course. Congratulations on arriving at a final draft. You should be proud. Overall this is a successful academic essay.""",

'adequate': """I appreciate and applaud your hard work so far in this course. Congratulations on arriving at a final draft. You should be proud. Overall this is an adequate academic essay.""",


'good theory': """One well executed aspect of your project is the critical thinking of your theory. The project’s prompt is very broad, so answering it critically in a arguable, specific way is always a challenge. You appear to answer the question of "Why has the US been slow to take climate action" with <describe theory>""",

'good reasoning': """One well executed aspect of your project is the good reasoning that connects your evidence with the assertions you make. Using reasoning to connect strong evidence to an assertion makes ones essay so much stronger. One example of this is when you support your thesis with the assertions <describe assertions> and the evidence <describe evidence>. I like <describe connective tissue>""",

'good evidence': """One well executed aspect of your project is the good evidence that supports your thesis. It’s clear you’re following along with the readings. Using strong evidence is an excellent first step to writing an argumentative persuasive paper. You use <describe evidence>. """,

'good transitions': """One well executed aspect of your project is your transition statements and "pink house" statements (recall Shelley Reid.) Making an argument that sounds compelling in your head is one thing, and helping the reader follow along with that argument is another. <example>""",

'good counterargument': """I really like your counterargument. Using a persuasive counterargument can show the reader that you are a reasonable, credible source and that your essay takes other perspectives into account. You use the counterargument <>""",
	

'improve theory': """One aspect of your project on which you can improve is your overarching theory. <describe theory>""",

'improve reasoning': """One aspect of your project on which you can improve is your reasoning that connects your theory to your evidence. Remember you are trying to use a good mix of "cherries" and "jello" to make you point (recall Shelly Reid on Perusall.) For example when you use <evidence> I’m a little lost as to the connection to <assertion>""",

'improve evidence': """One aspect of your project on which you can improve is your evidence that supports your thesis statement. Remember you are trying to use a good mix of "cherries" and "jello" to make you point (recall Shelly Reid on Perusall.) <describe evidence>""",

'improve transitions': """One aspect of your project on which you can improve is your transition statements and "pink house" statements (recall Shelley Reid.) Making an argument that sounds compelling in your head is one thing, and helping the reader follow along with that argument is another. <example>""",

'improve counterargument': """One aspect of your project on which you can improve is your counterargument.  Using a persuasive counterargument can show the reader that you are a reasonable, credible source and that your essay takes other perspectives into account. <describe problem with counterargument>"""

	}

import sys,pyperclip

if len(sys.argv) < 2:
	print('Usage: py comment.py [keyphrase] - copy phrase text')
	sys.exit()
	


keyphrases = sys.argv[1:4] #first three command line arg is keyphrase
copy_lst = []
for keyphrase in keyphrases:
	if keyphrase in TEXT:
		copy_lst.append(TEXT[keyphrase])
		print('Text for ' + keyphrase + ' copied to clipboard.')
	else:
		print('there is no text for ' + keyphrase)
temp = "\n".join(copy_lst)
pyperclip.copy(temp)