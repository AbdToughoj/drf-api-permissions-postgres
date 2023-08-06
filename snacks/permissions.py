from rest_framework import permissions

class IsPurchaserOrReadOnly(permissions.BasePermission):

    message = "You can't edit this snack, You are not the purchaser !!"
    def has_object_permission(self, request, view, obj):

        if request.method == 'GET':
            return True
        
        if request.user == obj.purchaser :
            return True 
        else : 
            return False 
