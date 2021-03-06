from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from dfirtrack_main.forms import TasknameForm
from dfirtrack_main.logger.default_logger import debug_logger
from dfirtrack_main.models import Taskname

class TasknameList(LoginRequiredMixin, ListView):
    login_url = '/login'
    model = Taskname
    template_name = 'dfirtrack_main/taskname/tasknames_list.html'
    context_object_name = 'taskname_list'

    def get_queryset(self):
        debug_logger(str(self.request.user), " TASKNAME_LIST_ENTERED")
        return Taskname.objects.order_by('taskname_name')

class TasknameDetail(LoginRequiredMixin, DetailView):
    login_url = '/login'
    model = Taskname
    template_name = 'dfirtrack_main/taskname/tasknames_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        taskname = self.object
        taskname.logger(str(self.request.user), " TASKNAME_DETAIL_ENTERED")
        return context

class TasknameCreate(LoginRequiredMixin, CreateView):
    login_url = '/login'
    model = Taskname
    form_class = TasknameForm
    template_name = 'dfirtrack_main/taskname/tasknames_add.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        debug_logger(str(request.user), " TASKNAME_ADD_ENTERED")
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            taskname = form.save(commit=False)
            taskname.save()
            taskname.logger(str(request.user), " TASKNAME_ADD_EXECUTED")
            messages.success(request, 'Taskname added')
            return redirect('/tasknames/' + str (taskname.taskname_id))
        else:
            return render(request, self.template_name, {'form': form})

class TasknameUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = Taskname
    form_class = TasknameForm
    template_name = 'dfirtrack_main/taskname/tasknames_edit.html'

    def get(self, request, *args, **kwargs):
        taskname = self.get_object()
        form = self.form_class(instance=taskname)
        taskname.logger(str(request.user), " TASKNAME_EDIT_ENTERED")
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        taskname = self.get_object()
        form = self.form_class(request.POST, instance=taskname)
        if form.is_valid():
            taskname = form.save(commit=False)
            taskname.save()
            taskname.logger(str(request.user), " TASKNAME_EDIT_EXECUTED")
            messages.success(request, 'Taskname edited')
            return redirect('/tasknames/' + str (taskname.taskname_id))
        else:
            return render(request, self.template_name, {'form': form})
