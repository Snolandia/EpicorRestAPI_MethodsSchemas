import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.InventoryQtyAdjSvc
# Description: Temporary datatables allow the user to enter data for
the quantity adjustments, serial numbers selected and
serial number formats.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CheckSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSN
   Description: Determines if serial numbers are required for this transaction
   OperationID: CheckSN
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSNFSA(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSNFSA
   OperationID: CheckSNFSA
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSNFSA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSNFSA_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPCIDAdjustmentInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPCIDAdjustmentInfo
   Description: Gets the InventoryQtyAdj and InventoryQtyAdjBrw datasets for the specified PCID.
   OperationID: GetPCIDAdjustmentInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPCIDAdjustmentInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCIDAdjustmentInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryQtyAdjForPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryQtyAdjForPCID
   Description: Gets the default InventoryQtyAdj values for the PCID and the Warehouse Bins (InventoryQtyAdjBrw)
   OperationID: GetInventoryQtyAdjForPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjForPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjForPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryQtyAdjPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryQtyAdjPCID
   Description: Gets the default values for the InventoryQtyAdj data table based on the PCID entered.
   OperationID: GetInventoryQtyAdjPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryQtyAdj(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryQtyAdj
   Description: Gets the default values for the InventoryQtyAdj data table based on the part
number entered.
   OperationID: GetInventoryQtyAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryQtyAdjForPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryQtyAdjForPart
   Description: Gets the default InventoryQtyAdj values for the Part and the Warehouse Bins (InventoryQtyAdjBrw)
   OperationID: GetInventoryQtyAdjForPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjForPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjForPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryQtyAdjBrwInclManaged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryQtyAdjBrwInclManaged
   Description: Gets the default values for the browse section of the adjustment screen (including SMI inventory)
   OperationID: GetInventoryQtyAdjBrwInclManaged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrwInclManaged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrwInclManaged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryQtyAdjBrwInclPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryQtyAdjBrwInclPCID
   Description: Gets the default values for the browse section of the adjustment screen (excluding SMI inventory and including PCID)
   OperationID: GetInventoryQtyAdjBrwInclPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrwInclPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrwInclPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryQtyAdjBrwInclPCIDInventoryTracking(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryQtyAdjBrwInclPCIDInventoryTracking
   Description: Gets the default values for the browse section of the adjustment screen (excluding SMI inventory and including PCID)
   OperationID: GetInventoryQtyAdjBrwInclPCIDInventoryTracking
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrwInclPCIDInventoryTracking_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrwInclPCIDInventoryTracking_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryQtyAdjBrw(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryQtyAdjBrw
   Description: Gets the default values for the browse section of the adjustment screen (excluding SMI inventory)
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInventoryQtyAdjBrwInventoryTracking(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInventoryQtyAdjBrwInventoryTracking
   Description: Gets the default values for the browse section of the adjustment screen (excluding SMI inventory)
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KitPartStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method KitPartStatus
   Description: Checks Part's type and returns warning message if the part is a Sales Kit.
   OperationID: KitPartStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/KitPartStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KitPartStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreSetInventoryQtyAdj(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreSetInventoryQtyAdj
   Description: This method performs multiple functions:
This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.
The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
            
And will auto select serial numbers if the adjustment is from a PCID and the entire PCID PartBin qty is being adjusted out.
   OperationID: PreSetInventoryQtyAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreSetInventoryQtyAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreSetInventoryQtyAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetInventoryQtyAdj(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetInventoryQtyAdj
   Description: Create Part Tran records from the Inventory QtyAdj dataset. If Serial numbers
are entered, SerialNo records and SNTran records are created.  If the Serial
number format is changed, the Part table will be updated with the information
provided in the SNFormat data table.
   OperationID: SetInventoryQtyAdj
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetInventoryQtyAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetInventoryQtyAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   OperationID: FindPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   OperationID: GetPartFromRowID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUOM
   OperationID: ChangeUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeBinNum
   Description: Validates that the bin entered is valid
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeWareHseCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeWareHseCode
   Description: Validates that the warehouse entered is valid
   OperationID: OnChangeWareHseCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeWareHseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWareHseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUnitOfMeasure(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUnitOfMeasure
   Description: Validates that the unit of measure entered is valid
   OperationID: OnChangeUnitOfMeasure
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUnitOfMeasure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUnitOfMeasure_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLotNum
   Description: Validates that the lotNum entered is valid
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePCID
   Description: Validates that the PCID entered is valid
   OperationID: OnChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSelectionAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSelectionAttributeSetID
   Description: Validates that the selectionAttributeSetID entered is valid
   OperationID: OnChangeSelectionAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSelectionAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSelectionAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingSelectionRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingSelectionRevisionNum
   Description: Call this method when the Revision changes.  Will select related bins.
   OperationID: OnChangingSelectionRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingSelectionRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSelectionRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingAdjustQuantity(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingAdjustQuantity
   Description: Logic for when the adjust quantity is changing
   OperationID: OnChangingAdjustQuantity
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingAdjustQuantity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAdjustQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingUnitOfMeasure(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingUnitOfMeasure
   Description: Logic for when the unit of measure is changing
   OperationID: OnChangingUnitOfMeasure
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingUnitOfMeasure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingUnitOfMeasure_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Logic for when the number of pieces is changing
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeUOM_input:
   """ Required : 
   UOM
   ds
   """  
   def __init__(self, obj):
      self.UOM:str = obj["UOM"]
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class ChangeUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckSNFSA_input:
   """ Required : 
   partNum
   warehouseCode
   binNum
   ipPCID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.binNum:str = obj["binNum"]
      self.ipPCID:str = obj["ipPCID"]
      """  PCID  """  
      pass

class CheckSNFSA_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.serialNumbersRequired:bool = obj["serialNumbersRequired"]
      pass

      """  output parameters  """  

class CheckSN_input:
   """ Required : 
   partNum
   warehouseCode
   ipPCID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.warehouseCode:str = obj["warehouseCode"]
      """  Warehouse Code  """  
      self.ipPCID:str = obj["ipPCID"]
      """  PCID  """  
      pass

class CheckSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.serialNumbersRequired:bool = obj["serialNumbersRequired"]
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

class Erp_Tablesets_InventoryQtyAdjRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.WareHseCode:str = obj["WareHseCode"]
      self.OnHandQty:int = obj["OnHandQty"]
      self.BinNum:str = obj["BinNum"]
      self.AdjustQuantity:int = obj["AdjustQuantity"]
      self.ReasonCode:str = obj["ReasonCode"]
      self.LotNum:str = obj["LotNum"]
      self.Reference:str = obj["Reference"]
      self.UnitOfMeasure:str = obj["UnitOfMeasure"]
      self.TransDate:str = obj["TransDate"]
      self.ReasonType:str = obj["ReasonType"]
      self.SerialNoQty:int = obj["SerialNoQty"]
      """  Total Serial number quantity  """  
      self.TempSerialNo:int = obj["TempSerialNo"]
      """  Temporary serial number  """  
      self.ReasonCodeReq:bool = obj["ReasonCodeReq"]
      """  Reason code required flag  """  
      self.AllowNegQty:bool = obj["AllowNegQty"]
      """  Determines if inventory level can be driven below zero.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.StkUOMCode:str = obj["StkUOMCode"]
      self.EnableSN:bool = obj["EnableSN"]
      """  True/False flag that determines if serial numbers are required for this transaction.  """  
      self.OnHandUOM:str = obj["OnHandUOM"]
      """  Unit of Measure that qualifies the OnHandQty.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.PCID:str = obj["PCID"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReasonCodeDescription:str = obj["ReasonCodeDescription"]
      self.MYImportNum:str = obj["MYImportNum"]
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  Related to an Epicor FSA transaction  """  
      self.ContractCode:str = obj["ContractCode"]
      """  Used by Epicor FSA  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Used by Epicor FSA  """  
      self.CallCode:str = obj["CallCode"]
      """  Used by Epicor FSA  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  FSA ContractNum  """  
      self.TrackSerialNo:bool = obj["TrackSerialNo"]
      self.FSABin:bool = obj["FSABin"]
      self.SelectionPCID:str = obj["SelectionPCID"]
      """  PCID used to populate the selection criteria.  This value is not used for update.  """  
      self.SelectionPartNum:str = obj["SelectionPartNum"]
      """  PartNum used to populate the selection criteria.  This value is not used for update.  """  
      self.SelectionPartDescription:str = obj["SelectionPartDescription"]
      """  The description of the selection part number.  """  
      self.AdvancedPackageControl:bool = obj["AdvancedPackageControl"]
      """  True/False that determines if Advanced Package Control is allowed.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.SelectionAttributeSetID:int = obj["SelectionAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SelectionAttributeSetDescription:str = obj["SelectionAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.SelectionAttributeSetShortDescription:str = obj["SelectionAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SelectionRevisionNum:str = obj["SelectionRevisionNum"]
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.PartTrackLots:bool = obj["PartTrackLots"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.PartSalesUM:str = obj["PartSalesUM"]
      self.PartPricePerCode:str = obj["PartPricePerCode"]
      self.PartSellingFactor:int = obj["PartSellingFactor"]
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.PartIUM:str = obj["PartIUM"]
      self.PartPartDescription:str = obj["PartPartDescription"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.WareHseDescription:str = obj["WareHseDescription"]
      self.WhseBinDescription:str = obj["WhseBinDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InventoryQtyAdjTableset:
   def __init__(self, obj):
      self.InventoryQtyAdj:list[Erp_Tablesets_InventoryQtyAdjRow] = obj["InventoryQtyAdj"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class FindPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      self.opMatchType:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AvailTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetInventoryQtyAdjBrwInclManaged_input:
   """ Required : 
   partNum
   wareHouseCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number for the adjustment.  """  
      self.wareHouseCode:str = obj["wareHouseCode"]
      """  Warehouse code used to get bin information.  """  
      pass

class GetInventoryQtyAdjBrwInclManaged_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryQtyAdjBrwTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.primaryBin:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetInventoryQtyAdjBrwInclPCIDInventoryTracking_input:
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
      """  Attribute Set ID used to get bin information. Bins are not filtered by Attribute Set ID if a zero is sent.  """  
      self.wareHouseCode:str = obj["wareHouseCode"]
      """  Warehouse code used to get bin information.  """  
      pass

class GetInventoryQtyAdjBrwInclPCIDInventoryTracking_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryQtyAdjBrwTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.primaryBin:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetInventoryQtyAdjBrwInclPCID_input:
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

class GetInventoryQtyAdjBrwInclPCID_output:
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

class GetInventoryQtyAdjForPCID_input:
   """ Required : 
   pcid
   doStatusValidation
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  The PCID to adjust  """  
      self.doStatusValidation:bool = obj["doStatusValidation"]
      """  Validate the PCID Status  """  
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class GetInventoryQtyAdjForPCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryQtyAdjBrwTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetInventoryQtyAdjForPart_input:
   """ Required : 
   partnumber
   uomCode
   ds
   """  
   def __init__(self, obj):
      self.partnumber:str = obj["partnumber"]
      """  The part to adjust  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM code if selected from part cross reference  """  
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class GetInventoryQtyAdjForPart_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryQtyAdjBrwTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetInventoryQtyAdjPCID_input:
   """ Required : 
   partnumber
   uomCode
   pcid
   """  
   def __init__(self, obj):
      self.partnumber:str = obj["partnumber"]
      """  Part number to adjust.  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      self.pcid:str = obj["pcid"]
      """  The parent PCID  """  
      pass

class GetInventoryQtyAdjPCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["returnObj"]
      pass

class GetInventoryQtyAdj_input:
   """ Required : 
   partnumber
   uomCode
   """  
   def __init__(self, obj):
      self.partnumber:str = obj["partnumber"]
      """  Part number to adjust.  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      pass

class GetInventoryQtyAdj_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["returnObj"]
      pass

class GetPCIDAdjustmentInfo_input:
   """ Required : 
   pcid
   doStatusValidations
   inventoryQtyAdj
   inventoryQtyAdjBrw
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  A PCID that has parts to be adjusted  """  
      self.doStatusValidations:bool = obj["doStatusValidations"]
      """  True if the status of the PCID should be validated  """  
      self.inventoryQtyAdj:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["inventoryQtyAdj"]
      self.inventoryQtyAdjBrw:list[Erp_Tablesets_InventoryQtyAdjBrwTableset] = obj["inventoryQtyAdjBrw"]
      pass

class GetPCIDAdjustmentInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.inventoryQtyAdj:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["inventoryQtyAdj"]
      self.inventoryQtyAdjBrw:list[Erp_Tablesets_InventoryQtyAdjBrwTableset] = obj["inventoryQtyAdjBrw"]
      pass

      """  output parameters  """  

class GetPartFromRowID_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      self.ipRowID:str = obj["ipRowID"]
      pass

class GetPartFromRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPartNum:str = obj["parameters"]
      self.opUOM:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   sysRowID
   rowType
   uomCode
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
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.uomCode:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ipCompany
   ipWareHseCode
   ipPartNum
   ipAttributeSetID
   ipAdjustQuantity
   ipBinNum
   ipUnitOfMeasure
   ipSysRowID
   ipPCID
   ipLotNum
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      self.ipWareHseCode:str = obj["ipWareHseCode"]
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      self.ipAdjustQuantity:int = obj["ipAdjustQuantity"]
      self.ipBinNum:str = obj["ipBinNum"]
      self.ipUnitOfMeasure:str = obj["ipUnitOfMeasure"]
      self.ipSysRowID:str = obj["ipSysRowID"]
      self.ipPCID:str = obj["ipPCID"]
      self.ipLotNum:str = obj["ipLotNum"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
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

class KitPartStatus_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number.  """  
      pass

class KitPartStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.kitMessage:str = obj["parameters"]
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

class OnChangeBinNum_input:
   """ Required : 
   binNum
   ds
   """  
   def __init__(self, obj):
      self.binNum:str = obj["binNum"]
      """  The proposed bin  """  
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class OnChangeBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLotNum_input:
   """ Required : 
   lotNum
   ds
   """  
   def __init__(self, obj):
      self.lotNum:str = obj["lotNum"]
      """  The proposed lot number  """  
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class OnChangeLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePCID_input:
   """ Required : 
   pcid
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  The proposed PCID number  """  
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class OnChangePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeSelectionAttributeSetID_input:
   """ Required : 
   selectionAttributeSetID
   ds
   """  
   def __init__(self, obj):
      self.selectionAttributeSetID:int = obj["selectionAttributeSetID"]
      """  The proposed attribute set id  """  
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class OnChangeSelectionAttributeSetID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryQtyAdjBrwTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeUnitOfMeasure_input:
   """ Required : 
   ium
   ds
   """  
   def __init__(self, obj):
      self.ium:str = obj["ium"]
      """  The proposed unit of measure  """  
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class OnChangeUnitOfMeasure_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeWareHseCode_input:
   """ Required : 
   wareHseCode
   ds
   """  
   def __init__(self, obj):
      self.wareHseCode:str = obj["wareHseCode"]
      """  The proposed warehouse  """  
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class OnChangeWareHseCode_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryQtyAdjBrwTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAdjustQuantity_input:
   """ Required : 
   adjustQuantity
   ds
   """  
   def __init__(self, obj):
      self.adjustQuantity:int = obj["adjustQuantity"]
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class OnChangingAdjustQuantity_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingSelectionRevisionNum_input:
   """ Required : 
   selectionRevisionNum
   ds
   """  
   def __init__(self, obj):
      self.selectionRevisionNum:str = obj["selectionRevisionNum"]
      """  The proposed Revision Number  """  
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class OnChangingSelectionRevisionNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InventoryQtyAdjBrwTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingUnitOfMeasure_input:
   """ Required : 
   unitOfMeasure
   ds
   """  
   def __init__(self, obj):
      self.unitOfMeasure:str = obj["unitOfMeasure"]
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class OnChangingUnitOfMeasure_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreSetInventoryQtyAdj_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class PreSetInventoryQtyAdj_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class SetInventoryQtyAdj_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      pass

class SetInventoryQtyAdj_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InventoryQtyAdjTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

