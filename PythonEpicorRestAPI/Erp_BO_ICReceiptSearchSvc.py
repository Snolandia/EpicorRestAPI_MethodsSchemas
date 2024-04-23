import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.ICReceiptSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICReceiptSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICReceiptSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClause, PONum, POLine, PORel, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This overload of AfterGetRows filters the Dataset for the criteria
   OperationID: Get_GetRows
      :param whereClause: Desc: The criteria   Required: True   Allow empty value : True
      :param PONum: Desc: PONum - Purchase Order Number   Required: True
      :param POLine: Desc: POLine - Line   Required: True
      :param PORel: Desc: PORel - Release   Required: True
      :param pageSize: Desc: Size of a page   Required: True
      :param absolutePage: Desc: The absolute page   Required: True
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
   params += "PONum=" + PONum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "POLine=" + POLine
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "PORel=" + PORel
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.ICReceiptSearchSvc/$metadata" + params,headers=creds) as resp:
           return await resp.json()

async def post_RcvHeadBeforeDelete(epicorHeaders = None):
   """  
   Summary: Invoke method RcvHeadBeforeDelete
   OperationID: RcvHeadBeforeDelete
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RcvHeadBeforeDelete_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ICReceiptSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_RcvHeadBeforeGetNew(epicorHeaders = None):
   """  
   Summary: Invoke method RcvHeadBeforeGetNew
   OperationID: RcvHeadBeforeGetNew
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RcvHeadBeforeGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ICReceiptSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def post_RcvHeadBeforeUpdate(epicorHeaders = None):
   """  
   Summary: Invoke method RcvHeadBeforeUpdate
   OperationID: RcvHeadBeforeUpdate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RcvHeadBeforeUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.ICReceiptSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_ICReceiptSearchTableset:
   def __init__(self, obj):
      self.RcvHead:list[Erp_Tablesets_RcvHeadRow] = obj["RcvHead"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RcvHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key that is used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  The Vendors purchase point ID.  """  
      self.PackSlip:str = obj["PackSlip"]
      """  Vendors Packing Slip #.  """  
      self.ReceiptDate:str = obj["ReceiptDate"]
      """  Receipt Date. Defaults as current system date.  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  Person that entered the transaction. It is set to the DCD-USERID that was logged on when the record was created . This is not maintainable by the user. This is could be used as a selection parameter for reporting and browsing.  """  
      self.SaveForInvoicing:bool = obj["SaveForInvoicing"]
      """  An internal flag that indicates this receipt document is to be saved for retrieval by A\P invoice entry. This is set based on the value stored in APSyst.SaveForInvoicing.  """  
      self.Invoiced:bool = obj["Invoiced"]
      """  An internal flag that indicates "ALL" the details items on this receipt document have been invoiced. This is set to "Yes" when there are no related RcvDtl records where RcvDtl.Invoiced = No. This flag along with the SaveForInvoicing flag are used to present a list of uninvoiced packing slips.  """  
      self.ReceiptComment:str = obj["ReceiptComment"]
      """  Contains comments about the overall Receipt.  """  
      self.ReceivePerson:str = obj["ReceivePerson"]
      """  Short name or initials of person who actually did the receiving. A totally optional field which can be used for internal reference.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  The code that links to the ShipVia master. Can be blank or must be valid in the ShipVia.  """  
      self.EntryDate:str = obj["EntryDate"]
      """  The system date when this record was created.  """  
      self.Plant:str = obj["Plant"]
      """  Site that received the goods.  """  
      self.PONum:int = obj["PONum"]
      """  Purchase order number that uniquely identifies the purchase order.  """  
      self.LCReference:str = obj["LCReference"]
      """  Reference field for Landed Costs  """  
      self.LCComment:str = obj["LCComment"]
      """  Comment field for Landed Costs  """  
      self.LandedCost:int = obj["LandedCost"]
      """  Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  """  
      self.LCVariance:int = obj["LCVariance"]
      """  This field holds the variance amount for the landed costs.  """  
      self.ICLinked:bool = obj["ICLinked"]
      """  Indicates if linked to a inter-company shipment  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Global Company identifier.  Used in Consolidated Purchasing.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  Global Vendor identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Global Purchase Point identifier.  Used in Consolidated Purchasing.  """  
      self.GlbPackSlip:str = obj["GlbPackSlip"]
      """  Global Packing Slip identifier.  Used in Consolidated Purchasing.  """  
      self.ContainerID:int = obj["ContainerID"]
      """  Autogenerated container ID.  Maintained by using the ContainerIDSeq.  """  
      self.Weight:int = obj["Weight"]
      """  Weight  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost was disbursed among the container details.  Valid options are Volume (only for po releases tied to a container), Weight, Value and Manual.  """  
      self.AutoReceipt:bool = obj["AutoReceipt"]
      """  This is a flag representing whether or not this is a receipt that was auto generated.  It could only be true if it is associated with an SMI type PO.  """  
      self.AutoTranType:str = obj["AutoTranType"]
      """  Indicates the type of transaction that created this auto receipt.  This field will only be populated if AutoReceipt = true.  """  
      self.POType:str = obj["POType"]
      """  POType Identifier of the associated PO ('Std', 'CMI', or 'SMI')  """  
      self.AutoTranID:int = obj["AutoTranID"]
      """  The unique number of the PartTran record that was the source of this transaction.  This field will only be populated if AutoReceipt = true.  """  
      self.WeightUOM:str = obj["WeightUOM"]
      """   Qualifies the unit of measure of the Weight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  if Part.NetWeightUOM is not known.  """  
      self.UpliftPercent:int = obj["UpliftPercent"]
      """  Uplift Percent is used to calculate additional landed cost amount on top of the given indirect cost.  """  
      self.SpecDutyAmt:int = obj["SpecDutyAmt"]
      """  This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  """  
      self.AppliedLCAmt:int = obj["AppliedLCAmt"]
      """  The total Landed Cost Amount disbursed for this receipt.  """  
      self.LCDutyAmt:int = obj["LCDutyAmt"]
      """  The total Duty Amount of the entire receipt.  """  
      self.LCIndCost:int = obj["LCIndCost"]
      """  The total Indirect Cost Amount of the entire receipt.  """  
      self.ApplyToLC:bool = obj["ApplyToLC"]
      """  Flag to indicate if all of the receipt duties and indirect costs needs to be applied or disbursed.  """  
      self.Received:bool = obj["Received"]
      """  Flag to indicate if the entire receipt has been completely received.  """  
      self.ArrivedDate:str = obj["ArrivedDate"]
      """  The date the shipment arrived. Defaults as current system date.  """  
      self.AppliedRcptLCAmt:int = obj["AppliedRcptLCAmt"]
      """  The total Landed Cost Amount applied for this receipt.  """  
      self.LCUpliftIndCost:int = obj["LCUpliftIndCost"]
      """  The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  """  
      self.AppliedLCVariance:int = obj["AppliedLCVariance"]
      """  This field holds the applied variance amount for the landed costs.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.ImportNum:str = obj["ImportNum"]
      """  Stores the number of the import document.  Default value for lines.  """  
      self.ImportedFrom:int = obj["ImportedFrom"]
      """  Stores the Country from which the document is imported.  Default value for lines.  """  
      self.ImportedFromDesc:str = obj["ImportedFromDesc"]
      """  Location description from which the document is imported.  Default value for lines.  """  
      self.GrossWeight:int = obj["GrossWeight"]
      """  Gross Weight  """  
      self.GrossWeightUOM:str = obj["GrossWeightUOM"]
      """   Qualifies the unit of measure of the GrossWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a defaul
