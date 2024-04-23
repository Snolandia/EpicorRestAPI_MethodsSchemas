import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.InvTransferSvc
# Description: Inventory Transfer
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_ChangeFromBinRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromBinRowMod
   Description: Kinetic client. This method will pull qty for the bin.
   OperationID: ChangeFromBinRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromBinRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromBinRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFromBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromBin
   Description: This method will pull qty for the bin.
   OperationID: ChangeFromBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFromWhseRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromWhseRowMod
   Description: Kinetic client. This method validate from warehouse.
   OperationID: ChangeFromWhseRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromWhseRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromWhseRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFromWhse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromWhse
   Description: This method validate from warehouse.
   OperationID: ChangeFromWhse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeFromWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLotRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLotRowMod
   Description: kinetic client. Recalculates on hand qty when lot number changes.
   OperationID: ChangeLotRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLotRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLotRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLot(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLot
   Description: Recalculates on hand qty when lot number changes.
   OperationID: ChangeLot
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAttributeSetIDRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAttributeSetIDRowMod
   Description: Kinetic client. Recalculates on hand qty when attribute set changes.
   OperationID: ChangeAttributeSetIDRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAttributeSetIDRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAttributeSetIDRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAttributeSetID
   Description: Recalculates on hand qty when attribute set changes.
   OperationID: ChangeAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToBinRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToBinRowMod
   Description: Kinetic client. This method will pull qty for the TO bin.
   OperationID: ChangeToBinRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToBinRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToBinRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToBin
   Description: This method will pull qty for the TO bin.
   OperationID: ChangeToBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToWhseRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToWhseRowMod
   Description: Kinetic client
   OperationID: ChangeToWhseRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToWhseRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToWhseRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToWhse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToWhse
   Description: This method validate to warehouse.
   OperationID: ChangeToWhse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeToWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUOMRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUOMRowMod
   Description: Kinetic client. Recalculates on hand qty and Num of Pieces when the inventory transfer UOM changes.
   OperationID: ChangeUOMRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUOMRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUOMRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUOM
   Description: Recalculates on hand qty when the inventory transfer UOM changes.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingTransferQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingTransferQty
   Description: Call this method when the transferQty changes
   OperationID: OnChangingTransferQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTransferQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTransferQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingTransferQtyUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingTransferQtyUOM
   Description: Call this method when the transferQtyUOM changes
   OperationID: OnChangingTransferQtyUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangingTransferQtyUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTransferQtyUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CommitTransfer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CommitTransfer
   Description: This method will commit the inventory transfer .
Serial numbers are passed from the serial number object through the
ttSelectedSerialNumbers temptable.
   OperationID: CommitTransfer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailBins(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailBins
   Description: Based on the parameter AllBins, either all bins or only current bins will be
returned in the Bins Data table.
   OperationID: GetAvailBins
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailBins_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailBins_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewInventoryTransfer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewInventoryTransfer
   OperationID: GetNewInventoryTransfer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewInventoryTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInventoryTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCID
   Description: Change PCID.
   OperationID: ChangePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTransferPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTransferPartNum
   OperationID: ChangeTransferPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTransferPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTransferPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTransferQtyRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTransferQtyRowMod
   Description: Kinetic client. Change Transfer Qty.
   OperationID: ChangeTransferQtyRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTransferQtyRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTransferQtyRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTransferQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTransferQty
   Description: Change Transfer Qty.
   OperationID: ChangeTransferQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTransferQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTransferQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPrimaryBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPrimaryBin
   Description: Note: This method should be called when either the From or To Warehouse code changes.
Purpose: Get the Part (From or To) Warehouse's Primary Bin when the Warehouse is changed.
   OperationID: GetPrimaryBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPrimaryBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrimaryBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSelectSerialNumbersParamsRowMod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParamsRowMod
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParamsRowMod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParamsRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParamsRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTransferRecord(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTransferRecord
   Description: This method creates a template transfer record . Gets defaults for the part to
be transfered  .
   OperationID: GetTransferRecord
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTransferRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransferRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNotSelectedInvTransferRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNotSelectedInvTransferRecords
   OperationID: GetNotSelectedInvTransferRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNotSelectedInvTransferRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNotSelectedInvTransferRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvTransferRecords(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvTransferRecords
   OperationID: GetInvTransferRecords
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvTransferRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvTransferRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreCommitTransfer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreCommitTransfer
   Description: This method will return a record in the LegalNumberGenerate datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreCommitTransfer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreCommitTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCommitTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AttributeSetSplitPreLoadCheck(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AttributeSetSplitPreLoadCheck
   Description: Specific checks related to Attribute Split to validate can load Inventory Attribute Entry form.
   OperationID: AttributeSetSplitPreLoadCheck
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AttributeSetSplitPreLoadCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AttributeSetSplitPreLoadCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AreSNumsAllocated(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AreSNumsAllocated
   Description: AreSNumsAllocated method.
   OperationID: AreSNumsAllocated
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AreSNumsAllocated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AreSNumsAllocated_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   Description: GetAvailTranDocTypes method.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_NegativeInventoryTest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NegativeInventoryTest
   Description: NegativeInventoryTest method.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MasterInventoryBinTests(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MasterInventoryBinTests
   Description: Methods to check Negative Inventory and Contract bin.
   OperationID: MasterInventoryBinTests
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MasterInventoryBinTests_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MasterInventoryBinTests_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   Description: GetPartFromRowID method.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvTransferRecordsForPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvTransferRecordsForPCID
   Description: Get records for a list of PCIDs
   OperationID: GetInvTransferRecordsForPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvTransferRecordsForPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvTransferRecordsForPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CommitTransferAndUpdateHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CommitTransferAndUpdateHistory
   Description: Used at the MetaFX. This method will commit the inventory transfer .
Serial numbers are passed from the serial number object through the
ttSelectedSerialNumbers temptable.
   OperationID: CommitTransferAndUpdateHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CommitTransferAndUpdateHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitTransferAndUpdateHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateHistory(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateHistory
   Description: This method will update the InventoryTransfer history using the info in the dataset
   OperationID: UpdateHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetInvTransferRecordsForStandardPCIDList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetInvTransferRecordsForStandardPCIDList
   Description: Used at the MetaFX. Get records for a list of PCIDs delimited by '~'
   OperationID: GetInvTransferRecordsForStandardPCIDList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetInvTransferRecordsForStandardPCIDList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvTransferRecordsForStandardPCIDList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckAdvancedMaterialAndPackageControl(epicorHeaders = None):
   """  
   Summary: Invoke method CheckAdvancedMaterialAndPackageControl
   Description: Check Advanced Material and Package Control availability
   OperationID: CheckAdvancedMaterialAndPackageControl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAdvancedMaterialAndPackageControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_ValidatePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePartNum
   Description: Used at the MetaFX.Client logic transition
   OperationID: ValidatePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePCID
   Description: Used at the MetaFX.Client logic transition
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AreSNumsAllocated_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      pass

class AreSNumsAllocated_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class AttributeSetSplitPreLoadCheck_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class AttributeSetSplitPreLoadCheck_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeAttributeSetIDRowMod_input:
   """ Required : 
   ipAttributeSetID
   ds
   """  
   def __init__(self, obj):
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeAttributeSetIDRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeAttributeSetID_input:
   """ Required : 
   ipAttributeSetID
   ds
   """  
   def __init__(self, obj):
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeAttributeSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFromBinRowMod_input:
   """ Required : 
   ipBinNum
   ds
   """  
   def __init__(self, obj):
      self.ipBinNum:str = obj["ipBinNum"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeFromBinRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFromBin_input:
   """ Required : 
   ipBinNum
   ds
   """  
   def __init__(self, obj):
      self.ipBinNum:str = obj["ipBinNum"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeFromBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFromWhseRowMod_input:
   """ Required : 
   ipwhseCode
   ds
   """  
   def __init__(self, obj):
      self.ipwhseCode:str = obj["ipwhseCode"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeFromWhseRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFromWhse_input:
   """ Required : 
   ipwhseCode
   ds
   """  
   def __init__(self, obj):
      self.ipwhseCode:str = obj["ipwhseCode"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeFromWhse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLotRowMod_input:
   """ Required : 
   ipLotNum
   ipFromTo
   ds
   """  
   def __init__(self, obj):
      self.ipLotNum:str = obj["ipLotNum"]
      self.ipFromTo:str = obj["ipFromTo"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeLotRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangeLot_input:
   """ Required : 
   ipLotNum
   ipFromTo
   ds
   """  
   def __init__(self, obj):
      self.ipLotNum:str = obj["ipLotNum"]
      self.ipFromTo:str = obj["ipFromTo"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeLot_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class ChangePCID_input:
   """ Required : 
   tranPCID
   ds
   """  
   def __init__(self, obj):
      self.tranPCID:str = obj["tranPCID"]
      """  Package Control ID  """  
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToBinRowMod_input:
   """ Required : 
   ipToBinNum
   ds
   """  
   def __init__(self, obj):
      self.ipToBinNum:str = obj["ipToBinNum"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeToBinRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToBin_input:
   """ Required : 
   ipToBinNum
   ds
   """  
   def __init__(self, obj):
      self.ipToBinNum:str = obj["ipToBinNum"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeToBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToWhseRowMod_input:
   """ Required : 
   ipToWhse
   ds
   """  
   def __init__(self, obj):
      self.ipToWhse:str = obj["ipToWhse"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeToWhseRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToWhse_input:
   """ Required : 
   ipToWhse
   ds
   """  
   def __init__(self, obj):
      self.ipToWhse:str = obj["ipToWhse"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeToWhse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTransferPartNum_input:
   """ Required : 
   tranPartNum
   ds
   """  
   def __init__(self, obj):
      self.tranPartNum:str = obj["tranPartNum"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeTransferPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTransferQtyRowMod_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:int = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeTransferQtyRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTransferQty_input:
   """ Required : 
   proposedValue
   ds
   """  
   def __init__(self, obj):
      self.proposedValue:int = obj["proposedValue"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeTransferQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeUOMRowMod_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeUOMRowMod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeUOM_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ChangeUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckAdvancedMaterialAndPackageControl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.amAvailable:bool = obj["amAvailable"]
      self.pcAvailable:bool = obj["pcAvailable"]
      pass

      """  output parameters  """  

class CommitTransferAndUpdateHistory_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class CommitTransferAndUpdateHistory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      self.LegalNumberMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CommitTransfer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class CommitTransfer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      self.LegalNumberMessage:str = obj["parameters"]
      self.partTranPKs:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_InvTransRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.TranDate:str = obj["TranDate"]
      """  Date of transaction.  """  
      self.FromWarehouseCode:str = obj["FromWarehouseCode"]
      """  The Warehouse the part is being transferred From.  """  
      self.FromWarehouseDesc:str = obj["FromWarehouseDesc"]
      self.ToWarehouseCode:str = obj["ToWarehouseCode"]
      """  The Warehouse the part is being transferred To.  """  
      self.ToWarehouseDesc:str = obj["ToWarehouseDesc"]
      self.FromBinNum:str = obj["FromBinNum"]
      """  The Warehouse Bin the part is being transferred From.  """  
      self.FromBinDesc:str = obj["FromBinDesc"]
      self.ToBinNum:str = obj["ToBinNum"]
      """  The Warehouse Bin the part is being transferred To.  """  
      self.ToBinDesc:str = obj["ToBinDesc"]
      self.FromLotNumber:str = obj["FromLotNumber"]
      """  The Lot number that is being transferred.  """  
      self.ToLotNumber:str = obj["ToLotNumber"]
      """  The Lot number that is being transferred to.  """  
      self.FromOnHandQty:int = obj["FromOnHandQty"]
      self.ToOnHandQty:int = obj["ToOnHandQty"]
      self.Plant:str = obj["Plant"]
      self.Plant2:str = obj["Plant2"]
      self.PartNum:str = obj["PartNum"]
      """  The Part Number selected for inventory transfer.  """  
      self.TrackDimension:bool = obj["TrackDimension"]
      self.TrackSerialnumbers:bool = obj["TrackSerialnumbers"]
      self.TrackLots:bool = obj["TrackLots"]
      self.PartDescription:str = obj["PartDescription"]
      self.SearchWord:str = obj["SearchWord"]
      self.TranReference:str = obj["TranReference"]
      """  Transaction reference.  Can be used to hold a short comment.  """  
      self.FromPlant:str = obj["FromPlant"]
      """  Plant than owns the FromWarehouseCode  """  
      self.FromPlantTracking:bool = obj["FromPlantTracking"]
      """  If FromPlant is Full Serial Tracking  """  
      self.ToPlant:str = obj["ToPlant"]
      """  Plant that owns the ToWarehouseCode  """  
      self.ToPlantTracking:bool = obj["ToPlantTracking"]
      """  If ToPlant is Full Serial Tracking  """  
      self.FromOnHandUOM:str = obj["FromOnHandUOM"]
      self.TransferQty:int = obj["TransferQty"]
      """  Transfer Quantity entered for this inventory transfer.  """  
      self.TransferQtyUOM:str = obj["TransferQtyUOM"]
      """  The unit of measure the quantify of this transfer is specified in.  """  
      self.ToOnHandUOM:str = obj["ToOnHandUOM"]
      self.TrackingUOM:str = obj["TrackingUOM"]
      self.TrackingQty:int = obj["TrackingQty"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  """  
      self.ToOrderNum:int = obj["ToOrderNum"]
      self.ToOrderLine:int = obj["ToOrderLine"]
      self.ToOrderRelNum:int = obj["ToOrderRelNum"]
      self.PCID:str = obj["PCID"]
      """  Package Control Identification Number.  """  
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.CallCode:str = obj["CallCode"]
      """  Call Code from FSA  """  
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code from FSA  """  
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty Code from FSA  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract Num from FSA  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.Source:str = obj["Source"]
      self.SysRowID:str = obj["SysRowID"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.PartTrackDimension:bool = obj["PartTrackDimension"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.WarehouseFilterPartNum_Kinetic:str = obj["WarehouseFilterPartNum_Kinetic"]
      self.WarehouseFilterPlant_Kinetic:str = obj["WarehouseFilterPlant_Kinetic"]
      self.Key_Kinetic:str = obj["Key_Kinetic"]
      """  Contains PCID or PartNum. Use for Crumb bar items  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.PartSysRowID:str = obj["PartSysRowID"]
      """  Unique SysRowID for the related part record.  """  
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      self.ToAttributeSetID:int = obj["ToAttributeSetID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_InvTransferTableset:
   def __init__(self, obj):
      self.InvTrans:list[Erp_Tablesets_InvTransRow] = obj["InvTrans"]
      self.TransferHistory:list[Erp_Tablesets_TransferHistoryRow] = obj["TransferHistory"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.Parts:list[Erp_Tablesets_PartsRow] = obj["Parts"]
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

class Erp_Tablesets_PartsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
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

class Erp_Tablesets_TransferHistoryRow:
   def __init__(self, obj):
      self.History:str = obj["History"]
      """  Transfer history  """  
      self.PartNum:str = obj["PartNum"]
      self.PartTranPKs:str = obj["PartTranPKs"]
      self.PCID:str = obj["PCID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAvailBins_input:
   """ Required : 
   PartNum
   AllBins
   WarehouseCode
   LotNum
   DimCode
   """  
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      """  Part Number  (current only).  """  
      self.AllBins:str = obj["AllBins"]
      """  A for all bins or C for current warehouse.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse code.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot number  (current only).  """  
      self.DimCode:str = obj["DimCode"]
      """  UNIT OF MEASURE (old Dimension Code)  """  
      pass

class GetAvailBins_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.BinList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.listAvailTranDocTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetInvTransferRecordsForPCID_input:
   """ Required : 
   ipPCIDList
   fromPCIDContextSearch
   ds
   """  
   def __init__(self, obj):
      self.ipPCIDList:str = obj["ipPCIDList"]
      self.fromPCIDContextSearch:bool = obj["fromPCIDContextSearch"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class GetInvTransferRecordsForPCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvTransferTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorMessages:str = obj["parameters"]
      self.PCIDList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetInvTransferRecordsForStandardPCIDList_input:
   """ Required : 
   ipPCIDList
   fromPCIDContextSearch
   ds
   """  
   def __init__(self, obj):
      self.ipPCIDList:str = obj["ipPCIDList"]
      self.fromPCIDContextSearch:bool = obj["fromPCIDContextSearch"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class GetInvTransferRecordsForStandardPCIDList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvTransferTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorMessages:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetInvTransferRecords_input:
   """ Required : 
   ipPartList
   ds
   """  
   def __init__(self, obj):
      self.ipPartList:str = obj["ipPartList"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class GetInvTransferRecords_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvTransferTableset] = obj["returnObj"]
      pass

class GetNewInventoryTransfer_input:
   """ Required : 
   ipSourceType
   ds
   """  
   def __init__(self, obj):
      self.ipSourceType:str = obj["ipSourceType"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class GetNewInventoryTransfer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNotSelectedInvTransferRecords_input:
   """ Required : 
   ipPartList
   ds
   """  
   def __init__(self, obj):
      self.ipPartList:str = obj["ipPartList"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class GetNotSelectedInvTransferRecords_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvTransferTableset] = obj["returnObj"]
      pass

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
   uomCode
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
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

class GetPrimaryBin_input:
   """ Required : 
   iPartNum
   iWarehouseCode
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  Part Number  """  
      self.iWarehouseCode:str = obj["iWarehouseCode"]
      """  WarehouseCode  """  
      pass

class GetPrimaryBin_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.PrimaryBin:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParamsRowMod_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class GetSelectSerialNumbersParamsRowMod_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetTransferRecord_input:
   """ Required : 
   iPartNum
   sysRowID
   iPCID
   uomCode
   ds
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  Part Number  """  
      self.sysRowID:str = obj["sysRowID"]
      """  row id  """  
      self.iPCID:str = obj["iPCID"]
      """  Package Control ID  """  
      self.uomCode:str = obj["uomCode"]
      """  UOM Code (only used for Product Codes)  """  
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class GetTransferRecord_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.rowAdded:bool = obj["rowAdded"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
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

class MasterInventoryBinTests_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class MasterInventoryBinTests_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      self.pcNeqQtyAction:str = obj["parameters"]
      self.pcNeqQtyMessage:str = obj["parameters"]
      self.pcFromPCBinAction:str = obj["parameters"]
      self.pcFromPCBinMessage:str = obj["parameters"]
      self.pcToPCBinAction:str = obj["parameters"]
      self.pcToPCBinMessage:str = obj["parameters"]
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
   pcUOMCode
   pdTranQty
   pdDimConvFactor
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      self.pcWhseCode:str = obj["pcWhseCode"]
      self.pcBinNum:str = obj["pcBinNum"]
      self.pcLotNum:str = obj["pcLotNum"]
      self.pcAttributeSetID:int = obj["pcAttributeSetID"]
      self.pcPCID:str = obj["pcPCID"]
      self.pcUOMCode:str = obj["pcUOMCode"]
      self.pdTranQty:int = obj["pdTranQty"]
      self.pdDimConvFactor:int = obj["pdDimConvFactor"]
      pass

class NegativeInventoryTest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.pcNeqQtyAction:str = obj["parameters"]
      self.pcMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   dispNumberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.dispNumberOfPieces:int = obj["dispNumberOfPieces"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingTransferQtyUOM_input:
   """ Required : 
   transferQtyUOM
   ds
   """  
   def __init__(self, obj):
      self.transferQtyUOM:str = obj["transferQtyUOM"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class OnChangingTransferQtyUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingTransferQty_input:
   """ Required : 
   transferQty
   ds
   """  
   def __init__(self, obj):
      self.transferQty:int = obj["transferQty"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class OnChangingTransferQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreCommitTransfer_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class PreCommitTransfer_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      self.RequiresUserInput:bool = obj["RequiresUserInput"]
      pass

      """  output parameters  """  

class UpdateHistory_input:
   """ Required : 
   ds
   partTransPKsParam
   tranQty
   tranQtyUOM
   fromWarehouseDesc
   fromBinDesc
   toWarehouseDesc
   toBinDesc
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      self.partTransPKsParam:str = obj["partTransPKsParam"]
      """  partTransPKs value generated from transfer, if applicable  """  
      self.tranQty:str = obj["tranQty"]
      """  Transfer Quantity  """  
      self.tranQtyUOM:str = obj["tranQtyUOM"]
      """  Transfer Quantity UOM  """  
      self.fromWarehouseDesc:str = obj["fromWarehouseDesc"]
      """  From Warehouse Description  """  
      self.fromBinDesc:str = obj["fromBinDesc"]
      """  From Warehouse Bin Description  """  
      self.toWarehouseDesc:str = obj["toWarehouseDesc"]
      """  To Warehouse Description  """  
      self.toBinDesc:str = obj["toBinDesc"]
      """  To Warehouse Bin Description  """  
      pass

class UpdateHistory_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePCID_input:
   """ Required : 
   proposedPCID
   uomCodePartXRef
   refreshMode
   pcidList
   ds
   """  
   def __init__(self, obj):
      self.proposedPCID:str = obj["proposedPCID"]
      self.uomCodePartXRef:str = obj["uomCodePartXRef"]
      self.refreshMode:bool = obj["refreshMode"]
      self.pcidList:str = obj["pcidList"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ValidatePCID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvTransferTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      self.rowAdded:bool = obj["rowAdded"]
      pass

      """  output parameters  """  

class ValidatePartNum_input:
   """ Required : 
   proposedPartNum
   uomCodePartXRef
   refreshMode
   partList
   ds
   """  
   def __init__(self, obj):
      self.proposedPartNum:str = obj["proposedPartNum"]
      self.uomCodePartXRef:str = obj["uomCodePartXRef"]
      self.refreshMode:bool = obj["refreshMode"]
      self.partList:str = obj["partList"]
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      pass

class ValidatePartNum_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_InvTransferTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      self.rowAdded:bool = obj["rowAdded"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   ds
   serialNumber
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_InvTransferTableset] = obj["ds"]
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

