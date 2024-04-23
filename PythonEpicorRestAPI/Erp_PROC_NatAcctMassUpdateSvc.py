import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.PROC.NatAcctMassUpdateSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_EditListValidateParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EditListValidateParam
   Description: Validates parameters prior to opening the Print Edit List
   OperationID: EditListValidateParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EditListValidateParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EditListValidateParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_checkForNaturalAccountControl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method checkForNaturalAccountControl
   Description: checkForNaturalAccountControl
   OperationID: checkForNaturalAccountControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/checkForNaturalAccountControl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/checkForNaturalAccountControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCOA_Type(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCOA_Type
   Description: Assign values to COACat
   OperationID: ChangeCOA_Type
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCOA_Type_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCOA_Type_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnCOACodeChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnCOACodeChanging
   Description: Validate COACode
   OperationID: OnCOACodeChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnCOACodeChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnCOACodeChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnCOASegValuesChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnCOASegValuesChanging
   Description: Validate Segment Values
   OperationID: OnCOASegValuesChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnCOASegValuesChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnCOASegValuesChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnAnalysisCodeChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnAnalysisCodeChange
   Description: Validate Analysis Code
   OperationID: OnAnalysisCodeChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnAnalysisCodeChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnAnalysisCodeChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnCategoryChanging(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnCategoryChanging
   Description: This method convert the document currency to the journal currency.
   OperationID: OnCategoryChanging
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnCategoryChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnCategoryChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateDefaultSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateDefaultSegment
   Description: Purpose:
Parameters:
<param name="ipCOACode"> COA Code</param><param name="ipSubSegmentNbr"> Segment Number to check for existence</param><param name="ipSegmentCode">Segment Code to search for </param>
Notes:
   OperationID: ValidateDefaultSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateDefaultSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDefaultSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSubSegment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSubSegment
   Description: Purpose:
Parameters:
<param name="ipCOACode"> COA Code</param><param name="ipSubSegmentNbr"> Segment Code to search for </param>
Notes:
   OperationID: ValidateSubSegment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSubSegment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSubSegment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_COACatofSegValues(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method COACatofSegValues
   Description: Return category type of segments
   OperationID: COACatofSegValues
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/COACatofSegValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/COACatofSegValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCurrencyAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCurrencyAccount
   Description: On currency account change all related currencies should be updated to allowed/not allowed
   OperationID: ChangeCurrencyAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCurrencyAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCurrencyAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRevalueOpt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRevalueOpt
   Description: On Revalue Option change
   OperationID: ChangeRevalueOpt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRevalueOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevalueOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRateType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRateType
   Description: On Rate Type changing
   OperationID: ChangeRateType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRateType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAccountContext(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAccountContext
   Description: On Account context changing
   OperationID: ChangeAccountContext
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAccountContext_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAccountContext_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultsOnAdd(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultsOnAdd
   Description: Set Default creating a new account
   OperationID: DefaultsOnAdd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultsOnAdd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultsOnAdd_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCurrencyAccountType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCurrencyAccountType
   Description: Validate Currency Account Type
   OperationID: ValidateCurrencyAccountType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCurrencyAccountType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCurrencyAccountType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCurrencyAccounts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCurrencyAccounts
   Description: Validate Currency Accounts book default data.
   OperationID: ValidateCurrencyAccounts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCurrencyAccounts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCurrencyAccounts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.PROC.NatAcctMassUpdateSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class COACatofSegValues_input:
   """ Required : 
   ipCOACode
   ipSegmentNbr
   ipSegmentRange
   refType
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  Segment number  """  
      self.ipSegmentRange:str = obj["ipSegmentRange"]
      """  Segment Value list  """  
      self.refType:str = obj["refType"]
      """  Category Type  """  
      pass

class COACatofSegValues_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.refType:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeAccountContext_input:
   """ Required : 
   context
   """  
   def __init__(self, obj):
      self.context:str = obj["context"]
      """  GL Account Context  """  
      pass

class ChangeAccountContext_output:
   def __init__(self, obj):
      pass

class ChangeCOA_Type_input:
   """ Required : 
   ipCOACode
   ipType
   ds
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  The COACode  """  
      self.ipType:str = obj["ipType"]
      """  The Type  """  
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class ChangeCOA_Type_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCurrencyAccount_input:
   """ Required : 
   ipValue
   ds
   """  
   def __init__(self, obj):
      self.ipValue:str = obj["ipValue"]
      """  Currency Account flag  """  
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class ChangeCurrencyAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRateType_input:
   """ Required : 
   rateType
   isCredit
   """  
   def __init__(self, obj):
      self.rateType:str = obj["rateType"]
      """  Rate Type to change.  """  
      self.isCredit:bool = obj["isCredit"]
      """  Flag to use Credit Rate Type instead of Debit.  """  
      pass

class ChangeRateType_output:
   def __init__(self, obj):
      pass

class ChangeRevalueOpt_input:
   """ Required : 
   proposedRevalue
   ds
   """  
   def __init__(self, obj):
      self.proposedRevalue:int = obj["proposedRevalue"]
      """  Proposed Revalue option  """  
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class ChangeRevalueOpt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultsOnAdd_input:
   """ Required : 
   ipGLAccount
   ipAccountField
   ds
   """  
   def __init__(self, obj):
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Account being added  """  
      self.ipAccountField:str = obj["ipAccountField"]
      """  GL Account being added  """  
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class DefaultsOnAdd_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class EditListValidateParam_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class EditListValidateParam_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_NatAcctMassUpdateRow:
   def __init__(self, obj):
      self.COACode:str = obj["COACode"]
      """  Chart of Accounts header table  """  
      self.AcctType:str = obj["AcctType"]
      """   COA category Types -                
Values:
A - All
B - Balance Sheet
I - Income Statement  """  
      self.COACat:str = obj["COACat"]
      """  COA Categories  """  
      self.SegRanges:str = obj["SegRanges"]
      """  Natural Account Segment Ranges  """  
      self.COADescription:str = obj["COADescription"]
      """  COA Description  """  
      self.COAMaster:bool = obj["COAMaster"]
      """  COA is Master  """  
      self.ActiveFlag:bool = obj["ActiveFlag"]
      """  Indicates if the segment is active. Transactions cannot be posted to inactive segments  """  
      self.ActiveFlagOrd:bool = obj["ActiveFlagOrd"]
      """  Override Active flag.  """  
      self.CategoryDesc:str = obj["CategoryDesc"]
      """  Category description  """  
      self.CategoryOrd:bool = obj["CategoryOrd"]
      """  Override Category flag.  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Date the segment begins to be used. It must be less than or equal to the Effective To Date  """  
      self.EffectiveFromOrd:bool = obj["EffectiveFromOrd"]
      """  Override Effective From date flag  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Date the segment is no longer used. It must be greater than or equal to the Effective From date, if a value was entered in that field  """  
      self.EffectiveToOrd:bool = obj["EffectiveToOrd"]
      """  Override Effective To flag.  """  
      self.ExtAnalysisCode:str = obj["ExtAnalysisCode"]
      """  External financial analysis code linked to the natural account  """  
      self.ExtAnalysisCodeDesc:str = obj["ExtAnalysisCodeDesc"]
      """  Analysis code description  """  
      self.MatchingEnabled:bool = obj["MatchingEnabled"]
      """  This flag determines if journal detail records with this natural account are allowed to be matched  """  
      self.MatchingEnabledOrd:bool = obj["MatchingEnabledOrd"]
      """  Override Matching Enabled flag.  """  
      self.NormalBalance:str = obj["NormalBalance"]
      """  Indicates if the account is a debit or credit and is only valid for the natural account (segment 1).  Valid values are D for Debit and C for Credit.  """  
      self.NormalBalanceDesc:str = obj["NormalBalanceDesc"]
      """  Normal balance description  """  
      self.NormalBalanceOrd:bool = obj["NormalBalanceOrd"]
      """  Override Normal Balance flag.  """  
      self.RestrictID:str = obj["RestrictID"]
      """  Executing dll name.  """  
      self.RestrictionMod:str = obj["RestrictionMod"]
      """   Modify restrictions:          
A - Add
O - Override
R - Replace  """  
      self.RestrictionsList:str = obj["RestrictionsList"]
      """  Lists of restrictions to add/override  """  
      self.ReverseCategory:str = obj["ReverseCategory"]
      """  Identifies the account category this is used to determine characteristics when the segment value is reversed.  """  
      self.ReverseCategoryDesc:str = obj["ReverseCategoryDesc"]
      """  Reverse category description.  """  
      self.ReverseCategoryOrd:bool = obj["ReverseCategoryOrd"]
      """  Override reverse category.  """  
      self.SegmentOptsList:str = obj["SegmentOptsList"]
      """  List of segment options to add/override  """  
      self.SegmentOptsMod:str = obj["SegmentOptsMod"]
      """   Modify segment options          
A - Add
O - Override
R - Replace  """  
      self.SegOptsEnabled:bool = obj["SegOptsEnabled"]
      """  Enable segment options  """  
      self.Summarization:int = obj["Summarization"]
      """   0)      Summarize (default)   
1)      Summarize debit and credits separately
2)      No summarization  """  
      self.SummarizationDesc:str = obj["SummarizationDesc"]
      """  Summarization description  """  
      self.SummarizationOrd:bool = obj["SummarizationOrd"]
      """  Override summarization flag.  """  
      self.ExtAnalysisCodeOrd:bool = obj["ExtAnalysisCodeOrd"]
      """  Override external analysis code flag.  """  
      self.Category:str = obj["Category"]
      """  Required for the Natrual Account (segment number 1). Identifies the account category that is used to determine other characteristics.  """  
      self.ValOption:str = obj["ValOption"]
      """   Indicates if a segment is used for the natural account.  Valid values are:
M - Mandatory
O - Optional
N - Not Used  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  CurrencyAcctType  """  
      self.RevalueOpt:int = obj["RevalueOpt"]
      """  RevalueOpt  """  
      self.CreditRateType:str = obj["CreditRateType"]
      """  Rate type used for credit balances  """  
      self.DebitRateType:str = obj["DebitRateType"]
      """  Rate type used for debit balances.  """  
      self.GainAccount:str = obj["GainAccount"]
      """  GainAccount  """  
      self.GainAcctDesc:str = obj["GainAcctDesc"]
      """  Gain Account Description  """  
      self.GainSegVal1:str = obj["GainSegVal1"]
      """  GainSegVal1  """  
      self.GainSegVal10:str = obj["GainSegVal10"]
      """  GainSegVal10  """  
      self.GainSegVal11:str = obj["GainSegVal11"]
      """  GainSegVal11  """  
      self.GainSegVal12:str = obj["GainSegVal12"]
      """  GainSegVal12  """  
      self.GainSegVal13:str = obj["GainSegVal13"]
      """  GainSegVal13  """  
      self.GainSegVal14:str = obj["GainSegVal14"]
      """  GainSegVal14  """  
      self.GainSegVal15:str = obj["GainSegVal15"]
      """  GainSegVal15  """  
      self.GainSegVal16:str = obj["GainSegVal16"]
      """  GainSegVal16  """  
      self.GainSegVal17:str = obj["GainSegVal17"]
      """  GainSegVal17  """  
      self.GainSegVal18:str = obj["GainSegVal18"]
      """  GainSegVal18  """  
      self.GainSegVal19:str = obj["GainSegVal19"]
      """  GainSegVal19  """  
      self.GainSegVal2:str = obj["GainSegVal2"]
      """  GainSegVal2  """  
      self.GainSegVal20:str = obj["GainSegVal20"]
      """  GainSegVal20  """  
      self.GainSegVal3:str = obj["GainSegVal3"]
      """  GainSegVal3  """  
      self.GainSegVal4:str = obj["GainSegVal4"]
      """  GainSegVal4  """  
      self.GainSegVal5:str = obj["GainSegVal5"]
      """  GainSegVal5  """  
      self.GainSegVal6:str = obj["GainSegVal6"]
      """  GainSegVal6  """  
      self.GainSegVal7:str = obj["GainSegVal7"]
      """  GainSegVal7  """  
      self.GainSegVal8:str = obj["GainSegVal8"]
      """  GainSegVal8  """  
      self.GainSegVal9:str = obj["GainSegVal9"]
      """  GainSegVal9  """  
      self.LossAccount:str = obj["LossAccount"]
      """  LossAccount  """  
      self.LossAcctDesc:str = obj["LossAcctDesc"]
      """  Loss Account Description  """  
      self.LossSegVal1:str = obj["LossSegVal1"]
      """  LossSegVal1  """  
      self.LossSegVal10:str = obj["LossSegVal10"]
      """  LossSegVal10  """  
      self.LossSegVal11:str = obj["LossSegVal11"]
      """  LossSegVal11  """  
      self.LossSegVal12:str = obj["LossSegVal12"]
      """  LossSegVal12  """  
      self.LossSegVal13:str = obj["LossSegVal13"]
      """  LossSegVal13  """  
      self.LossSegVal14:str = obj["LossSegVal14"]
      """  LossSegVal14  """  
      self.LossSegVal15:str = obj["LossSegVal15"]
      """  LossSegVal15  """  
      self.LossSegVal16:str = obj["LossSegVal16"]
      """  LossSegVal16  """  
      self.LossSegVal17:str = obj["LossSegVal17"]
      """  LossSegVal17  """  
      self.LossSegVal18:str = obj["LossSegVal18"]
      """  LossSegVal18  """  
      self.LossSegVal19:str = obj["LossSegVal19"]
      """  LossSegVal19  """  
      self.LossSegVal2:str = obj["LossSegVal2"]
      """  LossSegVal2  """  
      self.LossSegVal20:str = obj["LossSegVal20"]
      """  LossSegVal20  """  
      self.LossSegVal3:str = obj["LossSegVal3"]
      """  LossSegVal3  """  
      self.LossSegVal4:str = obj["LossSegVal4"]
      """  LossSegVal4  """  
      self.LossSegVal5:str = obj["LossSegVal5"]
      """  LossSegVal5  """  
      self.LossSegVal6:str = obj["LossSegVal6"]
      """  LossSegVal6  """  
      self.LossSegVal7:str = obj["LossSegVal7"]
      """  LossSegVal7  """  
      self.LossSegVal8:str = obj["LossSegVal8"]
      """  LossSegVal8  """  
      self.LossSegVal9:str = obj["LossSegVal9"]
      """  LossSegVal9  """  
      self.AccrualAccount:str = obj["AccrualAccount"]
      """  AccrualAccount  """  
      self.AccrualAcctDesc:str = obj["AccrualAcctDesc"]
      """  Accrual Account Description  """  
      self.AccrualSegVal1:str = obj["AccrualSegVal1"]
      """  AccrualSegVal1  """  
      self.AccrualSegVal10:str = obj["AccrualSegVal10"]
      """  AccrualSegVal10  """  
      self.AccrualSegVal11:str = obj["AccrualSegVal11"]
      """  AccrualSegVal11  """  
      self.AccrualSegVal12:str = obj["AccrualSegVal12"]
      """  AccrualSegVal12  """  
      self.AccrualSegVal13:str = obj["AccrualSegVal13"]
      """  AccrualSegVal13  """  
      self.AccrualSegVal14:str = obj["AccrualSegVal14"]
      """  AccrualSegVal14  """  
      self.AccrualSegVal15:str = obj["AccrualSegVal15"]
      """  AccrualSegVal15  """  
      self.AccrualSegVal16:str = obj["AccrualSegVal16"]
      """  AccrualSegVal16  """  
      self.AccrualSegVal17:str = obj["AccrualSegVal17"]
      """  AccrualSegVal17  """  
      self.AccrualSegVal18:str = obj["AccrualSegVal18"]
      """  AccrualSegVal18  """  
      self.AccrualSegVal19:str = obj["AccrualSegVal19"]
      """  AccrualSegVal19  """  
      self.AccrualSegVal2:str = obj["AccrualSegVal2"]
      """  AccrualSegVal2  """  
      self.AccrualSegVal20:str = obj["AccrualSegVal20"]
      """  AccrualSegVal20  """  
      self.AccrualSegVal3:str = obj["AccrualSegVal3"]
      """  AccrualSegVal3  """  
      self.AccrualSegVal4:str = obj["AccrualSegVal4"]
      """  AccrualSegVal4  """  
      self.AccrualSegVal5:str = obj["AccrualSegVal5"]
      """  AccrualSegVal5  """  
      self.AccrualSegVal6:str = obj["AccrualSegVal6"]
      """  AccrualSegVal6  """  
      self.AccrualSegVal7:str = obj["AccrualSegVal7"]
      """  AccrualSegVal7  """  
      self.AccrualSegVal8:str = obj["AccrualSegVal8"]
      """  AccrualSegVal8  """  
      self.AccrualSegVal9:str = obj["AccrualSegVal9"]
      """  AccrualSegVal9  """  
      self.COASegAcct:str = obj["COASegAcct"]
      """  Chart of Accounts Segment Values Currency Accounts List.  """  
      self.GLGainAcctContext:str = obj["GLGainAcctContext"]
      """  GLGainAcctContext  """  
      self.GLLossAcctContext:str = obj["GLLossAcctContext"]
      """  GLLossAcctContext  """  
      self.NewCurrency:bool = obj["NewCurrency"]
      self.OverrideCurrency:bool = obj["OverrideCurrency"]
      self.OverrideRT:bool = obj["OverrideRT"]
      self.ReplaceCurrency:bool = obj["ReplaceCurrency"]
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatisticalOrd:bool = obj["StatisticalOrd"]
      """  Override statistical flag.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  StatUOMCode  """  
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

class Erp_Tablesets_NatAcctMassUpdateTableset:
   def __init__(self, obj):
      self.NatAcctMassUpdate:list[Erp_Tablesets_NatAcctMassUpdateRow] = obj["NatAcctMassUpdate"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class GetDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewParameters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["returnObj"]
      pass

class GetParamTaskDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class GetParamTaskDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["returnObj"]
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

class OnAnalysisCodeChange_input:
   """ Required : 
   AnalysisCd
   ds
   """  
   def __init__(self, obj):
      self.AnalysisCd:str = obj["AnalysisCd"]
      """  Analysis Code  """  
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class OnAnalysisCodeChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnCOACodeChanging_input:
   """ Required : 
   ipCOACode
   ds
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  Proposed COACode  """  
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class OnCOACodeChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnCOASegValuesChanging_input:
   """ Required : 
   ipCOACode
   ipSegmentNbr
   ipSegmentCode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      self.ipSegmentNbr:int = obj["ipSegmentNbr"]
      """  Segment number  """  
      self.ipSegmentCode:str = obj["ipSegmentCode"]
      """  Proposed Segment Value  """  
      pass

class OnCOASegValuesChanging_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class OnCategoryChanging_input:
   """ Required : 
   proposedCategory
   isReverse
   ds
   """  
   def __init__(self, obj):
      self.proposedCategory:str = obj["proposedCategory"]
      """  The proposed Category  """  
      self.isReverse:bool = obj["isReverse"]
      """  Is true if the Category combo is for the reverse category  """  
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class OnCategoryChanging_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class RunDirect_output:
   def __init__(self, obj):
      pass

class SaveDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
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

class ValidateCurrencyAccountType_input:
   """ Required : 
   ipCurrencyAcct
   CurrencyAcctType
   """  
   def __init__(self, obj):
      self.ipCurrencyAcct:bool = obj["ipCurrencyAcct"]
      """  Flag identifying the segment as a currency account  """  
      self.CurrencyAcctType:str = obj["CurrencyAcctType"]
      """  Currency Account Type  """  
      pass

class ValidateCurrencyAccountType_output:
   def __init__(self, obj):
      pass

class ValidateCurrencyAccounts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class ValidateCurrencyAccounts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateDefaultSegment_input:
   """ Required : 
   ipCOACode
   ipSubSegmentNbr
   ipSegmentCode
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      self.ipSubSegmentNbr:int = obj["ipSubSegmentNbr"]
      self.ipSegmentCode:str = obj["ipSegmentCode"]
      pass

class ValidateDefaultSegment_output:
   def __init__(self, obj):
      pass

class ValidateSubSegment_input:
   """ Required : 
   ipCOACode
   ipSubSegmentNbr
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      self.ipSubSegmentNbr:int = obj["ipSubSegmentNbr"]
      pass

class ValidateSubSegment_output:
   def __init__(self, obj):
      pass

class checkForNaturalAccountControl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

class checkForNaturalAccountControl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NatAcctMassUpdateTableset] = obj["ds"]
      pass

      """  output parameters  """  

