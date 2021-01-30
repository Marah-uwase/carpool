import json
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed, HttpResponseBadRequest
from django.shortcuts import render
from .utils import clusterize_latlngs, search
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import datetime
# Create your views here.


def welcome(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
    return render(request, 'index.html')


@login_required
def new_trip(request):
    if request.method == 'GET':
        return render(request, '/trips/createJourney.html')
    else:
        return HttpResponseNotAllowed(['GET'])



def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        return HttpResponseNotAllowed(['GET'])


def signup(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first']
            last_name = request.POST['last']
            email = request.POST['email']
            password = request.POST['password']
            contact = request.POST['contact']

            user = CustomUser.objects.create_user(email, first_name, last_name, contact, password=password)
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
                else:
                    return HttpResponseRedirect('/welcome/')

            return HttpResponseRedirect('/welcome/')

        except KeyError:
            return HttpResponseRedirect('/welcome/')
    else:
        return HttpResponseNotAllowed(['POST'])


def signin(request):
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
                else:
                    return HttpResponseRedirect('/welcome/')

            return HttpResponseRedirect('/welcome/')

        except KeyError:
            return HttpResponseRedirect('/welcome/')
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required(login_url='/accounts/login/')
def individual_profile_page(request, username=None):
    if not username:
        username = request.user.username
    # images by user id
    images = Image.objects.filter(user_id=username)

    return render (request, 'django_registration/user_image_list.html', {'images':images, 'username': username})

@login_required(login_url='/accounts/login/')
def save_journey(request):
    if request.is_ajax() and request.method == "POST":
        try:
            res = json.loads(request.body)
            cords = res['cords']
            cords = [[x['d'], x['e']] for x in cords]
            distance = res['distance']
            start_place = res['start']
            end_place = res['end']
            clusters = clusterize_latlngs(cords, distance)
            time = datetime.datetime.strptime(res['time'], "%m/%d/%Y %H:%M")
            Trip.objects.create(user=request.user, time=time, cluster=json.dumps(clusters), travel_distance=distance,
                                start_place=start_place, end_place=end_place)

            return HttpResponse()
        except:
            return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(['POST'])


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/welcome/')


@login_required
def search_trip(request):
    return render(request, '/trips/searchjourney.html')


@login_required (login_url='/accounts/login/')
def get_results(request):
    if request.is_ajax() and request.method == "POST":
        try:
            res = json.loads(request.body)
            print (res)
            cords = res['cords']
            cords = cords[0:1] + cords[-1:]
            cords = [[x['d'], x['e']] for x in cords]
            temp = []
            temp.append(cords[0][0])
            temp.append(cords[0][1])
            temp.append(cords[1][0])
            temp.append(cords[1][1])
            distance = res['distance']
            start_place = res['start']
            end_place = res['end']
            radius = int(res['radius'])
            time = datetime.datetime.strptime(res['time'], "%m/%d/%Y %H:%M")
            matched_trips = search(cords, time, radius)

            results = []
            for trip in matched_trips:
                res = {}
                res['id'] = trip.id
                res['startPlace'] = trip.start_place
                res['endPlace'] = trip.end_place
                res['startTime'] = datetime.datetime.strftime(trip.time, "%d %b, %H:%M")
                results.append(res)
            data = json.dumps({'cords': temp, 'start_place': start_place, 'end_place': end_place})
            request.session['data'] = data
            request.session['results'] = results

            # print render(request, 'searchResults.html', {'results':results, 'data':data})
            # return render(request, 'searchResults.html', {'results':results, 'data':data})
            return HttpResponse()
        except:

            return HttpResponseBadRequest()

    else:
        return HttpResponseNotAllowed(['POST'])


@login_required(login_url='/accounts/login/')
def search_results(request):
    results = request.session.get('results', {})
    data = request.session.get('data', {})
    return render(request, 'searchResults.html', {'data': data, 'results': results})


@login_required
def request_success(request):
    return render(request, 'trips/requestsuccess.html')


@login_required
def trip_success(request):
    return render(request, 'trips/success.html')

@login_required
def send_request(request):
    if request.is_ajax() and request.method == 'POST':
        # try:
        res = json.loads(request.body)
        trip = Trip.objects.get(pk=res['id'])
        start_place = res['start_place']
        end_place = res['end_place']
        status = 'P'
        cords = res['cords']
        start_lat = cords[0]
        start_lng = cords[1]
        end_lat = cords[2]
        end_lng = cords[3]

        Request.objects.create(from_user=request.user, trip=trip, status=status, start_place=start_place,
                               start_lat=start_lat, start_lng=start_lng,
                               end_place=end_place, end_lat=end_lat, end_lng=end_lng)
        return HttpResponse()
        # except:
        #     return HttpResponseBadRequest()
    else:
        return HttpResponseNotAllowed(['POST'])


@login_required (login_url='/accounts/login/')
def sent_requests(request):
    if request.method=='GET':
        current_sent = request.user.current_sent_requests()
        curr = current_sent.values('id','status','trip__user__first_name','trip__user__last_name','start_place','end_place','trip__time')
        old_sent = request.user.previous_sent_requests()
        old = old_sent.values('id','status','trip__user__first_name','trip__user__last_name','start_place','end_place','trip__time')

        return render(request,'trips/sentrequests.html',{'current':curr, 'expired':old})
    else:
        return HttpResponseNotAllowed(['GET'])


def received_requests(request):
    if request.method=='GET':
        current_received = request.user.current_received_requests()
        curr = current_received.values('id','status','trip__user__first_name','trip__user__last_name','start_place','end_place','trip__time')

        return render(request,'receivedrequests.html',{'current':curr})
    else:
        return HttpResponseNotAllowed(['GET'])

@login_required (login_url='/accounts/login/')
def accept_requests(request):
    if request.method=='POST':
        res = json.loads(request.body)
        ids = res['selected']
        print (ids)
        for id in ids:
            req = Request.objects.get(pk=id)
            # print request.user.accept_request(req)

        return HttpResponse()

@login_required (login_url='/accounts/login/')
def decline_requests(request):
    if request.method=='POST':
        res = json.loads(request.body)
        ids = res['selected']
        for id in ids:
            req = Request.objects.get(pk=id)
            request.user.decline_request(req)

        return HttpResponse()

def newsletter(request):
    name = request.POST.get('your_name')
    email= request.POST.get('email')

    recipient= NewsLetterRecipients(name= name, email =email)
    recipient.save()
    send_welcome_email(name, email)
    data= {'success': 'You have been successfully added to the newsletter mailing list'}
    return JsonResponse(data)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'    
