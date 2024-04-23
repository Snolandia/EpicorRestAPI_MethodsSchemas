import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SerialMatchSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_SerialMatches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get SerialMatches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SerialMatches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialMatchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/SerialMatches",headers=creds) as resp:
           return await resp.json()

async def post_SerialMatches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SerialMatches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SerialMatchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.SerialMatchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/SerialMatches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_SerialMatches_Company_ChildPartNum_ChildSerialNo(Company, ChildPartNum, ChildSerialNo, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the SerialMatch item
   Description: Calls GetByID to retrieve the SerialMatch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialMatch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ChildPartNum: Desc: ChildPartNum   Required: True   Allow empty value : True
      :param ChildSerialNo: Desc: ChildSerialNo   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.SerialMatchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/SerialMatches(" + Company + "," + ChildPartNum + "," + ChildSerialNo + ")",headers=creds) as resp:
           return await resp.json()

async def patch_SerialMatches_Company_ChildPartNum_ChildSerialNo(Company, ChildPartNum, ChildSerialNo, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update SerialMatch for the service
   Description: Calls UpdateExt to update SerialMatch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SerialMatch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ChildPartNum: Desc: ChildPartNum   Required: True   Allow empty value : True
      :param ChildSerialNo: Desc: ChildSerialNo   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.SerialMatchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/SerialMatches(" + Company + "," + ChildPartNum + "," + ChildSerialNo + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_SerialMatches_Company_ChildPartNum_ChildSerialNo(Company, ChildPartNum, ChildSerialNo, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete SerialMatch item
   Description: Call UpdateExt to delete SerialMatch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SerialMatch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ChildPartNum: Desc: ChildPartNum   Required: True   Allow empty value : True
      :param ChildSerialNo: Desc: ChildSerialNo   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/SerialMatches(" + Company + "," + ChildPartNum + "," + ChildSerialNo + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialMatchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSerialMatch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSerialMatch=" + whereClauseSerialMatch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(childPartNum, childSerialNo, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "childPartNum=" + childPartNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "childSerialNo=" + childSerialNo

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsLLSerialNumberTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsLLSerialNumberTracker
   OperationID: GetRowsLLSerialNumberTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsLLSerialNumberTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsLLSerialNumberTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsWUSerialNumberTracker(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsWUSerialNumberTracker
   OperationID: GetRowsWUSerialNumberTracker
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsWUSerialNumberTracker_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWUSerialNumberTracker_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSerialMatch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSerialMatch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSerialMatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSerialMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialMatchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialMatchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SerialMatchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialMatchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_SerialMatchRow] = obj["value"]
      pass

class Erp_Tablesets_SerialMatchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part number for the assembly parent serial number  """  
      self.ParentSerialNo:str = obj["ParentSerialNo"]
      """  Assembly Parent serial number  """  
      self.ChildPartNum:str = obj["ChildPartNum"]
      """  Part number for the child serial number  """  
      self.ChildSerialNo:str = obj["ChildSerialNo"]
      """  Child  serial number  """  
      self.DateMatched:str = obj["DateMatched"]
      """  Date the child was matched to the parent  """  
      self.ChildIsAssembly:bool = obj["ChildIsAssembly"]
      """  Indicates whether the child part/serial is for an assembly. Indicates whether the match was made using SerialMatch Asmbl or SerialMatchMtl records in Serial Match process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SerialNoChildSNStatus:str = obj["SerialNoChildSNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.SerialNoParSNStatus:str = obj["SerialNoParSNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialMatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part number for the assembly parent serial number  """  
      self.ParentSerialNo:str = obj["ParentSerialNo"]
      """  Assembly Parent serial number  """  
      self.ChildPartNum:str = obj["ChildPartNum"]
      """  Part number for the child serial number  """  
      self.ChildSerialNo:str = obj["ChildSerialNo"]
      """  Child  serial number  """  
      self.DateMatched:str = obj["DateMatched"]
      """  Date the child was matched to the parent  """  
      self.ChildIsAssembly:bool = obj["ChildIsAssembly"]
      """  Indicates whether the child part/serial is for an assembly. Indicates whether the match was made using SerialMatch Asmbl or SerialMatchMtl records in Serial Match process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SerialNoChildSNStatus:str = obj["SerialNoChildSNStatus"]
      self.SerialNoParSNStatus:str = obj["SerialNoParSNStatus"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   childPartNum
   childSerialNo
   """  
   def __init__(self, obj):
      self.childPartNum:str = obj["childPartNum"]
      self.childSerialNo:str = obj["childSerialNo"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_SerialMatchLLSerTrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part number of the serial number for which all of the lower level components are being shown  """  
      self.ParentSerialNo:str = obj["ParentSerialNo"]
      """  The serial number for which all of the lower level components are being shown  """  
      self.ChildPartNum:str = obj["ChildPartNum"]
      """  Part number for the child serial number  """  
      self.ChildSerialNo:str = obj["ChildSerialNo"]
      """  Child  serial number  """  
      self.ChildPartDesc:str = obj["ChildPartDesc"]
      """  Part description of the child part  """  
      self.Level:int = obj["Level"]
      """  Indicates the level at which the child is related to the ParentSerialNo. If the child is a direct requirement it will be level 1, if it is the child of a subassembly that was a direct requirement it will be level 2, requirements of level 2 subassemblies will be level 3 and so on.  """  
      self.ChildIsAssembly:bool = obj["ChildIsAssembly"]
      """  Indicates whether the child part/serial is for an assembly. If so its children and its childrens children will also be added to the temp table under the Serial Number for which the lower level components are being shown.  """  
      self.LevelTxt:str = obj["LevelTxt"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialMatchLLSerTrkTableset:
   def __init__(self, obj):
      self.SerialMatchLLSerTrk:list[Erp_Tablesets_SerialMatchLLSerTrkRow] = obj["SerialMatchLLSerTrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SerialMatchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part number for the assembly parent serial number  """  
      self.ParentSerialNo:str = obj["ParentSerialNo"]
      """  Assembly Parent serial number  """  
      self.ChildPartNum:str = obj["ChildPartNum"]
      """  Part number for the child serial number  """  
      self.ChildSerialNo:str = obj["ChildSerialNo"]
      """  Child  serial number  """  
      self.DateMatched:str = obj["DateMatched"]
      """  Date the child was matched to the parent  """  
      self.ChildIsAssembly:bool = obj["ChildIsAssembly"]
      """  Indicates whether the child part/serial is for an assembly. Indicates whether the match was made using SerialMatch Asmbl or SerialMatchMtl records in Serial Match process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SerialNoChildSNStatus:str = obj["SerialNoChildSNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.SerialNoParSNStatus:str = obj["SerialNoParSNStatus"]
      """   INVENTORY, WIP, SHIPPED, INSPECTION, DMR, MISC-ISSUE,REJECTED,PACKED = assigned in shipment process but not yet shipped; CONSUMED = issued as raw material to a job parent assembly if full serial tracking or assigned as a child component if outbound tracking.

Add new status codes to Code/Desc and Description:
PACKED`Packed
CONSUMED`Consumed  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialMatchListTableset:
   def __init__(self, obj):
      self.SerialMatchList:list[Erp_Tablesets_SerialMatchListRow] = obj["SerialMatchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SerialMatchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part number for the assembly parent serial number  """  
      self.ParentSerialNo:str = obj["ParentSerialNo"]
      """  Assembly Parent serial number  """  
      self.ChildPartNum:str = obj["ChildPartNum"]
      """  Part number for the child serial number  """  
      self.ChildSerialNo:str = obj["ChildSerialNo"]
      """  Child  serial number  """  
      self.DateMatched:str = obj["DateMatched"]
      """  Date the child was matched to the parent  """  
      self.ChildIsAssembly:bool = obj["ChildIsAssembly"]
      """  Indicates whether the child part/serial is for an assembly. Indicates whether the match was made using SerialMatch Asmbl or SerialMatchMtl records in Serial Match process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SerialNoChildSNStatus:str = obj["SerialNoChildSNStatus"]
      self.SerialNoParSNStatus:str = obj["SerialNoParSNStatus"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialMatchTableset:
   def __init__(self, obj):
      self.SerialMatch:list[Erp_Tablesets_SerialMatchRow] = obj["SerialMatch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SerialMatchWUSerTrkRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.LLPartNum:str = obj["LLPartNum"]
      """  Part number of the lower level serial number for which all of the higher level serial parents are being shown  """  
      self.LLSerialNo:str = obj["LLSerialNo"]
      """  The lower level serial number for which all of the higher level serial parents are being shown  """  
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part number for the parent serial number  """  
      self.ParentSerialNo:str = obj["ParentSerialNo"]
      """  Parent serial number  """  
      self.ParentPartDesc:str = obj["ParentPartDesc"]
      """  Part description of the parent part  """  
      self.Level:int = obj["Level"]
      """  Indicates the level at which the child is related to the uppermost Parent Serial Number located. If the lower level serial number is a direct requirement it will be level 1, if it is the child of a subassembly that was a direct requirement it will be level 2, requirements of level 2 subassemblies will be level 3 and so on.  """  
      self.SeqNum:int = obj["SeqNum"]
      """  Used internally when building the where used data so that the Level numbers can be set at the end of gathering data to the desired values.  """  
      self.LevelTxt:str = obj["LevelTxt"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.PackLine:int = obj["PackLine"]
      self.PackNum:int = obj["PackNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialMatchWUSerTrkTableset:
   def __init__(self, obj):
      self.SerialMatchWUSerTrk:list[Erp_Tablesets_SerialMatchWUSerTrkRow] = obj["SerialMatchWUSerTrk"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtSerialMatchTableset:
   def __init__(self, obj):
      self.SerialMatch:list[Erp_Tablesets_SerialMatchRow] = obj["SerialMatch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   childPartNum
   childSerialNo
   """  
   def __init__(self, obj):
      self.childPartNum:str = obj["childPartNum"]
      self.childSerialNo:str = obj["childSerialNo"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialMatchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SerialMatchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SerialMatchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_SerialMatchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSerialMatch_input:
   """ Required : 
   ds
   childPartNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchTableset] = obj["ds"]
      self.childPartNum:str = obj["childPartNum"]
      pass

class GetNewSerialMatch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsLLSerialNumberTracker_input:
   """ Required : 
   serialNumber
   partNumber
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.serialNumber:str = obj["serialNumber"]
      self.partNumber:str = obj["partNumber"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsLLSerialNumberTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialMatchLLSerTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsWUSerialNumberTracker_input:
   """ Required : 
   serialNumber
   partNumber
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.serialNumber:str = obj["serialNumber"]
      self.partNumber:str = obj["partNumber"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsWUSerialNumberTracker_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialMatchWUSerTrkTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSerialMatch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSerialMatch:str = obj["whereClauseSerialMatch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialMatchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtSerialMatchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtSerialMatchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialMatchTableset] = obj["ds"]
      pass

      """  output parameters  """  

