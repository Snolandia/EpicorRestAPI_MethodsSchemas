import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.UserCompSearchSvc
# Description: Queries for UserComp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_UserCompSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get UserCompSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_UserCompSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/UserCompSearches",headers=creds) as resp:
           return await resp.json()

async def post_UserCompSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_UserCompSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.UserCompRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.UserCompRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/UserCompSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_UserCompSearches_DcdUserID_Company(DcdUserID, Company, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the UserCompSearch item
   Description: Calls GetByID to retrieve the UserCompSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_UserCompSearch
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.UserCompRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/UserCompSearches(" + DcdUserID + "," + Company + ")",headers=creds) as resp:
           return await resp.json()

async def patch_UserCompSearches_DcdUserID_Company(DcdUserID, Company, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update UserCompSearch for the service
   Description: Calls UpdateExt to update UserCompSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_UserCompSearch
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.UserCompRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/UserCompSearches(" + DcdUserID + "," + Company + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_UserCompSearches_DcdUserID_Company(DcdUserID, Company, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete UserCompSearch item
   Description: Call UpdateExt to delete UserCompSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_UserCompSearch
      :param DcdUserID: Desc: DcdUserID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/UserCompSearches(" + DcdUserID + "," + Company + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.UserCompListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseUserComp, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseUserComp=" + whereClauseUserComp
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(dcdUserID, epicorHeaders = None):
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
   params += "dcdUserID=" + dcdUserID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTransactionRetrievalDays(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTransactionRetrievalDays
   Description: Used when in VendorTracker the setting [UserComp].[TransactionRetrievalDays] is changed to a new value.
   OperationID: ChangeTransactionRetrievalDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTransactionRetrievalDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTransactionRetrievalDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTransactionRetrievalDays(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTransactionRetrievalDays
   Description: In VendorTracker the TransactionRetrievalDays is needed from table [UserComp] if there is a value, else from table [XaSyst]
   OperationID: GetTransactionRetrievalDays
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransactionRetrievalDays_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransactionRetrievalDays_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUserComp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUserComp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewUserComp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUserComp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUserComp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UserCompSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_UserCompListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_UserCompRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_UserCompRow] = obj["value"]
      pass

class Erp_Tablesets_UserCompListRow:
   def __init__(self, obj):
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurPlant:str = obj["CurPlant"]
      """  Site Identifier.  """  
      self.PlantList:str = obj["PlantList"]
      """  List of Sites the user has access to.  """  
      self.PrimBuyerID:str = obj["PrimBuyerID"]
      """  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  """  
      self.Name:str = obj["Name"]
      """  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  """  
      self.OverloadInfHeight:int = obj["OverloadInfHeight"]
      """  Initial height of the Overload Informer in pixels.  """  
      self.OverloadInfSort:str = obj["OverloadInfSort"]
      """  Initial overload informer sort option.  """  
      self.PrimSalesRepID:str = obj["PrimSalesRepID"]
      """  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  """  
      self.StartTaskSaleRepWB:bool = obj["StartTaskSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  """  
      self.StartTaskOppEnt:bool = obj["StartTaskOppEnt"]
      """  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  """  
      self.StartOppSaleRepWB:bool = obj["StartOppSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  """  
      self.StartOrdSaleRepWB:bool = obj["StartOrdSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  """  
      self.StartRMASaleRepWB:bool = obj["StartRMASaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  """  
      self.StartSCallSaleRepWB:bool = obj["StartSCallSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  """  
      self.WorkstationID:str = obj["WorkstationID"]
      """  Unique identifier of the Workstations  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.DCDUserIDName:str = obj["DCDUserIDName"]
      """  User Name  """  
      self.EmpIDName:str = obj["EmpIDName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.WorkstationIDDescription:str = obj["WorkstationIDDescription"]
      """  Description of the station  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UserCompRow:
   def __init__(self, obj):
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurPlant:str = obj["CurPlant"]
      """  Site Identifier.  """  
      self.PlantList:str = obj["PlantList"]
      """  List of Sites the user has access to.  """  
      self.PrimBuyerID:str = obj["PrimBuyerID"]
      """  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  """  
      self.Name:str = obj["Name"]
      """  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  """  
      self.OverloadInfHeight:int = obj["OverloadInfHeight"]
      """  Initial height of the Overload Informer in pixels.  """  
      self.OverloadInfSort:str = obj["OverloadInfSort"]
      """  Initial overload informer sort option.  """  
      self.PrimSalesRepID:str = obj["PrimSalesRepID"]
      """  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  """  
      self.StartTaskSaleRepWB:bool = obj["StartTaskSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  """  
      self.StartTaskOppEnt:bool = obj["StartTaskOppEnt"]
      """  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  """  
      self.StartOppSaleRepWB:bool = obj["StartOppSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  """  
      self.StartOrdSaleRepWB:bool = obj["StartOrdSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  """  
      self.StartRMASaleRepWB:bool = obj["StartRMASaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  """  
      self.StartSCallSaleRepWB:bool = obj["StartSCallSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  """  
      self.WorkstationID:str = obj["WorkstationID"]
      """  Unique identifier of the Workstations  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.CanUpdateExpense:bool = obj["CanUpdateExpense"]
      """  Indicates if the user can update expense entries (EmpExpense) for any employee.  """  
      self.CanUpdateTime:bool = obj["CanUpdateTime"]
      """  Indicates if the user can update time entries (LaborDtl) for any employee.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FWBLimitedRefresh:bool = obj["FWBLimitedRefresh"]
      """  FWBLimitedRefresh  """  
      self.FWBUseDemandWhseOnly:bool = obj["FWBUseDemandWhseOnly"]
      """  FWBUseDemandWhseOnly  """  
      self.SharedSupValidation:bool = obj["SharedSupValidation"]
      """  Is used by UIApps PurchaseContractScheduleEntry – it is used to set/toggle the Purchase Schedule Approval action menu item Part Schedule Shared Supplier Validation (SharedSupplierValidationToggleTool).  """  
      self.TransactionRetrievalDays:int = obj["TransactionRetrievalDays"]
      """  TransactionRetrievalDays  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanyName:str = obj["CompanyName"]
      self.DCDUserIDName:str = obj["DCDUserIDName"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.WorkstationIDDescription:str = obj["WorkstationIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeTransactionRetrievalDays_input:
   """ Required : 
   ipNumOfDays
   ds
   """  
   def __init__(self, obj):
      self.ipNumOfDays:int = obj["ipNumOfDays"]
      """  The amount of TransactionRetrievalDays for the current user.  """  
      self.ds:list[Erp_Tablesets_UserCompSearchTableset] = obj["ds"]
      pass

class ChangeTransactionRetrievalDays_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UserCompSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   dcdUserID
   """  
   def __init__(self, obj):
      self.dcdUserID:str = obj["dcdUserID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_UpdExtUserCompSearchTableset:
   def __init__(self, obj):
      self.UserComp:list[Erp_Tablesets_UserCompRow] = obj["UserComp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UserCompListRow:
   def __init__(self, obj):
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurPlant:str = obj["CurPlant"]
      """  Site Identifier.  """  
      self.PlantList:str = obj["PlantList"]
      """  List of Sites the user has access to.  """  
      self.PrimBuyerID:str = obj["PrimBuyerID"]
      """  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  """  
      self.Name:str = obj["Name"]
      """  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  """  
      self.OverloadInfHeight:int = obj["OverloadInfHeight"]
      """  Initial height of the Overload Informer in pixels.  """  
      self.OverloadInfSort:str = obj["OverloadInfSort"]
      """  Initial overload informer sort option.  """  
      self.PrimSalesRepID:str = obj["PrimSalesRepID"]
      """  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  """  
      self.StartTaskSaleRepWB:bool = obj["StartTaskSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  """  
      self.StartTaskOppEnt:bool = obj["StartTaskOppEnt"]
      """  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  """  
      self.StartOppSaleRepWB:bool = obj["StartOppSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  """  
      self.StartOrdSaleRepWB:bool = obj["StartOrdSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  """  
      self.StartRMASaleRepWB:bool = obj["StartRMASaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  """  
      self.StartSCallSaleRepWB:bool = obj["StartSCallSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  """  
      self.WorkstationID:str = obj["WorkstationID"]
      """  Unique identifier of the Workstations  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CompanyName:str = obj["CompanyName"]
      """  Company Name  """  
      self.DCDUserIDName:str = obj["DCDUserIDName"]
      """  User Name  """  
      self.EmpIDName:str = obj["EmpIDName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.WorkstationIDDescription:str = obj["WorkstationIDDescription"]
      """  Description of the station  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UserCompListTableset:
   def __init__(self, obj):
      self.UserCompList:list[Erp_Tablesets_UserCompListRow] = obj["UserCompList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UserCompRow:
   def __init__(self, obj):
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CurPlant:str = obj["CurPlant"]
      """  Site Identifier.  """  
      self.PlantList:str = obj["PlantList"]
      """  List of Sites the user has access to.  """  
      self.PrimBuyerID:str = obj["PrimBuyerID"]
      """  The primary BuyerID of the related PurAgent  for this User/Company. (See PurAgent.BuyerID).  This buyer will be the default buyer for Purchase Orders created by this user.  It is optional.  However, a buyer is mandatory on Purchase orders. This is set in Buyer maintenance (pmm10-dg).  """  
      self.Name:str = obj["Name"]
      """  Users Name. Not directly user maintainable. Mirror image of UserFile.Name.  Used to provide single index by Company/Name on this table.  """  
      self.OverloadInfHeight:int = obj["OverloadInfHeight"]
      """  Initial height of the Overload Informer in pixels.  """  
      self.OverloadInfSort:str = obj["OverloadInfSort"]
      """  Initial overload informer sort option.  """  
      self.PrimSalesRepID:str = obj["PrimSalesRepID"]
      """  The primary SalesRepID of the related SalesRep  for this User/Company. (See SalesRep.SalesRepID).  This Sales Rep will be the default Sales rep for Quotes created by this user.  It is optional.  """  
      self.StartTaskSaleRepWB:bool = obj["StartTaskSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the task list program will start automatically when the salesperson workbench is started.  """  
      self.StartTaskOppEnt:bool = obj["StartTaskOppEnt"]
      """  This flag is set from Opportunity/Quote entry and is used to indicate that the task list program will start automatically when Opportunity/Quote entry is started.  """  
      self.StartOppSaleRepWB:bool = obj["StartOppSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Opportunity entry program will start automatically when the salesperson workbench is started.  """  
      self.StartOrdSaleRepWB:bool = obj["StartOrdSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Order entry program will start automatically when the salesperson workbench is started.  """  
      self.StartRMASaleRepWB:bool = obj["StartRMASaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the RMA entry program will start automatically when the salesperson workbench is started.  """  
      self.StartSCallSaleRepWB:bool = obj["StartSCallSaleRepWB"]
      """  This flag is set from the sales person workbench and is used to indicate that the Service Call entry program will start automatically when the salesperson workbench is started.  """  
      self.WorkstationID:str = obj["WorkstationID"]
      """  Unique identifier of the Workstations  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.CanUpdateExpense:bool = obj["CanUpdateExpense"]
      """  Indicates if the user can update expense entries (EmpExpense) for any employee.  """  
      self.CanUpdateTime:bool = obj["CanUpdateTime"]
      """  Indicates if the user can update time entries (LaborDtl) for any employee.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.FWBLimitedRefresh:bool = obj["FWBLimitedRefresh"]
      """  FWBLimitedRefresh  """  
      self.FWBUseDemandWhseOnly:bool = obj["FWBUseDemandWhseOnly"]
      """  FWBUseDemandWhseOnly  """  
      self.SharedSupValidation:bool = obj["SharedSupValidation"]
      """  Is used by UIApps PurchaseContractScheduleEntry – it is used to set/toggle the Purchase Schedule Approval action menu item Part Schedule Shared Supplier Validation (SharedSupplierValidationToggleTool).  """  
      self.TransactionRetrievalDays:int = obj["TransactionRetrievalDays"]
      """  TransactionRetrievalDays  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CompanyName:str = obj["CompanyName"]
      self.DCDUserIDName:str = obj["DCDUserIDName"]
      self.EmpIDName:str = obj["EmpIDName"]
      self.WorkstationIDDescription:str = obj["WorkstationIDDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UserCompSearchTableset:
   def __init__(self, obj):
      self.UserComp:list[Erp_Tablesets_UserCompRow] = obj["UserComp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   dcdUserID
   """  
   def __init__(self, obj):
      self.dcdUserID:str = obj["dcdUserID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_UserCompSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_UserCompSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_UserCompSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_UserCompListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewUserComp_input:
   """ Required : 
   ds
   dcdUserID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UserCompSearchTableset] = obj["ds"]
      self.dcdUserID:str = obj["dcdUserID"]
      pass

class GetNewUserComp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UserCompSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseUserComp
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseUserComp:str = obj["whereClauseUserComp"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_UserCompSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTransactionRetrievalDays_input:
   """ Required : 
   company
   dcdUserID
   days
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      """  The company used for the current user.  """  
      self.dcdUserID:str = obj["dcdUserID"]
      """  The ID oF the current user.  """  
      self.days:int = obj["days"]
      """  The days from UserComp if there is any or from XaSyst.  """  
      pass

class GetTransactionRetrievalDays_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.days:int = obj["parameters"]
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
      self.ds:list[Erp_Tablesets_UpdExtUserCompSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtUserCompSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UserCompSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UserCompSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