t  if Part.GrossWeightUOM is not known.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  ChangedBy  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  ChangeDate  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  The Tax Liability for this Receipt  """  
      self.TaxPoint:str = obj["TaxPoint"]
      """  Tax Point  """  
      self.TaxRateDate:str = obj["TaxRateDate"]
      """  Date Used to calculate Tax Rates  """  
      self.InPrice:bool = obj["InPrice"]
      """  Indicates that the tax is included in the unit price  """  
      self.HdrTaxNoUpdt:bool = obj["HdrTaxNoUpdt"]
      """  ** NOT USED TO BE DROPPED 10.2 ** This flag determines whether any manual taxes were created for a header miscellaneous charge, if this is set to True then the tax engine will not calculate any miscellaneous charge tax information.  """  
      self.TaxRateGrpCode:str = obj["TaxRateGrpCode"]
      """  Tax Rate Group Code - FUTUREUSE  """  
      self.TaxesCalculated:bool = obj["TaxesCalculated"]
      """  The flag indicates that taxes have been calculated.  Once the flag is true is should never be changed back to false.  This will be set to true when any receipt line is marked as received, or when taxes have been calculated via the Calculate All Taxes menu option.  """  
      self.InAppliedLCAmt:int = obj["InAppliedLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount disbursed for this receipt.  """  
      self.InAppliedLCVariance:int = obj["InAppliedLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the applied variance amount for the landed costs.  """  
      self.InAppliedRcptLCAmt:int = obj["InAppliedRcptLCAmt"]
      """  Internal usage for inclusive taxes - The total Landed Cost Amount applied for this receipt.  """  
      self.InLandedCost:int = obj["InLandedCost"]
      """  Internal usage for inclusive taxes - Total amount of landed cost spread amongst the lines.  This amount includes all duties and indirect costs of all lines.  """  
      self.InLCDutyAmt:int = obj["InLCDutyAmt"]
      """  Internal usage for inclusive taxes - The total Duty Amount of the entire receipt.  """  
      self.InLCIndCost:int = obj["InLCIndCost"]
      """  Internal usage for inclusive taxes - The total Indirect Cost Amount of the entire receipt.  """  
      self.InLCUpliftIndCost:int = obj["InLCUpliftIndCost"]
      """  Internal usage for inclusive taxes - The total Uplift Indirect Cost Amount of the receipt. The total LandedCost is the sum of LCIndCost, LCDutyAmt, LCUpliftIndCost and SpecDutyAmt.  """  
      self.InLCVariance:int = obj["InLCVariance"]
      """  Internal usage for inclusive taxes - This field holds the variance amount for the landed costs.  """  
      self.InSpecDutyAmt:int = obj["InSpecDutyAmt"]
      """  Internal usage for inclusive taxes - This value overrides any tariffs on the duty lines.  The Specific Duty Amount is prorated among the receipt lines using the line tariffs as a factor.  """  
      self.CNDeclarationBill:str = obj["CNDeclarationBill"]
      """  Declaration Bill  """  
      self.CNBonded:bool = obj["CNBonded"]
      """  Bonded  """  
      self.APTaxRoundOption:int = obj["APTaxRoundOption"]
      """  APTaxRoundOption  """  
      self.AddrList:str = obj["AddrList"]
      """  Address Information from Vendor or VendorPP  """  
      self.PartialReceipt:bool = obj["PartialReceipt"]
      """  Logical indicating whether or not the receipt has been fully received.  If yes then the receipt has only been partially received.  """  
      self.POLine:int = obj["POLine"]
      self.PORel:int = obj["PORel"]
      self.POTypeDesc:str = obj["POTypeDesc"]
      self.ShipViaDesc:str = obj["ShipViaDesc"]
      self.TotalAmt:int = obj["TotalAmt"]
      """  Total amount.  This is the sum of all the other total fields.  """  
      self.TotDedTaxAmt:int = obj["TotDedTaxAmt"]
      """  Total dedicated Tax amount.  """  
      self.TotDutiesAmt:int = obj["TotDutiesAmt"]
      """  Total duties amount.  This is the sum of RcvHead.SpecDutyAmt + RcvHead.LCDutyAmt  """  
      self.TotGrossWeight:int = obj["TotGrossWeight"]
      """  Total Gross Weight of all receipt lines  """  
      self.TotGrossWeightUOM:str = obj["TotGrossWeightUOM"]
      """  Qualifies the unit of measure of the Gross Weight field.  """  
      self.TotIndirectCostsAmt:int = obj["TotIndirectCostsAmt"]
      """  Total Indirect Costs amount.  This is a sum of all RcvMisc.ActualAmt.  """  
      self.TotLinesAmt:int = obj["TotLinesAmt"]
      """  Total amount for all receipt lines.  This is the sum of RcvDtl.POTransValue.  """  
      self.TotSATaxAmt:int = obj["TotSATaxAmt"]
      """  Total Self Assessed Tax amount  """  
      self.TotTaxAmt:int = obj["TotTaxAmt"]
      """  Total tax amount.  This is the sum of RcvHeadTax.TaxAmt  """  
      self.TotWeight:int = obj["TotWeight"]
      """  Total Weight of all receipt lines  """  
      self.TotWeightUOM:str = obj["TotWeightUOM"]
      """  Qualifies the unit of measure of the Weight field.  """  
      self.TotWHTaxAmt:int = obj["TotWHTaxAmt"]
      """  Total WithHolding Tax amount  """  
      self.UpdateDtlArvdDate:bool = obj["UpdateDtlArvdDate"]
      """  Flag to indicate if receipt details need to be refreshed after changing the Arrival Date from header.  """  
      self.UpdateDtlRcptDate:bool = obj["UpdateDtlRcptDate"]
      """  Flag to indicate if receipt details need to be refreshed after changing the Receipt Date from header.  """  
      self.UpdateDtlRecs:bool = obj["UpdateDtlRecs"]
      """  Flag to indicate if details need to be refreshed after changing the UpliftPercent from header.  """  
      self.AllowLCUpdate:bool = obj["AllowLCUpdate"]
      """  Flag to indicate if record can be updated.  """  
      self.AllowUplift:bool = obj["AllowUplift"]
      """  Flag to indicate if UpliftPercent should be enabled.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.DispLandedCost:int = obj["DispLandedCost"]
      """  Display field used for container landed costs.  """  
      self.eshReceived:bool = obj["eshReceived"]
      """  Logical used to indicate if all details have been received.  """  
      self.IntQueID:int = obj["IntQueID"]
      self.LCMessage:str = obj["LCMessage"]
      """  Landed cost message used to inform the user on retrieval of data that the applied and landed costs do not equal.  """  
      self.LegalNumberMessage:str = obj["LegalNumberMessage"]
      self.OrigLandedCost:int = obj["OrigLandedCost"]
      """  This field is used to hold the original total landed cost for containers for all plants.  """  
      self.AddrListFormatted:str = obj["AddrListFormatted"]
      """  The formatted address Information from Vendor or VendorPP  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.vrPONumCNBonded:bool = obj["vrPONumCNBonded"]
      self.vrPONumShipToConName:str = obj["vrPONumShipToConName"]
      self.vrPONumShipName:str = obj["vrPONumShipName"]
      self.XbSystReceiptTaxCalculate:bool = obj["XbSystReceiptTaxCalculate"]
      self.XbSystAPTaxLnLevel:bool = obj["XbSystAPTaxLnLevel"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class GetRows_input:
   """ Required : 
   whereClause
   PONum
   POLine
   PORel
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  The criteria  """  
      self.PONum:int = obj["PONum"]
      """  PONum - Purchase Order Number  """  
      self.POLine:int = obj["POLine"]
      """  POLine - Line  """  
      self.PORel:int = obj["PORel"]
      """  PORel - Release  """  
      self.pageSize:int = obj["pageSize"]
      """  Size of a page  """  
      self.absolutePage:int = obj["absolutePage"]
      """  The absolute page  """  
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ICReceiptSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
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

class RcvHeadBeforeDelete_output:
   def __init__(self, obj):
      pass

class RcvHeadBeforeGetNew_output:
   def __init__(self, obj):
      pass

class RcvHeadBeforeUpdate_output:
   def __init__(self, obj):
      pass

