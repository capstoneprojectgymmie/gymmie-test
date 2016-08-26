# rendering the html files
from django.shortcuts import (
	render,
	render_to_response,
	get_object_or_404
	)
# forms we will use to make instances of
# related models inside of html template
from rango.forms import (
	WeightForm,
	UserForm,
	UserProfileForm,
	CalcForm,
	RoutineForm
	)
from django.template import RequestContext
# for graphing charts for our
# progress reports
from chartit import (
	DataPool,
	Chart
	)
# for when we have to use models in code
from rango.models import (
	Weightgraph,
	Calculations,
	ForGraphing,
	LevelGrowthGraph,
	Exercise,
	ExerciseRoutine
	)
	#SecretCalculator
	#)
# for authentication and log in
# for user instances
from django.contrib.auth import (
	authenticate,
	login,
	logout
	)
# redirecting to a different page
# as a reponse to an event
from django.http import (
	HttpResponseRedirect,
	HttpResponse
	)
# allowing access to page if
# user is logged in
from django.contrib.auth.decorators import login_required
# The views: Homepage, Meet the Team, Registration,
# Login, Logout, Update Weight, Show Weight, DeleteExLog
def index(request):
	return render(request,'rango/home.html')
def meet_the_team(request):
	return render(request, 'rango/meet_the_team.html')
def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		calc_form = CalcForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid() and calc_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			calc = calc_form.save(commit=False)
			calc.user = user
			calc.gender = profile.gender
			calc.height_for_calc = profile.height
			calc.weight_for_calc = profile.weight
			calc.save()
			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
		calc_form = CalcForm()
	return render_to_response('rango/register.html',{'user_form': user_form, 'profile_form': profile_form, 'calc_form': calc_form, 'registered' : registered}, context)
def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password =password)
		if user is not None:
			if user.is_active:
				login(request, user)
				#I can also add calculations as well 
				#Here i can add code for setting the weightgraph's first value
				return HttpResponseRedirect('/rango/view_weight/')
			else:
				return HttpResponse('Sorry but your account is disabled')
		else:
			return HttpResponse('You provided Invalid Details')
	else:
		return render_to_response('rango/login.html',{},context)
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/rango/')
@login_required
def update_weight(request):
	myweightgraph = Weightgraph(user=request.user)
	context = RequestContext(request)
	if request.method == 'POST':
		form = WeightForm(request.POST, instance = myweightgraph)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print (form.errors)
	else:
		form = WeightForm()
	return render_to_response('rango/update_weight.html',{'form':form}, context)
