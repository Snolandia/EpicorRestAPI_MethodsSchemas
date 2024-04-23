import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ReturnRequestSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewAssyMtlInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewAssyMtlInfo
   Description: Call this method to create a new Epicor.Mfg.BO.ReturnRequestDataSet with Job#
   OperationID: GetNewAssyMtlInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewAssyMtlInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAssyMtlInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewMiscInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewMiscInfo
   Description: Call this method to create a new Epicor.Mfg.BO.ReturnRequestDataSet with Part#
   OperationID: GetNewMiscInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewMiscInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMiscInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewSalvageInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewSalvageInfo
   Description: Call this method to create a new Epicor.Mfg.BO.ReturnRequestDataSet with Job#
   OperationID: GetNewSalvageInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewSalvageInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSalvageInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAssembly
   Description: Call this method to update the dataset when the ReturnRequest.AssemblySeq is changed
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromBin
   Description: Call this method to update the dataset when the RequestLines.FromBinNum is changed
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFromWhse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFromWhse
   Description: Call this method to update the dataset when the RequestLines.FromWhse is changed
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeIUM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeIUM
   Description: Call this method when the value of Epicor.Mfg.BO.ReturnRequest.IUM changes.
   OperationID: OnChangeIUM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeIUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeIUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobNum
   Description: Call this method to update the dataset when the ReturnRequest.JobNum is changed
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeMtlSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeMtlSeq
   Description: Call this method to update the dataset when the ReturnRequest.MtlSeq is changed
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartNum
   Description: Call this method to update the dataset when the ReturnRequest.PartNum is changed
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRequestQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRequestQty
   Description: Call this method when the value of Epicor.Mfg.BO.ReturnRequest.RequestQty changes.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeToBin(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeToBin
   Description: Call this method to update the dataset when the RequestLines.ToBinNum is changed
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeToWhse(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeToWhse
   Description: Call this method to update the dataset when the RequestLines.ToWhse is changed
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessLines
   Description: Run this method when done updating all the detail lines (currently OK button in 6.1)
clear screen when done
Must set the ReturnRequest RowMod to "U" for this method to work
   OperationID: ProcessLines
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessLines_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessLines_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Returns code description as string
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ReturnRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
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

class Erp_Tablesets_RequestLinesRow:
   def __init__(self, obj):
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.JobSeq:int = obj["JobSeq"]
      self.JobSeqType:str = obj["JobSeqType"]
      self.PartNum:str = obj["PartNum"]
      self.Description:str = obj["Description"]
      self.RequiredQty:int = obj["RequiredQty"]
      self.QtyIssued:int = obj["QtyIssued"]
      self.QtyStaged:int = obj["QtyStaged"]
      self.IUM:str = obj["IUM"]
      """  Unit of Measure used for the transaction  """  
      self.TranType:str = obj["TranType"]
      self.MtlQueueQty:int = obj["MtlQueueQty"]
      self.RequestQty:int = obj["RequestQty"]
      self.NextJobSeq:int = obj["NextJobSeq"]
      self.FromBinNum:str = obj["FromBinNum"]
      self.FromWhse:str = obj["FromWhse"]
      self.ToBinNum:str = obj["ToBinNum"]
      self.ToWhse:str = obj["ToWhse"]
      self.DummyKeyField:str = obj["DummyKeyField"]
      self.DummyLineField:str = obj["DummyLineField"]
      self.FromWhseDesc:str = obj["FromWhseDesc"]
      self.FromBinDesc:str = obj["FromBinDesc"]
      self.ToWhseDesc:str = obj["ToWhseDesc"]
      self.ToBinDesc:str = obj["ToBinDesc"]
      self.IssuedUM:str = obj["IssuedUM"]
      """  UOM for the Quantity Issued  """  
      self.ThisTranQty:int = obj["ThisTranQty"]
      """  The quantity value converted from Request UOM to Issued UOM.  """  
      self.RequiredQtyUOM:str = obj["RequiredQtyUOM"]
      self.RequestQtyUOM:str = obj["RequestQtyUOM"]
      self.QtyStagedUOM:str = obj["QtyStagedUOM"]
      self.MtlQueueQtyUOM:str = obj["MtlQueueQtyUOM"]
      """  Requested UOM  """  
      self.QtyIssuedUOM:str = obj["QtyIssuedUOM"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.Plant:str = obj["Plant"]
      """  Site Identifier  """  
      self.FromPCID:str = obj["FromPCID"]
      self.ToPCID:str = obj["ToPCID"]
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReturnRequestRow:
   def __init__(self, obj):
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
      self.ReturnType:str = obj["ReturnType"]
      self.DummyKeyField:str = obj["DummyKeyField"]
      """  Dummy Unique Key  """  
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.AttrClassID:str = obj["AttrClassID"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.Plant:str = obj["Plant"]
      self.PlantConfCtrlEnablePackageControl:bool = obj["PlantConfCtrlEnablePackageControl"]
      self.MtlRevisionNum:str = obj["MtlRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  Indicates if inventory for this part is tracked by revision number.  """  
      self.AsmRevisionNum:str = obj["AsmRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ReturnRequestTableset:
   def __init__(self, obj):
      self.ReturnRequest:list[Erp_Tablesets_ReturnRequestRow] = obj["ReturnRequest"]
      self.RequestLines:list[Erp_Tablesets_RequestLinesRow] = obj["RequestLines"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  table name  """  
      self.fieldName:str = obj["fieldName"]
      """  field name  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetNewAssyMtlInfo_input:
   """ Required : 
   jobNum
   ds
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  Job Number  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class GetNewAssyMtlInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewMiscInfo_input:
   """ Required : 
   partNum
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class GetNewMiscInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewSalvageInfo_input:
   """ Required : 
   jobNum
   ds
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  Job Number  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class GetNewSalvageInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
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

class OnChangeAssembly_input:
   """ Required : 
   assemblySeq
   ds
   """  
   def __init__(self, obj):
      self.assemblySeq:int = obj["assemblySeq"]
      """  AssemblySeq  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangeAssembly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFromBin_input:
   """ Required : 
   binNum
   cRowIdent
   ds
   """  
   def __init__(self, obj):
      self.binNum:str = obj["binNum"]
      """  BinNum  """  
      self.cRowIdent:str = obj["cRowIdent"]
      """  RequestLines RowIDent  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangeFromBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFromPCID_input:
   """ Required : 
   pcid
   ds
   pCallProcess
   """  
   def __init__(self, obj):
      self.pcid:str = obj["pcid"]
      """  Proposed PCID value  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      self.pCallProcess:str = obj["pCallProcess"]
      """  Calling Process value  """  
      pass

class OnChangeFromPCID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFromWhse_input:
   """ Required : 
   whseCode
   cRowIdent
   ds
   """  
   def __init__(self, obj):
      self.whseCode:str = obj["whseCode"]
      """  From Warehose  """  
      self.cRowIdent:str = obj["cRowIdent"]
      """  RequestLines RowIDent  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangeFromWhse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeIUM_input:
   """ Required : 
   pUM
   ds
   """  
   def __init__(self, obj):
      self.pUM:str = obj["pUM"]
      """  Transaction UOM  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangeIUM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeJobNum_input:
   """ Required : 
   jobNum
   ds
   """  
   def __init__(self, obj):
      self.jobNum:str = obj["jobNum"]
      """  JobNum  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeMtlSeq_input:
   """ Required : 
   mtlSeq
   ds
   """  
   def __init__(self, obj):
      self.mtlSeq:int = obj["mtlSeq"]
      """  MtlSeq  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangeMtlSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartNum_input:
   """ Required : 
   partNum
   ds
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  PartNum  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangePartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRequestQty_input:
   """ Required : 
   requestQty
   cRowIdent
   ds
   """  
   def __init__(self, obj):
      self.requestQty:int = obj["requestQty"]
      """  Request Quantity  """  
      self.cRowIdent:str = obj["cRowIdent"]
      """  SysRowID  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangeRequestQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeToBin_input:
   """ Required : 
   binNum
   cRowIdent
   ds
   """  
   def __init__(self, obj):
      self.binNum:str = obj["binNum"]
      """  BinNum  """  
      self.cRowIdent:str = obj["cRowIdent"]
      """  RequestLines RowIDent  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangeToBin_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeToWhse_input:
   """ Required : 
   whseCode
   cRowIdent
   ds
   """  
   def __init__(self, obj):
      self.whseCode:str = obj["whseCode"]
      """  To Warehose  """  
      self.cRowIdent:str = obj["cRowIdent"]
      """  RequestLines RowIDent  """  
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangeToWhse_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangingAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingRevisionNum_input:
   """ Required : 
   revisionNum
   ds
   """  
   def __init__(self, obj):
      self.revisionNum:str = obj["revisionNum"]
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class OnChangingRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessLines_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

class ProcessLines_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_ReturnRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

