import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.OrderJobWizSvc
# Description: JWJobHead
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_getNextOpDtlSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getNextOpDtlSeq
   OperationID: getNextOpDtlSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getNextOpDtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getNextOpDtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CreateJobs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CreateJobs
   Description: This method creates job for selected orderdtls and/or orderrels.
This method will process any and all records where the ttJWJobOrderDtl.JobChkBox or
ttJWOrderRel.RelJobChkBox is set to true.
This method will also process the getDetails, Schedule and Release booleans.
   OperationID: CreateJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CreateJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMatrix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetMatrix
   Description: To retrieve the OrdJobWiz dataset for a given part number.
This dataset consists of the Order Detail lines that are of type 'make' and thier
related releases. The dataset also includes open jobs for any part in the detail,
The client my need to filter the job dataset to represent only the jobs relevant to the
part on the detail. Index constraints on the xsd, did not allow me to do that in the BL.
   OperationID: GetMatrix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetMatrix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMatrix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_Link(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Link
   Description: Creates link between selected release and selected job .
   OperationID: Link
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Link_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Link_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SelectAll(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SelectAll
   Description: This method processes the select all, getallmethod, sheduleall and releaseall fields
in the ttJWJobOrderDtl record. If any of the values in these fields change, this
method must be invoked in order for that change to be refelcted to the database.
Notes:
ttJWJobOrderDtl.Selectall = Set all values of Job checkbox to true for all lines in the Order Lines
Grid EXCEPT whre partID is an MRP part OR any release line for the detail
line linked to a job.
            
ttJWJobOrderDtl.DetailChkBox = Get All methods for all dtl lines, Selectall must be checked
ttJWJobOrderDtl.ScheduleAll  = Schedule all jobs, DetailChkBox must be checked
ttJWJobOrderDtl.ReleaseAll   = Release all jobs,  ScheduleAll  must be checked
   OperationID: SelectAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SelectAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnLink
   Description: Unlink releases to Jobs .
   OperationID: UnLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateJobs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateJobs
   Description: Gather all of the parts that are flagged to create jobs, and display the
ones in a message that won't be getting details.
   OperationID: ValidateJobs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateJobs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateJobs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPlantConfCtrlUse3rdPartySched(epicorHeaders = None):
   """  
   Summary: Invoke method GetPlantConfCtrlUse3rdPartySched
   Description: Get the Use3rdPartySched field from PlantConfCtrl table.
   OperationID: GetPlantConfCtrlUse3rdPartySched
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPlantConfCtrlUse3rdPartySched_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.OrderJobWizSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CreateJobs_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderJobWizTableset] = obj["ds"]
      pass

class CreateJobs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderJobWizTableset] = obj["ds"]
      self.pErrorMessages:str = obj["parameters"]
      pass

      """  output parameters  """  

class Erp_Tablesets_JWJobHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.JobNum:str = obj["JobNum"]
      self.ProdQty:int = obj["ProdQty"]
      self.ReqDueDate:str = obj["ReqDueDate"]
      self.StartDate:str = obj["StartDate"]
      self.DueDate:str = obj["DueDate"]
      self.JobReleased:bool = obj["JobReleased"]
      self.SchedLocked:bool = obj["SchedLocked"]
      self.JobSources:str = obj["JobSources"]
      self.PartNum:str = obj["PartNum"]
      self.SelectedLinkJob:bool = obj["SelectedLinkJob"]
      self.IUM:str = obj["IUM"]
      self.ContractID:str = obj["ContractID"]
      """  Saves the ContractID value from JobHead  """  
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JWJobOrderDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      self.IUM:str = obj["IUM"]
      self.LineDesc:str = obj["LineDesc"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderQty:int = obj["OrderQty"]
      self.PartNum:str = obj["PartNum"]
      self.RequestDate:str = obj["RequestDate"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.SellingQuantity:int = obj["SellingQuantity"]
      self.UnitPrice:int = obj["UnitPrice"]
      self.SellingFactor:int = obj["SellingFactor"]
      self.JobChkBox:bool = obj["JobChkBox"]
      self.DetailChkBox:bool = obj["DetailChkBox"]
      self.ReleaseChkBox:bool = obj["ReleaseChkBox"]
      self.ScheduleChkBox:bool = obj["ScheduleChkBox"]
      self.MrpPart:bool = obj["MrpPart"]
      self.NonStock:bool = obj["NonStock"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.TotOnHand:int = obj["TotOnHand"]
      self.TotReserved:int = obj["TotReserved"]
      self.TotAvail:int = obj["TotAvail"]
      self.InPartTable:bool = obj["InPartTable"]
      self.ApprovedPartRev:bool = obj["ApprovedPartRev"]
      self.HasLinkedReleases:bool = obj["HasLinkedReleases"]
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      self.ApprovedMethod:bool = obj["ApprovedMethod"]
      """  Tells if the PartRev reord for the part is approved  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  Holds the BasePartNum value from OrderDtl  """  
      self.DefaultAltMethod:str = obj["DefaultAltMethod"]
      """  Default Alternate Method for the current PartNum  """  
      self.IsConfig:bool = obj["IsConfig"]
      """  Holds a logical value that will tell if the OrderDtl line is configurable, this field is set in the buildTempTables procedure.  """  
      self.LinkedQuote:bool = obj["LinkedQuote"]
      """  Tells if there is a Quote Linked to this record  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code of the related record  """  
      self.TotDemand:int = obj["TotDemand"]
      self.LinkToContract:bool = obj["LinkToContract"]
      """  If the OrderDtl record is flagged as LinkToContract  """  
      self.ContractID:str = obj["ContractID"]
      """  Save the ContractID related to the Sales Order Detail.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for the part is tracked at the attribute level. This requires Advanced Unit of Measure license.  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.KBOriginalConfigProdID:int = obj["KBOriginalConfigProdID"]
      """  The unique identifier of the related original CPQ Configured Quote Product.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_JWOrderRelRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RelSelectChkBox:bool = obj["RelSelectChkBox"]
      self.RelDetailChkBox:bool = obj["RelDetailChkBox"]
      self.RelScheduleChkBox:bool = obj["RelScheduleChkBox"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.NeedByDate:str = obj["NeedByDate"]
      self.OurJobQty:int = obj["OurJobQty"]
      self.ReqDate:str = obj["ReqDate"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.JobNum:str = obj["JobNum"]
      self.Make:bool = obj["Make"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.TargetJobNum:str = obj["TargetJobNum"]
      self.TargetAssemblySeq:int = obj["TargetAssemblySeq"]
      self.TargetMtlSeq:int = obj["TargetMtlSeq"]
      self.SellingReqQty:int = obj["SellingReqQty"]
      self.QuoteNum:int = obj["QuoteNum"]
      self.QuoteLine:int = obj["QuoteLine"]
      self.OrderRelROWID:str = obj["OrderRelROWID"]
      self.RelJobChkBox:bool = obj["RelJobChkBox"]
      self.RelReleaseChkBox:bool = obj["RelReleaseChkBox"]
      self.UM:str = obj["UM"]
      self.JobsAvail:bool = obj["JobsAvail"]
      self.LineJobCheckBox:bool = obj["LineJobCheckBox"]
      self.InPartTable:bool = obj["InPartTable"]
      self.BasePartNum:str = obj["BasePartNum"]
      """  Base Part, comes from the OrderDtl.BasePartNum record  """  
      self.DefaultAltMethod:str = obj["DefaultAltMethod"]
      """  Default Alternate Method for the parent OrderDtl of this release  """  
      self.LineIsConfig:bool = obj["LineIsConfig"]
      """  Tells if the PartRev reord for the part is approved  """  
      self.LinkToContract:bool = obj["LinkToContract"]
      """  Saves the value if the Order Release is flagged as Link To Contract  """  
      self.ContractID:str = obj["ContractID"]
      """  Saves the value of the ContractID related to the Order Release  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PartNum:str = obj["PartNum"]
      """  Partnum from OrderDtl  """  
      self.KBConfigProdID:int = obj["KBConfigProdID"]
      """  The unique identifier of the related CPQ Configured Quote Product.  """  
      self.KBOriginalConfigProdID:int = obj["KBOriginalConfigProdID"]
      """  The unique identifier of the related original CPQ Configured Quote Product.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_OrderJobWizTableset:
   def __init__(self, obj):
      self.JWJobHead:list[Erp_Tablesets_JWJobHeadRow] = obj["JWJobHead"]
      self.JWJobOrderDtl:list[Erp_Tablesets_JWJobOrderDtlRow] = obj["JWJobOrderDtl"]
      self.JWOrderRel:list[Erp_Tablesets_JWOrderRelRow] = obj["JWOrderRel"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetMatrix_input:
   """ Required : 
   CurOrderNum
   CurOrderLine
   CurOrderRelNum
   """  
   def __init__(self, obj):
      self.CurOrderNum:int = obj["CurOrderNum"]
      """  OrderNum to be processed  """  
      self.CurOrderLine:int = obj["CurOrderLine"]
      """  Optional, Passing in when comming from Job Planner to valid Suggestion  """  
      self.CurOrderRelNum:int = obj["CurOrderRelNum"]
      """  Optional, Passing in when comming from Job Planner to valid Suggestion  """  
      pass

class GetMatrix_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderJobWizTableset] = obj["returnObj"]
      pass

class GetPlantConfCtrlUse3rdPartySched_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  bool: the value  """  
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

class Link_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderJobWizTableset] = obj["ds"]
      pass

class Link_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderJobWizTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SelectAll_input:
   """ Required : 
   curOrderNum
   insavedSelectAll
   insavedgetallmethods
   insavedScheduleAll
   insavedReleaseAll
   """  
   def __init__(self, obj):
      self.curOrderNum:int = obj["curOrderNum"]
      """  Order Number  """  
      self.insavedSelectAll:bool = obj["insavedSelectAll"]
      self.insavedgetallmethods:bool = obj["insavedgetallmethods"]
      """  Get All Methods  """  
      self.insavedScheduleAll:bool = obj["insavedScheduleAll"]
      """  Schedule All  """  
      self.insavedReleaseAll:bool = obj["insavedReleaseAll"]
      """  Release All  """  
      pass

class SelectAll_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_OrderJobWizTableset] = obj["returnObj"]
      pass

class UnLink_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderJobWizTableset] = obj["ds"]
      pass

class UnLink_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderJobWizTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateJobs_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_OrderJobWizTableset] = obj["ds"]
      pass

class ValidateJobs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_OrderJobWizTableset] = obj["ds"]
      self.WarnMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class getNextOpDtlSeq_input:
   """ Required : 
   ipCompany
   ipJobNum
   ipAssemblySeq
   ipOprSeq
   """  
   def __init__(self, obj):
      self.ipCompany:str = obj["ipCompany"]
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      self.ipOprSeq:int = obj["ipOprSeq"]
      pass

class getNextOpDtlSeq_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