@login_required
def show_weight(request):
	weightdata = DataPool(
                  series=
                  [{'options': {
                       'source': Weightgraph.objects.filter(user=request.user).order_by('day')
                  },
                       'terms': [
                         'weight',
                         'date'
                       ]
                   }]
		)
	weightchart = Chart(
		           datasource = weightdata,
		           series_options =
		           [{ 'options': {
		                'type' : 'line',
		                'stacking' : False
		           },
		            'terms': {
		            'date': [
                       'weight',
		            ]
		            }
		           }],
		           chart_options =
		           { 'title' : {
		              'text' : 'Weight Report'
		           },
		           'xAxis' : {
		              'title': {
		                'text': 'Date'
		              }
		           },
		           'credits': False
		           }
		)
	weightchart2 = Chart(
		           datasource = weightdata,
		           series_options =
		           [{ 'options': {
		                'type' : 'line',
		                'stacking' : False
		           },
		            'terms': {
		            'date': [
                       'weight',
		            ]
		            }
		           }],
		           chart_options =
		           { 'title' : {
		              'text' : 'Weight Report'
		           },
		           'xAxis' : {
		              'title': {
		                'text': 'Date'
		              }
		           },
		           'credits': False
		           }
		)
	bmidata = DataPool(
                  series=
                  [{'options': {
                       'source': ForGraphing.objects.filter(user=request.user)
                  },
                       'terms': [
                         'bmi',
                         'user',
                       ]
                  }]
		)
	bmichart = Chart(
		           datasource = bmidata,
		           series_options =
		           [{ 'options': {
		                'type' : 'bar',
		                'stacking' : False
		           },
		            'terms': {
		            'user': [
                       'bmi',
		            ]
		            }
		           }],
		           chart_options =
		           { 'title' : {
		              'text' : 'My BMI'
		           },
		           'yAxis' : {
		              'title': {
		                'text': 'BMI'
		              }
		           },
		           'credits': False
		           }
		)
	bmichart2 = Chart(
		           datasource = bmidata,
		           series_options =
		           [{ 'options': {
		                'type' : 'bar',
		                'stacking' : False
		           },
		            'terms': {
		            'user': [
                       'bmi',
		            ]
		            }
		           }],
		           chart_options =
		           { 'title' : {
		              'text' : 'My BMI'
		           },
		           'yAxis' : {
		              'title': {
		                'text': 'BMI'
		              }
		           },
		           'credits': False
		           }
		)
	ibwdata = DataPool(
                  series=
                  [{'options': {
                       'source': ForGraphing.objects.filter(user=request.user)
                  },
                       'terms': [
                         'user',
                         'ibw',
                         'ibw_hamwi',
                         'current_weight',
                       ]
                  }]
		)
	ibwchart = Chart(
		           datasource = ibwdata,
		           series_options =
		           [{ 'options': {
		                'type' : 'column',
		                'stacking' : False
		           },
		            'terms': {
		            'user': [
                       'current_weight',
                       'ibw',
                       'ibw_hamwi',
		            ]
		            }
		           }],
		           chart_options =
		           { 'title' : {
		              'text' : 'My weight vs IBW'
		           },
		           'yAxis' : {
		              'title': {
		                'text': 'weight'
		              }
		           },
		           'credits': False
		           }
		)
	levelsdata = DataPool(
                  series=
                  [{'options': {
                       'source': LevelGrowthGraph.objects.filter(user=request.user)
                  },
                       'terms': [
                         'abslevel',
                         'leg',
                         'upperarm',
                         'lowerarm',
                         'back',
                         'chest',
                         'neck',
                         'overall',
                         'glutes',
                         'date'
                       ]
                  }]
		)
	levelschart = Chart(
		           datasource = levelsdata,
		           series_options =
		           [{ 'options': {
		                'type' : 'line',
		                'stacking' : False
		           },
		            'terms': {
		            'date': [
		                 'abslevel',
                         'leg',
                         'upperarm',
                         'lowerarm',
                         'back',
                         'chest',
                         'neck',
                         'overall',
                         'glutes',
		            ]
		            }
		           }],
		           chart_options =
		           { 'title' : {
		              'text' : 'Levels Progress Report'
		           },
		           'xAxis' : {
		              'title': {
		                'text': 'Date'
		              }
		           },
		           'yAxis' : {
		              'title': {
		                'text': 'Level'
		              }
		           },
		           'credits': False
		           }
		)
	levels = LevelGrowthGraph.objects.filter(user=request.user).last()
	#the filters for the lists of exercises
	# d-under contains allow us to search for exercise worked muscles
	all_ex = Exercise.objects.all()
	ab_ex = Exercise.objects.filter(categories__contains='Abs')
	abductor_ex = Exercise.objects.filter(categories__contains='Abductors')
	adductor_ex = Exercise.objects.filter(categories__contains='Adductors')
	biceps_ex = Exercise.objects.filter(categories__contains='Biceps')
	calves_ex = Exercise.objects.filter(categories__contains='Calves')
	chest_ex = Exercise.objects.filter(categories__contains='Chest')
	forearms_ex = Exercise.objects.filter(categories__contains='Forearms')
	glutes_ex = Exercise.objects.filter(categories__contains='Glutes')
	hamstrings_ex = Exercise.objects.filter(categories__contains='Hamstrings')
	lats_ex = Exercise.objects.filter(categories__contains='Lats')
	lback_ex = Exercise.objects.filter(categories__contains='Lower')
	mback_ex = Exercise.objects.filter(categories__contains='Middle')
	neck_ex = Exercise.objects.filter(categories__contains='Neck')
	quad_ex = Exercise.objects.filter(categories__contains='Quadriceps')
	shoulder_ex = Exercise.objects.filter(categories__contains='Shoulders')
	traps_ex = Exercise.objects.filter(categories__contains='Traps')
	triceps_ex = Exercise.objects.filter(categories__contains='Triceps')
	day_1log = ExerciseRoutine.objects.filter(user=request.user, day='DayOne')
	day_2log = ExerciseRoutine.objects.filter(user=request.user, day='DayTwo')
	day_3log = ExerciseRoutine.objects.filter(user=request.user, day='DayThree')	
	return render_to_response('rango/view_weight.html',{'chart_list': [weightchart,weightchart2,bmichart,bmichart2,ibwchart,levelschart],'levels':levels,'all_ex':all_ex,'ab_ex':ab_ex,'abductor_ex':abductor_ex,'adductor_ex':adductor_ex,'biceps_ex':biceps_ex,'calves_ex':calves_ex,'chest_ex':chest_ex,'forearms_ex':forearms_ex,'glutes_ex':glutes_ex,'hamstrings_ex':hamstrings_ex,'lats_ex':lats_ex,'lback_ex':lback_ex,'mback_ex':mback_ex,'neck_ex':neck_ex,'quad_ex':quad_ex,'shoulder_ex':shoulder_ex,'traps_ex':traps_ex,'triceps_ex':triceps_ex, 'day_1log':day_1log,'day_2log':day_2log, 'day_3log':day_3log})
@login_required
def add_to_exlog(request,exercise_id):
	# enter a if statement to check exercise equipment is bodyweight then get another form
	the_exercise = get_object_or_404(Exercise, ex_key = exercise_id)
	myroutine = ExerciseRoutine(user=request.user, exercise = the_exercise)
	context = RequestContext(request)
	if request.method == 'POST':
		form = RoutineForm(request.POST, instance = myroutine)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print (form.errors)
	else:
		form = RoutineForm()
	return render_to_response('rango/add_exlog.html',{'form':form,'the_exercise':the_exercise}, context)
@login_required
def delete_exlog(request,routine_id):
	to_be_removed = get_object_or_404(ExerciseRoutine,id=routine_id)
	to_be_removed.truedelete()
	return HttpResponseRedirect('/rango/view_weight/')
#add delete ex log function to remove exercises that have not been completed