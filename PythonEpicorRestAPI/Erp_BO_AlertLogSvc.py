import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.AlertLogSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_AlertLogs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AlertLogs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AlertLogs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlertLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/AlertLogs",headers=creds) as resp:
           return await resp.json()

async def post_AlertLogs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AlertLogs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AlertLogRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AlertLogRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/AlertLogs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AlertLogs_Company_Alertnum_ErrLogNum(Company, Alertnum, ErrLogNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AlertLog item
   Description: Calls GetByID to retrieve the AlertLog item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AlertLog
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Alertnum: Desc: Alertnum   Required: True
      :param ErrLogNum: Desc: ErrLogNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AlertLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/AlertLogs(" + Company + "," + Alertnum + "," + ErrLogNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AlertLogs_Company_Alertnum_ErrLogNum(Company, Alertnum, ErrLogNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AlertLog for the service
   Description: Calls UpdateExt to update AlertLog. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AlertLog
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Alertnum: Desc: Alertnum   Required: True
      :param ErrLogNum: Desc: ErrLogNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AlertLogRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/AlertLogs(" + Company + "," + Alertnum + "," + ErrLogNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AlertLogs_Company_Alertnum_ErrLogNum(Company, Alertnum, ErrLogNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AlertLog item
   Description: Call UpdateExt to delete AlertLog item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AlertLog
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Alertnum: Desc: Alertnum   Required: True
      :param ErrLogNum: Desc: ErrLogNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/AlertLogs(" + Company + "," + Alertnum + "," + ErrLogNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AlertLogListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseAlertLog, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseAlertLog=" + whereClauseAlertLog
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(alertnum, errLogNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "alertnum=" + alertnum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "errLogNum=" + errLogNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ALogDeleteAll(epicorHeaders = None):
   """  
   Summary: Invoke method ALogDeleteAll
   Description: This method deletes all alert logs for current company.
   OperationID: ALogDeleteAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ALogDeleteAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_Resend(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Resend
   Description: This method resends specified alert log row.
   OperationID: Resend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Resend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Resend_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAlertLogRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAlertLogRows
   Description: Method performing search for Alert Logs in Kinetic only.
   OperationID: GetAlertLogRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAlertLogRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAlertLogRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAlertLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAlertLog
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAlertLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAlertLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAlertLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.AlertLogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlertLogListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlertLogListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AlertLogRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AlertLogRow] = obj["value"]
      pass

class Erp_Tablesets_AlertLogListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Alertnum:int = obj["Alertnum"]
      """  Identifies the record  """  
      self.ErrLogNum:int = obj["ErrLogNum"]
      """   Unique identifier - created by finding the last GlbAlrtLog with the
same company and alert number and adding 1 to its ErrLogNum  """  
      self.ErrorType:str = obj["ErrorType"]
      """   Identifies the type of error that caused the email to fail,
'mail' - email not running, 'recp' - A recipient was not in the
email list  """  
      self.Description:str = obj["Description"]
      """  Description for the alert from GlbAlert  """  
      self.EMailAddr:str = obj["EMailAddr"]
      """   Email address list including additional mail to names like
salesperson  """  
      self.EMailCC:str = obj["EMailCC"]
      """  Email address list  """  
      self.Sender:str = obj["Sender"]
      """  The ID of the person that attempted to Send the email.  Defaults to current DCD-UserID when the record is created.  """  
      self.SentDate:str = obj["SentDate"]
      """  Date when the Email was sent.  """  
      self.SentTime:int = obj["SentTime"]
      """   Time of day when the email was sent.
(seconds since midnight format)  """  
      self.AlertText:str = obj["AlertText"]
      """  Alert text  """  
      self.EmailFromAddr:str = obj["EmailFromAddr"]
      """  The email address to be used as the "From" portion of the email.  """  
      self.EmailFromLabel:str = obj["EmailFromLabel"]
      """  The label used for the "From" email address.  If blank then just the email address will be used.  """  
      self.MimeHeader:str = obj["MimeHeader"]
      """  The Mime Header sent with the email.  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Error text returned through SMTP.  """  
      self.AlertDate:str = obj["AlertDate"]
      """  Date this alert was created.  """  
      self.AlertTime:int = obj["AlertTime"]
      """   Time of day when the alert was created.
(seconds since midnight format)  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AlertnumDescription:str = obj["AlertnumDescription"]
      """  User definable description for the alert  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlertLogRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Alertnum:int = obj["Alertnum"]
      """  Identifies the record  """  
      self.ErrLogNum:int = obj["ErrLogNum"]
      """   Unique identifier - created by finding the last GlbAlrtLog with the
same company and alert number and adding 1 to its ErrLogNum  """  
      self.ErrorType:str = obj["ErrorType"]
      """   Identifies the type of error that caused the email to fail,
'mail' - email not running, 'recp' - A recipient was not in the
email list  """  
      self.Description:str = obj["Description"]
      """  Description for the alert from GlbAlert  """  
      self.EMailAddr:str = obj["EMailAddr"]
      """   Email address list including additional mail to names like
salesperson  """  
      self.EMailCC:str = obj["EMailCC"]
      """  Email address list  """  
      self.Sender:str = obj["Sender"]
      """  The ID of the person that attempted to Send the email.  Defaults to current DCD-UserID when the record is created.  """  
      self.SentDate:str = obj["SentDate"]
      """  Date when the Email was sent.  """  
      self.SentTime:int = obj["SentTime"]
      """   Time of day when the email was sent.
(seconds since midnight format)  """  
      self.AlertText:str = obj["AlertText"]
      """  Alert text  """  
      self.EmailFromAddr:str = obj["EmailFromAddr"]
      """  The email address to be used as the "From" portion of the email.  """  
      self.EmailFromLabel:str = obj["EmailFromLabel"]
      """  The label used for the "From" email address.  If blank then just the email address will be used.  """  
      self.MimeHeader:str = obj["MimeHeader"]
      """  The Mime Header sent with the email.  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Error text returned through SMTP.  """  
      self.AlertDate:str = obj["AlertDate"]
      """  Date this alert was created.  """  
      self.AlertTime:int = obj["AlertTime"]
      """   Time of day when the alert was created.
(seconds since midnight format)  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AlertnumDescription:str = obj["AlertnumDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ALogDeleteAll_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   alertnum
   errLogNum
   """  
   def __init__(self, obj):
      self.alertnum:int = obj["alertnum"]
      self.errLogNum:int = obj["errLogNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AlertLogListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Alertnum:int = obj["Alertnum"]
      """  Identifies the record  """  
      self.ErrLogNum:int = obj["ErrLogNum"]
      """   Unique identifier - created by finding the last GlbAlrtLog with the
same company and alert number and adding 1 to its ErrLogNum  """  
      self.ErrorType:str = obj["ErrorType"]
      """   Identifies the type of error that caused the email to fail,
'mail' - email not running, 'recp' - A recipient was not in the
email list  """  
      self.Description:str = obj["Description"]
      """  Description for the alert from GlbAlert  """  
      self.EMailAddr:str = obj["EMailAddr"]
      """   Email address list including additional mail to names like
salesperson  """  
      self.EMailCC:str = obj["EMailCC"]
      """  Email address list  """  
      self.Sender:str = obj["Sender"]
      """  The ID of the person that attempted to Send the email.  Defaults to current DCD-UserID when the record is created.  """  
      self.SentDate:str = obj["SentDate"]
      """  Date when the Email was sent.  """  
      self.SentTime:int = obj["SentTime"]
      """   Time of day when the email was sent.
(seconds since midnight format)  """  
      self.AlertText:str = obj["AlertText"]
      """  Alert text  """  
      self.EmailFromAddr:str = obj["EmailFromAddr"]
      """  The email address to be used as the "From" portion of the email.  """  
      self.EmailFromLabel:str = obj["EmailFromLabel"]
      """  The label used for the "From" email address.  If blank then just the email address will be used.  """  
      self.MimeHeader:str = obj["MimeHeader"]
      """  The Mime Header sent with the email.  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Error text returned through SMTP.  """  
      self.AlertDate:str = obj["AlertDate"]
      """  Date this alert was created.  """  
      self.AlertTime:int = obj["AlertTime"]
      """   Time of day when the alert was created.
(seconds since midnight format)  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AlertnumDescription:str = obj["AlertnumDescription"]
      """  User definable description for the alert  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlertLogListTableset:
   def __init__(self, obj):
      self.AlertLogList:list[Erp_Tablesets_AlertLogListRow] = obj["AlertLogList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_AlertLogRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Alertnum:int = obj["Alertnum"]
      """  Identifies the record  """  
      self.ErrLogNum:int = obj["ErrLogNum"]
      """   Unique identifier - created by finding the last GlbAlrtLog with the
same company and alert number and adding 1 to its ErrLogNum  """  
      self.ErrorType:str = obj["ErrorType"]
      """   Identifies the type of error that caused the email to fail,
'mail' - email not running, 'recp' - A recipient was not in the
email list  """  
      self.Description:str = obj["Description"]
      """  Description for the alert from GlbAlert  """  
      self.EMailAddr:str = obj["EMailAddr"]
      """   Email address list including additional mail to names like
salesperson  """  
      self.EMailCC:str = obj["EMailCC"]
      """  Email address list  """  
      self.Sender:str = obj["Sender"]
      """  The ID of the person that attempted to Send the email.  Defaults to current DCD-UserID when the record is created.  """  
      self.SentDate:str = obj["SentDate"]
      """  Date when the Email was sent.  """  
      self.SentTime:int = obj["SentTime"]
      """   Time of day when the email was sent.
(seconds since midnight format)  """  
      self.AlertText:str = obj["AlertText"]
      """  Alert text  """  
      self.EmailFromAddr:str = obj["EmailFromAddr"]
      """  The email address to be used as the "From" portion of the email.  """  
      self.EmailFromLabel:str = obj["EmailFromLabel"]
      """  The label used for the "From" email address.  If blank then just the email address will be used.  """  
      self.MimeHeader:str = obj["MimeHeader"]
      """  The Mime Header sent with the email.  """  
      self.ErrorText:str = obj["ErrorText"]
      """  Error text returned through SMTP.  """  
      self.AlertDate:str = obj["AlertDate"]
      """  Date this alert was created.  """  
      self.AlertTime:int = obj["AlertTime"]
      """   Time of day when the alert was created.
(seconds since midnight format)  """  
      self.Plant:str = obj["Plant"]
      """  Unique identifier of this Site assigned by the user.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AlertnumDescription:str = obj["AlertnumDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AlertLogTableset:
   def __init__(self, obj):
      self.AlertLog:list[Erp_Tablesets_AlertLogRow] = obj["AlertLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtAlertLogTableset:
   def __init__(self, obj):
      self.AlertLog:list[Erp_Tablesets_AlertLogRow] = obj["AlertLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAlertLogRows_input:
   """ Required : 
   ipSender
   ipSentDate
   ipAll
   ipGlobalAlerts
   ipShopWarnings
   ipChangeLogAlerts
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.ipSender:str = obj["ipSender"]
      self.ipSentDate      #schema had no properties on an object.
      self.ipAll:bool = obj["ipAll"]
      self.ipGlobalAlerts:bool = obj["ipGlobalAlerts"]
      self.ipShopWarnings:bool = obj["ipShopWarnings"]
      self.ipChangeLogAlerts:bool = obj["ipChangeLogAlerts"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetAlertLogRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlertLogTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   alertnum
   errLogNum
   """  
   def __init__(self, obj):
      self.alertnum:int = obj["alertnum"]
      self.errLogNum:int = obj["errLogNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlertLogTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AlertLogTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AlertLogTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_AlertLogListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewAlertLog_input:
   """ Required : 
   ds
   alertnum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlertLogTableset] = obj["ds"]
      self.alertnum:int = obj["alertnum"]
      pass

class GetNewAlertLog_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlertLogTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseAlertLog
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseAlertLog:str = obj["whereClauseAlertLog"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_AlertLogTableset] = obj["returnObj"]
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

class Resend_input:
   """ Required : 
   AlertLogRowid
   ds
   """  
   def __init__(self, obj):
      self.AlertLogRowid:str = obj["AlertLogRowid"]
      """  The RowIdent of the record of which Resend  """  
      self.ds:list[Erp_Tablesets_AlertLogTableset] = obj["ds"]
      pass

class Resend_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlertLogTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAlertLogTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtAlertLogTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_AlertLogTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_AlertLogTableset] = obj["ds"]
      pass

      """  output parameters  """  

