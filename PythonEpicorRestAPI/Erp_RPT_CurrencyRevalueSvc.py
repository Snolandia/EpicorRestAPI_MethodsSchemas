import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.RPT.CurrencyRevalueSvc
# Description: CurrencyRevalueSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CheckAP(epicorHeaders = None):
   """  
   Summary: Invoke method CheckAP
   Description: Provides a warning message if Accounts Payable is not set up to interface to
the General Ledger.
            
Example output:
"WARNING: A/P is NOT interfaced with General Ledger.  G/L transactions will NOT be created.  Do you wish to continue?"
   OperationID: CheckAP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_CheckAR(epicorHeaders = None):
   """  
   Summary: Invoke method CheckAR
   Description: Provides a warning message if Accounts Receivable is not set up to interface to
the General Ledger.
            
Example output:
"WARNING: A/R is NOT interfaced with General Ledger.  G/L transactions will NOT be created.  Do you wish to continue?"
   OperationID: CheckAR
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAR_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetApplyDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetApplyDate
   Description: Update Apply Date information based on the UseApplyDate changing.
   OperationID: GetApplyDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAPSortByList(epicorHeaders = None):
   """  
   Summary: Invoke method GetAPSortByList
   Description: Call this method to get the delimited list of valid values available for the
APSortyBy parameter.
   OperationID: GetAPSortByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAPSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetARSortByList(epicorHeaders = None):
   """  
   Summary: Invoke method GetARSortByList
   Description: Call this method to get the delimited list of valid values available for the
ARSortyBy parameter.
   OperationID: GetARSortByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetBASortByList(epicorHeaders = None):
   """  
   Summary: Invoke method GetBASortByList
   Description: Call this method to get the delimited list of valid values available for the
BASortyBy parameter.
   OperationID: GetBASortByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBASortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetTopLevelSortByList(epicorHeaders = None):
   """  
   Summary: Invoke method GetTopLevelSortByList
   Description: Call this method to get the delimited list of valid values available for the
sorting top level parameter.
   OperationID: GetTopLevelSortByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTopLevelSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetExchangeDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetExchangeDate
   Description: Update Exchange Date information based on the UseExchangeDate changing.
   OperationID: GetExchangeDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetExchangeDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExchangeDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPCDSordByList(epicorHeaders = None):
   """  
   Summary: Invoke method GetPCDSordByList
   Description: Call this method to get the delimited list of valid values available for the
PCDSortyBy parameter.
   OperationID: GetPCDSordByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCDSordByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetPOSortByList(epicorHeaders = None):
   """  
   Summary: Invoke method GetPOSortByList
   Description: Call this method to get the delimited list of valid values available for the
