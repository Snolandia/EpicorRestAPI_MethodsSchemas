import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PackOutSearchSvc
# Description: This object replaces the current Warehouse object in some cases
           when building the combo-boxes/searches.  This is a non-standard
           object that will include shared warehouses in the result list
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackOutSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackOutSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClause, matchField, orderNum, packNum, pcid, packMode, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Get PackOut rows and filter them through POGetRows.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "matchField=" + matchField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "orderNum=" + orderNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "packNum=" + packNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pcid=" + pcid
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "packMode=" + packMode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackOutSearchSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_POGetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method POGetRows
   Description: This methods will return all of the ttPackOut search records.  This method will try
to mirror the functionality of the base GetRows method but since we are populating
a temp table we need our own public method.
   OperationID: POGetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/POGetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/POGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PackOutSearchSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TFOrderGetRows(matchField, packNum, orderNum, epicorHeaders = None):
   """  
   Summary: Invoke method TFOrderGetRows
   Description: Get PackOut rows and filter them through POGetRows.
   OperationID: Get_TFOrderGetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/TFOrderGetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "matchField=" + matchField
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "packNum=" + packNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "orderNum=" + orderNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PackOutSearchSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_LegalNumGenOptsRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.TransYear:int = obj["TransYear"]
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      self.DspTransYear:str = obj["DspTransYear"]
      self.ShowDspTransYear:bool = obj["ShowDspTransYear"]
      """  Indicates if DspTransYear should be displayed when prompting for a manual number.  """  
      self.Prefix:str = obj["Prefix"]
      self.PrefixList:str = obj["PrefixList"]
      """  The list of prefixes that can be selected by the user for manual numbers.  """  
      self.NumberSuffix:str = obj["NumberSuffix"]
      """  The suffix portion of the legal number.  """  
      self.EnablePrefix:bool = obj["EnablePrefix"]
      """  Indicates if the prefix can be entered by the user.  """  
      self.EnableSuffix:bool = obj["EnableSuffix"]
      """  Indicates if the suffix (number) can be entered by the user.  """  
      self.NumberOption:str = obj["NumberOption"]
      self.DocumentDate:str = obj["DocumentDate"]
      self.GenerationType:str = obj["GenerationType"]
      self.Description:str = obj["Description"]
      self.TransPeriod:int = obj["TransPeriod"]
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix for the period  """  
      self.ShowTransPeriod:bool = obj["ShowTransPeriod"]
      self.LegalNumber:str = obj["LegalNumber"]
      """  Used when the full legal number is entered  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.TranDocTypeID2:str = obj["TranDocTypeID2"]
      self.GenerationOption:str = obj["GenerationOption"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POSNFormatRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.HasSerialNumbers:bool = obj["HasSerialNumbers"]
      self.LeadingZeroes:bool = obj["LeadingZeroes"]
      """  Whether or not to have leading zeroes  """  
      self.NumberOfDigits:int = obj["NumberOfDigits"]
      """  Number of digits in the serial number  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.SNBaseDataType:str = obj["SNBaseDataType"]
      """  Serial Number base data type  """  
      self.SNFormat:str = obj["SNFormat"]
      """  Serial Number format  """  
      self.SNPrefix:str = obj["SNPrefix"]
      """  Current Prefix setting  """  
      self.Plant:str = obj["Plant"]
      self.SNLastUsedSeq:str = obj["SNLastUsedSeq"]
      self.SNMask:str = obj["SNMask"]
      self.SNMaskPrefix:str = obj["SNMaskPrefix"]
      self.SNMaskSuffix:str = obj["SNMaskSuffix"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_POSelectedSerialNumbersRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.Deselected:bool = obj["Deselected"]
      """  Used to flag previously selected serial numbers as deselected  """  
      self.KitWhseList:str = obj["KitWhseList"]
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.PassedInspection:bool = obj["PassedInspection"]
      """  True if this serial numbered part passed inspection  """  
      self.ReasonCodeDesc:str = obj["ReasonCodeDesc"]
      """  Reason code description  """  
      self.ReasonCodeType:str = obj["ReasonCodeType"]
      """  Reason code type = s  """  
      self.Reference:str = obj["Reference"]
      """  Reference field  """  
      self.Scrapped:bool = obj["Scrapped"]
      """  Scrapped flag  """  
      self.ScrappedReasonCode:str = obj["ScrappedReasonCode"]
      """  Scrapped reason code  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  SerialNumber  """  
      self.SNBaseNumber:str = obj["SNBaseNumber"]
      """  Base number used to create the serial number  """  
      self.SNPrefix:str = obj["SNPrefix"]
      self.SourceRowID:str = obj["SourceRowID"]
      """  RowID of the source record for this serial number  """  
      self.TransType:str = obj["TransType"]
      """  TransType of the record that created this serial number  """  
      self.Voided:bool = obj["Voided"]
      """  Voided flag  """  
      self.RawSerialNum:str = obj["RawSerialNum"]
      """  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  """  
      self.KBLbrAction:int = obj["KBLbrAction"]
      """  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  """  
      self.KBLbrActionDesc:str = obj["KBLbrActionDesc"]
      """  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  """  
      self.PreventDeselect:bool = obj["PreventDeselect"]
      """  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  """  
      self.poLinkValues:str = obj["poLinkValues"]
      """  temporary field used to link the packout lines to ship detail lines  """  
      self.SNMask:str = obj["SNMask"]
      """  The mask that was used to generate the serial number  """  
      self.NotSavedToDB:bool = obj["NotSavedToDB"]
      """  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  Used only by SN Assignment, needed here to keep POSelectedSerialNumbers in sync with SelectedSerialNumbers  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  Used only by SN Assignment: needed here to keep POSelctedSerialNumbers in sync with SelectedSerialNumbers  """  
      self.PreDeselected:bool = obj["PreDeselected"]
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackOutRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.PackNum:int = obj["PackNum"]
      self.ShipViaCode:str = obj["ShipViaCode"]
      self.EntryPerson:str = obj["EntryPerson"]
      self.LabelComment:str = obj["LabelComment"]
      self.ShipComment:str = obj["ShipComment"]
      self.ShipToNum:str = obj["ShipToNum"]
      self.CustNum:int = obj["CustNum"]
      self.PackLine:int = obj["PackLine"]
      self.OrderNum:int = obj["OrderNum"]
      self.OrderLine:int = obj["OrderLine"]
      self.OrderRelNum:int = obj["OrderRelNum"]
      self.LineType:str = obj["LineType"]
      self.OurInventoryShipQty:int = obj["OurInventoryShipQty"]
      self.OurJobShipQty:int = obj["OurJobShipQty"]
      self.JobNum:str = obj["JobNum"]
      self.PartNum:str = obj["PartNum"]
      self.LineDesc:str = obj["LineDesc"]
      self.RevisionNum:str = obj["RevisionNum"]
      self.ShipCmpl:bool = obj["ShipCmpl"]
      self.BinNum:str = obj["BinNum"]
      self.ShpConNum:int = obj["ShpConNum"]
      self.LotNum:str = obj["LotNum"]
      self.DimCode:str = obj["DimCode"]
      self.DUM:str = obj["DUM"]
      self.DimConvFactor:int = obj["DimConvFactor"]
      self.InvoiceComment:str = obj["InvoiceComment"]
      self.ShipStatus:str = obj["ShipStatus"]
      self.Stage:str = obj["Stage"]
      self.BTCustomerName:str = obj["BTCustomerName"]
      self.BTConNum:int = obj["BTConNum"]
      self.BTCustID:str = obj["BTCustID"]
      self.InvQty:int = obj["InvQty"]
      self.PackQty:int = obj["PackQty"]
      self.ShipAddr:str = obj["ShipAddr"]
      self.StockPart:bool = obj["StockPart"]
      self.CustName:str = obj["CustName"]
      self.KitPartNum:str = obj["KitPartNum"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.KitNumPartDescription:str = obj["KitNumPartDescription"]
      self.KitPartRev:str = obj["KitPartRev"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.TotRelQty:int = obj["TotRelQty"]
      self.PromptPartRev:bool = obj["PromptPartRev"]
      self.PromptKitRevision:bool = obj["PromptKitRevision"]
      self.PromptJobNum:bool = obj["PromptJobNum"]
      self.PromptOrderRel:bool = obj["PromptOrderRel"]
      self.PromptKit:bool = obj["PromptKit"]
      self.AutoQuantity:bool = obj["AutoQuantity"]
      self.PromptOrderLine:bool = obj["PromptOrderLine"]
      self.ToPlant:str = obj["ToPlant"]
      self.FromPlant:str = obj["FromPlant"]
      self.FromAddr:str = obj["FromAddr"]
      self.PackMode:str = obj["PackMode"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.TFOrdNum:str = obj["TFOrdNum"]
      self.BTCustNum:int = obj["BTCustNum"]
      self.AssemblySeq:int = obj["AssemblySeq"]
      self.OprSeq:int = obj["OprSeq"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.NumMatchs:int = obj["NumMatchs"]
      self.PackOutNum:int = obj["PackOutNum"]
      """  Unique identifer for the PackOut dataset  """  
      self.Plant:str = obj["Plant"]
      self.IsInvoiced:bool = obj["IsInvoiced"]
      self.MFTransNum:str = obj["MFTransNum"]
      self.TrackingNumber:str = obj["TrackingNumber"]
      self.MFCallTag:str = obj["MFCallTag"]
      self.MFPickUpNum:str = obj["MFPickUpNum"]
      self.MFZone:str = obj["MFZone"]
      self.MFFreightAmt:int = obj["MFFreightAmt"]
      self.MFDiscFreight:int = obj["MFDiscFreight"]
      self.MFOtherAmt:int = obj["MFOtherAmt"]
      self.MFOversized:bool = obj["MFOversized"]
      self.MFTemplate:str = obj["MFTemplate"]
      self.MFDimWeight:int = obj["MFDimWeight"]
      self.ShipDate:str = obj["ShipDate"]
      self.VendorID:str = obj["VendorID"]
      self.Quantity:int = obj["Quantity"]
      self.TotPackedQty:int = obj["TotPackedQty"]
      self.RemainQty:int = obj["RemainQty"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.HasCartonLines:bool = obj["HasCartonLines"]
      """  Set from ShipHead.HasCartonLines  """  
      self.PONum:int = obj["PONum"]
      self.POLine:int = obj["POLine"]
      self.PORelNum:int = obj["PORelNum"]
      self.EnableWeight:bool = obj["EnableWeight"]
      """  Determines whether the weight field should be enabled or not, depending on the current workstation settings.  """  
      self.ShipStatusXlate:str = obj["ShipStatusXlate"]
      self.PkgCode:str = obj["PkgCode"]
      self.PkgClass:str = obj["PkgClass"]
      self.KitFlag:str = obj["KitFlag"]
      self.PkgHeight:int = obj["PkgHeight"]
      """  Height of packaging  """  
      self.PkgHeightEnable:int = obj["PkgHeightEnable"]
      """  If zero the packaging height prompt is enabled.  """  
      self.PkgLength:int = obj["PkgLength"]
      """  Length of packaging  """  
      self.PkgLenEnable:int = obj["PkgLenEnable"]
      """  Zero indicates the length is to be enabled.  """  
      self.PkgWidth:int = obj["PkgWidth"]
      """  Width of packaging  """  
      self.PkgWidthEnable:int = obj["PkgWidthEnable"]
      """  Zero indicates the width prompt is enabled.  """  
      self.WayBillNbr:str = obj["WayBillNbr"]
      self.FreightedShipViaCode:str = obj["FreightedShipViaCode"]
      self.CODAmount:int = obj["CODAmount"]
      """  COD Amount  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Decared Insurance Amount  """  
      self.PhantomPack:bool = obj["PhantomPack"]
      """  Logical indicating this pack has phantom cases.  Used by UI to disable phantom controlled fields.  """  
      self.Weight:int = obj["Weight"]
      """  Pack weight.  """  
      self.MasterpackPackNum:int = obj["MasterpackPackNum"]
      """  Masterpack PackID this pack is on.  """  
      self.EnableWhseBin:bool = obj["EnableWhseBin"]
      """  Enables the Warehouse and Bin fields on the UIApp  """  
      self.PkgSizeUOMEnable:int = obj["PkgSizeUOMEnable"]
      """  0 indicates Pkg Size UOM should be enabled  """  
      self.PkgSizeUOM:str = obj["PkgSizeUOM"]
      self.WeightUOM:str = obj["WeightUOM"]
      self.InventoryShipUOM:str = obj["InventoryShipUOM"]
      self.JobShipUOM:str = obj["JobShipUOM"]
      self.EnablePOSerialBtn:bool = obj["EnablePOSerialBtn"]
      self.DocumentPrinted:bool = obj["DocumentPrinted"]
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  Ship To Customer  """  
      self.EnablePackageControl:bool = obj["EnablePackageControl"]
      """  Boolean indicating if the package control functionality should be enabled.  """  
      self.PCID:str = obj["PCID"]
      self.ShipToWarning:str = obj["ShipToWarning"]
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      """  temp message to display newly created legal number  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  Legal Number associated with pack  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  TranDocTypeID associated with Pack.  """  
      self.TranDocTypeDescription:str = obj["TranDocTypeDescription"]
      """  TranDocType Description associated with this Pack  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.KitAttributeSetID:int = obj["KitAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.KitAttributeSetDescription:str = obj["KitAttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.KitAttributeSetShortDescription:str = obj["KitAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.AllowChgAfterPrint:bool = obj["AllowChgAfterPrint"]
      """  Indicates if changes can occur after the document has been printed  """  
      self.HasLegNumCnfg:bool = obj["HasLegNumCnfg"]
      """  Indicates if a legal number configuration exists for pack out  """  
      self.EnableAssignLegNum:bool = obj["EnableAssignLegNum"]
      """  Indicates if assign legal number option is available.  """  
      self.EnableVoidLegNum:bool = obj["EnableVoidLegNum"]
      """  Indicates if the void legal number option is available  """  
      self.EnableTranDocType:bool = obj["EnableTranDocType"]
      """  Indicates if TranDocTypeID is available for input.  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.ReadyToInvoice:bool = obj["ReadyToInvoice"]
      self.EnableReadyToInvoice:bool = obj["EnableReadyToInvoice"]
      """  Indicates if Ready to Invoice is enabled or not  """  
      self.ShipToInactive:bool = obj["ShipToInactive"]
      """  Indicates if the record is inactive.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PackOutTableset:
   def __init__(self, obj):
      self.PackOut:list[Erp_Tablesets_PackOutRow] = obj["PackOut"]
      self.LegalNumGenOpts:list[Erp_Tablesets_LegalNumGenOptsRow] = obj["LegalNumGenOpts"]
      self.POSelectedSerialNumbers:list[Erp_Tablesets_POSelectedSerialNumbersRow] = obj["POSelectedSerialNumbers"]
      self.POSNFormat:list[Erp_Tablesets_POSNFormatRow] = obj["POSNFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetRows_input:
   """ Required : 
   whereClause
   matchField
   orderNum
   packNum
   pcid
   packMode
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.matchField:str = obj["matchField"]
      self.orderNum:int = obj["orderNum"]
      self.packNum:int = obj["packNum"]
      self.pcid:str = obj["pcid"]
      self.packMode:str = obj["packMode"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackOutTableset] = obj["returnObj"]
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

class POGetRows_input:
   """ Required : 
   whereClausettPackOutSearch
   matchfield
   ds
   """  
   def __init__(self, obj):
      self.whereClausettPackOutSearch:str = obj["whereClausettPackOutSearch"]
      """  The where clause to restrict data for  """  
      self.matchfield:str = obj["matchfield"]
      """  comma delimited list of field to find unique hits  """  
      self.ds:list[Erp_Tablesets_PackOutTableset] = obj["ds"]
      pass

class POGetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackOutTableset] = obj["returnObj"]
      pass

class TFOrderGetRows_input:
   """ Required : 
   matchField
   packNum
   orderNum
   """  
   def __init__(self, obj):
      self.matchField:str = obj["matchField"]
      self.packNum:int = obj["packNum"]
      self.orderNum:str = obj["orderNum"]
      pass

class TFOrderGetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PackOutTableset] = obj["returnObj"]
      pass

