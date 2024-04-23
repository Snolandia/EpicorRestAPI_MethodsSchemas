import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.SerialNoAssignSvc
# Description: This is a process based business object that does not use
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoAssignSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoAssignSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetSelectSerialNumbersParams(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipPartNum">ipPartNum</param><param name="ipAttributeSetID">ipAttributeSetID</param><param name="ipQuantity">ipQuantity</param><param name="ipJobNum">ipJobNum</param><param name="ipAssemblySeq">ipAssemblySeq</param><returns></returns>
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoAssignSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSerialNoAssign(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSerialNoAssign
   Description: Gets the default values for the Serial number assignment screen.
Also populates the Selectedserialnumbers table for the job.
   OperationID: GetSerialNoAssign
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialNoAssign_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNoAssign_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoAssignSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSerialAssignForIDPart(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetSerialAssignForIDPart
   Description: Gets the default values for the ID/Serial number assignment screen.
Also populates the Selectedserialnumbers table for the part.
   OperationID: GetSerialAssignForIDPart
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSerialAssignForIDPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialAssignForIDPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoAssignSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetSerialNoAssign(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetSerialNoAssign
   Description: Validates the job number, assembly sequence and part number. Also validates
the part is serial tracked.  Updates the SerialNo table and the Part table
for the SN Format fields.  Calls the SNTran create subroutine.
   OperationID: SetSerialNoAssign
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetSerialNoAssign_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetSerialNoAssign_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoAssignSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateDelete(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateDelete
   Description: Purpose:
Parameters:  validateDelete
Notes:
<param name="ipSerialNo">ipSerialNo</param><param name="ipPartNum">ipPartNum</param><param name="ipAttributeSetID">ipAttributeSetID</param><param name="ipJobNum">ipJobNum</param><param name="ipAssemblySeq">ipAssemblySeq</param><param name="ipDoOprCmpVldtn">ipDoOprCmpVldtn -whether or not do operation complete validation</param><param name="oprCmpWarning">oprCmpWarning</param><returns></returns>
   OperationID: ValidateDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateDelete_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoAssignSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateSN(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number manually entered is valid for this transaction
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoAssignSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetSiteSerialTracking(epicorHeaders = None):
   """  
   Summary: Invoke method GetSiteSerialTracking
   Description: Returns serial tracking settings for the current plant
   OperationID: GetSiteSerialTracking
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSiteSerialTracking_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.SerialNoAssignSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
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

class Erp_Tablesets_SerialNoAssignRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.JobNumber:str = obj["JobNumber"]
      """  Job number  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Part number description.  """  
      self.SerialNoQty:int = obj["SerialNoQty"]
      """  Serial number quantity  """  
      self.PartNum:str = obj["PartNum"]
      """  Part number  """  
      self.JobQty:int = obj["JobQty"]
      """  Job quantity  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_SerialNoAssignTableset:
   def __init__(self, obj):
      self.SelectedSerialNumbers:list[Erp_Tablesets_SelectedSerialNumbersRow] = obj["SelectedSerialNumbers"]
      self.SerialNoAssign:list[Erp_Tablesets_SerialNoAssignRow] = obj["SerialNoAssign"]
      self.SNFormat:list[Erp_Tablesets_SNFormatRow] = obj["SNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetSelectSerialNumbersParams_input:
   """ Required : 
   ipPartNum
   ipAttributeSetID
   ipQuantity
   ipJobNum
   ipAssemblySeq
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      self.ipQuantity:int = obj["ipQuantity"]
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      pass

class GetSelectSerialNumbersParams_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SelectSerialNumbersParamsTableset] = obj["returnObj"]
      pass

class GetSerialAssignForIDPart_input:
   """ Required : 
   ipPartNum
   ipPackNum
   ipPackLine
   ipRequiredQty
   """  
   def __init__(self, obj):
      self.ipPartNum:str = obj["ipPartNum"]
      """  Part  """  
      self.ipPackNum:int = obj["ipPackNum"]
      """  PackNum  """  
      self.ipPackLine:int = obj["ipPackLine"]
      """  PackLine  """  
      self.ipRequiredQty:int = obj["ipRequiredQty"]
      """  Required Quantity  """  
      pass

class GetSerialAssignForIDPart_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoAssignTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.TrackSerialNo:bool = obj["TrackSerialNo"]
      pass

      """  output parameters  """  

class GetSerialNoAssign_input:
   """ Required : 
   JobNum
   AssemblySeq
   ipPartNum
   ipReqQtyOverride
   """  
   def __init__(self, obj):
      self.JobNum:str = obj["JobNum"]
      """  Job number.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  Assembly sequence for the job.  """  
      self.ipPartNum:str = obj["ipPartNum"]
      """  (Possible) Job Part  """  
      self.ipReqQtyOverride:int = obj["ipReqQtyOverride"]
      """  (Possible) Override to RequiredQty  """  
      pass

class GetSerialNoAssign_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_SerialNoAssignTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.TrackSerialNo:bool = obj["TrackSerialNo"]
      pass

      """  output parameters  """  

class GetSiteSerialTracking_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.fullSerialTracking:bool = obj["fullSerialTracking"]
      self.lowLvlSerialTracking:bool = obj["lowLvlSerialTracking"]
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

class SetSerialNoAssign_input:
   """ Required : 
   ds
   ipDoOprCmpVldtn
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoAssignTableset] = obj["ds"]
      self.ipDoOprCmpVldtn:bool = obj["ipDoOprCmpVldtn"]
      """  ipDoOprCmpVldtn -whether or not do operation complete validation  """  
      pass

class SetSerialNoAssign_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_SerialNoAssignTableset] = obj["ds"]
      self.oprCmpWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateDelete_input:
   """ Required : 
   ipSerialNo
   ipPartNum
   ipAttributeSetID
   ipJobNum
   ipAssemblySeq
   ipDoOprCmpVldtn
   """  
   def __init__(self, obj):
      self.ipSerialNo:str = obj["ipSerialNo"]
      self.ipPartNum:str = obj["ipPartNum"]
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      self.ipJobNum:str = obj["ipJobNum"]
      self.ipAssemblySeq:int = obj["ipAssemblySeq"]
      self.ipDoOprCmpVldtn:bool = obj["ipDoOprCmpVldtn"]
      pass

class ValidateDelete_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.oprCmpWarning:str = obj["parameters"]
      pass

      """  output parameters  """  

class ValidateSN_input:
   """ Required : 
   serialNumber
   jobNum
   partNum
   ipAttributeSetID
   """  
   def __init__(self, obj):
      self.serialNumber:str = obj["serialNumber"]
      """  Serial number to validate.  """  
      self.jobNum:str = obj["jobNum"]
      """  Job Number.  """  
      self.partNum:str = obj["partNum"]
      """  Part Number.  """  
      self.ipAttributeSetID:int = obj["ipAttributeSetID"]
      """  Attribute Set  """  
      pass

class ValidateSN_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.isVoided:bool = obj["isVoided"]
      pass

      """  output parameters  """  

