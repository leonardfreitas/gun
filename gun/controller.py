import os
import sys
from .messages import Menssages
from .sources_views import SourceView

class Controller:

    #commmands for help
    commands_help = ['help', 'h']
    #list commands for generate
    commands_generate = ['generate', 'g']
    commands_generate_crud = ['crud', 'c']
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
        elif commands[0] in commands_generate_model:
            pass

    @classmethod
    def filter_crud_args(self, *args):
        commands = list(*args)
        try: app = commands[0]
        except IndexError: sys.exit('Especifique a APP para gera o crud')
        with open('%s/%s/views.py'%(self.path, app), 'w') as f:
            if len(commands)>=2: f.write(SourceView.get_source_all_class_view(commands[1]))
            else: f.write(SourceView.get_source_all_class_view())
            f.close()
