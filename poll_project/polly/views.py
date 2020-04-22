from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreatePollForm
from .models import Pollmd

"""
def poll_base(request):
    context = {}
    return render(request, 'pages/base.html', context)
# Create your views here.
"""

#def mapi(any, funt):
#    return map(funt, any)

def poll_home(request):
    pol_home = Pollmd.objects.all()

    context = {
        'pol_home': pol_home
    }
    return render(request, 'pages/home.html', context)

def poll_create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('poll_home')
    else:
        form = CreatePollForm()
    paul = Pollmd.objects.all()

    context = {
        'form': form,
        'paul': paul,
    }
    return render(request, 'pages/create.html', context)


def poll_vote(request, pol_id):
    pol_vote = Pollmd.objects.get(pk = pol_id)

    if request.method == 'POST':

        #print(request.POST['poll_v'])

        selected_option = request.POST['poll_v']
        if selected_option == 'option1':
            pol_vote.option_one_count += 1
        elif selected_option == 'option2':
            pol_vote.option_two_count += 1
        elif selected_option == 'option3':
            pol_vote.option_three_count += 1
        else:
            return HttpResponse(404, 'Invalid form option')

        pol_vote.save()
        return redirect('poll_results', pol_vote.id)

    context = {
        'pol_vote': pol_vote
    }

    return render(request, 'pages/vote.html', context)

def poll_results(request, pol_id):
    pol_results = Pollmd.objects.get(pk = pol_id)
    context = {
        'pol_results': pol_results
    }
    return render(request, 'pages/results.html', context)

def poll_vote1(request):
    import pipetools as pt
    pol_vote1 = Pollmd.objects.all()

    def collector(entriesKeyList):
        #print(entriesPairList[1:])
        for key in entriesKeyList[1:]:
            pol_vote2 = Pollmd.objects.get(pk=int(key))
            selected_option = request.POST[key]
            if selected_option == '0':
                pol_vote2.option_one_count += 1
            elif selected_option == '1':
                pol_vote2.option_two_count += 1
            elif selected_option == '2':
                pol_vote2.option_three_count += 1
            else:
                return HttpResponse(404, 'Invalid form option')

            pol_vote2.save()

    if request.method == 'POST':
        request.POST.dict().copy().keys() > pt.pipe|list|collector
    
    context = {
        'pol_vote1': pol_vote1

    }

    return render(request, 'pages/vote1.html', context)


    #if request.method == 'POST':
    #
    #    #print(request.POST['poll_v'])
    #
    #    selected_option = request.POST['poll_v']
    #    if selected_option == 'option1':
    #        pol_vote.option_one_count += 1
    #    elif selected_option == 'option2':
    #        pol_vote.option_two_count += 1
    #    elif selected_option == 'option3':
    #        pol_vote.option_three_count += 1
    #    else:
    #        return HttpResponse(404, 'Invalid form option')
    #
    #    pol_vote.save()
    #    return redirect('poll_results', pol_vote.id)


# lnt = [ x/x for x in range(len(entries_mutable - 1) )]
# map(entries_mutable[1:], int) > pt.pipe |  list | print
# print(  map(int, entries_mutable[1:])  )
##print ( [1]*(len(entries_mutable) - 1) )
##print( pol_vote.get(pk=3).option_one_count )
# print( map(int, entries_mutable[1:]) )

    #def counters(requestPostDict):
    #    #request.POST.dict()#immutable hence to be made a copy to edit
    #    entriesPairList = list( requestPostDict.copy().items() )
    #    for epl in entriesPairList[1:] : [pol_vote.get(pk=int(epl[1])).option_one_count, pol_vote.option_two_count, pol_vote.option_three_count]
    #
    #    #map(int, entries_mutable[1:]) > pt.pipe | list | print

    #
    #    ents = request.POST.dict()
    #    entries = list(ents.copy().items())
    #
    #    for th in entries[1:]:
    #
    #        #print ( eval( 'pol_vote.get(pk=int(th[0])).option_'+th[1]+'_count' ) )
    #        basket = [Pollmd.objects.get(pk=int(th[0])).option_one_count, Pollmd.objects.get(pk=int(th[0])).option_two_count, Pollmd.objects.get(pk=int(th[0])).option_three_count]
    #        #print(basket)
    #        basket[int(th[1])] += 1
    #        pol_vote.get(pk=int(th[0])).save()
    #        #Pollmd.objects.save()
    #
    #
    #        #print(basket)
    #        Pollmd.objects.get(pk=int(th[0])).option_one_count = basket[0]
    #        Pollmd.objects.get(pk=int(th[0])).option_two_count = basket[1]
    #        Pollmd.objects.get(pk=int(th[0])).option_three_count = basket[2]
    #        Pollmd.objects.get(pk=int(th[0])).save()
    #
    #        #temp = eval( 'pol_vote.get(pk=int(th[0])).option_'+th[1]+'_count' )
    #        #temp += 1
    #        #eval('pol_vote.get(pk=int(th[0])).option_' + th[1] + '_count') += 1

#    if request.method == 'POST':
#        entriesPairList = list(request.POST.dict().copy().items())
#        print(entriesPairList[1:])
#        for pair in entriesPairList[1:]:
#            pol_vote2 = Pollmd.objects.get(pk=int(pair[0]))
#            basket = [pol_vote2.option_one_count, pol_vote2.option_two_count, pol_vote2.option_three_count]
#            basket[int(pair[1])] += 1
#            pol_vote2.save()