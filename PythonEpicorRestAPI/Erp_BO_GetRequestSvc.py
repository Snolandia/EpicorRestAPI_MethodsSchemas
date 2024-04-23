import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.GetRequestSvc
# Description: Material Get Request
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEmpInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEmpInfo
   Description: Call this method to create a new Epicor.Mfg.BO.GetRequestDataSet with Job#
   OperationID: GetNewEmpInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEmpInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEmpInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeAssembly(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeAssembly
   Description: Call this method to update the dataset when the GetRequest.AssemblySeq is changed
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCalcHours(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCalcHours
   Description: Call this method to update the dataset when the GetRequest.CalcHours is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeCalcHours
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCalcHours_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCalcHours_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCalcOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCalcOption
   Description: Call this method to update the dataset when the GetRequest.CalcOption is changed
Valid values are "O" - Outstanding, "P" - Pieces, "H" - hours
CalcHours only enabled for "H" and CalcPieces only enabled for "P"
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeCalcOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCalcOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCalcOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCalcPieces(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCalcPieces
   Description: Call this method to update the dataset when the GetRequest.CalcPieces is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeCalcPieces
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCalcPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCalcPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeJobNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeJobNum
   Description: Call this method to update the dataset when the GetRequest.JobNum is changed
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOpr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOpr
   Description: Call this method to update the dataset when the GetRequest.OprSeq is changed
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeOpr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOpr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOpr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRequestQtyUOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRequestQtyUOM
   Description: Call this method when the value of Epicor.Mfg.BO.GetRequestDataSet.RequestQtyUOM changes.
   OperationID: OnChangeRequestQtyUOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeRequestQtyUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRequestQtyUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeRequestQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeRequestQty
   Description: Call this method when the value of Epicor.Mfg.BO.GetRequestDataSet.RequestQty changes.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessLines(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessLines
   Description: Run this method when done updating all the detail lines (currently OK button in 6.1)
clear screen when done
Must set the GetRequest RowMod to "U" for this method to work
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.GetRequestSvc/$metadata", json=requestBody,headers=creds) as resp:
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

class Erp_Tablesets_GetRequestRow:
   def __init__(self, obj):
      self.JobNum:str = obj["JobNum"]
      self.JobPartNum:str = obj["JobPartNum"]
      self.JobPartDesc:str = obj["JobPartDesc"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.AsmPartNum:str = obj["AsmPartNum"]
      self.AsmPartDesc:str = obj["AsmPartDesc"]
      self.OprSeq:int = obj["OprSeq"]
      self.OpCode:str = obj["OpCode"]
      self.CalcOption:str = obj["CalcOption"]
      self.CalcPieces:int = obj["CalcPieces"]
      self.CalcHours:int = obj["CalcHours"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.NeedByTime:int = obj["NeedByTime"]
      self.RunQty:int = obj["RunQty"]
      self.EstProdHours:int = obj["EstProdHours"]
      self.QtyCompleted:int = obj["QtyCompleted"]
      self.CompletedHours:int = obj["CompletedHours"]
      self.QtyRemaining:int = obj["QtyRemaining"]
      self.RemaingHours:int = obj["RemaingHours"]
      self.OPDesc:str = obj["OPDesc"]
      self.EmpID:str = obj["EmpID"]
      self.EmpName:str = obj["EmpName"]
      self.DummyKeyField:str = obj["DummyKeyField"]
      """  Dumy unique key  """  
      self.CalcPiecesUOM:str = obj["CalcPiecesUOM"]
      self.RunQtyUOM:str = obj["RunQtyUOM"]
      self.QtyCompletedUOM:str = obj["QtyCompletedUOM"]
      self.QtyRemainingUOM:str = obj["QtyRemainingUOM"]
      self.Warning:str = obj["Warning"]
      self.AsmRevisionNum:str = obj["AsmRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.JobRevisionNum:str = obj["JobRevisionNum"]
      """  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GetRequestTableset:
   def __init__(self, obj):
      self.GetRequest:list[Erp_Tablesets_GetRequestRow] = obj["GetRequest"]
      self.RequestLines:list[Erp_Tablesets_RequestLinesRow] = obj["RequestLines"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

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

class GetNewEmpInfo_input:
   """ Required : 
   empID
   ds
   """  
   def __init__(self, obj):
      self.empID:str = obj["empID"]
      """  Employee ID  """  
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

class GetNewEmpInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

class OnChangeAssembly_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCalcHours_input:
   """ Required : 
   hours
   ds
   """  
   def __init__(self, obj):
      self.hours:int = obj["hours"]
      """  Hours  """  
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

class OnChangeCalcHours_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCalcOption_input:
   """ Required : 
   calcOption
   ds
   """  
   def __init__(self, obj):
      self.calcOption:str = obj["calcOption"]
      """  calcOption  """  
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

class OnChangeCalcOption_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCalcPieces_input:
   """ Required : 
   pieces
   ds
   """  
   def __init__(self, obj):
      self.pieces:int = obj["pieces"]
      """  Pieces  """  
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

class OnChangeCalcPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

class OnChangeJobNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOpr_input:
   """ Required : 
   oprSeq
   ds
   """  
   def __init__(self, obj):
      self.oprSeq:int = obj["oprSeq"]
      """  OprSeq  """  
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

class OnChangeOpr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRequestQtyUOM_input:
   """ Required : 
   pRequestQtyUOM
   seq
   ds
   """  
   def __init__(self, obj):
      self.pRequestQtyUOM:str = obj["pRequestQtyUOM"]
      """  RequestQtyUOM  """  
      self.seq:int = obj["seq"]
      """  seq  """  
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

class OnChangeRequestQtyUOM_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeRequestQty_input:
   """ Required : 
   pdRequestQty
   seq
   ds
   """  
   def __init__(self, obj):
      self.pdRequestQty:int = obj["pdRequestQty"]
      """  Request Qty  """  
      self.seq:int = obj["seq"]
      """  seq  """  
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

class OnChangeRequestQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangingNumberOfPieces_input:
   """ Required : 
   numberOfPieces
   seq
   ds
   """  
   def __init__(self, obj):
      self.numberOfPieces:int = obj["numberOfPieces"]
      self.seq:int = obj["seq"]
      """  seq  """  
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

class OnChangingNumberOfPieces_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessLines_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

class ProcessLines_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GetRequestTableset] = obj["ds"]
      pass

      """  output parameters  """  

