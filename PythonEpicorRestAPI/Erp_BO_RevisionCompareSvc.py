import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RevisionCompareSvc
# Description: Revision Compare Bussines Object
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_BomSetDesignatorsChgFlag(epicorHeaders = None):
   """  
   Summary: Invoke method BomSetDesignatorsChgFlag
   Description: Set Reference Designator change flag
   OperationID: BomSetDesignatorsChgFlag
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/BomSetDesignatorsChgFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_GetComparisonWithComparisonTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetComparisonWithComparisonTypes
   Description: Performs validations based on comparison types, and performs revision comparison if validations pass
   OperationID: GetComparisonWithComparisonTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetComparisonWithComparisonTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetComparisonWithComparisonTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetComparison(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetComparison
   OperationID: GetComparison
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetComparison_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetComparison_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetJobMOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetJobMOM
   Description: To retrieve the Assemblies, Materials and Operations that make up the Method of Manufacturing
for the given Job (or optionally, the given assembly within that Job's MOM).
The set of fields in the dataset is NOT COMPLETE, it only contains fields that are in common
with the MOM definitions corresponding to all three of Quote, Job and Part.  (Actually, only
the fields that are present in Vantage 6.10 Revision Compare;  it is possible there are
fields have been omitted.)
   OperationID: GetJobMOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetJobMOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJobMOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPartMOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPartMOM
   Description: To retrieve the Assemblies, Materials and Operations that make up the Method of Manufacturing
for the given Part Revision.
The set of fields in the dataset is NOT COMPLETE, it only contains fields that are in common
with the MOM definitions corresponding to all three of Quote, Job and Part.  (Actually, only
the fields that are present in Vantage 6.10 Revision Compare;  it is possible there are
fields have been omitted.)
   OperationID: GetPartMOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPartMOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartMOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetQuoteMOM(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetQuoteMOM
   Description: To retrieve the Assemblies, Materials and Operations that make up the Method of Manufacturing
for the given QuoteLine (or optionally, the given assembly within that QuoteLine's MOM).
The set of fields in the dataset is NOT COMPLETE, it only contains fields that are in common
with the MOM definitions corresponding to all three of Quote, Job and Part.  (Actually, only
the fields that are present in Vantage 6.10 Revision Compare;  it is possible there are
fields have been omitted.)
   OperationID: GetQuoteMOM
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetQuoteMOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuoteMOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RevisionCompareSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class BomSetDesignatorsChgFlag_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_MaterialCompRow:
   def __init__(self, obj):
      self.Comparison:int = obj["Comparison"]
      """  1=LeftHandSide/From record is displayed; 2=RightHandSide/To record is displayed; 0=No change: displayed record is both LHS and RHS  """  
      self.EndPartNum:str = obj["EndPartNum"]
      """  Part number which has its indented bill of materials list created in this file.
