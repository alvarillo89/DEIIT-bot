import pytest
import sys
sys.path.append('src')
sys.path.append('../src')

from ExamList import ExamList
from DataWrapper import DataWrapperList
from DataWrapperJSON import DataWrapperJSON


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

dw_list = DataWrapperList()
dw_json = DataWrapperJSON()
dw_json.load_subject("../data/subjects.json")

def test_exception():
    sample_wrong_subject = "NAT"

    with pytest.raises(ValueError):
        exam_list = ExamList(sample_wrong_subject, sample_exams, dw_list)


def test_message():
    sample_subject = "IV"
    exam_list = ExamList(sample_subject, sample_exams, dw_list)

    assert exam_list.get_message_list() == result


def test_dependecy_injection():
    sample_subject = "IV"

    exam_list = ExamList(sample_subject, sample_exams, dw_list)
    exam_json = ExamList(sample_subject, sample_exams, dw_json)

    assert exam_json.data_wrapper.subjects == exam_list.data_wrapper.subjects
