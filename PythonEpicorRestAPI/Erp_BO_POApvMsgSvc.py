import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.POApvMsgSvc
# Description: Purchase Order Approval Message queue.
This table contains two record types.
One to notifiy the approver about PO's which have exceed the buyers limit and need to be reviewed.
The other to notify the buyer when the approver responds.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_POApvMsgs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get POApvMsgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_POApvMsgs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POApvMsgRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/POApvMsgs",headers=creds) as resp:
           return await resp.json()

async def post_POApvMsgs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_POApvMsgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.POApvMsgRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.POApvMsgRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/POApvMsgs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_POApvMsgs_Company_PONum(Company, PONum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the POApvMsg item
   Description: Calls GetByID to retrieve the POApvMsg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_POApvMsg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.POApvMsgRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/POApvMsgs(" + Company + "," + PONum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_POApvMsgs_Company_PONum(Company, PONum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update POApvMsg for the service
   Description: Calls UpdateExt to update POApvMsg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_POApvMsg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.POApvMsgRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/POApvMsgs(" + Company + "," + PONum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_POApvMsgs_Company_PONum(Company, PONum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete POApvMsg item
   Description: Call UpdateExt to delete POApvMsg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_POApvMsg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PONum: Desc: PONum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/POApvMsgs(" + Company + "," + PONum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.POApvMsgListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePOApvMsg, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePOApvMsg=" + whereClausePOApvMsg
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(poNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "poNum=" + poNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckApprovalLimit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckApprovalLimit
   Description: This method determines whether the Approval needs to be passed on to a manager
To be run before the update method
   OperationID: CheckApprovalLimit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckApprovalLimit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckApprovalLimit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAllRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllRows
   Description: GetAllRows displays all the rows from POApvMsg table just like GetRows.
Except - no filtering of POApvMsg records based on PurAuth will be
performed in afterGetRows.
   OperationID: GetAllRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetApprovalActivity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetApprovalActivity
   Description: GetApprovalActivity displays all the rows from POApvMsg table just like GetRows.
Only records for the current user OR to an authorized buyer are returned
   OperationID: GetApprovalActivity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetApprovalActivity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApprovalActivity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFullText(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFullText
   OperationID: GetFullText
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFullText_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFullText_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDateUser(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDateUser
   Description: This method puts a date/time/user stamp in the MsgText box for the user
   OperationID: GetDateUser
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDateUser_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDateUser_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPOApvMsg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPOApvMsg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPOApvMsg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPOApvMsg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPOApvMsg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.POApvMsgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POApvMsgListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_POApvMsgListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_POApvMsgRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_POApvMsgRow] = obj["value"]
      pass

class Erp_Tablesets_POApvMsgListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order record is related to.  """  
      self.MsgType:str = obj["MsgType"]
      """   1 = Request for approval.
2 = Approver Response.  """  
      self.MsgDate:str = obj["MsgDate"]
      """  Date of message.  """  
      self.MsgTime:int = obj["MsgTime"]
      """  Time of message.  Defined as secounds since midnight.  """  
      self.MsgTo:str = obj["MsgTo"]
      """  BuyerID of the user that is requesting or responding, depends on record type.  """  
      self.MsgFrom:str = obj["MsgFrom"]
      """  BuyerID of the user that is requesting or responding, depends on record type.  """  
      self.MsgText:str = obj["MsgText"]
      """  Contains text for communication.  """  
      self.ApproverResponse:str = obj["ApproverResponse"]
      """   Short description of the response from the approver.
Either "Approved","Rejected","Manually Unapproved" or "Manually Closed"  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID that created/updated the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorName:str = obj["VendorName"]
      self.BuyerName:str = obj["BuyerName"]
      self.BuyerLimit:int = obj["BuyerLimit"]
      self.POAmt:int = obj["POAmt"]
      self.ApvAmt:int = obj["ApvAmt"]
      self.MsgTimeString:str = obj["MsgTimeString"]
      self.ApproverName:str = obj["ApproverName"]
      self.MsgToName:str = obj["MsgToName"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POApvMsgRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order record is related to.  """  
      self.MsgType:str = obj["MsgType"]
      """   1 = Request for approval.
2 = Approver Response.  """  
      self.MsgDate:str = obj["MsgDate"]
      """  Date of message.  """  
      self.MsgTime:int = obj["MsgTime"]
      """  Time of message.  Defined as secounds since midnight.  """  
      self.MsgTo:str = obj["MsgTo"]
      """  BuyerID of the user that is requesting or responding, depends on record type.  """  
      self.MsgFrom:str = obj["MsgFrom"]
      """  BuyerID of the user that is requesting or responding, depends on record type.  """  
      self.MsgText:str = obj["MsgText"]
      """  Contains text for communication.  """  
      self.ApproverResponse:str = obj["ApproverResponse"]
      """   Short description of the response from the approver.
Either "Approved","Rejected","Manually Unapproved" or "Manually Closed"  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID that created/updated the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorName:str = obj["VendorName"]
      self.BuyerName:str = obj["BuyerName"]
      self.BuyerLimit:int = obj["BuyerLimit"]
      self.POAmt:int = obj["POAmt"]
      self.ApvAmt:int = obj["ApvAmt"]
      self.MsgTimeString:str = obj["MsgTimeString"]
      self.ApproverName:str = obj["ApproverName"]
      self.BitFlag:int = obj["BitFlag"]
      self.MsgToName:str = obj["MsgToName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckApprovalLimit_input:
   """ Required : 
   vPONum
   vAprvAmt
   vApproved
   """  
   def __init__(self, obj):
      self.vPONum:int = obj["vPONum"]
      """  PO Number  """  
      self.vAprvAmt:int = obj["vAprvAmt"]
      """  Amount being Approved  """  
      self.vApproved:str = obj["vApproved"]
      """  Approver Response  """  
      pass

class CheckApprovalLimit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   poNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_POApvMsgListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order record is related to.  """  
      self.MsgType:str = obj["MsgType"]
      """   1 = Request for approval.
2 = Approver Response.  """  
      self.MsgDate:str = obj["MsgDate"]
      """  Date of message.  """  
      self.MsgTime:int = obj["MsgTime"]
      """  Time of message.  Defined as secounds since midnight.  """  
      self.MsgTo:str = obj["MsgTo"]
      """  BuyerID of the user that is requesting or responding, depends on record type.  """  
      self.MsgFrom:str = obj["MsgFrom"]
      """  BuyerID of the user that is requesting or responding, depends on record type.  """  
      self.MsgText:str = obj["MsgText"]
      """  Contains text for communication.  """  
      self.ApproverResponse:str = obj["ApproverResponse"]
      """   Short description of the response from the approver.
Either "Approved","Rejected","Manually Unapproved" or "Manually Closed"  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID that created/updated the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorName:str = obj["VendorName"]
      self.BuyerName:str = obj["BuyerName"]
      self.BuyerLimit:int = obj["BuyerLimit"]
      self.POAmt:int = obj["POAmt"]
      self.ApvAmt:int = obj["ApvAmt"]
      self.MsgTimeString:str = obj["MsgTimeString"]
      self.ApproverName:str = obj["ApproverName"]
      self.MsgToName:str = obj["MsgToName"]
      """  Name of Purchasing Agent or Group. This is printed on the PO by the authorized signature line.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POApvMsgListTableset:
   def __init__(self, obj):
      self.POApvMsgList:list[Erp_Tablesets_POApvMsgListRow] = obj["POApvMsgList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_POApvMsgRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order record is related to.  """  
      self.MsgType:str = obj["MsgType"]
      """   1 = Request for approval.
2 = Approver Response.  """  
      self.MsgDate:str = obj["MsgDate"]
      """  Date of message.  """  
      self.MsgTime:int = obj["MsgTime"]
      """  Time of message.  Defined as secounds since midnight.  """  
      self.MsgTo:str = obj["MsgTo"]
      """  BuyerID of the user that is requesting or responding, depends on record type.  """  
      self.MsgFrom:str = obj["MsgFrom"]
      """  BuyerID of the user that is requesting or responding, depends on record type.  """  
      self.MsgText:str = obj["MsgText"]
      """  Contains text for communication.  """  
      self.ApproverResponse:str = obj["ApproverResponse"]
      """   Short description of the response from the approver.
Either "Approved","Rejected","Manually Unapproved" or "Manually Closed"  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID that created/updated the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.VendorName:str = obj["VendorName"]
      self.BuyerName:str = obj["BuyerName"]
      self.BuyerLimit:int = obj["BuyerLimit"]
      self.POAmt:int = obj["POAmt"]
      self.ApvAmt:int = obj["ApvAmt"]
      self.MsgTimeString:str = obj["MsgTimeString"]
      self.ApproverName:str = obj["ApproverName"]
      self.BitFlag:int = obj["BitFlag"]
      self.MsgToName:str = obj["MsgToName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POApvMsgTableset:
   def __init__(self, obj):
      self.POApvMsg:list[Erp_Tablesets_POApvMsgRow] = obj["POApvMsg"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPOApvMsgTableset:
   def __init__(self, obj):
      self.POApvMsg:list[Erp_Tablesets_POApvMsgRow] = obj["POApvMsg"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAllRows_input:
   """ Required : 
   whereClausePOApvMsg
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePOApvMsg:str = obj["whereClausePOApvMsg"]
      """  Where Clause for POApvMsg table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolutePage  """  
      pass

class GetAllRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POApvMsgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetApprovalActivity_input:
   """ Required : 
   whereClausePOApvMsg
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePOApvMsg:str = obj["whereClausePOApvMsg"]
      """  Where Clause for POApvMsg table.  """  
      self.pageSize:int = obj["pageSize"]
      """  Page Size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  absolutePage  """  
      pass

class GetApprovalActivity_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POApvMsgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   poNum
   """  
   def __init__(self, obj):
      self.poNum:int = obj["poNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POApvMsgTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_POApvMsgTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_POApvMsgTableset] = obj["returnObj"]
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

class GetDateUser_input:
   """ Required : 
   ipBuyerID
   """  
   def __init__(self, obj):
      self.ipBuyerID:str = obj["ipBuyerID"]
      """  Buyer ID  """  
      pass

class GetDateUser_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opName:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFullText_input:
   """ Required : 
   ipBuyerID
   opName
   msgText
   """  
   def __init__(self, obj):
      self.ipBuyerID:str = obj["ipBuyerID"]
      self.opName:str = obj["opName"]
      self.msgText:str = obj["msgText"]
      pass

class GetFullText_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.fullText:str = obj["parameters"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_POApvMsgListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPOApvMsg_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POApvMsgTableset] = obj["ds"]
      pass

class GetNewPOApvMsg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POApvMsgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePOApvMsg
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePOApvMsg:str = obj["whereClausePOApvMsg"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_POApvMsgTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtPOApvMsgTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPOApvMsgTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_POApvMsgTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_POApvMsgTableset] = obj["ds"]
      pass

      """  output parameters  """  

