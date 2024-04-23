import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.QuickEntrySearchSvc
# Description: The QuickEntrySearch bo. Used for the QuickEntrySearch Combo.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_QuickEntrySearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get QuickEntrySearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuickEntrySearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuickEntryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/QuickEntrySearches",headers=creds) as resp:
           return await resp.json()

async def post_QuickEntrySearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_QuickEntrySearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.QuickEntryRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.QuickEntryRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/QuickEntrySearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_QuickEntrySearches_Company_EmpID_QuickEntryType_QuickEntryCode(Company, EmpID, QuickEntryType, QuickEntryCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the QuickEntrySearch item
   Description: Calls GetByID to retrieve the QuickEntrySearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuickEntrySearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param QuickEntryType: Desc: QuickEntryType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.QuickEntryRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/QuickEntrySearches(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_QuickEntrySearches_Company_EmpID_QuickEntryType_QuickEntryCode(Company, EmpID, QuickEntryType, QuickEntryCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update QuickEntrySearch for the service
   Description: Calls UpdateExt to update QuickEntrySearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_QuickEntrySearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param QuickEntryType: Desc: QuickEntryType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.QuickEntryRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/QuickEntrySearches(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_QuickEntrySearches_Company_EmpID_QuickEntryType_QuickEntryCode(Company, EmpID, QuickEntryType, QuickEntryCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete QuickEntrySearch item
   Description: Call UpdateExt to delete QuickEntrySearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_QuickEntrySearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param EmpID: Desc: EmpID   Required: True   Allow empty value : True
      :param QuickEntryType: Desc: QuickEntryType   Required: True   Allow empty value : True
      :param QuickEntryCode: Desc: QuickEntryCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/QuickEntrySearches(" + Company + "," + EmpID + "," + QuickEntryType + "," + QuickEntryCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.QuickEntryListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseQuickEntry, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseQuickEntry=" + whereClauseQuickEntry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(empID, quickEntryType, quickEntryCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "empID=" + empID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "quickEntryType=" + quickEntryType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "quickEntryCode=" + quickEntryCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewQuickEntry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewQuickEntry
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewQuickEntry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewQuickEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewQuickEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.QuickEntrySearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuickEntryListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_QuickEntryRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_QuickEntryRow] = obj["value"]
      pass

class Erp_Tablesets_QuickEntryListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.QuickEntryType:str = obj["QuickEntryType"]
      """  Defines whether the Quick Entry Code relates to Time or Expenses.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Unique identifier of this Quick Entry Code.  """  
      self.LaborType:str = obj["LaborType"]
      """  Defines whether the Quick Entry Code is related to Project, Production or Indirect labor.  Relates only to Time Quick Entry Codes.  Valid values are P (Production) and I (Indirect).  """  
      self.ProjectID:str = obj["ProjectID"]
      """  This value is used to set the value for the Project.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  This value is used to set the value for WBS Phase.  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  This value is used to set the Time Type Code.  Relates only to Time Quick Entry Codes.  """  
      self.JobNum:str = obj["JobNum"]
      """  This value is used to set the value for Job.  Relates only to Time Quick Entry Codes.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  This value is used to set the value for Assembly.  Relates only to Time Quick Entry Codes.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  This value is used to set the value for Operation.  Relates only to Time Quick Entry Codes.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  This value is used to set the value for Project Role Code.  Relates only to Time Quick Entry Codes.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  This value is used to set the value for Indirect Code.  Relates only to Time Quick Entry Codes where the Labor Type is Indirect.  """  
      self.IndirectExpense:bool = obj["IndirectExpense"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Indirect Expense.  """  
      self.PMUID:int = obj["PMUID"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Payment Method.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Miscellaneous Charge ID.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Reimbursable.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Liability.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Expense Currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Included.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The Expense Code for the labor transaction.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The Resource Group in which the labor is performed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The Resource that was used to do the work.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours.  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.ExpenseCategory:str = obj["ExpenseCategory"]
      """  The expense category.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuickEntryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.QuickEntryType:str = obj["QuickEntryType"]
      """  Defines whether the Quick Entry Code relates to Time or Expenses.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Unique identifier of this Quick Entry Code.  """  
      self.LaborType:str = obj["LaborType"]
      """  Defines whether the Quick Entry Code is related to Project, Production or Indirect labor.  Relates only to Time Quick Entry Codes.  Valid values are P (Production) and I (Indirect).  """  
      self.ProjectID:str = obj["ProjectID"]
      """  This value is used to set the value for the Project.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  This value is used to set the value for WBS Phase.  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  This value is used to set the Time Type Code.  Relates only to Time Quick Entry Codes.  """  
      self.JobNum:str = obj["JobNum"]
      """  This value is used to set the value for Job.  Relates only to Time Quick Entry Codes.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  This value is used to set the value for Assembly.  Relates only to Time Quick Entry Codes.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  This value is used to set the value for Operation.  Relates only to Time Quick Entry Codes.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  This value is used to set the value for Project Role Code.  Relates only to Time Quick Entry Codes.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  This value is used to set the value for Indirect Code.  Relates only to Time Quick Entry Codes where the Labor Type is Indirect.  """  
      self.IndirectExpense:bool = obj["IndirectExpense"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Indirect Expense.  """  
      self.PMUID:int = obj["PMUID"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Payment Method.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Miscellaneous Charge ID.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Reimbursable.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Liability.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Expense Currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Included.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The Expense Code for the labor transaction.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The Resource Group in which the labor is performed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The Resource that was used to do the work.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours.  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.ExpenseCategory:str = obj["ExpenseCategory"]
      """  The expense category.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   empID
   quickEntryType
   quickEntryCode
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      self.quickEntryType:str = obj["quickEntryType"]
      self.quickEntryCode:str = obj["quickEntryCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_QuickEntryListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.QuickEntryType:str = obj["QuickEntryType"]
      """  Defines whether the Quick Entry Code relates to Time or Expenses.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Unique identifier of this Quick Entry Code.  """  
      self.LaborType:str = obj["LaborType"]
      """  Defines whether the Quick Entry Code is related to Project, Production or Indirect labor.  Relates only to Time Quick Entry Codes.  Valid values are P (Production) and I (Indirect).  """  
      self.ProjectID:str = obj["ProjectID"]
      """  This value is used to set the value for the Project.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  This value is used to set the value for WBS Phase.  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  This value is used to set the Time Type Code.  Relates only to Time Quick Entry Codes.  """  
      self.JobNum:str = obj["JobNum"]
      """  This value is used to set the value for Job.  Relates only to Time Quick Entry Codes.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  This value is used to set the value for Assembly.  Relates only to Time Quick Entry Codes.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  This value is used to set the value for Operation.  Relates only to Time Quick Entry Codes.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  This value is used to set the value for Project Role Code.  Relates only to Time Quick Entry Codes.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  This value is used to set the value for Indirect Code.  Relates only to Time Quick Entry Codes where the Labor Type is Indirect.  """  
      self.IndirectExpense:bool = obj["IndirectExpense"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Indirect Expense.  """  
      self.PMUID:int = obj["PMUID"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Payment Method.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Miscellaneous Charge ID.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Reimbursable.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Liability.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Expense Currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Included.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The Expense Code for the labor transaction.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The Resource Group in which the labor is performed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The Resource that was used to do the work.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours.  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.ExpenseCategory:str = obj["ExpenseCategory"]
      """  The expense category.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuickEntryListTableset:
   def __init__(self, obj):
      self.QuickEntryList:list[Erp_Tablesets_QuickEntryListRow] = obj["QuickEntryList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_QuickEntryRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmpID:str = obj["EmpID"]
      """  Descriptive code assigned by user which uniquely identifies a shopfloor employee master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.QuickEntryType:str = obj["QuickEntryType"]
      """  Defines whether the Quick Entry Code relates to Time or Expenses.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Unique identifier of this Quick Entry Code.  """  
      self.LaborType:str = obj["LaborType"]
      """  Defines whether the Quick Entry Code is related to Project, Production or Indirect labor.  Relates only to Time Quick Entry Codes.  Valid values are P (Production) and I (Indirect).  """  
      self.ProjectID:str = obj["ProjectID"]
      """  This value is used to set the value for the Project.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  This value is used to set the value for WBS Phase.  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  This value is used to set the Time Type Code.  Relates only to Time Quick Entry Codes.  """  
      self.JobNum:str = obj["JobNum"]
      """  This value is used to set the value for Job.  Relates only to Time Quick Entry Codes.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  This value is used to set the value for Assembly.  Relates only to Time Quick Entry Codes.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  This value is used to set the value for Operation.  Relates only to Time Quick Entry Codes.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  This value is used to set the value for Project Role Code.  Relates only to Time Quick Entry Codes.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  This value is used to set the value for Indirect Code.  Relates only to Time Quick Entry Codes where the Labor Type is Indirect.  """  
      self.IndirectExpense:bool = obj["IndirectExpense"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Indirect Expense.  """  
      self.PMUID:int = obj["PMUID"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Payment Method.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Miscellaneous Charge ID.  """  
      self.Reimbursable:bool = obj["Reimbursable"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Reimbursable.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Liability.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Expense Currency.  """  
      self.TaxIncluded:bool = obj["TaxIncluded"]
      """  If Quick Entry Type is Expense, this value is used to set the quick value for Tax Included.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The Expense Code for the labor transaction.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The Resource Group in which the labor is performed.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The Resource that was used to do the work.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours.  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.ExpenseCategory:str = obj["ExpenseCategory"]
      """  The expense category.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_QuickEntrySearchTableset:
   def __init__(self, obj):
      self.QuickEntry:list[Erp_Tablesets_QuickEntryRow] = obj["QuickEntry"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtQuickEntrySearchTableset:
   def __init__(self, obj):
      self.QuickEntry:list[Erp_Tablesets_QuickEntryRow] = obj["QuickEntry"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   empID
   quickEntryType
   quickEntryCode
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      self.quickEntryType:str = obj["quickEntryType"]
      self.quickEntryCode:str = obj["quickEntryCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuickEntrySearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QuickEntrySearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QuickEntrySearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_QuickEntryListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewQuickEntry_input:
   """ Required : 
   ds
   empID
   quickEntryType
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntrySearchTableset] = obj["ds"]
      self.empID:str = obj["empID"]
      self.quickEntryType:str = obj["quickEntryType"]
      pass

class GetNewQuickEntry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntrySearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseQuickEntry
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseQuickEntry:str = obj["whereClauseQuickEntry"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_QuickEntrySearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtQuickEntrySearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtQuickEntrySearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntrySearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_QuickEntrySearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

