from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
def datetime_offset(request):
    now = datetime.now()
    datetime_four_hours_ago = now - timedelta(hours=4)
    datetime_four_hours_ahead = now + timedelta(hours=4)
    datetime_four_days_ago = now - timedelta(days=4)
    datetime_four_days_ahead = now + timedelta(days=4)
    html = "<html><body>"
    html += "<html><body>Current time is : %s <br></body></html>" % now 
    html += "<html><body>time four hours ago is: %s <br></body></html>" % datetime_four_hours_ago
    html += "<html><body>time four hours ahead is: %s <br></body></html>" % datetime_four_hours_ahead
    html += "<html><body>time four days ago is:%s <br></body></html>" % datetime_four_days_ago
    html += "<html><body>time four days ahead is: %s <br></body></html>" % datetime_four_days_ahead
    html += "</html></body>"
    return HttpResponse(html)