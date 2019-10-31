import pytest
import sys
sys.path.append('../src')

from ExamList import ExamList


sample_exams = {
        "CAL": "https://url1.com",
        "IA": "https://url2.com",
        "IV": "https://url3.com",
        "SCD": "https://url4.com",
    }

result = """Examenes de la asignatura IV

* CAL: https://url1.com
* IA: https://url2.com
* IV: https://url3.com
* SCD: https://url4.com
"""

def test_exception():
    sample_wrong_subject = "NAT"

    with pytest.raises(ValueError):
        exam_list = ExamList(sample_wrong_subject, sample_exams)


def test_message():
    sample_subject = "IV"
    exam_list = ExamList(sample_subject, sample_exams)

    assert exam_list.get_message_list() == result