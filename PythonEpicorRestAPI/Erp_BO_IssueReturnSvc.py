import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IssueReturnSvc
# Description: Use this function to enter inventory issues or returns.
1) [Hold] Special public methods for DDSLs FromWhse and ToWhse as they have special conditions.
2) [ FYI ]This procedure gets called from lots of other program too -
im/ime20.w flmenu.w am/ame10.w am/ame20-am.p am/ame20-aw.p am/ame20-mm.p am/ame20-mw.p
Only am/ame20-dg.w uses MtlQueue functionality
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IssueReturnJobAsmblRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseJobHead, whereClauseJobAsmbl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: List of jobs that can be selected for Mass Issue.
   OperationID: Get_GetRows
      :param whereClauseJobHead: Desc: Where condition without the where word   Required: True   Allow empty value : True
      :param whereClauseJobAsmbl: Desc: Where condition without the where word   Required: True   Allow empty value : True
      :param pageSize: Desc: # of records returned.  0 means all   Required: True
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
   params += "whereClauseJobHead=" + whereClauseJobHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseJobAsmbl=" + whereClauseJobAsmbl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_History07_08(epicorHeaders = None):
   """  
   Summary: Invoke method _History07_08
   OperationID: _History07_08
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/_History07_08_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List",headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClauseJobHead, whereClauseJobAsmbl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: List of jobs that can be selected for Mass Issue.
   OperationID: Get_GetList
      :param whereClauseJobHead: Desc: Where condition without the where word   Required: True   Allow empty value : True
      :param whereClauseJobAsmbl: Desc: Where condition without the where word   Required: True   Allow empty value : True
      :param pageSize: Desc: # of records returned.  0 means all   Required: True
   Required: True
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
   params += "whereClauseJobHead=" + whereClauseJobHead
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseJobAsmbl=" + whereClauseJobAsmbl
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetListJobs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetListJobs
   Description: List of jobs that can be selected for Mass Issue.
   OperationID: GetListJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetListJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIssueReturn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIssueReturn
   Description: Call this method to create a new Epicor.Mfg.BO.IssueReturnDataSet with
default values.
   OperationID: GetNewIssueReturn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIssueReturn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIssueReturn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIssueReturnFromJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIssueReturnFromJob
   Description: Call this method to create a new Epicor.Mfg.BO.IssueReturnDataSet with
default values.
   OperationID: GetNewIssueReturnFromJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIssueReturnFromJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIssueReturnFromJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewIssueReturnToJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewIssueReturnToJob
   Description: Call this method to create a new Epicor.Mfg.BO.IssueReturnDataSet with
default values.
   OperationID: GetNewIssueReturnToJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewIssueReturnToJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewIssueReturnToJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobAsmblMultiple(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobAsmblMultiple
   Description: This method creates multiple IssueReturnJobs rows using IssueReturnJobSearch dataset.
   OperationID: GetNewJobAsmblMultiple
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobAsmblMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobAsmblMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobAsmblSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobAsmblSearch
   Description: This method creates a new ttSelectedJobAsmbl row entry.
   OperationID: GetNewJobAsmblSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewJobAsmblSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJobAsmblSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartMultiple(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartMultiple
   Description: This method creates multiple IssueReturnJobs rows using IssueReturnJobSearch dataset.
   OperationID: GetNewPartMultiple
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartNum
   Description: Call this method to create a new Epicor.Mfg.BO.IssueReturnDataSet with
Part#.
   OperationID: GetNewPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartSearch
   Description: This method creates a new ttSelectedParts row entry.
   OperationID: GetNewPartSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsJobAssemblies(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsJobAssemblies
   Description: List of jobs/assemblies that can be selected for Mass Issue.
   OperationID: Get_GetRowsJobAssemblies
      :param whereClause: Desc: Where condition without the where word   Required: True   Allow empty value : True
      :param pageSize: Desc: # of records returned.  0 means all   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsJobAssemblies_output
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetRowsWIP(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsWIP
   Description: List of jobs/assemblies that can be selected for Move WIP and Move Material.
   OperationID: Get_GetRowsWIP
      :param whereClause: Desc: Where condition without the where word   Required: True   Allow empty value : True
      :param pageSize: Desc: # of records returned.   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWIP_output
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUnissuedQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUnissuedQty
   Description: Call this method to set the Qty to the remaining unissued amount.
   OperationID: GetUnissuedQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUnissuedQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUnissuedQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetUnpickSettings(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetUnpickSettings
   Description: Sets ttIssueReturn fields for Unpick
   OperationID: GetUnpickSettings
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetUnpickSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetUnpickSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsValidAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsValidAssembly
   Description: Validate if an assembly is valid for a job. if not returns false,
otherwise returns true.
   OperationID: IsValidAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsValidAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsValidAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromPCID
   Description: Validate if FromPCID change is valid
otherwise returns true.
   OperationID: OnChangeFromPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_JobExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method JobExists
   Description: Check JobNum and return JobRelease and JobClosed
   OperationID: JobExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/JobExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/JobExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeToPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeToPCID
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.ToPCID changes (this is for ToPCID, for FromPCID use OnChangeFromPCID method).
   OperationID: OnChangeToPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromAssemblySeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromAssemblySeq
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.FromAssemblySeq changes.
   OperationID: OnChangeFromAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromBinNum
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.FromBinNum changes.
   OperationID: OnChangeFromBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromJobNum
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.FromJobNum changes.
   OperationID: OnChangeFromJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromJobSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromJobSeq
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.FromJobNum changes.
   OperationID: OnChangeFromJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromWarehouse
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.PartNum changes.
   OperationID: OnChangeFromWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFromWarehouseDefaultBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromWarehouseDefaultBin
   Description: Call when from warehouse changes.  This method will also reset the bin to the default value for the warehouse
   OperationID: ChangeFromWarehouseDefaultBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromWarehouseDefaultBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromWarehouseDefaultBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLotNum
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.LotNum changes.
   OperationID: OnChangeLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.PartNum changes.
   OperationID: OnChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeToAssemblySeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeToAssemblySeq
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.ToAssemblySeq changes.
   OperationID: OnChangeToAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeToJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeToJobNum
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.ToJobNum changes.
   OperationID: OnChangeToJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeToJobSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeToJobSeq
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.ToJobSeq changes.
   OperationID: OnChangeToJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeToWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeToWarehouse
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.PartNum changes.
   OperationID: OnChangeToWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToWarehouseDefaultBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToWarehouseDefaultBin
   Description: Call when to warehouse changes.  This method will also reset the bin to the default value for the warehouse
   OperationID: ChangeToWarehouseDefaultBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToWarehouseDefaultBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToWarehouseDefaultBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: OnChangingNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAttributeSetAdjustments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAttributeSetAdjustments
   Description: Call this method when the attribute set changes for adjustment transactions (Issue Misc, Return Misc) to maintain inventory tracking
   OperationID: OnChangingAttributeSetAdjustments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSetAdjustments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSetAdjustments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRevisionNumAdjustments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRevisionNumAdjustments
   Description: Call this method when the Revision changes for adjustment transactions (Issue Misc, Return Misc) to maintain inventory tracking
   OperationID: OnChangingRevisionNumAdjustments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNumAdjustments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNumAdjustments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTranQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTranQty
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.TranQty changes.
This method performs validation on TranQty and sets the Issued Complete flag.
   OperationID: OnChangeTranQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeTranQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUM
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.UM changes.
   OperationID: OnChangeUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeASTUom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeASTUom
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.FromBinNum is changing.
   OperationID: OnChangeASTUom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeASTUom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeASTUom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingFromBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingFromBinNum
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.FromBinNum is changing.
   OperationID: OnChangingFromBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingFromBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingFromBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingJobSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingJobSeq
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSetjobseq (either to or from is changing)
   OperationID: OnChangingJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingToJobSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingToJobSeq
   Description: Call this method when the value of Epicor.Mfg.BO.IssueReturnDataSet.ToJobSeq is changing.
   OperationID: OnChangingToJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingToJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingToJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PerformMaterialMovement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PerformMaterialMovement
   Description: Perform Material Movement.
   OperationID: PerformMaterialMovement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PerformMaterialMovement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformMaterialMovement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PerformMaterialMovement2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PerformMaterialMovement2
   Description: Perform Material Movement.
   OperationID: PerformMaterialMovement2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PerformMaterialMovement2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformMaterialMovement2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PerformMaterialMovementWithLegalNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PerformMaterialMovementWithLegalNum
   Description: Perform Material Movement.
   OperationID: PerformMaterialMovementWithLegalNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PerformMaterialMovementWithLegalNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PerformMaterialMovementWithLegalNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MassUnpickByPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MassUnpickByPCID
   Description: Performs a mass unpick by PCID - this handles the actual inventory movement - everything else is handled by UnpickTransaction BO
   OperationID: MassUnpickByPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MassUnpickByPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MassUnpickByPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateDynamicPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateDynamicPCID
   Description: Generate a dynamic PCID
   OperationID: GenerateDynamicPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateDynamicPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateDynamicPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SuppressPrintMessages(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SuppressPrintMessages
   Description: Returns if the employee has the 'Suppress Print Messages' flag on
   OperationID: SuppressPrintMessages
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SuppressPrintMessages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SuppressPrintMessages_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsAutoPrintSetup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsAutoPrintSetup
   Description: To verify if autoprint is setup
   OperationID: IsAutoPrintSetup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsAutoPrintSetup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAutoPrintSetup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePkgControlID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePkgControlID
   Description: Validates a pkg control ID code
   OperationID: ValidatePkgControlID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePkgControlID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePkgControlID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreGetNewIssueReturn(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreGetNewIssueReturn
   Description: This method will check, depending on the Tran Type, if the available quantity
has been reduced before the creation of the issue return.
   OperationID: PreGetNewIssueReturn
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreGetNewIssueReturn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreGetNewIssueReturn_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrePerformMaterialMovement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrePerformMaterialMovement
   Description: This method performs multiple functions:
It will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
            
It will also auto populate ttSelectedSerialNumbers table under some conditions for eligible types of IR transactions
   OperationID: PrePerformMaterialMovement
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrePerformMaterialMovement_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePerformMaterialMovement_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetQuantity(epicorHeaders = None):
   """  
   Summary: Invoke method SetQuantity
   Description: Purpose:  Gets the PartWip
