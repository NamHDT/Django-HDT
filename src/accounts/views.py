from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def get_all_jobs_by_auth_design(request):
    url = "https://workflow.base.vn/extapi/v1/jobs/get"

    payload='access_token=3275-RSMKMFWEWWPP24PBALFEPYF89F72D3HT-LYWF8BVMMLT87F4RSBSZ2HKRT8NBGS4M&page_id=100'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'basessid=hgvbogskso5s8ad5bbnf9vnnargfv3l4b9kilsoa6qo59nmn61llei3drjo8qtkrv1p6nu4l7jhbp00ltb325eugoktljgdpnema106aes2asohr5veoq8a6tbnar9nt'
    }

    response = request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)
    data = data['jobs']
    print(len(data))
    return HttpResponse(json.dumps(data), content_type='application/json')
