class Projetc:
    def __init__(self):
        print("Project class: instances")
    def create_project(self,param):
        print("ProjectClass: CreateProject" %param)
    def edit_project(self,project_id, body):
        print("ProjectClass: EditProject: $s, $s" % (project_id, body))