class User:
    def __init__(self,email,name,password,job_title):
      self.email = email
      self.name = name
      self.password = password
      self.job_title = job_title

    def change_password(self , new_password):
        self.password = new_password
    
    
    def change_job_title(self , new_job_title):
        self.job_title = new_job_title
    
    def get_user_info(self):
          print(f"User {self.name} is cuurently working as {self.job_title} and reachable at {self.email}") 

app_user_one = User("houimliraed@outlook.fr","raed","testing","software engineer")

app_user_one.get_user_info()

app_user_one.change_job_title("devops engineer")

app_user_one.get_user_info()