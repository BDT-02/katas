class Project:
    def __init__(self):
        print('Project Class:: Instance')


def create_project(param):
        print ('ProjectClass:: CreateProject:: %s' % param)


def edit_project(project_id, body):
        print ('ProjectClass::EditProject::%s, $s' % (project_id, body))



