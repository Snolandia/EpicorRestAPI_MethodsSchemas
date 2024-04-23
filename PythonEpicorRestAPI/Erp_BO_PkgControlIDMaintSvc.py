import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PkgControlIDMaintSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetPkgControlHdrByIDInvTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPkgControlHdrByIDInvTrans
   Description: Gets a PkgControlHeader, PkgControlStageHeader, or HXPkgControlHeader by ID
   OperationID: GetPkgControlHdrByIDInvTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlHdrByIDInvTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlHdrByIDInvTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPkgControlHdrByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPkgControlHdrByID
   Description: Gets a PkgControlHeader, PkgControlStageHeader, or HXPkgControlHeader by ID
   OperationID: GetPkgControlHdrByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlHdrByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlHdrByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPkgControlHdrByID2(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPkgControlHdrByID2
   Description: Gets a PkgControlHeader, PkgControlStageHeader, or HXPkgControlHeader by ID
Created for Kinetic so the LabelValue records all have a unique GUID
   OperationID: GetPkgControlHdrByID2
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlHdrByID2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlHdrByID2_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPkgControlHdrByGUID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPkgControlHdrByGUID
   Description: Gets a PkgControlHeader, PkgControlStageHeader, or HXPkgControlHeader by SysRowID
   OperationID: GetPkgControlHdrByGUID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlHdrByGUID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlHdrByGUID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetHeaderRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetHeaderRows
   Description: Gets PkgControlHeader, PkgControlStageHeader, and HXPkgControlHeader records into the Erp.BO.PkgControlIDMergedTableset
Based on the whereClauses provided and other parameters selected
   OperationID: GetHeaderRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHeaderRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHeaderRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetHeaderList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetHeaderList
   Description: Gets PkgControlHeader, PkgControlStageHeader, and HXPkgControlHeader records into the Erp.BO.PkgControlIDMergedTableset
Based on the whereClauses provided and other parameters selected
   OperationID: GetHeaderList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetHeaderList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetHeaderList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdatePkgControl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdatePkgControl
   Description: Updates PkgControlHeader, PkgControlStageHeader, and HXPkgControlHeader records
   OperationID: UpdatePkgControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePkgControl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePkgControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CommitPCIDTransfer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CommitPCIDTransfer
   Description: This method will commit the inventory transfer.
   OperationID: CommitPCIDTransfer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitPCIDTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitPCIDTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetValidPCIDRow(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetValidPCIDRow
   Description: This method verifies if a PCID entered is valid. If so, returns PkgControlIDMergedTableset with the PCID row value.
   OperationID: GetValidPCIDRow
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetValidPCIDRow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetValidPCIDRow_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidPCIDProcess(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidPCIDProcess
   Description: This method updates PkgControlStatus to VOID for a PCID.
   OperationID: VoidPCIDProcess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidPCIDProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidPCIDProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreSetLegalNumPkgControlVoidPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreSetLegalNumPkgControlVoidPCID
   Description: This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction. The RequiresUserInput
flag will indicate if this legal number requires input from the user. If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information. This method should be called when the user
inputs the target PCID or clicks the print button and the source qty > 0,
and before calling any update method that could generate PartTran.
   OperationID: PreSetLegalNumPkgControlVoidPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreSetLegalNumPkgControlVoidPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreSetLegalNumPkgControlVoidPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PCIDExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PCIDExists
   Description: Purpose:  Test if a given PCID already exists in the PkgControlHeader table.
   OperationID: PCIDExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PCIDExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PCIDExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WarehseEnforcePkgControlRulesExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WarehseEnforcePkgControlRulesExists
   Description: This method is udes to verify if a Warehouse with EnforcePkgControlRules exists
   OperationID: WarehseEnforcePkgControlRulesExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WarehseEnforcePkgControlRulesExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WarehseEnforcePkgControlRulesExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_WhseBinExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method WhseBinExists
   Description: This method is udes to verify if a WhseBin exists
   OperationID: WhseBinExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/WhseBinExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/WhseBinExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_isWhseBinManaged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method isWhseBinManaged
   Description: This method is used to verify if a WhseBin is Supplier or Customer Managed
   OperationID: isWhseBinManaged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/isWhseBinManaged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/isWhseBinManaged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_isWhseBinActive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method isWhseBinActive
   Description: This method is used to verify if a WhseBin is Active or Inactive
   OperationID: isWhseBinActive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/isWhseBinActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/isWhseBinActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConfirmSupervisorPassword(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConfirmSupervisorPassword
   Description: This method is used to confirm if the User/Supervisor Password provided is correct.
This is called from PackageControlLib.
   OperationID: ConfirmSupervisorPassword
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConfirmSupervisorPassword_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConfirmSupervisorPassword_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PrintLabel(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PrintLabel
   OperationID: PrintLabel
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PrintLabel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrintLabel_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSplitMergeData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSplitMergeData
   Description: Purpose: Get splitMerge target or source data for a PCID
Parameters:  none
Notes:
<param name="ipPCID">The PCID the data is being retrieved for</param><param name="ipSourceOrTarget">Retrieve Split Merge for the source or target (S or T) PCIDs for the input PCID</param><param name="ds">The PkgControlSplitMerge data set</param>
   OperationID: GetSplitMergeData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSplitMergeData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSplitMergeData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultTranDocTypeID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultTranDocTypeID
   Description: Returns the default Transaction Document Type ID for a given System Transaction.
   OperationID: GetDefaultTranDocTypeID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultTranDocTypeID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultTranDocTypeID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessAdhocRecipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessAdhocRecipt
   Description: Moves inventory from STAGE to INVENTORY
   OperationID: ProcessAdhocRecipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessAdhocRecipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessAdhocRecipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreProcessAdhocRecipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreProcessAdhocRecipt
   Description: Validates PCID for Adhoc Receipt and performs NegInvTest
   OperationID: PreProcessAdhocRecipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreProcessAdhocRecipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcessAdhocRecipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultAdhocMoveLocation(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultAdhocMoveLocation
   Description: Gets the default to warehouse and bin for Adhoc Receipt
   OperationID: GetDefaultAdhocMoveLocation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultAdhocMoveLocation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetPkgControlIDMergedList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPkgControlIDMergedList
   Description: Retrieves PkgControlHeader, PkgControlStageHeader, and HXPkgControlHeader records and their associated item records and merges into PkgControlIDMergedListTableset.
   OperationID: GetPkgControlIDMergedList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlIDMergedList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlIDMergedList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPkgControlIDMergedListAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPkgControlIDMergedListAll
   Description: Copy of GetPkgControlIDMergedList that sets pageSize to 0 to avoid a paging issue in kinetic.
   OperationID: GetPkgControlIDMergedListAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPkgControlIDMergedListAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPkgControlIDMergedListAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDMaintSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CommitPCIDTransfer_input:
   """ Required : 
   toWhse
   toBin
   ds
   """  
   def __init__(self, obj):
      self.toWhse:str = obj["toWhse"]
      self.toBin:str = obj["toBin"]
      self.ds:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["ds"]
      pass

class CommitPCIDTransfer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ConfirmSupervisorPassword_input:
   """ Required : 
   password
   """  
   def __init__(self, obj):
      self.password:str = obj["password"]
      pass

class ConfirmSupervisorPassword_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
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

class Erp_Tablesets_PCLabelValuesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LabelSeq:int = obj["LabelSeq"]
      self.LabelValues:str = obj["LabelValues"]
      self.PCID:str = obj["PCID"]
      self.ValueField:str = obj["ValueField"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlCustPartNumRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number.  """  
      self.PCIDCustPartSeq:int = obj["PCIDCustPartSeq"]
      """  PCID Customer Part Sequence.  """  
      self.CustPartNum:str = obj["CustPartNum"]
      """  Used for MixedMaster parent PCIDs.  Customer Part Number associated to the MixedMaster parent PCID.  """  
      self.CustQtyPerContainer:int = obj["CustQtyPerContainer"]
      """  Used for MixedMaster parent PCIDs. Number of parts per parent PCID for the Customer Part Number associated to the MixedMaster parent PCID.  """  
      self.CustNumContainers:int = obj["CustNumContainers"]
      """  Used for MixedMaster parent PCIDs.  Number of PCIDs for the Customer Part Number associated to the MixedMaster parent PCID.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlHeaderMergedListRow:
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
      """  Reserved for development use for PkgControlStatus value prior to being added to a pack.  """  
      self.PkgControlCharacter02:str = obj["PkgControlCharacter02"]
      """  Reserved for development use for LabelPrintControlStatus value prior to being added to a pack  """  
      self.PkgControlCharacter03:str = obj["PkgControlCharacter03"]
      """  Reserved for development use to indicate the source process when a PCID was added to a pack.  """  
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
      self.BeforePackPkgControlStatus:str = obj["BeforePackPkgControlStatus"]
      self.BeforePackLabelPrintControlStatus:str = obj["BeforePackLabelPrintControlStatus"]
      self.PackedFromSource:str = obj["PackedFromSource"]
      self.RecordTypeDesc:str = obj["RecordTypeDesc"]
      """  Record Type Description, can be Inventory, History or Stage  """  
      self.PCIDItemSeq:int = obj["PCIDItemSeq"]
      """  PCID Item Sequence  """  
      self.ItemPartNum:str = obj["ItemPartNum"]
      """  The Part Number of the item in this PCID.  """  
      self.ItemPartDesc:str = obj["ItemPartDesc"]
      """  The Part Description of the item in this PCID.  """  
      self.ItemLotNum:str = obj["ItemLotNum"]
      """  The Lot Number of the item in this PCID.  """  
      self.ItemIUM:str = obj["ItemIUM"]
      """  The Inventory UOM of the item in this PCID.  """  
      self.ItemQuantity:int = obj["ItemQuantity"]
      """  The Quantity of the item in this PCID.  """  
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      """  Job that is supplying the allocated quantity  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlHeaderMergedRow:
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
      """  If false then PCID is restricted to containing single-level child PCIDs only and those child PCIDs must contain the same PartNum, Part UOM, or Part Quantity per child PCID.  This is referred to as a Master PCID, otherwise it would be referred to as a Mixed PCID.  """  
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
      self.Expendable:bool = obj["Expendable"]
      """  if the PkgControlID is expendable  """  
      self.ExtensionDigit:int = obj["ExtensionDigit"]
      self.HHPackSlip:int = obj["HHPackSlip"]
      """   Used for handHeld             
If PkgControlHeader.PkgControlType = Static then PkgControlHeader.PackNum
If PkgControlHeader.PkgControlType = Dynamic then PkgControlItem.PackNum  """  
      self.HHPackSlipList:str = obj["HHPackSlipList"]
      """  Used for HandHeld, It could contains a list of PackNum from the children  """  
      self.PartDesc:str = obj["PartDesc"]
      self.PkgCodeDesc:str = obj["PkgCodeDesc"]
      self.ResCodeIn:str = obj["ResCodeIn"]
      self.ResCodeOut:str = obj["ResCodeOut"]
      self.RTWhseDesc:str = obj["RTWhseDesc"]
      self.WhseDesc:str = obj["WhseDesc"]
      self.ChildPCIDCount:int = obj["ChildPCIDCount"]
      """  Child PCID count  """  
      self.HHASN:bool = obj["HHASN"]
      """  Used for Handheld, this field will determine if the ASN (Advanced Ship Notice) has been sent/printed  """  
      self.HHLabelStatus:str = obj["HHLabelStatus"]
      """  Used for HandHeld, it can be either PkgControlHeader.LabelPrintControlStatus OR PkgControlHeader.PkgControlStatus  """  
      self.LWHDimUOM:str = obj["LWHDimUOM"]
      self.ParentPCID:str = obj["ParentPCID"]
      """  Parent Package Control Identification Number  """  
      self.ParentPlant:str = obj["ParentPlant"]
      """  Site where the Parent PCID is currently located.  """  
      self.ParentWarehouseCode:str = obj["ParentWarehouseCode"]
      """  Warehouse where the Parent PCID is currently located.  """  
      self.ParentBinNum:str = obj["ParentBinNum"]
      """  Warehouse Bin where the Parent PCID is currently located.  """  
      self.ParentCustID:str = obj["ParentCustID"]
      """  Parent Ship To Customer ID.  """  
      self.ParentShipToNum:str = obj["ParentShipToNum"]
      """  Parent Ship To Number.  """  
      self.ParentPkgCode:str = obj["ParentPkgCode"]
      """  Unique packaging code assigned by the user.  """  
      self.ParentPackNum:int = obj["ParentPackNum"]
      """  Pack Number if applicable.  """  
      self.ParentPkgCodePartNum:str = obj["ParentPkgCodePartNum"]
      """  The Internal PartNum for the Package Code.  """  
      self.ParentCustContainerPartNum:str = obj["ParentCustContainerPartNum"]
      """  Ship To Customer Container Part Number.  """  
      self.ParentNumberOfPCIDs:int = obj["ParentNumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.ParentPkgControlType:str = obj["ParentPkgControlType"]
      """  Package Control Type.  Valid values are “Static” or “Dynamic”.  """  
      self.ParentLabelPrintControlled:bool = obj["ParentLabelPrintControlled"]
      """  If false then the standard PCID printing logic is used. If true then the Label Print Control logic and rules will apply and be enforced.  """  
      self.ParentLabelType:str = obj["ParentLabelType"]
      """  Label Type.  """  
      self.ParentLabelPrintControlStatus:str = obj["ParentLabelPrintControlStatus"]
      """  Label Print Control status.  """  
      self.ParentCreatedDate:str = obj["ParentCreatedDate"]
      """  System date and time when the row was created.  """  
      self.ParentPkgControlStatus:str = obj["ParentPkgControlStatus"]
      """  PCID current status.  """  
      self.PkgType:str = obj["PkgType"]
      self.ParentPlantName:str = obj["ParentPlantName"]
      """  Site Name.  """  
      self.ParentWhseDesc:str = obj["ParentWhseDesc"]
      self.HHItemQuantity:int = obj["HHItemQuantity"]
      """  Used for Handheld.  """  
      self.HHItemIUM:str = obj["HHItemIUM"]
      self.HHItemPartNum:str = obj["HHItemPartNum"]
      self.HHItemRevisionNum:str = obj["HHItemRevisionNum"]
      self.DisableReasonCode:bool = obj["DisableReasonCode"]
      self.ReasonCode:str = obj["ReasonCode"]
      """  Reason Code  """  
      self.ShipToContainerPartID:str = obj["ShipToContainerPartID"]
      """  Ship To Container Part ID  """  
      self.ContainerUOM:str = obj["ContainerUOM"]
      """  Container UOM  """  
      self.AdjustInventory:bool = obj["AdjustInventory"]
      """  Adjust Inventory  """  
      self.EnableBtnVoidPCIDInv:bool = obj["EnableBtnVoidPCIDInv"]
      """  Indicates if BtnVoidPCIDInv control should be Enabled.  """  
      self.EnableCboReasonCode:bool = obj["EnableCboReasonCode"]
      """  Indicates if EnableCboReasonCode control should be Enabled.  """  
      self.RecordType:str = obj["RecordType"]
      self.RecordTypeDesc:str = obj["RecordTypeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.AdhocStagedInventory:bool = obj["AdhocStagedInventory"]
      self.Ext_PrevPCID:str = obj["Ext_PrevPCID"]
      self.ResCodeInDesc:str = obj["ResCodeInDesc"]
      self.ResCodeOutDesc:str = obj["ResCodeOutDesc"]
      self.OriginalSourcePCIDDisp:str = obj["OriginalSourcePCIDDisp"]
      """  Used for the PkgControl ID Maint form Activities  tab. It will display the PkgControlHeaderMerged.OriginalSourcePCID if there is only one, or "Multiple" if this PCID has PkgControlSplitMerger where it is specified as the Target.  """  
      self.OverlaidByPCIDDisp:str = obj["OverlaidByPCIDDisp"]
      """  Used for the PkgControl ID Maint form Activities  tab. It will display the PkgControlHeaderMerged.OverlaidByPCID if there is only one, or "Multiple" if this PCID has PkgControlSplitMerger where it is specified as the Source.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      """  Holds any message returned from the legal number generation.  """  
      self.UpdatedByEmpID:str = obj["UpdatedByEmpID"]
      """  The employee that last updated this row.  """  
      self.RawBarcodeScan:str = obj["RawBarcodeScan"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.TranDocTypeIDPCID:str = obj["TranDocTypeIDPCID"]
      """  Temporal Transaction Document Type. This is used to be able to have TranDocTypeIDs for different System Transactions in different tabs of the same form.  """  
      self.TranDocTypeIDPCIDInv:str = obj["TranDocTypeIDPCIDInv"]
      """  Temporal Transaction Document Type. This is used to be able to have TranDocTypeIDs for different System Transactions in different tabs of the same form.  """  
      self.OutboundContainer:bool = obj["OutboundContainer"]
      self.BeforePackPkgControlStatus:str = obj["BeforePackPkgControlStatus"]
      self.BeforePackLabelPrintControlStatus:str = obj["BeforePackLabelPrintControlStatus"]
      self.PackedFromSource:str = obj["PackedFromSource"]
      self.TFPackNum:int = obj["TFPackNum"]
      """  Transfer Shipment Pack Number if applicable.  """  
      self.ItemQuantity:int = obj["ItemQuantity"]
      """  Item Quantity for a PCID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlIDMergedListTableset:
   def __init__(self, obj):
      self.PkgControlHeaderMergedList:list[Erp_Tablesets_PkgControlHeaderMergedListRow] = obj["PkgControlHeaderMergedList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PkgControlIDMergedTableset:
   def __init__(self, obj):
      self.PkgControlHeaderMerged:list[Erp_Tablesets_PkgControlHeaderMergedRow] = obj["PkgControlHeaderMerged"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.PCLabelValues:list[Erp_Tablesets_PCLabelValuesRow] = obj["PCLabelValues"]
      self.PkgControlCustPartNum:list[Erp_Tablesets_PkgControlCustPartNumRow] = obj["PkgControlCustPartNum"]
      self.PkgControlItemMerged:list[Erp_Tablesets_PkgControlItemMergedRow] = obj["PkgControlItemMerged"]
      self.PkgControlSplitMerge:list[Erp_Tablesets_PkgControlSplitMergeRow] = obj["PkgControlSplitMerge"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PkgControlItemMergedRow:
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
      """  Site.  """  
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
      """  The internal Part for the Package Code.  """  
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
      """  Reserved for development use.  """  
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
      self.ChildPCIDOrPart:str = obj["ChildPCIDOrPart"]
      self.PackageCode:str = obj["PackageCode"]
      self.CustID:str = obj["CustID"]
      self.CustName:str = obj["CustName"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse where the PCID is currently located.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin where the PCID is currently located.  """  
      self.NumberOfPCIDs:int = obj["NumberOfPCIDs"]
      """  Number of next level down child PCIDs associated to this PCID.  """  
      self.PlantName:str = obj["PlantName"]
      """  Site Name.  """  
      self.WhseDesc:str = obj["WhseDesc"]
      self.ShipmentInvoicedPosted:str = obj["ShipmentInvoicedPosted"]
      self.RecordTypeDesc:str = obj["RecordTypeDesc"]
      self.ItemAttributeSetID:int = obj["ItemAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.TFPackNum:int = obj["TFPackNum"]
      """  Transfer Shipment Pack Number if applicable.  """  
      self.TFPackLine:int = obj["TFPackLine"]
      """  Transfer Shipment Line Num if applicable.  """  
      self.ItemAttributeSetDescription:str = obj["ItemAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.ItemAttributeSetShortDescription:str = obj["ItemAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ItemPartAttrClassID:str = obj["ItemPartAttrClassID"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Display (decimal) number of pieces for inventory tracked parts.  """  
      self.ItemPicked:bool = obj["ItemPicked"]
      """  Indicates the order info comes from picking/picked, used to determine whether to retain the demand data if the PCID is packed then unpacked.  """  
      self.ItemPartWipSysRowID:str = obj["ItemPartWipSysRowID"]
      """  SysRowID of the PartWip to which this item relates. The value is a GUID.  If the item is not WIP, this column is blank.  This value should only ever be populated in a Staging or History PCID, never an Inventory PCID.  """  
      self.TrackType:str = obj["TrackType"]
      """  Internal flag to distiguish between tracking of issued raw material, and the actual manufactured product.  "R" - Raw Material a part which was issued to the job.  "M" - Manufactured Part. The part that is being manufactured.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Job operation sequence number that part is related to.  """  
      self.ItemType:str = obj["ItemType"]
      self.InNonConformance:bool = obj["InNonConformance"]
      self.InDMRProcessing:bool = obj["InDMRProcessing"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlSplitMergeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.TranNum:int = obj["TranNum"]
      """  TranNum  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.SourcePCID:str = obj["SourcePCID"]
      """  SourcePCID  """  
      self.SourcePkgControlStatus:str = obj["SourcePkgControlStatus"]
      """  SourcePkgControlStatus  """  
      self.SourceWarehouseCode:str = obj["SourceWarehouseCode"]
      """  SourceWarehouseCode  """  
      self.SourceBinNum:str = obj["SourceBinNum"]
      """  SourceBinNum  """  
      self.SourceLabelPrintControlStatus:str = obj["SourceLabelPrintControlStatus"]
      """  SourceLabelPrintControlStatus  """  
      self.TargetPCID:str = obj["TargetPCID"]
      """  TargetPCID  """  
      self.TargetPkgControlStatus:str = obj["TargetPkgControlStatus"]
      """  TargetPkgControlStatus  """  
      self.TargetWarehouseCode:str = obj["TargetWarehouseCode"]
      """  TargetWarehouseCode  """  
      self.TargetBinNum:str = obj["TargetBinNum"]
      """  TargetBinNum  """  
      self.ItemPartNum:str = obj["ItemPartNum"]
      """  ItemPartNum  """  
      self.ItemRevisionNum:str = obj["ItemRevisionNum"]
      """  ItemRevisionNum  """  
      self.TargetLabelPrintControlStatus:str = obj["TargetLabelPrintControlStatus"]
      """  TargetLabelPrintControlStatus  """  
      self.ItemLotNum:str = obj["ItemLotNum"]
      """  ItemLotNum  """  
      self.ItemIUM:str = obj["ItemIUM"]
      """  ItemIUM  """  
      self.ItemQuantity:int = obj["ItemQuantity"]
      """  ItemQuantity  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  CreatedDate  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ItemAttributeSetID:int = obj["ItemAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetDefaultAdhocMoveLocation_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.whse:str = obj["parameters"]
      self.binNum:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDefaultTranDocTypeID_input:
   """ Required : 
   sysTranID
   """  
   def __init__(self, obj):
      self.sysTranID:str = obj["sysTranID"]
      """  The System Transaction ID as stored in the TranDocType table.  """  
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

class GetHeaderList_input:
   """ Required : 
   whereClausePkgControlHeader
   whereClauseHXPkgControlHeader
   whereClausePkgControlStageHeader
   whereClauseChild
   onlyTopParentPCID
   excludeInventory
   excludeHistory
   excludeStaged
   searchByPart
   pageSize
   """  
   def __init__(self, obj):
      self.whereClausePkgControlHeader:str = obj["whereClausePkgControlHeader"]
      """  Filter to be used on the PkgControlHeader Table  """  
      self.whereClauseHXPkgControlHeader:str = obj["whereClauseHXPkgControlHeader"]
      """  Filter to be used on the HXPkgControlHeader Table  """  
      self.whereClausePkgControlStageHeader:str = obj["whereClausePkgControlStageHeader"]
      """  Filter to be used on the PkgControlStageHeader Table  """  
      self.whereClauseChild:str = obj["whereClauseChild"]
      """  Filter to be used on the ChildTable for all the whereClause: whereClausePkgControlHeader, whereClauseHXPkgControlHeader, whereClausePkgControlStageHeader  """  
      self.onlyTopParentPCID:bool = obj["onlyTopParentPCID"]
      """  When true the search will retrieve only PCIDs that are not listed,as children, on other PCIDs  """  
      self.excludeInventory:bool = obj["excludeInventory"]
      """  When true will exclude PkgControlHeader table its whereClause from the search.  """  
      self.excludeHistory:bool = obj["excludeHistory"]
      """  When true will exclude HXPkgControlHeader table its whereClause from the search.  """  
      self.excludeStaged:bool = obj["excludeStaged"]
      """  When true will exclude PkgControlStageHeader table its whereClause from the search.  """  
      self.searchByPart:bool = obj["searchByPart"]
      """  When selected the search will retrieve one line for each of the child records for each PCID that meets the filter whereClause  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      pass

class GetHeaderList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDMergedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetHeaderRows_input:
   """ Required : 
   whereClausePkgControlHeader
   whereClauseHXPkgControlHeader
   whereClausePkgControlStageHeader
   onlyTopParentPCID
   excludeInventory
   excludeHistory
   excludeStaged
   """  
   def __init__(self, obj):
      self.whereClausePkgControlHeader:str = obj["whereClausePkgControlHeader"]
      """  Filter to be used on the PkgControlHeader Table  """  
      self.whereClauseHXPkgControlHeader:str = obj["whereClauseHXPkgControlHeader"]
      """  Filter to be used on the HXPkgControlHeader Table  """  
      self.whereClausePkgControlStageHeader:str = obj["whereClausePkgControlStageHeader"]
      """  Filter to be used on the PkgControlStageHeader Table  """  
      self.onlyTopParentPCID:bool = obj["onlyTopParentPCID"]
      """  When true the search will retrieve only PCIDs that are not listed,as children, on other PCIDs  """  
      self.excludeInventory:bool = obj["excludeInventory"]
      """  When true will exclude PkgControlHeader table its whereClause from the search.  """  
      self.excludeHistory:bool = obj["excludeHistory"]
      """  When true will exclude HXPkgControlHeader table its whereClause from the search.  """  
      self.excludeStaged:bool = obj["excludeStaged"]
      """  When true will exclude PkgControlStageHeader table its whereClause from the search.  """  
      pass

class GetHeaderRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["returnObj"]
      pass

class GetPkgControlHdrByGUID_input:
   """ Required : 
   sysRowID
   excludeInventory
   excludeHistory
   excludeStaged
   combineWhenInventoryAndStaged
   """  
   def __init__(self, obj):
      self.sysRowID:str = obj["sysRowID"]
      """  SysRowID of header to retrieve  """  
      self.excludeInventory:bool = obj["excludeInventory"]
      """  Flag to exclude Inventory PCIDs  """  
      self.excludeHistory:bool = obj["excludeHistory"]
      """  Flag to exclude History PCIDs  """  
      self.excludeStaged:bool = obj["excludeStaged"]
      """  Flag to exclude Staged PCIDs  """  
      self.combineWhenInventoryAndStaged:bool = obj["combineWhenInventoryAndStaged"]
      """  Flag to return both Inventory and Staged data if a PCID is both in Inventory and Staged at the same time  """  
      pass

class GetPkgControlHdrByGUID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["returnObj"]
      pass

class GetPkgControlHdrByID2_input:
   """ Required : 
   pcid
   excludeInventory
   excludeHistory
   excludeStaged
   combineWhenInventoryAndStaged
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  SysRowID of header to retrieve  """  
      self.excludeInventory:bool = obj["excludeInventory"]
      """  Flag to exclude Inventory PCIDs  """  
      self.excludeHistory:bool = obj["excludeHistory"]
      """  Flag to exclude History PCIDs  """  
      self.excludeStaged:bool = obj["excludeStaged"]
      """  Flag to exclude Staged PCIDs  """  
      self.combineWhenInventoryAndStaged:bool = obj["combineWhenInventoryAndStaged"]
      """  Flag to return both Inventory and Staged data if a PCID is both in Inventory and Staged at the same time  """  
      pass

class GetPkgControlHdrByID2_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["returnObj"]
      pass

class GetPkgControlHdrByIDInvTrans_input:
   """ Required : 
   pcid
   excludeInventory
   excludeHistory
   excludeStaged
   calledFrom
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      self.excludeInventory:bool = obj["excludeInventory"]
      self.excludeHistory:bool = obj["excludeHistory"]
      self.excludeStaged:bool = obj["excludeStaged"]
      self.calledFrom:str = obj["calledFrom"]
      pass

class GetPkgControlHdrByIDInvTrans_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["returnObj"]
      pass

class GetPkgControlHdrByID_input:
   """ Required : 
   pcid
   excludeInventory
   excludeHistory
   excludeStaged
   combineWhenInventoryAndStaged
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  SysRowID of header to retrieve  """  
      self.excludeInventory:bool = obj["excludeInventory"]
      """  Flag to exclude Inventory PCIDs  """  
      self.excludeHistory:bool = obj["excludeHistory"]
      """  Flag to exclude History PCIDs  """  
      self.excludeStaged:bool = obj["excludeStaged"]
      """  Flag to exclude Staged PCIDs  """  
      self.combineWhenInventoryAndStaged:bool = obj["combineWhenInventoryAndStaged"]
      """  Flag to return both Inventory and Staged data if a PCID is both in Inventory and Staged at the same time  """  
      pass

class GetPkgControlHdrByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["returnObj"]
      pass

class GetPkgControlIDMergedListAll_input:
   """ Required : 
   whoLaunched
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whoLaunched:str = obj["whoLaunched"]
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetPkgControlIDMergedListAll_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDMergedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetPkgControlIDMergedList_input:
   """ Required : 
   whoLaunched
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whoLaunched:str = obj["whoLaunched"]
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetPkgControlIDMergedList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDMergedListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetSplitMergeData_input:
   """ Required : 
   ipPCID
   ipSourceOrTarget
   ds
   """  
   def __init__(self, obj):
      self.ipPCID:str = obj["ipPCID"]
      self.ipSourceOrTarget:str = obj["ipSourceOrTarget"]
      self.ds:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["ds"]
      pass

class GetSplitMergeData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetValidPCIDRow_input:
   """ Required : 
   pcid
   excludeInventory
   excludeHistory
   excludeStaged
   calledFromHH
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  pcid  """  
      self.excludeInventory:bool = obj["excludeInventory"]
      """  excludeInventory  """  
      self.excludeHistory:bool = obj["excludeHistory"]
      """  excludeHistory  """  
      self.excludeStaged:bool = obj["excludeStaged"]
      """  excludeStaged  """  
      self.calledFromHH:bool = obj["calledFromHH"]
      """  calledFromHH  """  
      pass

class GetValidPCIDRow_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorMessage:str = obj["parameters"]
      self.supervisorRequired:bool = obj["supervisorRequired"]
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

class PCIDExists_input:
   """ Required : 
   ipPCID
   """  
   def __init__(self, obj):
      self.ipPCID:str = obj["ipPCID"]
      """  PCID  """  
      pass

class PCIDExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  bool  """  
      pass

class PreProcessAdhocRecipt_input:
   """ Required : 
   pcid
   whse
   binNum
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  PCID to move from staged  """  
      self.whse:str = obj["whse"]
      """  Warehouse to move to  """  
      self.binNum:str = obj["binNum"]
      """  Bin to move to  """  
      pass

class PreProcessAdhocRecipt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.negQtyAction:str = obj["parameters"]
      self.negQtyMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class PreSetLegalNumPkgControlVoidPCID_input:
   """ Required : 
   ds
   adjustInventory
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["ds"]
      self.adjustInventory:bool = obj["adjustInventory"]
      """  Helps to define the System Transaction that will be handled  """  
      pass

class PreSetLegalNumPkgControlVoidPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["ds"]
      self.requiresUserInput:bool = obj["requiresUserInput"]
      pass

      """  output parameters  """  

class PrintLabel_input:
   """ Required : 
   ipPCID
   """  
   def __init__(self, obj):
      self.ipPCID:str = obj["ipPCID"]
      pass

class PrintLabel_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.printerID:str = obj["parameters"]
      self.lpcPrintedFromTx:str = obj["parameters"]
      self.lpcPrintedFromTxType:str = obj["parameters"]
      self.numberOfLabels:int = obj["parameters"]
      self.styleNum:int = obj["parameters"]
      self.promptUser:bool = obj["promptUser"]
      pass

      """  output parameters  """  

class ProcessAdhocRecipt_input:
   """ Required : 
   pcid
   whse
   binNum
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  PCID to move from staged  """  
      self.whse:str = obj["whse"]
      """  Warehouse to move to  """  
      self.binNum:str = obj["binNum"]
      """  Bin to move to  """  
      pass

class ProcessAdhocRecipt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["returnObj"]
      pass

class UpdatePkgControl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["ds"]
      pass

class UpdatePkgControl_output:
   def __init__(self, obj):
      pass

class ValidateWhsePCIDAndGetDefaultBin_input:
   """ Required : 
   ToWhse
   PlantID
   """  
   def __init__(self, obj):
      self.ToWhse:str = obj["ToWhse"]
      """  Warehouse to validate.  """  
      self.PlantID:str = obj["PlantID"]
      """  current PlantID  """  
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

class VoidPCIDProcess_input:
   """ Required : 
   pcid
   reasonCode
   adjustInventory
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  pcid  """  
      self.reasonCode:str = obj["reasonCode"]
      """  Reason Code required as part of the Void of Inventory  """  
      self.adjustInventory:bool = obj["adjustInventory"]
      """  Set this to true when it is desired that the Inventory and/or WIP inside the PCID should be removed as part of the Void  """  
      self.ds:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["ds"]
      pass

class VoidPCIDProcess_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PkgControlIDMergedTableset] = obj["ds"]
      pass

      """  output parameters  """  

class WarehseEnforcePkgControlRulesExists_input:
   """ Required : 
   WarehouseCode
   PlantID
   """  
   def __init__(self, obj):
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode to search for  """  
      self.PlantID:str = obj["PlantID"]
      """  Current PlantID  """  
      pass

class WarehseEnforcePkgControlRulesExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if Warehouse exists  """  
      pass

class WhseBinExists_input:
   """ Required : 
   WarehouseCode
   BinNum
   """  
   def __init__(self, obj):
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Current WarehouseCode  """  
      self.BinNum:str = obj["BinNum"]
      """  BinNum to search for  """  
      pass

class WhseBinExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if WhseBin exists  """  
      pass

class isWhseBinActive_input:
   """ Required : 
   WarehouseCode
   BinNum
   """  
   def __init__(self, obj):
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Current WarehouseCode  """  
      self.BinNum:str = obj["BinNum"]
      """  BinNum to search for  """  
      pass

class isWhseBinActive_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if WhseBin is Active  """  
      pass

class isWhseBinManaged_input:
   """ Required : 
   WarehouseCode
   BinNum
   """  
   def __init__(self, obj):
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Current WarehouseCode  """  
      self.BinNum:str = obj["BinNum"]
      """  BinNum to search for  """  
      pass

class isWhseBinManaged_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if WhseBin is Supplier or Customer Managed  """  
      pass

