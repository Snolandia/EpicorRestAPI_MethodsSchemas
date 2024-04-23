import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PkgControlGenPCIDSvc
# Description: Class that handles the logic for the PCID generation. It is used in Adhoc Job Output, Partial, Ad Hoc and Overlay PCID screens.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_Init(epicorHeaders = None):
   """  
   Summary: Invoke method Init
   OperationID: Init
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Init_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetTempRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTempRow
   Description: Purpose: Creates a PkgControlGenPCID record. Get info from the input data.
Parameters:
<param name="ipJobNum">JobNum</param><param name="ipCustID">CustID</param><param name="ipXPartNum">Cross part num</param><param name="ipPartNum">PartNum from part master part, if available</param><param name="ipKeyFieldName">The keyfield can be JobNum, CustID or XPartNum</param><param name="ipWhoCalled">Name of the form that called this method</param><param name="isMES">is this called from MES</param><param name="empIDorUserID">EmpID or UserID</param><param name="ipRawPCID">Raw PCID value</param><param name="custXPrtRowID">User selected CustXPrt.SysRowID </param><returns>Erp.BO.PkgControlGenPCIDTableset</returns>
Notes:
   OperationID: GetTempRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTempRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTempRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPackageCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPackageCode
   Description: Purpose: Get next package code according to the sequence set in Part Maintenance
Parameters:
<param name="ipCompany">Current Company</param><param name="ipPartNum">Part Number</param><param name="refPkgCode">Package code, can be send as empty to get the first package code in the sequence</param><param name="outPkgCodeDesc">Package code description</param><param name="custNum">Customer Number</param><param name="shipToNum">ShipTo Number</param>
Notes:
   OperationID: GetPackageCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPackageCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPackageCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PerformMaterialMovement(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PerformMaterialMovement
   Description: PerformMaterialMovement
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GeneratePCIDList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GeneratePCIDList
   Description: This method will generate the PCID
   OperationID: GeneratePCIDList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePCIDList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePCIDList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GeneratePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GeneratePCID
   Description: This method will generate the PCID
   OperationID: GeneratePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GeneratePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GeneratePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NegativeInventoryTest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NegativeInventoryTest
   Description: check negative inventory
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSourcePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSourcePCID
   OperationID: ValidateSourcePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSourcePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSourcePCID
   Description: Logic to extract the source PCID
   OperationID: ChangeSourcePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWarehouseList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetWarehouseList
   OperationID: GetWarehouseList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetWarehouseList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarehouseList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetPCIDLabelTypeInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetPCIDLabelTypeInfo
   Description: Set PCID Label Type Info
   OperationID: SetPCIDLabelTypeInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetPCIDLabelTypeInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetPCIDLabelTypeInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReturnValidItems(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReturnValidItems
   Description: To get a list of history items to remove
   OperationID: ReturnValidItems
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReturnValidItems_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReturnValidItems_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CustomerChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CustomerChanged
   Description: Updates info when customer changes.
   OperationID: CustomerChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CustomerChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomerChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PkgControlGenPCIDXPartChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PkgControlGenPCIDXPartChanged
   Description: Called when XPartNum changes.  This method will additionally update customer information if a customer is not already selected when called from
Overlay Import
   OperationID: PkgControlGenPCIDXPartChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PkgControlGenPCIDXPartChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PkgControlGenPCIDXPartChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_XPartChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method XPartChanged
   Description: Updates info when customer part changes.
   OperationID: XPartChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/XPartChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/XPartChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ShipToChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ShipToChanged
   Description: Updates info when shipTo changes
   OperationID: ShipToChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ShipToChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ShipToChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PkgCodeChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PkgCodeChanged
   Description: Updates info when pkgCode changes
   OperationID: PkgCodeChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PkgCodeChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PkgCodeChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BinNumChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BinNumChanged
   Description: Updates info when BinNum changes
   OperationID: BinNumChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BinNumChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BinNumChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WarehouseCodeChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WarehouseCodeChanged
   Description: Updates info when Warehouse changes
   OperationID: WarehouseCodeChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarehouseCodeChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarehouseCodeChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateNumberToGen(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateNumberToGen
   Description: Validates number of PCIDs to generate
   OperationID: ValidateNumberToGen
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateNumberToGen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNumberToGen_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateShift(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateShift
   Description: Validates shift
   OperationID: ValidateShift
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateShift_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShift_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateXPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateXPart
   Description: Validates customer part
   OperationID: ValidateXPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateXPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateXPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePkgCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePkgCode
   Description: Validates package code
   OperationID: ValidatePkgCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePkgCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePkgCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateCustomer
   Description: Validates customer
   OperationID: ValidateCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateShipTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateShipTo
   Description: Validates ShipTo
   OperationID: ValidateShipTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateShipTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShipTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateJob(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateJob
   Description: Validates job number
   OperationID: ValidateJob
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateJob_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJob_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlGenPCIDSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BinNumChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

class BinNumChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSourcePCID_input:
   """ Required : 
   ds
   ipSourcePCID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      self.ipSourcePCID:str = obj["ipSourcePCID"]
      pass

class ChangeSourcePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPackageCodeAllocNegQty_input:
   """ Required : 
   ipCalledFrom
   ipPackageCode
   ipQty
   """  
   def __init__(self, obj):
      self.ipCalledFrom:str = obj["ipCalledFrom"]
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

class CustomerChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

class CustomerChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_PkgControlGenPCIDRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CurrentPkgCode:str = obj["CurrentPkgCode"]
      self.CustID:str = obj["CustID"]
      self.CustNum:int = obj["CustNum"]
      self.JobNum:str = obj["JobNum"]
      self.JobDate:str = obj["JobDate"]
      self.Name:str = obj["Name"]
      self.NumberToGen:int = obj["NumberToGen"]
      self.OprSeq:int = obj["OprSeq"]
      self.OurSupplierCode:str = obj["OurSupplierCode"]
      self.PartNum:str = obj["PartNum"]
      self.Plant:str = obj["Plant"]
      self.PONum:str = obj["PONum"]
      self.PrinterID:str = obj["PrinterID"]
      self.PrinterList:str = obj["PrinterList"]
      self.QtyPer:int = obj["QtyPer"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.Shift:int = obj["Shift"]
      self.ShipToContainerPartID:str = obj["ShipToContainerPartID"]
      self.ShipToName:str = obj["ShipToName"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.XPartNum:str = obj["XPartNum"]
      self.XRevisionNum:str = obj["XRevisionNum"]
      self.UOMCode:str = obj["UOMCode"]
      self.LabelType:str = obj["LabelType"]
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      self.PrintProgram:str = obj["PrintProgram"]
      self.CustomerList:str = obj["CustomerList"]
      self.ShipToList:str = obj["ShipToList"]
      self.PCID:str = obj["PCID"]
      self.PromptUser:bool = obj["PromptUser"]
      self.RowSeq:int = obj["RowSeq"]
      self.EnableCustPart:bool = obj["EnableCustPart"]
      """  Indicates if cust part can be enabled or not.  """  
      self.EnableQtyPer:bool = obj["EnableQtyPer"]
      """  Indicates if quantity per container can be enabled or not.  """  
      self.SourcePCID:str = obj["SourcePCID"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse code affected by the generation of the PCID in Ad hoc PCID  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin. Set in Ad hoc PCID  """  
      self.BinDesc:str = obj["BinDesc"]
      """  Warehouse bin description  """  
      self.NumLabelsToPrint:int = obj["NumLabelsToPrint"]
      """  Quantity of labels to print  """  
      self.EnableNumberToGen:bool = obj["EnableNumberToGen"]
      """  Indicates if the Number To Generate field should be enabled  """  
      self.WhoCalled:str = obj["WhoCalled"]
      """  Screen that is using the BO  """  
      self.ConvFactor:int = obj["ConvFactor"]
      self.WarehouseType:str = obj["WarehouseType"]
      """  Warehouse type. Some vaild options are STOCK, WIP and QUALITY  """  
      self.AdhocStagedInventory:bool = obj["AdhocStagedInventory"]
      """  When user sets to True the system will write out to the StageHeader and StageItem tables instead of the PCID Inventory tables (PkgControlHeader / PkgControlItem).  """  
      self.IsMES:bool = obj["IsMES"]
      self.EmpID:str = obj["EmpID"]
      self.ReportStyle:int = obj["ReportStyle"]
      """  Report style taken from the label type record  """  
      self.WhseDesc:str = obj["WhseDesc"]
      self.ScanPCID:str = obj["ScanPCID"]
      self.RawBarcodeScan:str = obj["RawBarcodeScan"]
      """  Raw barcode scanned PCID  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ShipToStdList:str = obj["ShipToStdList"]
      """  Ship To List using standard delimiters  """  
      self.WarehouseList:str = obj["WarehouseList"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlGenPCIDTableset:
   def __init__(self, obj):
      self.PkgControlGenPCID:list[Erp_Tablesets_PkgControlGenPCIDRow] = obj["PkgControlGenPCID"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GeneratePCIDList_input:
   """ Required : 
   whoCalled
   ds
   """  
   def __init__(self, obj):
      self.whoCalled:str = obj["whoCalled"]
      """  Form that is calling this method  """  
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

class GeneratePCIDList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The generated PCID  """  
      pass

   def parameters(self, obj):
      self.pcidRange:str = obj["parameters"]
      self.returnMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GeneratePCID_input:
   """ Required : 
   whoCalled
   ds
   """  
   def __init__(self, obj):
      self.whoCalled:str = obj["whoCalled"]
      """  Form that is calling this method  """  
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

class GeneratePCID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  The generated PCID  """  
      pass

   def parameters(self, obj):
      self.rangeMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPackageCode_input:
   """ Required : 
   ipCompany
   ipPartNum
   refPkgCode
   custNum
   shipToNum
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      self.ipPartNum:str = obj["ipPartNum"]
      self.refPkgCode:str = obj["refPkgCode"]
      self.custNum:int = obj["custNum"]
      self.shipToNum:str = obj["shipToNum"]
      pass

class GetPackageCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.refPkgCode:str = obj["parameters"]
      self.outPkgCodeDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetTempRow_input:
   """ Required : 
   ipJobNum
   ipCustID
   ipXPartNum
   ipPartNum
   ipKeyFieldName
   ipWhoCalled
   isMES
   empIDorUserID
   ipRawPCID
   custXPrtRowID
   """  
   def __init__(self, obj):
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipCustID:str = obj["ipCustID"]
      self.ipXPartNum:str = obj["ipXPartNum"]
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipKeyFieldName:str = obj["ipKeyFieldName"]
      self.ipWhoCalled:str = obj["ipWhoCalled"]
      self.isMES:bool = obj["isMES"]
      self.empIDorUserID:str = obj["empIDorUserID"]
      self.ipRawPCID:str = obj["ipRawPCID"]
      self.custXPrtRowID:str = obj["custXPrtRowID"]
      pass

class GetTempRow_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["returnObj"]
      pass

class GetWarehouseList_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class GetWarehouseList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.WarehouseList:str = obj["parameters"]
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

class Init_output:
   def __init__(self, obj):
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

class PerformMaterialMovement_input:
   """ Required : 
   ipPCID
   ds
   """  
   def __init__(self, obj):
      self.ipPCID:str = obj["ipPCID"]
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

class PerformMaterialMovement_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.legalNumberMessage:str = obj["parameters"]
      self.partTranPKs:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PkgCodeChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

class PkgCodeChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PkgControlGenPCIDXPartChanged_input:
   """ Required : 
   whoCalled
   ds
   """  
   def __init__(self, obj):
      self.whoCalled:str = obj["whoCalled"]
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

class PkgControlGenPCIDXPartChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ReturnValidItems_input:
   """ Required : 
   historyList
   returnList
   """  
   def __init__(self, obj):
      self.historyList:str = obj["historyList"]
      self.returnList:str = obj["returnList"]
      pass

class ReturnValidItems_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.returnList:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetPCIDLabelTypeInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

class SetPCIDLabelTypeInfo_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ShipToChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

class ShipToChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

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
      """  True if messages should be hidden  """  
      pass

class ValidateCustomer_input:
   """ Required : 
   proposedCustID
   partNum
   pkgCode
   calledFrom
   """  
   def __init__(self, obj):
      self.proposedCustID:str = obj["proposedCustID"]
      self.partNum:str = obj["partNum"]
      self.pkgCode:str = obj["pkgCode"]
      self.calledFrom:str = obj["calledFrom"]
      pass

class ValidateCustomer_output:
   def __init__(self, obj):
      pass

class ValidateJob_input:
   """ Required : 
   jobNum
   whoCalled
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      self.whoCalled:str = obj["whoCalled"]
      pass

class ValidateJob_output:
   def __init__(self, obj):
      pass

class ValidateNumberToGen_input:
   """ Required : 
   proposedNumberToGen
   """  
   def __init__(self, obj):
      self.proposedNumberToGen:str = obj["proposedNumberToGen"]
      """  proposedNumberToGen  """  
      pass

class ValidateNumberToGen_output:
   def __init__(self, obj):
      pass

class ValidatePkgCode_input:
   """ Required : 
   proposedPkgCode
   """  
   def __init__(self, obj):
      self.proposedPkgCode:str = obj["proposedPkgCode"]
      """  proposedPkgCode  """  
      pass

class ValidatePkgCode_output:
   def __init__(self, obj):
      pass

class ValidateShift_input:
   """ Required : 
   proposedShift
   """  
   def __init__(self, obj):
      self.proposedShift:str = obj["proposedShift"]
      """  proposedShift  """  
      pass

class ValidateShift_output:
   def __init__(self, obj):
      pass

class ValidateShipTo_input:
   """ Required : 
   custNum
   proposedShipTo
   partNum
   pkgCode
   calledFrom
   """  
   def __init__(self, obj):
      self.custNum:int = obj["custNum"]
      self.proposedShipTo:str = obj["proposedShipTo"]
      self.partNum:str = obj["partNum"]
      self.pkgCode:str = obj["pkgCode"]
      self.calledFrom:str = obj["calledFrom"]
      pass

class ValidateShipTo_output:
   def __init__(self, obj):
      pass

class ValidateSourcePCID_input:
   """ Required : 
   ipSourcePCID
   """  
   def __init__(self, obj):
      self.ipSourcePCID:str = obj["ipSourcePCID"]
      pass

class ValidateSourcePCID_output:
   def __init__(self, obj):
      pass

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

class ValidateWhsePCID_input:
   """ Required : 
   toWhse
   partNum
   warehouseType
   """  
   def __init__(self, obj):
      self.toWhse:str = obj["toWhse"]
      """  Warehouse to validate.  """  
      self.partNum:str = obj["partNum"]
      """  PartNum  """  
      self.warehouseType:str = obj["warehouseType"]
      """  warehouseType  """  
      pass

class ValidateWhsePCID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class ValidateXPart_input:
   """ Required : 
   proposedCustID
   proposedXPart
   pkgCode
   shipToNum
   calledFrom
   """  
   def __init__(self, obj):
      self.proposedCustID:str = obj["proposedCustID"]
      self.proposedXPart:str = obj["proposedXPart"]
      self.pkgCode:str = obj["pkgCode"]
      self.shipToNum:str = obj["shipToNum"]
      self.calledFrom:str = obj["calledFrom"]
      pass

class ValidateXPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.multipleMatches:bool = obj["multipleMatches"]
      self.newProposedXPart:str = obj["parameters"]
      pass

      """  output parameters  """  

class WarehouseCodeChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

class WarehouseCodeChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

class XPartChanged_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

class XPartChanged_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlGenPCIDTableset] = obj["ds"]
      pass

      """  output parameters  """  

