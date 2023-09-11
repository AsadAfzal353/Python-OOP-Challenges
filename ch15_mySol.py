
from collections.abc import Sequence

class JobApplicant:
    
    def __init__(self, applicant_id, years_experience, is_recommended, first_interview_score, second_interview_score):
        self.applicant_id = applicant_id
        self.years_experience = years_experience
        self.is_recommended = is_recommended
        self.first_interview_score = first_interview_score
        self.second_interview_score = second_interview_score
        self.score = (self.years_experience/2 + self.first_interview_score/2 + \
                     self.second_interview_score + (1 if self.is_recommended else 0))
        
class JobApplicantPool(Sequence):
    
    def __init__(self, *args):
        self.applicants = [*args]
        print(self.applicants)

    def add(self, item):
        self.applicants.append(item)
        return 
    
    def __repr__(self):
        newlist = sorted([(applicant.score, applicant.applicant_id) for applicant in self.applicants], key=lambda x:x[0], reverse=True)
        footer = ''.join([f"{i} - {j} \n" for i, j in newlist])

        return f"Applicant Pool\n (Score | ID)\n-------------------\n\t\n{footer}"
            
    def __len__(self):
        return len(self.applicants)
    
    def __getitem__(self, key):
        if type(key) == slice:
            return self.__class__(*self.applicants[key])


if __name__ == "__main__":

    ja1 = JobApplicant(applicant_id="1234", years_experience=2, is_recommended=True, first_interview_score=2.2, second_interview_score=3.1)
    ja2 = JobApplicant("6937", 12, False, 1.2, 9.4)

    jab = JobApplicantPool()

    isinstance(jab, Sequence)

    jab.add(ja1)
    jab.add(ja2)

    jab