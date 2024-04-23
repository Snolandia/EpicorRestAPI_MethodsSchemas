import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.APITraceSvc
# Description: API Trace service.
Allows to monitor server resource consumption.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_APITraces(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APITraces items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APITraces
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.APITraceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/APITraces",headers=creds) as resp:
           return await resp.json()

async def post_APITraces(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APITraces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.APITraceRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.APITraceRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/APITraces", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APITraces_Company_TenantID_ServiceName_ServiceMethod_CallDate_CalledFrom_UserID(Company, TenantID, ServiceName, ServiceMethod, CallDate, CalledFrom, UserID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APITrace item
   Description: Calls GetByID to retrieve the APITrace item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APITrace
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TenantID: Desc: TenantID   Required: True   Allow empty value : True
      :param ServiceName: Desc: ServiceName   Required: True   Allow empty value : True
      :param ServiceMethod: Desc: ServiceMethod   Required: True   Allow empty value : True
      :param CallDate: Desc: CallDate   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.APITraceRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/APITraces(" + Company + "," + TenantID + "," + ServiceName + "," + ServiceMethod + "," + CallDate + "," + CalledFrom + "," + UserID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APITraces_Company_TenantID_ServiceName_ServiceMethod_CallDate_CalledFrom_UserID(Company, TenantID, ServiceName, ServiceMethod, CallDate, CalledFrom, UserID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APITrace for the service
   Description: Calls UpdateExt to update APITrace. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APITrace
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TenantID: Desc: TenantID   Required: True   Allow empty value : True
      :param ServiceName: Desc: ServiceName   Required: True   Allow empty value : True
      :param ServiceMethod: Desc: ServiceMethod   Required: True   Allow empty value : True
      :param CallDate: Desc: CallDate   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.APITraceRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/APITraces(" + Company + "," + TenantID + "," + ServiceName + "," + ServiceMethod + "," + CallDate + "," + CalledFrom + "," + UserID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APITraces_Company_TenantID_ServiceName_ServiceMethod_CallDate_CalledFrom_UserID(Company, TenantID, ServiceName, ServiceMethod, CallDate, CalledFrom, UserID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APITrace item
   Description: Call UpdateExt to delete APITrace item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APITrace
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TenantID: Desc: TenantID   Required: True   Allow empty value : True
      :param ServiceName: Desc: ServiceName   Required: True   Allow empty value : True
      :param ServiceMethod: Desc: ServiceMethod   Required: True   Allow empty value : True
      :param CallDate: Desc: CallDate   Required: True   Allow empty value : True
      :param CalledFrom: Desc: CalledFrom   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/APITraces(" + Company + "," + TenantID + "," + ServiceName + "," + ServiceMethod + "," + CallDate + "," + CalledFrom + "," + UserID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.APITraceListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAPITrace, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
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
   params += "whereClauseAPITrace=" + whereClauseAPITrace
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tenantID, serviceName, serviceMethod, callDate, calledFrom, userID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "tenantID=" + tenantID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serviceName=" + serviceName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "serviceMethod=" + serviceMethod
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "callDate=" + callDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "calledFrom=" + calledFrom
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "userID=" + userID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAPITrace(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAPITrace
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPITrace
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAPITrace_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPITrace_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.APITraceSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_APITraceListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_APITraceListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_APITraceRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_APITraceRow] = obj["value"]
      pass

class Ice_Tablesets_APITraceListRow:
   def __init__(self, obj):
      self.TenantID:str = obj["TenantID"]
      """  TenantID  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ServiceName:str = obj["ServiceName"]
      """  ServiceName  """  
      self.ServiceMethod:str = obj["ServiceMethod"]
      """  ServiceMethod  """  
      self.CallDate:str = obj["CallDate"]
      """  CallDate  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.NumberOfCalls:int = obj["NumberOfCalls"]
      """  NumberOfCalls  """  
      self.TotalExecutionTime:int = obj["TotalExecutionTime"]
      """  TotalExecutionTime  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_APITraceRow:
   def __init__(self, obj):
      self.TenantID:str = obj["TenantID"]
      """  TenantID  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ServiceName:str = obj["ServiceName"]
      """  ServiceName  """  
      self.ServiceMethod:str = obj["ServiceMethod"]
      """  ServiceMethod  """  
      self.CallDate:str = obj["CallDate"]
      """  CallDate  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.NumberOfCalls:int = obj["NumberOfCalls"]
      """  NumberOfCalls  """  
      self.TotalExecutionTime:int = obj["TotalExecutionTime"]
      """  TotalExecutionTime  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   tenantID
   serviceName
   serviceMethod
   callDate
   calledFrom
   userID
   """  
   def __init__(self, obj):
      self.tenantID:str = obj["tenantID"]
      self.serviceName:str = obj["serviceName"]
      self.serviceMethod:str = obj["serviceMethod"]
      self.callDate:str = obj["callDate"]
      self.calledFrom:str = obj["calledFrom"]
      self.userID:str = obj["userID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   tenantID
   serviceName
   serviceMethod
   callDate
   calledFrom
   userID
   """  
   def __init__(self, obj):
      self.tenantID:str = obj["tenantID"]
      self.serviceName:str = obj["serviceName"]
      self.serviceMethod:str = obj["serviceMethod"]
      self.callDate:str = obj["callDate"]
      self.calledFrom:str = obj["calledFrom"]
      self.userID:str = obj["userID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_APITraceTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_APITraceTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_APITraceTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_APITraceListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAPITrace_input:
   """ Required : 
   ds
   tenantID
   serviceName
   serviceMethod
   callDate
   calledFrom
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_APITraceTableset] = obj["ds"]
      self.tenantID:str = obj["tenantID"]
      self.serviceName:str = obj["serviceName"]
      self.serviceMethod:str = obj["serviceMethod"]
      self.callDate:str = obj["callDate"]
      self.calledFrom:str = obj["calledFrom"]
      pass

class GetNewAPITrace_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_APITraceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAPITrace
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAPITrace:str = obj["whereClauseAPITrace"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_APITraceTableset] = obj["returnObj"]
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

class Ice_Tablesets_APITraceListRow:
   def __init__(self, obj):
      self.TenantID:str = obj["TenantID"]
      """  TenantID  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ServiceName:str = obj["ServiceName"]
      """  ServiceName  """  
      self.ServiceMethod:str = obj["ServiceMethod"]
      """  ServiceMethod  """  
      self.CallDate:str = obj["CallDate"]
      """  CallDate  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.NumberOfCalls:int = obj["NumberOfCalls"]
      """  NumberOfCalls  """  
      self.TotalExecutionTime:int = obj["TotalExecutionTime"]
      """  TotalExecutionTime  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_APITraceListTableset:
   def __init__(self, obj):
      self.APITraceList:list[Ice_Tablesets_APITraceListRow] = obj["APITraceList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_APITraceRow:
   def __init__(self, obj):
      self.TenantID:str = obj["TenantID"]
      """  TenantID  """  
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ServiceName:str = obj["ServiceName"]
      """  ServiceName  """  
      self.ServiceMethod:str = obj["ServiceMethod"]
      """  ServiceMethod  """  
      self.CallDate:str = obj["CallDate"]
      """  CallDate  """  
      self.CalledFrom:str = obj["CalledFrom"]
      """  CalledFrom  """  
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.NumberOfCalls:int = obj["NumberOfCalls"]
      """  NumberOfCalls  """  
      self.TotalExecutionTime:int = obj["TotalExecutionTime"]
      """  TotalExecutionTime  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_APITraceTableset:
   def __init__(self, obj):
      self.APITrace:list[Ice_Tablesets_APITraceRow] = obj["APITrace"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtAPITraceTableset:
   def __init__(self, obj):
      self.APITrace:list[Ice_Tablesets_APITraceRow] = obj["APITrace"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtAPITraceTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtAPITraceTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_APITraceTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_APITraceTableset] = obj["ds"]
      pass

      """  output parameters  """  

