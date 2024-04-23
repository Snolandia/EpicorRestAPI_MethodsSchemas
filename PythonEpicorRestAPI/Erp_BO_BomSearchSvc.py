import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.BomSearchSvc
# Description: bo/BomSearch/BomSearch.p
           To return records from the bom option for drag/drop inside
           Job Entry, QuoteAsm Entry, and Engineering Work Bench and any
           other places that may need to search this data.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_CreatePartMtlRefDes(epicorHeaders = None):
   """  
   Summary: Invoke method CreatePartMtlRefDes
   Description: Create Part Material Reference
   OperationID: CreatePartMtlRefDes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreatePartMtlRefDes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetAllAlternateTrees(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAllAlternateTrees
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartOpDtl, PartMtl,
PartMtlRestriction, PartMtlRestrictSubst, PartMtlRefDes, PartOprRestriction and PartOprRestrictSubst if those
records exist for the appropriate input parameters.
ALL ALTERNATES OF THE PARTREVISION WILL BE RETURNED if ipcomplete is true
This method will also allow you to return the whole dataset or allow the user to specify how
far down the tree they would like to return possible "part" records for.
   OperationID: GetAllAlternateTrees
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAllAlternateTrees_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAllAlternateTrees_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDatasetForTree(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDatasetForTree
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartOpDtl, PartMtl,
PartMtlRestriction, PartMtlRestrictSubst, PartOprRestriction and PartOprRestrictSubst if those
records exist for the appropriate input parameters.
This method will also allow you to return the whole dataset or allow the user to specify how
the revision to return possible "part" records for.
   OperationID: GetDatasetForTree
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDatasetForTreeByProcessMfgID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDatasetForTreeByProcessMfgID
   Description: This methods will return a dataset that will include PartRev, PartOpr, PartOpDtl, PartMtl,
PartMtlRestriction, PartMtlRestrictSubst, PartOprRestriction and PartOprRestrictSubst if those
records exist for the appropriate input parameters.
This method will also allow you to return the whole dataset or allow the user to specify how
the revision to return possible "part" records for.
   OperationID: GetDatasetForTreeByProcessMfgID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTreeByProcessMfgID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTreeByProcessMfgID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDatasetForTreeWithPartValidation(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDatasetForTreeWithPartValidation
   Description: Validates Part, finds default revision based on asOfDate and invokes GetDatasetForTree.
   OperationID: GetDatasetForTreeWithPartValidation
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDatasetForTreeWithPartValidation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDatasetForTreeWithPartValidation_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PartRevExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PartRevExists
   Description: Part Revision Exists
   OperationID: PartRevExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PartRevExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PartRevExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartNumSource(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartNumSource
   Description: Gets PartNum of the source record
   OperationID: GetPartNumSource
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartNumSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartNumSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.BomSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class CreatePartMtlRefDes_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_BomSearchTableset:
   def __init__(self, obj):
      self.PartRev:list[Erp_Tablesets_PartRevRow] = obj["PartRev"]
      self.PartRevAttch:list[Erp_Tablesets_PartRevAttchRow] = obj["PartRevAttch"]
      self.PartMtl:list[Erp_Tablesets_PartMtlRow] = obj["PartMtl"]
      self.PartMtlAttch:list[Erp_Tablesets_PartMtlAttchRow] = obj["PartMtlAttch"]
      self.PartMtlInsp:list[Erp_Tablesets_PartMtlInspRow] = obj["PartMtlInsp"]
      self.PartMtlRestriction:list[Erp_Tablesets_PartMtlRestrictionRow] = obj["PartMtlRestriction"]
      self.PartMtlRestrictSubst:list[Erp_Tablesets_PartMtlRestrictSubstRow] = obj["PartMtlRestrictSubst"]
      self.PartOpr:list[Erp_Tablesets_PartOprRow] = obj["PartOpr"]
      self.PartOprAttch:list[Erp_Tablesets_PartOprAttchRow] = obj["PartOprAttch"]
      self.PartOpDtl:list[Erp_Tablesets_PartOpDtlRow] = obj["PartOpDtl"]
      self.PartOprInsp:list[Erp_Tablesets_PartOprInspRow] = obj["PartOprInsp"]
      self.PartOprRestriction:list[Erp_Tablesets_PartOprRestrictionRow] = obj["PartOprRestriction"]
      self.PartOprRestrictSubst:list[Erp_Tablesets_PartOprRestrictSubstRow] = obj["PartOprRestrictSubst"]
      self.PartOprAction:list[Erp_Tablesets_PartOprActionRow] = obj["PartOprAction"]
      self.PartOprActionParam:list[Erp_Tablesets_PartOprActionParamRow] = obj["PartOprActionParam"]
      self.PartOprMachParam:list[Erp_Tablesets_PartOprMachParamRow] = obj["PartOprMachParam"]
      self.PartCOPart:list[Erp_Tablesets_PartCOPartRow] = obj["PartCOPart"]
      self.PartMtlRefDes:list[Erp_Tablesets_PartMtlRefDesRow] = obj["PartMtlRefDes"]
      self.PartStage:list[Erp_Tablesets_PartStageRow] = obj["PartStage"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartCOPartRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as part of the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.CoPartNum:str = obj["CoPartNum"]
      """  Companion PartNum identifies the Part that is manufactured along with the main part (ex: Right and Left parts)  """  
      self.CoRevisionNum:str = obj["CoRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the companion part, and is used as part of the primary key  """  
      self.PartsPerOp:int = obj["PartsPerOp"]
      """   Part Per Operation. Active only for Concurrent process
Jobs. Otherwise set to 1.  """  
      self.LbrCostBase:int = obj["LbrCostBase"]
      """   Defines an integer value which is used to calculate a
ratio for prorating the labor costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  """  
      self.MtlCostBase:int = obj["MtlCostBase"]
      """   Defines an integer value which is used to calculate a
ratio for prorating the material costs to the end part. For example a job produces parts A and B, and you want part B to have cost 2 times that of the cost of Part A.  Part A CostBase would be 1 and B would be 2.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.IUM:str = obj["IUM"]
      """  Defines the Unit of Measure used when part is issued, this is also how it is stocked.  Use the value from XaSyst.UM as a default when creating new part records.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.PreventSugg:bool = obj["PreventSugg"]
      """  If true, MRP will not generate change suggestions for the co-part  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimaryCost:bool = obj["PrimaryCost"]
      """  Indicates if the parent Part should be used as the primary costing method for the co-part  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.EnablePreventSugg:bool = obj["EnablePreventSugg"]
      self.PartMasterPart:bool = obj["PartMasterPart"]
      self.ProcessMode:str = obj["ProcessMode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartMtlAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      self.MtlSeq:int = obj["MtlSeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartMtlInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Parent Part number to which this material item is a component of  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number of the part that this material item is a component of.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Job/Lot/Assembly. This is system assigned. The next available # is determined by reading last JobMtl record on the Job/Lot/Assembly and then adding one to it.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the PartMtlInsp record within the Part material  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartMtlRefDesRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.RefDes:str = obj["RefDes"]
      """  Identifier of Reference Designator  """  
      self.RefDesSeq:int = obj["RefDesSeq"]
      """  Unique identifies the reference designator with the material sequence.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.Side:str = obj["Side"]
      """  Free form side location. (Top, Bottom, Both, Level, etc)  """  
      self.XLocation:int = obj["XLocation"]
      """  X Coordinate of the reference designator  """  
      self.YLocation:int = obj["YLocation"]
      """  Y Coordinate of the reference designator  """  
      self.ZLocation:int = obj["ZLocation"]
      """  Z Coordinate of the reference designator  """  
      self.Rotation:int = obj["Rotation"]
      """  Rotation of the reference designator. Max value = 360.000  """  
      self.Description:str = obj["Description"]
      """  Designator Description  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartMtlRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SubstanceID:str = obj["SubstanceID"]
      """  Substance identification.  """  
      self.Weight:int = obj["Weight"]
      """  Default weight of the substance per primary part of UOM  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  By default the primary UOM of the part.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.Exempt:bool = obj["Exempt"]
      self.ExemptDate:str = obj["ExemptDate"]
      self.ExemptCertificate:str = obj["ExemptCertificate"]
      self.Manual:bool = obj["Manual"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartMtlRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.Weight:bool = obj["Weight"]
      """  Yes to display when the part has no net weight or when one or more of the selected has no weight.  """  
      self.Manual:bool = obj["Manual"]
      self.ComplianceDate:str = obj["ComplianceDate"]
      self.LastRollUp:str = obj["LastRollUp"]
      self.RollUpType:str = obj["RollUpType"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartMtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Parent Part number to which this material item is a component of  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number of the part that this material item is a component of.  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  A sequence number that uniquely defines the Material record within a specific Job/Lot/Assembly. This is system assigned. The next available # is determined by reading last JobMtl record on the Job/Lot/Assembly and then adding one to it.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Quantity per parent  """  
      self.FixedQty:bool = obj["FixedQty"]
      """  Indicates if the QtyPer field represents a "Fixed Quantity".  If Yes, then the required quantity = QtyPer.  That is, the quantity does not change as the number of pieces being produced changes.  This can be used to enter Tooling or Fixture type of requirements.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   A material record can be related to a specific operation. This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job. The related operation is also used to calculate the JobMtl.ReqDate based on the operations scheduled start date and materials lead time.  """  
      self.SalvagePartNum:str = obj["SalvagePartNum"]
      """  Part number for Salvageable scrap from this material record.  An optional field. This does not have to be valid in the Part master. Salvage info is mainly to allow the credit back to a job for this type of scrap via Salvage receipt process.  """  
      self.SalvageDescription:str = obj["SalvageDescription"]
      """  Description of Salvageable material. Use Part.Description for a default.  """  
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the QtyPer results in the expected total salvage quantity.  """  
      self.SalvageUM:str = obj["SalvageUM"]
      """  Default Unit of measure for the Salvaged Part. Default from the Part.IUM.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  """  
      self.MfgComment:str = obj["MfgComment"]
      """  Material comments specific to this manufacturing process. These comments copied to Jobs/Quotes when pulled from BOM. ( See  """  
      self.OverRideMfgComments:bool = obj["OverRideMfgComments"]
      """  Indicates if these comments should override the comments defined in the part master. It controls how the MfgComments are created when this record is pulled into a Job or Quote.  If "Yes" then the comments that are defined in the Part master are NOT copied. If "No" then the PartMtl.MfgComments will be appended on to the Part.MfgComments when written to the Job/Quote material record.  """  
      self.PurComment:str = obj["PurComment"]
      """   Material comments specific to a manufacturing process. These comments (and optionally the comments from Part Master) are  copied to Jobs/Quotes when the BOM is pulled.
( See OverRidePurComments )  """  
      self.OverRidePurComments:bool = obj["OverRidePurComments"]
      """  Indicates if these comments should override the comments defined in the part master. It controls how the PurComments are created when this record is pulled into a Job or Quote.  If "Yes" then the comments that are defined in the Part master are NOT copied. If "No" then the PartMtl.PurComments will be appended on to the Part.PurComments when written to the Job/Quote material record.  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of required quantity.  """  
      self.PullAsAsm:bool = obj["PullAsAsm"]
      """  This is relevant for assemblies (Part.Method = Yes). Indicates that if this assembly should be pulled from stock or manufactured as part of the job it is pulled into. If PullAsAsm = No only the assembly record will be pulled into the job/quote (as a material), the related material and operations will not be pulled over.  """  
      self.FindNum:str = obj["FindNum"]
      """  Characters used on the drawing to show where material is used.  """  
      self.ViewAsAsm:bool = obj["ViewAsAsm"]
      """   This is relevant for assemblies (Part.Method = Yes). Indicates that if this assembly when shown in ABOM indented views or on reports it should be shown either as a subassembly or material requirement.  If Yes then the assemblies components will be shown else it is shown as a single material requirement line. Similar to the PullAsAsm flag however this is used to control how subassemblies appear in the ABOM module.
NOTE: AS OF 2.70.400 this function is not implemented.  Pending further analysis. It has been added to the schema to make it easier to implement when decision has been reached.  """  
      self.APSSchedulerName:str = obj["APSSchedulerName"]
      """  Indicates which APS Scheduler module the assembly is scheduled in.  """  
      self.APSSLDate:str = obj["APSSLDate"]
      """  APS Start Limit date.  Prevents APS from scheduling before this date.  """  
      self.APSSLTime:int = obj["APSSLTime"]
      """  APS Start Limit time.  Time, in decimal hours, that APS will not schedule before.  Only valid if APSSLDate is valid.  """  
      self.APSInsertDirection:str = obj["APSInsertDirection"]
      """  Schedule direction.  Valid options are: F=Forward, B=Backward, C=dynamic Constraint based, W=minimum WIP, E=End of work, S=Split longest duration, X=use the direction specified in task entry in APS.  """  
      self.APSInsertCriteria:str = obj["APSInsertCriteria"]
      """  Method of insertion into schedule.  Valid values are: T=best Time, G=same Group, N=uNscheduled, F=Force Insert, I=without resource assignment.  """  
      self.APSAttrib1:int = obj["APSAttrib1"]
      """  Used to calculated setup time during optimization.  """  
      self.APSAttrib2:int = obj["APSAttrib2"]
      """  Used to calculated setup time during optimization.  """  
      self.APSAttrib3:int = obj["APSAttrib3"]
      """  Used to calculated setup time during optimization.  """  
      self.APSAttrib4:int = obj["APSAttrib4"]
      """  Used to calculated setup time during optimization.  """  
      self.APSAddResType:str = obj["APSAddResType"]
      """   Advanced Planning and Scheduling Additional Resource Type.  Indicates whether the Part should be treated as an AdditionalResourceType by eScheduler.
'I' to ignore in eScheduler
'M' to treat at Material in eScheduler
'A' to treat as AddResType in eScheduler  """  
      self.SalvageMtlBurRate:int = obj["SalvageMtlBurRate"]
      """  The salvage material burden rate for this Part Material.  """  
      self.SalvageEstMtlBurUnitCredit:int = obj["SalvageEstMtlBurUnitCredit"]
      """  Estimated salvage Mtl Burden Unit Credit.  """  
      self.MtlBurRate:int = obj["MtlBurRate"]
      """  The material burden rate for this Part Material.  """  
      self.EstMtlBurUnitCost:int = obj["EstMtlBurUnitCost"]
      """  Estimated Mtl Burden Unit Cost.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this part material requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this part material.  Can be zero if RFQ(s) are not required.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.ReqdInPlant:str = obj["ReqdInPlant"]
      """  Site reference that requires this part in the current bill of Materials  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.RelatedStage:str = obj["RelatedStage"]
      """  A material record can be related to a specific operation by stage. This field contains the JobOper.StageNumber of the operation that it is related to.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method for the part material.  """  
      self.ParentMtlSeq:int = obj["ParentMtlSeq"]
      """  Indicates the parent material sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.UOMCode:str = obj["UOMCode"]
      """   Unit of Measure code of the Material requirement.
Mandatory, and must be a valid UOM of the Part's UOMClass.  """  
      self.Weight:int = obj["Weight"]
      """  Material Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Material Weight UOM defaulted from Part Master.  """  
      self.RuleTag:str = obj["RuleTag"]
      """  Rule Tag  """  
      self.ReqRefDes:int = obj["ReqRefDes"]
      """  Required number of designators  """  
      self.PlanAsAsm:bool = obj["PlanAsAsm"]
      """  This is relevant for assemblies (Part.Method = Yes). Indicates if the sub-assemby can be spawned off to a different job.  Can be true only if PullAsAsm = true.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ReassignSNAsm:bool = obj["ReassignSNAsm"]
      """  If checked this indicates that serial numbers from the job material/subassembly are going to be reassigned as the serial number of the  parent’s assembly.  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.LocationView:bool = obj["LocationView"]
      """  Controls if this material record is viewable in Location Management or the web.  """  
      self.MtlAttributeSetID:int = obj["MtlAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.SalvageAttributeSetID:int = obj["SalvageAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SalvagePlanningNumberOfPieces:int = obj["SalvagePlanningNumberOfPieces"]
      """  Salvage planning number of pieces for this attribute set.  """  
      self.SalvagePlanningAttributeSetID:int = obj["SalvagePlanningAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.CNWeightMeasurement:bool = obj["CNWeightMeasurement"]
      """  Weight Measurement  """  
      self.CNRequiredQty:int = obj["CNRequiredQty"]
      """  Required Qty  """  
      self.CNConsumedQty:int = obj["CNConsumedQty"]
      """  Consumed Qty  """  
      self.CNUOM:str = obj["CNUOM"]
      """  UOM  """  
      self.PlanningPct:int = obj["PlanningPct"]
      """  Planning Percent  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.MtlRevisionNum:str = obj["MtlRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.SalvageRevisionNum:str = obj["SalvageRevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.ExpandTree:bool = obj["ExpandTree"]
      self.GeneratedRuleTag:str = obj["GeneratedRuleTag"]
      self.MtlPartNumMfgComment:str = obj["MtlPartNumMfgComment"]
      """  The material part number mfg comment.  """  
      self.MtlPartNumPurComment:str = obj["MtlPartNumPurComment"]
      """  The material part number purchase comment.  """  
      self.MtlRevisionStatus:int = obj["MtlRevisionStatus"]
      """   Material Revision Status determined against AS OF DATE
Possible Values are: EffectiveApprovedAsOfDate = 1, EffectiveNotApprovedAsOfDate = 2, FutureEffectiveApprovedAsOfDate = 3, FutureEffectiveNotApprovedAsOfDate = 4, Unknown = 5  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Related operation description.  """  
      self.RDEndNum:int = obj["RDEndNum"]
      """  The starting and ending numbers define the reference designators that will be created. This field will be default to the same value as the ?Required Designators? field.  """  
      self.RDPrefix:str = obj["RDPrefix"]
      """  The prefix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.RDStartNum:int = obj["RDStartNum"]
      """  This number will be used to create reference designators. This field will be defaulted to ?1?  """  
      self.RDSuffix:str = obj["RDSuffix"]
      """  The suffix will be defaulted from the reference category defined for the material. The value on this field will be used to create reference designators.  """  
      self.SalvageBaseUOM:str = obj["SalvageBaseUOM"]
      self.DspUnitMeasure:str = obj["DspUnitMeasure"]
      """  The display unit of measure for the qty/parent field.  """  
      self.SalvEnableAttSetSearch:bool = obj["SalvEnableAttSetSearch"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.PlanningNumberOfPiecesDisp:int = obj["PlanningNumberOfPiecesDisp"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.SalvagePlanningNumberOfPiecesDisp:int = obj["SalvagePlanningNumberOfPiecesDisp"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.APSSchedulerNameAPSSchedulerName:str = obj["APSSchedulerNameAPSSchedulerName"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.MtlPartNumPricePerCode:str = obj["MtlPartNumPricePerCode"]
      self.MtlPartNumSellingFactor:int = obj["MtlPartNumSellingFactor"]
      self.MtlPartNumTrackSerialNum:bool = obj["MtlPartNumTrackSerialNum"]
      self.MtlPartNumPartDescription:str = obj["MtlPartNumPartDescription"]
      self.MtlPartNumIUM:str = obj["MtlPartNumIUM"]
      self.MtlPartNumTrackLots:bool = obj["MtlPartNumTrackLots"]
      self.MtlPartNumSalesUM:str = obj["MtlPartNumSalesUM"]
      self.MtlPartNumTrackDimension:bool = obj["MtlPartNumTrackDimension"]
      self.MtlPartNumTrackInventoryAttributes:bool = obj["MtlPartNumTrackInventoryAttributes"]
      self.MtlPartNumAttrClassID:str = obj["MtlPartNumAttrClassID"]
      self.MtlPartNumTypeCode:str = obj["MtlPartNumTypeCode"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.SalvagePartNumTrackLots:bool = obj["SalvagePartNumTrackLots"]
      self.SalvagePartNumTrackDimension:bool = obj["SalvagePartNumTrackDimension"]
      self.SalvagePartNumSalesUM:str = obj["SalvagePartNumSalesUM"]
      self.SalvagePartNumTrackInventoryAttributes:bool = obj["SalvagePartNumTrackInventoryAttributes"]
      self.SalvagePartNumAttrClassID:str = obj["SalvagePartNumAttrClassID"]
      self.SalvagePartNumPartDescription:str = obj["SalvagePartNumPartDescription"]
      self.SalvagePartNumIUM:str = obj["SalvagePartNumIUM"]
      self.SalvagePartNumTrackSerialNum:bool = obj["SalvagePartNumTrackSerialNum"]
      self.SalvagePartNumPricePerCode:str = obj["SalvagePartNumPricePerCode"]
      self.SalvagePartNumSellingFactor:int = obj["SalvagePartNumSellingFactor"]
      self.SalvDynAttrValueSetDescription:str = obj["SalvDynAttrValueSetDescription"]
      self.SalvDynAttrValueSetShortDescription:str = obj["SalvDynAttrValueSetShortDescription"]
      self.StageNoDescription:str = obj["StageNoDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartOpDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the PartOpr this record is linked to.  System assigned.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  System assigned.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  Uniquely identifies the PartOpDtl within the OpMaster.  """  
      self.OpDtlSeq:int = obj["OpDtlSeq"]
      """  Uniquely identifies an PartOpDtl.  System assigned.  """  
      self.CapabilityID:str = obj["CapabilityID"]
      """  The user can select the capability the operation is to perform.  The system will select the resource.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The user can select a Resource Group for the operation to be performed on.  The system will select the actual resource.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  Descriptive code assigned by the user to uniquely identify the Resource for this operation to be performed on.  """  
      self.SetupHours:int = obj["SetupHours"]
      """  The standard setup hours for the operation.   This is the setup time required for each machine.  """  
      self.ProdHours:int = obj["ProdHours"]
      """  Production hours for this operation.  It is the total hours, as though the operation were running on a single machine.  """  
      self.NumResources:int = obj["NumResources"]
      """  This is the number of resources the operation can run on.  If multiple resources can perform the required Capability, then up to this many will be employed.  This determines the number of setups the system will allow for the operation.  However, the number of setups cannot exceed the number of operations.  The idea being that once a part is on a machine you will complete the operation on that resource.  """  
      self.SetupOrProd:str = obj["SetupOrProd"]
      """  Identifies which part of the production, setup or production, the resource is required for.   Valid values are "S", indicating the resource is RequiredFor the Setup phase of this operation, "P" for Production phase, or "B" meaning Both setup and production phase.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.OpDtlDesc:str = obj["OpDtlDesc"]
      """  Description is initially created when the PartOpDtl is created.   If the PartOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method of this part operation.  """  
      self.ParentOprSeq:int = obj["ParentOprSeq"]
      """  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.ParentOpDtlSeq:int = obj["ParentOpDtlSeq"]
      """  Indicates the parent operation detail sequence.  """  
      self.ConcurrentCapacity:int = obj["ConcurrentCapacity"]
      """  Concurrent Capacity is a constraint that prevents a Resource from being overloaded because it has, at a given time, this much capacity.  For example, a Resource has 4 racks, and they can be reused, but once they've been selected for an operation, they're tied up until the operation is complete.  """  
      self.DailyProdRate:int = obj["DailyProdRate"]
      """  The Daily Prod rate contains the rate required to make 1. This is multiplied with the mfg qty of the job to get the total production qty. This total is then compared to the resource's daily production quantity  and with any usage stored in the Shopload record.   Once the production limit for a resource has been reached, the Resource has been consumed for that day.  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Duplicated from PartOper.SetupCrewSize.  The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Duplicated from PartOper.SetupCrewSize.  Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.ResourceDesc:str = obj["ResourceDesc"]
      """  Resource description  """  
      self.CapabilityDesc:str = obj["CapabilityDesc"]
      """  Capability description  """  
      self.ResourceGrpDesc:str = obj["ResourceGrpDesc"]
      """  Resource Group description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CapabilityIDDescription:str = obj["CapabilityIDDescription"]
      self.OprSeqAPSSchedulerName:str = obj["OprSeqAPSSchedulerName"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartOprActionParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part or process manufacture.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The ID of Process Manufacturing revision.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionParamSeq:int = obj["ActionParamSeq"]
      """  A sequence number which uniquely identifies parameter within the Operation/Action set.  """  
      self.ActionParamFieldDataType:str = obj["ActionParamFieldDataType"]
      """  Data type of Action Parameter.  """  
      self.ActionParamValueCharacter:str = obj["ActionParamValueCharacter"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDate:str = obj["ActionParamValueDate"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueDecimal:int = obj["ActionParamValueDecimal"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueInteger:int = obj["ActionParamValueInteger"]
      """  Value of Action Parameter.  """  
      self.ActionParamValueLogical:bool = obj["ActionParamValueLogical"]
      """  Value of Action Parameter.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartOprActionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part or process manufacture.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The ID of Process Manufacturing revision.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the method.  """  
      self.ActionSeq:int = obj["ActionSeq"]
      """  A sequence number which uniquely identifies action record within the operation set.  """  
      self.ActionDesc:str = obj["ActionDesc"]
      """  Description of Action.  """  
      self.Required:bool = obj["Required"]
      """  Indicated if this action must be completed before Operation can be completed.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartOprAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      self.OprSeq:int = obj["OprSeq"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartOprInspRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.PlanSeq:int = obj["PlanSeq"]
      """  A sequence number that uniquely identifies the PartOprInsp ecord within the Part operation  """  
      self.InspPlanPartNum:str = obj["InspPlanPartNum"]
      """  The inspection plan part number (configurator part number).  """  
      self.SpecID:str = obj["SpecID"]
      """  The specification ID.  Must be valid in the SpecHed table.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartOprMachParamRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.AltMethod:str = obj["AltMethod"]
      """  AltMethod  """  
      self.OprSeq:int = obj["OprSeq"]
      """  OprSeq  """  
      self.MachParamSeq:int = obj["MachParamSeq"]
      """  MachParamSeq  """  
      self.RequestCode:str = obj["RequestCode"]
      """  RequestCode  """  
      self.MachineNum:str = obj["MachineNum"]
      """  MachineNum  """  
      self.ToolNum:str = obj["ToolNum"]
      """  ToolNum  """  
      self.ParamNum:int = obj["ParamNum"]
      """  ParamNum  """  
      self.ParamUpperLimit:int = obj["ParamUpperLimit"]
      """  ParamUpperLimit  """  
      self.ParamNominalValue:int = obj["ParamNominalValue"]
      """  ParamNominalValue  """  
      self.ParamLowerLimit:int = obj["ParamLowerLimit"]
      """  ParamLowerLimit  """  
      self.ParamDelayValue:int = obj["ParamDelayValue"]
      """  ParamDelayValue  """  
      self.SpecEnable:bool = obj["SpecEnable"]
      """  SpecEnable  """  
      self.SpecControlAlarm:bool = obj["SpecControlAlarm"]
      """  SpecControlAlarm  """  
      self.SpecRunAlarm:bool = obj["SpecRunAlarm"]
      """  SpecRunAlarm  """  
      self.ProcSpecAlarm:bool = obj["ProcSpecAlarm"]
      """  ProcSpecAlarm  """  
      self.ProcControlAlarm:bool = obj["ProcControlAlarm"]
      """  ProcControlAlarm  """  
      self.PartQualSpecEnable:bool = obj["PartQualSpecEnable"]
      """  PartQualSpecEnable  """  
      self.PartQualControlEnable:bool = obj["PartQualControlEnable"]
      """  PartQualControlEnable  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartOprRestrictSubstRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number that uniquely defines the Material (JobMtl) record within a specific Job/Assembly.  This is system assigned.  The next available number is determined by reading last JobMtl record on the Job/Assembly and then adding ten to it.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SubstanceID:str = obj["SubstanceID"]
      """  Substance identification.  """  
      self.Weight:int = obj["Weight"]
      """  Defaulted from Operation Master Substances.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Defaulted from Operation Master Substances.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Exempt:bool = obj["Exempt"]
      self.ExemptDate:str = obj["ExemptDate"]
      self.ExemptCertificate:str = obj["ExemptCertificate"]
      self.Manual:bool = obj["Manual"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.SubstanceDescription:str = obj["SubstanceDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartOprRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.OpCode:str = obj["OpCode"]
      """  Descriptive code assigned by user which uniquely identifies a Operation master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.Weight:bool = obj["Weight"]
      """  Yes to display when the part has no net weight or when one or more of the selected has no weight.  """  
      self.Manual:bool = obj["Manual"]
      self.ComplianceDate:str = obj["ComplianceDate"]
      self.BitFlag:int = obj["BitFlag"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.RestrictionDescription:str = obj["RestrictionDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartOprRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If last = 17  next = 20.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.OpStdID:str = obj["OpStdID"]
      """   The Operation standard ID. This links the JobOPer to the OpStd master file. This can be blank or if entered must be valid if entered.  When this field is changed the ProdStandard, StdFormat and StdBasis should be refreshed with the new defaults.
Valid for "inside operations" only.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to recalculate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "OH" then (RunQty/OpsPerPart) / Std.
If StdFormat = "OM" then ((RunQty/OpsPerPart) / Std) / 60.
If StdFormat = "HP" then (RunQty/Basis) X Std.
If StdFormat = "MP" then ((RunQty/Basis) X Std) / 60.  """  
      self.ProdStandard:int = obj["ProdStandard"]
      """   The production standard for the operation. It can be expressed as Hours, Minutes per piece, Pieces per Time, Operations per Minute or Operations per hour. This along with the StdFormat, StdBasis, OpsPer and   fields are used to calculate the operations estimated production hours. A value can be defaulted from the OpStd master.
NOTE: The ProdStandard can only be zero if the EstSetHours are greater than zero.  """  
      self.StdFormat:str = obj["StdFormat"]
      """   Qualifier for the Production Standard field. This is used as a default to the qualifier field in operation details. The valid qualifiers are;
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour,
"PM" - Pieces/Minute, "OH" - Operations/Hour,
"OM"  - Operations/minute, HR - Fixed Hours.  """  
      self.StdBasis:str = obj["StdBasis"]
      """   A standard basis is to be used to with standards that are time per piece (HP & MP). The basis is a Divisor. Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours. The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  """  
      self.OpsPerPart:int = obj["OpsPerPart"]
      """  Number of operations per part. This is used in the calculation of the estimated production hours when the StdFormat is "OM" or "OH".  This should not be accessible if StdFormat is not "OM" or "OH".  It MUST BE > 0 if StdFormat is "OM" or "OH".  """  
      self.QtyPer:int = obj["QtyPer"]
      """  Production Quantity per one of the Parent Item.  """  
      self.Machines:int = obj["Machines"]
      """  Defaulted from the WrkCenter.SchMachines field. This is the number of machines that this operation will run on at the same time. Logically thought of as a "Squeeze factor" to scheduling. That is the more machines, the shorter the schedule. This affects how much of the total daily workcenter capacity that the operation will consume. For example; Center has 4 machines, 8 Hours per day and operation 2 machines. This operation would consume 16 hours of capacity per day. So if it had 32 hours of estimated production it would schedule as taking 2 days. NOTE THIS ONLY APPLIES TO PRODUCTION HOURS, TOTAL SETUP HOURS ARE ADDED TO THE SQUEEZED PRODUCTION HOURS TO GET THE NUMBER OF HOURS TO BE SCHEDULED. It is however used to calculate the total setup hours on the operation.  """  
      self.SetUpCrewSize:int = obj["SetUpCrewSize"]
      """  Defaulted from the WrkCenter.SetUpCrewSize field. Its the number of people it physically takes to se tup this operation. It is used as a  multiplier in the estimated labor hours calculation.  JobOper.EstSetHours * JobOper.SetUpCrewSize = Estimated Labor hours for the operation. This also affects the estimated labor cost. Est Cost = Est Labor Hours * SetUpLaborRate  """  
      self.ProdCrewSize:int = obj["ProdCrewSize"]
      """  Defaults from the WrkCenter.ProdCrewSize. The # of people it physically takes to perform the production on this operation per machine that it is run on.  CrewSize * JobOper.EstProdHours = Est. Prod. Labor Hours. Note this can be a fraction for operations that do not require full time attention of an employee. See also SetUpCrewSize  """  
      self.EstScrap:int = obj["EstScrap"]
      """  Estimated Scrap  """  
      self.EstScrapType:str = obj["EstScrapType"]
      """  Qualifies the ScrapQty entry as being a fixed quantity or a percentage of run quantity.  """  
      self.SubContract:bool = obj["SubContract"]
      """  This flags the operation as being a "SubContract" or an "Internal" operation.  This also controls what fields are allowed to be updated for this record. For example,  an internal operation will not have a PartNum.  """  
      self.IUM:str = obj["IUM"]
      """  Inventory UOM  """  
      self.EstUnitCost:int = obj["EstUnitCost"]
      """  Estimated Unit Cost for the SubContract operation.  Defaults from the Part table if valid PartNum.  """  
      self.DaysOut:int = obj["DaysOut"]
      """  Hours required is calculated as days * 8.  """  
      self.SubPartNum:str = obj["SubPartNum"]
      """  The PartNum to be shipped to the subcontract. Defaults as the Part number of the method to which it belongs (PartOpr.PartNum).  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The SubContractors VendorNum that ties back to the Vendor master file.  This is only valid for "SubContract"  operations. This field is not directly maintainable, instead its assigned by having the user either enter the "VendorID" and then finding the VendorNum in the Vendor file or by  selection list processing.  This is a mandatory entry for subcontract operations.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID. This field is only for the "Subcontract" operations. Along with the VendorNum is used to tie back to the VendorPP master file.  Use the default Purchase point defined in the Vendor file.  """  
      self.CommentText:str = obj["CommentText"]
      """  Editor widget for Job operation comments.  """  
      self.SchedRelation:str = obj["SchedRelation"]
      """   Indicates the scheduling relationship between this and the preceding operation. Possible values are "SS" - Start to Start, "FS" Finish to Start or "FF" Finish to Finish.
A "SS" can start when the preceding operation starts.
A "FS" starts when the preceding operation is finished.
A "FF" can finish when the preceding operation finishes.
These relationships do not span between levels of assemblies. The first operation on an assembly is always treated as being "FS" relationship.
A "FF" finishes when the preceding operation is finished.  """  
      self.RunQty:int = obj["RunQty"]
      """   The total operation quantity. This is a calculated field.  Calculated as (Assembly Required Qty X QtyPer) + Scrap. The assembly qty is either the JobHead.ProdQty if  JobOPer.AssemblySeq = 0 or (JobAsmbl.RequireQty - JobAsmbl.PullQty) if JobOPer.AssemblySeq > 0.
This value is refreshed when maintenance is performed on the operation record or an assemblies production qty is changed  """  
      self.AddlSetupHours:int = obj["AddlSetupHours"]
      """  Additional Setup Hours that will be required after a certain quantity has been run for this operation. The quantity at which this occurs is established in AddSetupQty field. The system determines the setup hours as SetupHrs + (Max((RunQty - AddlSetupQty,0))/AddlSetUpQty) * AddlSetupHours. Any fractional results of the AddlSetUpQty calculations are rounded up to the next whole number before multiplying by the AddlSetUpHours.  """  
      self.AddlSetUpQty:int = obj["AddlSetUpQty"]
      """  Additional Setup quantity indicates the quantity at which additional setup time will be incurred.  """  
      self.APSPrepOp:int = obj["APSPrepOp"]
      """  Indicates the operation that must precede this operation.  Mainly used to model one to many routing structures.  """  
      self.APSNextOp:int = obj["APSNextOp"]
      """  This is the next operation in the routing.  -1 makes this operation the last one in the routing so far; -2 makes it the first one in the routing so far; 0 means no successor.  """  
      self.APSAltOp:int = obj["APSAltOp"]
      """  Specifies the operation for which this is an alternate.  """  
      self.APSSpecificResource:str = obj["APSSpecificResource"]
      """  Used to assign an operation to a specific resource so that APS does not schedule it elsewhere.  Overrides APSCapability.  """  
      self.APSCycleTime:int = obj["APSCycleTime"]
      """   Cycles per minute.
SQL:  IIF(CINT(JobOper.RunQty) = 0 OR JobOper.SubContract = TRUE, "0", JobOper.EstProdHours * 60 /  JobOper.RunQty)  """  
      self.APSConstantTime:int = obj["APSConstantTime"]
      """   Fixed time, in decimal minutes, to be added to the operation.  Can be used to represent cleanup time or model outsource time.
SQL: IFF(JobOper.SubContract = TRUE, (JobOper.DaysOut * 1440), "0")  """  
      self.APSSetupGroup:int = obj["APSSetupGroup"]
      """  Used to group operations to save on setups.  """  
      self.APSMakeFactor:int = obj["APSMakeFactor"]
      """  Quantity of Part per cycle.  """  
      self.APSContainerSize:int = obj["APSContainerSize"]
      """  Quantity that must be completed before the next operation can start (for overlap); quantity per batch (for batch resources); Auxiliary resource quantity.  """  
      self.APSSchedulerName:str = obj["APSSchedulerName"]
      """  Name of the APS Scheduler Module in which to schedule this operation.  """  
      self.APSMaxLength:int = obj["APSMaxLength"]
      """  If the scheduled time exceeds this value then the operation is split into operations which do not exceed this length.  """  
      self.APSTransferTime:int = obj["APSTransferTime"]
      """  Time between the end of this operation and the start time of the successor operation.  """  
      self.APSEffectiveness:int = obj["APSEffectiveness"]
      """  Cycle time and constant times are divided by this value to get schedule times.  Zeros disable this feature.  """  
      self.APSOperationClass:str = obj["APSOperationClass"]
      """  Type of Operation: P for Prep, D for Processing (Dispatchable in APS terminology).  """  
      self.APSAuxResource:str = obj["APSAuxResource"]
      """  Auxiliary resource requirements.   This is a comma and tilde delimited list of APSAuxResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  """  
      self.APSAddResource:str = obj["APSAddResource"]
      """  Additional resource requirements.   This is a comma and tilde delimited list of APSAddResource.Name, Quantity, and Durations.  Example: "Setup crew,2.5,1~Bins,3.2,5".  There are two Resources specified in this list, Setup crew and Bins.  The tilde seperates the entries.  For Additional Resources the Duration = 5 (entire Operation).  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  """  
      self.FAQty:int = obj["FAQty"]
      """  The quantity requested for first article inspection.  """  
      self.RFQNeeded:bool = obj["RFQNeeded"]
      """  A flag to indicate that this part operation requires an RFQ.  If it does require an RFQ, the user must enter the number of vendor quotes that are required.  This only applies to subcontract operations.  """  
      self.RFQVendQuotes:int = obj["RFQVendQuotes"]
      """  The number of vendor quotes that are required for this part subcontract operation.  Can be zero if RFQ(s) are not required.  """  
      self.SetupGroup:str = obj["SetupGroup"]
      """  Used to group operation to save on setups.  """  
      self.AnalysisCode:str = obj["AnalysisCode"]
      """  Analysis Code  """  
      self.PrimarySetupOpDtl:int = obj["PrimarySetupOpDtl"]
      """   Identifies the primary PartOpDtl to be used for setup.  The setup time for the operation is determined on the PartOpDtl.
If <> 0, must identify a valid PartOpDtl.  The PartOpDtl needs to have a RequiredFor = S or B.  """  
      self.PrimaryProdOpDtl:int = obj["PrimaryProdOpDtl"]
      """   Identifies the primary PartOpDtl to be used for production.  The production run time for the operation is determined on the PartOpDtl.
If <> 0, must identify a valid PartOpDtl.  The PartOpDtl needs to have a RequiredFor = P or B.  """  
      self.RtgGroup:int = obj["RtgGroup"]
      """  1 is the Primary Routing Group  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.BaseMethodOverridden:bool = obj["BaseMethodOverridden"]
      """  Indicates if the base revision method was overridden.  Applies only when the AltMethod field is not blank.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The stage number of the operations.  Entered only when the related PartRev.UseStaging flag is true.  """  
      self.OpDesc:str = obj["OpDesc"]
      """  Operation Description.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  Parent Alternate Routing method of this part operation.  """  
      self.ParentOprSeq:int = obj["ParentOprSeq"]
      """  Indicates the parent operation sequence.  Applies specifically to alternate methods that inherit from a parent alternate method.  """  
      self.PBrkCost01:int = obj["PBrkCost01"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost02:int = obj["PBrkCost02"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost03:int = obj["PBrkCost03"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost04:int = obj["PBrkCost04"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost05:int = obj["PBrkCost05"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost06:int = obj["PBrkCost06"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost07:int = obj["PBrkCost07"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost08:int = obj["PBrkCost08"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost09:int = obj["PBrkCost09"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkCost10:int = obj["PBrkCost10"]
      """  if Subcontract then this is Unit Costs for the corresponding price break quantities. (BreakQty)  """  
      self.PBrkStdRate01:int = obj["PBrkStdRate01"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate02:int = obj["PBrkStdRate02"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate03:int = obj["PBrkStdRate03"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate04:int = obj["PBrkStdRate04"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate05:int = obj["PBrkStdRate05"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate06:int = obj["PBrkStdRate06"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate07:int = obj["PBrkStdRate07"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate08:int = obj["PBrkStdRate08"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate09:int = obj["PBrkStdRate09"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.PBrkStdRate10:int = obj["PBrkStdRate10"]
      """  If Internal operation (SubContract = no) then this is Production Standards for the corresponding break quantities.  """  
      self.BrkQty01:int = obj["BrkQty01"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty02:int = obj["BrkQty02"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty03:int = obj["BrkQty03"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty04:int = obj["BrkQty04"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty05:int = obj["BrkQty05"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty06:int = obj["BrkQty06"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty07:int = obj["BrkQty07"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty08:int = obj["BrkQty08"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty09:int = obj["BrkQty09"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.BrkQty10:int = obj["BrkQty10"]
      """  Price Break/Production Break Quantities. This is an array of 5 ascending quantities at which a price break occurs for subcontracting or a Production Break occurs for internal operations. The quantities represent the minimum qty that is needed to obtain the corresponding price/standard established in PBCost or PBStdRate arrays. Not all 5 elements need to be entered. However they must be entered consecutively in ascending order. Quoting selects the unit cost/Standard to use by first calculating the  Required Qty based on the quote quantity. Then searches the BreakQty array finding the element which is less than and closest to the required qty. If one is found then the corresponding PBCost/PBStdRate  is used else,  EstUnitCost for subcontract ProdStandard is used for internal operations.  """  
      self.SNRequiredOpr:bool = obj["SNRequiredOpr"]
      """  Indicates whether serial numbers are required form this operation. When true the system will prompt in labor entry processes for the serial numbers that have been completed on this operation.  """  
      self.SNRequiredSubConShip:bool = obj["SNRequiredSubConShip"]
      """  Indicates whether serial numbers are required on subcontract ship for a subcontract operation.  """  
      self.Weight:int = obj["Weight"]
      """  Operation Weight defaulted from Part Master.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """  Operation Weight UOM defaulted from Part Master.  """  
      self.SendAheadType:str = obj["SendAheadType"]
      """   Determines the scheduling offset for the secondary start-to-start operation, offset which will be either

calculated (or entered) on the primary operation. The offset time can be calculated by pieces, percentage 

of the operation duration or entered manually by the user on the primary operation. The secondary operation 

will scheduled to start after the offset period.  """  
      self.SendAheadOffset:int = obj["SendAheadOffset"]
      """   Scheduling offset for the secondary start-to-start operation. The offset time can be calculated by pieces,

percentage of the operation duration or entered manually by the user on the primary operation. The 

secondary operation will scheduled to start after the offset period.  """  
      self.PrjRoleList:str = obj["PrjRoleList"]
      """  Delimited list of PrjRoleCd codes that are allowed for this operation.  """  
      self.UseAllRoles:bool = obj["UseAllRoles"]
      """  Allow use all Roles  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.PctReg:int = obj["PctReg"]
      """  PctReg  """  
      self.SetupMaterial:int = obj["SetupMaterial"]
      """  SetupMaterial  """  
      self.MaterialColorRating:int = obj["MaterialColorRating"]
      """  MaterialColorRating  """  
      self.MiscInfo1:str = obj["MiscInfo1"]
      """  MiscInfo1  """  
      self.MiscInfo2:str = obj["MiscInfo2"]
      """  MiscInfo2  """  
      self.SetupURL:str = obj["SetupURL"]
      """  SetupURL  """  
      self.ExpPctUp:int = obj["ExpPctUp"]
      """  ExpPctUp  """  
      self.ExpCycTm:int = obj["ExpCycTm"]
      """  ExpCycTm  """  
      self.ExpGood:int = obj["ExpGood"]
      """  ExpGood  """  
      self.NonProdLimit:int = obj["NonProdLimit"]
      """  NonProdLimit  """  
      self.AutoSpcEnable:bool = obj["AutoSpcEnable"]
      """  AutoSpcEnable  """  
      self.AutoSpcPeriod:int = obj["AutoSpcPeriod"]
      """  AutoSpcPeriod  """  
      self.PartQualEnable:bool = obj["PartQualEnable"]
      """  PartQualEnable  """  
      self.AutoSpcSubgroup:int = obj["AutoSpcSubgroup"]
      """  AutoSpcSubgroup  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PulsesPerCycle:int = obj["PulsesPerCycle"]
      """  PulsesPerCycle  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.QtyPerCycle:int = obj["QtyPerCycle"]
      """  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.PlanningNumberOfPieces:int = obj["PlanningNumberOfPieces"]
      """  Planning number of pieces for this attribute set.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.TemplateID:str = obj["TemplateID"]
      """  TemplateID  """  
      self.SubRevisionNum:str = obj["SubRevisionNum"]
      """  SubRevisionNum  """  
      self.AutoReceive:bool = obj["AutoReceive"]
      """  Auto receive?  """  
      self.DspBillAddr:str = obj["DspBillAddr"]
      self.OpStdDescription:str = obj["OpStdDescription"]
      self.SetHoursPerMach:int = obj["SetHoursPerMach"]
      """  Setup hours per machine.  """  
      self.FinalOpr:bool = obj["FinalOpr"]
      """  Final Operation?  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.PrimaryProdOpDtlDesc:str = obj["PrimaryProdOpDtlDesc"]
      """  Description is initially created when the PartOpDtl is created. If the PartOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.PrimarySetupOpDtlDesc:str = obj["PrimarySetupOpDtlDesc"]
      """  Description is initially created when the PartOpDtl is created. If the PartOpDtl is created from a Resource it will be the Resource.Description, if it's created from an ResourceGroup it will be the ResourceGroup.Description.  Once set it is not changed by the system.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AnalysisCdDescription:str = obj["AnalysisCdDescription"]
      self.APSSchedulerNameAPSSchedulerName:str = obj["APSSchedulerNameAPSSchedulerName"]
      self.DynAttrValueSetDescription:str = obj["DynAttrValueSetDescription"]
      self.DynAttrValueSetShortDescription:str = obj["DynAttrValueSetShortDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.RevisionNumRevDescription:str = obj["RevisionNumRevDescription"]
      self.RevisionNumRevShortDesc:str = obj["RevisionNumRevShortDesc"]
      self.SetupGroupDescription:str = obj["SetupGroupDescription"]
      self.StageNoDescription:str = obj["StageNoDescription"]
      self.SubPartNumTrackInventoryAttributes:bool = obj["SubPartNumTrackInventoryAttributes"]
      self.SubPartNumPricePerCode:str = obj["SubPartNumPricePerCode"]
      self.SubPartNumTrackDimension:bool = obj["SubPartNumTrackDimension"]
      self.SubPartNumTrackSerialNum:bool = obj["SubPartNumTrackSerialNum"]
      self.SubPartNumSellingFactor:int = obj["SubPartNumSellingFactor"]
      self.SubPartNumIUM:str = obj["SubPartNumIUM"]
      self.SubPartNumTrackLots:bool = obj["SubPartNumTrackLots"]
      self.SubPartNumPartDescription:str = obj["SubPartNumPartDescription"]
      self.SubPartNumSalesUM:str = obj["SubPartNumSalesUM"]
      self.SubPartNumAttrClassID:str = obj["SubPartNumAttrClassID"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartRevAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PartNum:str = obj["PartNum"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.AltMethod:str = obj["AltMethod"]
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartRevRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part and is used as part of the primary key.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part, and is used as part of the primary key  """  
      self.RevShortDesc:str = obj["RevShortDesc"]
      """  Short description of the revision. This is NOT the Part description.  """  
      self.RevDescription:str = obj["RevDescription"]
      """  Used to enter a full description of the revision.  """  
      self.Approved:bool = obj["Approved"]
      """  Indicates if the methods of manufacturing have been approved for this revision.  Only approved methods can be pulled into jobs/quotes.  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  Date which this revision was approved for use by manufacturing/quoting.  This is set to the system date when the user marks the revision Approved. It is not maintainable by the user.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      """  UserID who approved the revision.  Not maintainable by the user.  """  
      self.EffectiveDate:str = obj["EffectiveDate"]
      """  Date at which this revision is considered effective.  This date is used to control the pulling of subassembly revisions.  """  
      self.TLRLaborCost:int = obj["TLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRBurdenCost:int = obj["TLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.TLRMaterialCost:int = obj["TLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSubcontractCost:int = obj["TLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRMtlBurCost:int = obj["TLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.TLRSetupLaborCost:int = obj["TLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.TLRSetupBurdenCost:int = obj["TLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRLaborCost:int = obj["LLRLaborCost"]
      """  This Level Unit Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRBurdenCost:int = obj["LLRBurdenCost"]
      """   This Level Unit Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.LLRMaterialCost:int = obj["LLRMaterialCost"]
      """  This Level Unit Material Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSubcontractCost:int = obj["LLRSubcontractCost"]
      """  This Level Unit Subcontract Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRMtlBurCost:int = obj["LLRMtlBurCost"]
      """  This Level Unit Material Burden Cost calculated by the BOM Cost rollup routine. "This level" cost excludes costs from sub assemblies.  """  
      self.LLRSetupLaborCost:int = obj["LLRSetupLaborCost"]
      """  This Level Setup Labor Cost calculated by the BOM Cost rollup routine. This level cost excludes costs from sub assemblies.  """  
      self.LLRSetupBurdenCost:int = obj["LLRSetupBurdenCost"]
      """   This Level Setup Burden Cost calculated by the BOM Cost rollup routine. "This level cost" excludes costs from sub assemblies.
Rolled up Burden cost. Calculated by the BOM cost rollup routine  """  
      self.RollupDate:str = obj["RollupDate"]
      """  Date that this part cost was last rolled up.  Updated by the BOM Cost Roll up routine.  """  
      self.DrawNum:str = obj["DrawNum"]
      """  Engineering Drawing Number. An optional field.  """  
      self.ECO:str = obj["ECO"]
      """  Engineering Change Order Number. An optional field for reference.  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part revision contains Method of Manufacture details (PartMtl/PartOpr records).  We use this to avoid processing raw material part records during processes such as BOM Cost roll up, Indented BOM lists, etc...  """  
      self.AutoRecOpr:int = obj["AutoRecOpr"]
      """   The operation number PartOpr.OprSeq) that is marked to do the Automatic Receipt to inventory.  Note: Zero = no operation is set to perform the auto receive into inventory function.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Auto Receive" which then updates this field with the operations sequence number.  """  
      self.FinalOpr:int = obj["FinalOpr"]
      """   The sequence of the operation that is to be considered as the operation which indicates the quantity complete for the Job/Assembly.  In other words this operations completed quantity = Job/Assembly completed.   Note: Zero = no operation is set and that the system should use the last operation to determine quantity complete.
This field is not directly maintainable. Instead it is set during operation maintenance by having the user mark a check box indicating "Final Operation" which then updates this field with the operations sequence number.  """  
      self.PDMObjID:str = obj["PDMObjID"]
      """  Holds the internal object id of pdm parts.  """  
      self.Configured:bool = obj["Configured"]
      """  If true then the revision has a configuration defined for it.  This will be set when a configuration is approved.  """  
      self.WebConfigured:bool = obj["WebConfigured"]
      """  If set to TRUE then the revision can be configured in StoreFront.  """  
      self.ShowInputPrice:bool = obj["ShowInputPrice"]
      """  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method to be used for this revision, and is used as part of the primary key  """  
      self.AltMethodDesc:str = obj["AltMethodDesc"]
      """  The description of the alternate method.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.ParentAltMethod:str = obj["ParentAltMethod"]
      """  The alternate method of the parent this method inherits from.  """  
      self.UseStaging:bool = obj["UseStaging"]
      """  Indicates if this revision is to use stage number or operations on materials.  If false, operation sequences are to be used.  If true, staging numbers are to be used.  """  
      self.UseAltRevForParts:bool = obj["UseAltRevForParts"]
      """  UseAltRevForParts: Flag to indicate if the Use Alternate method for parts option is selected, this flag affects directly the creation and loading of data inside EngWorkbench, because it will control the Alternate Method used.  """  
      self.OwnershipStatus:str = obj["OwnershipStatus"]
      """  This field can be used with external system integrations to identify which system currently has ownership of the record.  This field can hold either the name of the external system (example: PDM), ERP (Epicor) or null.  """  
      self.ExtConfig:bool = obj["ExtConfig"]
      """  External Configurator  """  
      self.ValRefDes:bool = obj["ValRefDes"]
      """  Validate Reference Designators.  """  
      self.PcGlobalPart:bool = obj["PcGlobalPart"]
      """  Is the part for this revision a global part  """  
      self.PcEntprsConf:bool = obj["PcEntprsConf"]
      """  If a configuration is created for this revision, is it marked as enterprise configurator  """  
      self.GlobalRev:bool = obj["GlobalRev"]
      """  Marks the Part Revision as a global Revision, available to be sent out to other companies  """  
      self.RoughCutCode:str = obj["RoughCutCode"]
      """  Rough Cut Code.  Rough cut parameters to use when rough cut scheduling for the revision.  """  
      self.RMAInspPlan:str = obj["RMAInspPlan"]
      """  The inspection plan part number (configurator part number) to use for RMA processing for this part.  """  
      self.RMASpecID:str = obj["RMASpecID"]
      """  The specification ID to use for RMA processing for this part.  """  
      self.RMASampleSize:int = obj["RMASampleSize"]
      """  The default sample size to use for RMA processing for this part  """  
      self.RMASampleSizePct:int = obj["RMASampleSizePct"]
      """  Percentage of quantity to be inspected for RMA processing of this part  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  The part number used to identify the configured part number that this part revision was created from  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  The revision number used to identify the configured part revision this part number was generated from.  """  
      self.ConfigID:str = obj["ConfigID"]
      """  ConfigID  """  
      self.RegenConfig:bool = obj["RegenConfig"]
      """  RegenConfig  """  
      self.SIValuesGroupSeq:int = obj["SIValuesGroupSeq"]
      """  SIValuesGroupSeq  """  
      self.SIValuesHeadNum:int = obj["SIValuesHeadNum"]
      """  SIValuesHeadNum  """  
      self.ExternalMES:bool = obj["ExternalMES"]
      """  Indicates the record is used with Machine MES  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ProcessMode:str = obj["ProcessMode"]
      """  Indicates the way in which parts are made for Co-Part jobs.  There are two value “S” – Sequential and “C” – Concurrent.  Sequential is the default. This field is similar to the JobHead.ProcessMode field.  """  
      self.DefaultConfigPart:bool = obj["DefaultConfigPart"]
      """  DefaultConfigPart  """  
      self.CoPartsReqQty:int = obj["CoPartsReqQty"]
      """  Number of COPart required in the Revision  """  
      self.MtlCostPct:int = obj["MtlCostPct"]
      """  Material Cost Factor  """  
      self.LaborCostPct:int = obj["LaborCostPct"]
      """  Labor Cost Factor  """  
      self.CoPartsPerOp:int = obj["CoPartsPerOp"]
      """  Number of COParts per Operation  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  CreatedBy  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  ChangedOn  """  
      self.ExternalMESSyncRequired:bool = obj["ExternalMESSyncRequired"]
      """  This field determines if the record needs to be synchronized to the Machine MES. Changes to the record will automatically set the value to true.  """  
      self.ExternalMESLastSync:str = obj["ExternalMESLastSync"]
      """  The date and time the record was last synched to Machine MES.  The field is maintained by the Export Mattec process.  """  
      self.CNCustomsBOM:bool = obj["CNCustomsBOM"]
      """  Customs BOM  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The identifier of related Process Manufacturing.  """  
      self.ProcessMfgType:str = obj["ProcessMfgType"]
      """  Type of Process Manufacturing this revision is for: General, Site, Master.  """  
      self.ProcessMfgDescription:str = obj["ProcessMfgDescription"]
      """  Description of Process Manufacturing revision.  """  
      self.UseAdvancedStaging:bool = obj["UseAdvancedStaging"]
      """  Indicates if this revision is to use Advanced Staging.  """  
      self.ProcessMfgLastGroupID:str = obj["ProcessMfgLastGroupID"]
      """  The last Group to modify this Revision for Recipe Authoring.  """  
      self.ECPCEnabled:bool = obj["ECPCEnabled"]
      """  Only Part Revisions marked as Connected Process Control (CPC) enable will be send to CPC.  """  
      self.DisableApproved:bool = obj["DisableApproved"]
      self.ECOGroup:str = obj["ECOGroup"]
      """  Name of ECO Group that this part is checked out to  """  
      self.HasCoParts:bool = obj["HasCoParts"]
      """  This field will be set to true if two or more ECOCoParts records exist for the revision.  """  
      self.ParentAltMethodDesc:str = obj["ParentAltMethodDesc"]
      self.ParentPartNum:str = obj["ParentPartNum"]
      """  Part Number of the Parent Part  """  
      self.ParentRevisionNum:str = obj["ParentRevisionNum"]
      """  Revision number  of Parent Part.  """  
      self.ProdCode:str = obj["ProdCode"]
      self.RevStatusAsOfDate:int = obj["RevStatusAsOfDate"]
      """   Revision Status used to determina in the Revision of all the Materials are Effective As Of Date
Used to indicate the MAX MtlRevisionStatus of all its Materials/SubAssemblies.
If <= 2 the all its materials/subAssemblies's Revisions are Effective As Of Date  """  
      self.SpecHedDescription:str = obj["SpecHedDescription"]
      self.vDate:str = obj["vDate"]
      """  Last date that this Revison is effective.  (Next Rev Effective date - 1)  """  
      self.vQty:int = obj["vQty"]
      self.Class:str = obj["Class"]
      self.NonStock:bool = obj["NonStock"]
      self.IsRootNode:bool = obj["IsRootNode"]
      """  Indicates that the PartRev is the root node in the tree  """  
      self.EngineeringApproved:bool = obj["EngineeringApproved"]
      """  Holds the ECORev Approved flag for the last ProcessMfgID specified against the PartRev  """  
      self.BitFlag:int = obj["BitFlag"]
      self.InspPlanDescription:str = obj["InspPlanDescription"]
      self.PartDescriptionTrackDimension:bool = obj["PartDescriptionTrackDimension"]
      self.PartDescriptionSellingFactor:int = obj["PartDescriptionSellingFactor"]
      self.PartDescriptionPartDescription:str = obj["PartDescriptionPartDescription"]
      self.PartDescriptionIUM:str = obj["PartDescriptionIUM"]
      self.PartDescriptionTrackLots:bool = obj["PartDescriptionTrackLots"]
      self.PartDescriptionPricePerCode:str = obj["PartDescriptionPricePerCode"]
      self.PartDescriptionSalesUM:str = obj["PartDescriptionSalesUM"]
      self.PartDescriptionTrackSerialNum:bool = obj["PartDescriptionTrackSerialNum"]
      self.PartDescriptionTypeCode:str = obj["PartDescriptionTypeCode"]
      self.PcStatusConfigType:str = obj["PcStatusConfigType"]
      self.PlantName:str = obj["PlantName"]
      self.RoughCutParamDescription:str = obj["RoughCutParamDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartStageRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It can be blank if using Process Manufacturing.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part or process manufacture.  """  
      self.AltMethod:str = obj["AltMethod"]
      """  Alternate Routing method for the part revision.  """  
      self.ProcessMfgID:str = obj["ProcessMfgID"]
      """  The ID of Process Manufacturing revision.  """  
      self.StageSeq:int = obj["StageSeq"]
      """  A sequence number which uniquely identifies stage record within the stage set.  """  
      self.StageNumber:str = obj["StageNumber"]
      """  The identification of related StageNo.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.GeneralRequirements:str = obj["GeneralRequirements"]
      """  High-level descriptions of General Requirements for Stage.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetAllAlternateTrees_input:
   """ Required : 
   ipPartNum
   ipRevisionNum
   ipUseDefaultMethod
   ipAsOfDate
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return data for.  """  
      self.ipUseDefaultMethod:bool = obj["ipUseDefaultMethod"]
      """  For partrev records other than the first one,
            would you like to use the default alternate method or the inputted one?  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to retun a complete dataset for this group?  """  
      pass

class GetAllAlternateTrees_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BomSearchTableset] = obj["returnObj"]
      pass

class GetDatasetForTreeByProcessMfgID_input:
   """ Required : 
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipProcessMfgID
   ipUseDefaultMethod
   ipAsOfDate
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return data for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to return data for.  """  
      self.ipProcessMfgID:str = obj["ipProcessMfgID"]
      """  The Alternate Method to return data for.  """  
      self.ipUseDefaultMethod:bool = obj["ipUseDefaultMethod"]
      """  For partrev records other than the first one, would you like to use the default alternate method or the inputted one?  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to retun a complete dataset for this group?  """  
      pass

class GetDatasetForTreeByProcessMfgID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BomSearchTableset] = obj["returnObj"]
      pass

class GetDatasetForTreeWithPartValidation_input:
   """ Required : 
   asOfDate
   partNum
   revisionNum
   altMethod
   isRootNode
   """  
   def __init__(self, obj):
      self.asOfDate:str = obj["asOfDate"]
      """  As Of Date  """  
      self.partNum:str = obj["partNum"]
      """  Part  """  
      self.revisionNum:str = obj["revisionNum"]
      """  Revision  """  
      self.altMethod:str = obj["altMethod"]
      """  Alt Method  """  
      self.isRootNode:bool = obj["isRootNode"]
      """  Indicates if this is the root part/rev in the tree  """  
      pass

class GetDatasetForTreeWithPartValidation_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BomSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.effectiveRevisionMessage:str = obj["parameters"]
      self.effectiveRevisionSubAsmMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetDatasetForTree_input:
   """ Required : 
   ipPartNum
   ipRevisionNum
   ipAltMethod
   ipUseDefaultMethod
   ipAsOfDate
   ipCompleteTree
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  The Part Number to return data for.  """  
      self.ipRevisionNum:str = obj["ipRevisionNum"]
      """  The Revision Number to return data for.  """  
      self.ipAltMethod:str = obj["ipAltMethod"]
      """  The Alternate Method to return data for.  """  
      self.ipUseDefaultMethod:bool = obj["ipUseDefaultMethod"]
      """  For partrev records other than the first one, would you like to use the default alternate method or the inputted one?  """  
      self.ipAsOfDate:str = obj["ipAsOfDate"]
      """  The as of date for the revisions, what would this look as of this date  """  
      self.ipCompleteTree:bool = obj["ipCompleteTree"]
      """  Would you like to retun a complete dataset for this group?  """  
      pass

class GetDatasetForTree_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_BomSearchTableset] = obj["returnObj"]
      pass

class GetPartNumSource_input:
   """ Required : 
   ipSourceRowID
   droppedAs
   """  
   def __init__(self, obj):
      self.ipSourceRowID:str = obj["ipSourceRowID"]
      self.droppedAs:str = obj["droppedAs"]
      pass

class GetPartNumSource_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  PartNum  """  
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

class PartRevExists_input:
   """ Required : 
   PartNum
   RevNum
   AltMethod
   """  
   def __init__(self, obj):
      self.PartNum:str = obj["PartNum"]
      """  Part ID  """  
      self.RevNum:str = obj["RevNum"]
      """  Revision ID  """  
      self.AltMethod:str = obj["AltMethod"]
      """  AltMethod  """  
      pass

class PartRevExists_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

