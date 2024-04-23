import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.PROC.BudgetImportProcSvc
# Description: BudgetImportProcSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GLBookPreValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GLBookPreValidation
   Description: Method performs validations of newly selected book.
   OperationID: GLBookPreValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GLBookPreValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GLBookPreValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FiscalCalPreValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FiscalCalPreValidation
   Description: Method performs validations of newly selected fiscal year/suffix.
   OperationID: FiscalCalPreValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FiscalCalPreValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FiscalCalPreValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BudgetCodePreValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BudgetCodePreValidation
   Description: Method performs validations of imported budget Code.
   OperationID: BudgetCodePreValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BudgetCodePreValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BudgetCodePreValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBudgetCodeDesc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBudgetCodeDesc
   Description: Check Budget Code Description
   OperationID: CheckBudgetCodeDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBudgetCodeDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBudgetCodeDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBudgetCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBudgetCode
   Description: Check existing budget codes and return its description
   OperationID: ChangeBudgetCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBudgetCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBudgetCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBudgetCodeDesc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBudgetCodeDesc
   Description: Validate new Budget Code Description
   OperationID: ChangeBudgetCodeDesc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBudgetCodeDesc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBudgetCodeDesc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeGLBook(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeGLBook
   Description: Validate new BookID value
   OperationID: ChangeGLBook
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeGLBook_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGLBook_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFiscalYear
   Description: Validate FiscalYear on change
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFiscalYear
   Description: Validate FiscalYear/FiscalYearSuffix
   OperationID: ValidateFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ParseInitialImportParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ParseInitialImportParams
   Description: Returns initial params for budget import
   OperationID: ParseInitialImportParams
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ParseInitialImportParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseInitialImportParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportData
   Description: Import Budget
   OperationID: ImportData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.BudgetImportProcSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BudgetCodePreValidation_input:
   """ Required : 
   budgetCodeID
   budgetCodeDesc
   """  
   def __init__(self, obj):
      self.budgetCodeID:str = obj["budgetCodeID"]
      """  Budget Code ID  """  
      self.budgetCodeDesc:str = obj["budgetCodeDesc"]
      """  Budget Code Description  """  
      pass

class BudgetCodePreValidation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeBudgetCodeDesc_input:
   """ Required : 
   budgetCodeID
   budgetCodeDesc
   """  
   def __init__(self, obj):
      self.budgetCodeID:str = obj["budgetCodeID"]
      """  Budget Code ID  """  
      self.budgetCodeDesc:str = obj["budgetCodeDesc"]
      """  Budget Code Description  """  
      pass

class ChangeBudgetCodeDesc_output:
   def __init__(self, obj):
      pass

class ChangeBudgetCode_input:
   """ Required : 
   budgetCodeID
   """  
   def __init__(self, obj):
      self.budgetCodeID:str = obj["budgetCodeID"]
      """  Budget Code ID  """  
      pass

class ChangeBudgetCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.budgetCodeDesc:str = obj["parameters"]
      self.isNewBudgetCode:bool = obj["isNewBudgetCode"]
      self.errMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeFiscalYear_input:
   """ Required : 
   fiscalCalID
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.fiscalCalID:str = obj["fiscalCalID"]
      """  Fiscal Calendar  """  
      self.fiscalYear:int = obj["fiscalYear"]
      """  Fiscal Year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      pass

class ChangeFiscalYear_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.fiscalYearSuffix:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeGLBook_input:
   """ Required : 
   newBookID
   oldBookID
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.newBookID:str = obj["newBookID"]
      """  Selected BookID  """  
      self.oldBookID:str = obj["oldBookID"]
      """  BookID from file  """  
      self.fiscalYear:int = obj["fiscalYear"]
      """  Selected Fiscal Year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Selected Fiscal Year Suffix  """  
      pass

class ChangeGLBook_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outBookDesc:str = obj["parameters"]
      self.outCalendarID:str = obj["parameters"]
      self.outCOACode:str = obj["parameters"]
      self.warningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckBudgetCodeDesc_input:
   """ Required : 
   budgetCodeID
   budgetCodeDesc
   """  
   def __init__(self, obj):
      self.budgetCodeID:str = obj["budgetCodeID"]
      """  Budget Code ID  """  
      self.budgetCodeDesc:str = obj["budgetCodeDesc"]
      """  Budget Code Description  """  
      pass

class CheckBudgetCodeDesc_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_BudgetImportProcParamRow:
   def __init__(self, obj):
      self.BookDescription:str = obj["BookDescription"]
      """  Book description from import file.  """  
      self.BookID:str = obj["BookID"]
      """  Book from import file.  """  
      self.ClientImportFileName:str = obj["ClientImportFileName"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Fiscal Calendar assigned to GL book.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  Fiscal year from import file.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix from import file.  """  
      self.ImportFinBudgets:bool = obj["ImportFinBudgets"]
      """  Indicates if the program should import Financial Budgets.  """  
      self.ImportMode:str = obj["ImportMode"]
      """  "Import Mode. Available Values  ""N"" - ""Add new values only"" - add only new recods if it does not corrupt existion data ""R"" - ""Add new and replace existing"" -  add new values and update existing ""O"" - ""Override all"" - remove existing and add records from file"  """  
      self.ImportStatBudgets:bool = obj["ImportStatBudgets"]
      """  Indicates if the program should import Statistical Budgets.  """  
      self.ServerImportFileName:str = obj["ServerImportFileName"]
      self.BudgetCodeID:str = obj["BudgetCodeID"]
      self.BudgetCodeDesc:str = obj["BudgetCodeDesc"]
      self.COACode:str = obj["COACode"]
      self.IsNewBudgetCode:bool = obj["IsNewBudgetCode"]
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

class Erp_Tablesets_BudgetImportProcTableset:
   def __init__(self, obj):
      self.BudgetImportProcParam:list[Erp_Tablesets_BudgetImportProcParamRow] = obj["BudgetImportProcParam"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FiscalCalPreValidation_input:
   """ Required : 
   fiscalCalID
   fiscalYear
   fiscalYearSuffix
   numOfPeriodsInFile
   """  
   def __init__(self, obj):
      self.fiscalCalID:str = obj["fiscalCalID"]
      self.fiscalYear:int = obj["fiscalYear"]
      """  Selected Fiscal Year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Selected Fiscal Year Suffix  """  
      self.numOfPeriodsInFile:int = obj["numOfPeriodsInFile"]
      """  Number of Periods in File  """  
      pass

class FiscalCalPreValidation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class GLBookPreValidation_input:
   """ Required : 
   bookID
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      """  BookID  """  
      pass

class GLBookPreValidation_output:
   def __init__(self, obj):
      pass

class GetDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BudgetImportProcTableset] = obj["ds"]
      pass

class GetDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BudgetImportProcTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewParameters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BudgetImportProcTableset] = obj["returnObj"]
      pass

class GetParamTaskDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BudgetImportProcTableset] = obj["ds"]
      pass

class GetParamTaskDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_BudgetImportProcTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_BudgetImportProcTableset] = obj["returnObj"]
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

class ImportData_input:
   """ Required : 
   ds
   importMode
   """  
   def __init__(self, obj):
      self.ds      #schema had no properties on an object.
      """  Dataset with data for import  """  
      self.importMode:str = obj["importMode"]
      """  Import Mode
            N = “Add new values only”
            R = “Add new and replace existing”
            O = “Override all”  """  
      pass

class ImportData_output:
   def __init__(self, obj):
      pass

class ParseInitialImportParams_input:
   """ Required : 
   serverFileName
   """  
   def __init__(self, obj):
      self.serverFileName:str = obj["serverFileName"]
      """  Server file name  """  
      pass

class ParseInitialImportParams_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.bookID:str = obj["parameters"]
      self.fiscalYear:int = obj["parameters"]
      self.fiscalYearSuffix:str = obj["parameters"]
      self.budgetCodeID:str = obj["parameters"]
      self.budgetCodeDesc:str = obj["parameters"]
      self.numOfPeriods:int = obj["parameters"]
      self.importFinBudgets:bool = obj["importFinBudgets"]
      self.importStatBudgets:bool = obj["importStatBudgets"]
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
      self.ds:list[Erp_Tablesets_BudgetImportProcTableset] = obj["ds"]
      pass

class RunDirect_output:
   def __init__(self, obj):
      pass

class SaveDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_BudgetImportProcTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_BudgetImportProcTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_BudgetImportProcTableset] = obj["ds"]
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

class ValidateFiscalYear_input:
   """ Required : 
   fiscalCalID
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.fiscalCalID:str = obj["fiscalCalID"]
      """  Fiscal Calendar  """  
      self.fiscalYear:int = obj["fiscalYear"]
      """  Fiscal Year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      pass

class ValidateFiscalYear_output:
   def __init__(self, obj):
      pass

