import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.PROC.RunGLAllocationsSvc
# Description: GL Allocations process
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetSchedAllocations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSchedAllocations
   Description: Fills allocation Batches List
   OperationID: GetSchedAllocations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSchedAllocations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSchedAllocations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSearchFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSearchFilter
   Description: Create Search filter string for Allocation batch Schedule Search
   OperationID: GetSearchFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSearchFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSearchFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetYTDStartDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetYTDStartDate
   Description: Purpose:  Default the start date to first date of current year when YTDAllocations = yes
Parameters:  none
Notes:
<param name="ds"> Run GL Allocations DataSet</param><param name="ipYTDAlloc">logical for ytd allocations</param>
   OperationID: SetYTDStartDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetYTDStartDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetYTDStartDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdGLAllocBatches(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdGLAllocBatches
   Description: Fills allocation Batches List
   OperationID: UpdGLAllocBatches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdGLAllocBatches_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdGLAllocBatches_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateApplyDate
   Description: Validate the Apply Date
   OperationID: ValidateApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultApplyDates(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultApplyDates
   Description: Calculates default Apply Date and Reversal Date in case of 'Manual' Apply Dates Option
   OperationID: GetDefaultApplyDates
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultApplyDates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultApplyDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnFiscalPeriodChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnFiscalPeriodChanged
   Description: Should be called when user changes Fiscal Year, Fiscal Year Suffix or Fislal Period.
   OperationID: OnFiscalPeriodChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnFiscalPeriodChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnFiscalPeriodChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnGLBookChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnGLBookChanged
   Description: Occurs when GL Book is changed.
   OperationID: OnGLBookChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnGLBookChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnGLBookChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultFiscalPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultFiscalPeriod
   Description: Determine default Fiscal Period based on today's date.
   OperationID: GetDefaultFiscalPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.RunGLAllocationsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_GLAllocBatchesRow:
   def __init__(self, obj):
      self.BatchID:str = obj["BatchID"]
      self.BookID:str = obj["BookID"]
      self.SchedDate:str = obj["SchedDate"]
      self.Reverse:bool = obj["Reverse"]
      self.BatchDescription:str = obj["BatchDescription"]
      self.BookDesc:str = obj["BookDesc"]
      self.FiscalCalDesc:str = obj["FiscalCalDesc"]
      self.ApplyDate:str = obj["ApplyDate"]
      self.ReversalDate:str = obj["ReversalDate"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RunGLAllocationsParamRow:
   def __init__(self, obj):
      self.ApplyDate:str = obj["ApplyDate"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.GLBookDesc:str = obj["GLBookDesc"]
      self.Simulation:bool = obj["Simulation"]
      """  Indicates if this is a simulation or general ledger run.  """  
      self.EditList:bool = obj["EditList"]
      """  Identifies if the allocations are ocurring in edit list mode or live mode.  """  
      self.BatchList:str = obj["BatchList"]
      """  List of batches to process  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.BookID:str = obj["BookID"]
      self.StartDate:str = obj["StartDate"]
      """  Starting date to use for selecting allocation data.  Defaults to the first day of the fiscal period based upon the Apply Date. Unless the alllocation is for Year-To-Date then the start date is the first date in the current fiscal year.  """  
      self.EndDate:str = obj["EndDate"]
      """  Ending date to use for selecting allocation data.  Defaults to the end of the fiscal period based upon the Apply Date.  """  
      self.YTDAlloc:bool = obj["YTDAlloc"]
      """  Year-to-date allocations.  If yes then allocation data selection starts at the beginning of the current fiscal year.  """  
      self.FiscalPerStart:str = obj["FiscalPerStart"]
      self.FiscalPerEnd:str = obj["FiscalPerEnd"]
      self.SchedDateList:str = obj["SchedDateList"]
      """  List scheduled dates for batches to process  """  
      self.ReversalDate:str = obj["ReversalDate"]
      self.ApplyDatesOption:str = obj["ApplyDatesOption"]
      self.SelectBy:str = obj["SelectBy"]
      """  Period, DatesRange  """  
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

class Erp_Tablesets_RunGLAllocationsTableset:
   def __init__(self, obj):
      self.RunGLAllocationsParam:list[Erp_Tablesets_RunGLAllocationsParamRow] = obj["RunGLAllocationsParam"]
      self.GLAllocBatches:list[Erp_Tablesets_GLAllocBatchesRow] = obj["GLAllocBatches"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetApplicationDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

class GetApplicationDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDefaultApplyDates_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

class GetDefaultApplyDates_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDefaultFiscalPeriod_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

class GetDefaultFiscalPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

class GetDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewParameters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["returnObj"]
      pass

class GetParamTaskDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

class GetParamTaskDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["returnObj"]
      pass

class GetSchedAllocations_input:
   """ Required : 
   ipBookID
   fieldName
   fieldValue
   ds
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID  for the Allocation Batch search  """  
      self.fieldName:str = obj["fieldName"]
      """  changed field's name for the Allocation Bacth search  """  
      self.fieldValue      #schema had no properties on an object.
      """  changed field's value for the Allocation Bacth search  """  
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

class GetSchedAllocations_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSearchFilter_input:
   """ Required : 
   ipBookID
   ipStartDate
   ipEndDate
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID  for the Allocation Batch search  """  
      self.ipStartDate:str = obj["ipStartDate"]
      """  Start Date for the Allocation Bacth search  """  
      self.ipEndDate:str = obj["ipEndDate"]
      """  End Date for the Allocation Bacth search  """  
      pass

class GetSearchFilter_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.myFilter:str = obj["parameters"]
      pass

      """  output parameters  """  

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

class OnFiscalPeriodChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

class OnFiscalPeriodChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnGLBookChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

class OnGLBookChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

      """  output parameters  """  

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
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

class RunDirect_output:
   def __init__(self, obj):
      pass

class SaveDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

class SaveProcessTask_output:
   def __init__(self, obj):
      pass

class SetYTDStartDate_input:
   """ Required : 
   ds
   ipYTDAlloc
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      self.ipYTDAlloc:bool = obj["ipYTDAlloc"]
      pass

class SetYTDStartDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SubmitToAgent_input:
   """ Required : 
   ds
   agentID
   agentSchedNum
   agentTaskNum
   maintProgram
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
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

class UpdGLAllocBatches_input:
   """ Required : 
   ipBookID
   ipBatchIDList
   ds
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID  for the Allocation Batch search  """  
      self.ipBatchIDList:str = obj["ipBatchIDList"]
      """  List of Batch IDs  """  
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

class UpdGLAllocBatches_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RunGLAllocationsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateApplyDate_input:
   """ Required : 
   ipBookID
   ipApplyDate
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID  for the Allocation Batch search  """  
      self.ipApplyDate:str = obj["ipApplyDate"]
      """  Apply Date for the Allocation Bacth search  """  
      pass

class ValidateApplyDate_output:
   def __init__(self, obj):
      pass

