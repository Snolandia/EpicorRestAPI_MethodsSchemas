import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.WorkStationSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_WorkStations(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get WorkStations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WorkStations
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WorkStationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations",headers=creds) as resp:
           return await resp.json()

async def post_WorkStations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WorkStations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WorkStationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.WorkStationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_WorkStations_Company_WorkStationID(Company, WorkStationID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the WorkStation item
   Description: Calls GetByID to retrieve the WorkStation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WorkStation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkStationID: Desc: WorkStationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.WorkStationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations(" + Company + "," + WorkStationID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_WorkStations_Company_WorkStationID(Company, WorkStationID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update WorkStation for the service
   Description: Calls UpdateExt to update WorkStation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WorkStation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkStationID: Desc: WorkStationID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.WorkStationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations(" + Company + "," + WorkStationID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_WorkStations_Company_WorkStationID(Company, WorkStationID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete WorkStation item
   Description: Call UpdateExt to delete WorkStation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WorkStation
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkStationID: Desc: WorkStationID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations(" + Company + "," + WorkStationID + ")",headers=creds) as resp:
           return await resp.json()

async def get_WorkStations_Company_WorkStationID_Devices(Company, WorkStationID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get Devices items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Devices1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkStationID: Desc: WorkStationID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DeviceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations(" + Company + "," + WorkStationID + ")/Devices",headers=creds) as resp:
           return await resp.json()

async def get_WorkStations_Company_WorkStationID_Devices_Company_WorkStationID_Type_DefaultDevice(Company, WorkStationID, Type, DefaultDevice, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Device item
   Description: Calls GetByID to retrieve the Device item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Device1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkStationID: Desc: WorkStationID   Required: True   Allow empty value : True
      :param Type: Desc: Type   Required: True   Allow empty value : True
      :param DefaultDevice: Desc: DefaultDevice   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DeviceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/WorkStations(" + Company + "," + WorkStationID + ")/Devices(" + Company + "," + WorkStationID + "," + Type + "," + DefaultDevice + ")",headers=creds) as resp:
           return await resp.json()

async def get_Devices(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Devices items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Devices
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DeviceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/Devices",headers=creds) as resp:
           return await resp.json()

async def post_Devices(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Devices
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DeviceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DeviceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/Devices", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Devices_Company_WorkStationID_Type_DefaultDevice(Company, WorkStationID, Type, DefaultDevice, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Device item
   Description: Calls GetByID to retrieve the Device item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Device
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkStationID: Desc: WorkStationID   Required: True   Allow empty value : True
      :param Type: Desc: Type   Required: True   Allow empty value : True
      :param DefaultDevice: Desc: DefaultDevice   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DeviceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/Devices(" + Company + "," + WorkStationID + "," + Type + "," + DefaultDevice + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Devices_Company_WorkStationID_Type_DefaultDevice(Company, WorkStationID, Type, DefaultDevice, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Device for the service
   Description: Calls UpdateExt to update Device. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Device
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkStationID: Desc: WorkStationID   Required: True   Allow empty value : True
      :param Type: Desc: Type   Required: True   Allow empty value : True
      :param DefaultDevice: Desc: DefaultDevice   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DeviceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/Devices(" + Company + "," + WorkStationID + "," + Type + "," + DefaultDevice + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Devices_Company_WorkStationID_Type_DefaultDevice(Company, WorkStationID, Type, DefaultDevice, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Device item
   Description: Call UpdateExt to delete Device item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Device
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param WorkStationID: Desc: WorkStationID   Required: True   Allow empty value : True
      :param Type: Desc: Type   Required: True   Allow empty value : True
      :param DefaultDevice: Desc: DefaultDevice   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/Devices(" + Company + "," + WorkStationID + "," + Type + "," + DefaultDevice + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WorkstationListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseWorkStation, whereClauseDevice, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseWorkStation=" + whereClauseWorkStation
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDevice=" + whereClauseDevice
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(workStationID, epicorHeaders = None):
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
   params += "workStationID=" + workStationID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckDeviceTypeCount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckDeviceTypeCount
   Description: Deterimine if a default device has been defined
   OperationID: CheckDeviceTypeCount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckDeviceTypeCount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDeviceTypeCount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckForDefaultDeviceType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckForDefaultDeviceType
   Description: Deterimine if a default device has been defined
   OperationID: CheckForDefaultDeviceType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckForDefaultDeviceType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckForDefaultDeviceType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DuplicateStation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DuplicateStation
   Description: To create a new part by duplicating from another.
   OperationID: DuplicateStation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DuplicateStation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateStation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewWorkStation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewWorkStation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWorkStation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewWorkStation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWorkStation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDevice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDevice
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDevice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDevice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDevice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.WorkStationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DeviceRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DeviceRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkStationRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WorkStationRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WorkstationListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_WorkstationListRow] = obj["value"]
      pass

class Erp_Tablesets_DeviceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WorkStationID:str = obj["WorkStationID"]
      """  Unique identifier of the WorkStations  """  
      self.Description:str = obj["Description"]
      """  A Device Description that uniquely describes a device within a workstation  """  
      self.Comport:int = obj["Comport"]
      """  Comport setting for scale interface  """  
      self.BaudRate:int = obj["BaudRate"]
      """  BaudRate setting for scale  """  
      self.DataBits:int = obj["DataBits"]
      """  DataBits setting for scales  """  
      self.Parity:int = obj["Parity"]
      """  Parity setting for scales  """  
      self.StopBits:int = obj["StopBits"]
      """  StopBits setting for scales  """  
      self.TimeOut:int = obj["TimeOut"]
      """  TimeOut setting for scales  """  
      self.InquireMsg:str = obj["InquireMsg"]
      """  InquireMsg for scales  """  
      self.AppendCR:bool = obj["AppendCR"]
      """  AppendCR to append carrage return to scale interface  """  
      self.PrinterID:str = obj["PrinterID"]
      """  PrinterID for printer  """  
      self.PrinterUsage:str = obj["PrinterUsage"]
      """  PrinterUseage - Use defined for this printer at a WorkStation. Valid values are Forms, Reports and Labels.  """  
      self.Type:str = obj["Type"]
      """  Device Type - valid values are Scale or Printer  """  
      self.DefaultDevice:bool = obj["DefaultDevice"]
      """  This checkbox will designate the device to use when there are multiple devices of the same type within a workstation.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.USBVendorID:str = obj["USBVendorID"]
      """  USBVendorID  """  
      self.USBProductID:str = obj["USBProductID"]
      """  USBProductID  """  
      self.USBUOM:str = obj["USBUOM"]
      """  USBUOM  """  
      self.USBUsagePage:int = obj["USBUsagePage"]
      """  USBUsagePage  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SysPrinterDescription:str = obj["SysPrinterDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WorkStationRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WorkStationID:str = obj["WorkStationID"]
      """  Unique identifier of the WorkStations  """  
      self.Description:str = obj["Description"]
      """  Description of the station  """  
      self.AutoQty:bool = obj["AutoQty"]
      """  If yes, the pack station will automatically enter '1' for the quantity  """  
      self.WeightType:str = obj["WeightType"]
      """   Describes how the weight is getting inputed
W = Prompt for Weight, P = Get Weight from Part, S = Get Weight from Scale  """  
      self.UseManifest:bool = obj["UseManifest"]
      """  If yes then enable manifest fields for entry  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Defines which warehouse is to be used as the Warehouse for this station.  This must be a valid record in the Warehouse master file. It can't be blank.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location for this Packing Station.  Bin Number cannot be blank.  """  
      self.WebServiceUrl:str = obj["WebServiceUrl"]
      """  URL for Pack Out manifest information  """  
      self.Type:str = obj["Type"]
      """  Defines WorkStation Type valid values are "Pack" and "Other"  """  
      self.WeightCaptPt:str = obj["WeightCaptPt"]
      """  Must contain the following values:    Carton,  Master Pack or  Both. If "Carton is selected, the weight is acquired for each carton and each carton is manifested separately.  If Master Pack is selected, the weight is acquired for the master pack, and only the master pack is manifested.  If Both selected, weight is acquired either at Pack or Master Pack  """  
      self.TransWUM:str = obj["TransWUM"]
      """  Unit of Measure of the Weight Class that is used as a default for the Shipping Total Weight.  """  
      self.SizeUOM:str = obj["SizeUOM"]
      """   Unit of measure used to qualify the Lenth, Height, Width to be used in the manifest.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")
System will take the length, width and height and the UOM defined in the package and will convert it to the length UOM defined in the manifest settings.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TimeOut:int = obj["TimeOut"]
      """  Specify how long in seconds  the client will wait for a response from your Freight Service  """  
      self.LogManifestMsg:bool = obj["LogManifestMsg"]
      """  Enable to Log Manifest Request and Response XML Messages to the file. Enabled to the System manager only  """  
      self.WhseList:str = obj["WhseList"]
      self.EnableLogManifestMsg:bool = obj["EnableLogManifestMsg"]
      self.DispLogManifest:bool = obj["DispLogManifest"]
      """  This flag is to show/hide Log Manufest and TimeOut fields based on Freight Service Integration that user selected in Company configuration  """  
      self.BitFlag:int = obj["BitFlag"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WorkstationListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WorkStationID:str = obj["WorkStationID"]
      """  Unique identifier of the WorkStations  """  
      self.Description:str = obj["Description"]
      """  Description of the station  """  
      self.AutoQty:bool = obj["AutoQty"]
      """  If yes, the pack station will automatically enter '1' for the quantity  """  
      self.WeightType:str = obj["WeightType"]
      """   Describes how the weight is getting inputed
W = Prompt for Weight, P = Get Weight from Part, S = Get Weight from Scale  """  
      self.UseManifest:bool = obj["UseManifest"]
      """  If yes then enable manifest fields for entry  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Defines which warehouse is to be used as the Warehouse for this station.  This must be a valid record in the Warehouse master file. It can't be blank.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location for this Packing Station.  Bin Number cannot be blank.  """  
      self.WebServiceUrl:str = obj["WebServiceUrl"]
      """  URL for Pack Out manifest information  """  
      self.Type:str = obj["Type"]
      """  Defines WorkStation Type valid values are "Pack" and "Other"  """  
      self.WeightCaptPt:str = obj["WeightCaptPt"]
      """  Must contain the following values:    Carton,  Master Pack or  Both. If "Carton is selected, the weight is acquired for each carton and each carton is manifested separately.  If Master Pack is selected, the weight is acquired for the master pack, and only the master pack is manifested.  If Both selected, weight is acquired either at Pack or Master Pack  """  
      self.TransWUM:str = obj["TransWUM"]
      """  Unit of Measure of the Weight Class that is used as a default for the Shipping Total Weight.  """  
      self.SizeUOM:str = obj["SizeUOM"]
      """   Unit of measure used to qualify the Lenth, Height, Width to be used in the manifest.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")
System will take the length, width and height and the UOM defined in the package and will convert it to the length UOM defined in the manifest settings.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WhseList:str = obj["WhseList"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckDeviceTypeCount_input:
   """ Required : 
   ipworkstationID
   ipdeviceType
   ds
   """  
   def __init__(self, obj):
      self.ipworkstationID:str = obj["ipworkstationID"]
      """  Workstation ID  """  
      self.ipdeviceType:str = obj["ipdeviceType"]
      """  Scale or Printer  """  
      self.ds:list[Erp_Tablesets_WorkStationTableset] = obj["ds"]
      pass

class CheckDeviceTypeCount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WorkStationTableset] = obj["ds"]
      self.deviceWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckForDefaultDeviceType_input:
   """ Required : 
   workstationID
   deviceType
   """  
   def __init__(self, obj):
      self.workstationID:str = obj["workstationID"]
      """  Workstation ID  """  
      self.deviceType:str = obj["deviceType"]
      """  Scale or Printer  """  
      pass

class CheckForDefaultDeviceType_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   workStationID
   """  
   def __init__(self, obj):
      self.workStationID:str = obj["workStationID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DuplicateStation_input:
   """ Required : 
   sourceStationID
   targetStationID
   """  
   def __init__(self, obj):
      self.sourceStationID:str = obj["sourceStationID"]
      """  Source Station ID  """  
      self.targetStationID:str = obj["targetStationID"]
      """  Target Station ID  """  
      pass

class DuplicateStation_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WorkStationTableset] = obj["returnObj"]
      pass

class Erp_Tablesets_DeviceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WorkStationID:str = obj["WorkStationID"]
      """  Unique identifier of the WorkStations  """  
      self.Description:str = obj["Description"]
      """  A Device Description that uniquely describes a device within a workstation  """  
      self.Comport:int = obj["Comport"]
      """  Comport setting for scale interface  """  
      self.BaudRate:int = obj["BaudRate"]
      """  BaudRate setting for scale  """  
      self.DataBits:int = obj["DataBits"]
      """  DataBits setting for scales  """  
      self.Parity:int = obj["Parity"]
      """  Parity setting for scales  """  
      self.StopBits:int = obj["StopBits"]
      """  StopBits setting for scales  """  
      self.TimeOut:int = obj["TimeOut"]
      """  TimeOut setting for scales  """  
      self.InquireMsg:str = obj["InquireMsg"]
      """  InquireMsg for scales  """  
      self.AppendCR:bool = obj["AppendCR"]
      """  AppendCR to append carrage return to scale interface  """  
      self.PrinterID:str = obj["PrinterID"]
      """  PrinterID for printer  """  
      self.PrinterUsage:str = obj["PrinterUsage"]
      """  PrinterUseage - Use defined for this printer at a WorkStation. Valid values are Forms, Reports and Labels.  """  
      self.Type:str = obj["Type"]
      """  Device Type - valid values are Scale or Printer  """  
      self.DefaultDevice:bool = obj["DefaultDevice"]
      """  This checkbox will designate the device to use when there are multiple devices of the same type within a workstation.  """  
      self.DeviceUOM:str = obj["DeviceUOM"]
      """  Unit of Measure of the Device (Scale) that is used at the time a pack is weighed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.USBVendorID:str = obj["USBVendorID"]
      """  USBVendorID  """  
      self.USBProductID:str = obj["USBProductID"]
      """  USBProductID  """  
      self.USBUOM:str = obj["USBUOM"]
      """  USBUOM  """  
      self.USBUsagePage:int = obj["USBUsagePage"]
      """  USBUsagePage  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SysPrinterDescription:str = obj["SysPrinterDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtWorkStationTableset:
   def __init__(self, obj):
      self.WorkStation:list[Erp_Tablesets_WorkStationRow] = obj["WorkStation"]
      self.Device:list[Erp_Tablesets_DeviceRow] = obj["Device"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WorkStationRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WorkStationID:str = obj["WorkStationID"]
      """  Unique identifier of the WorkStations  """  
      self.Description:str = obj["Description"]
      """  Description of the station  """  
      self.AutoQty:bool = obj["AutoQty"]
      """  If yes, the pack station will automatically enter '1' for the quantity  """  
      self.WeightType:str = obj["WeightType"]
      """   Describes how the weight is getting inputed
W = Prompt for Weight, P = Get Weight from Part, S = Get Weight from Scale  """  
      self.UseManifest:bool = obj["UseManifest"]
      """  If yes then enable manifest fields for entry  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Defines which warehouse is to be used as the Warehouse for this station.  This must be a valid record in the Warehouse master file. It can't be blank.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location for this Packing Station.  Bin Number cannot be blank.  """  
      self.WebServiceUrl:str = obj["WebServiceUrl"]
      """  URL for Pack Out manifest information  """  
      self.Type:str = obj["Type"]
      """  Defines WorkStation Type valid values are "Pack" and "Other"  """  
      self.WeightCaptPt:str = obj["WeightCaptPt"]
      """  Must contain the following values:    Carton,  Master Pack or  Both. If "Carton is selected, the weight is acquired for each carton and each carton is manifested separately.  If Master Pack is selected, the weight is acquired for the master pack, and only the master pack is manifested.  If Both selected, weight is acquired either at Pack or Master Pack  """  
      self.TransWUM:str = obj["TransWUM"]
      """  Unit of Measure of the Weight Class that is used as a default for the Shipping Total Weight.  """  
      self.SizeUOM:str = obj["SizeUOM"]
      """   Unit of measure used to qualify the Lenth, Height, Width to be used in the manifest.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")
System will take the length, width and height and the UOM defined in the package and will convert it to the length UOM defined in the manifest settings.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TimeOut:int = obj["TimeOut"]
      """  Specify how long in seconds  the client will wait for a response from your Freight Service  """  
      self.LogManifestMsg:bool = obj["LogManifestMsg"]
      """  Enable to Log Manifest Request and Response XML Messages to the file. Enabled to the System manager only  """  
      self.WhseList:str = obj["WhseList"]
      self.EnableLogManifestMsg:bool = obj["EnableLogManifestMsg"]
      self.DispLogManifest:bool = obj["DispLogManifest"]
      """  This flag is to show/hide Log Manufest and TimeOut fields based on Freight Service Integration that user selected in Company configuration  """  
      self.BitFlag:int = obj["BitFlag"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WorkStationTableset:
   def __init__(self, obj):
      self.WorkStation:list[Erp_Tablesets_WorkStationRow] = obj["WorkStation"]
      self.Device:list[Erp_Tablesets_DeviceRow] = obj["Device"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_WorkstationListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WorkStationID:str = obj["WorkStationID"]
      """  Unique identifier of the WorkStations  """  
      self.Description:str = obj["Description"]
      """  Description of the station  """  
      self.AutoQty:bool = obj["AutoQty"]
      """  If yes, the pack station will automatically enter '1' for the quantity  """  
      self.WeightType:str = obj["WeightType"]
      """   Describes how the weight is getting inputed
W = Prompt for Weight, P = Get Weight from Part, S = Get Weight from Scale  """  
      self.UseManifest:bool = obj["UseManifest"]
      """  If yes then enable manifest fields for entry  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Defines which warehouse is to be used as the Warehouse for this station.  This must be a valid record in the Warehouse master file. It can't be blank.  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location for this Packing Station.  Bin Number cannot be blank.  """  
      self.WebServiceUrl:str = obj["WebServiceUrl"]
      """  URL for Pack Out manifest information  """  
      self.Type:str = obj["Type"]
      """  Defines WorkStation Type valid values are "Pack" and "Other"  """  
      self.WeightCaptPt:str = obj["WeightCaptPt"]
      """  Must contain the following values:    Carton,  Master Pack or  Both. If "Carton is selected, the weight is acquired for each carton and each carton is manifested separately.  If Master Pack is selected, the weight is acquired for the master pack, and only the master pack is manifested.  If Both selected, weight is acquired either at Pack or Master Pack  """  
      self.TransWUM:str = obj["TransWUM"]
      """  Unit of Measure of the Weight Class that is used as a default for the Shipping Total Weight.  """  
      self.SizeUOM:str = obj["SizeUOM"]
      """   Unit of measure used to qualify the Lenth, Height, Width to be used in the manifest.
Must be valid in the standard "Length" UOMs  (UOMClass.ClassType = "Length")
System will take the length, width and height and the UOM defined in the package and will convert it to the length UOM defined in the manifest settings.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.WhseList:str = obj["WhseList"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_WorkstationListTableset:
   def __init__(self, obj):
      self.WorkstationList:list[Erp_Tablesets_WorkstationListRow] = obj["WorkstationList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   workStationID
   """  
   def __init__(self, obj):
      self.workStationID:str = obj["workStationID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WorkStationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WorkStationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WorkStationTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      self.fieldName:str = obj["fieldName"]
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_WorkstationListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDevice_input:
   """ Required : 
   ds
   workStationID
   type
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WorkStationTableset] = obj["ds"]
      self.workStationID:str = obj["workStationID"]
      self.type:str = obj["type"]
      pass

class GetNewDevice_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WorkStationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewWorkStation_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WorkStationTableset] = obj["ds"]
      pass

class GetNewWorkStation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WorkStationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseWorkStation
   whereClauseDevice
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseWorkStation:str = obj["whereClauseWorkStation"]
      self.whereClauseDevice:str = obj["whereClauseDevice"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_WorkStationTableset] = obj["returnObj"]
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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWorkStationTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtWorkStationTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_WorkStationTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_WorkStationTableset] = obj["ds"]
      pass

      """  output parameters  """  

