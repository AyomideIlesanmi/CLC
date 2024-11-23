from django.shortcuts import render
 
def number_pyramid(request, number):
    # Adjust for even numbers
    if number % 2 == 0:
        number -= 1
 
    # Generate the pyramid
    pyramid = []
    for i in range(1, number + 1):
        pyramid.append(list(range(1, i + 1)))
    for i in range(number - 1, 0, -1):
        pyramid.append(list(range(1, i + 1)))
 
    return render(request, 'pyramid.html', {'pyramid': pyramid})
 
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
 
def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_data')  # Redirect to user data page after successful registration
    else:
        form = UserRegistrationForm()
 
    return render(request, 'user_registration.html', {'form': form})
 
from .models import User
 
def user_data(request):
    users = User.objects.all()  # Retrieve all registered users from the database
    return render(request, 'user_data.html', {'users': users})

 
from django.http import JsonResponse
from .models import User

def ajax_search(request):
    query = request.GET.get('query', '')
    if query:
        users = User.objects.filter(username__icontains=query) | User.objects.filter(email__icontains=query)
    else:
        users = User.objects.all()
    
    user_data = []
    for user in users:
        user_data.append({
            'username': user.username,
            'email': user.email,
            'phone_number': user.phone_number,
            'profile_picture_url': user.profile_picture.url,
        })

    return JsonResponse(user_data, safe=False)
