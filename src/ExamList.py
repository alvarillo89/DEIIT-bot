from DataWrapper import DataWrapper

class ExamList:
    def __init__(self, subject_name, exams, data_wrapper):
        self.data_wrapper = data_wrapper
        
        if not subject_name in self.data_wrapper.subjects:
            raise ValueError("Unknown subject")
        
        self.subject_name = subject_name
        self.exams = exams

    def get_message_list(self):
        msg = "Examenes de la asignatura " + self.subject_name + "\n\n"

        for key in self.exams.keys():
            msg += "* {}: {}\n".format(key, self.exams[key])

        return msg