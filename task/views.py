from .models import Label, Task
from .serializers import (CreateTaskSerialiazer,
                          CreateLabelSerializer,
                          UpdateLabelSerializer,
                          LabelSerializer,
                          UpdateTaskSerializer)

from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CreateLabelView(CreateAPIView):
    serializer_class = CreateLabelSerializer
    queryset = Label.objects.all()


class CreateTaskView(CreateAPIView):
    serializer_class = CreateTaskSerialiazer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        label = serializer.validated_data["label"]
        max_sort = 0

        for task in label.tasks.all():
            if task.sort > max_sort:
                max_sort = task.sort

        serializer.save(label=label, sort = max_sort + 1)

class LabelListView(ListAPIView):
    serializer_class = LabelSerializer
    queryset = Label.objects.all()


class UpdateLabelView(UpdateAPIView):
    serializer_class = UpdateLabelSerializer
    queryset = Label.objects.all()

class UpdateTaskView(UpdateAPIView):
    serializer_class = UpdateTaskSerializer
    queryset = Task.objects.all()

class MoveTaskView(APIView):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)

        previous_task_id = request.data.get("previous_task_id")
        next_task_id = request.data.get("next_task_id")

        previous_task = None
        next_task = None

        if previous_task_id is not None:
            previous_task = Task.objects.get(pk=previous_task_id)

        if next_task_id is not None:
            next_task = Task.objects.get(pk=next_task_id)

        if previous_task and next_task:
            new_sort = (previous_task.sort + next_task.sort) / 2

        elif previous_task:
            new_sort = previous_task.sort + 1

        elif next_task:
            new_sort = next_task.sort - 1

        else:
            return Response(
                {"error": "At least one neighbor must be provided."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        task.sort = new_sort
        task.save()

        return Response(
            {
                "id": task.id,
                "sort": task.sort,
            }
        )

class DeleteTaskView(DestroyAPIView):
    queryset = Task.objects.all()


class DeleteLabelView(DestroyAPIView):
    queryset = Label.objects.all()