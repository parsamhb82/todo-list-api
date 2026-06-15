from rest_framework import serializers

from task.models import Task, Label

class CreateLabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Label
        fields = ['name']


class CreateTaskSerialiazer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["name", "label"]


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "is_finished",
            "sort",
            "dead_line",
        ]


class LabelSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()

    class Meta:
        model = Label
        fields = [
            "id",
            "name",
            "tasks",
        ]

    def get_tasks(self, obj):
        tasks = obj.tasks.order_by(
            "is_finished",
            "sort",
        )

        return TaskSerializer(tasks, many=True).data
    

class UpdateLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ["name"]


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "name",
            "is_finished",
            "dead_line",
        ]
