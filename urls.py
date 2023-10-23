from . import views
from django.urls import path

urlpatterns = [
    path('',views.login_home,name="loginhome"),
    path('loginhome',views.login_home,name="loginhome"),
    path('adminprofile', views.admin_profile, name='admin_profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('change_password', views.change_password, name='change_password'),
    path('login',views.login,name="login"),
    path('adminindex',views.admin_home,name="adminindex"),
    path('add_route', views.add_route, name='add_route'),
    path('view_route', views.view_route, name='view_route'),
    path('add_route_signal/<str:id>', views.add_signal, name='add_signal'),
    path('view_route_signal/<str:id>', views.view_signal, name='view_signal'),
    path('add_staff', views.add_staff, name='add_staff'),
    path('view_staff', views.view_staff, name='view_staff'),
    path('update_staff/<str:id>', views.update_staff, name='update_staff'),
    path('delete_staff/<str:id>', views.delete_staff, name='delete_staff'),
    path('allocate_staff/<str:id>', views.allocate_staff, name='allocate_staff'),
    path('view_allocated_staff/<str:id>', views.allocated_staff, name='allocated_staff'),
    path('remove_staff/<str:id>', views.remove_staff, name='remove_staff'),
    path('adminlogout',views.admin_logout,name="adminlogout"),
    path('add_fine/<str:id>', views.add_user_fine, name='add_fine'),
    path('view_fine/<str:id>', views.view_fine, name='view_fine'),
    path('location/<str:id>/<str:jd>', views.location, name='location'),
    path('edit_signal/<str:id>', views.edit_signal, name='edit_signal'),
    path('delete_signal/<str:id>', views.delete_signal, name ='delete_signal'),
    path('queries',views.feedback, name='feedback'),
    path('reply_query/<str:id>', views.reply_feed, name='reply_feedback'),
    path('delete_route/<str:id>', views.delete_route, name='delete_route'),

    # # ambulance
    # # ---------
    # path('ambulancehome',views.ambulance_home,name="ambulancehome"),
    # path('viewaccidentcases',views.view_accident_cases,name="viewaccidentcases"),
    # path('ambulanceviewlocation/<str:lat>/<str:lon>',views.ambulance_view_location,name="ambulanceviewlocation"),
    # path('ambulanceaccept/<str:id>',views.ambulance_accept,name="ambulanceaccept"),
    # path('viewacceptedrequest',views.view_accepted_request,name="viewacceptedrequest"),
    #
    # # admin
    # # ------------------------------------------------------------------------
    # path('logout',views.logout,name="logout"),
    # path('adminindex',views.admin_home,name="adminindex"),
    # path('publicreport',views.public_report,name="publicreport"),
    # path('accidentrequestapprove/<str:id>',views.accident_request_approve,name="accidentrequestapprove"),
    # path('addstation',views.add_station,name="addstation"),
    # path('addambulance',views.add_ambulance,name="addambulance"),
    # path('viewstation',views.view_station,name="viewstation"),
    # path('viewambulance',views.view_ambulance,name="viewambulance"),
    # path('deleteambulance/<str:id>',views.delete_ambulance,name="delete_ambulance"),
    # path('editstation/<str:id>',views.edit_station,name="editstation"),
    # path('deletestation/<str:id>',views.delete_station,name="deletestation"),
    # path('addfinecategory',views.add_fine_category,name="addfinecategory"),
    # path('viewfinecategory',views.view_fine_category,name="viewfinecategory"),
    # path('editfinecategory/<str:id>',views.edit_fine_category,name="editfinecategory"),
    # path('deletefinecategory/<str:id>',views.delete_fine_category,name="deletefinecategory"),
    # path('viewaccidentspot',views.view_accident_spot,name="viewaccidentspot"),
    # path('deleteaccidentspot/<str:id>',views.delete_accident_spot,name="deleteaccidentspot"),
    # path('aviewstation',views.aview_station,name="aviewstation"),
    # path('aviewfuelstation/<str:id>',views.aview_fuelstation,name="aviewfuelstation"),
    # path('viewlocation/<str:lat>/<str:lon>',views.view_location,name="viewlocation"),
    #  path('deletefuelstation1/<str:id>',views.delete_fuel_station1,name="deletefuelstaion1"),
    # # station
    # # ------------------------------------------------------------------------
    # path('stationhome',views.station_home,name="stationhome"),
    # path('stationlogout',views.station_logout,name="stationlogout"),
    # path('saddaccidentspot', views.station_add_accident_spot, name='saddaccidentspot'),
    # path('addfuelstation',views.add_fuel_station,name="addfuelstation"),
    # path('viewfuelstation',views.view_fuel_station,name="viewfuelstation"),
    # path('editfuelstation/<str:id>',views.edit_fuel_station,name="editfuelstation"),
    # path('deletefuelstation/<str:id>', views.delete_fuel_station, name="deletefuelstation"),
    # path('sviewfinecategory',views.station_view_fine_category,name="sviewfinecategory"),
    # path('addfine/<str:id>',views.add_fine,name="addfine"),
    # path('viewfinenotpaid',views.view_fine_notpaid,name="viewfinenotpaid"),
    # path('viewfinepaid', views.view_fine_paid, name="viewfinepaid"),
    # path('sviewaccidentspot',views.station_view_accident_spot,name="sviewaccidentspot"),
    # path('stationviewlocation/<str:lat>/<str:lon>',views.station_view_location,name="stationviewlocation"),
    #
    # # public
    # # ------------------------------------------------------------------------
    # path('userregister', views.user_registration, name="userregister"),
    # path('userhome',views.user_home,name="userhome"),
    # path('uaddaccidentspot',views.user_add_accident_spot,name='uaddaccidentspot'),
    # path('userviewambulance',views.user_view_ambulance,name="userviewambulance"),
    # path('userviewstation',views.user_view_station,name="userviewstation"),
    # path('userviewstation1',views.user_view_station1,name="userviewstation1"),
    # path('uviewfuelstation/<str:id>',views.user_view_fuelstation,name="uviewfuelstation"),
    # path('uviewlocation/<str:lat>/<str:lon>', views.user_view_location, name="uviewlocation"),
    # path('viewfineamount',views.view_fine_amount,name="viewfineamount"),
    # path('checkfine',views.check_fine,name="checkfine"),
    # path('checkpaiddetails', views.check_paid_details, name="checkpaiddetails"),
    # path('makepayment/<str:id>',views.make_payment,name="makepayment"),


]

