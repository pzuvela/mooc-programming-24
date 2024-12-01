
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000


_string = (
    f"my name is {name}, I am {age} years old\n"
    f"\n"
    f"my skills are\n"
    f" - {skill1} ({level1})\n"
    f" - {skill2} ({level2})\n"
    f" - {skill3} ({level3})\n"
    f"\n"
    f"I am looking for a job with a salary of {lower}-{upper} euros per month"
)

print(_string)
