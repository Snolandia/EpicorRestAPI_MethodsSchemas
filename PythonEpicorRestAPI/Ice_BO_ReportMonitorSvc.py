import asyncio
import aiohttp
import configEpicorSchemas



# Title: Ice.BO.ReportMonitorSvc
# Description: The report monitor service used by System Monitor.
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_ReportMonitors(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get ReportMonitors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReportMonitors
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysRptLstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/ReportMonitors",headers=creds) as resp:
           return await resp.json()

async def post_ReportMonitors(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReportMonitors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.SysRptLstRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Ice.Tablesets.SysRptLstRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/ReportMonitors", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_ReportMonitors_WorkStationID_Company_CreatedOn_RecSeq(WorkStationID, Company, CreatedOn, RecSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the ReportMonitor item
   Description: Calls GetByID to retrieve the ReportMonitor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportMonitor
      :param WorkStationID: Desc: WorkStationID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CreatedOn: Desc: CreatedOn   Required: True   Allow empty value : True
      :param RecSeq: Desc: RecSeq   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Ice.Tablesets.SysRptLstRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/ReportMonitors(" + WorkStationID + "," + Company + "," + CreatedOn + "," + RecSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_ReportMonitors_WorkStationID_Company_CreatedOn_RecSeq(WorkStationID, Company, CreatedOn, RecSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update ReportMonitor for the service
   Description: Calls UpdateExt to update ReportMonitor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReportMonitor
      :param WorkStationID: Desc: WorkStationID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CreatedOn: Desc: CreatedOn   Required: True   Allow empty value : True
      :param RecSeq: Desc: RecSeq   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Ice.Tablesets.SysRptLstRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/ReportMonitors(" + WorkStationID + "," + Company + "," + CreatedOn + "," + RecSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_ReportMonitors_WorkStationID_Company_CreatedOn_RecSeq(WorkStationID, Company, CreatedOn, RecSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete ReportMonitor item
   Description: Call UpdateExt to delete ReportMonitor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReportMonitor
      :param WorkStationID: Desc: WorkStationID   Required: True   Allow empty value : True
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param CreatedOn: Desc: CreatedOn   Required: True   Allow empty value : True
      :param RecSeq: Desc: RecSeq   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/ReportMonitors(" + WorkStationID + "," + Company + "," + CreatedOn + "," + RecSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.SysRptLstListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseSysRptLst, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseSysRptLst=" + whereClauseSysRptLst
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(workStationID, company, createdOn, recSeq, epicorHeaders = None):
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
   params += "workStationID=" + workStationID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "company=" + company
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "createdOn=" + createdOn
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "recSeq=" + recSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetReportData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReportData
   Description: Get a report's data from the server
   OperationID: GetReportData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportDefinition(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReportDefinition
   Description: Get a report's data from the server
   OperationID: GetReportDefinition
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportDefinition_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportDefinition_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsKeepIdleTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsKeepIdleTime
   Description: This method reverts the last used time so that we don't prevent
time-out from working. After that call base GetRows.
   OperationID: GetRowsKeepIdleTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsKeepIdleTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsKeepIdleTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsKeepIdleTimeWithBallonInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsKeepIdleTimeWithBallonInfo
   Description: Retrieves rows along with balloon data.
   OperationID: GetRowsKeepIdleTimeWithBallonInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsKeepIdleTimeWithBallonInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsKeepIdleTimeWithBallonInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportBytes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReportBytes
   Description: Gets the report bytes.
   OperationID: GetReportBytes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportBytes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportBytes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDataExportBytes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDataExportBytes
   Description: Gets the bytes of exported data.
   OperationID: GetDataExportBytes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDataExportBytes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataExportBytes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReportBytesAsExcel(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReportBytesAsExcel
   Description: Gets the Financial report in Excel format as bytes.
   OperationID: GetReportBytesAsExcel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReportBytesAsExcel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportBytesAsExcel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSysRptLst(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSysRptLst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSysRptLst
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSysRptLst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSysRptLst_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Ice.BO.ReportMonitorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysRptLstListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysRptLstListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_SysRptLstRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Ice_Tablesets_SysRptLstRow] = obj["value"]
      pass

class Ice_Tablesets_SysRptLstListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.RecSeq:int = obj["RecSeq"]
      """  Record Sequence  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Description  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.HostComputer:str = obj["HostComputer"]
      """  Name of Computer on which the file is located.  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.RptStatus:str = obj["RptStatus"]
      """  Pending, Printing, Printed  """  
      self.LastActionOn:str = obj["LastActionOn"]
      """  LastActionOn  """  
      self.LastAction:str = obj["LastAction"]
      """  Last Action  """  
      self.OutPutToPrinter:str = obj["OutPutToPrinter"]
      """  Name of Printer to use for Auto Print reports  """  
      self.AutoAction:str = obj["AutoAction"]
      """  Print, Preview, None  """  
      self.PrintDriver:str = obj["PrintDriver"]
      """  Program which calls the print program  """  
      self.PrintProgram:str = obj["PrintProgram"]
      """  Program which performs the actual printing  """  
      self.PrinterName:str = obj["PrinterName"]
      """  Name of "client" printer, used for auto print  """  
      self.PrintProgramOptions:str = obj["PrintProgramOptions"]
      """  additonal options/settings required by specfic PrintProgram  """  
      self.RptPageSettings:str = obj["RptPageSettings"]
      """  Report Page Settings  """  
      self.RptPrinterSettings:str = obj["RptPrinterSettings"]
      """  Report Printer Settings  """  
      self.RptVersion:str = obj["RptVersion"]
      """  Report Version  """  
      self.RptOutPutType:str = obj["RptOutPutType"]
      """  Report Output Type  """  
      self.WorkStationID:str = obj["WorkStationID"]
      """  name of computer/workstation that made the request for this report.  """  
      self.RptNote:str = obj["RptNote"]
      """  An optional descriptive note about this Report.  This value comes from the report parameter TaskNote field.  """  
      self.Archived:bool = obj["Archived"]
      """  Indicates that this Report has been Archived.  """  
      self.PurgeDate:str = obj["PurgeDate"]
      """  Date that this Report will be purged.  """  
      self.TxtLPP:int = obj["TxtLPP"]
      """  Number of lines per page for the specific text report. This was obtained from the XBSyst.TxtLPP..  """  
      self.FaxSubject:str = obj["FaxSubject"]
      """  Fax Subject  """  
      self.FaxTo:str = obj["FaxTo"]
      """  Fax To  """  
      self.FaxNumber:str = obj["FaxNumber"]
      """  Fax Number  """  
      self.EMailTo:str = obj["EMailTo"]
      """  Email To Address  """  
      self.EMailCC:str = obj["EMailCC"]
      """  Email  to CC  """  
      self.EMailBCC:str = obj["EMailBCC"]
      """  Email To BCC  """  
      self.SSRSURL:str = obj["SSRSURL"]
      """  SSRS URL  """  
      self.OutputEDI:str = obj["OutputEDI"]
      """  Field to save if file is going to be exported in txt o xml format  """  
      self.EMailBody:str = obj["EMailBody"]
      """  Email Body text  """  
      self.AttachmentType:str = obj["AttachmentType"]
      """  Attachment Type  """  
      self.SSRSRenderFormat:str = obj["SSRSRenderFormat"]
      """  SSRSRenderFormat  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysRptLstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.RecSeq:int = obj["RecSeq"]
      """  Record Sequence  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Description  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.HostComputer:str = obj["HostComputer"]
      """  Name of Computer on which the file is located.  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.RptStatus:str = obj["RptStatus"]
      """  Pending, Printing, Printed  """  
      self.LastActionOn:str = obj["LastActionOn"]
      """  LastActionOn  """  
      self.LastAction:str = obj["LastAction"]
      """  Last Action  """  
      self.OutPutToPrinter:str = obj["OutPutToPrinter"]
      """  Name of Printer to use for Auto Print reports  """  
      self.AutoAction:str = obj["AutoAction"]
      """  Print, Preview, None  """  
      self.PrintDriver:str = obj["PrintDriver"]
      """  Program which calls the print program  """  
      self.PrintProgram:str = obj["PrintProgram"]
      """  Program which performs the actual printing  """  
      self.PrinterName:str = obj["PrinterName"]
      """  Name of "client" printer, used for auto print  """  
      self.PrintProgramOptions:str = obj["PrintProgramOptions"]
      """  additonal options/settings required by specfic PrintProgram  """  
      self.RptPageSettings:str = obj["RptPageSettings"]
      """  Report Page Settings  """  
      self.RptPrinterSettings:str = obj["RptPrinterSettings"]
      """  Report Printer Settings  """  
      self.RptVersion:str = obj["RptVersion"]
      """  Report Version  """  
      self.RptOutPutType:str = obj["RptOutPutType"]
      """  Report Output Type  """  
      self.WorkStationID:str = obj["WorkStationID"]
      """  name of computer/workstation that made the request for this report.  """  
      self.RptNote:str = obj["RptNote"]
      """  An optional descriptive note about this Report.  This value comes from the report parameter TaskNote field.  """  
      self.Archived:bool = obj["Archived"]
      """  Indicates that this Report has been Archived.  """  
      self.PurgeDate:str = obj["PurgeDate"]
      """  Date that this Report will be purged.  """  
      self.TxtLPP:int = obj["TxtLPP"]
      """  Number of lines per page for the specific text report. This was obtained from the XBSyst.TxtLPP..  """  
      self.FaxSubject:str = obj["FaxSubject"]
      """  Fax Subject  """  
      self.FaxTo:str = obj["FaxTo"]
      """  Fax To  """  
      self.FaxNumber:str = obj["FaxNumber"]
      """  Fax Number  """  
      self.EMailTo:str = obj["EMailTo"]
      """  Email To Address  """  
      self.EMailCC:str = obj["EMailCC"]
      """  Email  to CC  """  
      self.EMailBCC:str = obj["EMailBCC"]
      """  Email To BCC  """  
      self.SSRSURL:str = obj["SSRSURL"]
      """  SSRS URL  """  
      self.OutputEDI:str = obj["OutputEDI"]
      """  Field to save if file is going to be exported in txt o xml format  """  
      self.EMailBody:str = obj["EMailBody"]
      """  Email Body text  """  
      self.AttachmentType:str = obj["AttachmentType"]
      """  Attachment Type  """  
      self.SSRSRenderFormat:str = obj["SSRSRenderFormat"]
      """  SSRSRenderFormat  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  StyleNum  """  
      self.UserDescription:str = obj["UserDescription"]
      """  UserDescription  """  
      self.DesignMode:str = obj["DesignMode"]
      """  DesignMode  """  
      self.DesignUser:str = obj["DesignUser"]
      """  DesignUser  """  
      self.DesignVersionLocalFolder:str = obj["DesignVersionLocalFolder"]
      """  DesignVersionLocalFolder  """  
      self.StyleDescription:str = obj["StyleDescription"]
      """  StyleDescription  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   workStationID
   company
   createdOn
   recSeq
   """  
   def __init__(self, obj):
      self.workStationID:str = obj["workStationID"]
      self.company:str = obj["company"]
      self.createdOn:str = obj["createdOn"]
      self.recSeq:int = obj["recSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class GetByID_input:
   """ Required : 
   workStationID
   company
   createdOn
   recSeq
   """  
   def __init__(self, obj):
      self.workStationID:str = obj["workStationID"]
      self.company:str = obj["company"]
      self.createdOn:str = obj["createdOn"]
      self.recSeq:int = obj["recSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ReportMonitorTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ReportMonitorTableset] = obj["returnObj"]
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
      self.returnObj:list[Ice_Tablesets_ReportMonitorTableset] = obj["returnObj"]
      pass

class GetDataExportBytes_input:
   """ Required : 
   sysRowId
   """  
   def __init__(self, obj):
      self.sysRowId:str = obj["sysRowId"]
      """  The system row identifier.  """  
      pass

class GetDataExportBytes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The bytes of the exported data.  """  
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
      self.returnObj:list[Ice_Tablesets_SysRptLstListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewSysRptLst_input:
   """ Required : 
   ds
   workStationID
   company
   createdOn
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ReportMonitorTableset] = obj["ds"]
      self.workStationID:str = obj["workStationID"]
      self.company:str = obj["company"]
      self.createdOn:str = obj["createdOn"]
      pass

class GetNewSysRptLst_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ReportMonitorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetReportBytesAsExcel_input:
   """ Required : 
   sysRowId
   currencyInfoList
   """  
   def __init__(self, obj):
      self.sysRowId:str = obj["sysRowId"]
      """  The system row identifier  """  
      self.currencyInfoList      #schema had no properties on an object.
      """  List of currency code and DecimalsGeneral value for current company  """  
      pass

class GetReportBytesAsExcel_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The bytes for the rendered report in excel format  """  
      pass

class GetReportBytes_input:
   """ Required : 
   sysRowId
   """  
   def __init__(self, obj):
      self.sysRowId:str = obj["sysRowId"]
      """  The system row identifier.  """  
      pass

class GetReportBytes_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The bytes for the rendered report.  """  
      pass

class GetReportData_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      """  The row ID of the report to get the data for  """  
      pass

class GetReportData_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ReportDataTableset] = obj["returnObj"]
      pass

class GetReportDefinition_input:
   """ Required : 
   sysRowID
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      """  The row ID of the report to get the data for  """  
      pass

class GetReportDefinition_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ReportDataTableset] = obj["returnObj"]
      pass

class GetRowsKeepIdleTimeWithBallonInfo_input:
   """ Required : 
   whereClauseSysRptLst
   getBallonInfo
   whereClauseSysTask
   whereClauseSysTaskLog
   sysMonitorData
   """  
   def __init__(self, obj):
      self.whereClauseSysRptLst:str = obj["whereClauseSysRptLst"]
      """  The where clause to restrict data for  """  
      self.getBallonInfo:bool = obj["getBallonInfo"]
      """  Include balloon info if true  """  
      self.whereClauseSysTask:str = obj["whereClauseSysTask"]
      self.whereClauseSysTaskLog:str = obj["whereClauseSysTaskLog"]
      self.sysMonitorData      #schema had no properties on an object.
      pass

class GetRowsKeepIdleTimeWithBallonInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ReportMonitorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.sysMonitorData: UNKNOW TYPE(error 2338) = obj["sysMonitorData"]
      pass

      """  output parameters  """  

class GetRowsKeepIdleTime_input:
   """ Required : 
   whereClauseSysRptLst
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSysRptLst:str = obj["whereClauseSysRptLst"]
      """  The where clause to restrict data for  """  
      self.pageSize:int = obj["pageSize"]
      """  The page size  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetRowsKeepIdleTime_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ReportMonitorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseSysRptLst
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseSysRptLst:str = obj["whereClauseSysRptLst"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_Tablesets_ReportMonitorTableset] = obj["returnObj"]
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

class Ice_Tablesets_ReportDataRow:
   def __init__(self, obj):
      self.Sequence:int = obj["Sequence"]
      self.Data:str = obj["Data"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_ReportDataTableset:
   def __init__(self, obj):
      self.ReportData:list[Ice_Tablesets_ReportDataRow] = obj["ReportData"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_ReportMonitorTableset:
   def __init__(self, obj):
      self.SysRptLst:list[Ice_Tablesets_SysRptLstRow] = obj["SysRptLst"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysRptLstListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.RecSeq:int = obj["RecSeq"]
      """  Record Sequence  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Description  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.HostComputer:str = obj["HostComputer"]
      """  Name of Computer on which the file is located.  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.RptStatus:str = obj["RptStatus"]
      """  Pending, Printing, Printed  """  
      self.LastActionOn:str = obj["LastActionOn"]
      """  LastActionOn  """  
      self.LastAction:str = obj["LastAction"]
      """  Last Action  """  
      self.OutPutToPrinter:str = obj["OutPutToPrinter"]
      """  Name of Printer to use for Auto Print reports  """  
      self.AutoAction:str = obj["AutoAction"]
      """  Print, Preview, None  """  
      self.PrintDriver:str = obj["PrintDriver"]
      """  Program which calls the print program  """  
      self.PrintProgram:str = obj["PrintProgram"]
      """  Program which performs the actual printing  """  
      self.PrinterName:str = obj["PrinterName"]
      """  Name of "client" printer, used for auto print  """  
      self.PrintProgramOptions:str = obj["PrintProgramOptions"]
      """  additonal options/settings required by specfic PrintProgram  """  
      self.RptPageSettings:str = obj["RptPageSettings"]
      """  Report Page Settings  """  
      self.RptPrinterSettings:str = obj["RptPrinterSettings"]
      """  Report Printer Settings  """  
      self.RptVersion:str = obj["RptVersion"]
      """  Report Version  """  
      self.RptOutPutType:str = obj["RptOutPutType"]
      """  Report Output Type  """  
      self.WorkStationID:str = obj["WorkStationID"]
      """  name of computer/workstation that made the request for this report.  """  
      self.RptNote:str = obj["RptNote"]
      """  An optional descriptive note about this Report.  This value comes from the report parameter TaskNote field.  """  
      self.Archived:bool = obj["Archived"]
      """  Indicates that this Report has been Archived.  """  
      self.PurgeDate:str = obj["PurgeDate"]
      """  Date that this Report will be purged.  """  
      self.TxtLPP:int = obj["TxtLPP"]
      """  Number of lines per page for the specific text report. This was obtained from the XBSyst.TxtLPP..  """  
      self.FaxSubject:str = obj["FaxSubject"]
      """  Fax Subject  """  
      self.FaxTo:str = obj["FaxTo"]
      """  Fax To  """  
      self.FaxNumber:str = obj["FaxNumber"]
      """  Fax Number  """  
      self.EMailTo:str = obj["EMailTo"]
      """  Email To Address  """  
      self.EMailCC:str = obj["EMailCC"]
      """  Email  to CC  """  
      self.EMailBCC:str = obj["EMailBCC"]
      """  Email To BCC  """  
      self.SSRSURL:str = obj["SSRSURL"]
      """  SSRS URL  """  
      self.OutputEDI:str = obj["OutputEDI"]
      """  Field to save if file is going to be exported in txt o xml format  """  
      self.EMailBody:str = obj["EMailBody"]
      """  Email Body text  """  
      self.AttachmentType:str = obj["AttachmentType"]
      """  Attachment Type  """  
      self.SSRSRenderFormat:str = obj["SSRSRenderFormat"]
      """  SSRSRenderFormat  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_SysRptLstListTableset:
   def __init__(self, obj):
      self.SysRptLstList:list[Ice_Tablesets_SysRptLstListRow] = obj["SysRptLstList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Tablesets_SysRptLstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.UserID:str = obj["UserID"]
      """  User ID  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.RecSeq:int = obj["RecSeq"]
      """  Record Sequence  """  
      self.RptDescription:str = obj["RptDescription"]
      """  Report Description  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  System Task Number  """  
      self.HostComputer:str = obj["HostComputer"]
      """  Name of Computer on which the file is located.  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.RptStatus:str = obj["RptStatus"]
      """  Pending, Printing, Printed  """  
      self.LastActionOn:str = obj["LastActionOn"]
      """  LastActionOn  """  
      self.LastAction:str = obj["LastAction"]
      """  Last Action  """  
      self.OutPutToPrinter:str = obj["OutPutToPrinter"]
      """  Name of Printer to use for Auto Print reports  """  
      self.AutoAction:str = obj["AutoAction"]
      """  Print, Preview, None  """  
      self.PrintDriver:str = obj["PrintDriver"]
      """  Program which calls the print program  """  
      self.PrintProgram:str = obj["PrintProgram"]
      """  Program which performs the actual printing  """  
      self.PrinterName:str = obj["PrinterName"]
      """  Name of "client" printer, used for auto print  """  
      self.PrintProgramOptions:str = obj["PrintProgramOptions"]
      """  additonal options/settings required by specfic PrintProgram  """  
      self.RptPageSettings:str = obj["RptPageSettings"]
      """  Report Page Settings  """  
      self.RptPrinterSettings:str = obj["RptPrinterSettings"]
      """  Report Printer Settings  """  
      self.RptVersion:str = obj["RptVersion"]
      """  Report Version  """  
      self.RptOutPutType:str = obj["RptOutPutType"]
      """  Report Output Type  """  
      self.WorkStationID:str = obj["WorkStationID"]
      """  name of computer/workstation that made the request for this report.  """  
      self.RptNote:str = obj["RptNote"]
      """  An optional descriptive note about this Report.  This value comes from the report parameter TaskNote field.  """  
      self.Archived:bool = obj["Archived"]
      """  Indicates that this Report has been Archived.  """  
      self.PurgeDate:str = obj["PurgeDate"]
      """  Date that this Report will be purged.  """  
      self.TxtLPP:int = obj["TxtLPP"]
      """  Number of lines per page for the specific text report. This was obtained from the XBSyst.TxtLPP..  """  
      self.FaxSubject:str = obj["FaxSubject"]
      """  Fax Subject  """  
      self.FaxTo:str = obj["FaxTo"]
      """  Fax To  """  
      self.FaxNumber:str = obj["FaxNumber"]
      """  Fax Number  """  
      self.EMailTo:str = obj["EMailTo"]
      """  Email To Address  """  
      self.EMailCC:str = obj["EMailCC"]
      """  Email  to CC  """  
      self.EMailBCC:str = obj["EMailBCC"]
      """  Email To BCC  """  
      self.SSRSURL:str = obj["SSRSURL"]
      """  SSRS URL  """  
      self.OutputEDI:str = obj["OutputEDI"]
      """  Field to save if file is going to be exported in txt o xml format  """  
      self.EMailBody:str = obj["EMailBody"]
      """  Email Body text  """  
      self.AttachmentType:str = obj["AttachmentType"]
      """  Attachment Type  """  
      self.SSRSRenderFormat:str = obj["SSRSRenderFormat"]
      """  SSRSRenderFormat  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReportID:str = obj["ReportID"]
      """  ReportID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  StyleNum  """  
      self.UserDescription:str = obj["UserDescription"]
      """  UserDescription  """  
      self.DesignMode:str = obj["DesignMode"]
      """  DesignMode  """  
      self.DesignUser:str = obj["DesignUser"]
      """  DesignUser  """  
      self.DesignVersionLocalFolder:str = obj["DesignVersionLocalFolder"]
      """  DesignVersionLocalFolder  """  
      self.StyleDescription:str = obj["StyleDescription"]
      """  StyleDescription  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_Tablesets_UpdExtReportMonitorTableset:
   def __init__(self, obj):
      self.SysRptLst:list[Ice_Tablesets_SysRptLstRow] = obj["SysRptLst"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtReportMonitorTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_UpdExtReportMonitorTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Ice_Tablesets_ReportMonitorTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Ice_Tablesets_ReportMonitorTableset] = obj["ds"]
      pass

      """  output parameters  """  

