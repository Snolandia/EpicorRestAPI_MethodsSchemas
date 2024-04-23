import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.MemoSvc
# Description: Memo records are used to hold "Internal Notes" about a related master record.
Memos can be related to many different types of masters. For example you can
create memos related to a Customer, Vendor, Employee, Order, Quote, etc...
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Memos(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Memos items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Memos
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MemoRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/Memos",headers=creds) as resp:
           return await resp.json()

async def post_Memos(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Memos
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.MemoRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.MemoRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/Memos", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Memos_RelatedToSchemaName_RelatedToFile_RelatedToSysRowID_MemoNum(RelatedToSchemaName, RelatedToFile, RelatedToSysRowID, MemoNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Memo item
   Description: Calls GetByID to retrieve the Memo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Memo
      :param RelatedToSchemaName: Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param RelatedToSysRowID: Desc: RelatedToSysRowID   Required: True   Allow empty value : True
      :param MemoNum: Desc: MemoNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.MemoRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/Memos(" + RelatedToSchemaName + "," + RelatedToFile + "," + RelatedToSysRowID + "," + MemoNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Memos_RelatedToSchemaName_RelatedToFile_RelatedToSysRowID_MemoNum(RelatedToSchemaName, RelatedToFile, RelatedToSysRowID, MemoNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Memo for the service
   Description: Calls UpdateExt to update Memo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Memo
      :param RelatedToSchemaName: Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param RelatedToSysRowID: Desc: RelatedToSysRowID   Required: True   Allow empty value : True
      :param MemoNum: Desc: MemoNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.MemoRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/Memos(" + RelatedToSchemaName + "," + RelatedToFile + "," + RelatedToSysRowID + "," + MemoNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Memos_RelatedToSchemaName_RelatedToFile_RelatedToSysRowID_MemoNum(RelatedToSchemaName, RelatedToFile, RelatedToSysRowID, MemoNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Memo item
   Description: Call UpdateExt to delete Memo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Memo
      :param RelatedToSchemaName: Desc: RelatedToSchemaName   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param RelatedToSysRowID: Desc: RelatedToSysRowID   Required: True   Allow empty value : True
      :param MemoNum: Desc: MemoNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/Memos(" + RelatedToSchemaName + "," + RelatedToFile + "," + RelatedToSysRowID + "," + MemoNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.MemoListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMemo, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseMemo=" + whereClauseMemo
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(relatedToSchemaName, relatedToFile, relatedToSysRowID, memoNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
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
   params += "relatedToSchemaName=" + relatedToSchemaName
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "relatedToFile=" + relatedToFile
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "relatedToSysRowID=" + relatedToSysRowID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "memoNum=" + memoNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMemo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMemo
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMemo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMemo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMemo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.MemoSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MemoListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_MemoListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_MemoRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_MemoRow] = obj["value"]
      pass

class Ice_Tablesets_MemoListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the memo is related to.  This field is used to properly  isolate memos to the masters they are related to.
For example; Customer, Vendor, PREmpMas identifies memos that are related to Customers, Vendor and Payroll Employee master records.  """  
      self.MemoDate:str = obj["MemoDate"]
      """  Date that the Memo was created.  """  
      self.MemoUserID:str = obj["MemoUserID"]
      """  User Id that created the memo. DCDUserID.  """  
      self.MemoDesc:str = obj["MemoDesc"]
      """  An abbreviated description of what the memo is about.  This will be shown in browses of memos.  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Category ID that this memo is assigned to .  This field contains the foreign key of the related MemoCat master.  It can be blank or it must be valid in the MemoCat.  """  
      self.CategoryDesc:str = obj["CategoryDesc"]
      """  Category ID that this memo is assigned to.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MemoRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the memo is related to.  This field is used to properly  isolate memos to the masters they are related to.
For example; Customer, Vendor, PREmpMas identifies memos that are related to Customers, Vendor and Payroll Employee master records.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  memo this field would contain the related Part Number,  for a "Customer" memo it contains the Customers CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "OrderDtl"  memo this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "Part" memo's do not use this field while PartRev memos would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "OrderRel"  memo this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependent on the type of record the memo is related to.  """  
      self.MemoDate:str = obj["MemoDate"]
      """  Date that the Memo was created.  """  
      self.MemoNum:int = obj["MemoNum"]
      """  An integer assigned by the system to uniquely identify the Memo. This integer is created by using the database sequence "MemoSeq".  """  
      self.MemoUserID:str = obj["MemoUserID"]
      """  User Id that created the memo. DCDUserID.  """  
      self.Notify:bool = obj["Notify"]
      """  Indicates if this memo is or is not on the memo "Notify" list. The user can set this flag to indicate that there is something about the  memo that they wish to be notified of at a later date (such as customer follow-up, callback...).  """  
      self.NotifyUserID:str = obj["NotifyUserID"]
      """  User Id that is to be Notified about this memo. Defaults to Current DCDUserID.  """  
      self.NotifyDate:str = obj["NotifyDate"]
      """  Date that the user is to be notified about this memo.  """  
      self.MemoDesc:str = obj["MemoDesc"]
      """  An abbreviated description of what the memo is about.  This will be shown in browses of memos.  """  
      self.MemoText:str = obj["MemoText"]
      """  MemoText contains the textual content of the memo. Intended to be used as internal online storage of text information related to a specific master. They do get pulled into other database records. To be viewed-as a progress  EDITOR widget.  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Category ID that this memo is assigned to .  This field contains the foreign key of the related MemoCat master.  It can be blank or it must be valid in the MemoCat.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.ChangeTrackChargeIDBtn:bool = obj["ChangeTrackChargeIDBtn"]
      """  ChangeTrackChargeIDBtn  """  
      self.ChangeTrackAmount:int = obj["ChangeTrackAmount"]
      """  ChangeTrackAmount  """  
      self.ChangeTrackChargeID:str = obj["ChangeTrackChargeID"]
      """  ChangeTrackChargeID  """  
      self.ChangeTrackChargeDesc:str = obj["ChangeTrackChargeDesc"]
      """  ChangeTrackChargeDesc  """  
      self.ChangeTrackStatus:str = obj["ChangeTrackStatus"]
      """  ChangeTrackStatus  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CategoryDesc:str = obj["CategoryDesc"]
      """  Description of Category ID  """  
      self.MemoCompanyDate:str = obj["MemoCompanyDate"]
      """  Date that the Memo was created (Company Time).  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   relatedToSchemaName
   relatedToFile
   relatedToSysRowID
   memoNum
   """  
   def __init__(self, obj):
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.memoNum:int = obj["memoNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   relatedToSchemaName
   relatedToFile
   relatedToSysRowID
   memoNum
   """  
   def __init__(self, obj):
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      self.memoNum:int = obj["memoNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MemoTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_MemoTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_MemoTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_MemoListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewMemo_input:
   """ Required : 
   ds
   relatedToSchemaName
   relatedToFile
   relatedToSysRowID
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MemoTableset] = obj["ds"]
      self.relatedToSchemaName:str = obj["relatedToSchemaName"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.relatedToSysRowID:str = obj["relatedToSysRowID"]
      pass

class GetNewMemo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseMemo
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMemo:str = obj["whereClauseMemo"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_MemoTableset] = obj["returnObj"]
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

class Ice_Tablesets_MemoListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the memo is related to.  This field is used to properly  isolate memos to the masters they are related to.
For example; Customer, Vendor, PREmpMas identifies memos that are related to Customers, Vendor and Payroll Employee master records.  """  
      self.MemoDate:str = obj["MemoDate"]
      """  Date that the Memo was created.  """  
      self.MemoUserID:str = obj["MemoUserID"]
      """  User Id that created the memo. DCDUserID.  """  
      self.MemoDesc:str = obj["MemoDesc"]
      """  An abbreviated description of what the memo is about.  This will be shown in browses of memos.  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Category ID that this memo is assigned to .  This field contains the foreign key of the related MemoCat master.  It can be blank or it must be valid in the MemoCat.  """  
      self.CategoryDesc:str = obj["CategoryDesc"]
      """  Category ID that this memo is assigned to.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MemoListTableset:
   def __init__(self, obj):
      self.MemoList:list[Ice_Tablesets_MemoListRow] = obj["MemoList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_MemoRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   The master file to which the memo is related to.  This field is used to properly  isolate memos to the masters they are related to.
For example; Customer, Vendor, PREmpMas identifies memos that are related to Customers, Vendor and Payroll Employee master records.  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  memo this field would contain the related Part Number,  for a "Customer" memo it contains the Customers CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
For example: For a "OrderDtl"  memo this field would contain the OrderLine # of the related Order detail record.  The usage of this field is dependent on the type of record the memo is related to.  For example "Part" memo's do not use this field while PartRev memos would.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
For example: For a "OrderRel"  memo this field would contain the Order Line Release # of the related Order Release record.  The usage of this field is dependent on the type of record the memo is related to.  """  
      self.MemoDate:str = obj["MemoDate"]
      """  Date that the Memo was created.  """  
      self.MemoNum:int = obj["MemoNum"]
      """  An integer assigned by the system to uniquely identify the Memo. This integer is created by using the database sequence "MemoSeq".  """  
      self.MemoUserID:str = obj["MemoUserID"]
      """  User Id that created the memo. DCDUserID.  """  
      self.Notify:bool = obj["Notify"]
      """  Indicates if this memo is or is not on the memo "Notify" list. The user can set this flag to indicate that there is something about the  memo that they wish to be notified of at a later date (such as customer follow-up, callback...).  """  
      self.NotifyUserID:str = obj["NotifyUserID"]
      """  User Id that is to be Notified about this memo. Defaults to Current DCDUserID.  """  
      self.NotifyDate:str = obj["NotifyDate"]
      """  Date that the user is to be notified about this memo.  """  
      self.MemoDesc:str = obj["MemoDesc"]
      """  An abbreviated description of what the memo is about.  This will be shown in browses of memos.  """  
      self.MemoText:str = obj["MemoText"]
      """  MemoText contains the textual content of the memo. Intended to be used as internal online storage of text information related to a specific master. They do get pulled into other database records. To be viewed-as a progress  EDITOR widget.  """  
      self.CategoryID:str = obj["CategoryID"]
      """  Category ID that this memo is assigned to .  This field contains the foreign key of the related MemoCat master.  It can be blank or it must be valid in the MemoCat.  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.ChangeTrackChargeIDBtn:bool = obj["ChangeTrackChargeIDBtn"]
      """  ChangeTrackChargeIDBtn  """  
      self.ChangeTrackAmount:int = obj["ChangeTrackAmount"]
      """  ChangeTrackAmount  """  
      self.ChangeTrackChargeID:str = obj["ChangeTrackChargeID"]
      """  ChangeTrackChargeID  """  
      self.ChangeTrackChargeDesc:str = obj["ChangeTrackChargeDesc"]
      """  ChangeTrackChargeDesc  """  
      self.ChangeTrackStatus:str = obj["ChangeTrackStatus"]
      """  ChangeTrackStatus  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CategoryDesc:str = obj["CategoryDesc"]
      """  Description of Category ID  """  
      self.MemoCompanyDate:str = obj["MemoCompanyDate"]
      """  Date that the Memo was created (Company Time).  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_MemoTableset:
   def __init__(self, obj):
      self.Memo:list[Ice_Tablesets_MemoRow] = obj["Memo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_UpdExtMemoTableset:
   def __init__(self, obj):
      self.Memo:list[Ice_Tablesets_MemoRow] = obj["Memo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtMemoTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtMemoTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_MemoTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_MemoTableset] = obj["ds"]
      pass

      """  output parameters  """  

