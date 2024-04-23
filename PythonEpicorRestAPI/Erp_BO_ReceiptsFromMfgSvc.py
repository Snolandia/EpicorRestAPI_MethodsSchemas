import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ReceiptsFromMfgSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/$metadata",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ReceiptsFromMfgJobAsmblRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CheckPackageCodeAllocNegQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPackageCodeAllocNegQty
   Description: Check Package Code Allocated negative quantity.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Get Available Transaction Doc Types.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultTranDocTypeID(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultTranDocTypeID
   Description: Get default trandoctypeid.
   OperationID: GetDefaultTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultWhseBin(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultWhseBin
   Description: Get Warehouse Code for PCID.
   OperationID: GetDefaultWhseBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultWhseBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Get Code Description List
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCIDParamsRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCIDParamsRow
   Description: Creates a new PCID Parameter row used to contain the PCID receipt to inventory default information.
   OperationID: GetNewPCIDParamsRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCIDParamsRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCIDParamsRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_IsValidAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method IsValidAssembly
   Description: Returns logical true if the assembly is valid and false otherwise.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NegativeInventoryTest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NegativeInventoryTest
   Description: <param name="pcPartNum"></param>
<param name="pcWhseCode"></param>
<param name="pcBinNum"></param>
<param name="pcLotNum"></param>
<param name="pcAttributeSetID"></param>
<param name="pcPCID"></param>
<param name="pcDimCode"></param>
<param name="pdDimConvFactor"></param>
<param name="ipSellingQuantity"></param>
<param name="pcNeqQtyAction"></param>
<param name="pcMessage"></param>
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateWhsePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateWhsePCID
   Description: Validates warehouse for PCID
   OperationID: ValidateWhsePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateWhsePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWhsePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateWhsePCIDAndGetDefaultBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateWhsePCIDAndGetDefaultBin
   Description: Validates warehouse for PCID and returns a bin if there is only one available.
   OperationID: ValidateWhsePCIDAndGetDefaultBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateWhsePCIDAndGetDefaultBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWhsePCIDAndGetDefaultBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateWhseBinPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateWhseBinPCID
   Description: Validates BinNum for PCID
   OperationID: ValidateWhseBinPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateWhseBinPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateWhseBinPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePCIDExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePCIDExists
   Description: Validate PCID Exists
   OperationID: ValidatePCIDExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePCIDExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePCIDExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPCID
   Description: Get PCID
   OperationID: GetPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ExecuteProcessPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ExecuteProcessPCID
   Description: Execute Process a PCID
   OperationID: ExecuteProcessPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ExecuteProcessPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteProcessPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePCID
   Description: Validates PCID
   OperationID: ValidatePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewJobAsmblMultiple(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewJobAsmblMultiple
   Description: This method creates a new ttSelectedJobAsmbl row entry.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReceiptsFromMfg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReceiptsFromMfg
   Description: This method creates a new ttPartTran row entry.
   OperationID: GetNewReceiptsFromMfg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReceiptsFromMfg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReceiptsFromMfg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateFromJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateFromJob
   Description: validate from job
   OperationID: ValidateFromJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateFromJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFromJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReceiptsFromMfgJobAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReceiptsFromMfgJobAsm
   Description: This method creates a new ttSelectedJobAsmbl row entry.
   OperationID: GetNewReceiptsFromMfgJobAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReceiptsFromMfgJobAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReceiptsFromMfgJobAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReceiptsFromMfgMtlQueue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReceiptsFromMfgMtlQueue
   Description: This method creates a new ReceiptsFromMfgDataSet using MtlQueue RowIdent.
   OperationID: GetNewReceiptsFromMfgMtlQueue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReceiptsFromMfgMtlQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReceiptsFromMfgMtlQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReceiptsFromPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReceiptsFromPCID
   Description: creates job receipt to inventory transactions for the selected PCID.
   OperationID: GetNewReceiptsFromPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReceiptsFromPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReceiptsFromPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReceiptsFromPCIDMultiple(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReceiptsFromPCIDMultiple
   Description: Creates job receipt to inventory transactions for the selected PCIDs.
   OperationID: GetNewReceiptsFromPCIDMultiple
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReceiptsFromPCIDMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReceiptsFromPCIDMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewReceiptsFromPCIDSupplyJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewReceiptsFromPCIDSupplyJobNum
   Description: Creates job receipt to inventory transactions for PCIDs associated with a JobNumber.
   OperationID: GetNewReceiptsFromPCIDSupplyJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewReceiptsFromPCIDSupplyJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReceiptsFromPCIDSupplyJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUpdate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUpdate
   Description: This method will return a record in the LegalNumberGenerate datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreProcessPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreProcessPCID
   Description: This method will return a record in the LegalNumberGenerate datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreProcessPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreProcessPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcessPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessPCID
   Description: Process a PCID
   OperationID: ProcessPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiveMfgPartToInventory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiveMfgPartToInventory
   Description: Update the Receipts from Manufacturing to Inventory.
   OperationID: ReceiveMfgPartToInventory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiveMfgPartToInventory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveMfgPartToInventory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiveMfgPartToJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiveMfgPartToJob
   Description: Update the Receipts from Manufacturing to Job.
   OperationID: ReceiveMfgPartToJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiveMfgPartToJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveMfgPartToJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiveMfgPCIDtoInventory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiveMfgPCIDtoInventory
   Description: Receives a PCID at WIPFG status into Inventory.
   OperationID: ReceiveMfgPCIDtoInventory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiveMfgPCIDtoInventory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveMfgPCIDtoInventory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiveMfgPCIDtoInventoryMultiple(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiveMfgPCIDtoInventoryMultiple
   Description: Receives multiple PCIDs which are at status WIPFG into inventory.
   OperationID: ReceiveMfgPCIDtoInventoryMultiple
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiveMfgPCIDtoInventoryMultiple_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveMfgPCIDtoInventoryMultiple_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReceiveSalvagedPartToInventory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReceiveSalvagedPartToInventory
   Description: Update Salvaged Material to Inventory.
   OperationID: ReceiveSalvagedPartToInventory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReceiveSalvagedPartToInventory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReceiveSalvagedPartToInventory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeActTranQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeActTranQty
   Description: Change the PartTran values based on the new value of PartTran.ActTranQty.
   OperationID: OnChangeActTranQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeActTranQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeActTranQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCalculateExtCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCalculateExtCost
   Description: Calculate Extend unit Cost
   OperationID: OnChangeCalculateExtCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCalculateExtCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCalculateExtCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeActTransUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeActTransUOM
   Description: Call this method when the value of Epicor.Mfg.BO.PartTran.ActTransUOM changes.
   OperationID: OnChangeActTransUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeActTransUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeActTransUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAssemblySeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAssemblySeq
   Description: Change the PartTran values based on the new PartTran.AssemblySeq.
   OperationID: OnChangeAssemblySeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAssemblySeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssemblySeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAssemblySeq2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAssemblySeq2
   Description: Change the PartTran values based on the new value of PartTran.AssemblySeq2.
   OperationID: OnChangeAssemblySeq2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAssemblySeq2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssemblySeq2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBinNum
   Description: Call this method when the value of Epicor.Mfg.BO.ReceiptsFromMfgDataSet.BinNum changes.
   OperationID: OnChangeBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobNum
   Description: When the user enters the Job# in ReceiptsFromMfgJobsDataSet call this method.
   OperationID: OnChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeExtCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeExtCost
   Description: Calculate extended cost
   OperationID: OnChangeExtCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeExtCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeExtCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobNum2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobNum2
   Description: Change the PartTran values based on the new value of PartTran.JobNum2.
   OperationID: OnChangeJobNum2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobSeq2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobSeq2
   Description: Change the PartTran values based on the new value of PartTran.JobSeq2.
   OperationID: OnChangeJobSeq2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeJobSeq2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobSeq2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLotNum
   Description: Change the PartTran values based on the new value of PartTran.LotNum.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOverrideCost(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOverrideCost
   Description: Recalculate the PartTran unit cost values when the user unchecks the Override Cost toggle box.
   OperationID: OnChangeOverrideCost
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOverrideCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOverrideCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: When the user changes the PartNum in ReceiptsFromMfgJobsDataSet call this method.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCIDParamsPlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCIDParamsPlant
   Description: Validate PCID defaults to site and then apply the value to all receipt transactions loaded.
   OperationID: OnChangePCIDParamsPlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCIDParamsPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDParamsPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCIDParamWarehouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCIDParamWarehouseCode
   Description: Validate PCID defaults to Warehouse code and then apply the value to all receipt transactions loaded.
   OperationID: OnChangePCIDParamWarehouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCIDParamWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDParamWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeToPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeToPCID
   Description: Call this method when the value of To PCID changes.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromPCID
   Description: Call this method when the value of From PCID changes.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCIDParamsBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCIDParamsBinNum
   Description: Validate PCID defaults To Bin and then apply the value to all receipt transactions loaded.
   OperationID: OnChangePCIDParamsBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCIDParamsBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDParamsBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCIDParamsTranDate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCIDParamsTranDate
   Description: Change the PCID defaults Transaction date and then apply the value to all receipt transactions loaded.
   OperationID: OnChangePCIDParamsTranDate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCIDParamsTranDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDParamsTranDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCIDParamsTranReference(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCIDParamsTranReference
   Description: Called when changing the PCID defaults transaction reference and then apply the value to all receipt transactions loaded.
   OperationID: OnChangePCIDParamsTranReference
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCIDParamsTranReference_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDParamsTranReference_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCIDParamsTranDocTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCIDParamsTranDocTypeID
   Description: Validate the PCID defaults transaction document type and then apply the value to all receipt transactions loaded.
   OperationID: OnChangePCIDParamsTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCIDParamsTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCIDParamsTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePlant
   Description: When the user changes the Plant2 in ReceiptsFromMfgJobsDataSet call this method.
   OperationID: OnChangePlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWareHouseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWareHouseCode
   Description: When the user changes the WareHouseCode in ReceiptsFromMfgJobsDataSet call this method.
   OperationID: OnChangeWareHouseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWareHouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWareHouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSalvageJobSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSalvageJobSeq
   Description: Change the PartTran values based on the new PartTran.JobSeq.
This method is used while receiving Salvaged material to Inventory.
   OperationID: OnChangeSalvageJobSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSalvageJobSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSalvageJobSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSalvagePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSalvagePartNum
   Description: Change the PartTran values based on the new PartTran.PartNum.
This method is used while receiving Salvaged material to Inventory.
   OperationID: OnChangeSalvagePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSalvagePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSalvagePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeTranQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeTranQty
   Description: Change the PartTran values based on the new value of PartTran.TranQty.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingRevisionNumMS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingRevisionNumMS
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNumMS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNumMS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNumMS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EnableSerialMatching(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method EnableSerialMatching
   Description: Validates if the option Serial Matching should be enabled.
   OperationID: EnableSerialMatching
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/EnableSerialMatching_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableSerialMatching_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VerifySerialMatchAndPlanContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifySerialMatchAndPlanContract
   Description: Verifies if the user should enter child serial numbers for the serial numbers
being received depending on the setting of the Serial Number Matching before save.
   OperationID: VerifySerialMatchAndPlanContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifySerialMatchAndPlanContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifySerialMatchAndPlanContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReceiptsFromMfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ReceiptsFromMfgJobAsmblRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ReceiptsFromMfgJobAsmblRow] = obj["value"]
      pass

class Erp_Tablesets_ReceiptsFromMfgJobAsmblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.PartNum:str = obj["PartNum"]
      self.Description:str = obj["Description"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.JobHeadPartNum:str = obj["JobHeadPartNum"]
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class CheckPackageCodeAllocNegQty_input:
   """ Required : 
   ipcalledFrom
   ipPackageCode
   ipQty
   """  
   def __init__(self, obj):
      self.ipcalledFrom:str = obj["ipcalledFrom"]
      self.ipPackageCode:str = obj["ipPackageCode"]
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

class EnableSerialMatching_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class EnableSerialMatching_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.plEnable:bool = obj["plEnable"]
      pass

      """  output parameters  """  

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

class Erp_Tablesets_PCIDReceiptsParamsRow:
   def __init__(self, obj):
      self.BinNum:str = obj["BinNum"]
      self.Plant2:str = obj["Plant2"]
      self.Plant2Name:str = obj["Plant2Name"]
      self.PreviousPCID:str = obj["PreviousPCID"]
      self.TranDate:str = obj["TranDate"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranReference:str = obj["TranReference"]
      self.WareHouseCode:str = obj["WareHouseCode"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.EnableReceiveAllPCIDs:bool = obj["EnableReceiveAllPCIDs"]
      """  Set to True if multiple PCIDs have been selected for processing  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCIDReceiptsSelectedRow:
   def __init__(self, obj):
      self.PCID:str = obj["PCID"]
      self.Company:str = obj["Company"]
      self.ActTranQty:int = obj["ActTranQty"]
      self.ActTransUOM:str = obj["ActTransUOM"]
      self.PartNum:str = obj["PartNum"]
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      self.TrackLots:bool = obj["TrackLots"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartTranRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.SysDate:str = obj["SysDate"]
      """  System date at time that record was created.  """  
      self.SysTime:int = obj["SysTime"]
      """  System Time (hr-min-sec) when transaction was created.  """  
      self.TranNum:int = obj["TranNum"]
      """  A number which is used to allow create a unique key for the file.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number that this transaction is for.  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse that transaction is applied to  """  
      self.BinNum:str = obj["BinNum"]
      """  Identifies the Bin location that this transaction affected.  """  
      self.TranClass:str = obj["TranClass"]
      """   Transaction Class...A-adjustment, D-DMR, I-issue, R-receipt, S-Shipment X-Job Adjustment. A character field which classifies PartTran records.  This is a higher level of classification of the TransType field. Their relationships are;
 R = DMR-STK, INS-MTL, INS-STK, INS-SUB, MFG-PLT, MFG-STK, MFG-WIP, PLT-STK, PUR-INS, PUR-MTL, PUR-STK, PUR-SUB, PUR-UKN, RMA-INS, STK-DMR, SVG-STK
I = ASM-INS, INS-ASM, INS-REJ, MTL-INS, PLT-ASM, PLT-MTL, STK-ASM, STK-INS, STK-MTL, STK-SRV, STK-UKN, SUB-DMR, SUB-INS,WIP-MFG
A = ADJ-CST, ADJ-PUR, ADJ-QTY, MFG-VAR, STK-PLT, STK-STK
S = MFG-CUS, MFG-VEN, STK-CUS
D = DMR-MTL, DMR-REJ, DMR-SUB, INS-DMR, MTL-DMR
X = ADJ-MTL, ADJ-SUB
Intended to  be used for record selection purposes.  """  
      self.TranType:str = obj["TranType"]
      """   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  """  
      self.InventoryTrans:bool = obj["InventoryTrans"]
      """  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  """  
      self.TranDate:str = obj["TranDate"]
      """  date of transaction.  """  
      self.TranQty:int = obj["TranQty"]
      """   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  """  
      self.UM:str = obj["UM"]
      """  Unit of Measure.  (part primary inventory uom)  """  
      self.MtlUnitCost:int = obj["MtlUnitCost"]
      """  Material Unit Cost  """  
      self.LbrUnitCost:int = obj["LbrUnitCost"]
      """  Labor Unit Cost  """  
      self.BurUnitCost:int = obj["BurUnitCost"]
      """  Burden Unit Cost  """  
      self.SubUnitCost:int = obj["SubUnitCost"]
      """  Subcontract Unit Cost  """  
      self.MtlBurUnitCost:int = obj["MtlBurUnitCost"]
      """  Material Burden Unit Cost  """  
      self.ExtCost:int = obj["ExtCost"]
      """   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  """  
      self.CostMethod:str = obj["CostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the Part.CostMethod.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number that transaction is associated with.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence #  """  
      self.JobSeqType:str = obj["JobSeqType"]
      """   Indicates the type of Job record that the transaction references.
"M" = Material (JobMtl),  "S" = SubContract Operation (JobOper) or "O" = Inside Operation(JobOper)
(FYI: Non-Coformance/Inspection transactions, ASM-INS, INS-ASM, INS-DMR, DMR-ASM are the only ones which create "O" types  """  
      self.JobSeq:int = obj["JobSeq"]
      """  Seq # of specific material or subcontract operation record.  """  
      self.PackType:str = obj["PackType"]
      """  Indicates the type of Packing Slip... "C" = Customer (related to ShipDtl), "M" = Miscellaneous(MscShpDt),  "S" = Subcontractor (SubShipd) "TO" = (Transfer Order). This field, used along with PackNum/PackLine can be used to find the related shipping document record.  """  
      self.PackNum:int = obj["PackNum"]
      """  Packing slip number.  """  
      self.PackLine:int = obj["PackLine"]
      """   The packing slip line # that this transaction is linked to.
Note: This field is used for both  a shipment to customer packing slip  or a receipt from vendor packing slip.  """  
      self.PONum:int = obj["PONum"]
      """  Created by Purchase Order Receipt Process.  """  
      self.POLine:int = obj["POLine"]
      """  The line # of detail record on the purchase order.  """  
      self.PORelNum:int = obj["PORelNum"]
      """  Purchase Order Release # of the POSched record that this transaction is for.  """  
      self.WareHouse2:str = obj["WareHouse2"]
      """  Transfer "From/To" warehouse code. This is used for the warehouse transfer transactions. For the Issue side of the transaction it identifies the "transfer to" warehouse. For the receipt side of the transaction it identifies the "transfer from" warehouse.  """  
      self.BinNum2:str = obj["BinNum2"]
      """  This value only exists for the warehouse transaction. TranSrc = "4".  For the Issue side of the transaction it identifies the Bin location that the quantity is transferred in to. On the Receipt side of the transaction it identifies the Bin location that the quantity was transferred from.  """  
      self.OrderNum:int = obj["OrderNum"]
      """   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  The sales order line that this transaction is associated with.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  The sales order release number that this shipment detail is linked to. The user never sees this field. It  is used as a foreign key back to the sales order release record.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  """  
      self.TranReference:str = obj["TranReference"]
      """  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part associated with this transaction. This is not directly entered by the user. Instead the entry programs pull it in from a parent record. The parent record could be the Part, JobOper, PODetl, JobMtl...  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that along with PurPoint is used to tie back to the VendorPP master file. Applicable for shipments to subcontractors (MFG-VEN) and receipts (PUR-STK, PUR-MTL, PUR-SUB, PUR-UKN).  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Vendor purchase point ID. (see VendorNum)  """  
      self.POReceiptQty:int = obj["POReceiptQty"]
      """  Quantity received against a purchase order in the vendors unit of measure.  """  
      self.POUnitCost:int = obj["POUnitCost"]
      """  Purchase Order Receipt actual unit cost in the vendors unit of measure. This is defaulted from the PO detail record. PO receipts uses this along with the calculated purchasing conversion factor to determine the MtlUnitCost field which is used as cost to job or stock.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.InvoiceNum:str = obj["InvoiceNum"]
      """  Invoice Number from corresponding APInvHed record. Applicable only with the purchase variance adjustment record (TranType = "ADJ-PUR") generated via A/P invoice posting.  """  
      self.InvoiceLine:int = obj["InvoiceLine"]
      """  Used along with InvoiceNum to relate to the corresponding APInvDtl record that generated this PartTran record. (see PartTran.InvoiceNum)  """  
      self.InvAdjSrc:str = obj["InvAdjSrc"]
      """  Inventory Adjustment Source for ADJ-QTY, ADJ-CST transaction types only.  "P" = Physical Inventory Count, "C" = Cycle Inventory Count, "O" = Other Adjustment  """  
      self.InvAdjReason:str = obj["InvAdjReason"]
      """  Used for Inventory Adjustment Source "Other" OR MTL-DMR, STK-DMR, SUB-DMR, or INS-DMR transaction types.  Refers to the Reason table.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot Number  """  
      self.DimCode:str = obj["DimCode"]
      """  Unique dimension code for the part.  """  
      self.DUM:str = obj["DUM"]
      """  Dimension unit of measure.  """  
      self.DimConvFactor:int = obj["DimConvFactor"]
      """   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  """  
      self.LotNum2:str = obj["LotNum2"]
      """  Transfer "From/To" lot number.  """  
      self.DimCode2:str = obj["DimCode2"]
      """  Transfer "From/To" Part Dimension  """  
      self.DUM2:str = obj["DUM2"]
      """  Transfer "From/To" Dimension unit of measure.  """  
      self.DimConvFactor2:int = obj["DimConvFactor2"]
      """  Transfer "From/To" Dimension conversion factor.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  For example: Adj-Cst for other than the parts costing method are not posted to G/L.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """  Indicates if transaction was posted to G/L.  Transactions are posted in summary form via the Job Management Capture COS/WIP process .  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal number that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.Costed:bool = obj["Costed"]
      """  The "Costed" field indicates if the Capture COS/Wip Activity has run on that part transaction. If "Yes" the transaction costs cant be changed anymore.  """  
      self.DMRNum:int = obj["DMRNum"]
      """  DMR number used to identify the related DMR record.  """  
      self.ActionNum:int = obj["ActionNum"]
      """  DMR action number  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number  """  
      self.COSPostingReqd:bool = obj["COSPostingReqd"]
      """   If the amount of this PartTran was posted to the A/R clearing account (COSPostingReq = Yes), then at sometime the amount needs to be moved to the COS account.   When the costs are moved, this flag is set to Yes.
When a product is shipped, its costs are put in A/R Clearing.  When it's invoiced the costs are ready to be moved to COS.  The Capture WIP/COS Activity procedure (JCP80.W) moves these costs.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.Plant2:str = obj["Plant2"]
      """  Site Identifier.  """  
      self.CallNum:int = obj["CallNum"]
      """  Reference to the service call that the material is being issued for.  """  
      self.CallLine:int = obj["CallLine"]
      """  Reference to the service call line  that the material is being issued for.  """  
      self.MatNum:int = obj["MatNum"]
      """  Reference to the service call line Material sequence that the material is being issued for.  """  
      self.JobNum2:str = obj["JobNum2"]
      """  Job Number of transfer source/target.  """  
      self.AssemblySeq2:int = obj["AssemblySeq2"]
      """  Assembly Sequence  of transfer source/target.  """  
      self.JobSeq2:int = obj["JobSeq2"]
      """  Seq # of transfer source/target.  """  
      self.CustNum:int = obj["CustNum"]
      """   NOTE: Applies only to the RMA-INS transactions.
Contains the system internal customer number of the related customer record. 
Not directly updateable, updated via the RmaRcpt write trigger.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line number of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.RMADisp:int = obj["RMADisp"]
      """  RMA Disposition  """  
      self.OtherDivValue:int = obj["OtherDivValue"]
      """  Other division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of Site transaction costs.  OtherDivValue only applies to Site to Site transactions (TranType="PLT-" and Site <> S  """  
      self.PlantTranNum:int = obj["PlantTranNum"]
      """  Site Transaction Number  """  
      self.NonConfID:int = obj["NonConfID"]
      """  Stores the linked non-conformance number from the NonConf record. (NonConf.TranID)  """  
      self.MtlMtlUnitCost:int = obj["MtlMtlUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlLabUnitCost:int = obj["MtlLabUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlSubUnitCost:int = obj["MtlSubUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  """  
      self.MtlBurdenUnitCost:int = obj["MtlBurdenUnitCost"]
      """  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  """  
      self.RefType:str = obj["RefType"]
      """  Link to the related GLRefTyp.RefType.  """  
      self.RefCode:str = obj["RefCode"]
      """  Link to the related Code in GLRefCod.RefCode  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.BeginQty:int = obj["BeginQty"]
      """  On Hand Quantity before the part costing calculations were run.  """  
      self.AfterQty:int = obj["AfterQty"]
      """  On Hand Quantity after part costing calculation were run.  """  
      self.BegBurUnitCost:int = obj["BegBurUnitCost"]
      """  Burden Unit cost before the part costing calculation was run  """  
      self.BegLbrUnitCost:int = obj["BegLbrUnitCost"]
      """  Labor Unit cost before the costing calculation was run  """  
      self.BegMtlBurUnitCost:int = obj["BegMtlBurUnitCost"]
      """  Material Burden Unit Cost before the costing calculation was run  """  
      self.BegMtlUnitCost:int = obj["BegMtlUnitCost"]
      """  Material Unit Cost before the costing calculation was run  """  
      self.BegSubUnitCost:int = obj["BegSubUnitCost"]
      """  Sub Contract Unit Cost before the costing calculation was run  """  
      self.AfterBurUnitCost:int = obj["AfterBurUnitCost"]
      """  Burden Unit cost after the part costing calculation was run  """  
      self.AfterLbrUnitCost:int = obj["AfterLbrUnitCost"]
      """  Labor Unit Cost after the costing calculation was run  """  
      self.AfterMtlBurUnitCost:int = obj["AfterMtlBurUnitCost"]
      """  Material Burden Unit Cost after the costing calculation was run  """  
      self.AfterMtlUnitCost:int = obj["AfterMtlUnitCost"]
      """  Material Unit Cost after the costing calculation was run  """  
      self.AfterSubUnitCost:int = obj["AfterSubUnitCost"]
      """  Sub Contract Unit Cost after the costing calculation was run  """  
      self.PlantCostValue:int = obj["PlantCostValue"]
      """  To Site division value.  The total price associated with the activity of moving (selling) an item from one Site to another. This is the rollup of To Site transaction costs.  SiteCostValue only applies to Site to Site transactions (TranType="PLT-" and Site  """  
      self.EmpID:str = obj["EmpID"]
      """  The Shop Employee ID of the user that created this transaction.  """  
      self.ReconcileNum:int = obj["ReconcileNum"]
      """  The unique identifier of the DemandReconcile that created this PartTran record.  """  
      self.CostID:str = obj["CostID"]
      """  Id to the Cost Set Group that is used as the default CostGrp.  """  
      self.FIFODate:str = obj["FIFODate"]
      """  For FIFO costed part, use this date to find the FIFO cost queue record affected by this transaction.  """  
      self.FIFOSeq:int = obj["FIFOSeq"]
      """  For FIFO costed part, use this sequence number to find the FIFO cost queue record affected by this transaction.  """  
      self.ActTranQty:int = obj["ActTranQty"]
      """   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  """  
      self.ActTransUOM:str = obj["ActTransUOM"]
      """  Actual Unit of Measure of the ActTransQty.  """  
      self.InvtyUOM:str = obj["InvtyUOM"]
      """  The Inventory Tracking Unit of Measure that transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.InvtyUOM2:str = obj["InvtyUOM2"]
      """  The Inventory Tracking Unit of Measure that inventory transfer transaction applies to. Normally the same as PartTran.UM unless its an inventory transaction against a part that is being tracked in multiple uoms.  """  
      self.FIFOAction:str = obj["FIFOAction"]
      """   Internal flag to indicate what type of FIFO update is needed.  Valid values are: (A/U/D)
"A" - Add new FIFO cost queue
"U" - Update existing FIFO cost queue
"D" - Delete existing FIFO cost queue (Technically, this is more of voiding/deactivating the FIFO since we don't delete historical FIFO records).  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BinType:str = obj["BinType"]
      """  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  Calendar month of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl..  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  CycleSeq of the CCDtl record that this PartTran adjustment relates to (populated by post counts). Company, Site, WareHouseCode, CCYear, CCMonth,  InvAdjSrc, CCCycleSeq and PartNum fields are used to link to CCDtl.  """  
      self.ABTUID:str = obj["ABTUID"]
      """  GUID - reference on PE ABT.  """  
      self.BaseCostMethod:str = obj["BaseCostMethod"]
      """  Defines the Costing method that was used to create the transaction.   A =  Average L= Last S = Standard. This is duplicated from the PartSite.CostMethod or Part.CostMethod  """  
      self.RevertStatus:int = obj["RevertStatus"]
      """   Revert Status field, with following values:
0.	Not reverted (default initial value)
1.	Reverted  """  
      self.RevertID:str = obj["RevertID"]
      """  Reference on revert line  by SySRowID.  """  
      self.DropShipPackSlip:str = obj["DropShipPackSlip"]
      """  Drop shipment Packing Slip.  """  
      self.VarTarget:str = obj["VarTarget"]
      """   PartTran.VarTarget, with following values:
'JOB' ? Use Job Expense Account
'STK' ? Use Inventory Account
'VAR' ? Use Purchase Variance Account
'INS' ? Use Inspection Account
'UKN' ? Expense Account (Miscellaneous receipt)
'MTL' ? Use WIP Material Account
'SUB' ? Use WIP Subcontract account
'DMR' ? Use DMR account
'REJ' ? Use DMR Write off Account
'ACA' ? Use Actual Cost Account  """  
      self.FIFOSubSeq:int = obj["FIFOSubSeq"]
      """  The FIFO subsequence number of the related PartFIFOCost record.  """  
      self.AltMtlUnitCost:int = obj["AltMtlUnitCost"]
      """  Alternate FIFO Material Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltLbrUnitCost:int = obj["AltLbrUnitCost"]
      """  Alternate FIFO Labor Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltBurUnitCost:int = obj["AltBurUnitCost"]
      """  Alternate FIFO Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltSubUnitCost:int = obj["AltSubUnitCost"]
      """  Alternate FIFO Subcontract Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlBurUnitCost:int = obj["AltMtlBurUnitCost"]
      """  Alternate FIFO Material Burden Unit Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltExtCost:int = obj["AltExtCost"]
      """  Alternate FIFO Extended Cost used when maintaining FIFO cost record (PartFIFOCost) for non-FIFO costed part.  """  
      self.AltMtlMtlUnitCost:int = obj["AltMtlMtlUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlLabUnitCost:int = obj["AltMtlLabUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlSubUnitCost:int = obj["AltMtlSubUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.AltMtlBurdenUnitCost:int = obj["AltMtlBurdenUnitCost"]
      """  Breakdown of AltMtlUnit cost into individual components. AltMtlUnitCost = AltMtlMtlUnitCost + AltMtlLabUnitCost + AltMtlBurdenUnitCost + AltMtlSubUnitCost.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  Invoice Number from Progress Billing Invoice preparation  """  
      self.LoanFlag:str = obj["LoanFlag"]
      """   This is only relevant for TranType MFG-MFG.
Valid types are '' , 'L', and 'B'.  
For Transfers, set to ''.
For Loans and Repayment of Loans set PartTran. LoanType to either 'L' or 'B' based on PartTran.JobNum.  If PartTran.JobNum is the job who is making the loan (or who made the loan, in the case of a repayment), then set to 'L' (loaner).  If PartTran.JobNum is the job who originally received the loan or who is receiving a loan set to 'B' (borrower).  """  
      self.AssetNum:str = obj["AssetNum"]
      """  Unique identifier of the Asset.  """  
      self.AdditionNum:int = obj["AdditionNum"]
      """  Unique number to identify the Addition activity of an asset.  """  
      self.DisposalNum:int = obj["DisposalNum"]
      """  Unique number to identify the Disposal activity of an asset.  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used by Project Analysis process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process  """  
      self.MscNum:int = obj["MscNum"]
      """  Like RcvMisc.MscNum. Filled only for ADJ-PUR transactions created from late costs.  """  
      self.ODCUnitCost:int = obj["ODCUnitCost"]
      """  ODC Unit Cost  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TranRefType:int = obj["TranRefType"]
      """  TranRefType  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.PCIDCollapseCounter:int = obj["PCIDCollapseCounter"]
      """  PCIDCollapseCounter  """  
      self.PCID2:str = obj["PCID2"]
      """  PCID2  """  
      self.ContractID:str = obj["ContractID"]
      """  ContractID  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  """  
      self.ExtMtlCost:int = obj["ExtMtlCost"]
      """  ExtMtlCost  """  
      self.ExtLbrCost:int = obj["ExtLbrCost"]
      """  ExtLbrCost  """  
      self.ExtBurCost:int = obj["ExtBurCost"]
      """  ExtBurCost  """  
      self.ExtSubCost:int = obj["ExtSubCost"]
      """  ExtSubCost  """  
      self.ExtMtlBurCost:int = obj["ExtMtlBurCost"]
      """  ExtMtlBurCost  """  
      self.ExtMtlMtlCost:int = obj["ExtMtlMtlCost"]
      """  ExtMtlMtlCost  """  
      self.ExtMtlLabCost:int = obj["ExtMtlLabCost"]
      """  ExtMtlLabCost  """  
      self.ExtMtlSubCost:int = obj["ExtMtlSubCost"]
      """  ExtMtlSubCost  """  
      self.ExtMtlBurdenCost:int = obj["ExtMtlBurdenCost"]
      """  ExtMtlBurdenCost  """  
      self.MYImportNum:str = obj["MYImportNum"]
      """  MYImportNum  """  
      self.AutoReverse:bool = obj["AutoReverse"]
      """  AutoReverse  """  
      self.RevTranNum:int = obj["RevTranNum"]
      """  RevTranNum  """  
      self.RevSysDate:str = obj["RevSysDate"]
      """  RevSysDate  """  
      self.RevSysTime:int = obj["RevSysTime"]
      """  RevSysTime  """  
      self.ExtNonRecoverableCost:int = obj["ExtNonRecoverableCost"]
      """  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.WIPPCID:str = obj["WIPPCID"]
      """  WIPPCID  """  
      self.WIPPCID2:str = obj["WIPPCID2"]
      """  WIPPCID2  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.DIMDescription:str = obj["DIMDescription"]
      self.DisableFieldPart:bool = obj["DisableFieldPart"]
      """  Part field objects must be enabled when the Final Assembly (0) is selected and the Job has multiple end parts.  """  
      self.DispSysTime:str = obj["DispSysTime"]
      """  Display format of System Time in Hrs:Min.  """  
      self.DispUOM:str = obj["DispUOM"]
      self.dummyKeyField:str = obj["dummyKeyField"]
      self.EnableSerialNumbers:bool = obj["EnableSerialNumbers"]
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  If InvAdjSrc = "P", then this field is true, InvAdjSrc = "C", then this field is false  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.InvBurUnitCost:int = obj["InvBurUnitCost"]
      """  Inventory subcontract unit cost  """  
      self.InvLbrUnitCost:int = obj["InvLbrUnitCost"]
      """  Inventory Labor unit cost.  """  
      self.InvMtlBurUnitCost:int = obj["InvMtlBurUnitCost"]
      """  Inventory burden unit cost  """  
      self.InvMtlUnitCost:int = obj["InvMtlUnitCost"]
      """  Inventory material unit cost  """  
      self.InvSubUnitCost:int = obj["InvSubUnitCost"]
      """  Inventory subcontract unit cost.  """  
      self.IssuedComplete:bool = obj["IssuedComplete"]
      self.JobBurUnitCost:int = obj["JobBurUnitCost"]
      self.JobLbrUnitCost:int = obj["JobLbrUnitCost"]
      self.JobMtlBurUnitCost:int = obj["JobMtlBurUnitCost"]
      self.JobMtlUnitCost:int = obj["JobMtlUnitCost"]
      self.JobSubUnitCost:int = obj["JobSubUnitCost"]
      self.LegalNumberNumber:str = obj["LegalNumberNumber"]
      self.LegalNumberPrefix:str = obj["LegalNumberPrefix"]
      self.LegalNumberPrefixList:str = obj["LegalNumberPrefixList"]
      self.LegalNumberReadOnlyFields:str = obj["LegalNumberReadOnlyFields"]
      self.LegalNumberYear:int = obj["LegalNumberYear"]
      self.MtlLbrUnitCost:int = obj["MtlLbrUnitCost"]
      self.MtlQueueRowId:str = obj["MtlQueueRowId"]
      self.MultiEndParts:bool = obj["MultiEndParts"]
      """  Used/Set only by MfgReceipts - Indicates if Job has multiple end parts.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      self.OverRideCosts:bool = obj["OverRideCosts"]
      """  Override Costs.  Set to yes if the user chooses to override the cost.  """  
      self.PartDescriptionAsm:str = obj["PartDescriptionAsm"]
      self.PartDescriptionJH:str = obj["PartDescriptionJH"]
      self.PartDescriptionMS:str = obj["PartDescriptionMS"]
      self.PartDescriptionSP:str = obj["PartDescriptionSP"]
      self.PartNumAsm:str = obj["PartNumAsm"]
      self.PartNumJH:str = obj["PartNumJH"]
      self.PartNumMS:str = obj["PartNumMS"]
      self.PartNumSP:str = obj["PartNumSP"]
      self.QtyAvailToComplete:int = obj["QtyAvailToComplete"]
      self.QtyBearing:bool = obj["QtyBearing"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      """  Quantity Completed  """  
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SalvageQtyToDate:int = obj["SalvageQtyToDate"]
      self.SerialNoTempTranID:int = obj["SerialNoTempTranID"]
      self.ThisTranQty:int = obj["ThisTranQty"]
      self.TranAmount:int = obj["TranAmount"]
      """  Transaction Amount  """  
      self.TreeDisplay:str = obj["TreeDisplay"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.CostMethodDisplay:str = obj["CostMethodDisplay"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts  """  
      self.RevisionNumAsm:str = obj["RevisionNumAsm"]
      self.RevisionNumMS:str = obj["RevisionNumMS"]
      self.RevisionNumSP:str = obj["RevisionNumSP"]
      self.PlantConfCtrlEnablePackageControl:bool = obj["PlantConfCtrlEnablePackageControl"]
      self.AttributeSetDescriptionMS:str = obj["AttributeSetDescriptionMS"]
      """  Description for AttributeSetID associated with PartNumMS  """  
      self.AttributeSetIDMS:int = obj["AttributeSetIDMS"]
      """  AttributeSetID associated with PartNumMS  """  
      self.AttributeSetShortDescriptionMS:str = obj["AttributeSetShortDescriptionMS"]
      """  AttributeSetShortDescription associated with PartNumMS  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AssemblySeqDescription:str = obj["AssemblySeqDescription"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CallLineLineDesc:str = obj["CallLineLineDesc"]
      self.CustNumCustID:str = obj["CustNumCustID"]
      self.CustNumBTName:str = obj["CustNumBTName"]
      self.CustNumName:str = obj["CustNumName"]
      self.DimCodeDimCodeDescription:str = obj["DimCodeDimCodeDescription"]
      self.DMRNumPartDescription:str = obj["DMRNumPartDescription"]
      self.FromBinDescription:str = obj["FromBinDescription"]
      self.FromPlantName:str = obj["FromPlantName"]
      self.FromWareHouseDescription:str = obj["FromWareHouseDescription"]
      self.InvoiceNumDescription:str = obj["InvoiceNumDescription"]
      self.JobNumPartDescription:str = obj["JobNumPartDescription"]
      self.MatNumLineDesc:str = obj["MatNumLineDesc"]
      self.OrderLineLineDesc:str = obj["OrderLineLineDesc"]
      self.OrderNumCardMemberName:str = obj["OrderNumCardMemberName"]
      self.OrderNumCurrencyCode:str = obj["OrderNumCurrencyCode"]
      self.PackLineLineDesc:str = obj["PackLineLineDesc"]
      self.PackNumName:str = obj["PackNumName"]
      self.PartLotPartLotDescription:str = obj["PartLotPartLotDescription"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PlantName:str = obj["PlantName"]
      self.POLineVenPartNum:str = obj["POLineVenPartNum"]
      self.POLinePartNum:str = obj["POLinePartNum"]
      self.POLineLineDesc:str = obj["POLineLineDesc"]
      self.RMALineLineDesc:str = obj["RMALineLineDesc"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorPPNumAddress1:str = obj["VendorPPNumAddress1"]
      self.VendorPPNumAddress2:str = obj["VendorPPNumAddress2"]
      self.VendorPPNumPrimPCon:int = obj["VendorPPNumPrimPCon"]
      self.VendorPPNumAddress3:str = obj["VendorPPNumAddress3"]
      self.VendorPPNumCountry:str = obj["VendorPPNumCountry"]
      self.VendorPPNumState:str = obj["VendorPPNumState"]
      self.VendorPPNumZip:str = obj["VendorPPNumZip"]
      self.VendorPPNumCity:str = obj["VendorPPNumCity"]
      self.VendorPPNumName:str = obj["VendorPPNumName"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlHeaderRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.Plant:str = obj["Plant"]
      """  Site where the PCID is currently located.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse where the PCID is currently located.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin where the PCID is currently located.  """  
      self.ReturnToWarehouseCode:str = obj["ReturnToWarehouseCode"]
      """  Warehouse where the PCID return stock needs to be returned to.  """  
      self.ReturnToBinNum:str = obj["ReturnToBinNum"]
      """  Warehouse Bin where the PCID return stock needs to be returned to.  """  
      self.PkgControlStatus:str = obj["PkgControlStatus"]
      """  PCID current status.  """  
      self.PkgControlPriorStatus:str = obj["PkgControlPriorStatus"]
      """  PCID prior status.  """  
      self.LabelPrintControlStatus:str = obj["LabelPrintControlStatus"]
      """  Label Print Control status.  """  
      self.LabelPrintControlPriorStatus:str = obj["LabelPrintControlPriorStatus"]
      """  Label Print Control prior status.  """  
      self.AllowParentPCID:bool = obj["AllowParentPCID"]
      """  If false then PCID is a single-level PCID that cannot be associated with a Parent.  """  
      self.AllowMixedParts:bool = obj["AllowMixedParts"]
      """  If false then PCID must contain only one PartNum.  """  
      self.AllowMixedLots:bool = obj["AllowMixedLots"]
      """  If false then PCID must contain only one LotNum for each Part on the PCID.  """  
      self.AllowMixedUOMs:bool = obj["AllowMixedUOMs"]
      """  If false then PCID must contain only one UOM per Part on the PCID.  """  
      self.AllowMixedChildPCIDs:bool = obj["AllowMixedChildPCIDs"]
      """  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM, or Part Quantity per child PCID.  This is referred to as a Master PCID, otherwise it would be referred to as a MixedMaster PCID.  """  
      self.AllowMultipleSerialNumPerPCID:bool = obj["AllowMultipleSerialNumPerPCID"]
      """  If false then PCID must contain only one Serial Number per PCID.  """  
      self.LabelPrintControlled:bool = obj["LabelPrintControlled"]
      """  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  """  
      self.LabelPrintCounter:bool = obj["LabelPrintCounter"]
      """  If false then the number of PCID label prints will not be tracked.  """  
      self.AllowVoids:bool = obj["AllowVoids"]
      """  If false then PkgControlHeader and PkgControlItem cannot be voided or deleted.  """  
      self.AllowDeletes:bool = obj["AllowDeletes"]
      """  If false then PkgControlHeader and PkgControlItem cannot be deleted.  """  
      self.ArchivePCIDHistory:bool = obj["ArchivePCIDHistory"]
      """  If true then PkgControlHeader and PkgControlItem will be written to history tables and removed from the maintenance tables on void, delete or close/collapse.  """  
      self.PkgCode:str = obj["PkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.LWHDimensionUOM:str = obj["LWHDimensionUOM"]
      """  User defined code which uniquely identifies the UOM for length, width, and height.  """  
      self.Length:int = obj["Length"]
      """  Length dimension.  """  
      self.Width:int = obj["Width"]
      """  Width dimension.  """  
      self.Height:int = obj["Height"]
      """  Height dimension.  """  
      self.VolumeUOM:str = obj["VolumeUOM"]
      """  User defined code which uniquely identifies the UOM for volume.  """  
      self.Volume:int = obj["Volume"]
      """  Volume.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  User defined code which uniquely identifies the UOM for weight.  """  
      self.MaximumWeight:int = obj["MaximumWeight"]
      """  Maximum Weight.  """  
      self.CalculatedWeight:int = obj["CalculatedWeight"]
      """  Calculated Weight.  """  
      self.TotalWeight:int = obj["TotalWeight"]
      """  The total weight of the parts and the container combined.  """  
      self.MaximumStack:int = obj["MaximumStack"]
      """  Maximum number of PCIDs allowed if vertically stacked.  """  
      self.PositionSeq:int = obj["PositionSeq"]
      """  Position Sequence within a parent PCID.  """  
      self.TrailerID:str = obj["TrailerID"]
      """  Trailer ID.  """  
      self.SecuritySealID:str = obj["SecuritySealID"]
      """  Bond or Security Seal ID.  """  
      self.RawPCIDLicensePlate:str = obj["RawPCIDLicensePlate"]
      """  Raw PCID as scanned or generated.  """  
      self.GS1128:str = obj["GS1128"]
      """  GS1-128 as generated by the Legal Number process.  GS1-128 supersedes the former UCC/EAN128 standards.  """  
      self.PkgControlCollapseCounter:int = obj["PkgControlCollapseCounter"]
      """  For a static PCID, each time the PCID is collapsed this counter is incremented, and the collapse counter is stamped on any PartTran records generated throughout the life of the PCID.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  System date and time when the row was created.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID that created this row.  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  System date and time when the row was last updated.  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  The user ID that last updated this row.  """  
      self.LastPCIDScanned:str = obj["LastPCIDScanned"]
      """  Last PCID Scanned.  """  
      self.NumberOfPCIDs:int = obj["NumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.AutoPrint:bool = obj["AutoPrint"]
      """  Flag used to fire the auto print rule that will print the labels.  """  
      self.LPCCreatedDate:str = obj["LPCCreatedDate"]
      """  System date and time when the row was created.  """  
      self.LPCCreatedBy:str = obj["LPCCreatedBy"]
      """  The user ID that created this record.  """  
      self.LPCPrinterID:str = obj["LPCPrinterID"]
      """  Printer ID that printed the label.  """  
      self.LPCPrintedBy:str = obj["LPCPrintedBy"]
      """  User that printed the label.  """  
      self.LPCPrintedFromTx:str = obj["LPCPrintedFromTx"]
      """  Label feature. Displays what transaction the label was printed from.  """  
      self.LPCPrintedFromTxType:str = obj["LPCPrintedFromTxType"]
      """  Ad Hoc feature. Displays what transaction type the label was printed from.  """  
      self.LPCJobNum:str = obj["LPCJobNum"]
      """  The job for which the label was printed.  """  
      self.LPCOprSeq:int = obj["LPCOprSeq"]
      """  The operation sequence for which the label was printed.  """  
      self.LPCAssemblySeq:int = obj["LPCAssemblySeq"]
      """  The assembly sequence for which the label was printed.  """  
      self.LPCShift:int = obj["LPCShift"]
      """  Shift that the label was created on or shift entered in Ad Hoc print program.  """  
      self.LPCOperatorEmpID:str = obj["LPCOperatorEmpID"]
      """  Operator who created the label if printed from MES, Labor Reporting employee if printed from Ad Hoc Manufacturing Backup, or blank otherwise.  """  
      self.OriginalSourcePCID:str = obj["OriginalSourcePCID"]
      """  Original Source PCID for repack. This field will be populated with the source container PCID when assigning a repack label.  """  
      self.OverlaidByPCID:str = obj["OverlaidByPCID"]
      """  This field will be populated with the new PCID that replaced this PCID when using the overlay feature.  """  
      self.Overlaid:bool = obj["Overlaid"]
      """  Set to True when PCID has been overlaid using the overlay feature.  """  
      self.ContainerPartial:bool = obj["ContainerPartial"]
      """  Partial Container – set to true when the container is created from the Ad Hoc – Partial program.  """  
      self.ContainerRepacked:bool = obj["ContainerRepacked"]
      """  If true the container was repacked.  """  
      self.ContainerReturnable:bool = obj["ContainerReturnable"]
      """  If true the container used is a returnable container.  """  
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      """  Our Vendor ID for the Customer being Shipped To.  """  
      self.PlantName:str = obj["PlantName"]
      """  Site Name.  """  
      self.PlantAddress1:str = obj["PlantAddress1"]
      """  Site Address line 1.  """  
      self.PlantAddress2:str = obj["PlantAddress2"]
      """  Site Address line 2.  """  
      self.PlantAddress3:str = obj["PlantAddress3"]
      """  Site Address line 3.  """  
      self.PlantCity:str = obj["PlantCity"]
      """  Site City.  """  
      self.PlantState:str = obj["PlantState"]
      """  Site State.  """  
      self.PlantZip:str = obj["PlantZip"]
      """  Site Zip.  """  
      self.PlantCountryNum:int = obj["PlantCountryNum"]
      """  Site Country Number.  """  
      self.PlantCountryDesc:str = obj["PlantCountryDesc"]
      """  Site Country Description.  """  
      self.PlantPhone:str = obj["PlantPhone"]
      """  Site Phone.  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack Number if applicable.  """  
      self.CustContainerPartNum:str = obj["CustContainerPartNum"]
      """  Ship To Customer Container Part Number.  """  
      self.EDIShipToNum:str = obj["EDIShipToNum"]
      """  EDI Ship To Number populated with the final destination if shipping to an Intermediate Consignee, otherwise an actual ShipToNum.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  Ship To Number.  """  
      self.ShipToName:str = obj["ShipToName"]
      """  Name of the Ship To that the PCID is going to.  """  
      self.ShipToAddress1:str = obj["ShipToAddress1"]
      """  Address line 1 of the Ship To that the PCID is going to.  """  
      self.ShipToAddress2:str = obj["ShipToAddress2"]
      """  Address line 2 of the Ship To that the PCID is going to.  """  
      self.ShipToAddress3:str = obj["ShipToAddress3"]
      """  Address line 3 of the Ship To that the PCID is going to.  """  
      self.ShipToCity:str = obj["ShipToCity"]
      """  City of the Ship To that the PCID is going to.  """  
      self.ShipToState:str = obj["ShipToState"]
      """  State of the Ship To that the PCID is going to.  """  
      self.ShipToZip:str = obj["ShipToZip"]
      """  Zip of the Ship To that the PCID is going to.  """  
      self.ShipToCountryNum:int = obj["ShipToCountryNum"]
      """  Country number of the Ship To that the PCID is going to.  """  
      self.ShipToCountryDesc:str = obj["ShipToCountryDesc"]
      """  Country of the Ship To that the PCID is going to.  """  
      self.ShipToDock:str = obj["ShipToDock"]
      """  The dock that the parts should be shipped to.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number.  """  
      self.VendorID:str = obj["VendorID"]
      """  Vendor ID.  """  
      self.VendorPurPoint:str = obj["VendorPurPoint"]
      """  Vendor Purchase Point.  """  
      self.VendorAddress1:str = obj["VendorAddress1"]
      """  Vendor Address line 1.  """  
      self.VendorAddress2:str = obj["VendorAddress2"]
      """  Vendor Address line 2.  """  
      self.VendorAddress3:str = obj["VendorAddress3"]
      """  Vendor Address line 3.  """  
      self.VendorCity:str = obj["VendorCity"]
      """  Vendor City.  """  
      self.VendorState:str = obj["VendorState"]
      """  Vendor State.  """  
      self.VendorZip:str = obj["VendorZip"]
      """  Vendor Zip.  """  
      self.VendorCountryNum:int = obj["VendorCountryNum"]
      """  Vendor Country Number.  """  
      self.VendorCountryDesc:str = obj["VendorCountryDesc"]
      """  Vendor Country Description.  """  
      self.OurDock:str = obj["OurDock"]
      """  Our Dock ID.  """  
      self.LabelValue01:str = obj["LabelValue01"]
      """  Value to display on package control label.  """  
      self.LabelValue02:str = obj["LabelValue02"]
      """  Value to display on package control label.  """  
      self.LabelValue03:str = obj["LabelValue03"]
      """  Value to display on package control label.  """  
      self.LabelValue04:str = obj["LabelValue04"]
      """  Value to display on package control label.  """  
      self.LabelValue05:str = obj["LabelValue05"]
      """  Value to display on package control label.  """  
      self.LabelValue06:str = obj["LabelValue06"]
      """  Value to display on package control label.  """  
      self.LabelValue07:str = obj["LabelValue07"]
      """  Value to display on package control label.  """  
      self.LabelValue08:str = obj["LabelValue08"]
      """  Value to display on package control label.  """  
      self.LabelValue09:str = obj["LabelValue09"]
      """  Value to display on package control label.  """  
      self.LabelValue10:str = obj["LabelValue10"]
      """  Value to display on package control label.  """  
      self.LabelValue11:str = obj["LabelValue11"]
      """  Value to display on package control label.  """  
      self.LabelValue12:str = obj["LabelValue12"]
      """  Value to display on package control label.  """  
      self.LabelValue13:str = obj["LabelValue13"]
      """  Value to display on package control label.  """  
      self.LabelValue14:str = obj["LabelValue14"]
      """  Value to display on package control label.  """  
      self.LabelValue15:str = obj["LabelValue15"]
      """  Value to display on package control label.  """  
      self.LabelValue16:str = obj["LabelValue16"]
      """  Value to display on package control label.  """  
      self.LabelValue17:str = obj["LabelValue17"]
      """  Value to display on package control label.  """  
      self.LabelValue18:str = obj["LabelValue18"]
      """  Value to display on package control label.  """  
      self.LabelValue19:str = obj["LabelValue19"]
      """  Value to display on package control label.  """  
      self.LabelValue20:str = obj["LabelValue20"]
      """  Value to display on package control label.  """  
      self.LabelValue21:str = obj["LabelValue21"]
      """  Value to display on package control label.  """  
      self.LabelValue22:str = obj["LabelValue22"]
      """  Value to display on package control label.  """  
      self.LabelValue23:str = obj["LabelValue23"]
      """  Value to display on package control label.  """  
      self.LabelValue24:str = obj["LabelValue24"]
      """  Value to display on package control label.  """  
      self.LabelValue25:str = obj["LabelValue25"]
      """  Value to display on package control label.  """  
      self.LabelValue26:str = obj["LabelValue26"]
      """  Value to display on package control label.  """  
      self.LabelValue27:str = obj["LabelValue27"]
      """  Value to display on package control label.  """  
      self.LabelValue28:str = obj["LabelValue28"]
      """  Value to display on package control label.  """  
      self.LabelValue29:str = obj["LabelValue29"]
      """  Value to display on package control label.  """  
      self.LabelValue30:str = obj["LabelValue30"]
      """  Value to display on package control label.  """  
      self.PkgControlCharacter01:str = obj["PkgControlCharacter01"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter02:str = obj["PkgControlCharacter02"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter03:str = obj["PkgControlCharacter03"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter04:str = obj["PkgControlCharacter04"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter05:str = obj["PkgControlCharacter05"]
      """  Reserved for development use.  """  
      self.PkgControlDate01:str = obj["PkgControlDate01"]
      """  Reserved for development use.  """  
      self.PkgControlDate02:str = obj["PkgControlDate02"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean01:bool = obj["PkgControlBoolean01"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean02:bool = obj["PkgControlBoolean02"]
      """  Reserved for development use.  """  
      self.PkgControlInteger01:int = obj["PkgControlInteger01"]
      """  Reserved for development use.  """  
      self.PkgControlInteger02:int = obj["PkgControlInteger02"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal01:int = obj["PkgControlDecimal01"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal02:int = obj["PkgControlDecimal02"]
      """  Reserved for development use.  """  
      self.PkgControlType:str = obj["PkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      """  Package Control ID Code.  """  
      self.ExternalLength:int = obj["ExternalLength"]
      """  External Length dimension.  """  
      self.ExternalWidth:int = obj["ExternalWidth"]
      """  External Width dimension.  """  
      self.ExternalHeight:int = obj["ExternalHeight"]
      """  External Height dimension.  """  
      self.ExternalVolume:int = obj["ExternalVolume"]
      """  External Volume.  """  
      self.TareWeight:int = obj["TareWeight"]
      """  Tare Weight.  """  
      self.LabelPrintCount:int = obj["LabelPrintCount"]
      """  Incremental tally of number of times PCID label has been printed.  """  
      self.TrackExpendable:bool = obj["TrackExpendable"]
      """  Indicates if the expendable PCID will be tracked.  """  
      self.TrackReturnable:bool = obj["TrackReturnable"]
      """  Indicates if the returnable PCID will be tracked.  """  
      self.LabelType:str = obj["LabelType"]
      """  Label Type.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.CustNum:int = obj["CustNum"]
      """  Ship To Customer Number.  """  
      self.ContainerExpendable:bool = obj["ContainerExpendable"]
      """  Indicates if the PCID is expendable.  """  
      self.CustID:str = obj["CustID"]
      """  Ship To Customer ID.  """  
      self.CustName:str = obj["CustName"]
      """  Ship To Customer Name.  """  
      self.VendorName:str = obj["VendorName"]
      """  Vendor Name.  """  
      self.VendorPPName:str = obj["VendorPPName"]
      """  Vendor Purchase Point Name.  """  
      self.AdhocStagedInventory:bool = obj["AdhocStagedInventory"]
      """  True if the inventory referenced during Adhoc PCID had not yet been received and the PCID needed to be staged.  """  
      self.UpdatedByEmpID:str = obj["UpdatedByEmpID"]
      """  UpdatedByEmpID  """  
      self.RawBarcodeScan:str = obj["RawBarcodeScan"]
      """  Raw Barcode Scan prior to execution of any extract logic.  """  
      self.OutboundContainer:bool = obj["OutboundContainer"]
      """  OutboundContainer  """  
      self.BeforePackPkgControlStatus:str = obj["BeforePackPkgControlStatus"]
      """  PkgControlStatus value prior to being added to a pack.  """  
      self.BeforePackLabelPrintControlStatus:str = obj["BeforePackLabelPrintControlStatus"]
      """  LabelPrintControlStatus value prior to being added to a pack.  """  
      self.PackedFromSource:str = obj["PackedFromSource"]
      """  To indicate the source process when a PCID was added to a pack.  """  
      self.LastCountedDate:str = obj["LastCountedDate"]
      """  Date last counted.  Updated during the cycle count Posting Process.  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  TFPackNum  """  
      self.ChildPCIDCount:int = obj["ChildPCIDCount"]
      """  Child PCID count  """  
      self.EnableCboReasonCode:bool = obj["EnableCboReasonCode"]
      """  Indicates if EnableCboReasonCode control should be Enabled.  """  
      self.Expendable:bool = obj["Expendable"]
      """  if the PkgControlID is expendable  """  
      self.ExtensionDigit:int = obj["ExtensionDigit"]
      self.HHASN:bool = obj["HHASN"]
      """  Used for Handheld, this field will determine if the ASN (Advanced Ship Notice) has been sent/printed  """  
      self.HHItemIUM:str = obj["HHItemIUM"]
      self.HHItemPartNum:str = obj["HHItemPartNum"]
      self.HHItemQuantity:int = obj["HHItemQuantity"]
      """  Used for Handheld.  """  
      self.HHItemRevisionNum:str = obj["HHItemRevisionNum"]
      self.HHLabelStatus:str = obj["HHLabelStatus"]
      """  Used for HandHeld, it can be either PkgControlHeader.LabelPrintControlStatus OR PkgControlHeader.PkgControlStatus  """  
      self.HHPackSlip:int = obj["HHPackSlip"]
      """   Used for handHeld             
If PkgControlHeader.PkgControlType = Static then PkgControlHeader.PackNum
If PkgControlHeader.PkgControlType = Dynamic then PkgControlItem.PackNum  """  
      self.HHPackSlipList:str = obj["HHPackSlipList"]
      """  Used for HandHeld, It could contains a list of PackNum from the children  """  
      self.LWHDimUOM:str = obj["LWHDimUOM"]
      self.ParentBinNum:str = obj["ParentBinNum"]
      """  Warehouse Bin where the Parent PCID is currently located.  """  
      self.ParentCreatedDate:str = obj["ParentCreatedDate"]
      """  System date and time when the row was created.  """  
      self.ParentCustContainerPartNum:str = obj["ParentCustContainerPartNum"]
      """  Ship To Customer Container Part Number.  """  
      self.ParentCustID:str = obj["ParentCustID"]
      """  Parent Ship To Customer ID.  """  
      self.ParentLabelPrintControlled:bool = obj["ParentLabelPrintControlled"]
      """  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  """  
      self.ParentLabelPrintControlStatus:str = obj["ParentLabelPrintControlStatus"]
      """  Label Print Control status.  """  
      self.ParentLabelType:str = obj["ParentLabelType"]
      """  Label Type.  """  
      self.ParentNumberOfPCIDs:int = obj["ParentNumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.ParentPackNum:int = obj["ParentPackNum"]
      """  Pack Number if applicable.  """  
      self.ParentPCID:str = obj["ParentPCID"]
      """  Parent Package Control Identification Number  """  
      self.ParentPkgCode:str = obj["ParentPkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.ParentPkgCodePartNum:str = obj["ParentPkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.ParentPkgControlStatus:str = obj["ParentPkgControlStatus"]
      """  PCID current status.  """  
      self.ParentPkgControlType:str = obj["ParentPkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.ParentPlant:str = obj["ParentPlant"]
      """  Site where the Parent PCID is currently located.  """  
      self.ParentPlantName:str = obj["ParentPlantName"]
      """  Site Name.  """  
      self.ParentShipToNum:str = obj["ParentShipToNum"]
      """  Parent Ship To Number.  """  
      self.ParentWarehouseCode:str = obj["ParentWarehouseCode"]
      """  Warehouse where the Parent PCID is currently located.  """  
      self.ParentWhseDesc:str = obj["ParentWhseDesc"]
      self.PartDesc:str = obj["PartDesc"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.PkgType:str = obj["PkgType"]
      self.ReasonCode:str = obj["ReasonCode"]
      """  Reason Code  """  
      self.ResCodeIn:str = obj["ResCodeIn"]
      self.ResCodeOut:str = obj["ResCodeOut"]
      self.RTWhseDesc:str = obj["RTWhseDesc"]
      self.ShipToContainerPartID:str = obj["ShipToContainerPartID"]
      """  Ship To Container Part ID  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type  """  
      self.WhseDesc:str = obj["WhseDesc"]
      self.AdjustInventory:bool = obj["AdjustInventory"]
      """  Adjust Inventory  """  
      self.ContainerUOM:str = obj["ContainerUOM"]
      """  Container UOM  """  
      self.DisableReasonCode:bool = obj["DisableReasonCode"]
      self.EnableBtnVoidPCIDInv:bool = obj["EnableBtnVoidPCIDInv"]
      """  Indicates if BtnVoidPCIDInv control should be Enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BinDescription:str = obj["BinDescription"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlItemRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number  """  
      self.PCIDItemSeq:int = obj["PCIDItemSeq"]
      """  PCID Item Sequence  """  
      self.ItemPCID:str = obj["ItemPCID"]
      """  The PCID of the item in this PCID.  """  
      self.ItemPartNum:str = obj["ItemPartNum"]
      """  The Part Number of the item in this PCID.  """  
      self.ItemRevisionNum:str = obj["ItemRevisionNum"]
      """  The Revision Number of the item in this PCID.  """  
      self.ItemPartDesc:str = obj["ItemPartDesc"]
      """  The Part Description of the item in this PCID.  """  
      self.ItemLotNum:str = obj["ItemLotNum"]
      """  The Lot Number of the item in this PCID.  """  
      self.ItemIUM:str = obj["ItemIUM"]
      """  The Inventory UOM of the item in this PCID.  """  
      self.ItemQuantity:int = obj["ItemQuantity"]
      """  The Quantity of the item in this PCID.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.DemandType:str = obj["DemandType"]
      """  Demand Type.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  Order Number of the demand.  """  
      self.OrderLine:int = obj["OrderLine"]
      """  Order Line Number of the demand.  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  Order Release Number of the demand.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job Number of the demand.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly Sequence Number of the demand.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  Material Sequence Number of the demand.  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order Number of the demand.  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Transfer Order Line of the demand.  """  
      self.PackNum:int = obj["PackNum"]
      """  Pack Number if applicable.  """  
      self.PackLine:int = obj["PackLine"]
      """  Pack Line Number if applicable.  """  
      self.CustPartNum:str = obj["CustPartNum"]
      """  Ship To Customer Part Number.  """  
      self.CustPartRev:str = obj["CustPartRev"]
      """  Ship To Customer Part Revision.  """  
      self.CustPONum:str = obj["CustPONum"]
      """  The PO number that these parts were created against.  """  
      self.CustShipToEngineerAlert:str = obj["CustShipToEngineerAlert"]
      """  Engineering Alert to display on the label.  """  
      self.SafetyIndicator:bool = obj["SafetyIndicator"]
      """  Safety Indicator to display on the label.  """  
      self.PkgCodePartNum:str = obj["PkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.VendorPOType:str = obj["VendorPOType"]
      """  Purchase Order Type.  """  
      self.VendorPONum:int = obj["VendorPONum"]
      """  Purchase Order Number.  """  
      self.VendorPOLine:int = obj["VendorPOLine"]
      """  Purchase Order Line Number.  """  
      self.VendorPORelNum:int = obj["VendorPORelNum"]
      """  Purchase Order Release Number.  """  
      self.VendorPartNum:str = obj["VendorPartNum"]
      """  Supplier Part Number.  """  
      self.VendorUOM:str = obj["VendorUOM"]
      """  Supplier Unit of Measure.  """  
      self.VendorQty:int = obj["VendorQty"]
      """  Supplier Quantity.  """  
      self.ReceiptPackSlip:str = obj["ReceiptPackSlip"]
      """  Receipt Packing Slip.  """  
      self.ReceiptType:str = obj["ReceiptType"]
      """  Receipt Type.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt Date.  """  
      self.ReceiptUOM:str = obj["ReceiptUOM"]
      """  Receipt UOM.  """  
      self.ReceiptQty:int = obj["ReceiptQty"]
      """  Receipt Quantity.  """  
      self.RMANum:int = obj["RMANum"]
      """  RMA Number.  """  
      self.RMALine:int = obj["RMALine"]
      """  RMA Line.  """  
      self.PkgControlCharacter01:str = obj["PkgControlCharacter01"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter02:str = obj["PkgControlCharacter02"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter03:str = obj["PkgControlCharacter03"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter04:str = obj["PkgControlCharacter04"]
      """  Reserved for development use.  """  
      self.PkgControlCharacter05:str = obj["PkgControlCharacter05"]
      """  Reserved for development use.  """  
      self.PkgControlDate01:str = obj["PkgControlDate01"]
      """  Reserved for development use.  """  
      self.PkgControlDate02:str = obj["PkgControlDate02"]
      """  Reserved for development use.  """  
      self.PkgControlBoolean01:bool = obj["PkgControlBoolean01"]
      """  Reserved for development  """  
      self.PkgControlBoolean02:bool = obj["PkgControlBoolean02"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal01:int = obj["PkgControlDecimal01"]
      """  Reserved for development use.  """  
      self.PkgControlDecimal02:int = obj["PkgControlDecimal02"]
      """  Reserved for development use.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ShipmentInvoicedPosted:str = obj["ShipmentInvoicedPosted"]
      """  Set to INVOICED when invoice created, set to POSTED when invoice is posted.  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  The job number on which the quantity on this record were produced  """  
      self.ItemAttributeSetID:int = obj["ItemAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  TFPackNum  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  TFPackLine  """  
      self.ItemPicked:bool = obj["ItemPicked"]
      """  Set to true if this PkgControlItem record was created by processing a mtl queue picking record  """  
      self.ItemPartWipSysRowID:str = obj["ItemPartWipSysRowID"]
      """  SysRowID of the PartWip to which this item relates. The value is a GUID.  If the item is not WIP, this column is blank.  This value should only ever be populated in a Staging or History PCID, never an Inventory PCID.  """  
      self.TrackType:str = obj["TrackType"]
      """  Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.  "R" - Raw Material a part which was issued to the job.  "M" - Manufactured Part. The part that is being manufactured.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job operation sequence number that part is related to.  """  
      self.InNonConformance:bool = obj["InNonConformance"]
      """  Indicates if the WIP has been sent to Non-Conformance.  """  
      self.InDMRProcessing:bool = obj["InDMRProcessing"]
      """  Indicates if the WIP has failed Non-Conformance and has been moved to DMR Processing.  """  
      self.ChildPCIDOrPart:str = obj["ChildPCIDOrPart"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.NumberOfPCIDs:int = obj["NumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.PackageCode:str = obj["PackageCode"]
      self.PlantName:str = obj["PlantName"]
      """  Site Name.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse where the PCID is currently located.  """  
      self.WhseDesc:str = obj["WhseDesc"]
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin where the PCID is currently located.  """  
      self.ItemAttributeSetDescription:str = obj["ItemAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.ItemAttributeSetShortDescription:str = obj["ItemAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ItemPartAttrClassID:str = obj["ItemPartAttrClassID"]
      self.ItemType:str = obj["ItemType"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReceiptsFromMfgJobAsmblRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.PartNum:str = obj["PartNum"]
      self.Description:str = obj["Description"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.JobHeadPartNum:str = obj["JobHeadPartNum"]
      self.JobHeadPartDescription:str = obj["JobHeadPartDescription"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReceiptsFromMfgJobAsmblTableset:
   def __init__(self, obj):
      self.ReceiptsFromMfgJobAsmbl:list[Erp_Tablesets_ReceiptsFromMfgJobAsmblRow] = obj["ReceiptsFromMfgJobAsmbl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ReceiptsFromMfgTableset:
   def __init__(self, obj):
      self.PartTran:list[Erp_Tablesets_PartTranRow] = obj["PartTran"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.PkgControlHeader:list[Erp_Tablesets_PkgControlHeaderRow] = obj["PkgControlHeader"]
      self.PkgControlItem:list[Erp_Tablesets_PkgControlItemRow] = obj["PkgControlItem"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class Erp_Tablesets_SelectedReceiptsJobAsmblTableset:
   def __init__(self, obj):
      self.SelectedJobAsmbl:list[Erp_Tablesets_SelectedJobAsmblRow] = obj["SelectedJobAsmbl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_SelectedReceiptsPCIDTableset:
   def __init__(self, obj):
      self.PCIDReceiptsParams:list[Erp_Tablesets_PCIDReceiptsParamsRow] = obj["PCIDReceiptsParams"]
      self.PCIDReceiptsSelected:list[Erp_Tablesets_PCIDReceiptsSelectedRow] = obj["PCIDReceiptsSelected"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class ExecuteProcessPCID_input:
   """ Required : 
   pcid
   whse
   binNum
   pcProcessID
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  pcid  """  
      self.whse:str = obj["whse"]
      """  whse  """  
      self.binNum:str = obj["binNum"]
      """  binNum  """  
      self.pcProcessID:str = obj["pcProcessID"]
      """  Process ID that calls this method  """  
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class ExecuteProcessPCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pcMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listAvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name  """  
      self.fieldName:str = obj["fieldName"]
      """  Field Name  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDefaultTranDocTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.defaultTranDocTypeID:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDefaultWhseBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.defaultWhse:str = obj["parameters"]
      self.defaultWhseDesc:str = obj["parameters"]
      self.defaultBinNum:str = obj["parameters"]
      self.defaultBinDescription:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_ReceiptsFromMfgJobAsmblTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewJobAsmblMultiple_input:
   """ Required : 
   ds
   pcTranType
   pcProcessID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SelectedReceiptsJobAsmblTableset] = obj["ds"]
      self.pcTranType:str = obj["pcTranType"]
      """  Tran Type.  Determines the nature of Receipts  """  
      self.pcProcessID:str = obj["pcProcessID"]
      """  Process ID that calls this method  """  
      pass

class GetNewJobAsmblMultiple_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SelectedReceiptsJobAsmblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewJobAsmblSearch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SelectedReceiptsJobAsmblTableset] = obj["ds"]
      pass

class GetNewJobAsmblSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SelectedReceiptsJobAsmblTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPCIDParamsRow_input:
   """ Required : 
   dsSelectedPCID
   """  
   def __init__(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      pass

class GetNewPCIDParamsRow_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      pass

      """  output parameters  """  

class GetNewReceiptsFromMfgJobAsm_input:
   """ Required : 
   pcJobNum
   piAssemblySeq
   pcTranType
   pcProcessID
   ds
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job Number  """  
      self.piAssemblySeq:int = obj["piAssemblySeq"]
      """  Assembly Sequence  """  
      self.pcTranType:str = obj["pcTranType"]
      """  Tran Type.  Determines the nature of Receipts  """  
      self.pcProcessID:str = obj["pcProcessID"]
      """  Process ID that calls this method  """  
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class GetNewReceiptsFromMfgJobAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewReceiptsFromMfgMtlQueue_input:
   """ Required : 
   pcMtlQueueRowIdent
   ds
   dsSelectedPCID
   """  
   def __init__(self, obj):
      self.pcMtlQueueRowIdent:str = obj["pcMtlQueueRowIdent"]
      """  RowIdent of MtlQueue record  """  
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      pass

class GetNewReceiptsFromMfgMtlQueue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      pass

      """  output parameters  """  

class GetNewReceiptsFromMfg_input:
   """ Required : 
   pcTranType
   ds
   """  
   def __init__(self, obj):
      self.pcTranType:str = obj["pcTranType"]
      """  Tran Type. Determines the nature of Receipts  """  
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class GetNewReceiptsFromMfg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewReceiptsFromPCIDMultiple_input:
   """ Required : 
   dsSelectedPCID
   tranType
   processID
   """  
   def __init__(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.tranType:str = obj["tranType"]
      """  The transaction type.  """  
      self.processID:str = obj["processID"]
      """  The process identifier.  """  
      pass

class GetNewReceiptsFromPCIDMultiple_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      pass

      """  output parameters  """  

class GetNewReceiptsFromPCIDSupplyJobNum_input:
   """ Required : 
   dsSelectedPCID
   supplyJobNum
   tranType
   processID
   """  
   def __init__(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.supplyJobNum:str = obj["supplyJobNum"]
      """  The job number used to retrieve all the PCIDs associated.  """  
      self.tranType:str = obj["tranType"]
      """  The transaction type.  """  
      self.processID:str = obj["processID"]
      """  The process identifier.  """  
      pass

class GetNewReceiptsFromPCIDSupplyJobNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      pass

      """  output parameters  """  

class GetNewReceiptsFromPCID_input:
   """ Required : 
   dsSelectedPCID
   pcid
   tranType
   processID
   """  
   def __init__(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.pcid:str = obj["pcid"]
      """  The package control ID.  """  
      self.tranType:str = obj["tranType"]
      """  The transaction type.  """  
      self.processID:str = obj["processID"]
      """  The process identifier.  """  
      pass

class GetNewReceiptsFromPCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      pass

      """  output parameters  """  

class GetPCID_input:
   """ Required : 
   pcid
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  pcid  """  
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class GetPCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.isJobClosed:bool = obj["isJobClosed"]
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
      self.returnObj:list[Erp_Tablesets_ReceiptsFromMfgJobAsmblTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ds
   pcProcessID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcProcessID:str = obj["pcProcessID"]
      """  The name of the calling process (UI Application).  """  
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
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

class IsValidAssembly_input:
   """ Required : 
   pcJobNum
   piAssemblySeq
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  The job number  """  
      self.piAssemblySeq:int = obj["piAssemblySeq"]
      """  The assembly sequence number.  """  
      pass

class IsValidAssembly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.plFound:bool = obj["plFound"]
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

class OnChangeActTranQty_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeActTranQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeActTransUOM_input:
   """ Required : 
   pUOM
   ds
   """  
   def __init__(self, obj):
      self.pUOM:str = obj["pUOM"]
      """  Transaction UOM  """  
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeActTransUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeAssemblySeq2_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeAssemblySeq2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeAssemblySeq_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeAssemblySeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeBinNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCalculateExtCost_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeCalculateExtCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeExtCost_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeExtCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFromPCID_input:
   """ Required : 
   ipPCID
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.ipPCID:str = obj["ipPCID"]
      """  Proposed PCID value  """  
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      pass

class OnChangeFromPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobNum2_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeJobNum2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeJobNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobSeq2_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeJobSeq2_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeLotNum_input:
   """ Required : 
   ds
   messageasked
   ProposedLotNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.messageasked:bool = obj["messageasked"]
      """  Set by the UI. If set to true then lot messages will not be returned. If false, either pcMessage or errormsg will be set if there is an error.  """  
      self.ProposedLotNumber:str = obj["ProposedLotNumber"]
      """  Lot number the user entered.  """  
      pass

class OnChangeLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      self.errormsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeOverrideCost_input:
   """ Required : 
   ds
   ProposedOverride
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.ProposedOverride:bool = obj["ProposedOverride"]
      """  Override Cost value that the user selected.  """  
      pass

class OnChangeOverrideCost_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCIDParamWarehouseCode_input:
   """ Required : 
   dsSelectedPCID
   ds
   pcProcessID
   warehouseCode
   """  
   def __init__(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcProcessID:str = obj["pcProcessID"]
      """  The calling process identifier.  """  
      self.warehouseCode:str = obj["warehouseCode"]
      """  The to warehouse code.  """  
      pass

class OnChangePCIDParamWarehouseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCIDParamsBinNum_input:
   """ Required : 
   dsSelectedPCID
   ds
   binNum
   """  
   def __init__(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.binNum:str = obj["binNum"]
      """  The to bin number.  """  
      pass

class OnChangePCIDParamsBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCIDParamsPlant_input:
   """ Required : 
   dsSelectedPCID
   ds
   pcProcessID
   plant2
   """  
   def __init__(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcProcessID:str = obj["pcProcessID"]
      """  The calling process identifier.  """  
      self.plant2:str = obj["plant2"]
      """  The To Site.  """  
      pass

class OnChangePCIDParamsPlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCIDParamsTranDate_input:
   """ Required : 
   dsSelectedPCID
   ds
   tranDate
   """  
   def __init__(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.tranDate:str = obj["tranDate"]
      """  The transaction date.  """  
      pass

class OnChangePCIDParamsTranDate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCIDParamsTranDocTypeID_input:
   """ Required : 
   dsSelectedPCID
   ds
   tranDocTypeID
   """  
   def __init__(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.tranDocTypeID:str = obj["tranDocTypeID"]
      """  The transaction document type identifier.  """  
      pass

class OnChangePCIDParamsTranDocTypeID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCIDParamsTranReference_input:
   """ Required : 
   dsSelectedPCID
   ds
   tranReference
   """  
   def __init__(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.tranReference:str = obj["tranReference"]
      """  The transaction reference.  """  
      pass

class OnChangePCIDParamsTranReference_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   ds
   ProposedPartNum
   ipContinue
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.ProposedPartNum:str = obj["ProposedPartNum"]
      """  The proposed PartNum  """  
      self.ipContinue:bool = obj["ipContinue"]
      """  The action from user in response to the question sent in opMessage  """  
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangePlant_input:
   """ Required : 
   pcProcessID
   ds
   """  
   def __init__(self, obj):
      self.pcProcessID:str = obj["pcProcessID"]
      """  Process ID where this method is called From  """  
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangePlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSalvageJobSeq_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeSalvageJobSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeSalvagePartNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeSalvagePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeToPCID_input:
   """ Required : 
   ipPCID
   pCallProcess
   ds
   """  
   def __init__(self, obj):
      self.ipPCID:str = obj["ipPCID"]
      """  Proposed To PCID value  """  
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeToPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeTranQty_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeTranQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeWareHouseCode_input:
   """ Required : 
   pcProcessID
   ds
   """  
   def __init__(self, obj):
      self.pcProcessID:str = obj["pcProcessID"]
      """  Process ID where this method is called From  """  
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangeWareHouseCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.outMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangingRevisionNumMS_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangingRevisionNumMS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreProcessPCID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class PreProcessPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class PreUpdate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class PreUpdate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class ProcessPCID_input:
   """ Required : 
   pcid
   whse
   binNum
   pcProcessID
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  pcid  """  
      self.whse:str = obj["whse"]
      """  whse  """  
      self.binNum:str = obj["binNum"]
      """  binNum  """  
      self.pcProcessID:str = obj["pcProcessID"]
      """  Process ID that calls this method  """  
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class ProcessPCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pcMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ReceiveMfgPCIDtoInventoryMultiple_input:
   """ Required : 
   ds
   dsSelectedPCID
   pcProcessID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.pcProcessID:str = obj["pcProcessID"]
      """  The process calling this method.  """  
      pass

class ReceiveMfgPCIDtoInventoryMultiple_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      self.pcPartTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReceiveMfgPCIDtoInventory_input:
   """ Required : 
   ds
   dsSelectedPCID
   pcid
   pcProcessID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.pcid:str = obj["pcid"]
      """  The pcid that is to be received into inventory.  """  
      self.pcProcessID:str = obj["pcProcessID"]
      """  The process calling this method.  """  
      pass

class ReceiveMfgPCIDtoInventory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.dsSelectedPCID:list[Erp_Tablesets_SelectedReceiptsPCIDTableset] = obj["dsSelectedPCID"]
      self.pcMessage:str = obj["parameters"]
      self.pcPartTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReceiveMfgPartToInventory_input:
   """ Required : 
   ds
   pdSerialNoQty
   plNegQtyAction
   pcProcessID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pdSerialNoQty:int = obj["pdSerialNoQty"]
      """  The quantity of Serialized parts.  This value is returned by Serial # selector object.  """  
      self.plNegQtyAction:bool = obj["plNegQtyAction"]
      """  When TranQty changes, perform NegativeInventoryTest. Provide the answer of that test here.  """  
      self.pcProcessID:str = obj["pcProcessID"]
      """  The name ID of the UI process that's calling this procedure.  """  
      pass

class ReceiveMfgPartToInventory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      self.pcPartTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReceiveMfgPartToJob_input:
   """ Required : 
   ds
   pdSerialNoQty
   plNegQtyAction
   plIssuedComplete
   pcProcessID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pdSerialNoQty:int = obj["pdSerialNoQty"]
      """  The quantity of Serialized parts.  This value is returned by Serial # selector object.  """  
      self.plNegQtyAction:bool = obj["plNegQtyAction"]
      """  When TranQty changes, perform NegativeInventoryTest. Provide the answer of that test here.  """  
      self.plIssuedComplete:bool = obj["plIssuedComplete"]
      """  Issue Complete  """  
      self.pcProcessID:str = obj["pcProcessID"]
      """  The name ID of the UI process that's calling this procedure.  """  
      pass

class ReceiveMfgPartToJob_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      self.pcPartTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class ReceiveSalvagedPartToInventory_input:
   """ Required : 
   ds
   pcProcessID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcProcessID:str = obj["pcProcessID"]
      """  The name ID of the UI process that's calling this procedure.  """  
      pass

class ReceiveSalvagedPartToInventory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMessage:str = obj["parameters"]
      self.pcPartTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateFromJob_input:
   """ Required : 
   pcJobNum
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      pass

class ValidateFromJob_output:
   def __init__(self, obj):
      pass

class ValidatePCIDExists_input:
   """ Required : 
   pcid
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  pcid  """  
      pass

class ValidatePCIDExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.isJobClosed:bool = obj["isJobClosed"]
      pass

      """  output parameters  """  

class ValidatePCID_input:
   """ Required : 
   pcid
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  pcid  """  
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class ValidatePCID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.isJobClosed:bool = obj["isJobClosed"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   pcProcessID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      self.pcProcessID:str = obj["pcProcessID"]
      """  The ID of the calling process in UI  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

class ValidateWhseBinPCID_input:
   """ Required : 
   ToWhse
   ToBinNum
   """  
   def __init__(self, obj):
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse  """  
      self.ToBinNum:str = obj["ToBinNum"]
      """  Bin Num to validate  """  
      pass

class ValidateWhseBinPCID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateWhsePCIDAndGetDefaultBin_input:
   """ Required : 
   ToWhse
   """  
   def __init__(self, obj):
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse to validate.  """  
      pass

class ValidateWhsePCIDAndGetDefaultBin_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.defaultBinNum:str = obj["parameters"]
      self.defaultBinDescription:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateWhsePCID_input:
   """ Required : 
   ToWhse
   """  
   def __init__(self, obj):
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse to validate.  """  
      pass

class ValidateWhsePCID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class VerifySerialMatchAndPlanContract_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      pass

class VerifySerialMatchAndPlanContract_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReceiptsFromMfgTableset] = obj["ds"]
      self.pcMsg:str = obj["parameters"]
      self.piMsgType:int = obj["parameters"]
      self.pcPCBinAction:str = obj["parameters"]
      self.pcPCBinMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

