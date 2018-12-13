class Project:
    def __init__(self):
        print("Project Class:: Instance")

    def create_project(self, param):
        print("ProjectClass:: CreateProject::#s"% param)

    def edit_project(self, project_id, body):
        print("ProjectClass::EditProject::%s,%s")

