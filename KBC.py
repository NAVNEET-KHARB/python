questions = ["President of India is : A) Draupadi Murmu B) Narendra Modi C) Rahul Gandhi D) Jagdeep Dhankhar",
             "ICC Men's CWC 2023 will be played in : A) Pakistan B) India + Bangladesh C) India D) Usa", "India first won the CWC in : A) 1971 B) 2011 C) 2007 D) 1983"]
answers = ["A", "C", "D"]
amount = 0
for i in range(0, len(questions)):
    print(questions[i])
    answer = input("Enter your answer")
    if (answer == answers[i]):
        amount += 5000
        print("Correct Answer. You've won Rs.", amount)
    else:
        print("Wrong Answer. Your journey ends with Rs.", amount)
