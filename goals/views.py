from django.shortcuts import get_object_or_404, render
#added froms and imports
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Exercise, UsersProfile, Abs, Shoulders, Glutes, Hamstrings, Lower_Back, Lats, Quadriceps, Triceps, Calves, Forearms, Traps, Abductors, Adductors, Middle_Back, Biceps, Chest, Neck
from django.contrib.auth.decorators import login_required
#For user creation
from .forms import UserForm, UserProfileForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.template import RequestContext



# Create your views here.
#so far: Homepage, Meet the Team, Progress Report, User Dashboard with
# required login
#Login decorator to not allow any view without authentication
def index(request):
    return render_to_response('goals/homepage.html')
def abss(request):
	abs_list = Abs.objects.order_by('ex_name')
	return render(request,'goals/Abdominals.html',{'abs_list':abs_list})
def adds(request):
	addu_list = Adductors.objects.order_by('ex_name')
	return render(request,'goals/Adductors.html',{'addu_list':addu_list})
def abds(request):
	abdu_list = Abductors.objects.order_by('ex_name')
	return render(request,'goals/Abductors.html',{'abdu_list':abdu_list})
def bis(request):
	biceps_list = Biceps.objects.order_by('ex_name')
	return render(request,'goals/Biceps,html',{'biceps_list':biceps_list})
def cavs(request):
	cavs_list = Calves.objects.order_by('ex_name')
	return render(request,'goals/Calves.html',{'cavs_list':cavs_list})
def chst(request):
	chest_list = Chest.objects.order_by('ex_name')
	return render(request,'goals/Chest.html',{'chest_list':chest_list})
def farms(request):
	farms_list = Forearms.objects.order_by('ex_name')
	return render(request,'goals/Forearms.html',{'farms_list':farms_list})
def gluts(request):
	glutes_list = Glutes.objects.order_by('ex_name')
	return render(request,'goals/Glutes.html',{'glutes_list':glutes_list})
def hams(request):
	ham_list = Hamstrings.objects.order_by('ex_name')
	return render(request,'goals/Hamstrings.html',{'ham_list':ham_list})
def lats(request):
	lats_list = Lats.objects.order_by('ex_name')
	return render(request,'goals/Lats.html',{'lats_list':lats_list})
def lback(request):
	lback_list = Lower_Back.objects.order_by('ex_name')
	return render(request,'goals/Lower_Back.html',{'lback_list':lback_list})
def mback(request):
	mback_list = Middle_Back.objects.order_by('ex_name')
	return render(request,'goals/Middle_Back.html',{'mback_list':mback_list})
def neck(request):
	neck_list = Neck.objects.order_by('ex_name')
	return render(request,'goals/Neck.html',{'neck_list':neck_list})
def quad(request):
	quad_list = Quadriceps.objects.order_by('ex_name')
	return render(request,'goals/Quadriceps.html',{'quad_list':quad_list})
def shldr(request):
	shoulders_list = Shoulders.objects.order_by('ex_name')
	return render(request,'goals/Shoulders.html',{'shoulders_list':shoulders_list})
def trap(request):
	traps_list = Traps.objects.order_by('ex_name')
	return render(request,'goals/Traps.html',{'traps_list':traps_list})
def tris(request):
	tri_list = Triceps.objects.order_by('ex_name')
	return render(request,'goals/Triceps',{'tri_list':tri_list})
def meettheteam(request):
	return render(request, 'goals/MeettheTeam/MeetTheTeam.html')
def progressreport(request):
	return render(request, 'goals/progressreportpage.html')
def exercise(request, exercise_id):
	the_exercise = get_object_or_404(Exercise, ex_key = exercise_id)
	return render(request, 'goals/ex_template.html', {'the_exercise': the_exercise})
def registeruser(request):
	context = RequestContext(request)
	registered = False
	if request.method == "POST":
		form = UserForm(request.POST or None)
		profile_form = UserProfileForm(request.POST or None)
		if form.is_valid() and profile_form.is_valid():
			form = form.save()
			form.set_password(form.password)
			form.save()
			profile = profile_form.save(commit = False)
			profile.user = form
			profile.save()
			registered = True
		else:
			print (profile_form.errors, form.errors)
	else:
		form = UserForm()
		profile_form = UserProfileForm()

	return render(request,'goals/user_registration.html', {'form': form, 'profile_form': profile_form}, context)
@login_required(login_url="login/")
def userdashboard(request):
	context = RequestContext(request)
	levels = get_object_or_404(UsersProfile)
	ex_list = Exercise.objects.order_by('ex_name')
	abs_list = Abs.objects.order_by('ex_name')
	shoulders_list = Shoulders.objects.order_by('ex_name')
	glutes_list = Glutes.objects.order_by('ex_name')
	ham_list = Hamstrings.objects.order_by('ex_name')
	lback_list = Lower_Back.objects.order_by('ex_name')
	lats_list = Lats.objects.order_by('ex_name')
	quad_list = Quadriceps.objects.order_by('ex_name')
	tri_list = Triceps.objects.order_by('ex_name')
	cavs_list = Calves.objects.order_by('ex_name')
	farms_list = Forearms.objects.order_by('ex_name')
	traps_list = Traps.objects.order_by('ex_name')
	addu_list = Adductors.objects.order_by('ex_name')
	abdu_list = Abductors.objects.order_by('ex_name')
	mback_list = Middle_Back.objects.order_by('ex_name')
	biceps_list = Biceps.objects.order_by('ex_name')
	chest_list = Chest.objects.order_by('ex_name')
	neck_list = Neck.objects.order_by('ex_name')
	return render(request,'userhome.html',{'levels':levels, 'ex_list':ex_list, 'abs_list':abs_list, 'shoulders_list':shoulders_list, 'glutes_list':glutes_list, 'ham_list':ham_list, 'lback_list':lback_list, 'lats_list':lats_list, 'quad_list':quad_list, 'tri_list':tri_list, 'cavs_list':cavs_list, 'farms_list':farms_list, 'traps_list':traps_list, 'addu_list':addu_list, 'abdu_list':abdu_list, 'mback_list':mback_list, 'biceps_list':biceps_list, 'chest_list':chest_list, 'neck_list':neck_list}, context)#name of html base file
