import json
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import TodoList

# Create your views here.

class TodoListAPIView(APIView):

    @staticmethod
    def get(request, *args, **kwargs):

        results = []

        todos = TodoList.objects.filter(active=True)

        for t in todos:
            results.append({
                'todo': t.todo,
                'completed': t.completed
            })

        return Response(results, status=status.HTTP_200_OK)
    
    @staticmethod
    def post(request, *args, **kwargs):

        result = {}

        data = {
            'todo': request.data.get('todo'),
            'completed': request.data.get('completed'),
        }

        if data :
            if data['todo'] != "":
                todoCreate = TodoList()
                todoCreate.todo = data['todo']
                todoCreate.completed = data['completed'] if data['completed'] else False
                todoCreate.save()

                result = {
                    'success': True,
                    'msg': 'Create success',
                    'data': {
                        'todo': todoCreate.todo,
                        'completed': todoCreate.completed
                    }
                }
                _status = status.HTTP_201_CREATED

            else:
                missing_data = ''
                for k,v in zip(data.keys(), data.values()):
                    if v == None or v == "":
                        missing_data += f'{k}, '

                        result = {
                            'success': False,
                            'msg': f'missing {missing_data[:-2]} data'
                        }
                _status = status.HTTP_400_BAD_REQUEST
        else:
            missing_data = ''
            for k,v in zip(data.keys(), data.values()):
                if v == None or v == "":
                    missing_data += f'{k}, '

                    result = {
                        'success': False,
                        'msg': f'missing {missing_data[:-2]} data'
                    }
            _status = status.HTTP_400_BAD_REQUEST

        return Response(result, status=_status)
    
class TodoListUpdateAPIView(APIView):
    @staticmethod
    def get(request, *args, **kwargs):
        result = {}

        todo_id = kwargs.get('pk', None)

        todo = TodoList.objects.get(id=todo_id)
        if todo.active == True:
            result = {
                'todo': todo.todo,
                'completed': todo.completed
            }
            _status = status.HTTP_200_OK
        else:
            result = {
                'success': False,
                'msg': f'This todo is deleted'
            }
            _status = status.HTTP_400_BAD_REQUEST

        return Response(result, status=_status)

    @staticmethod
    def put(request, *args, **kwargs):
        result = {}
        todo_id = kwargs.get('pk', None)
        todo = TodoList.objects.get(id=todo_id)

        data = {
            'todo': request.data.get('todo', None),
            'completed': request.data.get('completed', None),
        }
        if todo.active == True:
            if data:
                if data['todo'] != "" and data['todo'] != None:
                    todoUpdate = todo
                    todoUpdate.todo = data['todo']
                    todoUpdate.completed = data['completed']
                    todoUpdate.save()

                    result = {
                        'success': True,
                        'msg': 'Update success',
                        'data': {
                            'todo': todoUpdate.todo,
                            'completed': todoUpdate.completed
                        }
                    }
                    _status = status.HTTP_201_CREATED
                else:
                    missing_data = ''
                    for k,v in zip(data.keys(), data.values()):
                        if v == None or v == "":
                            missing_data += f'{k}, '

                            result = {
                                'success': False,
                                'msg': f'missing {missing_data[:-2]} data'
                            }
                    _status = status.HTTP_400_BAD_REQUEST
        else:
            result = {
                'success': False,
                'msg': f'This todo cannot updated because is deleted'
            }
            _status = status.HTTP_400_BAD_REQUEST

        return Response(result, status=_status)
    
    @staticmethod
    def delete(request, *args, **kwargs):
        result = {}
        todo_id = kwargs.get('pk', None)
        
        todo = TodoList.objects.get(id=todo_id)
        if todo:
            if todo.active == True:
                todoDelete = todo
                todoDelete.active = False
                todoDelete.save()
                result = {
                    'success': True,
                    'msg': 'Delete success',
                    'data': {
                        'id': todoDelete.id,
                        'todo': todoDelete.todo,
                        'active': todoDelete.active
                    }
                }
                _status = status.HTTP_200_OK
            else:
                result = {
                    'success': False,
                    'msg': f"This todo can't delete because is deleted"
                }
                _status = status.HTTP_400_BAD_REQUEST
        else:
            result = {
                'success': False,
                'msg': 'todo does not exists'
            }
            _status = status.HTTP_400_BAD_REQUEST

        return Response(result, status=_status)