import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.PROC.GLImportProcSvc
# Description: GL Import process
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetServerTempPath(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetServerTempPath
   Description: Return Path to upload import file
   OperationID: GetServerTempPath
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetServerTempPath_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetServerTempPath_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBookID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBookID
   Description: Method to call when changing the Book.
   OperationID: ChangeBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEntryMode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEntryMode
   Description: Method to call when changing the Entry Mode.
   OperationID: ChangeEntryMode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEntryMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEntryMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFiscalPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFiscalPeriod
   Description: Method to call when changing the Fiscal Period.
   OperationID: ChangeFiscalPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFiscalPeriodType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFiscalPeriodType
   Description: Method to call when changing the Fiscal Period Type.
   OperationID: ChangeFiscalPeriodType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFiscalPeriodType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalPeriodType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFiscalYear
   Description: Method to call when changing the Fiscal Year.
   OperationID: ChangeFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFiscalYearSuffix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFiscalYearSuffix
   Description: Method to call when changing the Fiscal Year Suffix.
   OperationID: ChangeFiscalYearSuffix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFiscalYearSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalYearSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJournalCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJournalCode
   Description: Method to call when changing the Journal Code
   OperationID: ChangeJournalCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJournalCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJournalCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckGroupID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckGroupID
   Description: Purpose:
Parameters:
<param name="ipGroupID">Group ID</param><param name="ds">Import parameters.</param><param name="opMessage">Information messages to be displayed by the UI</param>
Notes:
   OperationID: CheckGroupID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckGroupID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckGroupID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckFiscalYear
   Description: Method to call before updating the journal group. This method will check the
date that the user entered to verify it is in the current fiscal year and period.
If it is not then opMessage will be assigned with message text.  If it is
then the Fiscal Period and Year will be updated.
   OperationID: CheckFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetApplicationDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetApplicationDefaults
   Description: Purpose: to load params when form is opened
Parameters:
<param name="ds"></param>
Notes:
   OperationID: GetApplicationDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetApplicationDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApplicationDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetApplicationDefaultsExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetApplicationDefaultsExt
   Description: Purpose: to load params when form is opened
Parameters:
<param name="ds"></param><param name="clearGroup">True if group should be empty</param><param name="ipGroup">Group ID</param>
Notes:
   OperationID: GetApplicationDefaultsExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetApplicationDefaultsExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApplicationDefaultsExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultsAndApplicationDefaultsExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultsAndApplicationDefaultsExt
   Description: Purpose: to load params when form is opened
Parameters:
<param name="ds"></param>
Notes:
   OperationID: GetDefaultsAndApplicationDefaultsExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultsAndApplicationDefaultsExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultsAndApplicationDefaultsExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ClearAndGetApplicationDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ClearAndGetApplicationDefaults
   Description: Purpose: to load params when form is opened
Parameters:
<param name="ds"></param>
Notes:
   OperationID: ClearAndGetApplicationDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ClearAndGetApplicationDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearAndGetApplicationDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFiscalPeriodList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFiscalPeriodList
   Description: Returns fiscal period list in code/description format
   OperationID: GetFiscalPeriodList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFiscalPeriodList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalPeriodList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetTokenList(tokenDataType, epicorHeaders = None):
   """  
   Summary: Invoke method GetTokenList
   Description: Returns a comma separated list of valid tokens for the given datatype.
   OperationID: Get_GetTokenList
      :param tokenDataType: Desc: Type of token for which you want the list of valid values. Valid Types are; Date, FiscalPeriod, FiscalYear   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tokenDataType=" + tokenDataType

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetTokenValue(pcValue, epicorHeaders = None):
   """  
   Summary: Invoke method GetTokenValue
   Description: Returns a token list of values based on a type that is passed in.
   OperationID: Get_GetTokenValue
      :param pcValue: Desc: Type of token   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pcValue=" + pcValue

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_SubmitToAgent(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SubmitToAgent
   Description: Submits this report to a System Agent. The system agent will run the task based on the defined schedule.
   OperationID: SubmitToAgent
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SubmitToAgent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SubmitToAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaults
   Description: Use to get the current parameter defaults that the user has established for this report.
Note: This is automatically run as part of the GetNewParameters method.
In cases where the ParamSetID would be blank (this is most cases) you would not need to call this method.
It is provided to provide the ability to get the defaults after the user has enter a value into the field
designated as ParamSetID.
As is the case in GLFinancial Reports the GLFinancialParam.GLReportID is used as the ParamSetID field.
Another possible use would be to Reset the screen to default values.
   OperationID: GetDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetNewParameters(epicorHeaders = None):
   """  
   Summary: Invoke method GetNewParameters
   Description: Creates a new (parameter record) in the dataset.
Note: A parameter dataset should never contain more than one record.
   OperationID: Get_GetNewParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_GetParamsFromAgent(agentID, agentSchedNum, agentTaskNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetParamsFromAgent
   Description: Gets existing parameter values from the Task Agent and returns them in the in the dataset.
Note: Parameters are stored as individual fields in the database. This method is
used to retrieve those values and return them in the specific dataset.
   OperationID: Get_GetParamsFromAgent
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParamsFromAgent_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "agentID=" + agentID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "agentSchedNum=" + agentSchedNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "agentTaskNum=" + agentTaskNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetParamTaskDef(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetParamTaskDef
   Description: Use to get the specified ProcessSet Task defaults that the user has established for this report.
It is provided to provide the ability to get the defaults after the user has enter a value into the field
designated as ParamSetID.
   OperationID: GetParamTaskDef
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetParamTaskDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetParamTaskDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveDefaults
   Description: Use to remove the current parameter defaults that the user has established for this report.
   OperationID: RemoveDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunDirect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunDirect
   Description: Use to run the process directly from the client instead of submitting to a System Agent.
   OperationID: RunDirect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunDirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunDirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveDefaults
   Description: Use to save the current parameters as the users defaults for this report
   OperationID: SaveDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveProcessTask(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveProcessTask
   Description: Use to save the current parameters as the users defaults for this report
<param name="maintProgram">UI Maintenance program </param><param name="ds" />
   OperationID: SaveProcessTask
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveProcessTask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveProcessTask_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.GLImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeBookID_input:
   """ Required : 
   proposeBookID
   ds
   """  
   def __init__(self, obj):
      self.proposeBookID:str = obj["proposeBookID"]
      """  The proposed Book ID  """  
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class ChangeBookID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEntryMode_input:
   """ Required : 
   proposedBookMode
   ds
   """  
   def __init__(self, obj):
      self.proposedBookMode:str = obj["proposedBookMode"]
      """  The proposed Entry Mode  """  
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class ChangeEntryMode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFiscalPeriodType_input:
   """ Required : 
   proposedPeriodType
   ds
   """  
   def __init__(self, obj):
      self.proposedPeriodType:str = obj["proposedPeriodType"]
      """  The proposed Fiscal Period Type  """  
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class ChangeFiscalPeriodType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFiscalPeriod_input:
   """ Required : 
   proposedFiscalPeriod
   ds
   """  
   def __init__(self, obj):
      self.proposedFiscalPeriod:int = obj["proposedFiscalPeriod"]
      """  The proposed Fiscal Period  """  
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class ChangeFiscalPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFiscalYearSuffix_input:
   """ Required : 
   proposedFiscalYearSuffix
   ds
   """  
   def __init__(self, obj):
      self.proposedFiscalYearSuffix:str = obj["proposedFiscalYearSuffix"]
      """  The proposed Fiscal Year Suffix  """  
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class ChangeFiscalYearSuffix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFiscalYear_input:
   """ Required : 
   proposedFiscalYear
   ds
   """  
   def __init__(self, obj):
      self.proposedFiscalYear:int = obj["proposedFiscalYear"]
      """  The proposed Fiscal Year  """  
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class ChangeFiscalYear_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeJournalCode_input:
   """ Required : 
   ipJournalCode
   ds
   """  
   def __init__(self, obj):
      self.ipJournalCode:str = obj["ipJournalCode"]
      """  The proposed Journal Code  """  
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class ChangeJournalCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckFiscalYear_input:
   """ Required : 
   ds
   cGroupID
   cJEDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      self.cGroupID:str = obj["cGroupID"]
      """  Group Id field  """  
      self.cJEDate:str = obj["cJEDate"]
      """  JEDate proposed value  """  
      pass

class CheckFiscalYear_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckGroupID_input:
   """ Required : 
   ipGroupID
   ds
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class CheckGroupID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ClearAndGetApplicationDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class ClearAndGetApplicationDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_GLImportProcParamRow:
   def __init__(self, obj):
      self.GroupID:str = obj["GroupID"]
      """  GL Group ID to import.  """  
      self.CommentText:str = obj["CommentText"]
      """  Extended text to describe the journal header.  Defaults to all GLJrnDtl.CommentText.  """  
      self.Post:bool = obj["Post"]
      """  Flag to determine if the Imported Group will be posted.  """  
      self.InpDateFormat:str = obj["InpDateFormat"]
      """  Selected date format that will be imported.  """  
      self.InpNumFormat:str = obj["InpNumFormat"]
      """  Selected numeric format that will be imported.  """  
      self.BookMode:str = obj["BookMode"]
      """  Indicates what mode the GL transactions will be entered.  Valid values are (S) for Single Book and (M) for Multi-Book.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Unique code that identifies the currency.  """  
      self.RateGrpCode:str = obj["RateGrpCode"]
      self.JEDate:str = obj["JEDate"]
      """  Default Journal Date for all entries made in this group.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal Year to which all entries in this group will be posted.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  The Fiscal Period to which all entries in this group will be posted.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  A code that defines a journal.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal Year Suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period where derived from.  """  
      self.FiscalPeriodType:str = obj["FiscalPeriodType"]
      """  Indicates what type of fiscal periods can be selected for the group.  Values are: O - Ordinary periods, C - Closing Periods.  """  
      self.FiscalCalendarDesc:str = obj["FiscalCalendarDesc"]
      self.RateGrpDescription:str = obj["RateGrpDescription"]
      self.JournalCodeDesc:str = obj["JournalCodeDesc"]
      self.BookDescription:str = obj["BookDescription"]
      self.CurrencyCodeDesc:str = obj["CurrencyCodeDesc"]
      self.HasDetails:bool = obj["HasDetails"]
      """  Used by the UI for row rules.  Indicates if the group has GLJrnhed records.  """  
      self.CSVListDelimiter:str = obj["CSVListDelimiter"]
      """  Selected Delimiter to use when parsing the import/export file  """  
      self.ClientImportFileName:str = obj["ClientImportFileName"]
      self.ServerImportFileName:str = obj["ServerImportFileName"]
      self.InvalidLinesHandlingOp:str = obj["InvalidLinesHandlingOp"]
      """  Options for the system’s handling of invalid lines found in the import file. 'Skip Invalid Lines' means that the GL Import skips invalid lines and imports the valid ones. 'Cancel Import' means that if any lines are found invalid, then the process should roll back all imported data without creating any Journals.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.AutoAction:str = obj["AutoAction"]
      self.PrinterName:str = obj["PrinterName"]
      self.AgentSchedNum:int = obj["AgentSchedNum"]
      self.AgentID:str = obj["AgentID"]
      self.AgentTaskNum:int = obj["AgentTaskNum"]
      self.RecurringTask:bool = obj["RecurringTask"]
      self.RptPageSettings:str = obj["RptPageSettings"]
      self.RptPrinterSettings:str = obj["RptPrinterSettings"]
      self.RptVersion:str = obj["RptVersion"]
      self.ReportStyleNum:int = obj["ReportStyleNum"]
      self.WorkstationID:str = obj["WorkstationID"]
      self.TaskNote:str = obj["TaskNote"]
      self.ArchiveCode:int = obj["ArchiveCode"]
      self.DateFormat:str = obj["DateFormat"]
      self.NumericFormat:str = obj["NumericFormat"]
      self.AgentCompareString:str = obj["AgentCompareString"]
      self.ProcessID:str = obj["ProcessID"]
      self.ProcessCompany:str = obj["ProcessCompany"]
      self.ProcessSystemCode:str = obj["ProcessSystemCode"]
      self.ProcessTaskNum:int = obj["ProcessTaskNum"]
      self.DecimalsGeneral:int = obj["DecimalsGeneral"]
      self.DecimalsCost:int = obj["DecimalsCost"]
      self.DecimalsPrice:int = obj["DecimalsPrice"]
      self.GlbDecimalsGeneral:int = obj["GlbDecimalsGeneral"]
      self.GlbDecimalsCost:int = obj["GlbDecimalsCost"]
      self.GlbDecimalsPrice:int = obj["GlbDecimalsPrice"]
      self.FaxSubject:str = obj["FaxSubject"]
      self.FaxTo:str = obj["FaxTo"]
      self.FaxNumber:str = obj["FaxNumber"]
      self.EMailTo:str = obj["EMailTo"]
      self.EMailCC:str = obj["EMailCC"]
      self.EMailBCC:str = obj["EMailBCC"]
      self.EMailBody:str = obj["EMailBody"]
      self.AttachmentType:str = obj["AttachmentType"]
      self.ReportCurrencyCode:str = obj["ReportCurrencyCode"]
      self.ReportCultureCode:str = obj["ReportCultureCode"]
      self.SSRSRenderFormat:str = obj["SSRSRenderFormat"]
      self.UIXml:str = obj["UIXml"]
      self.PrintReportParameters:bool = obj["PrintReportParameters"]
      self.SSRSEnableRouting:bool = obj["SSRSEnableRouting"]
      self.DesignMode:bool = obj["DesignMode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLImportProcTableset:
   def __init__(self, obj):
      self.GLImportProcParam:list[Erp_Tablesets_GLImportProcParamRow] = obj["GLImportProcParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetApplicationDefaultsExt_input:
   """ Required : 
   ds
   clearGroup
   ipGroup
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      self.clearGroup:bool = obj["clearGroup"]
      self.ipGroup:str = obj["ipGroup"]
      pass

class GetApplicationDefaultsExt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetApplicationDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class GetApplicationDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDefaultsAndApplicationDefaultsExt_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class GetDefaultsAndApplicationDefaultsExt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class GetDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetFiscalPeriodList_input:
   """ Required : 
   fiscalCalendarID
   fiscalYear
   fiscalYearSuffix
   fiscalPeriod
   fiscalPeriodType
   """  
   def __init__(self, obj):
      self.fiscalCalendarID:str = obj["fiscalCalendarID"]
      """  Fiscal Calendar ID  """  
      self.fiscalYear:int = obj["fiscalYear"]
      """  Fiscal Year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.fiscalPeriod:int = obj["fiscalPeriod"]
      """  Fiscal Period  """  
      self.fiscalPeriodType:str = obj["fiscalPeriodType"]
      """  Fiscal Period Type  """  
      pass

class GetFiscalPeriodList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.fiscalPeriodList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewParameters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLImportProcTableset] = obj["returnObj"]
      pass

class GetParamTaskDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class GetParamTaskDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetParamsFromAgent_input:
   """ Required : 
   agentID
   agentSchedNum
   agentTaskNum
   """  
   def __init__(self, obj):
      self.agentID:str = obj["agentID"]
      self.agentSchedNum:int = obj["agentSchedNum"]
      self.agentTaskNum:int = obj["agentTaskNum"]
      pass

class GetParamsFromAgent_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLImportProcTableset] = obj["returnObj"]
      pass

class GetServerTempPath_input:
   """ Required : 
   fileName
   folder
   """  
   def __init__(self, obj):
      self.fileName:str = obj["fileName"]
      """  File name  """  
      self.folder:int = obj["folder"]
      """  Special folder  """  
      pass

class GetServerTempPath_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Full server path  """  
      pass

class GetTokenList_input:
   """ Required : 
   tokenDataType
   """  
   def __init__(self, obj):
      self.tokenDataType:str = obj["tokenDataType"]
      """  Type of token for which you want the list of valid values. Valid Types are; Date, FiscalPeriod, FiscalYear  """  
      pass

class GetTokenList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetTokenValue_input:
   """ Required : 
   pcValue
   """  
   def __init__(self, obj):
      self.pcValue:str = obj["pcValue"]
      """  Type of token  """  
      pass

class GetTokenValue_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pcTokenValue:str = obj["parameters"]
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

class RemoveDefaults_input:
   """ Required : 
   paramSetID
   """  
   def __init__(self, obj):
      self.paramSetID:str = obj["paramSetID"]
      """  The defaults are stored with a key of Company,UserID,ProgramID,ParamSetID and FieldName
            The values of all of these, except ParamSetID are controlled by the backend logic.
            In most cases the ParamSetID is blank. Usually for a single program the user can only have one set of defaults.
            This parameter provides multi parameters sets to be associated with a single report.
            As is the case of GL Financial Reports. The user picks from a list of reports to be run.
            In this case you would pass the GLFinancialParam.GLReportID as the ParamSetID  """  
      pass

class RemoveDefaults_output:
   def __init__(self, obj):
      pass

class RunDirect_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class RunDirect_output:
   def __init__(self, obj):
      pass

class SaveDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class SaveDefaults_output:
   def __init__(self, obj):
      pass

class SaveProcessTask_input:
   """ Required : 
   maintProgram
   ds
   """  
   def __init__(self, obj):
      self.maintProgram:str = obj["maintProgram"]
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      pass

class SaveProcessTask_output:
   def __init__(self, obj):
      pass

class SubmitToAgent_input:
   """ Required : 
   ds
   agentID
   agentSchedNum
   agentTaskNum
   maintProgram
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLImportProcTableset] = obj["ds"]
      self.agentID:str = obj["agentID"]
      """  Agent ID that will run this task  """  
      self.agentSchedNum:int = obj["agentSchedNum"]
      """  Identifies the agent schedule of when this task should be run.
           Set to zero if you want to run this immediately.  """  
      self.agentTaskNum:int = obj["agentTaskNum"]
      """  Identifies the agent task number within the schedule that is to be updated.
           Set to zero if you want to create a new task.  """  
      self.maintProgram:str = obj["maintProgram"]
      """  Identifies the Maintenance program to run  """  
      pass

class SubmitToAgent_output:
   def __init__(self, obj):
      pass

