class CandidateProfile:
    def __init__(self,name,email,score):
        # Create a public name attribute
        # Create a Protected email attribute
        # Create a private score attribute
        self.name = name
        self._email = email
        self.__score = score

    def get_email(self):
         # Return the Protected email
         return self._email

    def get_score(self):
         # Return the private score
         return self.__score

name = input().strip()
email = input().strip()
score = (int(input()))

# Create one CandidateProfile object
candidate = CandidateProfile(name,email,score)

# Print the name directly
# Print the email using get_email()
# print the score using get_Score()
print("CANDIDATE PROFILE")
print(f"Name: {candidate.name}")
print(f"Email: {candidate.get_email()}")
print(f"Score: {candidate.get_score()}")