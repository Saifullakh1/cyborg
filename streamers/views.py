from django.shortcuts import render
from .models import Stream, Streamer


def streams(request):
    streamers = Streamer.objects.all()
    streams = Stream.objects.all()
    return render(request, 'streams.html', {"streamers": streamers, "streams": streams})