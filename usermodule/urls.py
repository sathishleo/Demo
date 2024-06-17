from django.urls import path
from usermodule.controller import devicecontroller, checksheet_controller, Maintaince_controller
# from .swagger import schema_view

# import usermodule.controller



urlpatterns=[
    path('create_device',devicecontroller.device_create,name='create_device'),
    path('view_device/<device_id>',devicecontroller.view_device,name='view_device'),
    path('create_operator',devicecontroller.operator_create,name='create_operator'),
    path('view_operator/<operator_id>',devicecontroller.view_operator,name='view_operator'),
    path('create_ecac',devicecontroller.ecac_create,name='create_ecac'),
    path('view_ecac/<ecac_id>',devicecontroller.view_ecac,name='view_ecac'),
    path('create_checksheet',checksheet_controller.checksheet_create,name='create_checksheet'),
    path('view_checksheet/<control_sheet_id>',checksheet_controller.view_checksheet,name='view_checksheet'),
    path('create_checkrole', checksheet_controller.checkrole_create, name='create_checkrole'),
    path('view_checkrole/<id>', checksheet_controller.view_checkrole, name='view_checkrole'),
    path('create_scandetails', checksheet_controller.scandetails_create, name='create_scandetails'),
    path('view_scandetails/<scan_details_id>', checksheet_controller.view_scandetails, name='view_scandetails'),
    path('create_shiftdetails', checksheet_controller.shiftdetails_create, name='create_shiftdetails'),
    path('view_shiftdetails/<shift_details_id>', checksheet_controller.view_shiftdetails, name='view_shiftdetails'),
    path('create_dropdown', checksheet_controller.dropdown_create, name='create_dropdown'),
    path('view_dropdown/<id>', checksheet_controller.view_dropdown, name='view_dropdown'),
    path('create_shiftmaintaince', Maintaince_controller.create_shiftmaintaince, name='create_shiftmaintaince'),
    path('view_shiftmaintaince/<time_maintenance_id>', Maintaince_controller.view_shiftmaintaince, name='view_shiftmaintaince'),
    path('create_PauseDetails', Maintaince_controller.create_PauseDetails, name='create_scanmaintaince'),
    path('view_PauseDetails/<id>', Maintaince_controller.view_PauseDetails, name='view_scanmaintaince'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
