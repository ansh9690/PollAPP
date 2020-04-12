from django.shortcuts import render, redirect
from .models import CreatePoll
from django.contrib import messages
from django.http import HttpResponse


def all_polls(request):
    polls = CreatePoll.objects.all()
    context = {'polls': polls}
    return render(request, 'poll/all_polls.html', context)


def create_poll(request):
    if not request.user.is_authenticated:
        return render(request, 'accounts/login.html')
    else:
        if request.method == 'POST':
            if request.POST['question'] == '' or request.POST['option_one'] == '' or request.POST['option_two'] == '':
                messages.error(request, "Please fill all fields")
            else:
                poll = CreatePoll(question=request.POST['question'], option_one=request.POST['option_one'],
                                  option_two=request.POST['option_two'])
                poll.save()
                messages.success(request, 'New Poll Added')
                return redirect('poll:all_polls')
        return render(request, 'poll/create_poll.html')


def result(request, result_id):
    polls = CreatePoll.objects.get(pk=result_id)
    context = {'poll': polls}
    return render(request, 'poll/result.html', context)


def vote(request, vote_id):
    if not request.user.is_authenticated:
        return render(request, 'accounts/login.html')
    else:
        polls = CreatePoll.objects.get(pk=vote_id)
        if request.method == 'POST':
            selected_option = request.POST['polls']
            if selected_option == 'Option1':
                polls.option_one_count += 1
            elif selected_option == 'Option2':
                polls.option_two_count += 1
            else:
                return HttpResponse("Invalid")
            polls.save()
            return redirect('poll:result', polls.id)
        context = {'poll': polls}
        return render(request, 'poll/vote.html', context)