It is used to relate all indented BOM Component records to the final end part number which is being viewed.  """  
      self.EndRevision:str = obj["EndRevision"]
      """  Revision number of the EndPartNum (see EndPartNum)  """  
      self.EndRevisionChg:bool = obj["EndRevisionChg"]
      self.BOMSequence:int = obj["BOMSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.BOMStatus:str = obj["BOMStatus"]
      self.BOMStatusChg:bool = obj["BOMStatusChg"]
      self.BOMLevel:int = obj["BOMLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  """  
      self.BOMLevelChg:bool = obj["BOMLevelChg"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.IndMtlPartNum:str = obj["IndMtlPartNum"]
      """  The Indented Part Number of the component material record for the related Parent Part.  Ex. ...DCD-100-SP  """  
      self.IndMtlPartNumChg:bool = obj["IndMtlPartNumChg"]
      self.MtlRevision:str = obj["MtlRevision"]
      """  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  """  
      self.MtlRevisionChg:bool = obj["MtlRevisionChg"]
      self.PartDescription:str = obj["PartDescription"]
      """   Describes the material component Part.
Copied from the Part.PartDescription.  """  
      self.PartDescriptionChg:bool = obj["PartDescriptionChg"]
      self.QtyPer:int = obj["QtyPer"]
      self.QtyPerChg:bool = obj["QtyPerChg"]
      self.QtyRequired:int = obj["QtyRequired"]
      self.QtyRequiredChg:bool = obj["QtyRequiredChg"]
      self.BOMType:str = obj["BOMType"]
      """  Indicates if this is an assembly "ASM" or raw material "Mtl" requirement.  It is set based on the PartRev.PullAsAsm value, Yes = Asm, No = Mtl.  """  
      self.BOMTypeChg:bool = obj["BOMTypeChg"]
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the QtyRequired results in the expected total salvage quantity.  """  
      self.SalvageQtyPerChg:bool = obj["SalvageQtyPerChg"]
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  """  
      self.SalvageUnitCreditChg:bool = obj["SalvageUnitCreditChg"]
      self.RelatedOperation:int = obj["RelatedOperation"]
      self.RelatedOperationChg:bool = obj["RelatedOperationChg"]
      self.UOM:str = obj["UOM"]
      self.UOMChg:bool = obj["UOMChg"]
      self.Designators:str = obj["Designators"]
      """  Reference designators  """  
      self.DesignatorsChg:bool = obj["DesignatorsChg"]
      """  Reference designators change  """  
      self.MtlSeq:int = obj["MtlSeq"]
      self.MtlSeqChg:bool = obj["MtlSeqChg"]
      self.DspSequence:int = obj["DspSequence"]
      self.PlanningPct:int = obj["PlanningPct"]
      """  Planning Pct  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RevAsmRow:
   def __init__(self, obj):
      self.BOMSequence:int = obj["BOMSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.ParentBOMSequence:int = obj["ParentBOMSequence"]
      """  BOMSequence number of the Parent Assembly.  """  
      self.AsmPartNum:str = obj["AsmPartNum"]
      """  Part number for this assembly.  Cannot be blank.  Does not have to be valid in the Part master file.  """  
      self.AsmRevisionNum:str = obj["AsmRevisionNum"]
      """  The revision number for the assembly.  An optional field.  Defaults from the most current PartRev.RevisionNum.  """  
      self.AsmAltMethod:str = obj["AsmAltMethod"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RevComparisonTableset:
   def __init__(self, obj):
      self.MaterialComp:list[Erp_Tablesets_MaterialCompRow] = obj["MaterialComp"]
      self.RoutingComp:list[Erp_Tablesets_RoutingCompRow] = obj["RoutingComp"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RevDesRow:
   def __init__(self, obj):
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  """  
      self.BomMtlSequence:int = obj["BomMtlSequence"]
      """  A sequence number that uniquely defines the Material record within a specific Job/Part/Quote Assembly.  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.Description:str = obj["Description"]
      """  Link to PartMtlRefDes table when available.  """  
      self.EndAltMethod:str = obj["EndAltMethod"]
      self.EndPartNum:str = obj["EndPartNum"]
      """  Part number which has its indented bill of materials list created in this file.  It is used to relate all indented BOM Component records to the final end part number which is being viewed.  """  
      self.EndRevision:str = obj["EndRevision"]
      """  Revision number of the EndPartNum (see EndPartNum)  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      self.MtlRevision:str = obj["MtlRevision"]
      """  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  """  
      self.RefDes:str = obj["RefDes"]
      """  Link to PartMtlRefDes table when available.  """  
      self.RefDesSeq:int = obj["RefDesSeq"]
      """  Link to PartMtlRefDes table when available.  """  
      self.Rotation:int = obj["Rotation"]
      """  Link to PartMtlRefDes table when available.  """  
      self.Side:str = obj["Side"]
      self.XLocation:int = obj["XLocation"]
      """  Link to PartMtlRefDes table when available.  """  
      self.YLocation:int = obj["YLocation"]
      """  Link to PartMtlRefDes table when available.  """  
      self.ZLocation:int = obj["ZLocation"]
      """  Link to PartMtlRefDes table when available.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RevMtlRow:
   def __init__(self, obj):
      self.EndPartNum:str = obj["EndPartNum"]
      """  Part number which has its indented bill of materials list created in this file.
It is used to relate all indented BOM Component records to the final end part number which is being viewed.  """  
      self.EndRevision:str = obj["EndRevision"]
      """  Revision number of the EndPartNum (see EndPartNum)  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.BomMtlSequence:int = obj["BomMtlSequence"]
      """  A sequence number that uniquely defines the Material record within a specific Job/Part/Quote Assembly.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.MtlRevision:str = obj["MtlRevision"]
      """  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  """  
      self.PartDescription:str = obj["PartDescription"]
      """   Describes the material component Part.
Copied from the Part.PartDescription.  """  
      self.QtyPer:int = obj["QtyPer"]
      self.QtyRequired:int = obj["QtyRequired"]
      self.SalvageQtyPer:int = obj["SalvageQtyPer"]
      """  A factor that multiplied by the QtyRequired results in the expected total salvage quantity.  """  
      self.SalvageUnitCredit:int = obj["SalvageUnitCredit"]
      """  Estimated Salvage Unit Credit. Use the appropriate cost from the Part master as a default.  """  
      self.RelatedOperation:int = obj["RelatedOperation"]
      """   A material record can be related to a specific operation. This field contains the JobOper.OprSeq of the operation that it is related to.
It can be left as zero meaning that this material is required at the very beginning of the production job.  """  
      self.EndAltMethod:str = obj["EndAltMethod"]
      self.RelatedStage:str = obj["RelatedStage"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RevOprRow:
   def __init__(self, obj):
      self.EndPartNum:str = obj["EndPartNum"]
      """  Part number which has its indented bill of materials list created in this file.
It is used to relate all indented BOM Component records to the final end part number which is being viewed.  """  
      self.EndRevision:str = obj["EndRevision"]
      """  Revision number of the EndPartNum (see EndPartNum)  """  
      self.BomSequence:int = obj["BomSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.BomOprSequence:int = obj["BomOprSequence"]
      """  A sequence number which uniquely identifies the operation record within the Job/Part/Quote Assembly.  """  
      self.BomLevel:int = obj["BomLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  """  
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.MtlRevision:str = obj["MtlRevision"]
      """  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  """  
      self.PartDescription:str = obj["PartDescription"]
      """   Describes the material component Part.
Copied from the Part.PartDescription.  """  
      self.QtyPer:int = obj["QtyPer"]
      self.QtyRequired:int = obj["QtyRequired"]
      self.BOMType:str = obj["BOMType"]
      """  Indicates if this is an assembly "ASM" or raw material "Mtl" requirement.  It is set based on the PartRev.PullAsAsm value, Yes = Asm, No = Mtl.  """  
      self.OprSeq:int = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user. System generated numbers are determined by reading last JobOper for the job/lot/level and then figures out what the next number that is divisible by 10. If this number is within 3 of the last Number on file it will be bumped up another 10. This keeps a minimum of 2 available sequences between records. For example if last = 18 Next would be 30, If l  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """  The planned workcenter for this operation. Must  valid in the WrkCenter master file. Links the operation to a WorkCenter master.  """  
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.EstSetHours:int = obj["EstSetHours"]
      """  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  """  
      self.EstProdHours:int = obj["EstProdHours"]
      """   The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalcuate it  when it is needed.  It is calculated using the ProdStandard, StdFormat, StdBasis, OpsPerPart, QtyPer, EstScrap and EstScrapType.
FORMULAS:
If StdFormat = "HR" then EstProdHours = ProdStandard. 
If StdFormat = "PH" then (RunQty / Std).
If StdFormat = "PM" then (RunQty / Std ) / 60.
If StdFormat = "O  """  
      self.EndAltMethod:str = obj["EndAltMethod"]
      self.StageNumber:str = obj["StageNumber"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RevisionCompareTableset:
   def __init__(self, obj):
      self.RevAsm:list[Erp_Tablesets_RevAsmRow] = obj["RevAsm"]
      self.RevMtl:list[Erp_Tablesets_RevMtlRow] = obj["RevMtl"]
      self.RevOpr:list[Erp_Tablesets_RevOprRow] = obj["RevOpr"]
      self.RevDes:list[Erp_Tablesets_RevDesRow] = obj["RevDes"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RoutingCompRow:
   def __init__(self, obj):
      self.Comparison:int = obj["Comparison"]
      """  1=LeftHandSide/From record is displayed; 2=RightHandSide/To record is displayed; 0=No change: displayed record is both LHS and RHS  """  
      self.EndPartNum:str = obj["EndPartNum"]
      """  Part number which has its indented bill of materials list created in this file.
It is used to relate all indented BOM Component records to the final end part number which is being viewed.  """  
      self.EndRevision:str = obj["EndRevision"]
      """  Revision number of the EndPartNum (see EndPartNum)  """  
      self.EndRevisionChg:bool = obj["EndRevisionChg"]
      self.BOMSequence:int = obj["BOMSequence"]
      """  An internally system assigned integer which is used as part of an index to organize the records into a Bill of Material fashion sequence.  """  
      self.BOMStatus:str = obj["BOMStatus"]
      self.BOMStatusChg:bool = obj["BOMStatusChg"]
      self.BOMLevel:int = obj["BOMLevel"]
      """  An internally system assigned integer which represents the "Level of Indention" of the assembly in reference to the Bill of Material structure.  """  
      self.BOMLevelChg:bool = obj["BOMLevelChg"]
      self.MtlPartNum:str = obj["MtlPartNum"]
      """  The Part Number of the component material record for the related Parent Part.  """  
      self.IndMtlPartNum:str = obj["IndMtlPartNum"]
      """  The Indented Part Number of the component material record for the related Parent Part.  Ex. ...DCD-100-SP  """  
      self.IndMtlPartNumChg:bool = obj["IndMtlPartNumChg"]
      self.MtlRevision:str = obj["MtlRevision"]
      """  Revision number of the Material Component Part.  The revision is picked based on effectivity dates.  """  
      self.MtlRevisionChg:bool = obj["MtlRevisionChg"]
      self.PartDescription:str = obj["PartDescription"]
      """   Describes the material component Part.
Copied from the Part.PartDescription.  """  
      self.PartDescriptionChg:bool = obj["PartDescriptionChg"]
      self.QtyPer:int = obj["QtyPer"]
      self.QtyPerChg:bool = obj["QtyPerChg"]
      self.QtyRequired:int = obj["QtyRequired"]
      self.QtyRequiredChg:bool = obj["QtyRequiredChg"]
      self.BOMType:str = obj["BOMType"]
      """  Indicates if this is an assembly "ASM" or raw material "Mtl" requirement.  It is set based on the PartRev.PullAsAsm value, Yes = Asm, No = Mtl.  """  
      self.BOMTypeChg:bool = obj["BOMTypeChg"]
      self.ResourceGroup:str = obj["ResourceGroup"]
      """  The planned ResourceGroup (workcenter) for this operation. Must  valid in the ResourceGroup master file. Links the operation to a ResourceGroup master.  """  
      self.ResourceGroupChg:bool = obj["ResourceGroupChg"]
      self.OpCode:str = obj["OpCode"]
      """   Operation Master Code - Links the JobOper  record with a OpMaster record. Default is given from WrkCenter.OpCode.
Must be valid in the OpMaster file.  """  
      self.OpCodeChg:bool = obj["OpCodeChg"]
      self.OprSeq:str = obj["OprSeq"]
      """  A sequence number which uniquely identifies the operation record within the Job/lot/level. The sequence can be system generated or assigned by user.  """  
      self.OprSeqChg:bool = obj["OprSeqChg"]
      self.EstSetHours:int = obj["EstSetHours"]
      """  The estimated set up hours. This can be zero only if the ProdStandard is greater than zero. Default from OpStd.SetupHours.  """  
      self.EstSetHoursChg:bool = obj["EstSetHoursChg"]
      self.EstProdHours:int = obj["EstProdHours"]
      """  The estimated Production run hours for internal operations (Subcontract = No) . This is not directly maintainable. It exists so that it will be easier to display than always having to  recalcuate it  when it is needed.  """  
      self.EstProdHoursChg:bool = obj["EstProdHoursChg"]
      self.DspSequence:int = obj["DspSequence"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetComparisonWithComparisonTypes_input:
   """ Required : 
   fromComparison
   toComparison
   pcMOM1PartNum
   pcMOM1RevisionNum
   pcMOM1AltMethod
   pcMOM1JobNum
   piMOM1QuoteNum
   piMOM1QuoteLine
   piMOM1AssemblySeq
   pdMOM1AsOfDate
   pcMOM2PartNum
   pcMOM2RevisionNum
   pcMOM2AltMethod
   pcMOM2JobNum
   piMOM2QuoteNum
   piMOM2QuoteLine
   piMOM2AssemblySeq
   pdMOM2AsOfDate
   """  
   def __init__(self, obj):
      self.fromComparison:str = obj["fromComparison"]
      """  Indicates what the from comparison is: Quote, Job, Part  """  
      self.toComparison:str = obj["toComparison"]
      """  Indicates what the to comparison is: Quote, Job, Part  """  
      self.pcMOM1PartNum:str = obj["pcMOM1PartNum"]
      """  Item1 Part number (applies to Part comparison).  """  
      self.pcMOM1RevisionNum:str = obj["pcMOM1RevisionNum"]
      """  Item1 RevisionNum (applies to Part comparison).  """  
      self.pcMOM1AltMethod:str = obj["pcMOM1AltMethod"]
      """  (optional) Item1 AltMethod (applies to Part comparison).  """  
      self.pcMOM1JobNum:str = obj["pcMOM1JobNum"]
      """  Item1 JobNum (applies to Job comparison).  """  
      self.piMOM1QuoteNum:int = obj["piMOM1QuoteNum"]
      """  Item1 QuoteNum (applies to Quote comparison).  """  
      self.piMOM1QuoteLine:int = obj["piMOM1QuoteLine"]
      """  Item1 QuoteLine (applies to Quote comparison).  """  
      self.piMOM1AssemblySeq:int = obj["piMOM1AssemblySeq"]
      """  Item1 AssemblySeq (applies to Job or Quote comparison).  """  
      self.pdMOM1AsOfDate:str = obj["pdMOM1AsOfDate"]
      """  (optional) Item1 "as of" date for Revisions to be used (applies to Job or Part comparison).  """  
      self.pcMOM2PartNum:str = obj["pcMOM2PartNum"]
      """  Item2 Part number (applies to Part comparison).  """  
      self.pcMOM2RevisionNum:str = obj["pcMOM2RevisionNum"]
      """  Item2 RevisionNum (applies to Part comparison).  """  
      self.pcMOM2AltMethod:str = obj["pcMOM2AltMethod"]
      """  (optional) Item2 AltMethod (applies to Part comparison).  """  
      self.pcMOM2JobNum:str = obj["pcMOM2JobNum"]
      """  Item2 JobNum (applies to Job comparison).  """  
      self.piMOM2QuoteNum:int = obj["piMOM2QuoteNum"]
      """  Item2 QuoteNum (applies to Quote comparison).  """  
      self.piMOM2QuoteLine:int = obj["piMOM2QuoteLine"]
      """  Item2 QuoteLine (applies to Quote comparison).  """  
      self.piMOM2AssemblySeq:int = obj["piMOM2AssemblySeq"]
      """  Item2 AssemblySeq (applies to Job or Quote comparison).  """  
      self.pdMOM2AsOfDate:str = obj["pdMOM2AsOfDate"]
      """  (optional) Item2 "as of" date for Revisions to be used (applies to Job or Part comparison).  """  
      pass

class GetComparisonWithComparisonTypes_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RevComparisonTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pcFrameTitle:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetComparison_input:
   """ Required : 
   pcMOM1PartNum
   pcMOM1RevisionNum
   pcMOM1AltMethod
   pcMOM1JobNum
   piMOM1QuoteNum
   piMOM1QuoteLine
   piMOM1AssemblySeq
   pdMOM1AsOfDate
   pcMOM2PartNum
   pcMOM2RevisionNum
   pcMOM2AltMethod
   pcMOM2JobNum
   piMOM2QuoteNum
   piMOM2QuoteLine
   piMOM2AssemblySeq
   pdMOM2AsOfDate
   """  
   def __init__(self, obj):
      self.pcMOM1PartNum:str = obj["pcMOM1PartNum"]
      """  Item1 Part number (applies to Part comparison).  """  
      self.pcMOM1RevisionNum:str = obj["pcMOM1RevisionNum"]
      """  Item1 RevisionNum (applies to Part comparison).  """  
      self.pcMOM1AltMethod:str = obj["pcMOM1AltMethod"]
      """  (optional) Item1 AltMethod (applies to Part comparison).  """  
      self.pcMOM1JobNum:str = obj["pcMOM1JobNum"]
      """  Item1 JobNum (applies to Job comparison).  """  
      self.piMOM1QuoteNum:int = obj["piMOM1QuoteNum"]
      """  Item1 QuoteNum (applies to Quote comparison).  """  
      self.piMOM1QuoteLine:int = obj["piMOM1QuoteLine"]
      """  Item1 QuoteLine (applies to Quote comparison).  """  
      self.piMOM1AssemblySeq:int = obj["piMOM1AssemblySeq"]
      """  Item1 AssemblySeq (applies to Job or Quote comparison).  """  
      self.pdMOM1AsOfDate:str = obj["pdMOM1AsOfDate"]
      """  (optional) Item1 "as of" date for Revisions to be used (applies to Job or Part comparison).  """  
      self.pcMOM2PartNum:str = obj["pcMOM2PartNum"]
      """  Item2 Part number (applies to Part comparison).  """  
      self.pcMOM2RevisionNum:str = obj["pcMOM2RevisionNum"]
      """  Item2 RevisionNum (applies to Part comparison).  """  
      self.pcMOM2AltMethod:str = obj["pcMOM2AltMethod"]
      """  (optional) Item2 AltMethod (applies to Part comparison).  """  
      self.pcMOM2JobNum:str = obj["pcMOM2JobNum"]
      """  Item2 JobNum (applies to Job comparison).  """  
      self.piMOM2QuoteNum:int = obj["piMOM2QuoteNum"]
      """  Item2 QuoteNum (applies to Quote comparison).  """  
      self.piMOM2QuoteLine:int = obj["piMOM2QuoteLine"]
      """  Item2 QuoteLine (applies to Quote comparison).  """  
      self.piMOM2AssemblySeq:int = obj["piMOM2AssemblySeq"]
      """  Item2 AssemblySeq (applies to Job or Quote comparison).  """  
      self.pdMOM2AsOfDate:str = obj["pdMOM2AsOfDate"]
      """  (optional) Item2 "as of" date for Revisions to be used (applies to Job or Part comparison).  """  
      pass

class GetComparison_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RevComparisonTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.pcFrameTitle:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetJobMOM_input:
   """ Required : 
   pcJobNum
   piAssemblySeq
   """  
   def __init__(self, obj):
      self.pcJobNum:str = obj["pcJobNum"]
      """  Job ID of MOM (Bill of Materials + Bill of Operations) to be retrieved.  """  
      self.piAssemblySeq:int = obj["piAssemblySeq"]
      """  (optional) Assembly number of MOM to be retrieved.  """  
      pass

class GetJobMOM_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RevisionCompareTableset] = obj["returnObj"]
      pass

class GetPartMOM_input:
   """ Required : 
   pcPartNum
   pcRevisionNum
   pcAltMethod
   pdAsOfDate
   """  
   def __init__(self, obj):
      self.pcPartNum:str = obj["pcPartNum"]
      """  Part number of MOM (Bill of Materials + Bill of Operations) to be retrieved.  """  
      self.pcRevisionNum:str = obj["pcRevisionNum"]
      """  Revision ID of MOM to be retrieved.  """  
      self.pcAltMethod:str = obj["pcAltMethod"]
      """  Alt Method of MOM to be retrieved.  """  
      self.pdAsOfDate:str = obj["pdAsOfDate"]
      """  (optional) Revisions that were current as of this date to be used.  """  
      pass

class GetPartMOM_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RevisionCompareTableset] = obj["returnObj"]
      pass

class GetQuoteMOM_input:
   """ Required : 
   piQuoteNum
   piQuoteLine
   piAssemblySeq
   pdAsOfDate
   """  
   def __init__(self, obj):
      self.piQuoteNum:int = obj["piQuoteNum"]
      """  Quote number of MOM (Bill of Materials + Bill of Operations) to be retrieved.  """  
      self.piQuoteLine:int = obj["piQuoteLine"]
      """  Quote Line of MOM to be retrieved.  """  
      self.piAssemblySeq:int = obj["piAssemblySeq"]
      """  (optional) Assembly number of MOM to be retrieved.  """  
      self.pdAsOfDate:str = obj["pdAsOfDate"]
      """  (optional) Revisions that were current as of this date to be used.  """  
      pass

class GetQuoteMOM_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RevisionCompareTableset] = obj["returnObj"]
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

