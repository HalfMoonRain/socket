from django.shortcuts import render

# views.py
from django.http import JsonResponse
from django.conf import settings
import redis

def redis_test_view(request):
    redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
    
    # 데이터 쓰기
    try:
        redis_client.set('test_key', 'connection_success')
    except Exception as e:
        return JsonResponse({"status": "failed", "error": str(e)})

    # 데이터 읽기
    try:
        value = redis_client.get('test_key').decode('utf-8')
        return JsonResponse({"status": "success", "value": value})
    except Exception as e:
        return JsonResponse({"status": "failed", "error": str(e)})
