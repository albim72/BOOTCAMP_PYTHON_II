from homework import Homework
from exam import Exam

jurek = Homework()
jurek.grade = 94

assert jurek.grade == 94

st = Exam()
st.writing_grade = 80
st.math_grade = 76

assert st.writing_grade == 80
assert st.math_grade == 76
