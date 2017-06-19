import socket

class SourceView:
    head_author = "#View gerada pelo GUN\n#CRIADO POR: %s\n" %(socket.gethostname().upper()) #get name of user OS
    imports_view_class_based = """
from django.shortcuts import render
from django.views.generic import (
CreateView,
UpdateView,
ListView,
DetailView,
DeleteView)
    """
    
    @classmethod
    def get_source_create_class_view(self, model="<MODEL>"):
        return """
#Create view
class Create(CreateView):
    model = %s
    template_name = <TEMPLATE>
    form_class = <FORM CLASS>
    success_url = reverse_lazy(<ROUTE>)
        """ %(model)

    @classmethod
    def get_source_update_class_view(self, model="<MODEL>"):
        return """
#Update view
class Update(UpdateView):
    model = %s
    template_name = <TEMPLATE>
    form_class = <FORM CLASS>
    success_url = reverse_lazy(<TEMPLATE>)
        """ %(model)

    @classmethod
    def get_source_list_class_view(self, model="<MODEL>"):
        return """
#List view
class List(ListView):
    model = %s
    template_name = <TEMPLATE>
    paginate_by = 10 #paginate
        """ %(model)

    @classmethod
    def get_source_detail_class_view(self, model="<MODEL>"):
        return """
#Detail view
class Detail(DetailView):
    model = %s
    template_name = <TEMPLATE>
        """ %(model)

    @classmethod
    def get_source_delete_class_view(self, model="<MODEL>"):
        return """
#Delete view
class Delete(DeleteView):
    model = %s
    template_name = <TEMPLATE> #template for delete confirm object
    success_url = reverse_lazy(<TEMPLATE>)
        """ %(model)

    @classmethod
    def get_source_all_class_view(self, model="MODEL"):
        return (self.head_author+self.imports_view_class_based+self.get_source_create_class_view(model)+
        self.get_source_update_class_view(model)+self.get_source_list_class_view(model)+
        self.get_source_detail_class_view(model)+self.get_source_delete_class_view(model))
