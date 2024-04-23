import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.IoTDeviceSvc
# Description: IoT Device allowing configuration and communication with IoT Hub
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_IoTDevices(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IoTDevices items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IoTDevices
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IoTDeviceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDevices",headers=creds) as resp:
           return await resp.json()

async def post_IoTDevices(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IoTDevices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.IoTDeviceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.IoTDeviceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDevices", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IoTDevices_Company_DeviceID(Company, DeviceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IoTDevice item
   Description: Calls GetByID to retrieve the IoTDevice item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IoTDevice
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeviceID: Desc: DeviceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IoTDeviceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDevices(" + Company + "," + DeviceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IoTDevices_Company_DeviceID(Company, DeviceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IoTDevice for the service
   Description: Calls UpdateExt to update IoTDevice. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IoTDevice
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeviceID: Desc: DeviceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.IoTDeviceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDevices(" + Company + "," + DeviceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IoTDevices_Company_DeviceID(Company, DeviceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IoTDevice item
   Description: Call UpdateExt to delete IoTDevice item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IoTDevice
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeviceID: Desc: DeviceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDevices(" + Company + "," + DeviceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_IoTDeviceRules(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IoTDeviceRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IoTDeviceRules
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IoTDeviceRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceRules",headers=creds) as resp:
           return await resp.json()

async def post_IoTDeviceRules(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IoTDeviceRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.IoTDeviceRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.IoTDeviceRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceRules", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IoTDeviceRules_Company_DeviceID_RuleID(Company, DeviceID, RuleID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IoTDeviceRule item
   Description: Calls GetByID to retrieve the IoTDeviceRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IoTDeviceRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeviceID: Desc: DeviceID   Required: True   Allow empty value : True
      :param RuleID: Desc: RuleID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IoTDeviceRuleRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceRules(" + Company + "," + DeviceID + "," + RuleID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IoTDeviceRules_Company_DeviceID_RuleID(Company, DeviceID, RuleID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IoTDeviceRule for the service
   Description: Calls UpdateExt to update IoTDeviceRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IoTDeviceRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeviceID: Desc: DeviceID   Required: True   Allow empty value : True
      :param RuleID: Desc: RuleID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.IoTDeviceRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceRules(" + Company + "," + DeviceID + "," + RuleID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IoTDeviceRules_Company_DeviceID_RuleID(Company, DeviceID, RuleID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IoTDeviceRule item
   Description: Call UpdateExt to delete IoTDeviceRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IoTDeviceRule
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeviceID: Desc: DeviceID   Required: True   Allow empty value : True
      :param RuleID: Desc: RuleID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceRules(" + Company + "," + DeviceID + "," + RuleID + ")",headers=creds) as resp:
           return await resp.json()

async def get_IoTDeviceStatus(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IoTDeviceStatus items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IoTDeviceStatus
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IoTDeviceStatusRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceStatus",headers=creds) as resp:
           return await resp.json()

async def post_IoTDeviceStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IoTDeviceStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.IoTDeviceStatusRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.IoTDeviceStatusRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceStatus", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IoTDeviceStatus_Company_DeviceID(Company, DeviceID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IoTDeviceStatu item
   Description: Calls GetByID to retrieve the IoTDeviceStatu item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IoTDeviceStatu
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeviceID: Desc: DeviceID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.IoTDeviceStatusRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceStatus(" + Company + "," + DeviceID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IoTDeviceStatus_Company_DeviceID(Company, DeviceID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IoTDeviceStatu for the service
   Description: Calls UpdateExt to update IoTDeviceStatu. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IoTDeviceStatu
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeviceID: Desc: DeviceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.IoTDeviceStatusRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceStatus(" + Company + "," + DeviceID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IoTDeviceStatus_Company_DeviceID(Company, DeviceID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IoTDeviceStatu item
   Description: Call UpdateExt to delete IoTDeviceStatu item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IoTDeviceStatu
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeviceID: Desc: DeviceID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/IoTDeviceStatus(" + Company + "," + DeviceID + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.IoTDeviceListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseIoTDevice, whereClauseIoTDeviceRule, whereClauseIoTDeviceStatus, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseIoTDevice=" + whereClauseIoTDevice
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseIoTDeviceRule=" + whereClauseIoTDeviceRule
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseIoTDeviceStatus=" + whereClauseIoTDeviceStatus
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(deviceID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "deviceID=" + deviceID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableRelatedTo(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableRelatedTo
   Description: Gets a list of available related to which have searches available.
   OperationID: GetAvailableRelatedTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableRelatedTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDeviceRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDeviceRules
   Description: Deprecated: the method is used for the classic UI only.
Get applicable rules for the Device and whether they are currently active
This includes any assigned by associated group. Inactive rules are not included.
   OperationID: GetDeviceRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDeviceRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeviceRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDeviceStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDeviceStatus
   Description: Deprecated: the method is used for the classic UI only.
Get the status of a device from IoT Hub
   OperationID: GetDeviceStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDeviceStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeviceStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDeviceTwin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDeviceTwin
   Description: Get all the Device Twin Properties from IoT Hub
   OperationID: GetDeviceTwin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDeviceTwin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeviceTwin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateDeviceTwin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateDeviceTwin
   Description: Update the Device Twin desired properties for a device
   OperationID: UpdateDeviceTwin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDeviceTwin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDeviceTwin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SendDeviceMessage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SendDeviceMessage
   Description: Sends a Cloud to Device message via the IoT Hub
   OperationID: SendDeviceMessage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SendDeviceMessage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendDeviceMessage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SendDeviceData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SendDeviceData
   Description: Sends a Cloud to Device message via the IoT Hub
   OperationID: SendDeviceData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SendDeviceData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SendDeviceData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RetrieveMissingDevicesFromIoTHuB(epicorHeaders = None):
   """  
   Summary: Invoke method RetrieveMissingDevicesFromIoTHuB
   Description: Get a dataset of devices that exist in IoT Hub but have not been configured within ERP
   OperationID: RetrieveMissingDevicesFromIoTHuB
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveMissingDevicesFromIoTHuB_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetMissingDevicesFromIoTHub(epicorHeaders = None):
   """  
   Summary: Invoke method GetMissingDevicesFromIoTHub
   Description: Deprecated: the method is used for the classic UI only.
Get a list of devices that exist in IoT Hub but have not been configured within ERP
   OperationID: GetMissingDevicesFromIoTHub
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMissingDevicesFromIoTHub_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_UpdateDevicesToERPFromIoTHub(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateDevicesToERPFromIoTHub
   Description: Add one or more devices that exist in the IoT Hub but have not yet been created within ERP
   OperationID: UpdateDevicesToERPFromIoTHub
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateDevicesToERPFromIoTHub_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateDevicesToERPFromIoTHub_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddMissingDevicesFromIoTHub(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddMissingDevicesFromIoTHub
   Description: Deprecated: the method is used for the classic UI only.
Add one or more devices that exist in the IoT Hub but have not yet been created within ERP
   OperationID: AddMissingDevicesFromIoTHub
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddMissingDevicesFromIoTHub_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddMissingDevicesFromIoTHub_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UploadDevicesToIoTHub(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UploadDevicesToIoTHub
   Description: Add one or more devices that exist in ERP but have not yet been created within IoT Hub
   OperationID: UploadDevicesToIoTHub
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadDevicesToIoTHub_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadDevicesToIoTHub_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddDevicesToIoTHub(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddDevicesToIoTHub
   Description: Deprecated: the method is used for the classic UI only.
Add one or more devices that exist in ERP but have not yet been created within IoT Hub
   OperationID: AddDevicesToIoTHub
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddDevicesToIoTHub_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddDevicesToIoTHub_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateDeviceGroupID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateDeviceGroupID
   Description: Verifies if a device group ID is valid
   OperationID: ValidateDeviceGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateDeviceGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDeviceGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UploadImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UploadImage
   Description: Upload an image for the Device to be used on the widget
   OperationID: UploadImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UploadImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UploadImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveImage
   Description: Remove an image for the Device
   OperationID: RemoveImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DownloadImage(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DownloadImage
   Description: Download an image assigned to a Device. If there is no image assigned nothing is returned
   OperationID: DownloadImage
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DownloadImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DownloadImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSysRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSysRowID
   OperationID: ChangeSysRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSysRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RetrieveDeviceRules(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrieveDeviceRules
   Description: Get applicable rules for the Device and whether they are currently active
This includes any assigned by associated group. Inactive rules are not included.
   OperationID: RetrieveDeviceRules
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveDeviceRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveDeviceRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RetrieveDeviceStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrieveDeviceStatus
   Description: Get the status of a device from IoT Hub
   OperationID: RetrieveDeviceStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrieveDeviceStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveDeviceStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDeviceTwinDatasetForTree(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDeviceTwinDatasetForTree
   Description: Get all the Device Twin Properties from IoT Hub
   OperationID: GetDeviceTwinDatasetForTree
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDeviceTwinDatasetForTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDeviceTwinDatasetForTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRelatedToKeyDescription(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRelatedToKeyDescription
   Description: Get Related To Description
   OperationID: GetRelatedToKeyDescription
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRelatedToKeyDescription_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelatedToKeyDescription_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultSearch
   Description: Get default search for specified table
   OperationID: GetDefaultSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIoTDevice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIoTDevice
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIoTDevice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIoTDevice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIoTDevice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.IoTDeviceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_IoTDeviceListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_IoTDeviceRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceRuleRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_IoTDeviceRuleRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_IoTDeviceStatusRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_IoTDeviceStatusRow] = obj["value"]
      pass

class Ice_Tablesets_IoTDeviceListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeviceID:str = obj["DeviceID"]
      """  DeviceID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IoTDeviceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeviceID:str = obj["DeviceID"]
      """  DeviceID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RelatedToDescription:str = obj["RelatedToDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.IoTDeviceGroupLinkDescription:str = obj["IoTDeviceGroupLinkDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IoTDeviceRuleRow:
   def __init__(self, obj):
      self.Active:bool = obj["Active"]
      self.Company:str = obj["Company"]
      self.Description:str = obj["Description"]
      self.DeviceID:str = obj["DeviceID"]
      self.RuleID:str = obj["RuleID"]
      self.Stateful:bool = obj["Stateful"]
      self.StoreEventData:bool = obj["StoreEventData"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IoTDeviceStatusRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DeviceID:str = obj["DeviceID"]
      self.DeviceOnline:bool = obj["DeviceOnline"]
      self.DeviceStatus:str = obj["DeviceStatus"]
      self.HubRegistered:bool = obj["HubRegistered"]
      self.IoTEdge:bool = obj["IoTEdge"]
      self.AuthenticationType:str = obj["AuthenticationType"]
      self.LastActivity:str = obj["LastActivity"]
      self.LastStatusUpdate:str = obj["LastStatusUpdate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AddDevicesToIoTHub_input:
   """ Required : 
   deviceIDs
   """  
   def __init__(self, obj):
      self.deviceIDs:str = obj["deviceIDs"]
      pass

class AddDevicesToIoTHub_output:
   def __init__(self, obj):
      pass

class AddMissingDevicesFromIoTHub_input:
   """ Required : 
   deviceIDs
   """  
   def __init__(self, obj):
      self.deviceIDs:str = obj["deviceIDs"]
      """  Collection of Device IDs  """  
      pass

class AddMissingDevicesFromIoTHub_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeSysRowID_input:
   """ Required : 
   sysRowID
   ds
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      self.ds:list[Ice_Tablesets_IoTDeviceTableset] = obj["ds"]
      pass

class ChangeSysRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_IoTDeviceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   deviceID
   """  
   def __init__(self, obj):
      self.deviceID:str = obj["deviceID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DownloadImage_input:
   """ Required : 
   deviceID
   """  
   def __init__(self, obj):
      self.deviceID:str = obj["deviceID"]
      """  Device ID  """  
      pass

class DownloadImage_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Image data  """  
      pass

   def parameters(self, obj):
      self.fileName:str = obj["parameters"]
      self.mimeType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAvailableRelatedTo_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IoTDeviceRelatedToTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   deviceID
   """  
   def __init__(self, obj):
      self.deviceID:str = obj["deviceID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IoTDeviceTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IoTDeviceTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IoTDeviceTableset] = obj["returnObj"]
      pass

class GetDefaultSearch_input:
   """ Required : 
   systemCode
   tableName
   """  
   def __init__(self, obj):
      self.systemCode:str = obj["systemCode"]
      """  System code of the table  """  
      self.tableName:str = obj["tableName"]
      """  Name of the table  """  
      pass

class GetDefaultSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.folderName:str = obj["parameters"]
      self.subfolderName:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDeviceRules_input:
   """ Required : 
   ts
   deviceID
   """  
   def __init__(self, obj):
      self.ts:list[Ice_Tablesets_IoTDeviceTableset] = obj["ts"]
      self.deviceID:str = obj["deviceID"]
      """  Device ID  """  
      pass

class GetDeviceRules_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ts:list[Ice_Tablesets_IoTDeviceTableset] = obj["ts"]
      pass

      """  output parameters  """  

class GetDeviceStatus_input:
   """ Required : 
   ts
   deviceID
   """  
   def __init__(self, obj):
      self.ts:list[Ice_Tablesets_IoTDeviceTableset] = obj["ts"]
      self.deviceID:str = obj["deviceID"]
      """  Device ID  """  
      pass

class GetDeviceStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ts:list[Ice_Tablesets_IoTDeviceTableset] = obj["ts"]
      pass

      """  output parameters  """  

class GetDeviceTwinDatasetForTree_input:
   """ Required : 
   deviceID
   errorOnNotFound
   """  
   def __init__(self, obj):
      self.deviceID:str = obj["deviceID"]
      """  Device ID within Company  """  
      self.errorOnNotFound:bool = obj["errorOnNotFound"]
      """  Flag whether to error if the twin is not found  """  
      pass

class GetDeviceTwinDatasetForTree_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IoTDeviceTwinTableset] = obj["returnObj"]
      pass

class GetDeviceTwin_input:
   """ Required : 
   deviceID
   errorOnNotFound
   """  
   def __init__(self, obj):
      self.deviceID:str = obj["deviceID"]
      """  Device ID within Company  """  
      self.errorOnNotFound:bool = obj["errorOnNotFound"]
      """  Flag whether to error if the twin is not found  """  
      pass

class GetDeviceTwin_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Device JSON Twin  """  
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IoTDeviceListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMissingDevicesFromIoTHub_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Collection of Device IDs  """  
      pass

class GetNewIoTDevice_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_IoTDeviceTableset] = obj["ds"]
      pass

class GetNewIoTDevice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_IoTDeviceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRelatedToKeyDescription_input:
   """ Required : 
   schemaName
   tableName
   sysRowID
   """  
   def __init__(self, obj):
      self.schemaName:str = obj["schemaName"]
      """  Related To Schema Name  """  
      self.tableName:str = obj["tableName"]
      """  Related To Table Name  """  
      self.sysRowID:str = obj["sysRowID"]
      """  Related To SysRowID  """  
      pass

class GetRelatedToKeyDescription_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  RelatedToDescription string  """  
      pass

class GetRows_input:
   """ Required : 
   whereClauseIoTDevice
   whereClauseIoTDeviceRule
   whereClauseIoTDeviceStatus
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseIoTDevice:str = obj["whereClauseIoTDevice"]
      self.whereClauseIoTDeviceRule:str = obj["whereClauseIoTDeviceRule"]
      self.whereClauseIoTDeviceStatus:str = obj["whereClauseIoTDeviceStatus"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IoTDeviceTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class Ice_Tablesets_IoTDeviceListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeviceID:str = obj["DeviceID"]
      """  DeviceID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IoTDeviceListTableset:
   def __init__(self, obj):
      self.IoTDeviceList:list[Ice_Tablesets_IoTDeviceListRow] = obj["IoTDeviceList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_IoTDeviceRelatedToRow:
   def __init__(self, obj):
      self.SystemCode:str = obj["SystemCode"]
      self.ClassName:str = obj["ClassName"]
      self.DataTableID:str = obj["DataTableID"]
      self.DBTableName:str = obj["DBTableName"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IoTDeviceRelatedToTableset:
   def __init__(self, obj):
      self.IoTDeviceRelatedTo:list[Ice_Tablesets_IoTDeviceRelatedToRow] = obj["IoTDeviceRelatedTo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_IoTDeviceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DeviceID:str = obj["DeviceID"]
      """  DeviceID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RelatedToDescription:str = obj["RelatedToDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.IoTDeviceGroupLinkDescription:str = obj["IoTDeviceGroupLinkDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IoTDeviceRuleRow:
   def __init__(self, obj):
      self.Active:bool = obj["Active"]
      self.Company:str = obj["Company"]
      self.Description:str = obj["Description"]
      self.DeviceID:str = obj["DeviceID"]
      self.RuleID:str = obj["RuleID"]
      self.Stateful:bool = obj["Stateful"]
      self.StoreEventData:bool = obj["StoreEventData"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IoTDeviceSelectionRow:
   def __init__(self, obj):
      self.DeviceID:str = obj["DeviceID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IoTDeviceSelectionTableset:
   def __init__(self, obj):
      self.IoTDeviceSelection:list[Ice_Tablesets_IoTDeviceSelectionRow] = obj["IoTDeviceSelection"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_IoTDeviceStatusRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DeviceID:str = obj["DeviceID"]
      self.DeviceOnline:bool = obj["DeviceOnline"]
      self.DeviceStatus:str = obj["DeviceStatus"]
      self.HubRegistered:bool = obj["HubRegistered"]
      self.IoTEdge:bool = obj["IoTEdge"]
      self.AuthenticationType:str = obj["AuthenticationType"]
      self.LastActivity:str = obj["LastActivity"]
      self.LastStatusUpdate:str = obj["LastStatusUpdate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IoTDeviceTableset:
   def __init__(self, obj):
      self.IoTDevice:list[Ice_Tablesets_IoTDeviceRow] = obj["IoTDevice"]
      self.IoTDeviceRule:list[Ice_Tablesets_IoTDeviceRuleRow] = obj["IoTDeviceRule"]
      self.IoTDeviceStatus:list[Ice_Tablesets_IoTDeviceStatusRow] = obj["IoTDeviceStatus"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_IoTDeviceTwinDataRow:
   def __init__(self, obj):
      self.Id:int = obj["Id"]
      self.ParentId:int = obj["ParentId"]
      self.Key:str = obj["Key"]
      self.Value:str = obj["Value"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_IoTDeviceTwinTableset:
   def __init__(self, obj):
      self.IoTDeviceTwinData:list[Ice_Tablesets_IoTDeviceTwinDataRow] = obj["IoTDeviceTwinData"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtIoTDeviceTableset:
   def __init__(self, obj):
      self.IoTDevice:list[Ice_Tablesets_IoTDeviceRow] = obj["IoTDevice"]
      self.IoTDeviceRule:list[Ice_Tablesets_IoTDeviceRuleRow] = obj["IoTDeviceRule"]
      self.IoTDeviceStatus:list[Ice_Tablesets_IoTDeviceStatusRow] = obj["IoTDeviceStatus"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class RemoveImage_input:
   """ Required : 
   deviceID
   """  
   def __init__(self, obj):
      self.deviceID:str = obj["deviceID"]
      """  Device ID  """  
      pass

class RemoveImage_output:
   def __init__(self, obj):
      pass

class RetrieveDeviceRules_input:
   """ Required : 
   deviceID
   """  
   def __init__(self, obj):
      self.deviceID:str = obj["deviceID"]
      """  Device ID  """  
      pass

class RetrieveDeviceRules_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IoTDeviceTableset] = obj["returnObj"]
      pass

class RetrieveDeviceStatus_input:
   """ Required : 
   deviceID
   """  
   def __init__(self, obj):
      self.deviceID:str = obj["deviceID"]
      """  Device ID  """  
      pass

class RetrieveDeviceStatus_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IoTDeviceTableset] = obj["returnObj"]
      pass

class RetrieveMissingDevicesFromIoTHuB_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_IoTDeviceSelectionTableset] = obj["returnObj"]
      pass

class SendDeviceData_input:
   """ Required : 
   deviceID
   byteArray
   """  
   def __init__(self, obj):
      self.deviceID:str = obj["deviceID"]
      """  Device ID  """  
      self.byteArray:str = obj["byteArray"]
      """  Byte data  """  
      pass

class SendDeviceData_output:
   def __init__(self, obj):
      pass

class SendDeviceMessage_input:
   """ Required : 
   deviceID
   message
   """  
   def __init__(self, obj):
      self.deviceID:str = obj["deviceID"]
      """  Device ID  """  
      self.message:str = obj["message"]
      """  Message encoded as UTF8  """  
      pass

class SendDeviceMessage_output:
   def __init__(self, obj):
      pass

class UpdateDeviceTwin_input:
   """ Required : 
   deviceID
   jsonTwinPatch
   """  
   def __init__(self, obj):
      self.deviceID:str = obj["deviceID"]
      """  Device ID within Company  """  
      self.jsonTwinPatch:str = obj["jsonTwinPatch"]
      """  JSON Twin patch data  """  
      pass

class UpdateDeviceTwin_output:
   def __init__(self, obj):
      pass

class UpdateDevicesToERPFromIoTHub_input:
   """ Required : 
   deviceIDs
   """  
   def __init__(self, obj):
      self.deviceIDs:str = obj["deviceIDs"]
      """  String of Device IDs delimeted by '~'  """  
      pass

class UpdateDevicesToERPFromIoTHub_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  message  """  
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtIoTDeviceTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtIoTDeviceTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_IoTDeviceTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_IoTDeviceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UploadDevicesToIoTHub_input:
   """ Required : 
   deviceIDs
   """  
   def __init__(self, obj):
      self.deviceIDs:str = obj["deviceIDs"]
      """  String of Device IDs delimeted by '~'  """  
      pass

class UploadDevicesToIoTHub_output:
   def __init__(self, obj):
      pass

class UploadImage_input:
   """ Required : 
   deviceID
   data
   fileName
   """  
   def __init__(self, obj):
      self.deviceID:str = obj["deviceID"]
      """  Device ID  """  
      self.data:str = obj["data"]
      """  Image data  """  
      self.fileName:str = obj["fileName"]
      """  Filename of image  """  
      pass

class UploadImage_output:
   def __init__(self, obj):
      pass

class ValidateDeviceGroupID_input:
   """ Required : 
   deviceGroupID
   """  
   def __init__(self, obj):
      self.deviceGroupID:str = obj["deviceGroupID"]
      """  GroupID to validate  """  
      pass

class ValidateDeviceGroupID_output:
   def __init__(self, obj):
      pass

