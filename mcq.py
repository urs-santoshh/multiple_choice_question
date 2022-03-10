print("Welcome to MCQ  program in python")

questions_prompt = ["Who is known as the father of Computer science?\n(a) Charles Babbage\n(b) Pascal\n(c) Archimedes\n",
"What is the main part of a computer?\n(a) CPU\n(b) Mouse\n(c) Keyboard\n",
"Who is the first programmer?\n(a) Ada Lovlace\n(b) John Napier\n(c) Newton\n"
]

class MCQ:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer

    
questions = [
    MCQ(questions_prompt[0],"a"),
MCQ(questions_prompt[1],"a"),
MCQ(questions_prompt[2],"a")
]


def run_mcq(questions):
    score = 0
    for question in questions:
        ans = input(question.prompt)
        if ans == question.answer:
            score +=1
    print(f"Your score is {score}/{len(questions)}")
run_mcq(questions)



    