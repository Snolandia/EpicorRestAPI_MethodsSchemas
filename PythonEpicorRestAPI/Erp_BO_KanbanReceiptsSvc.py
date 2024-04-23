import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.KanbanReceiptsSvc
# Description: Kanban Receipts Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CalculateLotPartSelectedQuantities(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateLotPartSelectedQuantities
   Description: Calculate the correct quantities when selecting quantity for a Lot Bin part.
   OperationID: CalculateLotPartSelectedQuantities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateLotPartSelectedQuantities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateLotPartSelectedQuantities_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeProposedBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeProposedBinNum
   Description: Set proposed bin num when binnum is changing
   OperationID: ChangeProposedBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeProposedBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProposedBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBin
   Description: Update default information based on the bin changing
   OperationID: ChangeBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeEmployee(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeEmployee
   Description: Update default information based on the employee changing
   OperationID: ChangeEmployee
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeEmployee_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmployee_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeInventoryUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeInventoryUM
   Description: Procedure for changing KanbanReceipts.InventoryUM field
   OperationID: ChangeInventoryUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeInventoryUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInventoryUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeProposedLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeProposedLotNum
   Description: Set proposed lot num when lot num is changing
   OperationID: ChangeProposedLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeProposedLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProposedLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLotNum
   Description: Update default information based on the lot changing
   OperationID: ChangeLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeNonConfReason(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeNonConfReason
   Description: Update default information based on the bin changing
   OperationID: ChangeNonConfReason
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeNonConfReason_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeNonConfReason_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeProposedPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeProposedPart
   Description: Set a proposed part num when part number is changing
   OperationID: ChangeProposedPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeProposedPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProposedPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePart
   Description: Update default information based on the part number changing
   OperationID: ChangePart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRevision(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRevision
   Description: Update default information based on the revision number changing
   OperationID: ChangeRevision
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeContractID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeContractID
   Description: Update information based on the ContractID changed.
   OperationID: ChangeContractID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeContractID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeContractID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeScrapReason(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeScrapReason
   Description: Update default information based on the scrap reason changing
   OperationID: ChangeScrapReason
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeScrapReason_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeScrapReason_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUsePartNumForLot(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUsePartNumForLot
   Description: Update lot number and description if the value is changed to true.
   OperationID: ChangeUsePartNumForLot
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUsePartNumForLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUsePartNumForLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeProposedWarehosue(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeProposedWarehosue
   Description: Set a proposed part num when part number is changing
   OperationID: ChangeProposedWarehosue
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeProposedWarehosue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProposedWarehosue_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeWarehouse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeWarehouse
   Description: Update default information based on the warehouse changing
   OperationID: ChangeWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckProcessRunning(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckProcessRunning
   Description: Verify if a similar process is running for the same part.
   OperationID: CheckProcessRunning
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckProcessRunning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckProcessRunning_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ConvertUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ConvertUOM
   Description: This procedure will update the OnhandQty for the LotPartBin record where the qty is retrived and also will update the Total Selected Qty
from LotPartMtl in the correct UOM.
   OperationID: ConvertUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ConvertUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DoesMtlsMatch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DoesMtlsMatch
   Description: Validates if the Total Selected Qty for Each Part Mtl match with Required Qty. If not
a message is returned to used to inform that case.
   OperationID: DoesMtlsMatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DoesMtlsMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoesMtlsMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_KanbanReceiptsGetNew(epicorHeaders = None):
   """  
   Summary: Invoke method KanbanReceiptsGetNew
   Description: Creates a temporary record to store information needed for the receipt process.
   OperationID: KanbanReceiptsGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/KanbanReceiptsGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_PreProcessKanbanReceipts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreProcessKanbanReceipts
   Description: This method will return a record in the LegalNumGenOpts datatable if
a WIPStock / NonConf / StockWIP legal number is required for this transaction.
The promptWIPStock / promptNonConf flags will indicate whether these legal number types require user input
the LegalNumberPrompt business objects needs to be called to gather that information.
Note - You cannot currently cater for manual StockWIP LN's as this will generate multiple PartTransactions
This method should be called when the user saves the record but before the Update method is called.
   OperationID: PreProcessKanbanReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreProcessKanbanReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcessKanbanReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessKanbanReceipts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessKanbanReceipts
   Description: Processes the Kanban Receipt.
   OperationID: ProcessKanbanReceipts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessKanbanReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessKanbanReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetActionToSelSerNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetActionToSelSerNum
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: SetActionToSelSerNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetActionToSelSerNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetActionToSelSerNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Submit(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Submit
   Description: Submit the Kanban Receipt Process.
   OperationID: Submit
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Submit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Submit_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateNegQtyAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateNegQtyAction
   Description: Checks if the Selected Qty from PartBin will result into a negative Onhand Quantity and returns this value to UI
   OperationID: ValidateNegQtyAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateNegQtyAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNegQtyAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateLowerLevelLotTrackedParts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateLowerLevelLotTrackedParts
   Description: Validates if there are Lot Tracked Part Materials. If there are at least one, ttKanbanPartLotBin table
is filled with those records and returned to UI to prompt the user to select form which lot he wants to
get the Required Qty.
   OperationID: ValidateLowerLevelLotTrackedParts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateLowerLevelLotTrackedParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLowerLevelLotTrackedParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSelectedSerNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSelectedSerNum
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: ValidateSelectedSerNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateSelectedSerNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSelectedSerNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number manually entered is valid for this transaction
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RestoreKanbanReceipt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RestoreKanbanReceipt
   Description: This procedure will reset the KanbanRecetips fields related with process of Lot Tracked Mtl feature.
   OperationID: RestoreKanbanReceipt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RestoreKanbanReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RestoreKanbanReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   Description: Find Part
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   Description: GetPartFromRowID
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePartMOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePartMOM
   Description: This method validates status of the MOM before proceed to generate the Kanban Job
More validations can be added here.
   OperationID: ValidatePartMOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePartMOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartMOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateParts_Kit_NonStock_Phantom(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateParts_Kit_NonStock_Phantom
   Description: This method validates NonStock Phantoms
   OperationID: ValidateParts_Kit_NonStock_Phantom
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateParts_Kit_NonStock_Phantom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateParts_Kit_NonStock_Phantom_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailAutoTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailAutoTranDocTypes
   Description: Method to get available automatic tran doc types.
   OperationID: GetAvailAutoTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailAutoTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_CalculateLotPartSelectedDecimalQuantities(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CalculateLotPartSelectedDecimalQuantities
   Description: Calculate the correct quantities with decimals when selecting quantity for a Lot Bin part.
   OperationID: CalculateLotPartSelectedDecimalQuantities
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CalculateLotPartSelectedDecimalQuantities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateLotPartSelectedDecimalQuantities_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CalculateLotPartSelectedDecimalQuantities_input:
   """ Required : 
   ds
   selectedConvQty
   proposedSelectedQtyForBin
   selectedQtyForMtl
   proposedSelectedQtyForMtl
   partNum
   lotNum
   warehouseCode
   binNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.selectedConvQty:int = obj["selectedConvQty"]
      """  The currently selected converted quantity  """  
      self.proposedSelectedQtyForBin:int = obj["proposedSelectedQtyForBin"]
      """  The new quantity being selected from the bin  """  
      self.selectedQtyForMtl:int = obj["selectedQtyForMtl"]
      """  The currently selected material quantity  """  
      self.proposedSelectedQtyForMtl:int = obj["proposedSelectedQtyForMtl"]
      """  The new quantity being selected for the material  """  
      self.partNum:str = obj["partNum"]
      """  The current row's part number  """  
      self.lotNum:str = obj["lotNum"]
      """  The current row's lot number  """  
      self.warehouseCode:str = obj["warehouseCode"]
      """  The current row's warehouse code  """  
      self.binNum:str = obj["binNum"]
      """  The current row's bin number  """  
      pass

class CalculateLotPartSelectedDecimalQuantities_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CalculateLotPartSelectedQuantities_input:
   """ Required : 
   ds
   selectedConvQty
   proposedSelectedQtyForBin
   selectedQtyForMtl
   proposedSelectedQtyForMtl
   partNum
   lotNum
   warehouseCode
   binNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.selectedConvQty:int = obj["selectedConvQty"]
      """  The currently selected converted quantity  """  
      self.proposedSelectedQtyForBin:int = obj["proposedSelectedQtyForBin"]
      """  The new quantity being selected from the bin  """  
      self.selectedQtyForMtl:int = obj["selectedQtyForMtl"]
      """  The currently selected material quantity  """  
      self.proposedSelectedQtyForMtl:int = obj["proposedSelectedQtyForMtl"]
      """  The new quantity being selected for the material  """  
      self.partNum:str = obj["partNum"]
      """  The current row's part number  """  
      self.lotNum:str = obj["lotNum"]
      """  The current row's lot number  """  
      self.warehouseCode:str = obj["warehouseCode"]
      """  The current row's warehouse code  """  
      self.binNum:str = obj["binNum"]
      """  The current row's bin number  """  
      pass

class CalculateLotPartSelectedQuantities_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeBin_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class ChangeBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.lValidBin:bool = obj["lValidBin"]
      pass

      """  output parameters  """  

class ChangeContractID_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class ChangeContractID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeEmployee_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class ChangeEmployee_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.lValidEmployee:bool = obj["lValidEmployee"]
      pass

      """  output parameters  """  

class ChangeInventoryUM_input:
   """ Required : 
   ds
   ipProposedIUM
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.ipProposedIUM:str = obj["ipProposedIUM"]
      """  The Proposed IUM  """  
      pass

class ChangeInventoryUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLotNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class ChangeLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.lValidLot:bool = obj["lValidLot"]
      pass

      """  output parameters  """  

class ChangeNonConfReason_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class ChangeNonConfReason_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.lValidNonConfReason:bool = obj["lValidNonConfReason"]
      pass

      """  output parameters  """  

class ChangePart_input:
   """ Required : 
   ds
   uomCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      pass

class ChangePart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.lValidPart:bool = obj["lValidPart"]
      pass

      """  output parameters  """  

class ChangeProposedBinNum_input:
   """ Required : 
   ds
   proposedBinNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.proposedBinNum:str = obj["proposedBinNum"]
      pass

class ChangeProposedBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.lValidLot:bool = obj["lValidLot"]
      pass

      """  output parameters  """  

class ChangeProposedLotNum_input:
   """ Required : 
   ds
   proposedLotNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.proposedLotNum:str = obj["proposedLotNum"]
      pass

class ChangeProposedLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.lValidLot:bool = obj["lValidLot"]
      pass

      """  output parameters  """  

class ChangeProposedPart_input:
   """ Required : 
   ds
   uomCode
   proposedPartNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.uomCode:str = obj["uomCode"]
      self.proposedPartNum:str = obj["proposedPartNum"]
      pass

class ChangeProposedPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.lValidPart:bool = obj["lValidPart"]
      pass

      """  output parameters  """  

class ChangeProposedWarehosue_input:
   """ Required : 
   ds
   proposedWhseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.proposedWhseCode:str = obj["proposedWhseCode"]
      pass

class ChangeProposedWarehosue_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.lValidPart:bool = obj["lValidPart"]
      pass

      """  output parameters  """  

class ChangeRevision_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class ChangeRevision_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeScrapReason_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class ChangeScrapReason_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.lValidScrapReason:bool = obj["lValidScrapReason"]
      pass

      """  output parameters  """  

class ChangeUsePartNumForLot_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class ChangeUsePartNumForLot_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeWarehouse_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class ChangeWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.lValidWarehouse:bool = obj["lValidWarehouse"]
      pass

      """  output parameters  """  

class CheckProcessRunning_input:
   """ Required : 
   ip_partnum
   """  
   def __init__(self, obj):
      self.ip_partnum:str = obj["ip_partnum"]
      """  The required PartNum to run the Kanban Receipt.  """  
      pass

class CheckProcessRunning_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.oMsgText:str = obj["parameters"]
      pass

      """  output parameters  """  

class ConvertUOM_input:
   """ Required : 
   ipPartNum
   ipFromUOM
   ipFromQty
   ipToUOM
   doRounding
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Unit of Measure of LotPartBin.  """  
      self.ipFromUOM:str = obj["ipFromUOM"]
      """  The Unit of Measure of LotPartBin.  """  
      self.ipFromQty:int = obj["ipFromQty"]
      """  SelectedQty from LotPartBin.  """  
      self.ipToUOM:str = obj["ipToUOM"]
      """  The Unit of Measure of LotPartMtl.  """  
      self.doRounding:bool = obj["doRounding"]
      """  Is set to false if rounding is not needed.  """  
      pass

class ConvertUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opNewQty:int = obj["parameters"]
      pass

      """  output parameters  """  

class DoesMtlsMatch_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class DoesMtlsMatch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_KanbanReceiptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.EmployeeID:str = obj["EmployeeID"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.LotNum:str = obj["LotNum"]
      self.Quantity:int = obj["Quantity"]
      self.JobDate:str = obj["JobDate"]
      self.ScrapQuantity:int = obj["ScrapQuantity"]
      self.ScrapReason:str = obj["ScrapReason"]
      self.NonConfQuantity:int = obj["NonConfQuantity"]
      self.NonConfReason:str = obj["NonConfReason"]
      self.DimCode:str = obj["DimCode"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.BinNum:str = obj["BinNum"]
      self.CanReportScrapQty:bool = obj["CanReportScrapQty"]
      self.CanReportNCQty:bool = obj["CanReportNCQty"]
      self.EmployeeName:str = obj["EmployeeName"]
      self.PartDescription:str = obj["PartDescription"]
      self.ScrapReasonDesc:str = obj["ScrapReasonDesc"]
      self.NonConfReasonDesc:str = obj["NonConfReasonDesc"]
      self.TrackLots:bool = obj["TrackLots"]
      self.TrackDimension:bool = obj["TrackDimension"]
      self.TrackSerialNum:bool = obj["TrackSerialNum"]
      self.JobFirm:bool = obj["JobFirm"]
      self.JobEngineered:bool = obj["JobEngineered"]
      self.JobReleased:bool = obj["JobReleased"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.BinDescription:str = obj["BinDescription"]
      self.LegalNumber:str = obj["LegalNumber"]
      self.JobNum:str = obj["JobNum"]
      self.SerialNoTempTranID:int = obj["SerialNoTempTranID"]
      self.LotNumDescription:str = obj["LotNumDescription"]
      self.UseJobNumForLot:bool = obj["UseJobNumForLot"]
      """  Indicates if the job number should be used for the lot number  """  
      self.AltMethod:str = obj["AltMethod"]
      self.DisableAltMethod:bool = obj["DisableAltMethod"]
      """  Flag to be set to enable/disable a Revision's Alternate Method  """  
      self.DimCodeDescription:str = obj["DimCodeDescription"]
      self.InventoryUM:str = obj["InventoryUM"]
      self.InventoryUMDisp:str = obj["InventoryUMDisp"]
      """  Display only version of InventoryUM  """  
      self.ValidateOK:bool = obj["ValidateOK"]
      """  This field is used in BO program KanBan Receipts to validate issues regarding the serial numbers.  """  
      self.SNQuantity:int = obj["SNQuantity"]
      """  For serial processing, the number of serial numbers required for the KanbanReceipts.Quantity based on the Part.IUM.  """  
      self.TotalReqQty:int = obj["TotalReqQty"]
      self.PartNumDisp:str = obj["PartNumDisp"]
      self.JobAlreadyCreated:bool = obj["JobAlreadyCreated"]
      self.BaseUOM:str = obj["BaseUOM"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.ContractID:str = obj["ContractID"]
      """  The identifier of the planning contract.  """  
      self.TranDocTypeIDStockWIP:str = obj["TranDocTypeIDStockWIP"]
      """  Legal number transaction document type used for backflushed components (StockWIP)  """  
      self.LegalNumberNonConf:str = obj["LegalNumberNonConf"]
      """  Legal number used for Non-Conformance  """  
      self.TranDocTypeIDNonConf:str = obj["TranDocTypeIDNonConf"]
      """  Transaction document type used for Non conformance  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_KanbanReceiptsTableset:
   def __init__(self, obj):
      self.KanbanReceipts:list[Erp_Tablesets_KanbanReceiptsRow] = obj["KanbanReceipts"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.LotPartBin:list[Erp_Tablesets_LotPartBinRow] = obj["LotPartBin"]
      self.LotPartMtl:list[Erp_Tablesets_LotPartMtlRow] = obj["LotPartMtl"]
      self.PartLotAttributes:list[Erp_Tablesets_PartLotAttributesRow] = obj["PartLotAttributes"]
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

class Erp_Tablesets_LotPartBinRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.LotNum:str = obj["LotNum"]
      self.BinNum:str = obj["BinNum"]
      self.OnhandQty:int = obj["OnhandQty"]
      self.SelectedQty:int = obj["SelectedQty"]
      self.IsEnabled:bool = obj["IsEnabled"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.InventoryUOM:str = obj["InventoryUOM"]
      self.ParentMtlSeq:int = obj["ParentMtlSeq"]
      self.GrpWrhBin:str = obj["GrpWrhBin"]
      """  Group by criteria stored in one field (WH + Bin)  """  
      self.SelectedUOM:str = obj["SelectedUOM"]
      """  Selected Qty UOM  """  
      self.SelectedConvQty:int = obj["SelectedConvQty"]
      """  Selected Qty converted to InventoryUOM  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LotPartMtlRow:
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      self.Company:str = obj["Company"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  Mtl Part Num configured in Enginering Workbench  """  
      self.RequiredQty:int = obj["RequiredQty"]
      self.QtyPer:int = obj["QtyPer"]
      self.TotSelectedQty:int = obj["TotSelectedQty"]
      self.FixedQty:bool = obj["FixedQty"]
      self.ScrapQty:int = obj["ScrapQty"]
      self.ScrapType:str = obj["ScrapType"]
      self.UOMCode:str = obj["UOMCode"]
      self.LotTracked:bool = obj["LotTracked"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartLotAttributesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.Batch:str = obj["Batch"]
      self.MfgBatch:str = obj["MfgBatch"]
      self.MfgLot:str = obj["MfgLot"]
      self.HeatNum:str = obj["HeatNum"]
      self.FirmWare:str = obj["FirmWare"]
      self.BestBeforeDt:str = obj["BestBeforeDt"]
      self.CureDt:str = obj["CureDt"]
      self.ExpirationDate:str = obj["ExpirationDate"]
      self.ShipDocAvail:bool = obj["ShipDocAvail"]
      self.PartLotDescription:str = obj["PartLotDescription"]
      self.MfgDt:str = obj["MfgDt"]
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

class GetAvailAutoTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AvailTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartFromRowID_input:
   """ Required : 
   rowType
   vSysRowID
   """  
   def __init__(self, obj):
      self.rowType:str = obj["rowType"]
      self.vSysRowID:str = obj["vSysRowID"]
      pass

class GetPartFromRowID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.xrUomCode:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartXRefInfo_input:
   """ Required : 
   partNum
   SysRowID
   rowType
   uomCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.SysRowID:str = obj["SysRowID"]
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
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
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

class KanbanReceiptsGetNew_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["returnObj"]
      pass

class PreProcessKanbanReceipts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class PreProcessKanbanReceipts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.promptWIPStock:bool = obj["promptWIPStock"]
      self.promptNonConf:bool = obj["promptNonConf"]
      pass

      """  output parameters  """  

class ProcessKanbanReceipts_input:
   """ Required : 
   ds
   dSerialNoQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.dSerialNoQty:int = obj["dSerialNoQty"]
      """  The quantity of Serialized parts.  This value is returned by Serial # selector object.  """  
      pass

class ProcessKanbanReceipts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      pass

      """  output parameters  """  

class RestoreKanbanReceipt_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

class RestoreKanbanReceipt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetActionToSelSerNum_input:
   """ Required : 
   ds
   ipInventory
   ipScrapped
   ipNonconformance
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.ipInventory:int = obj["ipInventory"]
      """  Is the quantity of serial numbers to inventory  """  
      self.ipScrapped:int = obj["ipScrapped"]
      """  Is quantity of serial numbers to scrapped  """  
      self.ipNonconformance:int = obj["ipNonconformance"]
      """  Is the quantity of serial numbers nonconformance  """  
      pass

class SetActionToSelSerNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Submit_input:
   """ Required : 
   ds
   dSerialNoQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.dSerialNoQty:int = obj["dSerialNoQty"]
      """  The quantity of Serialized parts.  This value is returned by Serial # selector object.  """  
      pass

class Submit_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateLowerLevelLotTrackedParts_input:
   """ Required : 
   ds
   dSerialNoQty
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.dSerialNoQty:int = obj["dSerialNoQty"]
      """  The quantity of Serialized parts.  This value is returned by Serial # selector object.  """  
      pass

class ValidateLowerLevelLotTrackedParts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.cMessageText:str = obj["parameters"]
      self.lLotTrackedMtlExist:bool = obj["lLotTrackedMtlExist"]
      pass

      """  output parameters  """  

class ValidateNegQtyAction_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The quantity of Serialized parts.  This value is returned by Serial # selector object.  """  
      pass

class ValidateNegQtyAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opNegQtyAction:int = obj["parameters"]
      pass

      """  output parameters  """  

class ValidatePartMOM_input:
   """ Required : 
   partNum
   revNum
   altMethod
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part Num to be Validated  """  
      self.revNum:str = obj["revNum"]
      """  Revision Number  """  
      self.altMethod:str = obj["altMethod"]
      """  Alternate Method  """  
      pass

class ValidatePartMOM_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if validation passes.  """  
      pass

   def parameters(self, obj):
      self.oMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateParts_Kit_NonStock_Phantom_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part Num to be Validated  """  
      pass

class ValidateParts_Kit_NonStock_Phantom_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  True if validation passes.  """  
      pass

   def parameters(self, obj):
      self.oMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateSelectedSerNum_input:
   """ Required : 
   ds
   ipInventory
   ipScrapped
   ipNonconf
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      self.ipInventory:int = obj["ipInventory"]
      """  Is the quantity of serial numbers to inventory  """  
      self.ipScrapped:int = obj["ipScrapped"]
      """  Is quantity of serial numbers to scrapped  """  
      self.ipNonconf:int = obj["ipNonconf"]
      """  Is the quantity of serial numbers nonconformance  """  
      pass

class ValidateSelectedSerNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_KanbanReceiptsTableset] = obj["ds"]
      pass

      """  output parameters  """  

