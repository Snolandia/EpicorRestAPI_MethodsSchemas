import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PkgControlIDBuildSplitMergeSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AddPartToPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddPartToPCID
   Description: Add Part to PCID
   OperationID: AddPartToPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddPartToPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddPartToPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddPartToPCIDAndRefreshDest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddPartToPCIDAndRefreshDest
   Description: Add Part to PCID
   OperationID: AddPartToPCIDAndRefreshDest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddPartToPCIDAndRefreshDest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddPartToPCIDAndRefreshDest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AddPCIDToPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddPCIDToPCID
   Description: Add PCID to PCID
   OperationID: AddPCIDToPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddPCIDToPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddPCIDToPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveFromSourcePCIDToDestPCIDAndRefresh(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveFromSourcePCIDToDestPCIDAndRefresh
   Description: Move from Source PCID to Destination PCID
   OperationID: MoveFromSourcePCIDToDestPCIDAndRefresh
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveFromSourcePCIDToDestPCIDAndRefresh_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveFromSourcePCIDToDestPCIDAndRefresh_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveFromDestPCIDToSourcePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveFromDestPCIDToSourcePCID
   Description: Move from Destination PCID to Source PCID
   OperationID: MoveFromDestPCIDToSourcePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveFromDestPCIDToSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveFromDestPCIDToSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MoveFromSourcePCIDToDestPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MoveFromSourcePCIDToDestPCID
   Description: Move from Source PCID to Destination PCID
   OperationID: MoveFromSourcePCIDToDestPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MoveFromSourcePCIDToDestPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MoveFromSourcePCIDToDestPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveFromDestPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveFromDestPCID
   Description: Remove from Dest PCID
   OperationID: RemoveFromDestPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveFromDestPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveFromDestPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveFromSourcePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveFromSourcePCID
   Description: Remove from Source PCID
   OperationID: RemoveFromSourcePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveFromSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveFromSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSourcePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSourcePCID
   Description: Returns the Source PCID dataset.
   OperationID: GetSourcePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDestPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDestPCID
   Description: Returns the Destination PCID dataset.
   OperationID: GetDestPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDestPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDestPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDestPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDestPCID
   Description: OnChangeDestPCID
   OperationID: OnChangeDestPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDestPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDestPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeDestBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeDestBinNum
   Description: OnChangeDestBinNum
   OperationID: OnChangeDestBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeDestBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDestBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeItemPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeItemPartNum
   Description: OnChangeItemPartNum
   OperationID: OnChangeItemPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeItemPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeItemPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeItemPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeItemPCID
   Description: OnChangeItemPCID
   OperationID: OnChangeItemPCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeItemPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeItemPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeItemLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeItemLotNum
   Description: Method to call when the source item lot number changes.
   OperationID: OnChangeItemLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeItemLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeItemLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSourcePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSourcePartNum
   Description: OnChangeSourcePartNum
   OperationID: OnChangeSourcePartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSourcePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourcePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSourceAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSourceAttributeSetID
   Description: OnChangeSourceAttributeSetID
   OperationID: OnChangeSourceAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSourceAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourceAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSourcePartBinNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSourcePartBinNum
   Description: OnChangeSourcePartBinNum
   OperationID: OnChangeSourcePartBinNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSourcePartBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourcePartBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSourcePartLotNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSourcePartLotNum
   Description: OnChangeSourcePartLotNum
   OperationID: OnChangeSourcePartLotNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSourcePartLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourcePartLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSourceQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSourceQty
   Description: OnChangeSourcePartQuantity
   OperationID: OnChangeSourceQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSourceQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourceQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangingNumberOfPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new request qty
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSourcePartUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSourcePartUOM
   Description: OnChangeSourcePartIUM
   OperationID: OnChangeSourcePartUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSourcePartUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourcePartUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSourcePCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSourcePCID
   Description: OnChangeSourcePCID
   OperationID: OnChangeSourcePCID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSourcePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourcePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSourcePCIDHandheld(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSourcePCIDHandheld
   Description: OnChangeSourcePCIDHandheld
   OperationID: OnChangeSourcePCIDHandheld
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSourcePCIDHandheld_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourcePCIDHandheld_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeSourceRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeSourceRevisionNum
   Description: OnChangeSourceRevisionNum
   OperationID: OnChangeSourceRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeSourceRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSourceRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultWarehouse(epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultWarehouse
   Description: Returns the Default Warehouse for the current session company and site
   OperationID: GetDefaultWarehouse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCIDDestination(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCIDDestination
   OperationID: GetNewPCIDDestination
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCIDDestination_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCIDDestination_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCIDSource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCIDSource
   OperationID: GetNewPCIDSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCIDSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCIDSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPCIDPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPCIDPart
   OperationID: GetNewPCIDPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPCIDPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPCIDPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_NegativeInventoryTest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method NegativeInventoryTest
   Description: Checks if the quantity will move the inventory quantity negative
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PkgControlIDBuildSplitMergeSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AddPCIDToPCID_input:
   """ Required : 
   sourceDS
   destDS
   """  
   def __init__(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

class AddPCIDToPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

      """  output parameters  """  

class AddPartToPCIDAndRefreshDest_input:
   """ Required : 
   sourceDS
   destDS
   destPCID
   warehouseCode
   """  
   def __init__(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourceDS"]
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      self.destPCID:str = obj["destPCID"]
      """  Destination PCID  """  
      self.warehouseCode:str = obj["warehouseCode"]
      """  Selected Warehouse  """  
      pass

class AddPartToPCIDAndRefreshDest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourceDS"]
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

      """  output parameters  """  

class AddPartToPCID_input:
   """ Required : 
   sourceDS
   destDS
   """  
   def __init__(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourceDS"]
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

class AddPartToPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourceDS"]
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

      """  output parameters  """  

class Erp_Tablesets_PCIDBuildSplitMergeDestItemRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PCID:str = obj["PCID"]
      self.PCIDItemSeq:int = obj["PCIDItemSeq"]
      self.ItemPCID:str = obj["ItemPCID"]
      self.ItemPartNum:str = obj["ItemPartNum"]
      self.ItemPartDesc:str = obj["ItemPartDesc"]
      self.ItemLotNum:str = obj["ItemLotNum"]
      self.ItemIUM:str = obj["ItemIUM"]
      self.ItemQuantity:int = obj["ItemQuantity"]
      self.SerialTrackedPart:bool = obj["SerialTrackedPart"]
      self.PrevItemPCID:str = obj["PrevItemPCID"]
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.MoveQuantity:int = obj["MoveQuantity"]
      self.LotTrackedPart:bool = obj["LotTrackedPart"]
      self.ItemAttributeSetID:int = obj["ItemAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ItemAttributeSetDescription:str = obj["ItemAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.ItemAttributeSetShortDescription:str = obj["ItemAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ItemPartAttrClassID:str = obj["ItemPartAttrClassID"]
      self.ItemRevisionNum:str = obj["ItemRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCIDBuildSplitMergeDestRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PCID:str = obj["PCID"]
      self.PkgControlStatus:str = obj["PkgControlStatus"]
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgControlIDDesc:str = obj["PkgControlIDDesc"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.PreviousPCID:str = obj["PreviousPCID"]
      self.Plant:str = obj["Plant"]
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      self.BinNum:str = obj["BinNum"]
      self.BinDescription:str = obj["BinDescription"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.PCIDContainsChildParts:bool = obj["PCIDContainsChildParts"]
      self.PCIDContainsChildPCIDs:bool = obj["PCIDContainsChildPCIDs"]
      self.BinNumEnabled:bool = obj["BinNumEnabled"]
      self.SerialNumberTracking:bool = obj["SerialNumberTracking"]
      """  Indicates if serial number tracking is available.  Is set to true when the warehouse plant does full serial tracking, or the warehouse plant does outbound serial tracking and the PCID is an outbound container.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCIDBuildSplitMergeDestTableset:
   def __init__(self, obj):
      self.PCIDBuildSplitMergeDest:list[Erp_Tablesets_PCIDBuildSplitMergeDestRow] = obj["PCIDBuildSplitMergeDest"]
      self.PCIDBuildSplitMergeDestItem:list[Erp_Tablesets_PCIDBuildSplitMergeDestItemRow] = obj["PCIDBuildSplitMergeDestItem"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PCIDBuildSplitMergeSourceItemRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PCID:str = obj["PCID"]
      self.PCIDItemSeq:int = obj["PCIDItemSeq"]
      self.ItemPCID:str = obj["ItemPCID"]
      self.ItemPartNum:str = obj["ItemPartNum"]
      self.ItemPartDesc:str = obj["ItemPartDesc"]
      self.ItemLotNum:str = obj["ItemLotNum"]
      self.ItemIUM:str = obj["ItemIUM"]
      self.ItemQuantity:int = obj["ItemQuantity"]
      self.MoveQuantity:int = obj["MoveQuantity"]
      self.PrevItemPCID:str = obj["PrevItemPCID"]
      self.SerialTrackedPart:bool = obj["SerialTrackedPart"]
      self.SelectedForAction:bool = obj["SelectedForAction"]
      self.LotTrackedPart:bool = obj["LotTrackedPart"]
      self.ItemAttributeSetID:int = obj["ItemAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ItemAttributeSetDescription:str = obj["ItemAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.ItemAttributeSetShortDescription:str = obj["ItemAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.ItemPartAttrClassID:str = obj["ItemPartAttrClassID"]
      self.ItemRevisionNum:str = obj["ItemRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCIDBuildSplitMergeSourcePartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Plant:str = obj["Plant"]
      self.PartNum:str = obj["PartNum"]
      self.PartDescription:str = obj["PartDescription"]
      self.BinNum:str = obj["BinNum"]
      self.BinDescription:str = obj["BinDescription"]
      self.LotNum:str = obj["LotNum"]
      self.LotTrackedPart:bool = obj["LotTrackedPart"]
      self.SerialTrackedPart:bool = obj["SerialTrackedPart"]
      self.OnHandQuantity:int = obj["OnHandQuantity"]
      self.SourceQuantity:int = obj["SourceQuantity"]
      self.AvailableQuantity:int = obj["AvailableQuantity"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.SourceUOM:str = obj["SourceUOM"]
      self.AvailableUOM:str = obj["AvailableUOM"]
      self.OnHandUOM:str = obj["OnHandUOM"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      self.PartTrackInventoryAttributes:bool = obj["PartTrackInventoryAttributes"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.PartTrackInventoryByRevision:bool = obj["PartTrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset:
   def __init__(self, obj):
      self.PCIDBuildSplitMergeSourcePart:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartRow] = obj["PCIDBuildSplitMergeSourcePart"]
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PCIDBuildSplitMergeSourceRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.PCID:str = obj["PCID"]
      self.PkgControlStatus:str = obj["PkgControlStatus"]
      self.PkgControlIDCode:str = obj["PkgControlIDCode"]
      self.PkgCode:str = obj["PkgCode"]
      self.WarehouseDescription:str = obj["WarehouseDescription"]
      self.PkgControlIDDesc:str = obj["PkgControlIDDesc"]
      self.PkgCodeDescription:str = obj["PkgCodeDescription"]
      self.PreviousPCID:str = obj["PreviousPCID"]
      self.Plant:str = obj["Plant"]
      self.PCIDContainsChildPCIDs:bool = obj["PCIDContainsChildPCIDs"]
      self.PCIDContainsChildParts:bool = obj["PCIDContainsChildParts"]
      self.BinNum:str = obj["BinNum"]
      self.BinDescription:str = obj["BinDescription"]
      self.BinNumEnabled:bool = obj["BinNumEnabled"]
      self.SerialNumberTracking:bool = obj["SerialNumberTracking"]
      """  Indicates if serial number tracking is available.  Is set to true when the warehouse plant does full serial tracking, or the warehouse plant does outbound serial tracking and the PCID is an outbound container.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PCIDBuildSplitMergeSourceTableset:
   def __init__(self, obj):
      self.PCIDBuildSplitMergeSource:list[Erp_Tablesets_PCIDBuildSplitMergeSourceRow] = obj["PCIDBuildSplitMergeSource"]
      self.PCIDBuildSplitMergeSourceItem:list[Erp_Tablesets_PCIDBuildSplitMergeSourceItemRow] = obj["PCIDBuildSplitMergeSourceItem"]
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

class GetDefaultWarehouse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warehouseCode:str = obj["parameters"]
      self.warehouseDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDestPCID_input:
   """ Required : 
   destPCID
   getPCIDContents
   destDS
   """  
   def __init__(self, obj):
      self.destPCID:str = obj["destPCID"]
      """  Destination PCID  """  
      self.getPCIDContents:bool = obj["getPCIDContents"]
      """  Get PCID Contents  """  
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

class GetDestPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

      """  output parameters  """  

class GetNewPCIDDestination_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["ds"]
      pass

class GetNewPCIDDestination_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPCIDPart_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["ds"]
      pass

class GetNewPCIDPart_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPCIDSource_input:
   """ Required : 
   ds
   clearWarehouse
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["ds"]
      self.clearWarehouse:bool = obj["clearWarehouse"]
      pass

class GetNewPCIDSource_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetSelectSerialNumbersParams_input:
   """ Required : 
   partNum
   attributeSetID
   quantity
   unitOfMeasure
   warehouseCode
   binNum
   lotNum
   pcid
   dataSource
   voidedOnly
   sysRowID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  The source part number  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The part's attribute set  """  
      self.quantity:int = obj["quantity"]
      """  The source quantity  """  
      self.unitOfMeasure:str = obj["unitOfMeasure"]
      """  The source unit of measure  """  
      self.warehouseCode:str = obj["warehouseCode"]
      """  The warehouse code  """  
      self.binNum:str = obj["binNum"]
      """  The source bin number  """  
      self.lotNum:str = obj["lotNum"]
      """  The source lot number  """  
      self.pcid:str = obj["pcid"]
      """  The source pcid number  """  
      self.dataSource:str = obj["dataSource"]
      """  Indicates the source of the data: SourcePart = from part, SourceItem = from source control item, DestItem = from destination control item  """  
      self.voidedOnly:bool = obj["voidedOnly"]
      """  Indicates if only voided serial numbers should be returned  """  
      self.sysRowID:str = obj["sysRowID"]
      """  The source SysRowID  """  
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

class GetSourcePCID_input:
   """ Required : 
   sourcePCID
   getPCIDContents
   sourceDS
   """  
   def __init__(self, obj):
      self.sourcePCID:str = obj["sourcePCID"]
      """  Source PCID  """  
      self.getPCIDContents:bool = obj["getPCIDContents"]
      """  Get PCID Contents  """  
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

class GetSourcePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
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

class MoveFromDestPCIDToSourcePCID_input:
   """ Required : 
   destDS
   sourceDS
   """  
   def __init__(self, obj):
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

class MoveFromDestPCIDToSourcePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      self.pcidNotMovedMessage:str = obj["parameters"]
      self.serialTrackPartsNotMovedMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class MoveFromSourcePCIDToDestPCIDAndRefresh_input:
   """ Required : 
   sourceDS
   destDS
   """  
   def __init__(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

class MoveFromSourcePCIDToDestPCIDAndRefresh_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      self.pcidNotMovedMessage:str = obj["parameters"]
      self.serialTrackPartsNotMovedMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class MoveFromSourcePCIDToDestPCID_input:
   """ Required : 
   sourceDS
   destDS
   fromHandHeld
   validateSNForOutbound
   """  
   def __init__(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      self.fromHandHeld:bool = obj["fromHandHeld"]
      """  Indicates if the method was called from handheld  """  
      self.validateSNForOutbound:bool = obj["validateSNForOutbound"]
      """  Indicates the validation for serial number selection should be validated when moving from a non-outbound container to an outbound container  """  
      pass

class MoveFromSourcePCIDToDestPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      self.pcidNotMovedMessage:str = obj["parameters"]
      self.serialTrackPartsNotMovedMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class NegativeInventoryTest_input:
   """ Required : 
   partNum
   warehouseCode
   binNum
   lotNum
   attributeSetID
   pcid
   dimCode
   dimConvFactor
   quantity
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.binNum:str = obj["binNum"]
      self.lotNum:str = obj["lotNum"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.pcid:str = obj["pcid"]
      self.dimCode:str = obj["dimCode"]
      self.dimConvFactor:int = obj["dimConvFactor"]
      self.quantity:int = obj["quantity"]
      pass

class NegativeInventoryTest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.negativeQuantityAction:str = obj["parameters"]
      self.message:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeDestBinNum_input:
   """ Required : 
   newDestBinNum
   destDS
   """  
   def __init__(self, obj):
      self.newDestBinNum:str = obj["newDestBinNum"]
      """  Dest BinNum  """  
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

class OnChangeDestBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

      """  output parameters  """  

class OnChangeDestPCID_input:
   """ Required : 
   newDestPCID
   getPCIDContents
   destDS
   """  
   def __init__(self, obj):
      self.newDestPCID:str = obj["newDestPCID"]
      """  Dest PCID  """  
      self.getPCIDContents:bool = obj["getPCIDContents"]
      """  Get PCID Contents  """  
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

class OnChangeDestPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

      """  output parameters  """  

class OnChangeItemLotNum_input:
   """ Required : 
   newItemLotNum
   sourceDS
   """  
   def __init__(self, obj):
      self.newItemLotNum:str = obj["newItemLotNum"]
      """  Item Lot Number  """  
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

class OnChangeItemLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

      """  output parameters  """  

class OnChangeItemPCID_input:
   """ Required : 
   newItemPCID
   sourceDS
   """  
   def __init__(self, obj):
      self.newItemPCID:str = obj["newItemPCID"]
      """  Item PCID  """  
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

class OnChangeItemPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

      """  output parameters  """  

class OnChangeItemPartNum_input:
   """ Required : 
   newItemPartNum
   sourceDS
   """  
   def __init__(self, obj):
      self.newItemPartNum:str = obj["newItemPartNum"]
      """  Item PartNum  """  
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

class OnChangeItemPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

      """  output parameters  """  

class OnChangeSourceAttributeSetID_input:
   """ Required : 
   newSourceAttributeSetID
   sourcePartDS
   """  
   def __init__(self, obj):
      self.newSourceAttributeSetID:int = obj["newSourceAttributeSetID"]
      """  Attribute Set  """  
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

class OnChangeSourceAttributeSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

      """  output parameters  """  

class OnChangeSourcePCIDHandheld_input:
   """ Required : 
   newSourcePCID
   getPCIDContents
   sourceDS
   """  
   def __init__(self, obj):
      self.newSourcePCID:str = obj["newSourcePCID"]
      """  Source PCID  """  
      self.getPCIDContents:bool = obj["getPCIDContents"]
      """  Get PCID Contents  """  
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

class OnChangeSourcePCIDHandheld_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

      """  output parameters  """  

class OnChangeSourcePCID_input:
   """ Required : 
   newSourcePCID
   getPCIDContents
   sourceDS
   """  
   def __init__(self, obj):
      self.newSourcePCID:str = obj["newSourcePCID"]
      """  Source PCID  """  
      self.getPCIDContents:bool = obj["getPCIDContents"]
      """  Get PCID Contents  """  
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

class OnChangeSourcePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

      """  output parameters  """  

class OnChangeSourcePartBinNum_input:
   """ Required : 
   newSourceBinNum
   sourcePartDS
   """  
   def __init__(self, obj):
      self.newSourceBinNum:str = obj["newSourceBinNum"]
      """  Bin Number  """  
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

class OnChangeSourcePartBinNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

      """  output parameters  """  

class OnChangeSourcePartLotNum_input:
   """ Required : 
   newSourceLotNum
   sourcePartDS
   """  
   def __init__(self, obj):
      self.newSourceLotNum:str = obj["newSourceLotNum"]
      """  Lot Number  """  
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

class OnChangeSourcePartLotNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

      """  output parameters  """  

class OnChangeSourcePartNum_input:
   """ Required : 
   newSourcePartNum
   newSourceWarehouseCode
   sourcePartDS
   """  
   def __init__(self, obj):
      self.newSourcePartNum:str = obj["newSourcePartNum"]
      """  Part Number  """  
      self.newSourceWarehouseCode:str = obj["newSourceWarehouseCode"]
      """  Warehouse Code can be specified if the Source PCID is empty and does not currently have a Warehouse assigned  """  
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

class OnChangeSourcePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

      """  output parameters  """  

class OnChangeSourcePartUOM_input:
   """ Required : 
   newSourceUOM
   sourcePartDS
   """  
   def __init__(self, obj):
      self.newSourceUOM:str = obj["newSourceUOM"]
      """  Unit of Measure  """  
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

class OnChangeSourcePartUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

      """  output parameters  """  

class OnChangeSourceQty_input:
   """ Required : 
   sourceQuantity
   sourcePartDS
   """  
   def __init__(self, obj):
      self.sourceQuantity:int = obj["sourceQuantity"]
      """  Source Quantity  """  
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

class OnChangeSourceQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

      """  output parameters  """  

class OnChangeSourceRevisionNum_input:
   """ Required : 
   newRevisionNum
   sourcePartDS
   """  
   def __init__(self, obj):
      self.newRevisionNum:str = obj["newRevisionNum"]
      """  Revision num  """  
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

class OnChangeSourceRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   sourcePartDS
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourcePartDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourcePartTableset] = obj["sourcePartDS"]
      pass

      """  output parameters  """  

class RemoveFromDestPCID_input:
   """ Required : 
   destDS
   sourceDS
   """  
   def __init__(self, obj):
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

class RemoveFromDestPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      pass

      """  output parameters  """  

class RemoveFromSourcePCID_input:
   """ Required : 
   sourceDS
   destDS
   """  
   def __init__(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

class RemoveFromSourcePCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sourceDS:list[Erp_Tablesets_PCIDBuildSplitMergeSourceTableset] = obj["sourceDS"]
      self.destDS:list[Erp_Tablesets_PCIDBuildSplitMergeDestTableset] = obj["destDS"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   partNum
   attributeSetID
   warehouseCode
   serialNumber
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part number to validate.  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  The part's attribute set  """  
      self.warehouseCode:str = obj["warehouseCode"]
      """  Warehouse to validate.  """  
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