POSortyBy parameter.
   OperationID: GetPOSortByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPOSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetRevaluationOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRevaluationOption
   Description: Update the revaluation value based on the Override option changing.
   OperationID: GetRevaluationOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRevaluationOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRevaluationOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetReverseDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetReverseDate
   Description: Update Reverse Date based on Revalue Date, Apply Date, or UseApplyDate changing
   OperationID: GetReverseDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetReverseDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReverseDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSOSortByList(epicorHeaders = None):
   """  
   Summary: Invoke method GetSOSortByList
   Description: Call this method to get the delimited list of valid values available for the
SOSortyBy parameter.
   OperationID: GetSOSortByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSOSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_inOpenFiscalPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method inOpenFiscalPeriod
   OperationID: inOpenFiscalPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/inOpenFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/inOpenFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateRateTypeGrpSubs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateRateTypeGrpSubs
   Description: Call this method to check if RateTypeGrpSubs is valid
   OperationID: ValidateRateTypeGrpSubs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateRateTypeGrpSubs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRateTypeGrpSubs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCAllCurrenciesList(epicorHeaders = None):
   """  
   Summary: Invoke method GetCAllCurrenciesList
   Description: Call this method from Kinetic UI to load all Currencies
   OperationID: GetCAllCurrenciesList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCAllCurrenciesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetRptArchiveList(epicorHeaders = None):
   """  
   Summary: Invoke method GetRptArchiveList
   Description: Returns a sub-delimited list of valid archive codes/descriptions.
   OperationID: GetRptArchiveList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRptArchiveList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.CurrencyRevalueSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CheckAP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckAR_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_CurrencyRevalueParamRow:
   def __init__(self, obj):
      self.RevalueDate:str = obj["RevalueDate"]
      """  The currency revaluation process will perform revaluations up to and including the revalue date, but not after.  """  
      self.RevalueDateToken:str = obj["RevalueDateToken"]
      """  The currency revaluation process will perform revaluations up to and including the revalue date, but not after.  """  
      self.ARSortBy:str = obj["ARSortBy"]
      """  Sort options for Accounts Receivable invoices  """  
      self.APSortBy:str = obj["APSortBy"]
      """  Sort options for Accounts Payable invoices  """  
      self.BASortBy:str = obj["BASortBy"]
      """  Sort options for Bank Accounts  """  
      self.SOSortBy:str = obj["SOSortBy"]
      """  Sort options for Sales Orders  """  
      self.POSortBy:str = obj["POSortBy"]
      """  Sort options for Purchase Orders  """  
      self.NewPage:bool = obj["NewPage"]
      """  Indicates whether each area of the report should start on its own page. If this is the case, check this box.  """  
      self.CurrencyCodeList:str = obj["CurrencyCodeList"]
      """  A delimited list of CurrencyCodes to process.  The corresponding exchange rate for each currency is in the ExchangeRateList.  """  
      self.ReportOnly:bool = obj["ReportOnly"]
      """  When TRUE, this will only print a report, no database updates will take place.  """  
      self.Reverse:bool = obj["Reverse"]
      self.JournalCode:str = obj["JournalCode"]
      self.ARInvoice:bool = obj["ARInvoice"]
      """  If checked AR Invoice filter tab will be enabled  """  
      self.APInvoice:bool = obj["APInvoice"]
      """  If checked AP Invoice filter tab will be enabled  """  
      self.BankAcct:bool = obj["BankAcct"]
      """  If checked Bank Acct filter tab will be enabled  """  
      self.SO:bool = obj["SO"]
      """  If checked Sales Orders will be revaluated  """  
      self.PO:bool = obj["PO"]
      """  If checked Purchase Orders will be revaluated  """  
      self.ExchangeDate:str = obj["ExchangeDate"]
      """  Defaults to Revaluate Date  """  
      self.ApplyDate:str = obj["ApplyDate"]
      """  Defaults to RevalueDate  """  
      self.ApplyDateToken:str = obj["ApplyDateToken"]
      self.ReverseDate:str = obj["ReverseDate"]
      self.ARAcctList:str = obj["ARAcctList"]
      """  List of selected AR Accounts  """  
      self.APAcctList:str = obj["APAcctList"]
      """  List of AP Accounts selected  """  
      self.BankAcctList:str = obj["BankAcctList"]
      """  List of selected Bank Accounts  """  
      self.ExchangeDateToken:str = obj["ExchangeDateToken"]
      self.UseExchangeDate:bool = obj["UseExchangeDate"]
      self.UseApplyDate:bool = obj["UseApplyDate"]
      self.JrnlDescription:str = obj["JrnlDescription"]
      self.APGLCntrlType:str = obj["APGLCntrlType"]
      self.ARGLCntrlType:str = obj["ARGLCntrlType"]
      self.APGLDesc:str = obj["APGLDesc"]
      self.ARGLDesc:str = obj["ARGLDesc"]
      self.PIPSortBy:str = obj["PIPSortBy"]
      """  Sort options for Payment Instrument Payable  """  
      self.PIRSortBy:str = obj["PIRSortBy"]
      """  Sort options for Payment Instrument Receivable  """  
      self.PIP:bool = obj["PIP"]
      """  If checked Payment Instrument Payable filter tab will be enabled  """  
      self.PIR:bool = obj["PIR"]
      """  If checked Payment Instrument Receivable filter tab will be enabled  """  
      self.PIPAcctList:str = obj["PIPAcctList"]
      """  List of Payment Instrument Payable Accounts selected  """  
      self.PIRAcctList:str = obj["PIRAcctList"]
      """  List of Payment Instrument Receivable Accounts selected  """  
      self.PIPGLDesc:str = obj["PIPGLDesc"]
      self.PIRGLDesc:str = obj["PIRGLDesc"]
      self.PIPGLCntrlType:str = obj["PIPGLCntrlType"]
      self.PIRGLCntrlType:str = obj["PIRGLCntrlType"]
      self.APPrepayments:bool = obj["APPrepayments"]
      self.ARPrepayments:bool = obj["ARPrepayments"]
      self.PeriodEnd:bool = obj["PeriodEnd"]
      self.PCashDesk:bool = obj["PCashDesk"]
      """  If checked Petty Cash Desks filter tab will be enabled  """  
      self.PCashDeskList:str = obj["PCashDeskList"]
      """  List of selected Petty Cash Desks  """  
      self.PCDSortBy:str = obj["PCDSortBy"]
      """  Sort options for Petty Cash Desks  """  
      self.ReverseChange:bool = obj["ReverseChange"]
      """   Flag to define if change of Reverse Option is available for the users.
