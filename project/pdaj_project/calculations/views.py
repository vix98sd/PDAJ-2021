from django.shortcuts import render
import json
from django.http import JsonResponse

import time
import tracemalloc

import algorithms.sequential as seq
import algorithms.list_comprehension as lc
import algorithms.generators as gen
import algorithms.mltprocessing as mltp

# Create your views here.

def test_works(request):
    if request.method == 'POST':
        n, m, special_fields = _get_data_from_request(request)
        # n = 10
        # m = 10
        # special_fields = [(1,3), (3,2), (6,8), (9,6), (5,5)]
        res, time, mbs = _calculate(seq.sequential, n, m, special_fields)
        print(res)
        # json_res = json.dumps({"result":res})
        return JsonResponse({"result": res, "time_in_s": 0.00, "max_memory_in_MB": 0.00}, safe=False, status=200)
    res = "GET request is not supported!"
    return JsonResponse(res, safe=False, status=404)

def sequential(request):
    if request.method == 'POST':
        n, m, special_fields = _get_data_from_request(request)
        res, time, mbs = _calculate(seq.sequential, n, m, special_fields)
        return JsonResponse({"result": res, "time_in_s": time, "max_memory_in_MB": mbs}, safe=False, status=200)
    res = "GET request is not supported!"
    return JsonResponse(res, safe=False, status=404)

def list_comprehension(request):
    if request.method == 'POST':
        n, m, special_fields = _get_data_from_request(request)
        res, time, mbs = _calculate(lc.list_comprehension, n, m, special_fields)
        return JsonResponse({"result": res, "time_in_s": time, "max_memory_in_MB": mbs}, safe=False, status=200)
    res = "GET request is not supported!"
    return JsonResponse(res, safe=False, status=404)

def generators(request):
    if request.method == 'POST':
        n, m, special_fields = _get_data_from_request(request)
        res, time, mbs = _calculate(gen.generators, n, m, special_fields)
        return JsonResponse({"result": res, "time_in_s": time, "max_memory_in_MB": mbs}, safe=False, status=200)
    res = "GET request is not supported!"
    return JsonResponse(res, safe=False, status=404)

def multiprocessing(request):
    if request.method == 'POST':
        n, m, special_fields = _get_data_from_request(request)
        res, time, mbs = _calculate(mltp.multiprocessing, n, m, special_fields)
        return JsonResponse({"result": res, "time_in_s": time, "max_memory_in_MB": mbs}, safe=False, status=200)
    res = "GET request is not supported!"
    return JsonResponse(res, safe=False, status=404)

def _calculate(function, n, m, special_points):
    tracemalloc.start()
    start = time.time()
    results = function(n, m, special_points)
    end = time.time()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tm = end - start
    return results, tm, peak / 10**6

def _get_data_from_request(request):
    data = json.loads(request.body)
    n, m, points = int(data["n"]), int(data["m"]), data["points"]
    point_list = _get_points_from_json(points)
    return n, m, point_list

def _get_points_from_json(json_points):
    point_list = []
    for point in json_points:
        x, y = point.split(',')
        x, y = int(x), int(y)
        point_list.append((x, y))
    return point_list