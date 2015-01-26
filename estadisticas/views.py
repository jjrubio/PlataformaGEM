from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext


def stats(request):
    template = "estadistica.html"
    return render_to_response(template, context_instance = RequestContext(request,locals()))