sets the "From quantity" (ttIssueReturn.QtyPrevioulsyIssued)
and "TO Quantity" (ttIssueReturn.TranQty) to the PartWip.
Notes:This is called when the from fields are changed. (FromJobNum, FromAssemblySeq, FromJobSeq, FromWarehouseCode, FromBinNum)
Currently this is only for a WIP-WIP transaction
Created as part of scr57730
   OperationID: SetQuantity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_validateToBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method validateToBinNum
   Description: Validates To Location, Bin Number exists
   OperationID: validateToBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/validateToBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/validateToBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryQtyAdjBrw(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryQtyAdjBrw
   Description: Gets the default values for the browse section of the adjustment screen
   OperationID: GetInventoryQtyAdjBrw
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrw_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrw_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryQtyAdjBrwInventoryTracking(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryQtyAdjBrwInventoryTracking
   Description: Gets the default values for the browse section of the adjustment screen
   OperationID: GetInventoryQtyAdjBrwInventoryTracking
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrwInventoryTracking_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrwInventoryTracking_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryQtyAdjBrwForWeb(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryQtyAdjBrwForWeb
   Description: Gets the default values for the browse section of the adjustment screen
Copy of the same method of BO InventoryQtyAdj
Specific for web (client) use.
   OperationID: GetInventoryQtyAdjBrwForWeb
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrwForWeb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrwForWeb_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartXRefInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidUOM
   OperationID: ValidUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Method to call to get available tran doc types.
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_NegativeInventoryTestTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NegativeInventoryTestTran
   OperationID: NegativeInventoryTestTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NegativeInventoryTestTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryTestTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NegativeInventoryTest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NegativeInventoryTest
   OperationID: NegativeInventoryTest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/NegativeInventoryTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MasterInventoryBinTests(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MasterInventoryBinTests
   Description: Methods to check Negative Inventory and Contract bin.
Planning Contract Bin Actions.
   OperationID: MasterInventoryBinTests
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MasterInventoryBinTests_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MasterInventoryBinTests_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_checkWhseBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method checkWhseBin
   Description: Method to check values for whsebin.
   OperationID: checkWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/checkWhseBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/checkWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FillForeignFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FillForeignFields
   OperationID: FillForeignFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FillForeignFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FillForeignFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackageCodeAllocNegQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackageCodeAllocNegQty
   OperationID: CheckPackageCodeAllocNegQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPackageCodeAllocNegQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPackageCodeAllocNegQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AreSNumsAllocated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AreSNumsAllocated
   Description: Returns true if there are any PartAllocSerial records for the company/part, consistent with InvTransfer.
   OperationID: AreSNumsAllocated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AreSNumsAllocated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AreSNumsAllocated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetToBinNumWhereClause(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetToBinNumWhereClause
   Description: Returns a whereclause for To Bin Num searches
   OperationID: GetToBinNumWhereClause
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetToBinNumWhereClause_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetToBinNumWhereClause_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IssueReturnSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IssueReturnJobAsmblRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_IssueReturnJobAsmblRow] = obj["value"]
      pass

class Erp_Tablesets_IssueReturnJobAsmblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.PartNum:str = obj["PartNum"]
      self.Description:str = obj["Description"]
      self.JobHeadPartNum:str = obj["JobHeadPartNum"]
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      self.EquipID:str = obj["EquipID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AreSNumsAllocated_input:
   """ Required : 
   companyID
   partNum
   """  
   def __init__(self, obj):
      self.companyID:str = obj["companyID"]
      self.partNum:str = obj["partNum"]
      pass

class AreSNumsAllocated_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ChangeFromWarehouseDefaultBin_input:
   """ Required : 
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      pass

class ChangeFromWarehouseDefaultBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToWarehouseDefaultBin_input:
   """ Required : 
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      pass

class ChangeToWarehouseDefaultBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPackageCodeAllocNegQty_input:
   """ Required : 
   ipcalledFrom
   ipPCID
   ipQty
   """  
   def __init__(self, obj):
      self.ipcalledFrom:str = obj["ipcalledFrom"]
      self.ipPCID:str = obj["ipPCID"]
      self.ipQty:int = obj["ipQty"]
      pass

class CheckPackageCodeAllocNegQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opWarning:str = obj["parameters"]
      self.opAction:str = obj["parameters"]
      self.opAllocWarning:str = obj["parameters"]
      self.opAllocAction:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_InventoryQtyAdjBrwRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.BinNum:str = obj["BinNum"]
      """  Bin number  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  On hand quantity  """  
      self.NonNettable:bool = obj["NonNettable"]
      """  Non nettable flag  """  
      self.WareHseCode:str = obj["WareHseCode"]
      """  Ware house code  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot number  """  
      self.WhseBinDesc:str = obj["WhseBinDesc"]
      """  WareHouse Bin description.  """  
      self.StkUOMCode:str = obj["StkUOMCode"]
      self.StkUOMDesc:str = obj["StkUOMDesc"]
      self.BaseOnHandQty:int = obj["BaseOnHandQty"]
      """  The PartBin.OnHandQty expressed in Part Base UOM  """  
      self.BaseOnHandUOM:str = obj["BaseOnHandUOM"]
      """  Unit of Measure to qualifiy BaseOnHandQty. This is the Part Base UOM.  """  
      self.BinType:str = obj["BinType"]
      self.BinTypeDesc:str = obj["BinTypeDesc"]
      """  Translated description string of Bin Type  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Part Bin has to be synchronized with Epicor FSA application.  """  
      self.PCID:str = obj["PCID"]
      """  The parent PCID for the bin or child PCID record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum for the bin record.  """  
      self.ItemPCID:str = obj["ItemPCID"]
      """  The PCID of the child in the parent PCID.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InventoryQtyAdjBrwTableset:
   def __init__(self, obj):
      self.InventoryQtyAdjBrw:list[Erp_Tablesets_InventoryQtyAdjBrwRow] = obj["InventoryQtyAdjBrw"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IssueReturnJobAsmblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.PartNum:str = obj["PartNum"]
      self.Description:str = obj["Description"]
      self.JobHeadPartNum:str = obj["JobHeadPartNum"]
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      self.EquipID:str = obj["EquipID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IssueReturnJobAsmblTableset:
   def __init__(self, obj):
      self.IssueReturnJobAsmbl:list[Erp_Tablesets_IssueReturnJobAsmblRow] = obj["IssueReturnJobAsmbl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IssueReturnJobListTableset:
   def __init__(self, obj):
      self.JobHead:list[Erp_Tablesets_JobHeadRow] = obj["JobHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IssueReturnRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company identifier  """  
      self.TranDate:str = obj["TranDate"]
      """  Transaction Date  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number  """  
      self.TranQty:int = obj["TranQty"]
      """  Transaction Quantity  """  
      self.DimCode:str = obj["DimCode"]
      """  Dimension code  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot number  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Reason code  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order number  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Line #  """  
      self.OrderRel:int = obj["OrderRel"]
      """  Release #  """  
      self.FromJobNum:str = obj["FromJobNum"]
      """  From Job #  """  
      self.FromAssemblySeq:int = obj["FromAssemblySeq"]
      """  From Assembly Seq  """  
      self.FromJobSeq:int = obj["FromJobSeq"]
      """  From Job sequence  """  
      self.FromWarehouseCode:str = obj["FromWarehouseCode"]
      """  From Warehouse code  """  
      self.FromBinNum:str = obj["FromBinNum"]
      """  From Bin number  """  
      self.FromJobPartNum:str = obj["FromJobPartNum"]
      """  From Job Part num  """  
      self.FromAssemblyPartNum:str = obj["FromAssemblyPartNum"]
      """  From Assembly Part num  """  
      self.FromJobSeqPartNum:str = obj["FromJobSeqPartNum"]
      """  From Job sequence Part num  """  
      self.FromJobPartDesc:str = obj["FromJobPartDesc"]
      """  From Job Part Desc  """  
      self.FromAssemblyPartDesc:str = obj["FromAssemblyPartDesc"]
      """  From Assembly Part Desc  """  
      self.FromJobSeqPartDesc:str = obj["FromJobSeqPartDesc"]
      """  From Job sequence Part Desc  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  On hand quantity  """  
      self.QtyRequired:int = obj["QtyRequired"]
      """  Quantity required  """  
      self.QtyPreviouslyIssued:int = obj["QtyPreviouslyIssued"]
      """  Quantity previously required  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      """  Issued Complete  """  
      self.ToJobNum:str = obj["ToJobNum"]
      """  To Job #  """  
      self.ToAssemblySeq:int = obj["ToAssemblySeq"]
      """  To Assembly Seq  """  
      self.ToJobSeq:int = obj["ToJobSeq"]
      """  To Job sequence  """  
      self.ToWarehouseCode:str = obj["ToWarehouseCode"]
      """  To Warehouse code  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  To Bin number  """  
      self.ToJobPartNum:str = obj["ToJobPartNum"]
      """  To Job Part num  """  
      self.ToAssemblyPartNum:str = obj["ToAssemblyPartNum"]
      """  To Assembly Part num  """  
      self.ToJobSeqPartNum:str = obj["ToJobSeqPartNum"]
      """  To Job sequence Part num  """  
      self.ToJobPartDesc:str = obj["ToJobPartDesc"]
      """  To Job Part Desc  """  
      self.ToAssemblyPartDesc:str = obj["ToAssemblyPartDesc"]
      """  To Assembly Part Desc  """  
      self.ToJobSeqPartDesc:str = obj["ToJobSeqPartDesc"]
      """  To Job sequence part desc  """  
      self.ReasonType:str = obj["ReasonType"]
      self.FromJobPartDescription:str = obj["FromJobPartDescription"]
      self.FromAssemblyPartDescription:str = obj["FromAssemblyPartDescription"]
      self.FromJobSeqPartDescription:str = obj["FromJobSeqPartDescription"]
      self.ToJobPartDescription:str = obj["ToJobPartDescription"]
      self.ToAssemblyPartDescription:str = obj["ToAssemblyPartDescription"]
      self.ToJobSeqPartDescription:str = obj["ToJobSeqPartDescription"]
      self.TranReference:str = obj["TranReference"]
      self.SerialNoQty:int = obj["SerialNoQty"]
      self.MtlQueueRowId:str = obj["MtlQueueRowId"]
      self.TranType:str = obj["TranType"]
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.InvAdjReason:str = obj["InvAdjReason"]
      self.DUM:str = obj["DUM"]
      self.UM:str = obj["UM"]
      self.FromJobPlant:str = obj["FromJobPlant"]
      self.ToJobPlant:str = obj["ToJobPlant"]
      self.DummyKeyField:str = obj["DummyKeyField"]
      """  Dummy key field.  It is the primary key of the dataset  """  
      self.TreeDisplay:str = obj["TreeDisplay"]
      """  The value displayed in the JobAsmbl tree  """  
      self.EnableToFields:bool = obj["EnableToFields"]
      self.EnableFromFields:bool = obj["EnableFromFields"]
      self.RequirementUOM:str = obj["RequirementUOM"]
      self.RequirementQty:int = obj["RequirementQty"]
      self.EnableSN:bool = obj["EnableSN"]
      """  This external field would be used to indicate for the BL whether serial numbers should be validated/updated and indicated for the various UIs whether the serial number button will be enabled.  """  
      self.SerialControlPlant:str = obj["SerialControlPlant"]
      """  The plant id of the plant that is controlling the serial tracking options, set depending on the IssueReturn UI  """  
      self.SerialControlPlantIsFromPlt:bool = obj["SerialControlPlantIsFromPlt"]
      """  Indicates whether the plant in SerialControlPlant field is the from plant. Yes = is the from plant, No= is the to plant.  """  
      self.ProcessID:str = obj["ProcessID"]
      """  The process ID for the UI process that has created this IssueReturn record, only used by serial tracking logic  """  
      self.SerialControlPlant2:str = obj["SerialControlPlant2"]
      """  If SerialControlPlantIsFromPlt = yes, then this field contains the to plant for the issue or return; it will be blank for Misc Issue  """  
      self.TrackDimension:bool = obj["TrackDimension"]
      """  It is true when Multi UOM is tracked for the PartNum  """  
      self.OnHandUM:str = obj["OnHandUM"]
      """  Unit of measure of the On Hand Quantity displayed  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type ID  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      self.ReplenishDecreased:bool = obj["ReplenishDecreased"]
      self.EnablePCIDGen:bool = obj["EnablePCIDGen"]
      """  Sets whether generate button in process material queue screen is enabled.  """  
      self.EnablePCIDPrint:bool = obj["EnablePCIDPrint"]
      """  Sets whether print button in process material queue screen is enabled.  """  
      self.Plant:str = obj["Plant"]
      """  Current Plant ID - external - used for filtering combos  """  
      self.PkgControlID:str = obj["PkgControlID"]
      self.FromPCID:str = obj["FromPCID"]
      """  PCID to pick from.  """  
      self.ToPCID:str = obj["ToPCID"]
      """  PCID to pick to.  """  
      self.ToPCIDItemSeq:int = obj["ToPCIDItemSeq"]
      self.FromPCIDItemSeq:int = obj["FromPCIDItemSeq"]
      self.DisablePCIDRelatedFields:bool = obj["DisablePCIDRelatedFields"]
      """  Disable PCID related fields  """  
      self.PlantConfCtrlEnablePackageControl:bool = obj["PlantConfCtrlEnablePackageControl"]
      """  Flag in PlantConfCtrl that enables Package Control functionality.  """  
      self.EnableToPCID:bool = obj["EnableToPCID"]
      self.EnableFromPCID:bool = obj["EnableFromPCID"]
      self.PkgControlHeaderDeleted:bool = obj["PkgControlHeaderDeleted"]
      """  Indicates if a PkgControlHeader record was deleted during the Unpick Transaction.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision related to this transaction.  """  
      self.FromJobRevisionNum:str = obj["FromJobRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.FromAssemblyRevisionNum:str = obj["FromAssemblyRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.PartWipSysRowID:str = obj["PartWipSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.FromBinNumDescription:str = obj["FromBinNumDescription"]
      self.FromWarehouseCodeDescription:str = obj["FromWarehouseCodeDescription"]
      self.LotNumPartLotDescription:str = obj["LotNumPartLotDescription"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.ReasonCodeDescription:str = obj["ReasonCodeDescription"]
      self.ToBinNumDescription:str = obj["ToBinNumDescription"]
      self.ToWarehouseCodeDescription:str = obj["ToWarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IssueReturnTableset:
   def __init__(self, obj):
      self.IssueReturn:list[Erp_Tablesets_IssueReturnRow] = obj["IssueReturn"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_JobHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.JobClosed:bool = obj["JobClosed"]
      """  Indicates if Job is closed.  A closed Job cannot be accessed for maintenance.  """  
      self.ClosedDate:str = obj["ClosedDate"]
      """  Date the Job was closed.  Defaults as the system but can be overridden.  """  
      self.JobComplete:bool = obj["JobComplete"]
      """  Indicates if production is complete for the job.  A complete job cannot be scheduled.  It can still have cost posted against it.  Maintained via Job Completion processing.  """  
      self.JobCompletionDate:str = obj["JobCompletionDate"]
      """  The date that production was completed for this Job.  Maintained via Job Completion Processing.  """  
      self.JobEngineered:bool = obj["JobEngineered"]
      """  Indicates if Engineering is complete for this job.  That is, all departments that need to "check off" on this job before it is actually considered ready to go have done so.  A job must be Engineered before it  can be scheduled.  Non Engineered Jobs are excluded from most reports.  """  
      self.CheckOff1:bool = obj["CheckOff1"]
      """   Optional Job check off number 1.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff2:bool = obj["CheckOff2"]
      """   Optional Job check off number 2.  The label for this field is found in JCSyst. If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff3:bool = obj["CheckOff3"]
      """   Optional Job check off number 3.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff4:bool = obj["CheckOff4"]
      """  Optional Job check off number 4.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.CheckOff5:bool = obj["CheckOff5"]
      """  Optional Job check off number 5.  The label for this field is found in JCSyst.  If the label field is blank then field should be invisible.
These "check offs" will be used for selecting jobs.  An example would be a "Engineering" or "Purchasing" check off.  """  
      self.JobReleased:bool = obj["JobReleased"]
      """  Indicates if job has been "Released" to production.  Only jobs that are released can have labor posted against them.  Once labor is posted to a Job this flag cannot be changed.  """  
      self.JobHeld:bool = obj["JobHeld"]
      """  Indicates if the Job has been placed on "HOLD".  Currently this field is only used for display purposes.  It may be used later to prevent or provide warnings and messages in appropriate areas such as Shipping, Purchasing, Labor processing, etc.  """  
      self.SchedStatus:str = obj["SchedStatus"]
      """  Scheduling Status Control (R-Required, P-Pending, A-Active, C-Complete).  NOT CURRENTLY IMPLEMENTED.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number.  Unique key to identify the production job.  When adding "new" records and this is left blank the system will assign a job number.  Assigning numbers will be done by using a "database" sequence number.  Then using that number loop and increment until an available number is found.  """  
      self.PartNum:str = obj["PartNum"]
      """   Part number of the manufactured item.  Does not have to be valid in the Part master.  Cannot be blank.
With verion 8.0 and Advanced Production License a job can have multiple end parts. These are defined in the JobPart table.
This field has not changed. But will now be used to indicate the primary end part that is being produced. That is, the JobPart record where JobPart.PartNum = JobHead.PartNum will be considered as the primary end part. A primary part is only significant on Concurrent mode of production, because it?s quantity drives the material/operation requirements.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number.  Defaults from the most current PartRev.RevisionNum.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number.  An optional field.  Defaulted from BomHead.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  The description of the part that is to be manufactured.  Use the Part.Description as the default.  """  
      self.ProdQty:int = obj["ProdQty"]
      """  This field is not directly maintainable. The value stored here will be different than it was in the pre 8.0- versions. If ProcessMode is  Sequential then this is a total of ALL end parts that are being produced on the job. If Concurrent then it is the production quantity of the primary part /PartsPerOp .  For example 1000 bottle caps are require, 100 caps are produced per machine cycle would result in ProdQty of 10.
See JobPart table for information on end parts of a job.  """  
      self.IUM:str = obj["IUM"]
      """  The unit of measure for the job.  Defaulted from Part.IUM.  """  
      self.StartDate:str = obj["StartDate"]
      """  The Scheduled job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.StartHour:int = obj["StartHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.DueDate:str = obj["DueDate"]
      """  Scheduled finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.DueHour:int = obj["DueHour"]
      """  This field is established by scheduling.  It represents the "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.ReqDueDate:str = obj["ReqDueDate"]
      """  Indicates the date at which this job needs to be completed.  This is maintainable by the user.  It can be defaulted as the earliest due date of the linked orders.  This due date is used as the default date for "backward" scheduling of the job.  """  
      self.JobCode:str = obj["JobCode"]
      """  An optional user defined code.  This will be used for report selections and views of job headers.  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  Contains the Quote number reference.  This was assigned when the job details were pulled in from the quote.  It will be used to show quote figures compared to estimated and actual.  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  Contains the quote line number reference. (see QuoteNum )  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group Code.  Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job header comments.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The default override expense code that will be used for all labor reported against this job.  When this is entered then it will override all over default logic for developing the default G/L expense account in labor entry.  This can be blank or must be valid in the LabExpCd master file.  """  
      self.InCopyList:bool = obj["InCopyList"]
      """  Indicates if the final assembly is to be included in the browse of assemblies in the  "get details"  function.  The user can use to option to keep the "Copy from" list from becoming cluttered with too many assemblies.  This does not prevent the user from copying this assembly it just keeps it out of the browse.  """  
      self.WIName:str = obj["WIName"]
      """   This field is blank or contains the UserID.  When not blank it indicates that some or all the operations of this job are in a "What if" scheduling mode.  In this condition the scheduling board prevents other users from modifying any operations on this job until the changes get committed.
This field is also used as part of an index which allows the system to quickly find the operations that need to be reset to "Actual Schedule".  """  
      self.WIStartDate:str = obj["WIStartDate"]
      """  The Scheduled "What If" job start date (including queue time).  This is not directly user maintainable.  It is calculated/updated via the scheduling functions  """  
      self.WIStartHour:int = obj["WIStartHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to begin (including queue time).  """  
      self.WIDueDate:str = obj["WIDueDate"]
      """  Scheduled "What If" finish date for the entire Job (including move time).  This is not user maintainable.  It is updated via the scheduling process.  """  
      self.WIDueHour:int = obj["WIDueHour"]
      """  This field is established by scheduling.  It represents the What-If "Hour offset from the beginning of the work day" when this job is scheduled to end (including move time).  """  
      self.Candidate:bool = obj["Candidate"]
      """   Indicates if the system considers this  Job as a candidate for the completion process.  Jobs that are marked as JobClosed = No, JobComplete = No and Candidate = Yes can be viewed in the Job Completion/Closing program by selecting the Candidates option.
This field is not directly maintainable.  It is set to based on the value of JobOper.OpComplete of the last operation of the final assembly.  """  
      self.SchedCode:str = obj["SchedCode"]
      """  Scheduling Code.  SchedCode references a record in the SchedPri table.  """  
      self.SchedLocked:bool = obj["SchedLocked"]
      """  If yes the Jobs' schedule is locked, and not affected by the SchedCode.  Locked jobs are allocated (and over-allocated) machine time before any non-locked jobs are scheduled.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Associates the JobHead with a project in the Project table.  This can be blank.  """  
      self.WIPCleared:bool = obj["WIPCleared"]
      """  For closed jobs (JobHead.JobClosed = yes) this indicates if all of the costs on this job have been removed from WIP.  Costs are moved out of WIP during the "Generate WIP transactions" process.  """  
      self.JobFirm:bool = obj["JobFirm"]
      """  A flag which controls whether or not the MRP process can make changes to this job.  MRP can only make changes when JobFirm = No.  """  
      self.PersonList:str = obj["PersonList"]
      """  A LIST-DELIM delimited list of people.  """  
      self.PersonID:str = obj["PersonID"]
      """   Identifies the Person to be used as the Production Planner.  This person is responsible for handling the manufacturing suggestions to this job.
Manufacturing suggestions can be filtered by Planner.
Relates to the Person table.  Defaults from the ProdGrup.PersonID.  """  
      self.ProdTeamID:str = obj["ProdTeamID"]
      """  Production Team for the Job.  Associates the JobHead with a ProdTeam.  """  
      self.QtyCompleted:int = obj["QtyCompleted"]
      """   Production quantity completed.
Updated via JobOper write trigger.  If JobOper is the "Final Operation" (see JobAsmbl.FinalOpr) then this is set equal to JobOper.QtyCompleted.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DatePurged:str = obj["DatePurged"]
      """  The date the detail for the Job was purged.  The detail is the LaborDtl, PartTrans, and JobOpMac records associated with the job.  Once details have been purged the job cannot be reopened.  A job must be closed for it to be purged.  """  
      self.TravelerReadyToPrint:bool = obj["TravelerReadyToPrint"]
      """  Indicates if the Traveler can be printed. Print functions are not available if this is = No.  """  
      self.TravelerLastPrinted:str = obj["TravelerLastPrinted"]
      """  The last date the job traveler was mass printed.  """  
      self.StatusReadyToPrint:bool = obj["StatusReadyToPrint"]
      """  Indicates if the Status can be printed. Print functions are not available if this is = No.  """  
      self.StatusLastPrinted:str = obj["StatusLastPrinted"]
      """  The last date the job status was mass printed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The Service Call number that this Job is linked to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The Service Call Line that this Job is linked to.  """  
      self.JobType:str = obj["JobType"]
      """  Describe the type of job this is: MFG = Manufacturing, MNT = Maintenance, PRJ = Project, SRV = Service  """  
      self.RestoreFlag:str = obj["RestoreFlag"]
      """  Used to determine if this record was modified during the last What-If Schedule Restore.  The contents are Date-Time.  Example: "04/11/02-34221".  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.LockQty:bool = obj["LockQty"]
      """  Indicates that the quantity on this job is locked  """  
      self.HDCaseNum:int = obj["HDCaseNum"]
      """  The help desk case that created this job.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """   Values: S(Sequential) or C(Concurrent).
Defaults as S. Must have Advanced Production License to change. Controls how the operations and material requirements are developed. Concurrent jobs are used where the production time is based on the number of machine operations performed and not on the number of parts created. For example, a stamping operation where each cycle of the machine stamps out x number of parts. A further extension of this is that the operation can yield multiple different parts from each cycle of the machine.  Identification of these parts and there associated PPO (parts per operation) is define in the JobPart table.  """  
      self.PlannedActionDate:str = obj["PlannedActionDate"]
      """  The planned date when the job needs to be actioned by the production department to make sure that the job is ready on the planned completion date.  """  
      self.PlannedKitDate:str = obj["PlannedKitDate"]
      """  The date that the job needs to be ready for the warehouse to kit to make sure that it is ready for the job start date.  """  
      self.MSPTaskID:str = obj["MSPTaskID"]
      """  The task ID that is returned from Microsoft Project.  """  
      self.MSPPredecessor:str = obj["MSPPredecessor"]
      """  This is the Microsoft Project predecessor. This needs to be a text field as Microsoft Project may pass back an alpha numeric string.  """  
      self.UserMapData:str = obj["UserMapData"]
      """  Character field that will contain the coma separated data that has been returned from Microsoft Project. This data will be retained exactly as it was returned from Microsoft Project. This field will NOT be editable within Epicor.  """  
      self.ProductionYield:bool = obj["ProductionYield"]
      """  Flag to indicate whether operations for this job will use the production yield features set up in OpMaster for the operation code. Defaulted from Site.ProductionYield  """  
      self.OrigProdQty:int = obj["OrigProdQty"]
      """  This field will be set to the value of the JobHead.ProdQty at the time the JobHead.Engineered flag is set to true.  """  
      self.PreserveOrigQtys:bool = obj["PreserveOrigQtys"]
      """  This field is used to indicate whether the original quantities should be reset in the job header and its assemblies at JobHead update if JobHead.JobEngineered has been changed from false to true. Generally the orig qtys will be reset, unless this flag is set to true because the user was asked if they wanted to reset the orig qtys and they answered yes.  """  
      self.NoAutoCompletion:bool = obj["NoAutoCompletion"]
      """  If set to yes then exclude this job from the Job Auto-Completion process. Not directly maintainable.  """  
      self.NoAutoClosing:bool = obj["NoAutoClosing"]
      """  No Auto Closing. If set to yes then exclude this job from the Job Auto-Closing process.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user that created this Job.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date that this Job was created.  """  
      self.WhseAllocFlag:bool = obj["WhseAllocFlag"]
      """  Indicates if the PartWhse allocation needs to be/has been updated by the new time delated process.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of PDM parts.  """  
      self.ExportRequested:str = obj["ExportRequested"]
      """  This field is used to store a code that represents the external system that the Job is being exported to (ex. PDM).  This field is short lived, it is used to instruct the write trigger logic to create IM records for certain types of external systems.  After creating the IM records, the trigger logic should immediately clear the field.  """  
      self.SplitMfgCostElements:bool = obj["SplitMfgCostElements"]
      """  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  This is defaulted from the JCSyst.SplitMfgCostElements and is not user maintainable.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Cross Reference Part Num. Used for alternate serial mask support.  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """   Cross Reference Part Type. Used for alternate serial mask support.

I=Internal Cross Reference / C = Customer Part  """  
      self.XRefCustNum:int = obj["XRefCustNum"]
      """  Customer Number XRefPartNum is related to if it is a customer part. Used for alternate serial number mask support.  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part Number. Used in the configurator to identify the configurator part Number.  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  Base Revision Number. Used in the configurator to identify the configurator part revision Number.  """  
      self.RoughCutScheduled:bool = obj["RoughCutScheduled"]
      """  Indicates if the job was rough cut scheduled.  """  
      self.EquipID:str = obj["EquipID"]
      """   The ID of the Equipment that this "Maintenance Job" is for.
Foreign key component to Equip table.  """  
      self.PlanNum:int = obj["PlanNum"]
      """   Preventive Maintenance Plan Number that this "Maintenance Job" is for. Foreign key component to EquipPlan table.
Note: A Maintenance Job does not have to be for a Preventive Maintenance plan, in which case this is zero.
If time based plan, then the closing process will update the EquipPlan.NextDate. Therefore, the Job must know the EquipID and PlanNum in order to do this.  """  
      self.MaintPriority:str = obj["MaintPriority"]
      """  Maintenance Job Priority. Valid values: H - High, M - Medium, L - Low.  M is default or if created from a Maint Request then MaintReq.Priority is used as default.  """  
      self.SplitJob:bool = obj["SplitJob"]
      """  Internal field indicating this job was created by a job split.  Assigned true when a job has been split due to start minimum lot size quantity processing.  """  
      self.NumberSource:bool = obj["NumberSource"]
      """  Indicates the type of prefix which is used for create jobs in MRP  """  
      self.CloseMeterReading:int = obj["CloseMeterReading"]
      """  The Meter Reading value entered at time of Job Closing.  """  
      self.IssueTopicID1:str = obj["IssueTopicID1"]
      """  Maintenance Issue Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintIssue = Yes  """  
      self.IssueTopicID2:str = obj["IssueTopicID2"]
      """  Maintenance Issue Topic 2. A sub-topic of IssueTopicID1.  """  
      self.IssueTopicID3:str = obj["IssueTopicID3"]
      """  Maintenance Issue Topic 3. A sub-topic of IssueTopicID2.  """  
      self.IssueTopicID4:str = obj["IssueTopicID4"]
      """  Maintenance Issue Topic 4. A sub-topic of IssueTopicID3.  """  
      self.IssueTopicID5:str = obj["IssueTopicID5"]
      """  Maintenance Issue Topic 5. A sub-topic of IssueTopicID4.  """  
      self.IssueTopicID6:str = obj["IssueTopicID6"]
      """  Maintenance Issue Topic 6. A sub-topic of IssueTopicID5.  """  
      self.IssueTopicID7:str = obj["IssueTopicID7"]
      """  Maintenance Issue Topic 7. A sub-topic of IssueTopicID6.  """  
      self.IssueTopicID8:str = obj["IssueTopicID8"]
      """  Maintenance Issue Topic 8. A sub-topic of IssueTopicID7.  """  
      self.IssueTopicID9:str = obj["IssueTopicID9"]
      """  Maintenance Issue Topic 9. A sub-topic of IssueTopicID8.  """  
      self.IssueTopicID10:str = obj["IssueTopicID10"]
      """  Maintenance Issue Topic 10. A sub-topic of IssueTopicID9.  """  
      self.IssueTopics:str = obj["IssueTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.ResTopicID1:str = obj["ResTopicID1"]
      """  Maintenance Resolution Topic 1.  Pertinent to maint jobs only. (JobType = "MNT") Foreign Key to HDTopic table.  Must be a top level topic (HDTopic.TopLevel = Yes) and HDTopic.MaintRes = Yes  """  
      self.ResTopicID2:str = obj["ResTopicID2"]
      """  Maintenance Resolution Topic 2. A sub-topic of ResTopicID1.  """  
      self.ResTopicID3:str = obj["ResTopicID3"]
      """  Maintenace  Resolution Topic 3. A sub-topic of ResTopicID2.  """  
      self.ResTopicID4:str = obj["ResTopicID4"]
      """  Maintenance Resolution Topic 4. A sub-topic of ResTopicID3.  """  
      self.ResTopicID5:str = obj["ResTopicID5"]
      """  Maintenance Resolution Topic 5. A sub-topic of ResTopicID4.  """  
      self.ResTopicID6:str = obj["ResTopicID6"]
      """  Maintenance Resolution Topic 6. A sub-topic of ResTopicID5.  """  
      self.ResTopicID7:str = obj["ResTopicID7"]
      """  Maintenance Resolution Topic 7. A sub-topic of ResTopicID6.  """  
      self.ResTopicID8:str = obj["ResTopicID8"]
      """  Maintenance Resolution Topic 8. A sub-topic of ResTopicID7.  """  
      self.ResTopicID9:str = obj["ResTopicID9"]
      """  Maintenance Resolution Topic 9. A sub-topic of ResTopicID8.  """  
      self.ResTopicID10:str = obj["ResTopicID10"]
      """  Maintenance Resolution Topic 10. A sub-topic of ResTopicID9.  """  
      self.ResTopics:str = obj["ResTopics"]
      """  This is the combination of TopicID1 - TopicID10.  This is system maintained and provides a single word-indexed field for searching.  """  
      self.Forward:bool = obj["Forward"]
      """  It is updated by Calculate Global Scheduling Order process, it indicates if a job has to be scheduled Backwards or Forwards by Global Scheduling Process and it can be modified by Adjust Scheduling Global Order  """  
      self.SchedSeq:int = obj["SchedSeq"]
      """  This is the sequence number used to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.PAAExists:bool = obj["PAAExists"]
      """  Indicates if at least one subassembly contains a part that is plan as assembly.  It does not indicate if the assembly is marked as PAA - only that the part is PAA in the BOM.  Used in MRP when determining if a job can be reused.  """  
      self.DtlsWithinLeadTime:bool = obj["DtlsWithinLeadTime"]
      """  Indicates if the job structure (BOM) was created inside or outside of the mfg lead time for the job part.  Used in MRP when determining if a job can be reused.  """  
      self.GroupSeq:int = obj["GroupSeq"]
      """  GroupSeq  """  
      self.RoughCut:bool = obj["RoughCut"]
      """  It indicates that the shop load for that job was not generated (shopload table). The load in shopload can be recreated by Save Resource Load process  """  
      self.PlanGUID:str = obj["PlanGUID"]
      """  PlanGUID  """  
      self.PlanUserID:str = obj["PlanUserID"]
      """  PlanUserID  """  
      self.LastChangedBy:str = obj["LastChangedBy"]
      """  LastChangedBy  """  
      self.LastChangedOn:str = obj["LastChangedOn"]
      """  LastChangedOn  """  
      self.EPMExportLevel:int = obj["EPMExportLevel"]
      """  EPMExportLevel  """  
      self.JobWorkflowState:str = obj["JobWorkflowState"]
      """  JobWorkflowState  """  
      self.JobCSR:str = obj["JobCSR"]
      """  JobCSR  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LastExternalMESDate:str = obj["LastExternalMESDate"]
      """  LastExternalMESDate  """  
      self.LastScheduleDate:str = obj["LastScheduleDate"]
      """  LastScheduleDate  """  
      self.LastScheduleProc:str = obj["LastScheduleProc"]
      """  LastScheduleProc  """  
      self.SchedPriority:int = obj["SchedPriority"]
      """  Sequence priority used internally by Calculate Global Scheduling Order process to order the jobs to be scheduled by Global Scheduling, it is generated by Scheduling Order Process taking into account the priorities of the jobs  """  
      self.DaysLate:int = obj["DaysLate"]
      """  It indicates the days a job is going to be late in relation to its required due date  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process  """  
      self.SyncReqBy:bool = obj["SyncReqBy"]
      """  SyncReqBy  """  
      self.CustName:str = obj["CustName"]
      """  CustName  """  
      self.CustID:str = obj["CustID"]
      """  CustID  """  
      self.IsCSRSet:bool = obj["IsCSRSet"]
      """  IsCSRSet  """  
      self.UnReadyCostProcess:bool = obj["UnReadyCostProcess"]
      """  UnReadyCostProcess  """  
      self.ProcSuspendedUpdates:str = obj["ProcSuspendedUpdates"]
      """  ProcSuspendedUpdates  """  
      self.ProjProcessedDate:str = obj["ProjProcessedDate"]
      """  DateTime field to indicate when this record has been read by project analysis process  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to Epicor FSA  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PersonIDName:str = obj["PersonIDName"]
      """  PersonIDName  """  
      self.ReadyToFulfill:bool = obj["ReadyToFulfill"]
      """  This flag indicates if the job is ready to be fulfilled.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.FSMServiceReportID:str = obj["FSMServiceReportID"]
      """  FSMServiceReportID  """  
      self.AdvanceLaborRate:bool = obj["AdvanceLaborRate"]
      self.dspReadyCostProcess:bool = obj["dspReadyCostProcess"]
      """  Calculated field is set Not UnReadyCostProcess  """  
      self.EnableJobEngineered:bool = obj["EnableJobEngineered"]
      """  Determine if jobengineered is enabled or disabled.  """  
      self.EnableJobFirm:bool = obj["EnableJobFirm"]
      """  Should JobFirm be enabled or disabled?  """  
      self.EnableJobReleased:bool = obj["EnableJobReleased"]
      """  Determine if jobreleased is enabled or disabled.  """  
      self.EnableMaterialStatus:bool = obj["EnableMaterialStatus"]
      self.EnableProject:bool = obj["EnableProject"]
      self.EngineerAllowed:bool = obj["EngineerAllowed"]
      """  Is the job allowed to be engineered?  """  
      self.EquipLocDesc:str = obj["EquipLocDesc"]
      self.ExtUpdated:bool = obj["ExtUpdated"]
      """  If some fields except ToFirm have been updated  """  
      self.FinalOpDueDate:str = obj["FinalOpDueDate"]
      """   Final Operation – This is scheduled Due Date for either:
1.	Operation on ASM that has Final Operation checkbox selected
2.	If no Operation on ASM has Final Operation selected than use Last Operation on ASM  """  
      self.FirmProcEnable:bool = obj["FirmProcEnable"]
      """  If it's Stocked assembly and PlanAsAsm is true.  """  
      self.FirmProcess:bool = obj["FirmProcess"]
      """  is used to select stocked Job which will be processed by Firming Process instead of Firm check-box. Is available only for .FirmProcEnable = true (in Job Status Maintenance).  """  
      self.HasPlanAsAsm:bool = obj["HasPlanAsAsm"]
      """  Job has at least one assembly with flag Plan as Assembly.  """  
      self.HeaderSensitive:bool = obj["HeaderSensitive"]
      """  Depending on the engineered job flag, is the header information enabled?  """  
      self.IgnoreMtlConstraints:bool = obj["IgnoreMtlConstraints"]
      """  It will allow displaying default of this value from Plant.IgnoreMtlConstraints  """  
      self.JobTypeName:str = obj["JobTypeName"]
      self.KitTime:int = obj["KitTime"]
      """  If part is backflush the kit time is ignored.  """  
      self.LockedQty:bool = obj["LockedQty"]
      """  Locked Qty Flag  """  
      self.NewMeter:int = obj["NewMeter"]
      self.OldJobNum:str = obj["OldJobNum"]
      """  The old Job Number when JobFirm is changed from no to yes.  """  
      self.OrderQty:int = obj["OrderQty"]
      """  The order qty  """  
      self.PartmasterPart:bool = obj["PartmasterPart"]
      """  Logical field signifying whether JobHead.PartNum is a valid part master part.  """  
      self.PhaseDescription:str = obj["PhaseDescription"]
      self.PMJob:bool = obj["PMJob"]
      """  Relative to Maintenance Jobs (JobType = "MNT") indicates if job is for "Preventive Maintenance".  This is a job that was created for a Equipment Maintenance Plan (JobHead.PlanNum > 0)  """  
      self.ProcessModeDescription:str = obj["ProcessModeDescription"]
      """  Process Mode Description  """  
      self.ReceiveTime:int = obj["ReceiveTime"]
      """  Receive Time field for Job Part entered on Job  """  
      self.SmartString:str = obj["SmartString"]
      """  Original smart string passed in for configuration  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  If TRUE then this field will mean that the smart string has already been processed  """  
      self.SOExists:bool = obj["SOExists"]
      self.StockQty:int = obj["StockQty"]
      self.ToFirm:bool = obj["ToFirm"]
      """  To be Firmed  """  
      self.XRefPartTypeDesc:str = obj["XRefPartTypeDesc"]
      """  Description for XRefPartType  """  
      self.ChangeDescription:str = obj["ChangeDescription"]
      """  The audit change description for the jobaudit record.  """  
      self.ClearDataset:bool = obj["ClearDataset"]
      self.IsCoPart:bool = obj["IsCoPart"]
      """  True if more than one co-part exists  """  
      self.PartRevProcessMfgID:str = obj["PartRevProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.PartRevProcessMfgType:str = obj["PartRevProcessMfgType"]
      """  Type of Process Manufacturing.  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  Determines if the Service Job has to be synchronized with Epicor FSI application.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.EquipMeterUOM:str = obj["EquipMeterUOM"]
      self.EquipSerialNum:str = obj["EquipSerialNum"]
      self.EquipLocID:str = obj["EquipLocID"]
      self.EquipPlant:str = obj["EquipPlant"]
      self.EquipDescription:str = obj["EquipDescription"]
      self.EquipBrand:str = obj["EquipBrand"]
      self.EquipModel:str = obj["EquipModel"]
      self.EquipCurrentMeter:int = obj["EquipCurrentMeter"]
      self.EquipTypeID:str = obj["EquipTypeID"]
      self.EquipOEM:str = obj["EquipOEM"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HDCaseDescription:str = obj["HDCaseDescription"]
      self.IssueTopicID1Description:str = obj["IssueTopicID1Description"]
      self.IssueTopicID10Description:str = obj["IssueTopicID10Description"]
      self.IssueTopicID2Description:str = obj["IssueTopicID2Description"]
      self.IssueTopicID3Description:str = obj["IssueTopicID3Description"]
      self.IssueTopicID4Description:str = obj["IssueTopicID4Description"]
      self.IssueTopicID5Description:str = obj["IssueTopicID5Description"]
      self.IssueTopicID6Description:str = obj["IssueTopicID6Description"]
      self.IssueTopicID7Description:str = obj["IssueTopicID7Description"]
      self.IssueTopicID8Description:str = obj["IssueTopicID8Description"]
      self.IssueTopicID9Description:str = obj["IssueTopicID9Description"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumLocationIDNumReq:bool = obj["PartNumLocationIDNumReq"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.PlantMaintPlant:str = obj["PlantMaintPlant"]
      self.ProdCodeDescription:str = obj["ProdCodeDescription"]
      self.ProdTeamIDDescription:str = obj["ProdTeamIDDescription"]
      self.ProdTeamIDName:str = obj["ProdTeamIDName"]
      self.ProjectIDDescription:str = obj["ProjectIDDescription"]
      self.QuoteLineLineDesc:str = obj["QuoteLineLineDesc"]
      self.QuoteNumCurrencyCode:str = obj["QuoteNumCurrencyCode"]
      self.ResTopicID1Description:str = obj["ResTopicID1Description"]
      self.ResTopicID10Description:str = obj["ResTopicID10Description"]
      self.ResTopicID2Description:str = obj["ResTopicID2Description"]
      self.ResTopicID3Description:str = obj["ResTopicID3Description"]
      self.ResTopicID4Description:str = obj["ResTopicID4Description"]
      self.ResTopicID5Description:str = obj["ResTopicID5Description"]
      self.ResTopicID6Description:str = obj["ResTopicID6Description"]
      self.ResTopicID7Description:str = obj["ResTopicID7Description"]
      self.ResTopicID8Description:str = obj["ResTopicID8Description"]
      self.ResTopicID9Description:str = obj["ResTopicID9Description"]
      self.SchedCodeDescription:str = obj["SchedCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used in the primary key.  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.SNMask:str = obj["SNMask"]
      """  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  """  
      self.SNFormat:str = obj["SNFormat"]
      """   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  """  
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  """  
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      """  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  """  
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      """  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  """  
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      """  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.SerialMaskMaskType:int = obj["SerialMaskMaskType"]
      self.SerialMaskMask:str = obj["SerialMaskMask"]
      self.SerialMaskExample:str = obj["SerialMaskExample"]
      self.SerialMaskDescription:str = obj["SerialMaskDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsRow:
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The part number to which the serial numbers have been assigned.  """  
      self.quantity:int = obj["quantity"]
      """  The quantity of serial numbers that need to be selected.  """  
      self.whereClause:str = obj["whereClause"]
      """  whereClause for filtering available serial numbers  """  
      self.transType:str = obj["transType"]
      """  transType of this transaction  """  
      self.sourceRowID:str = obj["sourceRowID"]
      """  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  """  
      self.enableCreate:bool = obj["enableCreate"]
      """  Determines if serial numbers can be created.  """  
      self.enableSelect:bool = obj["enableSelect"]
      """  Determines if serial numbers can be selected.  """  
      self.enableRetrieve:bool = obj["enableRetrieve"]
      """  Determines if serial numbers can be retrieved.  """  
      self.allowVoided:bool = obj["allowVoided"]
      """  Specifies whether Voided serial numbers can be manually selected.  """  
      self.plant:str = obj["plant"]
      """  The Plant associated with this transaction  """  
      self.xrefPartNum:str = obj["xrefPartNum"]
      self.xrefPartType:str = obj["xrefPartType"]
      self.xrefCustNum:int = obj["xrefCustNum"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.attributeSetShortDescription:str = obj["attributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectSerialNumbersParamsTableset:
   def __init__(self, obj):
      self.SelectSerialNumbersParams:list[Erp_Tablesets_SelectSerialNumbersParamsRow] = obj["SelectSerialNumbersParams"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedJobAsmblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedJobAsmblTableset:
   def __init__(self, obj):
      self.SelectedJobAsmbl:list[Erp_Tablesets_SelectedJobAsmblRow] = obj["SelectedJobAsmbl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedPartTableset:
   def __init__(self, obj):
      self.SelectedParts:list[Erp_Tablesets_SelectedPartsRow] = obj["SelectedParts"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedPartsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNumber  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Serial number prefix  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask the was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.RowSelected:bool = obj["RowSelected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class FillForeignFields_input:
   """ Required : 
   ttIssueReturn
   """  
   def __init__(self, obj):
      self.ttIssueReturn:list[Erp_Tablesets_IssueReturnRow] = obj["ttIssueReturn"]
      pass

class FillForeignFields_output:
   def __init__(self, obj):
      pass

class GenerateDynamicPCID_input:
   """ Required : 
   pkgControlID
   """  
   def __init__(self, obj):
      self.pkgControlID:str = obj["pkgControlID"]
      """  Package control ID code  """  
      pass

class GenerateDynamicPCID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  PCID  """  
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AvailTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetInventoryQtyAdjBrwForWeb_input:
   """ Required : 
   partNum
   attributeSetID
   wareHouseCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number for the adjustment.  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  Attribute Set ID for the adjustment  """  
      self.wareHouseCode:str = obj["wareHouseCode"]
      """  Warehouse code used to get bin information.  """  
      pass

class GetInventoryQtyAdjBrwForWeb_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryQtyAdjBrwTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.primaryBin:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetInventoryQtyAdjBrwInventoryTracking_input:
   """ Required : 
   partNum
   revisionNum
   attributeSetID
   wareHouseCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number for the adjustment.  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision Number used to get bin information. Bins are not filtered by Revision Number if no value is sent.  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  Attribute Set ID used to get bin information. Bins are not filtered by Attribute Set ID if a zero is sent  """  
      self.wareHouseCode:str = obj["wareHouseCode"]
      """  Warehouse code used to get bin information.  """  
      pass

class GetInventoryQtyAdjBrwInventoryTracking_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryQtyAdjBrwTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.primaryBin:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetInventoryQtyAdjBrw_input:
   """ Required : 
   partNum
   attributeSetID
   wareHouseCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number for the adjustment.  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  Attribute Set ID used to get bin information. Bins are not filtered by Attribute Set ID if a zero is sent  """  
      self.wareHouseCode:str = obj["wareHouseCode"]
      """  Warehouse code used to get bin information.  """  
      pass

class GetInventoryQtyAdjBrw_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryQtyAdjBrwTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.primaryBin:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetListJobs_input:
   """ Required : 
   whereClauseJobHead
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobHead:str = obj["whereClauseJobHead"]
      """  Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetListJobs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IssueReturnJobListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetList_input:
   """ Required : 
   whereClauseJobHead
   whereClauseJobAsmbl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobHead:str = obj["whereClauseJobHead"]
      """  Where condition without the where word  """  
      self.whereClauseJobAsmbl:str = obj["whereClauseJobAsmbl"]
      """  Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IssueReturnJobAsmblTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewIssueReturnFromJob_input:
   """ Required : 
   pcFromJobNum
   piFromAssemblySeq
   pcTranType
   pcMtlQueueRowID
   ds
   """  
   def __init__(self, obj):
      self.pcFromJobNum:str = obj["pcFromJobNum"]
      """  From Job number.  """  
      self.piFromAssemblySeq:int = obj["piFromAssemblySeq"]
      """  From Assembly Seq.  """  
      self.pcTranType:str = obj["pcTranType"]
      """  Material movement type XXX-XXX e.g STK-MTL  """  
      self.pcMtlQueueRowID:str = obj["pcMtlQueueRowID"]
      """  Progress database rowid for MtlQueue record  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class GetNewIssueReturnFromJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewIssueReturnToJob_input:
   """ Required : 
   pcToJobNum
   piToAssemblySeq
   pcTranType
   pcMtlQueueRowID
   ds
   """  
   def __init__(self, obj):
      self.pcToJobNum:str = obj["pcToJobNum"]
      """  To Job number.  """  
      self.piToAssemblySeq:int = obj["piToAssemblySeq"]
      """  To Assembly Seq.  """  
      self.pcTranType:str = obj["pcTranType"]
      """  Material movement type XXX-XXX e.g STK-MTL  """  
      self.pcMtlQueueRowID:str = obj["pcMtlQueueRowID"]
      """  Progress database rowid for MtlQueue record  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class GetNewIssueReturnToJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewIssueReturn_input:
   """ Required : 
   pcTranType
   pcMtlQueueRowID
   pCallProcess
   ds
   """  
   def __init__(self, obj):
      self.pcTranType:str = obj["pcTranType"]
      """  Material movement type XXX-XXX e.g STK-MTL.  It can be blank when a valid MtlQueue RowIdent is passed.  """  
      self.pcMtlQueueRowID:str = obj["pcMtlQueueRowID"]
      """  Progress database RowId of MtlQueue record  """  
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class GetNewIssueReturn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewJobAsmblMultiple_input:
   """ Required : 
   pcTranType
   pcMtlQueueRowID
   pCallProcess
   ds
   """  
   def __init__(self, obj):
      self.pcTranType:str = obj["pcTranType"]
      """  Material movement type XXX-XXX e.g STK-MTL  """  
      self.pcMtlQueueRowID:str = obj["pcMtlQueueRowID"]
      """  Progress database rowid for MtlQueue record  """  
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process  """  
      self.ds:list[Erp_Tablesets_SelectedJobAsmblTableset] = obj["ds"]
      pass

class GetNewJobAsmblMultiple_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IssueReturnTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SelectedJobAsmblTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewJobAsmblSearch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SelectedJobAsmblTableset] = obj["ds"]
      pass

class GetNewJobAsmblSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SelectedJobAsmblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartMultiple_input:
   """ Required : 
   pcTranType
   pcMtlQueueRowID
   ds
   """  
   def __init__(self, obj):
      self.pcTranType:str = obj["pcTranType"]
      """  Material movement type XXX-XXX e.g STK-MTL  """  
      self.pcMtlQueueRowID:str = obj["pcMtlQueueRowID"]
      """  Progress database rowid for MtlQueue record  """  
      self.ds:list[Erp_Tablesets_SelectedPartTableset] = obj["ds"]
      pass

class GetNewPartMultiple_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IssueReturnTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SelectedPartTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewPartNum_input:
   """ Required : 
   pcPartNum
   pcTranType
   pcMtlQueueRowID
   ds
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part number  """  
      self.pcTranType:str = obj["pcTranType"]
      """  Material movement type XXX-XXX e.g STK-UKN  """  
      self.pcMtlQueueRowID:str = obj["pcMtlQueueRowID"]
      """  Progress database rowid for MtlQueue record  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class GetNewPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartSearch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SelectedPartTableset] = obj["ds"]
      pass

class GetNewPartSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SelectedPartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   sysRowID
   rowType
   uomCode
   qty
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.sysRowID:str = obj["sysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      self.qty:int = obj["qty"]
      """  Qty (converted if UOM is different)  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.uomCode:str = obj["parameters"]
      self.qty:int = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetRowsJobAssemblies_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsJobAssemblies_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IssueReturnJobAsmblTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRowsWIP_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRowsWIP_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IssueReturnJobAsmblTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseJobHead
   whereClauseJobAsmbl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseJobHead:str = obj["whereClauseJobHead"]
      """  Where condition without the where word  """  
      self.whereClauseJobAsmbl:str = obj["whereClauseJobAsmbl"]
      """  Where condition without the where word  """  
      self.pageSize:int = obj["pageSize"]
      """  # of records returned.  0 means all  """  
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_IssueReturnJobAsmblTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetToBinNumWhereClause_input:
   """ Required : 
   tranType
   toWarehouseCode
   toBinNum
   """  
   def __init__(self, obj):
      self.tranType:str = obj["tranType"]
      """  Tran Type from IssueReturn  """  
      self.toWarehouseCode:str = obj["toWarehouseCode"]
      """  To Warehouse Code from IssueReturn  """  
      self.toBinNum:str = obj["toBinNum"]
      """  To Bin Num from IssueReturn (can be blank)  """  
      pass

class GetToBinNumWhereClause_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.toBinNumWhereClause:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetUnissuedQty_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class GetUnissuedQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetUnpickSettings_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class GetUnpickSettings_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

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

class IsAutoPrintSetup_input:
   """ Required : 
   ipWriteToStaged
   """  
   def __init__(self, obj):
      self.ipWriteToStaged:bool = obj["ipWriteToStaged"]
      """  write to staged table  """  
      pass

class IsAutoPrintSetup_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class IsValidAssembly_input:
   """ Required : 
   pcJobNum
   piAssemblySeq
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job Number  """  
      self.piAssemblySeq:int = obj["piAssemblySeq"]
      """  A sequence number that uniquely
            identifies the JobAsmbl record within the JobNum.  """  
      pass

class IsValidAssembly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.plFound:bool = obj["plFound"]
      pass

      """  output parameters  """  

class JobExists_input:
   """ Required : 
   ipJobNum
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      """  JobNum which should check  """  
      pass

class JobExists_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opJobReleased:bool = obj["opJobReleased"]
      self.opJobClosed:bool = obj["opJobClosed"]
      self.opJobExists:bool = obj["opJobExists"]
      pass

      """  output parameters  """  

class MassUnpickByPCID_input:
   """ Required : 
   pcid
   whse
   bin
   partNum
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  PCID  """  
      self.whse:str = obj["whse"]
      """  Destination Warehouse Code  """  
      self.bin:str = obj["bin"]
      """  Destination Bin Num  """  
      self.partNum:str = obj["partNum"]
      """  Part number for Mass Unpick By PCID (optional)  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class MassUnpickByPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.legalNumMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class MasterInventoryBinTests_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class MasterInventoryBinTests_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pcNeqQtyAction:str = obj["parameters"]
      self.pcNeqQtyMessage:str = obj["parameters"]
      self.pcPCBinAction:str = obj["parameters"]
      self.pcPCBinMessage:str = obj["parameters"]
      self.pcOutBinAction:str = obj["parameters"]
      self.pcOutBinMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class NegativeInventoryTestTran_input:
   """ Required : 
   pcPartNum
   pcWhseCode
   pcBinNum
   pcLotNum
   pcAttributeSetID
   pcPCID
   pcDimCode
   pdDimConvFactor
   pgTranRowId
   ipSellingQuantity
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      self.pcWhseCode:str = obj["pcWhseCode"]
      self.pcBinNum:str = obj["pcBinNum"]
      self.pcLotNum:str = obj["pcLotNum"]
      self.pcAttributeSetID:int = obj["pcAttributeSetID"]
      self.pcPCID:str = obj["pcPCID"]
      self.pcDimCode:str = obj["pcDimCode"]
      self.pdDimConvFactor:int = obj["pdDimConvFactor"]
      self.pgTranRowId:str = obj["pgTranRowId"]
      self.ipSellingQuantity:int = obj["ipSellingQuantity"]
      pass

class NegativeInventoryTestTran_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcNeqQtyAction:str = obj["parameters"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class NegativeInventoryTest_input:
   """ Required : 
   pcPartNum
   pcWhseCode
   pcBinNum
   pcLotNum
   pcAttributeSetID
   pcPCID
   pcDimCode
   pdDimConvFactor
   ipSellingQuantity
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      self.pcWhseCode:str = obj["pcWhseCode"]
      self.pcBinNum:str = obj["pcBinNum"]
      self.pcLotNum:str = obj["pcLotNum"]
      self.pcAttributeSetID:int = obj["pcAttributeSetID"]
      self.pcPCID:str = obj["pcPCID"]
      self.pcDimCode:str = obj["pcDimCode"]
      self.pdDimConvFactor:int = obj["pdDimConvFactor"]
      self.ipSellingQuantity:int = obj["ipSellingQuantity"]
      pass

class NegativeInventoryTest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcNeqQtyAction:str = obj["parameters"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeASTUom_input:
   """ Required : 
   pUM
   ds
   """  
   def __init__(self, obj):
      self.pUM:str = obj["pUM"]
      """  from unit of measure  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangeASTUom_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFromAssemblySeq_input:
   """ Required : 
   piFromAssemblySeq
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.piFromAssemblySeq:int = obj["piFromAssemblySeq"]
      """  From Assembly Seq  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      pass

class OnChangeFromAssemblySeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFromBinNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangeFromBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFromJobNum_input:
   """ Required : 
   pcFromJobNum
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.pcFromJobNum:str = obj["pcFromJobNum"]
      """  From Job Number  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      pass

class OnChangeFromJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFromJobSeq_input:
   """ Required : 
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      pass

class OnChangeFromJobSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeFromPCID_input:
   """ Required : 
   fromPCID
   allowDiffPartAndUM
   questionCheck
   pCallProcess
   ds
   """  
   def __init__(self, obj):
      self.fromPCID:str = obj["fromPCID"]
      """  From PCID  """  
      self.allowDiffPartAndUM:bool = obj["allowDiffPartAndUM"]
      """  If true allows to default parts that have a different part and/or  unit of measure  """  
      self.questionCheck:bool = obj["questionCheck"]
      """  If true throws questions  for the user before defaulting PCID and Part values,
            depending on whether it found a match for the Assembly part on the selected PCID  """  
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling process  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangeFromPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.questionMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeFromWarehouse_input:
   """ Required : 
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      pass

class OnChangeFromWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLotNum_input:
   """ Required : 
   pcLotNum
   ds
   """  
   def __init__(self, obj):
      self.pcLotNum:str = obj["pcLotNum"]
      """  Proposed LotNum value  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangeLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeToAssemblySeq_input:
   """ Required : 
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      pass

class OnChangeToAssemblySeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeToJobNum_input:
   """ Required : 
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      pass

class OnChangeToJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeToJobSeq_input:
   """ Required : 
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      pass

class OnChangeToJobSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeToPCID_input:
   """ Required : 
   ipPCID
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.ipPCID:str = obj["ipPCID"]
      """  Proposed To PCID value  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      pass

class OnChangeToPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeToWarehouse_input:
   """ Required : 
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      pass

class OnChangeToWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTranQty_input:
   """ Required : 
   pdTranQty
   ds
   """  
   def __init__(self, obj):
      self.pdTranQty:int = obj["pdTranQty"]
      """  Transaction Qty  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangeTranQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeUM_input:
   """ Required : 
   pUM
   ds
   """  
   def __init__(self, obj):
      self.pUM:str = obj["pUM"]
      """  Transaction UOM  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangeUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAttributeSetAdjustments_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangingAttributeSetAdjustments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingFromBinNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangingFromBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangingJobSeq_input:
   """ Required : 
   piJobSeq
   pcDirection
   pCallProcess
   ds
   """  
   def __init__(self, obj):
      self.piJobSeq:int = obj["piJobSeq"]
      """  JobSeq  """  
      self.pcDirection:str = obj["pcDirection"]
      """  Direction  """  
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangingJobSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNumAdjustments_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangingRevisionNumAdjustments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingToJobSeq_input:
   """ Required : 
   piToJobSeq
   ds
   """  
   def __init__(self, obj):
      self.piToJobSeq:int = obj["piToJobSeq"]
      """  Propose ToJobSeq value.  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class OnChangingToJobSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PerformMaterialMovement2_input:
   """ Required : 
   plNegQtyAction
   ds
   """  
   def __init__(self, obj):
      self.plNegQtyAction:bool = obj["plNegQtyAction"]
      """  when TranQty changes, perform NegativeInventoryTest. Provide the answer of that test here.  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class PerformMaterialMovement2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.legalNumberMessage:str = obj["parameters"]
      self.message:str = obj["parameters"]
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class PerformMaterialMovementWithLegalNum_input:
   """ Required : 
   plNegQtyAction
   ds
   legalNum
   """  
   def __init__(self, obj):
      self.plNegQtyAction:bool = obj["plNegQtyAction"]
      """  when TranQty changes, perform NegativeInventoryTest. Provide the answer of that test here.  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.legalNum:str = obj["legalNum"]
      """  The Legal Number to be used in PartTran.  """  
      pass

class PerformMaterialMovementWithLegalNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.legalNumberMessage:str = obj["parameters"]
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class PerformMaterialMovement_input:
   """ Required : 
   plNegQtyAction
   ds
   """  
   def __init__(self, obj):
      self.plNegQtyAction:bool = obj["plNegQtyAction"]
      """  when TranQty changes, perform NegativeInventoryTest. Provide the answer of that test here.  """  
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class PerformMaterialMovement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.legalNumberMessage:str = obj["parameters"]
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreGetNewIssueReturn_input:
   """ Required : 
   pcMtlQueueRowID
   """  
   def __init__(self, obj):
      self.pcMtlQueueRowID:str = obj["pcMtlQueueRowID"]
      """  Progress database RowId of MtlQueue record  """  
      pass

class PreGetNewIssueReturn_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcAction:str = obj["parameters"]
      self.pcMessage:str = obj["parameters"]
      self.pdQtyAvailable:int = obj["parameters"]
      pass

      """  output parameters  """  

class PrePerformMaterialMovement_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

class PrePerformMaterialMovement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class SetQuantity_output:
   def __init__(self, obj):
      pass

class SuppressPrintMessages_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Employee ID  """  
      pass

class SuppressPrintMessages_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  Suppress Print Messages  """  
      pass

class ValidUOM_input:
   """ Required : 
   iPartNum
   iUOM
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      self.iUOM:str = obj["iUOM"]
      pass

class ValidUOM_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidatePkgControlID_input:
   """ Required : 
   pkgControlIDCode
   """  
   def __init__(self, obj):
      self.pkgControlIDCode:str = obj["pkgControlIDCode"]
      """  Proposed package control ID code  """  
      pass

class ValidatePkgControlID_output:
   def __init__(self, obj):
      pass

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

class _History07_08_output:
   def __init__(self, obj):
      pass

class checkWhseBin_input:
   """ Required : 
   ttIssueReturn
   """  
   def __init__(self, obj):
      self.ttIssueReturn:list[Erp_Tablesets_IssueReturnRow] = obj["ttIssueReturn"]
      pass

class checkWhseBin_output:
   def __init__(self, obj):
      pass

class validateToBinNum_input:
   """ Required : 
   ds
   binNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      self.binNum:str = obj["binNum"]
      """  binNum  """  
      pass

class validateToBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_IssueReturnTableset] = obj["ds"]
      pass

      """  output parameters  """  

