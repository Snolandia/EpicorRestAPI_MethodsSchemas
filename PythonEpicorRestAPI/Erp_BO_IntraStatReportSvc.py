import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IntraStatReportSvc
# Description: IntraStatReport Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_IntraStatReports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get IntraStatReports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_IntraStatReports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IntraStatReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/IntraStatReports",headers=creds) as resp:
           return await resp.json()

async def post_IntraStatReports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_IntraStatReports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.IntraStatReportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.IntraStatReportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/IntraStatReports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_IntraStatReports_Company_ReportID(Company, ReportID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the IntraStatReport item
   Description: Calls GetByID to retrieve the IntraStatReport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_IntraStatReport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.IntraStatReportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/IntraStatReports(" + Company + "," + ReportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_IntraStatReports_Company_ReportID(Company, ReportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update IntraStatReport for the service
   Description: Calls UpdateExt to update IntraStatReport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_IntraStatReport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.IntraStatReportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/IntraStatReports(" + Company + "," + ReportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_IntraStatReports_Company_ReportID(Company, ReportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete IntraStatReport item
   Description: Call UpdateExt to delete IntraStatReport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_IntraStatReport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ReportID: Desc: ReportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/IntraStatReports(" + Company + "," + ReportID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IntraStatReportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseIntraStatReport, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseIntraStatReport=" + whereClauseIntraStatReport
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(reportID, epicorHeaders = None):
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
   params += "reportID=" + reportID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnPeriodChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnPeriodChanged
   OperationID: OnPeriodChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnPeriodChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnPeriodChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PostReportName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PostReportName
   OperationID: PostReportName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PostReportName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostReportName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateReportsDateFlow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateReportsDateFlow
   OperationID: ValidateReportsDateFlow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateReportsDateFlow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateReportsDateFlow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIntraStatReport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIntraStatReport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewIntraStatReport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIntraStatReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIntraStatReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IntraStatReportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IntraStatReportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_IntraStatReportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IntraStatReportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_IntraStatReportRow] = obj["value"]
      pass

class Erp_Tablesets_IntraStatReportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DateSelection:str = obj["DateSelection"]
      """  DateSelection  """  
      self.Year:int = obj["Year"]
      """  Year  """  
      self.Period:int = obj["Period"]
      """  Period  """  
      self.AccountSelection:str = obj["AccountSelection"]
      """  AccountSelection  """  
      self.Flow:str = obj["Flow"]
      """  Flow  """  
      self.BackDatedItems:str = obj["BackDatedItems"]
      """  BackDatedItems  """  
      self.RoundWeight:bool = obj["RoundWeight"]
      """  RoundWeight  """  
      self.RoundAmount:bool = obj["RoundAmount"]
      """  RoundAmount  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.DateFrom:str = obj["DateFrom"]
      """  DateFrom  """  
      self.DateTo:str = obj["DateTo"]
      """  DateTo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntraStatReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DateSelection:str = obj["DateSelection"]
      """  DateSelection  """  
      self.Year:int = obj["Year"]
      """  Year  """  
      self.Period:int = obj["Period"]
      """  Period  """  
      self.AccountSelection:str = obj["AccountSelection"]
      """  AccountSelection  """  
      self.Flow:str = obj["Flow"]
      """  Flow  """  
      self.BackDatedItems:str = obj["BackDatedItems"]
      """  BackDatedItems  """  
      self.RoundWeight:bool = obj["RoundWeight"]
      """  RoundWeight  """  
      self.RoundAmount:bool = obj["RoundAmount"]
      """  RoundAmount  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.DateFrom:str = obj["DateFrom"]
      """  DateFrom  """  
      self.DateTo:str = obj["DateTo"]
      """  DateTo  """  
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
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_IntraStatReportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DateSelection:str = obj["DateSelection"]
      """  DateSelection  """  
      self.Year:int = obj["Year"]
      """  Year  """  
      self.Period:int = obj["Period"]
      """  Period  """  
      self.AccountSelection:str = obj["AccountSelection"]
      """  AccountSelection  """  
      self.Flow:str = obj["Flow"]
      """  Flow  """  
      self.BackDatedItems:str = obj["BackDatedItems"]
      """  BackDatedItems  """  
      self.RoundWeight:bool = obj["RoundWeight"]
      """  RoundWeight  """  
      self.RoundAmount:bool = obj["RoundAmount"]
      """  RoundAmount  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.DateFrom:str = obj["DateFrom"]
      """  DateFrom  """  
      self.DateTo:str = obj["DateTo"]
      """  DateTo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntraStatReportListTableset:
   def __init__(self, obj):
      self.IntraStatReportList:list[Erp_Tablesets_IntraStatReportListRow] = obj["IntraStatReportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IntraStatReportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.DateSelection:str = obj["DateSelection"]
      """  DateSelection  """  
      self.Year:int = obj["Year"]
      """  Year  """  
      self.Period:int = obj["Period"]
      """  Period  """  
      self.AccountSelection:str = obj["AccountSelection"]
      """  AccountSelection  """  
      self.Flow:str = obj["Flow"]
      """  Flow  """  
      self.BackDatedItems:str = obj["BackDatedItems"]
      """  BackDatedItems  """  
      self.RoundWeight:bool = obj["RoundWeight"]
      """  RoundWeight  """  
      self.RoundAmount:bool = obj["RoundAmount"]
      """  RoundAmount  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.DateFrom:str = obj["DateFrom"]
      """  DateFrom  """  
      self.DateTo:str = obj["DateTo"]
      """  DateTo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntraStatReportTableset:
   def __init__(self, obj):
      self.IntraStatReport:list[Erp_Tablesets_IntraStatReportRow] = obj["IntraStatReport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtIntraStatReportTableset:
   def __init__(self, obj):
      self.IntraStatReport:list[Erp_Tablesets_IntraStatReportRow] = obj["IntraStatReport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   reportID
   """  
   def __init__(self, obj):
      self.reportID:str = obj["reportID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IntraStatReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_IntraStatReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_IntraStatReportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_IntraStatReportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewIntraStatReport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IntraStatReportTableset] = obj["ds"]
      pass

class GetNewIntraStatReport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IntraStatReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseIntraStatReport
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseIntraStatReport:str = obj["whereClauseIntraStatReport"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IntraStatReportTableset] = obj["returnObj"]
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

class OnPeriodChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IntraStatReportTableset] = obj["ds"]
      pass

class OnPeriodChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IntraStatReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PostReportName_input:
   """ Required : 
   ReportName
   Posted
   """  
   def __init__(self, obj):
      self.ReportName:str = obj["ReportName"]
      """  IntraStatReport.ReportID  """  
      self.Posted:bool = obj["Posted"]
      pass

class PostReportName_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtIntraStatReportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtIntraStatReportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IntraStatReportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IntraStatReportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateReportsDateFlow_input:
   """ Required : 
   intraStatRecordID
   intraStatDateFrom
   intraStatDateTo
   intraStatFlow
   """  
   def __init__(self, obj):
      self.intraStatRecordID:str = obj["intraStatRecordID"]
      self.intraStatDateFrom:str = obj["intraStatDateFrom"]
      self.intraStatDateTo:str = obj["intraStatDateTo"]
      self.intraStatFlow:str = obj["intraStatFlow"]
      pass

class ValidateReportsDateFlow_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

