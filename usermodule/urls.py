from django.urls import path
from usermodule.controller import devicecontroller, checksheet_controller, Maintaince_controller



urlpatterns=[
    path('device',devicecontroller.device_create,name='create_device'),
    path('device/<device_id>',devicecontroller.view_device,name='view_device'),
    path('operator',devicecontroller.operator_create,name='create_operator'),
    path('operator/<operator_id>',devicecontroller.view_operator,name='view_operator'),
    path('ecac',devicecontroller.ecac_create,name='create_ecac'),
    path('ecac/<ecac_id>',devicecontroller.view_ecac,name='view_ecac'),
    path('checksheet',checksheet_controller.checksheet_create,name='create_checksheet'),
    path('checksheet/<control_sheet_id>',checksheet_controller.view_checksheet,name='view_checksheet'),
    path('checkrole', checksheet_controller.checkrole_create, name='create_checkrole'),
    path('checkrole/<id>', checksheet_controller.view_checkrole, name='view_checkrole'),
    path('scandetails', checksheet_controller.scandetails_create, name='create_scandetails'),
    path('scandetails/<scan_details_id>', checksheet_controller.view_scandetails, name='view_scandetails'),
    path('shiftdetails', checksheet_controller.shiftdetails_create, name='create_shiftdetails'),
    path('shiftdetails/<shift_details_id>', checksheet_controller.view_shiftdetails, name='view_shiftdetails'),
    path('dropdown', checksheet_controller.dropdown_create, name='create_dropdown'),
    path('dropdown/<id>', checksheet_controller.view_dropdown, name='view_dropdown'),
    path('shiftmaintaince', Maintaince_controller.create_shiftmaintaince, name='create_shiftmaintaince'),
    path('shiftmaintaince/<time_maintenance_id>', Maintaince_controller.view_shiftmaintaince, name='view_shiftmaintaince'),
    path('PauseDetails', Maintaince_controller.create_PauseDetails, name='create_scanmaintaince'),
    path('PauseDetails/<pause_details_id>', Maintaince_controller.view_PauseDetails, name='view_scanmaintaince'),
    # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
