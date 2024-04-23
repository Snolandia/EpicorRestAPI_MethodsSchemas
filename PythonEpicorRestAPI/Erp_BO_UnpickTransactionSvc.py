import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.UnpickTransactionSvc
# Description: BO for Unpick screens
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_Init(epicorHeaders = None):
   """  
   Summary: Invoke method Init
   Description: Init
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_ChangeFromBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromBin
   Description: Validate the bin and populate description
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeFromWhse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeFromWhse
   Description: Validate the warehouse and populate description
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJobAsm(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJobAsm
   Description: Validate the job assembly
   OperationID: ChangeJobAsm
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJobMtlSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJobMtlSeq
   Description: Validate the job mtl seqr and populate mtl data
   OperationID: ChangeJobMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeJobNum
   Description: Validate the job number
   OperationID: ChangeJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeLotNum
   Description: Validate the part and set the description
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOrderLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOrderLine
   Description: Validate the order line
   OperationID: ChangeOrderLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOrderNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOrderNum
   Description: Validate the order number
   OperationID: ChangeOrderNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeOrderRelNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeOrderRelNum
   Description: Validate the order release number and populate release data
   OperationID: ChangeOrderRelNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeOrderRelNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderRelNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePartNum
   Description: Validate the part and set the description
   OperationID: ChangePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeAttributeSetID
   Description: Validate the attribute set and set the description
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRevisionNum
   Description: Validate revision num
   OperationID: ChangeRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSupplyJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSupplyJobNum
   Description: Validate the supply job number
   OperationID: ChangeSupplyJobNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSupplyJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSupplyJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUnpickQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUnpickQty
   Description: Call this method when the UnpickQty changes
   OperationID: ChangeUnpickQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUnpickQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnpickQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeUnpickUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeUnpickUOM
   Description: Call this method when the unpickQtyUOM changes
   OperationID: ChangeUnpickUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeUnpickUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnpickUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: ChangeNumberOfPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangePCID
   Description: Validate the PCID
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFOrdLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFOrdLine
   Description: Validate the transfer order line number and populate line data
   OperationID: ChangeTFOrdLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTFOrdNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTFOrdNum
   Description: Validate the transfer order number
   OperationID: ChangeTFOrdNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToBin
   Description: Validate the bin and populate description
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeToWhse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeToWhse
   Description: Validate the whse and populate description
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewUnpickTransaction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewUnpickTransaction
   Description: Gets a new ttUnpickTransaction record
   OperationID: GetNewUnpickTransaction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewUnpickTransaction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUnpickTransaction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreUnpickTransaction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreUnpickTransaction
   Description: PreUnpickTransaction - Validates unpick before any changes happen
   OperationID: PreUnpickTransaction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreUnpickTransaction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUnpickTransaction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnpickTransaction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method _UnpickTransaction
   Description: Unpicks a transaction
1) Validates Unpick
2) Updates PartAlloc for Transfer Orders
3) Updates Picked Orders for Sales Orders
   OperationID: _UnpickTransaction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/_UnpickTransaction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/_UnpickTransaction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailTranDocTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Method to call to get available tran doc types.
   OperationID: GetAvailTranDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailTranDocTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_HandheldPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method HandheldPCID
   Description: Validate that the current Transfer Order/Line is not attached to a PCID
   OperationID: HandheldPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/HandheldPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HandheldPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeAttributeSetID_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:int = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeAttributeSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFromBin_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:str = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeFromBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeFromWhse_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:str = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeFromWhse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeJobAsm_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:int = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeJobAsm_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeJobMtlSeq_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:int = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeJobMtlSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeJobNum_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:str = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeLotNum_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:str = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeNumberOfPieces_input:
   """ Required : 
   dispNumberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.dispNumberOfPieces:int = obj["dispNumberOfPieces"]
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOrderLine_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:int = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeOrderLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOrderNum_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:int = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeOrderNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeOrderRelNum_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:int = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeOrderRelNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePCID_input:
   """ Required : 
   ipPCID
   ds
   """  
   def __init__(self, obj):
      self.ipPCID:str = obj["ipPCID"]
      """  Proposed PCID value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangePCID_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangePartNum_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:str = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSupplyJobNum_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:str = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeSupplyJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFOrdLine_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:int = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeTFOrdLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTFOrdNum_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:str = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeTFOrdNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToBin_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:str = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeToBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeToWhse_input:
   """ Required : 
   ipProposedValue
   ds
   """  
   def __init__(self, obj):
      self.ipProposedValue:str = obj["ipProposedValue"]
      """  Proposed Value  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeToWhse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeUnpickQty_input:
   """ Required : 
   unpickQty
   ds
   """  
   def __init__(self, obj):
      self.unpickQty:int = obj["unpickQty"]
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeUnpickQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeUnpickUOM_input:
   """ Required : 
   unpickUOM
   ds
   """  
   def __init__(self, obj):
      self.unpickUOM:str = obj["unpickUOM"]
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class ChangeUnpickUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_UnpickTransactionRow:
   def __init__(self, obj):
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.TFOrdLine:int = obj["TFOrdLine"]
      self.PartNum:str = obj["PartNum"]
      self.LotNum:str = obj["LotNum"]
      self.UnpickQty:int = obj["UnpickQty"]
      self.UnpickUOM:str = obj["UnpickUOM"]
      self.FromWhse:str = obj["FromWhse"]
      self.ToWhse:str = obj["ToWhse"]
      self.FromBin:str = obj["FromBin"]
      self.ToBin:str = obj["ToBin"]
      self.AvailQty:int = obj["AvailQty"]
      self.AvailUOM:str = obj["AvailUOM"]
      self.FromBinDesc:str = obj["FromBinDesc"]
      self.ToBinDesc:str = obj["ToBinDesc"]
      self.FromWhseDesc:str = obj["FromWhseDesc"]
      self.ToWhseDesc:str = obj["ToWhseDesc"]
      self.PartDesc:str = obj["PartDesc"]
      self.LotTracked:bool = obj["LotTracked"]
      self.SerialTracked:bool = obj["SerialTracked"]
      self.UnpickType:str = obj["UnpickType"]
      """  Valid values are "O" for sales order, "J" for job, or "T" for transfer order.  """  
      self.PCID:str = obj["PCID"]
      """  PCID to Unpick From  """  
      self.EnablePCID:bool = obj["EnablePCID"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.PkgControlHeaderDeleted:bool = obj["PkgControlHeaderDeleted"]
      """  Indicates if a PkgControlHeader record was deleted during the Unpick Transaction.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.SupplyJobNum:str = obj["SupplyJobNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UnpickTransactionTableset:
   def __init__(self, obj):
      self.UnpickTransaction:list[Erp_Tablesets_UnpickTransactionRow] = obj["UnpickTransaction"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAvailTranDocTypes_input:
   """ Required : 
   unpickType
   """  
   def __init__(self, obj):
      self.unpickType:str = obj["unpickType"]
      """  The unpick type of the transaction  """  
      pass

class GetAvailTranDocTypes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.AvailTypes:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetNewUnpickTransaction_input:
   """ Required : 
   ipType
   ds
   """  
   def __init__(self, obj):
      self.ipType:str = obj["ipType"]
      """  Type (O=Order/J=Job/T=TO)  """  
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class GetNewUnpickTransaction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

class HandheldPCID_input:
   """ Required : 
   TFOrdNum
   TFOrdLine
   LotNum
   UOM
   """  
   def __init__(self, obj):
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  Transfer Order Number  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  Transfer Order Line  """  
      self.LotNum:str = obj["LotNum"]
      """  Part Lot Number  """  
      self.UOM:str = obj["UOM"]
      """  Available Unit of Measure  """  
      pass

class HandheldPCID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
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

class Init_output:
   def __init__(self, obj):
      pass

class PreUnpickTransaction_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class PreUnpickTransaction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      self.msg:str = obj["parameters"]
      pass

      """  output parameters  """  

class _UnpickTransaction_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

class _UnpickTransaction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UnpickTransactionTableset] = obj["ds"]
      pass

      """  output parameters  """  

