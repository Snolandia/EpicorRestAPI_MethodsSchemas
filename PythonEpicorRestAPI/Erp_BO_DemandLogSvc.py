import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DemandLogSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DemandLogs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandLogs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandLogs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/DemandLogs",headers=creds) as resp:
           return await resp.json()

async def post_DemandLogs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandLogs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandLogRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandLogRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/DemandLogs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandLogs_Company_TranNum_SysDate_SysTime(Company, TranNum, SysDate, SysTime, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandLog item
   Description: Calls GetByID to retrieve the DemandLog item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandLog
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandLogRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/DemandLogs(" + Company + "," + TranNum + "," + SysDate + "," + SysTime + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandLogs_Company_TranNum_SysDate_SysTime(Company, TranNum, SysDate, SysTime, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandLog for the service
   Description: Calls UpdateExt to update DemandLog. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandLog
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandLogRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/DemandLogs(" + Company + "," + TranNum + "," + SysDate + "," + SysTime + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandLogs_Company_TranNum_SysDate_SysTime(Company, TranNum, SysDate, SysTime, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandLog item
   Description: Call UpdateExt to delete DemandLog item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandLog
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranNum: Desc: TranNum   Required: True
      :param SysDate: Desc: SysDate   Required: True   Allow empty value : True
      :param SysTime: Desc: SysTime   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/DemandLogs(" + Company + "," + TranNum + "," + SysDate + "," + SysTime + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandLogListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseDemandLog, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseDemandLog=" + whereClauseDemandLog
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(tranNum, sysDate, sysTime, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
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
   params += "tranNum=" + tranNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sysDate=" + sysDate
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sysTime=" + sysTime

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandLog(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandLog
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandLog
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandLog_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandLog_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandLogSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandLogListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandLogListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandLogRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandLogRow] = obj["value"]
      pass

class Erp_Tablesets_DemandLogListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The Demand Contract this record is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead, DemandDetail, or DemandSchedule record this DemandLog is related to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  The detail line sequence from the DemandDetail or DemandSchedule record this DemandLog is related to.  If this value is zero, the record is related to DemandHead.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  The demand schedule sequence from the DemandSchedule record this DemandLog is related to.  If this and DemandDetailSeq are zero, this record is related to DemandHead.  If this field is zero but DemandDetailSeq is not, this record is related to DemandDetail.  Otherwise this record is related to DemandSchedule.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique identifier for the error log record.  The value is obtained from the DemandLogSeq sequence.  """  
      self.SysDate:str = obj["SysDate"]
      """  The system date the record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.LogText:str = obj["LogText"]
      """  The warning or error text.  """  
      self.Action:str = obj["Action"]
      """  The action that was taken when the demand log entry was created. The valid values are ?Stop? and ?Warning?  """  
      self.LogCode:str = obj["LogCode"]
      """  Code for the Log Action.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  """  
      self.DemandContract:str = obj["DemandContract"]
      self.DispSysTime:str = obj["DispSysTime"]
      self.Code:str = obj["Code"]
      """  Error Code needed for TaskMonitor app in the Workflows of Service Connect.  """  
      self.POnum:str = obj["POnum"]
      """  PO number, The value is obtained from demand Head POnum  """  
      self.CurrentSchNumber:str = obj["CurrentSchNumber"]
      """  Current Schedule Number - get it from demandhead  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandLogRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The Demand Contract this record is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead, DemandDetail, or DemandSchedule record this DemandLog is related to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  The detail line sequence from the DemandDetail or DemandSchedule record this DemandLog is related to.  If this value is zero, the record is related to DemandHead.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  The demand schedule sequence from the DemandSchedule record this DemandLog is related to.  If this and DemandDetailSeq are zero, this record is related to DemandHead.  If this field is zero but DemandDetailSeq is not, this record is related to DemandDetail.  Otherwise this record is related to DemandSchedule.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique identifier for the error log record.  The value is obtained from the DemandLogSeq sequence.  """  
      self.SysDate:str = obj["SysDate"]
      """  The system date the record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.LogText:str = obj["LogText"]
      """  The warning or error text.  """  
      self.Action:str = obj["Action"]
      """  The action that was taken when the demand log entry was created. The valid values are ?Stop? and ?Warning?  """  
      self.LogCode:str = obj["LogCode"]
      """  Code for the Log Action.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  """  
      self.DemandContract:str = obj["DemandContract"]
      self.DispSysTime:str = obj["DispSysTime"]
      self.Code:str = obj["Code"]
      """  Error Code needed for TaskMonitor app in the Workflows of Service Connect.  """  
      self.POnum:str = obj["POnum"]
      """  PO number, The value is obtained from demand Head POnum  """  
      self.CurrentSchNumber:str = obj["CurrentSchNumber"]
      """  Current Schedule Number - get it from demandhead  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   tranNum
   sysDate
   sysTime
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      self.sysDate:str = obj["sysDate"]
      self.sysTime:int = obj["sysTime"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DemandLogListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The Demand Contract this record is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead, DemandDetail, or DemandSchedule record this DemandLog is related to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  The detail line sequence from the DemandDetail or DemandSchedule record this DemandLog is related to.  If this value is zero, the record is related to DemandHead.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  The demand schedule sequence from the DemandSchedule record this DemandLog is related to.  If this and DemandDetailSeq are zero, this record is related to DemandHead.  If this field is zero but DemandDetailSeq is not, this record is related to DemandDetail.  Otherwise this record is related to DemandSchedule.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique identifier for the error log record.  The value is obtained from the DemandLogSeq sequence.  """  
      self.SysDate:str = obj["SysDate"]
      """  The system date the record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.LogText:str = obj["LogText"]
      """  The warning or error text.  """  
      self.Action:str = obj["Action"]
      """  The action that was taken when the demand log entry was created. The valid values are ?Stop? and ?Warning?  """  
      self.LogCode:str = obj["LogCode"]
      """  Code for the Log Action.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  """  
      self.DemandContract:str = obj["DemandContract"]
      self.DispSysTime:str = obj["DispSysTime"]
      self.Code:str = obj["Code"]
      """  Error Code needed for TaskMonitor app in the Workflows of Service Connect.  """  
      self.POnum:str = obj["POnum"]
      """  PO number, The value is obtained from demand Head POnum  """  
      self.CurrentSchNumber:str = obj["CurrentSchNumber"]
      """  Current Schedule Number - get it from demandhead  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandLogListTableset:
   def __init__(self, obj):
      self.DemandLogList:list[Erp_Tablesets_DemandLogListRow] = obj["DemandLogList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DemandLogRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The Demand Contract this record is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead, DemandDetail, or DemandSchedule record this DemandLog is related to.  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  The detail line sequence from the DemandDetail or DemandSchedule record this DemandLog is related to.  If this value is zero, the record is related to DemandHead.  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  The demand schedule sequence from the DemandSchedule record this DemandLog is related to.  If this and DemandDetailSeq are zero, this record is related to DemandHead.  If this field is zero but DemandDetailSeq is not, this record is related to DemandDetail.  Otherwise this record is related to DemandSchedule.  """  
      self.TranNum:int = obj["TranNum"]
      """  Unique identifier for the error log record.  The value is obtained from the DemandLogSeq sequence.  """  
      self.SysDate:str = obj["SysDate"]
      """  The system date the record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.LogText:str = obj["LogText"]
      """  The warning or error text.  """  
      self.Action:str = obj["Action"]
      """  The action that was taken when the demand log entry was created. The valid values are ?Stop? and ?Warning?  """  
      self.LogCode:str = obj["LogCode"]
      """  Code for the Log Action.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  An internal identifier to group demand schedules together.  """  
      self.DemandContract:str = obj["DemandContract"]
      self.DispSysTime:str = obj["DispSysTime"]
      self.Code:str = obj["Code"]
      """  Error Code needed for TaskMonitor app in the Workflows of Service Connect.  """  
      self.POnum:str = obj["POnum"]
      """  PO number, The value is obtained from demand Head POnum  """  
      self.CurrentSchNumber:str = obj["CurrentSchNumber"]
      """  Current Schedule Number - get it from demandhead  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandLogTableset:
   def __init__(self, obj):
      self.DemandLog:list[Erp_Tablesets_DemandLogRow] = obj["DemandLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtDemandLogTableset:
   def __init__(self, obj):
      self.DemandLog:list[Erp_Tablesets_DemandLogRow] = obj["DemandLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   tranNum
   sysDate
   sysTime
   """  
   def __init__(self, obj):
      self.tranNum:int = obj["tranNum"]
      self.sysDate:str = obj["sysDate"]
      self.sysTime:int = obj["sysTime"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandLogTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandLogTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandLogTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandLogListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDemandLog_input:
   """ Required : 
   ds
   tranNum
   sysDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandLogTableset] = obj["ds"]
      self.tranNum:int = obj["tranNum"]
      self.sysDate:str = obj["sysDate"]
      pass

class GetNewDemandLog_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandLogTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDemandLog
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDemandLog:str = obj["whereClauseDemandLog"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandLogTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtDemandLogTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDemandLogTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandLogTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandLogTableset] = obj["ds"]
      pass

      """  output parameters  """  

