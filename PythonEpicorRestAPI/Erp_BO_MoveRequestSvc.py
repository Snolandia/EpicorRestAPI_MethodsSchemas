import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MoveRequestSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CheckEmployee(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckEmployee
   Description: This method needs to be called from the main menu only.  if the object
is being called from the shop floor menu then the employee id has already been determined
and validated and is passed in
   OperationID: CheckEmployee
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckEmployee_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEmployee_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMoveRequest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMoveRequest
   Description: Call this method to create a new Epicor.Mfg.BO.MoveRequestDataSet with the RequestType
   OperationID: GetNewMoveRequest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMoveRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMoveRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAssembly
   Description: Call this method when the AssemblySeq field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeAssembly
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromBin
   Description: Call this method when the FromBin field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeFromBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromWhse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromWhse
   Description: Call this method when the FromWhse field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeFromWhse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFromWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobNum
   Description: Call this method when the JobNum field changes
RowMod must be "A" or "U" for this method to work
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeLot(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeLot
   Description: Call this method when the lotNum field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeLot
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMtlSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMtlSeq
   Description: Call this method when the MtlSeq field changes
if RequestType = "MW":U then MtlSeq is actually the JobOper.OprSeq
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeMtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Call this method when the PartNum field changes
RowMod must be "A" or "U" for this method to work
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromPCID
   Description: Validates that PCID exists
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeToPCID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeToPCID
   Description: Validates that PCID exists
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetWarehouses(epicorHeaders = None):
   """  
   Summary: Invoke method GetWarehouses
   Description: Returns a list of warehouses
   OperationID: GetWarehouses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarehouses_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetPartWarehouses(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartWarehouses
   Description: Returns a list of warehouses that are valid for a part
   OperationID: GetPartWarehouses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartWarehouses_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartWarehouses_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeReqDirection(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeReqDirection
   Description: Call this method when the ReqDirection field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeReqDirection
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeReqDirection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReqDirection_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeToBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeToBin
   Description: Call this method when the ToBin field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeToBin
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeToWhse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeToWhse
   Description: Call this method when the ToWhse field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeToWhse
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeToWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRequestQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRequestQty
   Description: Call this method when the value of Epicor.Mfg.BO.MoveRequestDataSet.RequestQty changes.
   OperationID: OnChangeRequestQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRequestQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRequestQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeUOM
   Description: Call this method when the value of Epicor.Mfg.BO.MoveRequestDataSet.UOM changes.
   OperationID: OnChangeUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessRequest(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessRequest
   Description: Must set the MoveRequest RowMod to "U" or "A" for this method to work
The method updates the Mtl Queue record when the user is done inputing data
   OperationID: ProcessRequest
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDetailPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDetailPartNum
   OperationID: ChangeDetailPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDetailPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VerifyEmpID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VerifyEmpID
   Description: Verify Employee ID and return name if valid.
   OperationID: VerifyEmpID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VerifyEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class ChangeDetailPartNum_input:
   """ Required : 
   NewPartNum
   SysRowID
   rowType
   ds
   """  
   def __init__(self, obj):
      self.NewPartNum:str = obj["NewPartNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.rowType:str = obj["rowType"]
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class ChangeDetailPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.NewPartNum:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckEmployee_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Employee ID  """  
      pass

class CheckEmployee_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.empName:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_MoveRequestRow:
   def __init__(self, obj):
      self.RequestType:str = obj["RequestType"]
      self.ReqDirection:str = obj["ReqDirection"]
      self.RequestQty:int = obj["RequestQty"]
      self.JobNum:str = obj["JobNum"]
      self.JobPartNum:str = obj["JobPartNum"]
      self.JobPartDesc:str = obj["JobPartDesc"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.AsmPartNum:str = obj["AsmPartNum"]
      self.AsmPartDesc:str = obj["AsmPartDesc"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      self.MtlPartDesc:str = obj["MtlPartDesc"]
      self.PartNum:str = obj["PartNum"]
      self.PartDesc:str = obj["PartDesc"]
      self.LotNumber:str = obj["LotNumber"]
      self.FromWhse:str = obj["FromWhse"]
      self.FromWhseDesc:str = obj["FromWhseDesc"]
      self.FromBin:str = obj["FromBin"]
      self.FromBinDesc:str = obj["FromBinDesc"]
      self.ToWhse:str = obj["ToWhse"]
      self.ToWhseDesc:str = obj["ToWhseDesc"]
      self.ToBin:str = obj["ToBin"]
      self.ToBinDesc:str = obj["ToBinDesc"]
      self.DummyKeyField:str = obj["DummyKeyField"]
      self.EmpId:str = obj["EmpId"]
      self.EmpName:str = obj["EmpName"]
      self.ToMultiBin:bool = obj["ToMultiBin"]
      """  If yes, ToBin should be enabled, otherwise diable tobin  """  
      self.FromMultiBin:bool = obj["FromMultiBin"]
      """  if true then enable FromBin otherwise disable from bin  """  
      self.TrackLot:bool = obj["TrackLot"]
      self.LotDesc:str = obj["LotDesc"]
      self.UOM:str = obj["UOM"]
      """  Unit of measure for the Part (JobPartNum) being moved  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSADelete:bool = obj["FSADelete"]
      """  Used by EpicorFSA. Set to true to delete related MtlQueue.  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  The optional NeedByDate the generated MtlQueue should use.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AsmAttributeSetID:int = obj["AsmAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.MtlAttributeSetID:int = obj["MtlAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.MtlAttributeSetDescription:str = obj["MtlAttributeSetDescription"]
      """  The Full Description of the Material Attribute Set.  """  
      self.MtlAttributeSetShortDescription:str = obj["MtlAttributeSetShortDescription"]
      """  The Short Description of the Material Attribute Set.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Inventory Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Inventory Attribute Set.  """  
      self.Plant:str = obj["Plant"]
      self.ToPCID:str = obj["ToPCID"]
      self.FromPCID:str = obj["FromPCID"]
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.MtlRevisionNum:str = obj["MtlRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.PlantConfCtrlEnablePackageControl:bool = obj["PlantConfCtrlEnablePackageControl"]
      self.AsmRevisionNum:str = obj["AsmRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MoveRequestTableset:
   def __init__(self, obj):
      self.MoveRequest:list[Erp_Tablesets_MoveRequestRow] = obj["MoveRequest"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetNewMoveRequest_input:
   """ Required : 
   requestType
   ds
   """  
   def __init__(self, obj):
      self.requestType:str = obj["requestType"]
      """  Request Type  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class GetNewMoveRequest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPartWarehouses_input:
   """ Required : 
   partNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      pass

class GetPartWarehouses_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetWarehouses_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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

class OnChangeAssembly_input:
   """ Required : 
   asmSeq
   ds
   """  
   def __init__(self, obj):
      self.asmSeq:int = obj["asmSeq"]
      """  Assembly Sequence  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeAssembly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFromBin_input:
   """ Required : 
   fromBin
   ds
   """  
   def __init__(self, obj):
      self.fromBin:str = obj["fromBin"]
      """  From Bin Number  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeFromBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFromPCID_input:
   """ Required : 
   pcid
   pCallProcess
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      self.pCallProcess:str = obj["pCallProcess"]
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeFromPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      self.warehousesList:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeFromWhse_input:
   """ Required : 
   fromWhse
   ds
   """  
   def __init__(self, obj):
      self.fromWhse:str = obj["fromWhse"]
      """  From Warehouse  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeFromWhse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobNum_input:
   """ Required : 
   jobNum
   ds
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  Job Number  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeLot_input:
   """ Required : 
   lotNum
   ds
   """  
   def __init__(self, obj):
      self.lotNum:str = obj["lotNum"]
      """  Lot Number  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeLot_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMtlSeq_input:
   """ Required : 
   mtlSeq
   ds
   """  
   def __init__(self, obj):
      self.mtlSeq:int = obj["mtlSeq"]
      """  Material Sequence  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeMtlSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   partNum
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      self.warehousesList:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeReqDirection_input:
   """ Required : 
   reqDirection
   ds
   """  
   def __init__(self, obj):
      self.reqDirection:str = obj["reqDirection"]
      """  Request Direction  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeReqDirection_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRequestQty_input:
   """ Required : 
   pdRequestQty
   ds
   """  
   def __init__(self, obj):
      self.pdRequestQty:int = obj["pdRequestQty"]
      """  Request Qty  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeRequestQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeToBin_input:
   """ Required : 
   toBin
   ds
   """  
   def __init__(self, obj):
      self.toBin:str = obj["toBin"]
      """  To Bin Number  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeToBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeToPCID_input:
   """ Required : 
   pcid
   pCallProcess
   ds
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      self.pCallProcess:str = obj["pCallProcess"]
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeToPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      self.warehousesList:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangeToWhse_input:
   """ Required : 
   toWhse
   ds
   """  
   def __init__(self, obj):
      self.toWhse:str = obj["toWhse"]
      """  To Warehouse  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeToWhse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeUOM_input:
   """ Required : 
   pUOM
   ds
   """  
   def __init__(self, obj):
      self.pUOM:str = obj["pUOM"]
      """  UOM  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangeUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingAttributeSet_input:
   """ Required : 
   attributeSetID
   ds
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      """  attributeSetID  """  
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessRequest_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

class ProcessRequest_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MoveRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VerifyEmpID_input:
   """ Required : 
   empID
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      pass

class VerifyEmpID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.empName:str = obj["parameters"]
      pass

      """  output parameters  """  

