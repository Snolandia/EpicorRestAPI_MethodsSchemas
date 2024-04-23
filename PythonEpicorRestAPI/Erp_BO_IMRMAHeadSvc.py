import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.IMRMAHeadSvc
# Description: Business Object to handle: Add, Update, Delete of RMAHead
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMRMAHeadSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.IMRMAHeadSvc/$metadata",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_AddRMAHead(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AddRMAHead
   Description: Add RMAHead related tables
   OperationID: AddRMAHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AddRMAHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddRMAHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.IMRMAHeadSvc/$metadata", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################



#########################################################################
# Custom Schemas:
#########################################################################
class AddRMAHead_input:
   """ Required : 
   IMRMAHeadTableset
   company
   extSystemID
   transferMethod
   extCompanyID
   saveAddOnError
   imIntegrationKey
   """  
   def __init__(self, obj):
      self.IMRMAHeadTableset:list[Erp_Tablesets_IMRMAHeadTableset] = obj["IMRMAHeadTableset"]
      self.company:str = obj["company"]
      self.extSystemID:str = obj["extSystemID"]
      self.transferMethod:str = obj["transferMethod"]
      self.extCompanyID:str = obj["extCompanyID"]
      self.saveAddOnError:bool = obj["saveAddOnError"]
      self.imIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyTableset] = obj["imIntegrationKey"]
      pass

class AddRMAHead_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.errorsOccurred:bool = obj["errorsOccurred"]
      self.imIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyTableset] = obj["imIntegrationKey"]
      pass

      """  output parameters  """  

class Erp_Tablesets_IMIntegrationKeyRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      """  The master file which the integration is related to.  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record.  The value is a GUID.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMIntegrationKeyTableset:
   def __init__(self, obj):
      self.IMIntegrationKey:list[Erp_Tablesets_IMIntegrationKeyRow] = obj["IMIntegrationKey"]
      self.IMNaturalKeys:list[Erp_Tablesets_IMNaturalKeysRow] = obj["IMNaturalKeys"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMNaturalKeysRow:
   def __init__(self, obj):
      self.KeyValue:str = obj["KeyValue"]
      self.KeyColumn:str = obj["KeyColumn"]
      self.Sequence:int = obj["Sequence"]
      self.PrimaryKey:bool = obj["PrimaryKey"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMRMADtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number. Used to relate RMADtl to RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  An integer that uniquely identifies a detail record within a Return Authorization document. Assigned by the system. Generated by reading last related RMADtl record and use its RALine 1.  """  
      self.ReturnReasonCode:str = obj["ReturnReasonCode"]
      """  Reason code that links this return detail  to a Reason master record, which indicates why the item is being returned  and allows the system the ability to recap scrap by a code for analysis purposes. Uses Reason.ReasonType = "C" (customer returns) to find Reason master.  """  
      self.Note:str = obj["Note"]
      """   Notes the about the RMA detail.
Used to key in customer comments, explanation of why item is returned, inspection results, Order/Mfg instructions, and perhaps information concerning Billing.  """  
      self.PartNum:str = obj["PartNum"]
      """  The user's Internal Part number used to identify line item part. It cannot  be blank. It does NOT have to valid in the Part master.  Defaulted from the OrderDtl if available.  """  
      self.LineDesc:str = obj["LineDesc"]
      """  Line Item description. Defaults for OrderDtl if available, else from  Part master if available.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Optional field that contains the customers revision.  Default OrderDtl if available, else from finding the PartRev that is most current as of entry date.  """  
      self.ReturnQty:int = obj["ReturnQty"]
      """  Quantity that is to be returned  """  
      self.ReturnQtyUOM:str = obj["ReturnQtyUOM"]
      """  Unit Of Measure of the  ReturnQty.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The Ship to number of the related header contact.  """  
      self.ConNum:int = obj["ConNum"]
      """  The Contact Number of the related header contact  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number used to relate this record to the customer master.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier for transaction  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record. The value is  GUID.  """  
      self.CallCode:str = obj["CallCode"]
      """  Call Code  """  
      self.EmpID:str = obj["EmpID"]
      """  Employee ID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMRMAHeadRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  When creating a new Return Authorization the user is prompted for a Return number. If the field is zero , the next available # is assigned by the system. The system generates a number by finding the last CRAHead on file and uses its RANum + 1.  """  
      self.RMADate:str = obj["RMADate"]
      """  Date of the Return Material Authorization.  Default as System date.  """  
      self.CustNum:int = obj["CustNum"]
      """  Contains the system internal customer number used to relate this record to the customer master.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The Ship to number of the related header contact.  """  
      self.ConNum:int = obj["ConNum"]
      """  The Contact Number of the related header contact  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  Bill To Customer Number  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RMAComment:str = obj["RMAComment"]
      """  Comments about the RMA overall  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  EpicorFSA  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier for transaction  """  
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record. The value is  GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IMRMAHeadTableset:
   def __init__(self, obj):
      self.IntQueInOut:list[Erp_Tablesets_IntQueInOutRow] = obj["IntQueInOut"]
      self.IMRMADtl:list[Erp_Tablesets_IMRMADtlRow] = obj["IMRMADtl"]
      self.IMRMAHead:list[Erp_Tablesets_IMRMAHeadRow] = obj["IMRMAHead"]
      self.IMRMARcpt:list[Erp_Tablesets_IMRMARcptRow] = obj["IMRMARcpt"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_IMRMARcptRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RMANum:int = obj["RMANum"]
      """  Return Authorization Number of related RMAHead.  """  
      self.RMALine:int = obj["RMALine"]
      """  Line # of the related RMADtl record.  """  
      self.RMAReceipt:int = obj["RMAReceipt"]
      """  RMA Receipt  """  
      self.WareHouseCode:str = obj["WareHouseCode"]
      """  Warehouse ID the item was received into.  Normally this would be a "Inspection" type of warehouse.  """  
      self.BinNum:str = obj["BinNum"]
      """  Warehouse Bin location in which the received item was placed.  """  
      self.RcvDate:str = obj["RcvDate"]
      """  Receipt Date  """  
      self.LotNum:str = obj["LotNum"]
      """  Unique lot number for the part.  """  
      self.Plant:str = obj["Plant"]
      """  The Site that this RMA receipt was received to.  This is set as from the "Current Site" at the time of receipt.  It will be used in the filtering of receipts in the Disposition process.  """  
      self.ReceivedQty:int = obj["ReceivedQty"]
      """  Quantity that has been received.  """  
      self.ReceivedQtyUOM:str = obj["ReceivedQtyUOM"]
      """  Received Quantity unit of measure.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IntQueID:int = obj["IntQueID"]
      """  Unique identifier for transaction.  """  
      self.SerialNumber:str = obj["SerialNumber"]
      self.ExternalKey:str = obj["ExternalKey"]
      """  Unique identifier of related integration record. The value is  GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_IntQueInOutRow:
   def __init__(self, obj):
      self.IntQueID:int = obj["IntQueID"]
      """  The unique key from IntQueIn or IntQueOut  """  
      self.Action:str = obj["Action"]
      """  Action to perform - valid values are "Upd", "Add", "Del", & "Ack"  """  
      self.IncomingOutgoing:str = obj["IncomingOutgoing"]
      """  "I" for incoming or "O" for outgoing  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
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

