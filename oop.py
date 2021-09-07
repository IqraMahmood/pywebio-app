# A simple script to calculate BMI
import pywebio
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server


class SafetyTemplate:

    def investigation_manager(self):
        put_markdown('# **Investigation Manager**')
        self.manager_name = input('What is the Name of manager\n')
        login = input('What is the login of manager \n')
        return put_text('Name of manager is ', self.manager_name, 'and login of manager is ', login)

    def shift(self):
        put_markdown('# **Shift**')
        shift = input('What is the shift code\n')
        return put_text('Shift code is ', shift)

    def department(self):
        put_markdown('# **Department**')
        dep = input('What is the department\n')
        return put_text('Department is ', dep)

    def initial(self):
        put_markdown('# **Initial**')
        injury_date = input('When did the injury occur (date)\n')
        self.time_of_incident = input('What was time (describe in AM or PM)\n')
        self.pain_area = input('What was area of pain\n')
        return put_text(
            'On {}, at approximately {}, on site AM was informed in-person of the associate having pain in the {}  ,{} were called to investigate the issue'.format(
                injury_date, self.time_of_incident, self.pain_area, self.manager_name))

    def Location(self):
        put_markdown('# **Location**')

        self.station = input('At which location accident occurs? write station No')
        if self.station == None:
            put_text('NA')
        else:
            put_text('It occurs at{}'.format(self.station))

    def first_aid(self):
        put_markdown('# **First Aid**')
        self.pain_level = input('Pain level (out of 10)\n')
        put_text(self.pain_level)
        self.pain_level_after_first_aid = input('After offering first aid Did pain depreciate?\n')
        put_text(self.pain_level_after_first_aid)
        # self.z = ''

        if self.pain_level_after_first_aid == 'yes':
            self.x = input('What is the pain level now?\n')
            put_text(self.x)
            self.z = 'pain level depreciated to level {} '.format(self.x)
        else:
            self.z = 'pain did not depreciate'

        put_text(
            'At the time of the report, associate reported pain level of {} out of 10. After offering first aid {}'.format(
                self.pain_level, self.z))

        put_text('At around {}, {} was working on {} and felt pain in {}, {},  .'.format(self.time_of_incident,
                                                                                         self.name_of_employee,
                                                                                         self.project, self.pain_area,
                                                                                         self.y))
        put_text('{} finished shift in routine function of {} within restrictions outlined below {}'.format(
            self.name_of_employee, self.now_project, self.list_of_res))


if __name__ == '__main__':
    obj = SafetyTemplate()
    pywebio.start_server(obj.investigation_manager, port=55)
    # parser.add_argument("-p", "--port", type=int, default=8080)
    # args = parser.parse_args()

    # start_server(predict, port=args.port)

    # obj = SafetyTemplate()
    obj.investigation_manager()
    obj.shift()
    obj.department()
    obj.initial()
    obj.Location()
    obj.first_aid()

