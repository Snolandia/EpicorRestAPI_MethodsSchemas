import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.TimePhasSvc
# Description: Time Phase Business Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_EnableDisableWhatIfAndTFSugTogs(epicorHeaders = None):
   """  
   Summary: Invoke method EnableDisableWhatIfAndTFSugTogs
   Description: SET Enable or Disable WhatIf And TFSugTogs
   OperationID: EnableDisableWhatIfAndTFSugTogs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnableDisableWhatIfAndTFSugTogs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetFrameTitle(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFrameTitle
   OperationID: GetFrameTitle
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFrameTitle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFrameTitle_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFrameTitleWithTime(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFrameTitleWithTime
   Description: Geting of FrameTitle by Plant. It called from Kinetic UI to get time portion separately
   OperationID: GetFrameTitleWithTime
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFrameTitleWithTime_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFrameTitleWithTime_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLastRunDateTimes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetLastRunDateTimes
   Description: Gets the last mrp run date and time and the last scheduled date
   OperationID: GetLastRunDateTimes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetLastRunDateTimes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLastRunDateTimes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetContractByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetContractByID
   Description: This method retrieve an active and approved planning contract
   OperationID: GetContractByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetContractByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContractByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GoProcessTimePhase(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GoProcessTimePhase
   Description: Creating the TimePhase by PartNum and Plant
   OperationID: GoProcessTimePhase
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GoProcessTimePhase_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GoProcessTimePhase_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPlanningAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPlanningAttributeSetID
   Description: Get the AttributeSetID of the Planning Attribute Set of any Attribute Set
by passing in its AttributeSetID.
   OperationID: GetPlanningAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPlanningAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlanningAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPart
   Description: Find part.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartFromRowID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartFromRowID
   Description: GetPartFromRowID.
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindPlanningAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindPlanningAttributeSet
   Description: Resolve Attribute ID passed into form
   OperationID: FindPlanningAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindPlanningAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPlanningAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_FindAttributeSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method FindAttributeSet
   Description: Find attribute short description and attributeSetDesc
   OperationID: FindAttributeSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/FindAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateAttributeSetIDFromRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateAttributeSetIDFromRevisionNum
   Description: This method updates attributeSetID and planningAttributeSetSeq when new revision is selected.
   OperationID: UpdateAttributeSetIDFromRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAttributeSetIDFromRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateRevisionNumFromAttributeSetID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateRevisionNumFromAttributeSetID
   Description: This method updates the revision number from an attributeSetID when new attributeSetID is selected.
   OperationID: UpdateRevisionNumFromAttributeSetID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateRevisionNumFromAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateRevisionNumFromAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartsAttributeClassHasRevisionAndIsMRPTracked(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartsAttributeClassHasRevisionAndIsMRPTracked
   Description: This method determines whether revision is Used in Planning.
   OperationID: PartsAttributeClassHasRevisionAndIsMRPTracked
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartsAttributeClassHasRevisionAndIsMRPTracked_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.TimePhasSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class EnableDisableWhatIfAndTFSugTogs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.EnableBoth:bool = obj["EnableBoth"]
      pass

      """  output parameters  """  

class Erp_Tablesets_PartPlanningAttributeRow:
   def __init__(self, obj):
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  AttributeSetDescription  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PlanningAttributeSet:str = obj["PlanningAttributeSet"]
      """  Description of the Planning Attribute Set  """  
      self.PlanningAttributeSetSeq:int = obj["PlanningAttributeSetSeq"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartPlanningAttributeTableset:
   def __init__(self, obj):
      self.PartPlanningAttribute:list[Erp_Tablesets_PartPlanningAttributeRow] = obj["PartPlanningAttribute"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_TimePhasRow:
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      self.SortByDate:bool = obj["SortByDate"]
      self.DueDate:str = obj["DueDate"]
      self.RequirementFlag:bool = obj["RequirementFlag"]
      self.ReceiptQty:int = obj["ReceiptQty"]
      self.RequiredQty:int = obj["RequiredQty"]
      self.JobNum:str = obj["JobNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.LeadTime:int = obj["LeadTime"]
      self.BalanceQty:int = obj["BalanceQty"]
      self.ExceptionReason:str = obj["ExceptionReason"]
      self.SugOrderDate:str = obj["SugOrderDate"]
      self.SourceName:str = obj["SourceName"]
      self.PartDescription:str = obj["PartDescription"]
      self.IUM:str = obj["IUM"]
      self.BuyForJob:bool = obj["BuyForJob"]
      self.PrintMe:bool = obj["PrintMe"]
      self.SourceFile:str = obj["SourceFile"]
      self.Plant:str = obj["Plant"]
      self.JobStatus:str = obj["JobStatus"]
      self.Suggestions:bool = obj["Suggestions"]
      self.TOSuggestions:bool = obj["TOSuggestions"]
      self.TFOrder:str = obj["TFOrder"]
      self.ContainerID:int = obj["ContainerID"]
      """  Container ID the PO release is tied to.  This is used for display purposes only.  """  
      self.PromiseDate:str = obj["PromiseDate"]
      """  Promise Date for the Part Release given by the PO Vendor  """  
      self.ContractID:str = obj["ContractID"]
      self.LinkToContract:bool = obj["LinkToContract"]
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision Number associated with part.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TimePhasTableset:
   def __init__(self, obj):
      self.TimePhas:list[Erp_Tablesets_TimePhasRow] = obj["TimePhas"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class FindAttributeSet_input:
   """ Required : 
   attributeSetID
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class FindAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.attributeSetShortDesc:str = obj["parameters"]
      self.attributeSetDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class FindPart_input:
   """ Required : 
   ipPartNum
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  PartNum  """  
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

