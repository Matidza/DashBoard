from django.shortcuts import render

# Create your views here.
def homepage(request):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    #user = request.User 
    #if user.usertype == 'jobseeker':    
    #    return render(request, 'jobseeker:jobseeker/dashboard.html')
    #else:
    #    return message('')
    
    #if user.usertype == 'employer':
    #    return render(request, 'employer/dashboard.html')
    return render(request, 'employer/dashboard.html')