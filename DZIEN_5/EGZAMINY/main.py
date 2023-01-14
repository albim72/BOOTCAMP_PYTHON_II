from homework import Homework
from exam import OldExam
from grade import Exam
from specialgrade import NewExam

jurek = Homework()
jurek.grade = 94

assert jurek.grade == 94

st = OldExam()
st.writing_grade = 80
st.math_grade = 76

assert st.writing_grade == 80
assert st.math_grade == 76

print("__________egzaminy: pierwszy i drugi________")

first_exam = Exam()
first_exam.writing_grade = 82
first_exam.science_grade = 76
first_exam.math_grade = 56

print("___________egazmin pierwszy________")
print(f'Pisanie -> ocena: {first_exam.writing_grade}')
print(f'Nauka -> ocena: {first_exam.science_grade}')
print(f'Matematyka -> ocena: {first_exam.math_grade}')

print("___________egazmin drugi________")
second_exam = Exam()
second_exam.writing_grade = 77
second_exam.science_grade = 71
second_exam.math_grade = 59
print(f'Nauka -> ocena z drugiego egazminu: {second_exam.science_grade}')
print(f'Nauka -> ocena z pierwszego egazminu: {first_exam.science_grade} -> błąd!!!')

print("________ grade -> wersja poprawiona______________")

first_exam = NewExam()
first_exam.writing_grade = 88
second_exam = NewExam()
second_exam.writing_grade = 70

print(f'Pisanie -> ocena z pierwszego egazminu: {first_exam.writing_grade}')
print(f'Pisanie -> ocena z drugiego egazminu: {second_exam.writing_grade}')
