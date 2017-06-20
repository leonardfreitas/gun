import os
import sys
from .messages import Messages
from .sources_views import SourceView
from .spinner import Spinner

class Controller:

    spinner = Spinner()
    #commmands for help
    commands_help = ['help', 'h']
    #list commands for generate
    commands_generate = ['generate', 'g']
    commands_generate_crud = ['crud', 'c']
    commands_generate_crud_one = ['+create', '+update', '+delete', '+list', '+detail']
    commands_generate_model = ['model', 'm']


    @classmethod
    def path(self, path_project):
        self.path = path_project
    @classmethod
    def get_path(self):
        return self.path

    @classmethod
    def get_params_args(self, *args):
        args = list(*args)
        if args[1:]:
            self.filter_base_args(args[1:])
        else:
            print(Menssages.default)
            sys.exit(0)

    @classmethod
    def filter_base_args(self, *args):
        commands = list(*args)
        if commands[0] in self.commands_generate:
            self.filter_action_args(commands[1:])
        elif commands[0] in self.commands_help:
            print(Menssages.help_gun)
            sys.exit(0)

    @classmethod
    def filter_action_args(self, *args):
        commands = list(*args)
        if commands[0] in self.commands_generate_crud:
            self.filter_crud_args(commands[1:])
        if commands[0] in self.commands_generate_crud_one:
            self.filter_class_crud_args(commands)
        elif commands[0] in commands_generate_model:
            pass

    @classmethod
    def filter_crud_args(self, *args):
        commands = list(*args)
        try: app = commands[0]
        except IndexError: sys.exit('\033[31m '+'ERROR! Specify APP to generate crud'+'\033[0;0m')
        with open('%s/%s/views.py'%(self.path, app), 'w') as f:
            self.spinner.start()

            if len(commands)==1:
                f.write(SourceView.get_source_all_class_view())
                feedback = 'GENERATE CRUD IN %s'%app
            elif len(commands)==2:
                f.write(SourceView.get_source_all_class_view(commands[1]))
                feedback = 'GENERATE CRUD IN %s WITH %s MODEL'%(app, commands[1])

            f.close()
            self.spinner.stop()
            sys.exit('\033[32m '+feedback+' \033[0;0m')

    @classmethod
    def filter_class_crud_args(self, *args):
        commands = list(*args)
        model = '<MODEL>'
        for arg in commands:
            if arg.startswith('--'):
                model = arg[2:].split('=')[0]
                app = arg[2:].split('=')[1]
        for param in commands:
            with open('%s/%s/views.py'%(self.path, app), 'a') as f:
                self.spinner.start()
                if param == '+create':
                    f.write(SourceView.get_source_create_class_view(model))
                elif param == '+update':
                    f.write(SourceView.get_source_update_class_view(model))
                elif param == '+delete':
                    f.write(SourceView.get_source_delete_class_view(model))
                elif param == '+list':
                    f.write(SourceView.get_source_list_class_view(model))
                elif param == '+detail':
                    f.write(SourceView.get_source_detail_class_view(model))
                f.close()
                self.spinner.stop()
