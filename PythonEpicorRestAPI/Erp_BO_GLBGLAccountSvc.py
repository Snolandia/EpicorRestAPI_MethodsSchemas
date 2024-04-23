import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLBGLAccountSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GLBGLAccounts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get GLBGLAccounts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLBGLAccounts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLBGLAccountRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GLBGLAccounts",headers=creds) as resp:
           return await resp.json()

async def post_GLBGLAccounts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLBGLAccounts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLBGLAccountRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.GLBGLAccountRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GLBGLAccounts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GLBGLAccounts_Company_ExtCompanyID_COACode_GLAccount(Company, ExtCompanyID, COACode, GLAccount, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the GLBGLAccount item
   Description: Calls GetByID to retrieve the GLBGLAccount item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLBGLAccount
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param GLAccount: Desc: GLAccount   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.GLBGLAccountRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GLBGLAccounts(" + Company + "," + ExtCompanyID + "," + COACode + "," + GLAccount + ")",headers=creds) as resp:
           return await resp.json()

async def patch_GLBGLAccounts_Company_ExtCompanyID_COACode_GLAccount(Company, ExtCompanyID, COACode, GLAccount, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update GLBGLAccount for the service
   Description: Calls UpdateExt to update GLBGLAccount. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLBGLAccount
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param GLAccount: Desc: GLAccount   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLBGLAccountRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GLBGLAccounts(" + Company + "," + ExtCompanyID + "," + COACode + "," + GLAccount + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_GLBGLAccounts_Company_ExtCompanyID_COACode_GLAccount(Company, ExtCompanyID, COACode, GLAccount, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete GLBGLAccount item
   Description: Call UpdateExt to delete GLBGLAccount item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLBGLAccount
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ExtCompanyID: Desc: ExtCompanyID   Required: True   Allow empty value : True
      :param COACode: Desc: COACode   Required: True   Allow empty value : True
      :param GLAccount: Desc: GLAccount   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/GLBGLAccounts(" + Company + "," + ExtCompanyID + "," + COACode + "," + GLAccount + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbGLAccountListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseGLBGLAccount, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseGLBGLAccount=" + whereClauseGLBGLAccount
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(extCompanyID, coACode, glAccount, epicorHeaders = None):
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
   params += "extCompanyID=" + extCompanyID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "coACode=" + coACode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "glAccount=" + glAccount

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewGLBGLAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewGLBGLAccount
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLBGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewGLBGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLBGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLBGLAccountSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLBGLAccountRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GLBGLAccountRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbGLAccountListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_GlbGLAccountListRow] = obj["value"]
      pass

class Erp_Tablesets_GLBGLAccountRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.AccountDesc:str = obj["AccountDesc"]
      """  Text that describes the account.  """  
      self.GLShortAcct:str = obj["GLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The initial default value consits of the concatenation of the first three segments in display sequence order.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.PreservDesc:bool = obj["PreservDesc"]
      """  Indicates if the entered description shall be preserved when the tool to automatically generate GL Acocunts is used.  Default value = yes.  """  
      self.PreserveActivation:bool = obj["PreserveActivation"]
      """  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this accoun tis active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  """  
      self.EffFrom:str = obj["EffFrom"]
      """  Date the GL Account beings to be effective.  It must be less than or equal to the Effective to date if one has been entered.  """  
      self.EffTo:str = obj["EffTo"]
      """  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  A flag to indicate this GL Account my recieve multi-company journals.  """  
      self.ParentGLAccount:str = obj["ParentGLAccount"]
      """  Full account including separator value up to 200 characters.  Unique identifier for the GL Account.  """  
      self.PntSegValue1:str = obj["PntSegValue1"]
      """  Parent SegmentValue 1.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue2:str = obj["PntSegValue2"]
      """  Parent SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.PntSegValue3:str = obj["PntSegValue3"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue4:str = obj["PntSegValue4"]
      """  Parent SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.PntSegValue5:str = obj["PntSegValue5"]
      """  Parent SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.PntSegValue6:str = obj["PntSegValue6"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue7:str = obj["PntSegValue7"]
      """  Parent SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.PntSegValue8:str = obj["PntSegValue8"]
      """  Parent SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.PntSegValue9:str = obj["PntSegValue9"]
      """  Parent SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.PntSegValue10:str = obj["PntSegValue10"]
      """  Parent SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.PntSegValue11:str = obj["PntSegValue11"]
      """  Parent SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue12:str = obj["PntSegValue12"]
      """  Parent SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.PntSegValue13:str = obj["PntSegValue13"]
      """  Parent SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.PntSegValue14:str = obj["PntSegValue14"]
      """  Parent SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.PntSegValue15:str = obj["PntSegValue15"]
      """  Parent SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.PntSegValue16:str = obj["PntSegValue16"]
      """  Parent SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.PntSegValue17:str = obj["PntSegValue17"]
      """  Parent SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.PntSegValue18:str = obj["PntSegValue18"]
      """  Parent SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.PntSegValue19:str = obj["PntSegValue19"]
      """  Parent SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.PntSegValue20:str = obj["PntSegValue20"]
      """  Parent SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtCompID:str = obj["ExtCompID"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GlbGLAcctDispGLAcctDisp:str = obj["GlbGLAcctDispGLAcctDisp"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbGLAccountListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.AccountDesc:str = obj["AccountDesc"]
      """  Text that describes the account.  """  
      self.GLShortAcct:str = obj["GLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The initial default value consits of the concatenation of the first three segments in display sequence order.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.PreservDesc:bool = obj["PreservDesc"]
      """  Indicates if the entered description shall be preserved when the tool to automatically generate GL Acocunts is used.  Default value = yes.  """  
      self.PreserveActivation:bool = obj["PreserveActivation"]
      """  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this accoun tis active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  """  
      self.EffFrom:str = obj["EffFrom"]
      """  Date the GL Account beings to be effective.  It must be less than or equal to the Effective to date if one has been entered.  """  
      self.EffTo:str = obj["EffTo"]
      """  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  A flag to indicate this GL Account my recieve multi-company journals.  """  
      self.ParentGLAccount:str = obj["ParentGLAccount"]
      """  Full account including separator value up to 200 characters.  Unique identifier for the GL Account.  """  
      self.PntSegValue1:str = obj["PntSegValue1"]
      """  Parent SegmentValue 1.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue2:str = obj["PntSegValue2"]
      """  Parent SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.PntSegValue3:str = obj["PntSegValue3"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue4:str = obj["PntSegValue4"]
      """  Parent SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.PntSegValue5:str = obj["PntSegValue5"]
      """  Parent SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.PntSegValue6:str = obj["PntSegValue6"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue7:str = obj["PntSegValue7"]
      """  Parent SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.PntSegValue8:str = obj["PntSegValue8"]
      """  Parent SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.PntSegValue9:str = obj["PntSegValue9"]
      """  Parent SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.PntSegValue10:str = obj["PntSegValue10"]
      """  Parent SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.PntSegValue11:str = obj["PntSegValue11"]
      """  Parent SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue12:str = obj["PntSegValue12"]
      """  Parent SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.PntSegValue13:str = obj["PntSegValue13"]
      """  Parent SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.PntSegValue14:str = obj["PntSegValue14"]
      """  Parent SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.PntSegValue15:str = obj["PntSegValue15"]
      """  Parent SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.PntSegValue16:str = obj["PntSegValue16"]
      """  Parent SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.PntSegValue17:str = obj["PntSegValue17"]
      """  Parent SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.PntSegValue18:str = obj["PntSegValue18"]
      """  Parent SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.PntSegValue19:str = obj["PntSegValue19"]
      """  Parent SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.PntSegValue20:str = obj["PntSegValue20"]
      """  Parent SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtCompID:str = obj["ExtCompID"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbGLAcctDispGLAcctDisp:str = obj["GlbGLAcctDispGLAcctDisp"]
      """  This is the GL Account in display order sequence.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   extCompanyID
   coACode
   glAccount
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      self.glAccount:str = obj["glAccount"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_GLBGLAccountRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.AccountDesc:str = obj["AccountDesc"]
      """  Text that describes the account.  """  
      self.GLShortAcct:str = obj["GLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The initial default value consits of the concatenation of the first three segments in display sequence order.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.PreservDesc:bool = obj["PreservDesc"]
      """  Indicates if the entered description shall be preserved when the tool to automatically generate GL Acocunts is used.  Default value = yes.  """  
      self.PreserveActivation:bool = obj["PreserveActivation"]
      """  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this accoun tis active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  """  
      self.EffFrom:str = obj["EffFrom"]
      """  Date the GL Account beings to be effective.  It must be less than or equal to the Effective to date if one has been entered.  """  
      self.EffTo:str = obj["EffTo"]
      """  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  A flag to indicate this GL Account my recieve multi-company journals.  """  
      self.ParentGLAccount:str = obj["ParentGLAccount"]
      """  Full account including separator value up to 200 characters.  Unique identifier for the GL Account.  """  
      self.PntSegValue1:str = obj["PntSegValue1"]
      """  Parent SegmentValue 1.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue2:str = obj["PntSegValue2"]
      """  Parent SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.PntSegValue3:str = obj["PntSegValue3"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue4:str = obj["PntSegValue4"]
      """  Parent SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.PntSegValue5:str = obj["PntSegValue5"]
      """  Parent SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.PntSegValue6:str = obj["PntSegValue6"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue7:str = obj["PntSegValue7"]
      """  Parent SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.PntSegValue8:str = obj["PntSegValue8"]
      """  Parent SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.PntSegValue9:str = obj["PntSegValue9"]
      """  Parent SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.PntSegValue10:str = obj["PntSegValue10"]
      """  Parent SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.PntSegValue11:str = obj["PntSegValue11"]
      """  Parent SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue12:str = obj["PntSegValue12"]
      """  Parent SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.PntSegValue13:str = obj["PntSegValue13"]
      """  Parent SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.PntSegValue14:str = obj["PntSegValue14"]
      """  Parent SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.PntSegValue15:str = obj["PntSegValue15"]
      """  Parent SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.PntSegValue16:str = obj["PntSegValue16"]
      """  Parent SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.PntSegValue17:str = obj["PntSegValue17"]
      """  Parent SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.PntSegValue18:str = obj["PntSegValue18"]
      """  Parent SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.PntSegValue19:str = obj["PntSegValue19"]
      """  Parent SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.PntSegValue20:str = obj["PntSegValue20"]
      """  Parent SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtCompID:str = obj["ExtCompID"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.GlbGLAcctDispGLAcctDisp:str = obj["GlbGLAcctDispGLAcctDisp"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLBGLAccountTableset:
   def __init__(self, obj):
      self.GLBGLAccount:list[Erp_Tablesets_GLBGLAccountRow] = obj["GLBGLAccount"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GlbGLAccountListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Company ID of the external company this COA was imported from.  """  
      self.COACode:str = obj["COACode"]
      """  Chart of Account ID  """  
      self.GLAccount:str = obj["GLAccount"]
      """  Full GL account containing the controlled segment valid combinations up to 200 characters including the segment separator.  This si the unique identifier for the GL Account.  """  
      self.AccountDesc:str = obj["AccountDesc"]
      """  Text that describes the account.  """  
      self.GLShortAcct:str = obj["GLShortAcct"]
      """  Optional field that may be used for reporting purpose when the GL Account exceeds the space available on a printed document.  It is a shortened version of the 200 character GL Account that displays on reports.  The initial default value consits of the concatenation of the first three segments in display sequence order.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.PreservDesc:bool = obj["PreservDesc"]
      """  Indicates if the entered description shall be preserved when the tool to automatically generate GL Acocunts is used.  Default value = yes.  """  
      self.PreserveActivation:bool = obj["PreserveActivation"]
      """  Indicates if the 'Active' flag and the 'Effective Date Range' shall be preserved when the tool to automatically generate GL accounts is used.  Default value = no.  """  
      self.Active:bool = obj["Active"]
      """  Indicates if this accoun tis active.  The user cannot post to an inactive account.  Yes indicates the account is active.  No indicates the account is not active.  """  
      self.EffFrom:str = obj["EffFrom"]
      """  Date the GL Account beings to be effective.  It must be less than or equal to the Effective to date if one has been entered.  """  
      self.EffTo:str = obj["EffTo"]
      """  Date the GL Account is no longer effective.  This date must be greater than or equal to the Effective From date if one has been entered.  """  
      self.MultiCompany:bool = obj["MultiCompany"]
      """  A flag to indicate this GL Account my recieve multi-company journals.  """  
      self.ParentGLAccount:str = obj["ParentGLAccount"]
      """  Full account including separator value up to 200 characters.  Unique identifier for the GL Account.  """  
      self.PntSegValue1:str = obj["PntSegValue1"]
      """  Parent SegmentValue 1.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue2:str = obj["PntSegValue2"]
      """  Parent SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.PntSegValue3:str = obj["PntSegValue3"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue4:str = obj["PntSegValue4"]
      """  Parent SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.PntSegValue5:str = obj["PntSegValue5"]
      """  Parent SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.PntSegValue6:str = obj["PntSegValue6"]
      """  Parent SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.PntSegValue7:str = obj["PntSegValue7"]
      """  Parent SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.PntSegValue8:str = obj["PntSegValue8"]
      """  Parent SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.PntSegValue9:str = obj["PntSegValue9"]
      """  Parent SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.PntSegValue10:str = obj["PntSegValue10"]
      """  Parent SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.PntSegValue11:str = obj["PntSegValue11"]
      """  Parent SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.PntSegValue12:str = obj["PntSegValue12"]
      """  Parent SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.PntSegValue13:str = obj["PntSegValue13"]
      """  Parent SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.PntSegValue14:str = obj["PntSegValue14"]
      """  Parent SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.PntSegValue15:str = obj["PntSegValue15"]
      """  Parent SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.PntSegValue16:str = obj["PntSegValue16"]
      """  Parent SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.PntSegValue17:str = obj["PntSegValue17"]
      """  Parent SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.PntSegValue18:str = obj["PntSegValue18"]
      """  Parent SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.PntSegValue19:str = obj["PntSegValue19"]
      """  Parent SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.PntSegValue20:str = obj["PntSegValue20"]
      """  Parent SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.ExtCompID:str = obj["ExtCompID"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbGLAcctDispGLAcctDisp:str = obj["GlbGLAcctDispGLAcctDisp"]
      """  This is the GL Account in display order sequence.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbGLAccountListTableset:
   def __init__(self, obj):
      self.GlbGLAccountList:list[Erp_Tablesets_GlbGLAccountListRow] = obj["GlbGLAccountList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtGLBGLAccountTableset:
   def __init__(self, obj):
      self.GLBGLAccount:list[Erp_Tablesets_GLBGLAccountRow] = obj["GLBGLAccount"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   extCompanyID
   coACode
   glAccount
   """  
   def __init__(self, obj):
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      self.glAccount:str = obj["glAccount"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBGLAccountTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBGLAccountTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GLBGLAccountTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_GlbGLAccountListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewGLBGLAccount_input:
   """ Required : 
   ds
   extCompanyID
   coACode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBGLAccountTableset] = obj["ds"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.coACode:str = obj["coACode"]
      pass

class GetNewGLBGLAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBGLAccountTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseGLBGLAccount
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseGLBGLAccount:str = obj["whereClauseGLBGLAccount"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLBGLAccountTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtGLBGLAccountTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtGLBGLAccountTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLBGLAccountTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLBGLAccountTableset] = obj["ds"]
      pass

      """  output parameters  """  

