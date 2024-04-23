import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GLTrackerSvc
# Description: GL Account Period Balance for Tracker
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(vBookID, vBalanceType, vUseCarryFwdBal, sBalanceAcct, fiscalYear, fiscalYearSuffix, budgetCodeID, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This method replaces the standard GetRows method
   OperationID: Get_GetRows
      :param vBookID: Desc: Book ID   Required: True   Allow empty value : True
      :param vBalanceType: Desc: Balance Type P or T   Required: True   Allow empty value : True
      :param vUseCarryFwdBal: Desc: Use Carry Forward Balance   Required: True
      :param sBalanceAcct: Desc: Balance Account   Required: True   Allow empty value : True
      :param fiscalYear: Desc: Fiscal Year   Required: True
      :param fiscalYearSuffix: Desc: Fiscal Year Suffix   Required: True   Allow empty value : True
      :param budgetCodeID: Desc: Fiscal Year Suffix   Required: True   Allow empty value : True
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
   params += "vBookID=" + vBookID
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "vBalanceType=" + vBalanceType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "vUseCarryFwdBal=" + vUseCarryFwdBal
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "sBalanceAcct=" + sBalanceAcct
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalYear=" + fiscalYear
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fiscalYearSuffix=" + fiscalYearSuffix
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "budgetCodeID=" + budgetCodeID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetByIDBalanceAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByIDBalanceAccount
   Description: Performs a GLAcctDspSvc.GetByID of the GLAccount based on the balance type.
   OperationID: GetByIDBalanceAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByIDBalanceAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDBalanceAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultChartTrackerFilters(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultChartTrackerFilters
   Description: Get the default Chart Tracker filters
   OperationID: GetDefaultChartTrackerFilters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultChartTrackerFilters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetFiscalPerDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFiscalPerDate
   OperationID: GetFiscalPerDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFiscalPerDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalPerDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFiscalPeriods(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFiscalPeriods
   OperationID: GetFiscalPeriods
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFiscalPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFiscalYear
   OperationID: GetFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultBudgetCode(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultBudgetCode
   Description: Get default BudgetCode
   OperationID: GetDefaultBudgetCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultBudgetCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetFiscalYearSuffix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFiscalYearSuffix
   Description: Returns the Current Fiscal Year Suffix
   OperationID: GetFiscalYearSuffix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFiscalYearSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFiscalYearSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJournalHeaderComments(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJournalHeaderComments
   Description: Returns GL Journal header comments.
   OperationID: GetJournalHeaderComments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJournalHeaderComments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournalHeaderComments_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsSpecificGLAccount(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsSpecificGLAccount
   Description: This method overloads GetRows method
   OperationID: GetRowsSpecificGLAccount
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsSpecificGLAccount_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsSpecificGLAccount_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCurrBal(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCurrBal
   Description: Get currency balance rows for specified balance account.
   OperationID: GetRowsCurrBal
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCurrBal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCurrBal_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsCurrBalWithOpeningBalance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsCurrBalWithOpeningBalance
   OperationID: GetRowsCurrBalWithOpeningBalance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsCurrBalWithOpeningBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsCurrBalWithOpeningBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsGLAccountList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsGLAccountList
   Description: Invokes GetRowsMultiple using a delimited list of GL accounts
   OperationID: GetRowsGLAccountList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsGLAccountList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsGLAccountList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsMultiple(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsMultiple
   Description: This method gets all the rows for a group of glaccounts specified GLAccount table
   OperationID: GetRowsMultiple
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBookID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBookID
   Description: On change of BookID
   OperationID: OnChangeBookID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBudgetCodeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBudgetCodeID
   Description: On change of BudgetCodeID
   OperationID: OnChangeBudgetCodeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBudgetCodeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBudgetCodeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFiscalYear
   Description: On change of FiscalYear
   OperationID: OnChangeFiscalYear
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFiscalYearSuffix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFiscalYearSuffix
   Description: On change of FiscalYearSuffix
   OperationID: OnChangeFiscalYearSuffix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFiscalYearSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFiscalYearSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeStartEndDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeStartEndDate
   Description: On change of StartDate or EndDate
   OperationID: OnChangeStartEndDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeStartEndDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeStartEndDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeStartEndPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeStartEndPeriod
   Description: On change of StartPeriod or EndPeriod
   OperationID: OnChangeStartEndPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeStartEndPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeStartEndPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFiscalPerDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFiscalPerDate
   Description: Returns the Fiscal Year periods
   OperationID: ValidateFiscalPerDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFiscalPerDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalPerDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFiscalPeriod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFiscalPeriod
   Description: Validate the Fiscal Period
   OperationID: ValidateFiscalPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFiscalYearSuffix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFiscalYearSuffix
   Description: Validate the Fiscal Year Suffix
   OperationID: ValidateFiscalYearSuffix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFiscalYearSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFiscalYearSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFiscalYear(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFiscalYear
   Description: Validate the Fiscal Year
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateBudgetCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateBudgetCode
   Description: Validate Budget Code
   OperationID: ValidateBudgetCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateBudgetCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBudgetCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetBalAcctFromGlAcct(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetBalAcctFromGlAcct
   Description: Get Balance Accounts
   OperationID: GetBalAcctFromGlAcct
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetBalAcctFromGlAcct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBalAcctFromGlAcct_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateSiteFilter(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateSiteFilter
   Description: Creates siteFilter query based on selected Sites and allowed sites
   OperationID: GenerateSiteFilter
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateSiteFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateSiteFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSiteFilterAndText(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSiteFilterAndText
   Description: Gets site filter string for record retrieval and sites selected text
   OperationID: GetSiteFilterAndText
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSiteFilterAndText_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSiteFilterAndText_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGLTrackerSites(epicorHeaders = None):
   """  
   Summary: Invoke method GetGLTrackerSites
   Description: Returns Sites that can be selected for filtering tracker results
   OperationID: GetGLTrackerSites
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGLTrackerSites_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GLTrackerSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_ChartTrackerFiltersRow:
   def __init__(self, obj):
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.StartPeriod:int = obj["StartPeriod"]
      self.EndPeriod:int = obj["EndPeriod"]
      self.StartDate:str = obj["StartDate"]
      self.EndDate:str = obj["EndDate"]
      self.BookID:str = obj["BookID"]
      self.BookIDDesc:str = obj["BookIDDesc"]
      self.COACode:str = obj["COACode"]
      self.BalanceType:str = obj["BalanceType"]
      """  Balance Type of either Detailed Balances or Summary Balances  """  
      self.UseCarryFwdBal:bool = obj["UseCarryFwdBal"]
      self.UseCarryFwdBalTotal:bool = obj["UseCarryFwdBalTotal"]
      self.UseCarryFwdBalCurr:bool = obj["UseCarryFwdBalCurr"]
      self.BookCurrencyCode:str = obj["BookCurrencyCode"]
      self.BookCurrencyDesc:str = obj["BookCurrencyDesc"]
      self.TransCurrencyCode:str = obj["TransCurrencyCode"]
      self.TransCurrencyDesc:str = obj["TransCurrencyDesc"]
      self.BudgetCodeID:str = obj["BudgetCodeID"]
      self.BudgetCodeDesc:str = obj["BudgetCodeDesc"]
      self.GLAccount:str = obj["GLAccount"]
      self.GLAccountList:str = obj["GLAccountList"]
      """  List of GL Accounts separated by tilde  """  
      self.CurrentFiscalYear:int = obj["CurrentFiscalYear"]
      """  The current fiscal year  """  
      self.JournalCode:str = obj["JournalCode"]
      self.JournalCodeList:str = obj["JournalCodeList"]
      """  List of Journal Codes separated by tilde  """  
      self.SiteList:str = obj["SiteList"]
      self.SiteFilter:str = obj["SiteFilter"]
      """  Calculated filter based on selected Sites. This is partial SQL where clause.  """  
      self.SiteIsLegalEntity:bool = obj["SiteIsLegalEntity"]
      """  Setting from XbSyst datatable.  """  
      self.BookContainsSiteSegment:bool = obj["BookContainsSiteSegment"]
      """  Determine it current filter book contains site segment  """  
      self.SitesSelectedText:str = obj["SitesSelectedText"]
      """  Text indicating what sites are selected  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ChartTrackerFiltersTableset:
   def __init__(self, obj):
      self.ChartTrackerFilters:list[Erp_Tablesets_ChartTrackerFiltersRow] = obj["ChartTrackerFilters"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CurrOpenBalRow:
   def __init__(self, obj):
      self.CYOpenBBookC:int = obj["CYOpenBBookC"]
      """  Current Year Opening Balance Book Currency  """  
      self.CYOpenBTranC:int = obj["CYOpenBTranC"]
      """  Current Year Opening Balance Transaction Currency  """  
      self.CurrencyBook:str = obj["CurrencyBook"]
      """  Currency Book  """  
      self.CurrencyTran:str = obj["CurrencyTran"]
      """  Currency Transaction  """  
      self.GLAccount:str = obj["GLAccount"]
      """  GLAccount  """  
      self.CYOpenBalance:int = obj["CYOpenBalance"]
      """  Current Year Opening Balance  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAccountTrackerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.SegValue1:str = obj["SegValue1"]
      self.SegValue2:str = obj["SegValue2"]
      self.SegValue3:str = obj["SegValue3"]
      self.SegValue4:str = obj["SegValue4"]
      self.SegValue5:str = obj["SegValue5"]
      self.SegValue6:str = obj["SegValue6"]
      self.SegValue7:str = obj["SegValue7"]
      self.SegValue8:str = obj["SegValue8"]
      self.SegValue9:str = obj["SegValue9"]
      self.SegValue10:str = obj["SegValue10"]
      self.SegValue11:str = obj["SegValue11"]
      self.SegValue12:str = obj["SegValue12"]
      self.SegValue13:str = obj["SegValue13"]
      self.SegValue14:str = obj["SegValue14"]
      self.SegValue15:str = obj["SegValue15"]
      self.SegValue16:str = obj["SegValue16"]
      self.SegValue17:str = obj["SegValue17"]
      self.SegValue18:str = obj["SegValue18"]
      self.SegValue19:str = obj["SegValue19"]
      self.SegValue20:str = obj["SegValue20"]
      self.BalanceType:str = obj["BalanceType"]
      self.BookID:str = obj["BookID"]
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.GLAccount:str = obj["GLAccount"]
      self.GLAcctDisp:str = obj["GLAcctDisp"]
      self.AccountDesc:str = obj["AccountDesc"]
      self.CategoryDesc:str = obj["CategoryDesc"]
      self.NormalBalDesc:str = obj["NormalBalDesc"]
      self.CanUseCarryFwdBal:bool = obj["CanUseCarryFwdBal"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLAccountTrackerTableset:
   def __init__(self, obj):
      self.GLAccountTracker:list[Erp_Tablesets_GLAccountTrackerRow] = obj["GLAccountTracker"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLTrackerCurrBalRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.DocCurrency:str = obj["DocCurrency"]
      """  A unique code that identifies the document currency.  """  
      self.CurrBalAcct:str = obj["CurrBalAcct"]
      """  The GL Account used to record balances.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  the fiscal period's number in the fiscal year.  """  
      self.SegValue1:str = obj["SegValue1"]
      """  SegmentValue 1.  See COASegment segment number 1 for a description of this field.  This is the natural account.  """  
      self.SegValue2:str = obj["SegValue2"]
      """  SegmentValue 2.  See COASegment segment number 2 for a description of this field.  """  
      self.SegValue3:str = obj["SegValue3"]
      """  SegmentValue 3.  See COASegment segment number 3 for a description of this field.  """  
      self.SegValue4:str = obj["SegValue4"]
      """  SegmentValue 4.  See COASegment segment number 4 for a description of this field.  """  
      self.SegValue5:str = obj["SegValue5"]
      """  SegmentValue 5.  See COASegment segment number 5 for a description of this field.  """  
      self.SegValue6:str = obj["SegValue6"]
      """  SegmentValue 6.  See COASegment segment number 6 for a description of this field.  """  
      self.SegValue7:str = obj["SegValue7"]
      """  SegmentValue 7.  See COASegment segment number 7 for a description of this field.  """  
      self.SegValue8:str = obj["SegValue8"]
      """  SegmentValue 8.  See COASegment segment number 8 for a description of this field.  """  
      self.SegValue9:str = obj["SegValue9"]
      """  SegmentValue 9.  See COASegment segment number 9 for a description of this field.  """  
      self.SegValue10:str = obj["SegValue10"]
      """  SegmentValue 10.  See COASegment segment number 10 for a description of this field.  """  
      self.SegValue11:str = obj["SegValue11"]
      """  SegmentValue 11.  See COASegment segment number 11 for a description of this field.  """  
      self.SegValue12:str = obj["SegValue12"]
      """  SegmentValue 12.  See COASegment segment number 12 for a description of this field.  """  
      self.SegValue13:str = obj["SegValue13"]
      """  SegmentValue 13.  See COASegment segment number 13 for a description of this field.  """  
      self.SegValue14:str = obj["SegValue14"]
      """  SegmentValue 14.  See COASegment segment number 14 for a description of this field.  """  
      self.SegValue15:str = obj["SegValue15"]
      """  SegmentValue 15.  See COASegment segment number 15 for a description of this field.  """  
      self.SegValue16:str = obj["SegValue16"]
      """  SegmentValue 16.  See COASegment segment number 16 for a description of this field.  """  
      self.SegValue17:str = obj["SegValue17"]
      """  SegmentValue 17.  See COASegment segment number 17 for a description of this field.  """  
      self.SegValue18:str = obj["SegValue18"]
      """  SegmentValue 18.  See COASegment segment number 18 for a description of this field.  """  
      self.SegValue19:str = obj["SegValue19"]
      """  SegmentValue 19.  See COASegment segment number 19 for a description of this field.  """  
      self.SegValue20:str = obj["SegValue20"]
      """  SegmentValue 20.  See COASegment segment number 20 for a description of this field.  """  
      self.DocDebitAmt:int = obj["DocDebitAmt"]
      """  Total debit amount that has been posted to the account for a specific fisccal year/period.  This is in document currency.  """  
      self.DocCreditAmt:int = obj["DocCreditAmt"]
      """  Total Credit amount that has been posted to the account for a specific fiscal year/period.  This is in document currency.  """  
      self.BaseDebitAmt:int = obj["BaseDebitAmt"]
      """  Total debit amount that has been posted to the account for a specific fisccal year/period.  This is in base currency.  """  
      self.BaseCreditAmt:int = obj["BaseCreditAmt"]
      """  Total Credit amount that has been posted to the account for a specific fiscal year/period.  This is in base currency.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseOpenBal:int = obj["BaseOpenBal"]
      """  Base Opening Balance  """  
      self.DocOpenBal:int = obj["DocOpenBal"]
      """  Doc Opening Balance  """  
      self.BaseRunningBal:int = obj["BaseRunningBal"]
      """  Base Running Balance  """  
      self.DocRunningBal:int = obj["DocRunningBal"]
      """  Doc Running Balance  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLTrackerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this record.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of the balance record.  """  
      self.DebitAmt:int = obj["DebitAmt"]
      """  The Total Debit amount that has been posted to the account for a specific fiscal year/period.  Created from GLPeriodBal.DebitAmt.  """  
      self.CreditAmt:int = obj["CreditAmt"]
      """  The Total Credit amount that has been posted to the account for a specific fiscal year/period.  Created from GLPeriodBal.CreditAmt.  Note the negative sign has been removed for display purposes.  """  
      self.CYBalance:int = obj["CYBalance"]
      """  Current Year Account Balance.  A sum of opening balance plus all the period activity for the fiscal year up to and including the period defined by this record.  """  
      self.CPBudget:int = obj["CPBudget"]
      """  Current Fiscal period Budget amount.  Created from GLBudgetDtl.BudgetAmt.  """  
      self.CYBudget:int = obj["CYBudget"]
      """  The Current Year Account Budget Balance.  Holds the total budgeted amount for the fiscal year up to and including the period defined by this record. This is an accumulation of GLBudgetDtl.BudgetAmt.  """  
      self.CPBudgetPct:int = obj["CPBudgetPct"]
      """  Current period percent of budget.  Calculated as (GLPeriodBal.DebitAmt + CreditAmt) / GLBudgetDtl.BudgetAmt.  """  
      self.CYBudgetPct:int = obj["CYBudgetPct"]
      """  Current Year Account Balance percent of budget.  Calculated as CurYrBalance / CurYrBudget.  """  
      self.PYCPAmt:int = obj["PYCPAmt"]
      """  The Prior fiscal years transaction activity summary amount for the specific fiscal period defined by this record.  A sum GLPeriodBal.DebitAmt + CreditAmt.  """  
      self.PYBalance:int = obj["PYBalance"]
      """  Current Year Account Balance.  A sum of opening balance plus all the period activity for the fiscal year up to and including the period defined by this record.  """  
      self.PYCPPct:int = obj["PYCPPct"]
      """  The Current fiscal period to prior year fiscal period amount comparative percentage.  Calculated as (GLPeriodBal.DebitAmt + CreditAmt) / PYCPAmt.  """  
      self.PYPct:int = obj["PYPct"]
      """  Current years balance to prior years balance comparative percent.  Calculated as CYBalance / PYBalance.  """  
      self.BookID:str = obj["BookID"]
      """  Unique Book Identifier  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CPStatBudget:int = obj["CPStatBudget"]
      """  Current Fiscal period Budget Statistical amount.  Created from GLBudgetDtl.BudgetStatAmt.  """  
      self.CYStatBudget:int = obj["CYStatBudget"]
      """  The Current Year Account Budget Statistical Balance.  Holds the total budgeted amount for the fiscal year up to and including the period defined by this record. This is an accumulation of GLBudgetDtl.BudgetStatAmt.  """  
      self.CPStatBudgetPct:int = obj["CPStatBudgetPct"]
      """  Current period percent of statisctical budget.  Calculated as (GLPeriodBal.DebitStatAmt + CreditStatAmt) / GLBudgetDtl.BudgetStatAmt.  """  
      self.CYStatBudgetPct:int = obj["CYStatBudgetPct"]
      """  Current Year Account Balance percent of statistical budget.  Calculated as CurYrStatBalance / CurYrStatBudget.  """  
      self.CYOpenBalance:int = obj["CYOpenBalance"]
      """  Current Year Opening Balance  """  
      self.GLAccount:str = obj["GLAccount"]
      self.SegValue1:str = obj["SegValue1"]
      self.SegValue2:str = obj["SegValue2"]
      self.SegValue3:str = obj["SegValue3"]
      self.SegValue4:str = obj["SegValue4"]
      self.SegValue5:str = obj["SegValue5"]
      self.SegValue6:str = obj["SegValue6"]
      self.SegValue7:str = obj["SegValue7"]
      self.SegValue8:str = obj["SegValue8"]
      self.SegValue9:str = obj["SegValue9"]
      self.SegValue10:str = obj["SegValue10"]
      self.SegValue11:str = obj["SegValue11"]
      self.SegValue12:str = obj["SegValue12"]
      self.SegValue13:str = obj["SegValue13"]
      self.SegValue14:str = obj["SegValue14"]
      self.SegValue15:str = obj["SegValue15"]
      self.SegValue16:str = obj["SegValue16"]
      self.SegValue17:str = obj["SegValue17"]
      self.SegValue18:str = obj["SegValue18"]
      self.SegValue19:str = obj["SegValue19"]
      self.SegValue20:str = obj["SegValue20"]
      self.COACode:str = obj["COACode"]
      """  COA Code  """  
      self.PeriodStartDate:str = obj["PeriodStartDate"]
      self.PeriodEndDate:str = obj["PeriodEndDate"]
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CYStatBalance:int = obj["CYStatBalance"]
      self.PYStatBalance:int = obj["PYStatBalance"]
      self.StatAmount:int = obj["StatAmount"]
      self.StatUOMDesc:str = obj["StatUOMDesc"]
      self.PYCPStatAmt:int = obj["PYCPStatAmt"]
      """  The Prior fiscal years transaction activity summary statistical amount for the specific fiscal period defined by this record.  A sum GLPeriodBal.DebitStatAmt + CreditStatAmt.  """  
      self.PYStatPct:int = obj["PYStatPct"]
      """  Current years statistical balance to prior years statistical balance comparative percent.  Calculated as CYStatBalance / PYStatBalance.  """  
      self.PYCPStatPct:int = obj["PYCPStatPct"]
      """  The Current fiscal period to prior year fiscal period statistical amount comparative percentage.  Calculated as (GLPeriodBal.DebitStatAmt + CreditStatAmt) / PYCPStatAmt.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLTrackerSitesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Name:str = obj["Name"]
      self.Plant:str = obj["Plant"]
      self.Selected:bool = obj["Selected"]
      """  Row is selected  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GLTrackerSitesTableset:
   def __init__(self, obj):
      self.GLTrackerSites:list[Erp_Tablesets_GLTrackerSitesRow] = obj["GLTrackerSites"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLTrackerTableset:
   def __init__(self, obj):
      self.GLTracker:list[Erp_Tablesets_GLTrackerRow] = obj["GLTracker"]
      self.CurrOpenBal:list[Erp_Tablesets_CurrOpenBalRow] = obj["CurrOpenBal"]
      self.GLTrackerCurrBal:list[Erp_Tablesets_GLTrackerCurrBalRow] = obj["GLTrackerCurrBal"]
      self.GLTrackerTotals:list[Erp_Tablesets_GLTrackerTotalsRow] = obj["GLTrackerTotals"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_GLTrackerTotalsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """  The fiscal year of this record.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """  Fiscal period of the balance record.  """  
      self.DebitAmt:int = obj["DebitAmt"]
      """  The Total Debit amount that has been posted to the account for a specific fiscal year/period.  Created from GLPeriodBal.DebitAmt.  """  
      self.CreditAmt:int = obj["CreditAmt"]
      """  The Total Credit amount that has been posted to the account for a specific fiscal year/period.  Created from GLPeriodBal.CreditAmt.  Note the negative sign has been removed for display purposes.  """  
      self.CYBalance:int = obj["CYBalance"]
      """  Current Year Account Balance.  A sum of opening balance plus all the period activity for the fiscal year up to and including the period defined by this record.  """  
      self.CPBudget:int = obj["CPBudget"]
      """  Current Fiscal period Budget amount.  Created from GLBudgetDtl.BudgetAmt.  """  
      self.CYBudget:int = obj["CYBudget"]
      """  The Current Year Account Budget Balance.  Holds the total budgeted amount for the fiscal year up to and including the period defined by this record. This is an accumulation of GLBudgetDtl.BudgetAmt.  """  
      self.CPBudgetPct:int = obj["CPBudgetPct"]
      """  Current period percent of budget.  Calculated as (GLPeriodBal.DebitAmt + CreditAmt) / GLBudgetDtl.BudgetAmt.  """  
      self.CYBudgetPct:int = obj["CYBudgetPct"]
      """  Current Year Account Balance percent of budget.  Calculated as CurYrBalance / CurYrBudget.  """  
      self.PYCPAmt:int = obj["PYCPAmt"]
      """  The Prior fiscal years transaction activity summary amount for the specific fiscal period defined by this record.  A sum GLPeriodBal.DebitAmt + CreditAmt.  """  
      self.PYBalance:int = obj["PYBalance"]
      """  Current Year Account Balance.  A sum of opening balance plus all the period activity for the fiscal year up to and including the period defined by this record.  """  
      self.PYCPPct:int = obj["PYCPPct"]
      """  The Current fiscal period to prior year fiscal period amount comparative percentage.  Calculated as (GLPeriodBal.DebitAmt + CreditAmt) / PYCPAmt.  """  
      self.PYPct:int = obj["PYPct"]
      """  Current years balance to prior years balance comparative percent.  Calculated as CYBalance / PYBalance.  """  
      self.Statistical:int = obj["Statistical"]
      """   Identifies if statistical information may be entered for the natural (chart) account.
Accounts can be used only for monetary amounts, both monetary and statistical amounts or only for statistical amounts.
0 = Only used for monetary amounts.
1 = Used for both monetary and statistical amounts.
2 = Only used for statistical amounts.  """  
      self.StatUOMCode:str = obj["StatUOMCode"]
      """  Statistical UOM code.  """  
      self.DebitStatAmt:int = obj["DebitStatAmt"]
      """  This field shows Debit statistical amount.  """  
      self.CreditStatAmt:int = obj["CreditStatAmt"]
      """  This field shows Credit statistical amount.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CPStatBudget:int = obj["CPStatBudget"]
      """  Current Fiscal period Budget Statistical amount.  Created from GLBudgetDtl.BudgetStatAmt.  """  
      self.CYStatBudget:int = obj["CYStatBudget"]
      """  The Current Year Account Budget Statistical Balance.  Holds the total budgeted amount for the fiscal year up to and including the period defined by this record. This is an accumulation of GLBudgetDtl.BudgetStatAmt.  """  
      self.CPStatBudgetPct:int = obj["CPStatBudgetPct"]
      """  Current period percent of statisctical budget.  Calculated as (GLPeriodBal.DebitStatAmt + CreditStatAmt) / GLBudgetDtl.BudgetStatAmt.  """  
      self.CYStatBudgetPct:int = obj["CYStatBudgetPct"]
      """  Current Year Account Balance percent of statistical budget.  Calculated as CurYrStatBalance / CurYrStatBudget.  """  
      self.CYOpenBalance:int = obj["CYOpenBalance"]
      """  Current Year Opening Balance  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.CYStatBalance:int = obj["CYStatBalance"]
      self.PYStatBalance:int = obj["PYStatBalance"]
      self.StatAmount:int = obj["StatAmount"]
      self.StatUOMDesc:str = obj["StatUOMDesc"]
      self.PYCPStatAmt:int = obj["PYCPStatAmt"]
      """  The Prior fiscal years transaction activity summary statistical amount for the specific fiscal period defined by this record.  A sum GLPeriodBal.DebitStatAmt + CreditStatAmt.  """  
      self.PYStatPct:int = obj["PYStatPct"]
      """  Current years statistical balance to prior years statistical balance comparative percent.  Calculated as CYStatBalance / PYStatBalance.  """  
      self.PYCPStatPct:int = obj["PYCPStatPct"]
      """  The Current fiscal period to prior year fiscal period statistical amount comparative percentage.  Calculated as (GLPeriodBal.DebitStatAmt + CreditStatAmt) / PYCPStatAmt.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GenerateSiteFilter_input:
   """ Required : 
   bookID
   siteList
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.siteList:str = obj["siteList"]
      pass

class GenerateSiteFilter_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetBalAcctFromGlAcct_input:
   """ Required : 
   ipCOACode
   ipGLAccount
   """  
   def __init__(self, obj):
      self.ipCOACode:str = obj["ipCOACode"]
      """  COA Code  """  
      self.ipGLAccount:str = obj["ipGLAccount"]
      """  GL Row  """  
      pass

class GetBalAcctFromGlAcct_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outPerBalAcct:str = obj["parameters"]
      self.outTBBalAcct:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByIDBalanceAccount_input:
   """ Required : 
   coaCode
   balanceType
   glAccountList
   ds
   """  
   def __init__(self, obj):
      self.coaCode:str = obj["coaCode"]
      self.balanceType:str = obj["balanceType"]
      self.glAccountList:str = obj["glAccountList"]
      """  Tilde separated list of GL Accounts  """  
      self.ds:list[Erp_Tablesets_GLAccountTrackerTableset] = obj["ds"]
      pass

class GetByIDBalanceAccount_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLAccountTrackerTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetDefaultBudgetCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outBudgetCodeID:str = obj["parameters"]
      self.outBudgetCodeDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDefaultChartTrackerFilters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["returnObj"]
      pass

class GetFiscalPerDate_input:
   """ Required : 
   ipBookID
   ipFiscalYear
   ipFiscalYearSuffix
   ipFiscalPeriod
   ipStartOrEndDate
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      self.ipFiscalPeriod:int = obj["ipFiscalPeriod"]
      self.ipStartOrEndDate:str = obj["ipStartOrEndDate"]
      pass

class GetFiscalPerDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFiscalPerDate:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFiscalPeriods_input:
   """ Required : 
   ipBookID
   ipFiscalYear
   ipFiscalYearSuffix
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      pass

class GetFiscalPeriods_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opFiscalPerStart:int = obj["parameters"]
      self.opFiscalPerEnd:int = obj["parameters"]
      self.opStartDate:str = obj["parameters"]
      self.opEndDate:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFiscalYearSuffix_input:
   """ Required : 
   vBookID
   vFiscalYear
   """  
   def __init__(self, obj):
      self.vBookID:str = obj["vBookID"]
      """  Book ID if not specified values will be based on Company.FiscalCalendarID"  """  
      self.vFiscalYear:int = obj["vFiscalYear"]
      """  Current Fiscal Year  """  
      pass

class GetFiscalYearSuffix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outFiscalYearSuffix:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFiscalYear_input:
   """ Required : 
   vBookID
   """  
   def __init__(self, obj):
      self.vBookID:str = obj["vBookID"]
      pass

class GetFiscalYear_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.outFiscalCalendarID:str = obj["parameters"]
      self.outFiscalYear:int = obj["parameters"]
      self.outFiscalYearSuffix:str = obj["parameters"]
      self.outFiscalPeriod:int = obj["parameters"]
      self.outStartDate:str = obj["parameters"]
      self.outEndDate:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetGLTrackerSites_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLTrackerSitesTableset] = obj["returnObj"]
      pass

class GetJournalHeaderComments_input:
   """ Required : 
   ipBookID
   ipJournalCode
   ipFiscalYear
   ipFiscalYearSuffix
   ipJournalNum
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID value  """  
      self.ipJournalCode:str = obj["ipJournalCode"]
      """  Journal Code  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Current Fiscal Year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  Current Fiscal Year Suffix  """  
      self.ipJournalNum:int = obj["ipJournalNum"]
      """  Journal number  """  
      pass

class GetJournalHeaderComments_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opCommentText:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetRowsCurrBalWithOpeningBalance_input:
   """ Required : 
   vBookID
   vBalanceType
   vTransCurrencyCode
   vUseCarryFwdBal
   sBalanceAcct
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.vBookID:str = obj["vBookID"]
      self.vBalanceType:str = obj["vBalanceType"]
      self.vTransCurrencyCode:str = obj["vTransCurrencyCode"]
      self.vUseCarryFwdBal:bool = obj["vUseCarryFwdBal"]
      self.sBalanceAcct:str = obj["sBalanceAcct"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      pass

class GetRowsCurrBalWithOpeningBalance_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLTrackerTableset] = obj["returnObj"]
      pass

class GetRowsCurrBal_input:
   """ Required : 
   vBookID
   vTransCurrencyCode
   vUseCarryFwdBal
   sBalanceAcct
   fiscalYear
   fiscalYearSuffix
   """  
   def __init__(self, obj):
      self.vBookID:str = obj["vBookID"]
      """  Book ID  """  
      self.vTransCurrencyCode:str = obj["vTransCurrencyCode"]
      """  Transactional CurrencyCode  """  
      self.vUseCarryFwdBal:bool = obj["vUseCarryFwdBal"]
      """  Use Carry Forward Balance  """  
      self.sBalanceAcct:str = obj["sBalanceAcct"]
      """  Balance Account  """  
      self.fiscalYear:int = obj["fiscalYear"]
      """  Fiscal Year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      pass

class GetRowsCurrBal_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLTrackerTableset] = obj["returnObj"]
      pass

class GetRowsGLAccountList_input:
   """ Required : 
   vBookID
   vBalanceType
   vUseCarryFwdBal
   fiscalYear
   fiscalYearSuffix
   budgetCodeID
   glAccountList
   """  
   def __init__(self, obj):
      self.vBookID:str = obj["vBookID"]
      self.vBalanceType:str = obj["vBalanceType"]
      self.vUseCarryFwdBal:bool = obj["vUseCarryFwdBal"]
      self.fiscalYear:int = obj["fiscalYear"]
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.budgetCodeID:str = obj["budgetCodeID"]
      self.glAccountList:str = obj["glAccountList"]
      """  Tilde delimited list of GL Accounts  """  
      pass

class GetRowsGLAccountList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLTrackerTableset] = obj["returnObj"]
      pass

class GetRowsMultiple_input:
   """ Required : 
   vBookID
   vBalanceType
   vUseCarryFwdBal
   fiscalYear
   fiscalYearSuffix
   budgetCodeID
   ds
   """  
   def __init__(self, obj):
      self.vBookID:str = obj["vBookID"]
      """  Book ID  """  
      self.vBalanceType:str = obj["vBalanceType"]
      """  Balance Type  """  
      self.vUseCarryFwdBal:bool = obj["vUseCarryFwdBal"]
      """  Use Carry Forward Balance  """  
      self.fiscalYear:int = obj["fiscalYear"]
      """  Fiscal Year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.budgetCodeID:str = obj["budgetCodeID"]
      """  Budget Code  """  
      self.ds:list[Erp_Tablesets_GLAccountTrackerTableset] = obj["ds"]
      pass

class GetRowsMultiple_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLTrackerTableset] = obj["returnObj"]
      pass

class GetRowsSpecificGLAccount_input:
   """ Required : 
   vBookID
   vBalanceType
   vUseCarryFwdBal
   sBalanceAcct
   fiscalYear
   fiscalYearSuffix
   budgetCodeID
   """  
   def __init__(self, obj):
      self.vBookID:str = obj["vBookID"]
      """  Book ID  """  
      self.vBalanceType:str = obj["vBalanceType"]
      """  Balance Type P or T  """  
      self.vUseCarryFwdBal:bool = obj["vUseCarryFwdBal"]
      """  Use Carry Forward Balance  """  
      self.sBalanceAcct:str = obj["sBalanceAcct"]
      """  Balance Account  """  
      self.fiscalYear:int = obj["fiscalYear"]
      """  Fiscal Year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.budgetCodeID:str = obj["budgetCodeID"]
      """  Fiscal Year Suffix  """  
      pass

class GetRowsSpecificGLAccount_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLTrackerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.openBalance:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   vBookID
   vBalanceType
   vUseCarryFwdBal
   sBalanceAcct
   fiscalYear
   fiscalYearSuffix
   budgetCodeID
   """  
   def __init__(self, obj):
      self.vBookID:str = obj["vBookID"]
      """  Book ID  """  
      self.vBalanceType:str = obj["vBalanceType"]
      """  Balance Type P or T  """  
      self.vUseCarryFwdBal:bool = obj["vUseCarryFwdBal"]
      """  Use Carry Forward Balance  """  
      self.sBalanceAcct:str = obj["sBalanceAcct"]
      """  Balance Account  """  
      self.fiscalYear:int = obj["fiscalYear"]
      """  Fiscal Year  """  
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      self.budgetCodeID:str = obj["budgetCodeID"]
      """  Fiscal Year Suffix  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GLTrackerTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.openBalance:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetSiteFilterAndText_input:
   """ Required : 
   ds
   bookID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GLTrackerSitesTableset] = obj["ds"]
      self.bookID:str = obj["bookID"]
      """  Book ID  """  
      pass

class GetSiteFilterAndText_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GLTrackerSitesTableset] = obj["ds"]
      self.siteFilter:str = obj["parameters"]
      self.sitesSelectedText:str = obj["parameters"]
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

class OnChangeBookID_input:
   """ Required : 
   bookID
   ds
   """  
   def __init__(self, obj):
      self.bookID:str = obj["bookID"]
      self.ds:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["ds"]
      pass

class OnChangeBookID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBudgetCodeID_input:
   """ Required : 
   budgetCodeID
   ds
   """  
   def __init__(self, obj):
      self.budgetCodeID:str = obj["budgetCodeID"]
      self.ds:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["ds"]
      pass

class OnChangeBudgetCodeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFiscalYearSuffix_input:
   """ Required : 
   fiscalYearSuffix
   ds
   """  
   def __init__(self, obj):
      self.fiscalYearSuffix:str = obj["fiscalYearSuffix"]
      self.ds:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["ds"]
      pass

class OnChangeFiscalYearSuffix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFiscalYear_input:
   """ Required : 
   fiscalYear
   ds
   """  
   def __init__(self, obj):
      self.fiscalYear:int = obj["fiscalYear"]
      self.ds:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["ds"]
      pass

class OnChangeFiscalYear_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeStartEndDate_input:
   """ Required : 
   startEndDate
   isStartDate
   ds
   """  
   def __init__(self, obj):
      self.startEndDate:str = obj["startEndDate"]
      self.isStartDate:bool = obj["isStartDate"]
      self.ds:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["ds"]
      pass

class OnChangeStartEndDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeStartEndPeriod_input:
   """ Required : 
   startEndPeriod
   isStartDate
   ds
   """  
   def __init__(self, obj):
      self.startEndPeriod:int = obj["startEndPeriod"]
      self.isStartDate:bool = obj["isStartDate"]
      self.ds:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["ds"]
      pass

class OnChangeStartEndPeriod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ChartTrackerFiltersTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateBudgetCode_input:
   """ Required : 
   budgetCodeID
   """  
   def __init__(self, obj):
      self.budgetCodeID:str = obj["budgetCodeID"]
      """  Budget Code ID  """  
      pass

class ValidateBudgetCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.budgetCodeID:str = obj["parameters"]
      self.budgetCodeDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateFiscalPerDate_input:
   """ Required : 
   ipBookID
   ipFiscalYear
   ipFiscalYearSuffix
   ipFiscalPerDate
   ipFiscalPer
   """  
   def __init__(self, obj):
      self.ipBookID:str = obj["ipBookID"]
      """  Book ID if not specified values will be based on Company.FiscalCalendarID"  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Current Fiscal Year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  Current Fiscal Year Suffix  """  
      self.ipFiscalPerDate:str = obj["ipFiscalPerDate"]
      """  Date to validate  """  
      self.ipFiscalPer:int = obj["ipFiscalPer"]
      """  old Fiscal Period  """  
      pass

class ValidateFiscalPerDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ipOutFiscalPeriod:int = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateFiscalPeriod_input:
   """ Required : 
   vBookID
   ipFiscalYear
   ipFiscalYearSuffix
   ipFiscalPer
   """  
   def __init__(self, obj):
      self.vBookID:str = obj["vBookID"]
      """  Book ID if not specified values will be based on Company.FiscalCalendarID"  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal Year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  Fiscal Suffix  """  
      self.ipFiscalPer:int = obj["ipFiscalPer"]
      """  Fiscal Period  """  
      pass

class ValidateFiscalPeriod_output:
   def __init__(self, obj):
      pass

class ValidateFiscalYearSuffix_input:
   """ Required : 
   vBookID
   ipFiscalYear
   ipFiscalYearSuffix
   """  
   def __init__(self, obj):
      self.vBookID:str = obj["vBookID"]
      """  Book ID if not specified values will be based on Company.FiscalCalendarID"  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal Year  """  
      self.ipFiscalYearSuffix:str = obj["ipFiscalYearSuffix"]
      """  Fiscal Year Suffix  """  
      pass

class ValidateFiscalYearSuffix_output:
   def __init__(self, obj):
      pass

class ValidateFiscalYear_input:
   """ Required : 
   vBookID
   ipFiscalYear
   """  
   def __init__(self, obj):
      self.vBookID:str = obj["vBookID"]
      """  Book ID if not specified values will be based on Company.FiscalCalendarID"  """  
      self.ipFiscalYear:int = obj["ipFiscalYear"]
      """  Fiscal Year  """  
      pass

class ValidateFiscalYear_output:
   def __init__(self, obj):
      pass