class FindPlanningAttributeSet_input:
   """ Required : 
   partNum
   attributeSetID
   trackInventoryAttributes
   hasMRPPlanningAttribute
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.attributeSetID:int = obj["attributeSetID"]
      self.trackInventoryAttributes:bool = obj["trackInventoryAttributes"]
      self.hasMRPPlanningAttribute:bool = obj["hasMRPPlanningAttribute"]
      pass

class FindPlanningAttributeSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.attributeSetShortDesc:str = obj["parameters"]
      self.attributeSetDesc:str = obj["parameters"]
      self.newAttributeSetID:int = obj["parameters"]
      pass

      """  output parameters  """  

class GetContractByID_input:
   """ Required : 
   contractID
   """  
   def __init__(self, obj):
      self.contractID:str = obj["contractID"]
      """  ContractID changed  """  
      pass

class GetContractByID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.description:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFrameTitleWithTime_input:
   """ Required : 
   inPlant
   inPart
   """  
   def __init__(self, obj):
      self.inPlant:str = obj["inPlant"]
      """  The Plant  """  
      self.inPart:str = obj["inPart"]
      """  The Partt  """  
      pass

class GetFrameTitleWithTime_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.mRPLastRun:str = obj["parameters"]
      self.mRPLastScheduled:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetFrameTitle_input:
   """ Required : 
   inPlant
   inPart
   """  
   def __init__(self, obj):
      self.inPlant:str = obj["inPlant"]
      self.inPart:str = obj["inPart"]
      pass

class GetFrameTitle_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.frameTitle:str = obj["parameters"]
      self.mRPLastRunDate:str = obj["parameters"]
      self.FrameLastSchedTitle:str = obj["parameters"]
      self.mRPLastScheduledDate:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetLastRunDateTimes_input:
   """ Required : 
   inPlant
   inPart
   """  
   def __init__(self, obj):
      self.inPlant:str = obj["inPlant"]
      """  The Plant  """  
      self.inPart:str = obj["inPart"]
      """  The Part  """  
      pass

class GetLastRunDateTimes_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.mrpLastRun:str = obj["parameters"]
      self.mrpLastRunTime:str = obj["parameters"]
      self.mrpLastScheduled:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPartFromRowID_input:
   """ Required : 
   ipRowType
   ipRowID
   """  
   def __init__(self, obj):
      self.ipRowType:str = obj["ipRowType"]
      """  Row Type  """  
      self.ipRowID:str = obj["ipRowID"]
      """  Row ID  """  
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
   plantID
   SysRowID
   rowType
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Proposed PartNumber change  """  
      self.plantID:str = obj["plantID"]
      """  Plant ID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class GetPartXRefInfo_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartPlanningAttributeTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.partNum:str = obj["parameters"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      self.partFound:bool = obj["partFound"]
      self.partDesc:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetPlanningAttributeSetID_input:
   """ Required : 
   attributeSetID
   """  
   def __init__(self, obj):
      self.attributeSetID:int = obj["attributeSetID"]
      pass

class GetPlanningAttributeSetID_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

class GoProcessTimePhase_input:
   """ Required : 
   partNum
   attributeSetID
   plant
   whatIfTog
   tFSug
   plnCtInfo
   contractID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  Part Number  """  
      self.attributeSetID:int = obj["attributeSetID"]
      self.plant:str = obj["plant"]
      """  Plant  """  
      self.whatIfTog:bool = obj["whatIfTog"]
      """  Suggestions  """  
      self.tFSug:bool = obj["tFSug"]
      """  Transfer Order Suggestions  """  
      self.plnCtInfo:bool = obj["plnCtInfo"]
      """  Planning Contract Info  """  
      self.contractID:str = obj["contractID"]
      """  ContractID  """  
      pass

class GoProcessTimePhase_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_TimePhasTableset] = obj["returnObj"]
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

class PartsAttributeClassHasRevisionAndIsMRPTracked_input:
   """ Required : 
   attrClassID
   """  
   def __init__(self, obj):
      self.attrClassID:str = obj["attrClassID"]
      """  current Attribute Class ID  """  
      pass

class PartsAttributeClassHasRevisionAndIsMRPTracked_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UpdateAttributeSetIDFromRevisionNum_input:
   """ Required : 
   partNum
   revisionNum
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  current part number  """  
      self.revisionNum:str = obj["revisionNum"]
      """  new revision selected  """  
      pass

class UpdateAttributeSetIDFromRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.attributeSetID:int = obj["parameters"]
      pass

      """  output parameters  """  

class UpdateRevisionNumFromAttributeSetID_input:
   """ Required : 
   partNum
   attributeSetID
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      """  current part number  """  
      self.attributeSetID:int = obj["attributeSetID"]
      """  new AttributeSetID selected  """  
      pass

class UpdateRevisionNumFromAttributeSetID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.revisionNum:str = obj["parameters"]
      pass

      """  output parameters  """  