If Reverse is false only  AR Invoice and AP Invoice check boxes could  be checked.  """  
      self.OverrideRevalueAR:bool = obj["OverrideRevalueAR"]
      self.RevaluationAR:str = obj["RevaluationAR"]
      self.OverrideRevalueAP:bool = obj["OverrideRevalueAP"]
      self.RevaluationAP:str = obj["RevaluationAP"]
      self.OverrideRevalueBA:bool = obj["OverrideRevalueBA"]
      self.RevaluationBA:str = obj["RevaluationBA"]
      self.OverrideRevaluePCD:bool = obj["OverrideRevaluePCD"]
      self.RevaluationPCD:str = obj["RevaluationPCD"]
      self.RevaluationPIP:str = obj["RevaluationPIP"]
      self.RevaluationPIR:str = obj["RevaluationPIR"]
      self.BankAveRates:bool = obj["BankAveRates"]
      self.TopLevelSortBy:str = obj["TopLevelSortBy"]
      """  Top-Level Sort By:  """  
      self.CurrencyIncludeList:str = obj["CurrencyIncludeList"]
      """  A delimited list of CurrencyCodes to include in the report.Corresponding to base/ reporting currrencies.  """  
      self.PrintSelCriteria:bool = obj["PrintSelCriteria"]
      self.RateTypeGrpSubs:str = obj["RateTypeGrpSubs"]
      self.RateTypeGrpSubsDesc:str = obj["RateTypeGrpSubsDesc"]
      self.RevaluationBAUnrealized:bool = obj["RevaluationBAUnrealized"]
      self.RevaluationPCDUnrealized:bool = obj["RevaluationPCDUnrealized"]
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

class Erp_Tablesets_CurrencyRevalueTableset:
   def __init__(self, obj):
      self.CurrencyRevalueParam:list[Erp_Tablesets_CurrencyRevalueParamRow] = obj["CurrencyRevalueParam"]
      self.ReportStyle:list[Erp_Tablesets_ReportStyleRow] = obj["ReportStyle"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ReportStyleRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.ReportID:str = obj["ReportID"]
      """  Report ID  """  
      self.StyleNum:int = obj["StyleNum"]
      """  Report Style Number  """  
      self.StyleDescription:str = obj["StyleDescription"]
      """  Report Style Description  """  
      self.RptTypeID:str = obj["RptTypeID"]
      """  Foreign key to the ReportType table which defines the type of report (Crystal, EpiForms, etc)  """  
      self.PrintProgram:str = obj["PrintProgram"]
      """  Program which performs the actual printing  """  
      self.PrintProgramOptions:str = obj["PrintProgramOptions"]
      """  additonal options/settings required by specfic PrintProgram  """  
      self.RptDefID:str = obj["RptDefID"]
      """  Foreign Key to RptDef table.  """  
      self.CompanyList:str = obj["CompanyList"]
      """   Delimited list of company id's that can use this ReportStyle.
Blank = All Companies. This field will not be overlaid during release upgrades.
This field is not intended to be directly updatable. Instead it is exposed to the UI in a separate table (ReportCompany) which is not a physical db table. All Companies are created in ReportCompany. If in the CompanyList, then ReportCompany.ValidStyle = Yes
Delimeter character is global LIST-DELIM value  (~)  """  
      self.ServerNum:int = obj["ServerNum"]
      """  This is a Crystal Server Num that is defined in CrystalServer table.  """  
      self.OutputLocation:str = obj["OutputLocation"]
      """   Specifies an output location for Bartender and Outbound EDI Reports to override the default locations:
mfgsysdata\Bartender
mfgsysdata\EDI  """  
      self.OutputEDI:str = obj["OutputEDI"]
      """  Field to save if file is going to be exported in txt o xml format  """  
      self.SystemFlag:bool = obj["SystemFlag"]
      """  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  """  
      self.CGCCode:str = obj["CGCCode"]
      """  Country Group Code / Country Code for CSF  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RptCriteriaSetID:str = obj["RptCriteriaSetID"]
      """  RptCriteriaSetID  """  
      self.RptStructuredOutputDefID:str = obj["RptStructuredOutputDefID"]
      """  RptStructuredOutputDefID  """  
      self.StructuredOutputEnabled:bool = obj["StructuredOutputEnabled"]
      """  StructuredOutputEnabled  """  
      self.RequireSubmissionID:bool = obj["RequireSubmissionID"]
      """  RequireSubmissionID  """  
      self.AllowResetAfterSubmit:bool = obj["AllowResetAfterSubmit"]
      """  AllowResetAfterSubmit  """  
      self.CertificateID:str = obj["CertificateID"]
      """  CertificateID  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Language  """  
      self.FormatCulture:str = obj["FormatCulture"]
      """  Culture Format  """  
      self.StructuredOutputCertificateID:str = obj["StructuredOutputCertificateID"]
      """  StructuredOutputCertificateID  """  
      self.StructuredOutputAlgorithm:str = obj["StructuredOutputAlgorithm"]
      """  StructuredOutputAlgorithm  """  
      self.HasBAQOrEI:bool = obj["HasBAQOrEI"]
      """  True if any data source for this report data definition is related to a BAQ or EI. False in other case.  """  
      self.RoutingRuleEnabled:bool = obj["RoutingRuleEnabled"]
      """  Flag to indicate if this report style record has an enabled routing rule.  """  
      self.CertificateIsAllComp:bool = obj["CertificateIsAllComp"]
      """  Digital cert for signing is an All Company cert.  """  
      self.CertificateIsSystem:bool = obj["CertificateIsSystem"]
      """  Indicates the certificate is a system cert.  """  
      self.CertExpiration:str = obj["CertExpiration"]
      """  Certificate expiration date.  """  
      self.Status:int = obj["Status"]
      """  Report Style status (from HealthCheck).It indicates if there are issues in the report style: 0 - OK, 1 - Missing RDL, etc.  """  
      self.StatusMessage:str = obj["StatusMessage"]
      """  Report Style status message (from HealthCheck).It is a more detailed message with  issues found, ie. the names of the missing RDL files.  """  
      self.RptDefSystemFlag:bool = obj["RptDefSystemFlag"]
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.IsBAQReport:bool = obj["IsBAQReport"]
      self.StructuredOutputCertificateIsAllComp:bool = obj["StructuredOutputCertificateIsAllComp"]
      self.StructuredOutputCertificateIsSystem:bool = obj["StructuredOutputCertificateIsSystem"]
      self.StructuredOutputCertificateExpirationDate:str = obj["StructuredOutputCertificateExpirationDate"]
      self.AllowGenerateEDI:bool = obj["AllowGenerateEDI"]
      self.BitFlag:int = obj["BitFlag"]
      self.ReportRptDescription:str = obj["ReportRptDescription"]
      self.RptDefRptDescription:str = obj["RptDefRptDescription"]
      self.RptTypeRptTypeDescription:str = obj["RptTypeRptTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAPSortByList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetARSortByList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetApplyDate_input:
   """ Required : 
   ds
   lUseApplyDateOn
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
      self.lUseApplyDateOn:bool = obj["lUseApplyDateOn"]
      """  Flag to indicate if ApplyDate will be cleared or set  """  
      pass

class GetApplyDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetBASortByList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCAllCurrenciesList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.currCodeList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
      pass

class GetDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetExchangeDate_input:
   """ Required : 
   ds
   lUseExchangeDateOn
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
      self.lUseExchangeDateOn:bool = obj["lUseExchangeDateOn"]
      """  Flag to indicate if ExchangeDate will be cleared or set  """  
      pass

class GetExchangeDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewParameters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["returnObj"]
      pass

class GetPCDSordByList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPOSortByList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetParamTaskDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
      pass

class GetParamTaskDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["returnObj"]
      pass

class GetRevaluationOption_input:
   """ Required : 
   ds
   lOverride
   cOption
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
      self.lOverride:bool = obj["lOverride"]
      """  Flag to indicate if the revaluation option is overridden  """  
      self.cOption:str = obj["cOption"]
      """  Indicates which option the override was changed for  """  
      pass

class GetRevaluationOption_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetReverseDate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
      pass

class GetReverseDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRptArchiveList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetSOSortByList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcList:str = obj["parameters"]
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

class GetTopLevelSortByList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcList:str = obj["parameters"]
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
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
      pass

class RunDirect_output:
   def __init__(self, obj):
      pass

class SaveDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_CurrencyRevalueTableset] = obj["ds"]
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

class ValidateRateTypeGrpSubs_input:
   """ Required : 
   RateTypeGrpSubs
   """  
   def __init__(self, obj):
      self.RateTypeGrpSubs:str = obj["RateTypeGrpSubs"]
      """  RateTypeGrpSubs parameter  """  
      pass

class ValidateRateTypeGrpSubs_output:
   def __init__(self, obj):
      pass

class inOpenFiscalPeriod_input:
   """ Required : 
   id_RevalueDate
   """  
   def __init__(self, obj):
      self.id_RevalueDate:str = obj["id_RevalueDate"]
      pass

class inOpenFiscalPeriod_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pcMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

