from src.pivotal_services.conection import ConnectionPivotal


class Projects:
    def __init__(self):
        self.service = 'projects'
        self.request_pivotal = ConnectionPivotal()

    def create_project(self, name_project):
        return self.request_pivotal.post(self.service, {'name': name_project})
