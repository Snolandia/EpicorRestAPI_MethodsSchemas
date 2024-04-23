import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.RPT.ProcessPaymentSvc
# Description: Initializes a new class of "ProcessPaymentSvc" />.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GenerateBankExportFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateBankExportFile
   Description: GetBankExportFile.
   OperationID: GenerateBankExportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateBankExportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateBankExportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewProcessPayment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewProcessPayment
   Description: Call this method instead of GetNewParameters.
This method has the functionality of GetNewParameters and it takes
GroupID as input so it can fill the ProcessPaymentDataset with
relevant data for the GroupID.
The BL determines whether its a Start / ReStart process payment and sends the data accordingly.
   OperationID: GetNewProcessPayment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewProcessPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProcessPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewProcessPaymentForSingleRemitAdvice(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewProcessPaymentForSingleRemitAdvice
   Description: Call this method instead of GetNewParameters when printing a remittance advice for a single check.
This method has the functionality of GetNewParameters and it takes
HeadNum as input so it can fill the ProcessPaymentDataset with
relevant data for the CHeck.
   OperationID: GetNewProcessPaymentForSingleRemitAdvice
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewProcessPaymentForSingleRemitAdvice_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewProcessPaymentForSingleRemitAdvice_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankAcctID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankAcctID
   Description: Call method when the user changes the Bank account in Process Payment.
   OperationID: OnChangeBankAcctID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCheckDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCheckDate
   Description: Call method when the over rides the check # in Process Payment.
   OperationID: OnChangeCheckDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCheckDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCheckDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLoadedCheckNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLoadedCheckNum
   Description: Call method when the over rides the check # in Process Payment.
   OperationID: OnChangeLoadedCheckNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLoadedCheckNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLoadedCheckNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBankExportFileName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBankExportFileName
   Description: Call method when the BankExportFileName changes
   OperationID: OnChangeBankExportFileName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBankExportFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankExportFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OverwriteFileWarning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OverwriteFileWarning
   Description: Purpose:
Parameters:  none
Notes:
<param name="inFileName">File Name</param><param name="vWarningMessage">Overwrite file warning message.</param>
   OperationID: OverwriteFileWarning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OverwriteFileWarning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OverwriteFileWarning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_paymentGroupingPO3(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method paymentGroupingPO3
   Description: Process group for PO3
   OperationID: paymentGroupingPO3
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/paymentGroupingPO3_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/paymentGroupingPO3_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreRunDirect(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreRunDirect
   Description: This method is called when printing or generating and contains extra logic which is run before RunDirect.
   OperationID: PreRunDirect
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreRunDirect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreRunDirect_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RunProcessPayment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RunProcessPayment
   Description: Process Payments.
   OperationID: RunProcessPayment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunProcessPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunProcessPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReStartProcessPayment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReStartProcessPayment
   Description: Process Payments.
   OperationID: ReStartProcessPayment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReStartProcessPayment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReStartProcessPayment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestGroupProcessing(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestGroupProcessing
   Description: Test Group Processing
   OperationID: TestGroupProcessing
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestGroupProcessing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestGroupProcessing_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateElecIntFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateElecIntFile
   Description: Validate Electronic Interface File
   OperationID: ValidateElecIntFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateElecIntFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateElecIntFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_validateProcessPaymentParam(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method validateProcessPaymentParam
   Description: Purpose:     Common validations used by ReStartProcessPayment and ProcessPayment.
Parameters:  none
Notes:
   OperationID: validateProcessPaymentParam
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/validateProcessPaymentParam_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/validateProcessPaymentParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescrList(epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescrList
   Description: Purpose:     Get code descriptions list
Parameters:  none
Notes:
   OperationID: GetCodeDescrList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescrList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_getCurrencyID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getCurrencyID
   Description: Purpose:     Get the currency id
Parameters:  none
Notes:
   OperationID: getCurrencyID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getCurrencyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getCurrencyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getEFTProductionNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getEFTProductionNumber
   Description: Purpose:     Get Production Number for EFT from patch field.
Parameters:  The Product Number is between 1 - 9 for each day and restarts after 9.
If this method is being called by a validation process, the inUpdate should
be assigned to false until ready to post.
Notes:
   OperationID: getEFTProductionNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getEFTProductionNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getEFTProductionNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getNextECheckNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getNextECheckNum
   Description: Purpose:     Get the last payment number for the specified bank account for Electronic payment
Parameters:  none
Notes:
   OperationID: getNextECheckNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getNextECheckNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getNextECheckNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getStartCheckNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getStartCheckNum
   Description: Purpose:     Get the last payment number for the specified bank account,
increment by 1 to display the starting payment number.
Parameters:  none
Notes:
   OperationID: getStartCheckNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getStartCheckNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getStartCheckNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSortByList(epicorHeaders = None):
   """  
   Summary: Invoke method GetSortByList
   Description: Returns a list of SortBy options
   OperationID: GetSortByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_validateNegativePaymentExist(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method validateNegativePaymentExist
   Description: Purpose:     Validate a negative payment exists
Parameters:  none
Notes:
   OperationID: validateNegativePaymentExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/validateNegativePaymentExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/validateNegativePaymentExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LockRecord(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LockRecord
   Description: Create the document lock
   OperationID: LockRecord
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LockRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsLocked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsLocked
   Description: Check is a document lock is in place
   OperationID: IsLocked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsGenerated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsGenerated
   Description: Check if the payment has already been generated
   OperationID: IsGenerated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/IsGenerated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsGenerated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.RPT.ProcessPaymentSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_ProcessPaymentParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CheckDate:str = obj["CheckDate"]
      self.FiscalYear:int = obj["FiscalYear"]
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      self.BankAcctID:str = obj["BankAcctID"]
      self.LastUsedCheckNum:int = obj["LastUsedCheckNum"]
      self.BankExportFileName:str = obj["BankExportFileName"]
      self.ElecPayment:bool = obj["ElecPayment"]
      self.ReStartProcessPayment:bool = obj["ReStartProcessPayment"]
      """  Indicates wether its a restart payment or a process payment.  """  
      self.GroupID:str = obj["GroupID"]
      self.LastGoodCheckNum:int = obj["LastGoodCheckNum"]
      """  Last good check number printed.  Used in re-process payments  """  
      self.BankAcctIdDescription:str = obj["BankAcctIdDescription"]
      self.BankAcctIdBankName:str = obj["BankAcctIdBankName"]
      self.OverridePayment:bool = obj["OverridePayment"]
      self.FormsToGenerate:str = obj["FormsToGenerate"]
      """  Can be C for checks, B for both or R for remit.  """  
      self.EnableFormsPrompt:bool = obj["EnableFormsPrompt"]
      """  enable forms prompt.  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      self.SortBy:str = obj["SortBy"]
      self.LoadedCheckNum:int = obj["LoadedCheckNum"]
      self.CheckPrinting:bool = obj["CheckPrinting"]
      """  Determine if the payment method is Check Printing.  """  
      self.SupplierList:str = obj["SupplierList"]
      """  Suppliers filtering list. Only for Remittance Advice reprinting.  """  
      self.PaymentList:str = obj["PaymentList"]
      """  Payments filtering list. Only for Remittance Advice reprinting.  """  
      self.RemittanceReprint:bool = obj["RemittanceReprint"]
      """  Remmitance Advice reprinting  """  
      self.ElecPaymentGen:bool = obj["ElecPaymentGen"]
      self.BankExportDisplayFileName:str = obj["BankExportDisplayFileName"]
      self.MICRCheck:bool = obj["MICRCheck"]
      self.ProcessType:str = obj["ProcessType"]
      """  Process Type  """  
      self.SupplierIDList:str = obj["SupplierIDList"]
      self.HeadNum:int = obj["HeadNum"]
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

class Erp_Tablesets_ProcessPaymentTableset:
   def __init__(self, obj):
      self.ProcessPaymentParam:list[Erp_Tablesets_ProcessPaymentParamRow] = obj["ProcessPaymentParam"]
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

class GenerateBankExportFile_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

class GenerateBankExportFile_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetCodeDescrList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

class GetDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewParameters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProcessPaymentTableset] = obj["returnObj"]
      pass

class GetNewProcessPaymentForSingleRemitAdvice_input:
   """ Required : 
   headNum
   """  
   def __init__(self, obj):
      self.headNum:int = obj["headNum"]
      """  Check Head Num  """  
      pass

class GetNewProcessPaymentForSingleRemitAdvice_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProcessPaymentTableset] = obj["returnObj"]
      pass

class GetNewProcessPayment_input:
   """ Required : 
   pcGroupID
   formCalled
   """  
   def __init__(self, obj):
      self.pcGroupID:str = obj["pcGroupID"]
      """  AP Check Group ID  """  
      self.formCalled:str = obj["formCalled"]
      """  Which form called process payments.  """  
      pass

class GetNewProcessPayment_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ProcessPaymentTableset] = obj["returnObj"]
      pass

class GetParamTaskDef_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

class GetParamTaskDef_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
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
      self.returnObj:list[Erp_Tablesets_ProcessPaymentTableset] = obj["returnObj"]
      pass

class GetRptArchiveList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetSortByList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sortbylist:str = obj["parameters"]
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

class IsGenerated_input:
   """ Required : 
   company
   groupID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.groupID:str = obj["groupID"]
      pass

class IsGenerated_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class IsLocked_input:
   """ Required : 
   company
   groupID
   relatedToFile
   lockStatus
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.groupID:str = obj["groupID"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.lockStatus:str = obj["lockStatus"]
      pass

class IsLocked_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class LockRecord_input:
   """ Required : 
   groupID
   """  
   def __init__(self, obj):
      self.groupID:str = obj["groupID"]
      pass

class LockRecord_output:
   def __init__(self, obj):
      pass

class OnChangeBankAcctID_input:
   """ Required : 
   pcBankAcctID
   ds
   """  
   def __init__(self, obj):
      self.pcBankAcctID:str = obj["pcBankAcctID"]
      """  Proposed bank account ID value.  """  
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

class OnChangeBankAcctID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeBankExportFileName_input:
   """ Required : 
   ipBankExportFileName
   ds
   """  
   def __init__(self, obj):
      self.ipBankExportFileName:str = obj["ipBankExportFileName"]
      """  File name including the full path  """  
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

class OnChangeBankExportFileName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCheckDate_input:
   """ Required : 
   CheckDate
   ds
   """  
   def __init__(self, obj):
      self.CheckDate:str = obj["CheckDate"]
      """  Payment Date  """  
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

class OnChangeCheckDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLoadedCheckNum_input:
   """ Required : 
   piLoadedCheckNum
   ds
   """  
   def __init__(self, obj):
      self.piLoadedCheckNum:int = obj["piLoadedCheckNum"]
      """  Loaded check number  """  
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

class OnChangeLoadedCheckNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OverwriteFileWarning_input:
   """ Required : 
   inFileName
   """  
   def __init__(self, obj):
      self.inFileName:str = obj["inFileName"]
      pass

class OverwriteFileWarning_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vWarningMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreRunDirect_input:
   """ Required : 
   ds
   printRemit
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      self.printRemit:bool = obj["printRemit"]
      """  This should be true if Forms to Generate is "Both" and we want to print Remit  """  
      pass

class PreRunDirect_output:
   def __init__(self, obj):
      pass

class ReStartProcessPayment_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

class ReStartProcessPayment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

class RunDirect_output:
   def __init__(self, obj):
      pass

class RunProcessPayment_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

class RunProcessPayment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SaveDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_ProcessPaymentTableset] = obj["ds"]
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

class TestGroupProcessing_input:
   """ Required : 
   eGroupID
   """  
   def __init__(self, obj):
      self.eGroupID:str = obj["eGroupID"]
      """  Group ID  """  
      pass

class TestGroupProcessing_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.NegativeGroupList:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateElecIntFile_input:
   """ Required : 
   ipGroupID
   ipCheckDate
   """  
   def __init__(self, obj):
      self.ipGroupID:str = obj["ipGroupID"]
      """  Group ID  """  
      self.ipCheckDate:str = obj["ipCheckDate"]
      """  Check Date  """  
      pass

class ValidateElecIntFile_output:
   def __init__(self, obj):
      pass

class getCurrencyID_input:
   """ Required : 
   inCurrencyCode
   """  
   def __init__(self, obj):
      self.inCurrencyCode:str = obj["inCurrencyCode"]
      pass

class getCurrencyID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class getEFTProductionNumber_input:
   """ Required : 
   inCompany
   inPMUID
   inUpdate
   """  
   def __init__(self, obj):
      self.inCompany:str = obj["inCompany"]
      self.inPMUID:int = obj["inPMUID"]
      self.inUpdate:bool = obj["inUpdate"]
      pass

class getEFTProductionNumber_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class getNextECheckNum_input:
   """ Required : 
   CurBankAcctID
   """  
   def __init__(self, obj):
      self.CurBankAcctID:str = obj["CurBankAcctID"]
      pass

class getNextECheckNum_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class getStartCheckNum_input:
   """ Required : 
   pcBankAcctID
   """  
   def __init__(self, obj):
      self.pcBankAcctID:str = obj["pcBankAcctID"]
      pass

class getStartCheckNum_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class paymentGroupingPO3_input:
   """ Required : 
   iPO3PayType
   cGroupID
   """  
   def __init__(self, obj):
      self.iPO3PayType:int = obj["iPO3PayType"]
      """  PO3 Pay Type  """  
      self.cGroupID:str = obj["cGroupID"]
      """  Group ID  """  
      pass

class paymentGroupingPO3_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cErrorMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class validateNegativePaymentExist_input:
   """ Required : 
   inCompany
   inGroupID
   inAllowZeroCheckAmt
   inValidateBySupplyer
   inSPecialPayType
   """  
   def __init__(self, obj):
      self.inCompany:str = obj["inCompany"]
      self.inGroupID:str = obj["inGroupID"]
      self.inAllowZeroCheckAmt:bool = obj["inAllowZeroCheckAmt"]
      self.inValidateBySupplyer:bool = obj["inValidateBySupplyer"]
      self.inSPecialPayType:int = obj["inSPecialPayType"]
      pass

class validateNegativePaymentExist_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class validateProcessPaymentParam_input:
   """ Required : 
   ttProcessPaymentParam
   """  
   def __init__(self, obj):
      self.ttProcessPaymentParam:list[Erp_Tablesets_ProcessPaymentParamRow] = obj["ttProcessPaymentParam"]
      pass

class validateProcessPaymentParam_output:
   def __init__(self, obj):
      pass

