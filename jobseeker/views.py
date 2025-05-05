from email import message
from django.shortcuts import render
# Import th GateWay API to get access to the loggedin user Access token and refresh token
# import the Gateway API to get access to the Ccustom user model/ or just cconnect the app with the odel directly from the Railway



# Create your views here.
def homepage(request):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    #user = request.User 
    #if user.usertype == 'jobseeker':    
    #    return render(request, 'jobseeker/dashboard.html')
    #else:
    #    return message('')
    
    #if user.usertype == 'employer':
    #    return render(request, 'employer:employer/dashboard.html')
    
    return render(request, 'jobseeker/dashboard.html')